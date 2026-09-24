#!/usr/bin/env python3
"""
build_criteria.py -- NEEC Session 27: criteria.json, generated from the Paper (corrected, Session 36)
=====================================================================================================
Part of the reproducibility kit (decision D3). Writes criteria.json: the 26
criteria of the NEEC v2 structure, in canonical order, each with its
definition and its 1.0 / 0.5 / 0.0 scoring anchors. Nothing is retyped:

  * definitions of the 23 unchanged criteria come from Paper Section 6;
  * definitions of C1.2a, C1.2b and C1.5 (narrowed) come from Section 12.3;
  * anchors of the 23 unchanged criteria come from Appendix H.7;
  * anchors of C1.2a, C1.2b and C1.5 (narrowed) come from Appendix H.7v2.
    (H.7's legacy C1.2 and C1.5 anchors describe the 25-criterion structure
    and are not carried.)

Two editorial rules are applied mechanically, and every application is printed:

  R1. Excluded fields. Section 6's "Threshold Justification" and "Current
      Performance" paragraphs are argument and dated evidence, not
      definition; they stay in the Paper and are not copied here.
  R2. Corpus-comparative clauses. An H.7 note whose opening clause makes a
      claim about the corpus ("NEEC's single most discriminating
      criterion", "the criterion most often failed ...") loses that clause;
      the guidance after the dash is kept. Comparative claims go stale when
      the corpus grows, so under D15 they belong to the corpus-level checker,
      not to a criterion definition. The removed clauses are printed below.

CORRECTIONS (Session 36, protocol v2.0-draft.5). After transcription, three
corrections are applied to the anchors. Each old text is asserted before it is
replaced, and every change is printed and recorded in the output's
source.corrections, so the record of what Paper v1.4 said stays in the pinned
Session 35 file (criteria_s35_snapshot.json, written by
build_criteria_s35_snapshot.py) and the record of what changed stays here:

  T. Thresholds (decision D28(g)). Every anchor's threshold line carries its
     definition's Pass Threshold verbatim, with a closing full stop. Where an
     H.7 threshold line differed, it is replaced; SUBSTANTIVE names the six
     that differed in substance and how, and the rest differed in wording only.
  B. C3.2's bands (decision D26, revision R3). The 0.0 band is reserved for an
     active inflationary mechanism with no counterbalancing element; the stale
     count "no system in the 13" goes with it (Correction 7, for this anchor);
     the 0.5 band gains the absence case that D26 scores 0.5.
  M. C1.5's threshold line (H.7v2) carried a sentence of band reasoning after
     the threshold. Under T it moves, unchanged, into the anchor's note, which
     was empty.

After the corrections the script asserts that all 26 anchor thresholds equal
their definitions.

ANCHOR CHECK. Every system an anchor cites as an example of its band is
looked up in the canonical corpus (neec_weighting_robustness_analysis_v2.py,
imported unmodified). A mismatch is either a KNOWN open correction, recorded
in the anchor itself so that no reader relies on it, or a failure. The run
exits 1 if any mismatch is not a known correction, or any known correction
no longer occurs.

Usage:  python3 build_criteria.py          check, write criteria.json, print the log
Looks for inputs beside itself, then in the working directory. Deterministic.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = "NEEC_Paper_v1_4.md"
CANON_FILE = "neec_weighting_robustness_analysis_v2.py"
OUT = "criteria.json"


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name} beside this script or in the working directory")


raw_bytes = open(locate(PAPER), "rb").read()
PAPER_MD5 = "5e2c2c3e9dc305c95ed7536db95ba1b8"   # Paper v1.4, pinned
got = hashlib.md5(raw_bytes).hexdigest()
if got != PAPER_MD5:
    sys.exit(f"ERROR: {PAPER} has MD5 {got}, expected {PAPER_MD5}; the extractor is written for Paper v1.4")
LINES = raw_bytes.decode("utf-8").split("\n")

spec = importlib.util.spec_from_file_location("_neec_canon", locate(CANON_FILE))
canon = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(canon)
CRITS = list(canon.ALL_CRITS)
SCORES = canon.SCORES

DOMAINS = [("D1", "Material Security"), ("D2", "Human Autonomy"), ("D3", "System Resilience"),
           ("D4", "Ethical Integrity"), ("D5", "Implementation Viability")]
V2_SPLIT = ("C1.2a", "C1.2b", "C1.5")
EXCLUDED_FIELDS = ("Threshold Justification", "Current Performance")

# Names under which the anchors cite the thirteen legacy systems (canonical key first).
ALIASES = {
    "Status Quo Market Capitalism": ("Status Quo Market Capitalism", "Status Quo Capitalism", "Status Quo"),
    "Nordic Social Democracy": ("Nordic Social Democracy",),
    "Centrally Planned Socialism": ("Centrally Planned Socialism",),
    "Market Socialism": ("Market Socialism",),
    "Libertarian Minarchism": ("Libertarian Minarchism",),
    "MMT + Job Guarantee": ("MMT + Job Guarantee", "MMT+Job Guarantee", "MMT+JG", "MMT + JG"),
    "Universal Basic Income": ("Universal Basic Income",),
    "Degrowth Economics": ("Degrowth Economics", "Degrowth"),
    "Stakeholder Capitalism": ("Stakeholder Capitalism",),
    "Fully Automated Luxury Communism": ("Fully Automated Luxury Communism", "FALC"),
    "Participatory Economics": ("Participatory Economics", "ParEcon"),
    "CCO-PTF-CIP-SZH": ("CCO-PTF-CIP-SZH", "CCO-PTF"),
    "Integral": ("Integral",),
}

# Open corrections: anchor examples whose cited band disagrees with the published score.
KNOWN_CORRECTIONS = {
    ("C4.3", "0.0", "Status Quo Market Capitalism"):
        "Open correction (Handoff 23, Correction 4): Status Quo Market Capitalism's published C4.3 score is "
        "0.5, not 0.0, so this example does not illustrate the 0.0 band. Do not use it as a 0.0 exemplar; "
        "the Appendix H.7 anchor is to be corrected in Paper v2.0.",
    ("C4.5", "1.0", "Participatory Economics"):
        "Open correction (found Session 27 by this check): the quoted rationale is Degrowth Economics' published "
        "C4.5 text (Report v1.6, System 8, scored 1.0), not Participatory Economics', whose published C4.5 score "
        "is 0.0 (a structural failure). Read this band's example as Degrowth Economics (1.0); the Appendix H.7 "
        "anchor is to be corrected in Paper v2.0.",
}


# ------------------------------------------------------------------ Session 36 corrections (see docstring)
THRESHOLD_BASIS = "decision D28(g): the anchor's threshold line is the definition's Pass Threshold, verbatim"
SUBSTANTIVE = {
    "C2.1": "dropped the revealed-preference elaboration (noted by the R4 audit, outside its four)",
    "C2.2": "dropped the population clause 'for all residents' and the list of basic needs, and added the "
            "Measurement line's conditions (found in Session 36)",
    "C2.5": "dropped 'voluntary association protected' (R4 audit)",
    "C3.1": "added 'no legislative delay' from the Measurement line and dropped the 1:1 example (R4 audit)",
    "C5.1": "dropped 'matching claimed benefits' (R4 audit)",
    "C5.3": "dropped 'through modeling' and 'coordination protocols established' (R4 audit)",
}
MOVED_SENTENCE = ("This band's reasoning is unchanged from legacy C1.5's anchors (H.7 above); narrowing the "
                  "threshold doesn't change which systems clear an access-breadth bar, only removes a second, "
                  "now-separate test that used to ride alongside it.")
BAND_BASIS = "decision D26 (revision R3); Correction 7's stale count removed from this anchor"
C32_00_OLD = ("No credible inflation-control mechanism is specified, or the system's design actively risks "
              "compounding inflation with no offset. This band is rare in the corpus (no system in the 13 scores "
              "0.0 here); reserve it for cases with an active inflationary mechanism and literally no "
              "counterbalancing design element, rather than merely \"unaddressed.\"")
C32_00_NEW = ("The system's design actively risks compounding inflation, with no counterbalancing design element. "
              "Reserve this band for an active inflationary mechanism: a system that specifies no "
              "inflation-control mechanism of its own, or has no monetary function, scores 0.5, not 0.0 "
              "(decision D26).")
C32_05_OLD = "or a proposed mechanism is theoretically plausible but unproven at scale."
C32_05_NEW = ("or a proposed mechanism is theoretically plausible but unproven at scale, or the system specifies no "
              "inflation-control mechanism of its own and has no active inflationary mechanism (decision D26).")


def closing(t):
    return t if t.endswith(".") else t + "."


def unescape(s):
    """Section 6 was exported with Markdown escapes (\\*, \\#, \\-, ...); remove them."""
    return re.sub(r"\\([\\`*_{}\[\]()#+\-.!<>=~|])", r"\1", s)


def block(start_pred, stop_pred, lo=0, hi=None):
    hi = len(LINES) if hi is None else hi
    i = next(k for k in range(lo, hi) if start_pred(LINES[k]))
    j = next((k for k in range(i + 1, hi) if stop_pred(LINES[k])), hi)
    return i, j


def fields(lines):
    """Paragraphs that open with **Label:** -> {label: text}, in order."""
    out = {}
    paras = "\n".join(lines).split("\n\n")
    for p in paras:
        p = " ".join(x.strip() for x in p.strip().split("\n"))
        m = re.match(r"^\*\*([^*]+?):\*\*\s*(.*)$", p)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def snake(label):
    return re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")


LOG = []
REMOVED = []

# ------------------------------------------------------------------ Section 6 (escaped)
s6_lo = next(i for i, l in enumerate(LINES) if unescape(l).startswith("## 6. NEEC Applied"))
s6_hi = next(i for i, l in enumerate(LINES) if unescape(l).startswith("## 7. "))
S6 = [unescape(l) for l in LINES[s6_lo:s6_hi]]
core_q, defs = {}, {}
dom = None
for k, l in enumerate(S6):
    m = re.match(r"^### DOMAIN ([1-5]): ", l)
    if m:
        dom = f"D{m.group(1)}"
        nxt = next(x for x in S6[k + 1:] if x.strip())
        core_q[dom] = re.sub(r"^\*\*Core Question:\*\*\s*", "", nxt).strip()
    m = re.match(r"^##### (C[1-5]\.[1-5]): (.+)$", l)
    if m:
        end = next((j for j in range(k + 1, len(S6)) if re.match(r"^#{2,5} ", S6[j])), len(S6))
        defs[m.group(1)] = dict(name=m.group(2).strip(), domain=dom, fields=fields(S6[k + 1:end]),
                                source="Paper Section 6")
LOG.append(f"Section 6: {len(defs)} legacy criterion definitions, {len(core_q)} domain core questions")

# ------------------------------------------------------------------ Section 12.3 (plain Markdown)
s12_lo = next(i for i, l in enumerate(LINES) if l.startswith("### 12.3 The v2 specification"))
s12_hi = next(i for i, l in enumerate(LINES) if l.startswith("### 12.4 "))
S12 = LINES[s12_lo:s12_hi]
n12 = 0
for k, l in enumerate(S12):
    m = re.match(r"^#### (C1\.2a|C1\.2b|C1\.5)(?: \(narrowed\))?: (.+)$", l)
    if m:
        end = next((j for j in range(k + 1, len(S12)) if S12[j].startswith("#### ")), len(S12))
        defs[m.group(1)] = dict(name=m.group(2).strip(), domain="D1", fields=fields(S12[k + 1:end]),
                                source="Paper Section 12.3")
        n12 += 1
defs.pop("C1.2", None)
LOG.append(f"Section 12.3: {n12} v2 definitions (C1.2a, C1.2b, C1.5 narrowed); legacy C1.2 dropped")

# ------------------------------------------------------------------ Appendix H.7 / H.7v2 anchors
h7_lo = next(i for i, l in enumerate(LINES) if l.startswith("### H.7 Criterion-by-criterion"))
h7v2_lo = next(i for i, l in enumerate(LINES) if l.startswith("### H.7v2 "))
h8_lo = next(i for i, l in enumerate(LINES) if l.startswith("### H.8 "))
HEAD = re.compile(r"^\*\*(C[1-5]\.[1-6][ab]?)(?: \(narrowed\))? — (.+?)\.\*\* \*Threshold: (.+?)\*(.*)$")
BAND = re.compile(r"^- \*\*(1\.0|0\.5|0\.0):\*\* (.*)$")
COMPARATIVE = re.compile(r"^(This is NEEC's (?:single )?most discriminating criterion \(Section 11\.2\)"
                         r"|NEEC's second most discriminating criterion \(Section 11\.2\)"
                         r"|This is the criterion most often failed by otherwise-strong systems in this corpus"
                         r" \([^)]*\)) — ")
anchors = {}


def parse_anchors(lo, hi, label, wanted):
    i = lo
    while i < hi:
        m = HEAD.match(LINES[i])
        if m and m.group(1) in wanted:
            cid, note = m.group(1), m.group(4).strip()
            rc = COMPARATIVE.match(note)
            if rc:
                REMOVED.append((cid, rc.group(1)))
                rest = note[rc.end():]
                note = rest[:1].upper() + rest[1:]
            bands = {}
            j = i + 1
            while j < hi and (BAND.match(LINES[j]) or not LINES[j].strip()) and len(bands) < 3:
                b = BAND.match(LINES[j])
                if b:
                    bands[b.group(1)] = b.group(2).strip()
                j += 1
            if sorted(bands) != ["0.0", "0.5", "1.0"]:
                sys.exit(f"ERROR: {label} {cid}: expected three bands, found {sorted(bands)}")
            anchors[cid] = dict(threshold=m.group(3).strip(), note=note, bands=bands, source=label)
            i = j
        else:
            i += 1


parse_anchors(h7_lo, h7v2_lo, "Paper Appendix H.7", [c for c in CRITS if c not in V2_SPLIT])
parse_anchors(h7v2_lo, h8_lo, "Paper Appendix H.7v2", list(V2_SPLIT))
LOG.append(f"Appendix H.7 / H.7v2: anchors for {len(anchors)} criteria")
missing = [c for c in CRITS if c not in defs or c not in anchors]
if missing or len(defs) != 26:
    sys.exit(f"ERROR: incomplete extraction; missing {missing}, definitions {len(defs)}")

# ------------------------------------------------------------------ Session 36 corrections (T, M, B)
CORRECTED, CLOG, CASE_ONLY = [], [], []
for cid in CRITS:
    a, want = anchors[cid], closing(defs[cid]["fields"]["Pass Threshold"])
    old = a["threshold"]
    if cid == "C1.5":                                    # M: the band reasoning moves to the note
        if not old.endswith(" " + MOVED_SENTENCE) or a["note"]:
            sys.exit("ERROR: C1.5's threshold line is not the H.7v2 text this correction was written for")
        old = old[:-len(MOVED_SENTENCE) - 1]
        a["note"] = MOVED_SENTENCE
        CORRECTED.append(dict(criterion=cid, field="anchors.note", kind="moved",
                              basis="decision D28(g): band reasoning formerly appended to the threshold line"))
    if old != want:                                      # T
        kind = "substantive" if cid in SUBSTANTIVE else "wording"
        rec = dict(criterion=cid, field="anchors.threshold", kind=kind, basis=THRESHOLD_BASIS)
        if cid in SUBSTANTIVE:
            rec["departure"] = SUBSTANTIVE[cid]
        CORRECTED.append(rec)
        if old[:1].lower() + old[1:] == want[:1].lower() + want[1:]:
            CASE_ONLY.append(cid)
        CLOG.append(f"T {cid} [{kind}]")
        CLOG.append(f"    was: {a['threshold']}")
        CLOG.append(f"    now: {want}")
        if cid in SUBSTANTIVE:
            CLOG.append(f"    departure: {SUBSTANTIVE[cid]}")
    elif cid in SUBSTANTIVE:
        sys.exit(f"ERROR: {cid} is listed as a substantive departure but its threshold already matches")
    a["threshold"] = want
missing_sub = [c for c in SUBSTANTIVE if not any(r["criterion"] == c and r["field"] == "anchors.threshold"
                                                  for r in CORRECTED)]
if missing_sub:
    sys.exit(f"ERROR: substantive departures not found: {missing_sub}")
b00, b05 = anchors["C3.2"]["bands"]["0.0"], anchors["C3.2"]["bands"]["0.5"]
if b00 != C32_00_OLD or b05.count(C32_05_OLD) != 1:     # B
    sys.exit("ERROR: C3.2's bands are not the H.7 text this correction was written for")
anchors["C3.2"]["bands"]["0.0"] = C32_00_NEW
anchors["C3.2"]["bands"]["0.5"] = b05.replace(C32_05_OLD, C32_05_NEW)
CORRECTED += [dict(criterion="C3.2", field="anchors.bands.0.0", kind="band", basis=BAND_BASIS),
              dict(criterion="C3.2", field="anchors.bands.0.5", kind="band", basis=BAND_BASIS)]
CLOG += ["M C1.5 note (was empty)", f"    now: {MOVED_SENTENCE}",
         "B C3.2 0.0", f"    was: {C32_00_OLD}", f"    now: {C32_00_NEW}",
         "B C3.2 0.5", f"    was: ...{C32_05_OLD}", f"    now: ...{C32_05_NEW}"]
unequal = [c for c in CRITS if anchors[c]["threshold"] != closing(defs[c]["fields"]["Pass Threshold"])]
if unequal:
    sys.exit(f"ERROR: anchor thresholds still differ from their definitions: {unequal}")

# ------------------------------------------------------------------ anchor examples
ALIAS_RE = sorted(((a, k) for k, al in ALIASES.items() for a in al), key=lambda t: -len(t[0]))


def examples(text, band):
    """Systems cited in a band's italic example text, with the score the anchor assigns them."""
    found, seen = [], set()
    for italic in re.findall(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", text):
        for alias, key in ALIAS_RE:
            for m in re.finditer(r"(?<![A-Za-z])" + re.escape(alias) + r"(?![A-Za-z])", italic):
                if key in seen:
                    continue
                # an explicit "(x.y)" right after the name is the cited score; otherwise the band value
                tail = italic[m.end():m.end() + 8]
                ex = re.match(r"\s*\((\d\.\d)\)", tail)
                cited = float(ex.group(1)) if ex else float(band)
                seen.add(key)
                found.append((key, cited, bool(ex)))
            # strip matched alias so shorter aliases ("Status Quo") do not re-match inside longer ones
            italic = re.sub(r"(?<![A-Za-z])" + re.escape(alias) + r"(?![A-Za-z])", " ", italic)
    return found


rows, unexpected, seen_known = [], [], set()
for cid in CRITS:
    for band in ("1.0", "0.5", "0.0"):
        for key, cited, explicit in examples(anchors[cid]["bands"][band], band):
            pub = SCORES[key][cid]
            ok = abs(pub - float(band)) < 1e-9 and abs(cited - float(band)) < 1e-9
            known = (cid, band, key) in KNOWN_CORRECTIONS
            if not ok:
                (seen_known.add((cid, band, key)) if known else unexpected.append((cid, band, key, cited, pub)))
            rows.append((cid, band, key, cited, explicit, pub, "ok" if ok else ("KNOWN" if known else "MISMATCH")))

# ------------------------------------------------------------------ assemble
FIELD_ORDER = ("Derivation", "Requirement", "Rationale", "Distinguishes", "Measurement", "Measurement Protocol",
               "Stress Test Scenarios", "Threshold Application", "Cultural/Geographic Adaptation", "Pass Threshold")
excluded_seen = {}
criteria = []
for cid in CRITS:
    d, a = defs[cid], anchors[cid]
    f = d["fields"]
    extra = [k for k in f if k not in FIELD_ORDER and k not in EXCLUDED_FIELDS]
    for k in f:
        if k in EXCLUDED_FIELDS:
            excluded_seen[k] = excluded_seen.get(k, 0) + 1
    definition = {snake(k): f[k] for k in FIELD_ORDER if k in f}
    definition.update({snake(k): f[k] for k in extra})
    if "requirement" not in definition or "pass_threshold" not in definition:
        sys.exit(f"ERROR: {cid}: definition lacks a Requirement or a Pass Threshold")
    bands = {}
    for band in ("1.0", "0.5", "0.0"):
        ex = [dict(system=k, cited=c) for k, c, _ in examples(a["bands"][band], band)]
        entry = dict(text=a["bands"][band], examples=ex)
        corr = [KNOWN_CORRECTIONS[(cid, band, e["system"])] for e in ex if (cid, band, e["system"]) in KNOWN_CORRECTIONS]
        if corr:
            entry["corrections"] = corr
        bands[band] = entry
    criteria.append(dict(
        id=cid, domain=d["domain"], name=d["name"],
        definition=definition,
        anchors=dict(threshold=a["threshold"], note=a["note"], bands=bands),
        sources=dict(definition=d["source"],
                     anchors=a["source"] + (" (0.0 and 0.5 bands corrected: " + BAND_BASIS + ")" if cid == "C3.2"
                                            else ""),
                     threshold=d["source"] + ", Pass Threshold, verbatim (decision D28(g))"),
    ))

doc = dict(
    schema="neec-criteria/1.0",
    framework="NEEC Applied, v2 structure: 26 criteria in five domains",
    generated_by="build_criteria.py (Session 27; corrections of Session 36, protocol v2.0-draft.5); do not edit by hand",
    source=dict(document=PAPER, md5=PAPER_MD5,
                excluded_fields=list(EXCLUDED_FIELDS),
                removed_comparative_clauses=[dict(criterion=c, clause=t) for c, t in REMOVED],
                corrections=CORRECTED),
    scale=dict(values=[0.0, 0.5, 1.0],
               labels={"1.0": "Pass", "0.5": "Partial / Conditional", "0.0": "Full Failure"},
               rule="Reason continuously, then round once, at the criterion level (Appendix H.3)."),
    structure=dict(criteria=26, total_max=26.0,
                   domain_max={dm: float(sum(1 for c in CRITS if c.startswith(f"C{dm[1]}."))) for dm, _ in DOMAINS}),
    tiers=[dict(name="Potentially Adequate", failures_min=0, failures_max=2),
           dict(name="Partially Adequate", failures_min=3, failures_max=5),
           dict(name="Structurally Inadequate", failures_min=6, failures_max=26)],
    domains=[dict(id=dm, name=nm, core_question=core_q[dm],
                  criteria=[c for c in CRITS if c.startswith(f"C{dm[1]}.")]) for dm, nm in DOMAINS],
    criteria=criteria,
)
text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"

# ------------------------------------------------------------------ report
print("build_criteria.py -- NEEC v2 criteria, generated from " + PAPER)
print("=" * 92)
print(f"Source: {PAPER} (md5 {PAPER_MD5[:8]}); corpus: {CANON_FILE} ({len(SCORES)} systems)")
for line in LOG:
    print("  " + line)
print(f"R1 excluded fields: " + ", ".join(f"{k} ({v} criteria)" for k, v in sorted(excluded_seen.items())))
nT = sum(1 for r in CORRECTED if r["field"] == "anchors.threshold")
print(f"Session 36 corrections (protocol v2.0-draft.5): {len(CORRECTED)} fields; {nT} threshold lines replaced "
      f"({sum(1 for r in CORRECTED if r['kind'] == 'substantive')} substantive, "
      f"{sum(1 for r in CORRECTED if r['kind'] == 'wording')} in wording only, {len(CASE_ONLY)} of those only in the "
      f"case of the first letter), 1 note, 2 bands")
for line in CLOG:
    print("  " + line)
print(f"  All 26 anchor thresholds now equal their definitions' Pass Thresholds ({THRESHOLD_BASIS}).")
print("R2 corpus-comparative clauses removed from H.7 notes:")
for c, t in REMOVED:
    print(f"  {c}: \"{t}\"")
print("Corpus-scoped statements retained verbatim inside band texts (true as scoped; review in Paper v2.0):")
for cid in CRITS:
    for band in ("1.0", "0.5", "0.0"):
        for sent in re.split(r"(?<=[.)])\s+", anchors[cid]["bands"][band]):
            if re.search(r"\bin the 13\b|\bthe 13\b|\bthis corpus\b|\bin the corpus\b", sent):
                print(f"  {cid} {band}: \"{sent.strip()[:150]}\"")
print("\nFailure counts per criterion on the current corpus (context for R2; not written to criteria.json):")
fc = {c: sum(1 for s in SCORES.values() if s[c] == 0.0) for c in CRITS}
for dm, _ in DOMAINS:
    print("  " + "  ".join(f"{c} {fc[c]:2d}" for c in CRITS if c.startswith(f"C{dm[1]}.")))
print("\nAnchor examples against the canonical corpus (band = the band the anchor cites them for):")
print(f"  {'crit':6} {'band':4}  {'system':34} {'cited':>5} {'published':>9}  status")
for cid, band, key, cited, explicit, pub, st in rows:
    print(f"  {cid:6} {band:4}  {key:34} {cited:5.1f}{'*' if explicit else ' '} {pub:9.1f}  {st}")
print("  (* = score stated explicitly beside the name; otherwise the band value)")
n_ok = sum(1 for r in rows if r[-1] == "ok")
print(f"\n{len(rows)} anchor examples: {n_ok} consistent, {len(seen_known)} known open correction(s), "
      f"{len(unexpected)} unexpected mismatch(es).")
stale_known = [k for k in KNOWN_CORRECTIONS if k not in seen_known]
for k in stale_known:
    print(f"FAIL: known correction {k} no longer occurs; remove it from KNOWN_CORRECTIONS")
for u in unexpected:
    print(f"FAIL: unexpected mismatch {u}")
if unexpected or stale_known:
    sys.exit(1)
with open(os.path.join(os.getcwd(), OUT), "w", encoding="utf-8") as fh:
    fh.write(text)
print(f"Wrote {OUT}: {len(criteria)} criteria, md5 {hashlib.md5(text.encode('utf-8')).hexdigest()[:8]}.")
