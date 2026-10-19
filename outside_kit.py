#!/usr/bin/env python3
"""
outside_kit.py -- NEEC: the outside blind review's kit (Session 80; decisions 79.6, 79.8, 80.x; ledger S63)
===========================================================================================================
The outside review (NEEC_OutsideReview_Plan_s79.md) has a reader from outside the Claude family read every one
of the 667 units blind, and Jev check each clause's status with the evidence held fixed. This script builds what
they are shown, the kit, and nothing else. The runner (outside_review_runner.py) assembles each prompt from the
kit alone; outside_kit_check.py builds every prompt the runner would send and fails on any leak.

WHAT THE READER SEES (plan, section 3; all of it under outside_kit/, every file named in manifest.json)
  prompt/instructions.md   the task, the output format and the rules of reading; names no system and no score.
  prompt/protocol.md       the protocol's scale and clause rule (2.1 to 2.3), the scope classes and how population
                           thresholds and reach are applied (3.1, 3.2), evidence by type of system and ambiguity
                           (4.1, 4.2), and anchors (4.6): any sentence or list item that names a scored system, a
                           record, a script or a session is dropped without a marker (R8, protocol 11.2).
  criteria/<cid>.md        the criterion's v2.0 definition, its Pass Threshold and clauses in order, and its anchor
                           bands with the worked examples removed (they cite scored systems with their v1 scores);
                           the same sentence rule as the protocol. No class, revision or source field.
  systems/<code>.md        the system's name, its scope class with the class's definition, and, for a configured
                           national economy or a mechanism with a stated boundary, its configuration.
  files/<id>.txt           the source packs' files: evidence_cache/<cid>/ screened (below), converted to text; and
                           passages of the design's own documents for the two designs with a full public text
                           (CCO-PTF-CIP-SZH: the Research Hub at 8e8a6ba and the simulation's v5.6 pages; Integral:
                           its white paper v0.1), chosen by one retrieval rule (BM25 against the criterion's text).
WHAT IT NEVER SEES: any score, verdict, clause status, reading, flag, close call, total, rank or tier; v1
  rationales; evidence/, docs/, STATE.md, handoffs, rescoring, blind or owner records; the cache's own notes
  (sources_s*.md, notes*.md, index.json, designs_index_s70.json); the author's name (redacted in the design's
  pages to "the author"); the name NEEC.

PACK RULE (decision 80.3). A cache file that quotes one design's own documents goes to that design's units only
(DESIGN_FILES); every other screened file of the criterion goes to every unit of the criterion. A unit with no
file and no design passage is closed-book: the reader answers from its own knowledge, and says so.

ORDER (plan, section 4; never in a prompt): group 1 the 29 CCO-PTF-CIP-SZH units; group 2 Participatory Economics,
  Integral, Nordic Social Democracy and Degrowth Economics (116); then CCO-PTF-CIP-SZH's 29 again (the consistency
  repeat, "#2"); group 3 every other unit with a close call in summary_blocks_v2.json (135); group 4 the rest (387).
  Stage B (not blind): the eight owner-decided units, after their blind reading is pushed (stage_b/).

Usage:
  python3 outside_kit.py --fetch HUB_DIR SIM_DIR   network and the two pinned clones: (re)write outside_kit_sources/
                                                   (the design texts; Integral's PDF through pdftotext, the
                                                   simulation's pages rendered by render_pages.js) and print md5s
  python3 outside_kit.py                           build outside_kit/ from the repository alone (stdlib only)
  python3 outside_kit.py --check                   rebuild in memory; fail on any difference from outside_kit/
Prints file names and counts, never data. Deterministic.
"""
import hashlib
import html
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HERE, "outside_kit")
SRC = os.path.join(HERE, "outside_kit_sources")
VERSION = "1.0"

HUB_PIN = "8e8a6ba"
SIM_PIN = "d10ed6e"
WP_URL = "https://integralcollective.io/documents/INTEGRAL-Paper-V0.1.pdf"
WP_MD5 = "a6defc9a0ec7c4ace56509dffd680307"   # the PDF as fetched in Session 80 (2026-10-19)

# The Research Hub's pages read as CCO-PTF-CIP-SZH's own documents: every page at the root and in wiki/, less the
# site's furniture and a page of jokes.
HUB_SKIP = {"404.html", "googlea418ef0496eb2fdc.html", "comedy.html", "comedy.md", "CONTRIBUTING.md",
            "README.md", "new-frame-and-lens.md", "research-summary.md"}
# The simulation's public pages at the v5.6 pin: two rendered by a browser (their figures are filled in by script),
# four read as written. replication.html is left out: it reports the NEEC maintainers' audit notes.
SIM_RENDERED = ["findings.html", "study.html"]
SIM_TEXT = ["README.md", "MODEL_SPEC.md", "ODD.md", "TESTBED_SPEC.md"]

TOP = ["PE", "INT", "NSD", "DG"]
STAGE_B = [("CCO", "C3.2"), ("CCO", "C1.2a"), ("CCO", "C2.5"), ("CCO", "C3.4"),
           ("INT", "C3.4"), ("PE", "C3.4"), ("DG", "C3.4"), ("OS", "C3.4")]

# A cache file quoting one design's own documents, by file-name prefix (decision 80.3).
DESIGN_FILES = [("integral_", "INT"), ("cco_", "CCO"), ("research_hub_", "CCO"), ("lp_platform", "LM"),
                ("pe_model", "PE"), ("hahnel_wright", "PE"), ("george_", "GEO"), ("levy_jg", "MMT"),
                ("bien_", "UBI"), ("ostrom_", "OS"), ("wef_metrics", "SC")]
# The cache's own notes and indexes, written by NEEC sessions: never in a pack.
CACHE_SKIP = re.compile(r"(^sources_s\d+\.md$|notes.*\.md$|^index\.json$)")

KIND = {
    "configured_national_economy": ("configured national economy", "An existing or historical national political "
        "economy, scored as configured at a stated date. Everyone who lives and works in the economy counts as its "
        "population, non-citizens included."),
    "mechanism": ("mechanism", "An institution, instrument or policy family that operates inside a wider economy "
        "without itself specifying that economy. It is scored as though it governed every part of an economy it "
        "could govern; a country's outcomes are credited to it only where the mechanism does the work."),
    "comprehensive_system": ("comprehensive system", "A design or vision for a whole economy, scored as its own "
        "sources specify it, for the population those sources claim to serve."),
}
CONFIG = {
    "SQ": "The United States' market economy as configured at the evaluation date (2026), read mainly from US "
          "data and informed by its record.",
    "NSD": "The Nordic social democracies (Denmark, Finland, Norway and Sweden) as configured at the evaluation "
           "date (2026), informed by their record.",
    "CPS": "The Soviet-type centrally planned economy, chiefly the USSR (1928 to 1991), read on its record.",
    "CN": "The People's Republic of China's post-1978 political economy as configured at the evaluation date "
          "(September 2026), informed by its full reform-era record.",
    "SG": "The Republic of Singapore's political economy as configured at the evaluation date (September 2026), "
          "informed by its record since independence in 1965.",
    "QA": "The State of Qatar's political economy as configured at the evaluation date (September 2026), informed "
          "by its longer record.",
    "SWF": "Sovereign wealth funds that return resource or investment income to the public, in two variants read "
           "together: general budget support (Norway's Government Pension Fund Global) and a direct dividend "
           "(Alaska's Permanent Fund and its dividend). Gulf-state and Singaporean funds are outside this entry.",
}

# Words that mark a scored system, a record, a script or a session: a protocol or criterion sentence holding one
# is dropped (R8: no marker). outside_kit_check.py tests the same list, and more, on every assembled prompt.
SYSTEM_WORDS = [r"Nordic", r"Status Quo", r"Socialis", r"Singapore", r"China", r"Chinese", r"Qatar", r"Integral",
                r"CCO", r"Georgis", r"Ostrom", r"Doughnut", r"Degrowth", r"\bUBI\b", r"Basic Income",
                r"Participatory", r"Parecon", r"\bMMT\b", r"Job Guarantee", r"Mutual Credit", r"\bLETS\b",
                r"Islamic", r"Sovereign Wealth", r"Libertarian", r"\bFALC\b", r"Luxury", r"Stakeholder",
                r"Basic Services", r"Compassion", r"\bITC\b", r"\bPTF\b"]
RECORD_WORDS = [r"NEEC", r"Session", r"Step 1b", r"Handoff", r"Paper v", r"Report v", r"\.py\b", r"\.md\b",
                r"\.json\b", r"\bD17\b", r"Appendix H", r"Correction", r"Adequate", r"Inadequate",
                r"Appendix A\b"]
DROP = re.compile("|".join(SYSTEM_WORDS + RECORD_WORDS))

PROTOCOL_SECTIONS = [("2.1", "2.4"), ("3.1", "3.3"), ("4.1", "4.3"), ("4.6", None)]


def md5(b):
    return hashlib.md5(b).hexdigest()


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


DROP_PARAS = ("**Assigned classes", "- Configured national economy: Status", "The closest calls", "Within each class",
              "Appendix H.2 calls", "Score against the criterion's", "`criteria.json` gives", "Two examples are wrong",
              "---")
LIST = re.compile(r"\s*([-*]|\d+\.) ")


def sentences_kept(text):
    """Drop every sentence or list item that names a scored system, a record, a script or a session, and the
    paragraphs in DROP_PARAS (R8: no marker). Headings and list structure are kept."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        b = block.strip()
        if b.startswith(DROP_PARAS):
            continue
        if b.startswith("#"):
            out.append(b)
            continue
        if LIST.match(b):
            items, cur = [], []
            for line in b.split("\n"):
                if LIST.match(line) and cur:
                    items.append("\n".join(cur)); cur = []
                cur.append(line)
            items.append("\n".join(cur))
            kept = [k for k in (keep_sentences(i) for i in items if not i.strip().startswith(DROP_PARAS)) if k]
            if kept:
                out.append("\n".join(kept))
            continue
        k = keep_sentences(b)
        if k:
            out.append(k)
    return "\n\n".join(out)


def keep_sentences(block):
    """The block on one line, less every sentence DROP matches; "" if nothing is left but a list marker."""
    flat = re.sub(r"\s*\n\s*", " ", block.strip())
    if not DROP.search(flat):
        return flat
    lead = LIST.match(flat)
    body = flat[lead.end():] if lead else flat
    kept = [p for p in re.split(r"(?<=[.;])\s+(?=[A-Za-z(*\"'])", body) if not DROP.search(p)]
    if not kept:
        return ""
    return (lead.group(0) if lead else "") + " ".join(kept)


def protocol_md(proto):
    out = ["# The scoring rules", "",
           "Excerpts of the evaluation's scoring protocol: the scale and the clause rule (2.1 to 2.3), scope (3.1, "
           "3.2), evidence (4.1, 4.2) and anchors (4.6). Sentences that refer to particular systems, earlier "
           "documents or internal procedures have been left out; no rule is changed. Section numbers are the "
           "protocol's own; cross-references to sections not included can be ignored."]
    for a, b in PROTOCOL_SECTIONS:
        i = proto.index("\n### " + a + " ")
        j = proto.index("\n### " + b + " ") if b else proto.index("\n## ", i + 5)
        out.append("")
        out.append(sentences_kept(proto[i:j].strip()))
    return "\n".join(out) + "\n"


def criterion_md(c):
    d, a = c["definition"], c["anchors"]
    L = ["# %s %s" % (c["id"], c["name"]), ""]
    order = ["requirement", "pass_threshold", "clause_scope", "measurement_protocol", "measurement", "indicators",
             "threshold_note", "distinguishes", "rationale", "disclosure", "benchmark", "comparison",
             "mechanisms_required", "stress_test_scenarios", "evidence_of_need", "examples_of_proven_components",
             "staged_transition_10_25_years_for_stable_contexts",
             "rapid_deployment_18_36_months_for_post_crisis_contexts", "historical_precedents",
             "cross_ideological_appeal_examples", "parameter_adjustment_examples_high_income_nations",
             "middle_income_nations", "low_income_nations", "cultural_variation_accommodated", "derivation"]
    assert set(d) - {"clauses"} <= set(order), sorted(set(d) - set(order))
    for k in order:
        if k in d:
            v = keep_sentences(d[k]) if isinstance(d[k], str) else None
            if v:
                L.append("**%s.** %s" % (k.replace("_", " ").capitalize(), v))
                L.append("")
    L.append("**Pass Threshold, clause by clause** (all must be shown cleared for 1.0; protocol 2.3):")
    L.append("")
    for n, cl in enumerate(d["clauses"], 1):
        L.append("%d. %s" % (n, cl))
    L.append("")
    if a.get("note") and keep_sentences(a["note"]):
        L.append("**Note.** " + keep_sentences(a["note"]))
        L.append("")
    L.append("**Anchor bands** (they describe; the Pass Threshold governs, protocol 4.6):")
    L.append("")
    for band in ("1.0", "0.5", "0.0"):
        t = re.sub(r"\*[^*]+\*", "", a["bands"][band]["text"])
        t = keep_sentences(re.sub(r"\s+", " ", t).strip())
        L.append("- **%s** %s" % (band, t))
    return "\n".join(L).rstrip() + "\n"


def system_md(e):
    kind, defn = KIND[e["scope_class"]]
    L = ["# %s" % e["display_name"], "", "**Kind:** %s. %s" % (kind, defn)]
    if e["code"] in CONFIG:
        L += ["", "**Configuration:** " + CONFIG[e["code"]]]
    return "\n".join(L) + "\n"


def html_text(s):
    s = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li|tr|section|article)>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n\n", s).strip()


def redact(t):
    """The author's name and address (plan, section 3: the reader never sees the owner's authorship)."""
    t = re.sub(r"(?i)duke\.?\s*t\.?\s*james\s*@\s*gmail\.com", "", t)
    t = re.sub(r"Duke\s*Johnson(?![a-z])", "the author", t)
    t = re.sub(r"\bDuke(?=['’]s\b)", "the author", t)
    t = re.sub(r"\bDuke\b", "the author", t)
    t = re.sub(r"\bJohnson\s*(&|and)\s*Claude\b", r"the author \1 Claude", t)
    t = re.sub(r"(Email|Corresponding Author)\s*:\s*(\(\s*\))?", r"\1:", t)
    return t


def cache_text(path):
    name = os.path.basename(path)
    if name.endswith(".pdf"):
        alt = os.path.join(SRC, "cache_pdf", os.path.relpath(path, os.path.join(HERE, "evidence_cache"))
                           .replace(os.sep, "__") + ".txt")
        return read(alt) if os.path.exists(alt) else None
    raw = read(path)
    if name.endswith(".json"):
        t = json.dumps(json.loads(raw), separators=(",", ":"), ensure_ascii=False)
    elif name.endswith(".html"):
        t = html_text(raw)
    else:
        t = raw
    # the cache's provenance lines name the NEEC session and script that cached them
    t = re.sub(r"\s*\(the commits? Sessions? [^)]*\)", "", t)
    t = re.sub(r";?\s*text by evidence_cache_s\d+\.\w+\(\)", "", t)
    return t.strip() + "\n"


def label_of(name):
    return re.sub(r"_s\d+(?=\.)", "", name)


# ---- design documents and retrieval -------------------------------------------------------------------------

def design_docs():
    """{code: [(title, text)]} from outside_kit_sources/ (manifest order)."""
    man = json.loads(read(os.path.join(SRC, "manifest.json")))
    out = {}
    for f in man["files"]:
        if f["design"]:
            out.setdefault(f["design"], []).append((f["title"], read(os.path.join(SRC, f["path"]))))
    return out


def passages(docs, size=1200):
    ps = []
    for title, text in docs:
        paras = [p.strip() for p in re.split(r"\n\s*\n|\n(?=[A-Z0-9#])", text) if p.strip()]
        cur = ""
        for p in paras:
            p = re.sub(r"\s+", " ", p)
            if cur and len(cur) + len(p) > size:
                ps.append((title, cur)); cur = ""
            cur = (cur + " " + p).strip()
            while len(cur) > 2 * size:
                ps.append((title, cur[:size])); cur = cur[size:]
        if cur:
            ps.append((title, cur))
    return ps


STOP = set("the and for that with this from are was were not but its has have had which their they them than "
           "into within under over any each all one two per such can may must also more most other only".split())


def toks(s):
    return [w for w in re.findall(r"[a-z][a-z0-9]{2,}", s.lower()) if w not in STOP]


def retrieve(ps, query, budget):
    """BM25 (k1 1.2, b 0.75) of each passage against the criterion's text; the best passages up to `budget`
    characters, returned in document order. Ties go to the earlier passage."""
    docs = [toks(p) for _, p in ps]
    N, avg = len(docs), sum(map(len, docs)) / max(1, len(docs))
    df = {}
    for d in docs:
        for w in set(d):
            df[w] = df.get(w, 0) + 1
    q = toks(query)
    scores = []
    for i, d in enumerate(docs):
        tf, s = {}, 0.0
        for w in d:
            tf[w] = tf.get(w, 0) + 1
        for w in set(q):
            if w in tf:
                idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * tf[w] * 2.2 / (tf[w] + 1.2 * (1 - 0.75 + 0.75 * len(d) / avg))
        scores.append((-round(s, 9), i))
    chosen, used = [], 0
    for s, i in sorted(scores):
        if s == 0:
            break
        if used + len(ps[i][1]) > budget:
            continue
        chosen.append(i); used += len(ps[i][1])
    return sorted(chosen)


def query_of(c):
    d = c["definition"]
    return " ".join([c["name"], d["requirement"], d["pass_threshold"], " ".join(d["clauses"]),
                     d.get("measurement_protocol", "") or d.get("measurement", ""), d.get("indicators", "")])


# ---- the kit --------------------------------------------------------------------------------------------------

INSTRUCTIONS = """# Your task

You are an independent reader for an evaluation of economic systems. The evaluation scores each system on 29
criteria, each on a three-value scale (1.0, 0.5, 0.0). You are given one unit: one system and one criterion. Read it
from the materials below, as the scoring rules direct, and give your own reading. No earlier reading of this unit is
given to you, and you should not try to recall one.

The materials are, in order: the scoring rules (excerpts of the protocol); the criterion; the system; and the source
pack, the documents and data you may rely on. Rely on the source pack first. Where it is empty, says the unit is
closed-book, or is silent on a clause, you may use your own knowledge of the system's literature and record; then
begin that clause's source with "closed-book:" and name what you rely on.

How to read:
1. For each clause of the Pass Threshold, in order, form your own estimate of the system's actual or credibly
   projected performance against that clause, grounded in the source pack (or, closed-book, your own knowledge), and
   name the source. Give the clause one status:
   - "cleared": the estimate shows the clause met;
   - "short": the estimate falls short of the clause;
   - "not_shown": the sources do not let the clause be estimated (silence is not clearance, protocol 2.3(b));
   - "moot": the clause's condition cannot apply to this system (protocol 2.3(e)).
2. The verdict follows the clause rule (protocol 2.3): 1.0 only if every clause is cleared or moot; otherwise 0.5,
   unless the 0.0 conditions of protocol 2.1 hold for the criterion as a whole, in which case 0.0 (and say which).
3. Reason first, at whatever length you need. Then end your answer with the line FINAL: followed by one JSON object,
   and nothing after it:

FINAL: {"clauses": [{"n": 1, "status": "cleared|short|not_shown|moot", "estimate": "...", "source": "..."}, ...],
"verdict": 1.0, "zero_basis": null, "closed_book": false, "confidence": 0.7, "note": "..."}

- "clauses" has exactly one entry per clause, numbered from 1 in the criterion's order.
- "verdict" is 1.0, 0.5 or 0.0; "zero_basis" is null unless the verdict is 0.0, when it names the 0.0 condition.
- "closed_book" is true if any clause rests on your own knowledge rather than the source pack.
- "confidence" (0 to 1) is how sure you are of the verdict; "note" is one or two sentences, or empty.
"""

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "outside reader FINAL object (one unit)",
    "type": "object",
    "required": ["clauses", "verdict", "zero_basis", "closed_book"],
    "properties": {
        "clauses": {"type": "array", "items": {
            "type": "object", "required": ["n", "status", "estimate", "source"],
            "properties": {"n": {"type": "integer", "minimum": 1},
                           "status": {"enum": ["cleared", "short", "not_shown", "moot"]},
                           "estimate": {"type": "string", "minLength": 1},
                           "source": {"type": "string", "minLength": 1}}}},
        "verdict": {"enum": [1.0, 0.5, 0.0]},
        "zero_basis": {"type": ["string", "null"]},
        "closed_book": {"type": "boolean"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "note": {"type": "string"}},
    "x-rules": ["len(clauses) equals the criterion's clause count, n = 1..k in order",
                "verdict 1.0 if and only if every status is cleared or moot (protocol 2.3)",
                "verdict 0.0 requires a non-empty zero_basis; any other verdict requires zero_basis null"],
}

# Stage B (plan, section 4.5; not blind, labelled so): the argument the owner made for each owner-decided unit,
# quoted from the decision records with their internal references removed.
STAGE_B_TEXT = {
    ("CCO", "C3.2"): "The backing of the currency by creative output is an original feature of the design and is "
        "read as backing what the Source pays. Keep the system at 1.0 until an empirical study shows that the "
        "backing does not hold up in real-world data.",
    ("CCO", "C1.2a"): "The backing of the currency by creative output is an original feature of the design and is "
        "read as backing what the Source pays. At full backing the design's model clears the bar in every seed "
        "(91.1% of participants at $60,000 or more), and the simulation's BLEI ladder agrees (76.2% Flourishing). "
        "The reading reopens toward 0.5 on an empirical study showing that the backing does not hold in real-world "
        "data.",
    ("CCO", "C2.5"): "Exit is leaving the system entirely: a member may stop taking Basic Units at any time, and no "
        "one is made to work. The early-exit haircut on Acre Equity is a stability provision on an asset a "
        "non-member never accrues, so a leaver is no worse off than one who never joined; moving within the "
        "network keeps the equity.",
    ("CCO", "C3.4"): "A collapse is a breakdown an adjustment causes (runaway prices, a run that fails), not the "
        "direct effect of a smaller allowance on hardship; on that reading no step of the design's adjustment run "
        "collapses at either backing. The test was fixed before the run; reading it afterwards as not counting "
        "the cut's direct effect is disclosed.",
}
RULE_794 = ("Where a system clears clauses 1 to 3 (the parameters adjust over 30% or more, updates follow evidence "
            "within six months, those affected can challenge and reverse them) and no implementation record or "
            "model located shows a collapse caused by an adjustment, clause 4 is cleared. The rule departs from "
            "'silence is not clearance' for this one clause.")
for _code in ("INT", "PE", "DG", "OS"):
    STAGE_B_TEXT[(_code, "C3.4")] = RULE_794


def build():
    """{relative path: bytes} for the whole kit."""
    crit = json.loads(read(os.path.join(HERE, "criteria.json")))["criteria"]
    corpus = json.loads(read(os.path.join(HERE, "neec_corpus_v2.json")))["entries"]
    blocks = json.loads(read(os.path.join(HERE, "summary_blocks_v2.json")))
    proto = read(os.path.join(HERE, "SCORING_PROTOCOL.md"))
    out = {}

    def put(path, text):
        out[path] = text.encode("utf-8")

    put("prompt/instructions.md", INSTRUCTIONS)
    put("prompt/protocol.md", protocol_md(proto))
    for c in crit:
        put("criteria/%s.md" % c["id"], criterion_md(c))
    for e in corpus:
        put("systems/%s.md" % e["code"], system_md(e))
    put("schema.json", json.dumps(SCHEMA, indent=1) + "\n")

    # the cache files, screened and converted once each
    cache = {}
    for c in crit:
        d = os.path.join(HERE, "evidence_cache", c["id"])
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if CACHE_SKIP.search(name):
                continue
            t = cache_text(os.path.join(d, name))
            fid = "%s__%s" % (c["id"], label_of(name))
            owner = next((code for pre, code in DESIGN_FILES if name.startswith(pre)), None)
            if t is None:
                cache.setdefault(c["id"], []).append((fid, owner, None))
                continue
            put("files/%s.txt" % fid, "SOURCE: %s (cached for %s)\n\n%s" % (label_of(name), c["id"], t))
            cache.setdefault(c["id"], []).append((fid, owner, t))

    docs = design_docs()
    ps = {code: passages(dl) for code, dl in docs.items()}
    codes = [e["code"] for e in corpus]
    close = {(b["code"], f["criterion"]) for b in blocks for f in b["flags"]}
    units = []
    for e in corpus:
        for c in crit:
            files = [fid for fid, owner, t in cache.get(c["id"], []) if t is not None and owner in (None, e["code"])]
            unread = [fid for fid, owner, t in cache.get(c["id"], []) if t is None and owner in (None, e["code"])]
            if e["code"] in ps:
                chosen = retrieve(ps[e["code"]], query_of(c), 40000)
                body = "\n\n".join("[%s] %s" % (ps[e["code"]][i][0], ps[e["code"]][i][1]) for i in chosen)
                fid = "design__%s__%s" % (e["code"], c["id"])
                put("files/%s.txt" % fid, "SOURCE: passages of the design's own documents most relevant to this "
                    "criterion (%d passages)\n\n%s\n" % (len(chosen), redact(body)))
                files.append(fid)
            mine = any(owner == e["code"] for _, owner, _ in cache.get(c["id"], [])) or e["code"] in ps
            mode = "sources" if mine or (e["scope_class"] != "comprehensive_system" and files) else "closed-book"
            if e["code"] == "CCO":
                g = 1
            elif e["code"] in TOP:
                g = 2
            elif (e["code"], c["id"]) in close:
                g = 3
            else:
                g = 4
            units.append({"unit": "%s|%s" % (e["code"], c["id"]), "code": e["code"], "cid": c["id"], "group": g,
                          "clauses": len(c["definition"]["clauses"]), "mode": mode, "files": files,
                          "unreadable": unread})
    order = sorted(units, key=lambda u: (u["group"], codes.index(u["code"]), [x["id"] for x in crit].index(u["cid"])))
    rep = [dict(u, unit=u["unit"] + "#2", group=2.5) for u in order if u["group"] == 1]
    order = [u for u in order if u["group"] <= 2] + rep + [u for u in order if u["group"] > 2]
    for i, u in enumerate(order, 1):
        u["order"] = i
    put("units.jsonl", "".join(json.dumps(u, sort_keys=True) + "\n" for u in order))
    for (code, cid), t in sorted(STAGE_B_TEXT.items()):
        put("stage_b/%s__%s.md" % (code, cid), "# The argument made for a different reading\n\n%s\n" % t)
    man = {"kit": "neec-outside-review", "version": VERSION, "units": len(units), "calls_planned": len(order),
           "files": {k: md5(v) for k, v in sorted(out.items())}}
    out["manifest.json"] = (json.dumps(man, indent=1, sort_keys=True) + "\n").encode("utf-8")
    return out


def write_kit(out):
    for k, v in out.items():
        p = os.path.join(KIT, k)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "wb") as f:
            f.write(v)
    have = {os.path.relpath(os.path.join(r, n), KIT) for r, _, ns in os.walk(KIT) for n in ns}
    for stale in sorted(have - set(out)):
        os.remove(os.path.join(KIT, stale))


def summary(out):
    units = [json.loads(l) for l in out["units.jsonl"].decode().splitlines()]
    from collections import Counter
    g = Counter(u["group"] for u in units)
    m = Counter(u["mode"] for u in units if not u["unit"].endswith("#2"))
    print("kit: %d files, %d bytes; manifest md5 %s" % (len(out), sum(map(len, out.values())),
                                                        md5(out["manifest.json"])))
    print("calls planned: %d (groups 1: %d, 2: %d, repeat: %d, 3: %d, 4: %d)" % (
        len(units), g[1], g[2], g[2.5], g[3], g[4]))
    print("units: %d (sources %d, closed-book %d); stage B units: %d" % (
        sum(m.values()), m["sources"], m["closed-book"], len(STAGE_B_TEXT)))


# ---- fetching the design texts (network; not in the harness) ---------------------------------------------------

def fetch(hub, sim):
    import urllib.request
    def git_head(d):
        return subprocess.run(["git", "-C", d, "rev-parse", "--short=7", "HEAD"], capture_output=True,
                              text=True).stdout.strip()
    assert git_head(hub) == HUB_PIN, "research-hub must be checked out at " + HUB_PIN
    assert git_head(sim) == SIM_PIN, "compassionism-simulation must be checked out at " + SIM_PIN
    os.makedirs(os.path.join(SRC, "cache_pdf"), exist_ok=True)
    files = []

    def save(rel, text, design, title, origin):
        with open(os.path.join(SRC, rel), "w", encoding="utf-8") as f:
            f.write(text)
        files.append({"path": rel, "design": design, "title": title, "origin": origin,
                      "md5": md5(text.encode("utf-8"))})

    pages = sorted(n for n in os.listdir(hub) if n.endswith((".html", ".md")) and n not in HUB_SKIP)
    pages += sorted("wiki/" + n for n in os.listdir(os.path.join(hub, "wiki")) if n.endswith(".html"))
    for n in pages:
        t = read(os.path.join(hub, n))
        t = redact(html_text(t) if n.endswith(".html") else t)
        save("cco_hub__%s.txt" % n.replace("/", "_").rsplit(".", 1)[0], t, "CCO", "Research Hub: " + n,
             "github.com/BetterToBest/research-hub@%s/%s" % (HUB_PIN, n))
    rendered = os.path.join(HERE, "outside_kit_sources", "rendered")
    for n in SIM_RENDERED:
        t = read(os.path.join(rendered, n + ".txt"))
        save("cco_sim__%s.txt" % n.rsplit(".", 1)[0], redact(t), "CCO", "Simulation v5.6: " + n,
             "github.com/BetterToBest/compassionism-simulation@%s/%s (rendered by render_pages.js)" % (SIM_PIN, n))
    for n in SIM_TEXT:
        save("cco_sim__%s.txt" % n.rsplit(".", 1)[0], redact(read(os.path.join(sim, n))), "CCO",
             "Simulation v5.6: " + n, "github.com/BetterToBest/compassionism-simulation@%s/%s" % (SIM_PIN, n))
    pdf = urllib.request.urlopen(WP_URL, timeout=120).read()
    assert md5(pdf) == WP_MD5, "Integral white paper changed: md5 %s" % md5(pdf)
    tmp = os.path.join(SRC, "integral.pdf")
    with open(tmp, "wb") as f:
        f.write(pdf)
    t = subprocess.run(["pdftotext", tmp, "-"], capture_output=True, text=True).stdout
    os.remove(tmp)
    t = re.sub(r"[ \t]+\n", "\n", t)
    save("integral_wp_v01.txt", t, "INT", "Integral white paper v0.1 (December 2025)", WP_URL)
    for d in sorted(os.listdir(os.path.join(HERE, "evidence_cache"))):
        dd = os.path.join(HERE, "evidence_cache", d)
        if not os.path.isdir(dd):
            continue
        for n in sorted(os.listdir(dd)):
            if n.endswith(".pdf"):
                t = subprocess.run(["pdftotext", "-layout", os.path.join(dd, n), "-"], capture_output=True,
                                   text=True).stdout
                if len(t.strip()) > 200:
                    rel = "cache_pdf/%s__%s.txt" % (d, n)
                    save(rel, t, None, "text layer of evidence_cache/%s/%s" % (d, n), "pdftotext -layout")
    man = {"about": "Design texts and PDF text layers for outside_kit.py, written by outside_kit.py --fetch",
           "pins": {"research-hub": HUB_PIN, "compassionism-simulation": SIM_PIN, "integral_wp_md5": WP_MD5},
           "files": files}
    with open(os.path.join(SRC, "manifest.json"), "w") as f:
        f.write(json.dumps(man, indent=1) + "\n")
    for x in files:
        print(x["md5"], x["path"])


def verify_sources():
    man = json.loads(read(os.path.join(SRC, "manifest.json")))
    bad = [f["path"] for f in man["files"] if md5(read(os.path.join(SRC, f["path"])).encode("utf-8")) != f["md5"]]
    return man, bad


def main(argv):
    if argv[:1] == ["--fetch"]:
        fetch(argv[1], argv[2])
        return 0
    man, bad = verify_sources()
    if bad:
        print("FAIL: outside_kit_sources/ differs from its manifest: %s" % ", ".join(bad))
        return 1
    print("outside_kit_sources/: %d files match their md5s (pins %s)" % (
        len(man["files"]), ", ".join("%s %s" % kv for kv in sorted(man["pins"].items()))))
    out = build()
    if argv[:1] == ["--check"]:
        have = {os.path.relpath(os.path.join(r, n), KIT): None for r, _, ns in os.walk(KIT) for n in ns}
        diff = sorted(k for k in set(have) | set(out)
                      if k not in out or k not in have or open(os.path.join(KIT, k), "rb").read() != out[k])
        summary(out)
        if diff:
            print("FAIL: outside_kit/ differs from what outside_kit.py builds: %d files (first: %s)" % (
                len(diff), diff[0]))
            return 1
        print("PASS: outside_kit/ is exactly what outside_kit.py builds from the repository")
        return 0
    write_kit(out)
    summary(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
