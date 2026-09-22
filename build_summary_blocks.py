#!/usr/bin/env python3
"""
build_summary_blocks.py -- NEEC Session 27: the 23 summary blocks, staged
=========================================================================
Decision D3(a): every scoring document carries one machine-readable summary
block (schema: summary_block.schema.json; validator: neec_entry.py). Decision
D14 (closed Session 27): the blocks are embedded in the documents in the same
pass that restates the seven earlier Step 1b documents, so that each document
is edited once. This script therefore STAGES the blocks in one file,
summary_blocks_s27.json, for review; it edits no document.

NOTHING IS RETYPED OR NEWLY JUDGED.
  * Vectors, domain totals, totals: the canonical corpus
    (neec_weighting_robustness_analysis_v2.py, imported unmodified).
    Failures and tier: neec_scores.csv. The validator recomputes both.
  * Flags of China, Singapore, Qatar, Islamic finance and Ostrom: their
    verifiers' flag registers (Python literals read by ast, never executed).
  * Flags of every other entry: the documents' own prose. Each such flag
    carries a verbatim phrase (whitespace and emphasis markers normalised)
    that this script asserts occurs in the flagged criterion's own section,
    or in the named document where the flag is stated outside it.
  * Joint readings stated in a document (D6: Islamic finance, Ostrom) and
    scenarios: the verifiers' literals, with every stated result asserted
    against the document's own sentence or table row.
  * Scope classes (D8): "stated" where a document declares the entry's
    archetype; otherwise "proposed" (decision D17, open).

Two encoding rules are applied where the documents predate the protocol
(decision D16, open; see SCORING_PROTOCOL.md 6.1 and 6.2):
  * a 0.5 flagged with evidence argued in both directions and no named
    alternative is encoded with both neighbours, [0.0, 1.0];
  * an entry that states no coherent joint readings gets the two extremes of
    its register (every call resolved up; every call resolved down), as the
    China, Singapore and Qatar verifiers already computed them.

Usage:  python3 build_summary_blocks.py      writes summary_blocks_s27.json, prints the log
Looks for inputs beside itself, then in the working directory. Deterministic.
"""
import ast
import csv
import hashlib
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "summary_blocks_s27.json"


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name} beside this script or in the working directory")


_spec = importlib.util.spec_from_file_location("neec_entry", locate("neec_entry.py"))
NE = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(NE)
CRITS, SCORES, KEYS = NE.CRITS, NE.SCORES, NE.KEYS

CODES = ["SQ", "NSD", "CPS", "MS", "LM", "MMT", "UBI", "DG", "SC", "FALC", "PE", "CCO", "INT",
         "GEO", "MC", "DE", "UBS", "SWF", "CN", "SG", "QA", "IF", "OS"]
if len(CODES) != len(KEYS):
    sys.exit("ERROR: code list and canonical corpus differ in length")
KEY = dict(zip(CODES, KEYS))

REPORT, STEP1C, PAPER = "NEEC_Report_v1_6.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md", "NEEC_Paper_v1_4.md"
DOC = {"GEO": "NEEC_Georgism_LVT_scoring_scratch.md", "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
       "DE": "NEEC_DoughnutEconomics_scoring_scratch.md", "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
       "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
       "CN": "NEEC_StateCapitalism_China_scoring_scratch.md", "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
       "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "IF": "NEEC_IslamicFinance_scoring_scratch.md",
       "OS": "NEEC_Ostrom_Commons_scoring_scratch.md"}
SESSION = {"GEO": 6, "MC": 7, "DE": 14, "UBS": 15, "SWF": 17, "CN": 18, "SG": 19, "QA": 21, "IF": 22, "OS": 23}
LEGACY = CODES[:13]

_TEXT = {}


def norm(s):
    s = re.sub(r"\\([\\`*_{}\[\]()#+\-.!<>=~|])", r"\1", s)
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def text(fn):
    if fn not in _TEXT:
        _TEXT[fn] = open(locate(fn), encoding="utf-8").read()
    return _TEXT[fn]


def section(fn, crit):
    """The criterion's own section: from its criterion heading to the next heading of level 1-4."""
    lines = text(fn).split("\n")
    head = re.compile(r"^#{2,5} " + re.escape(crit) + r"\b")
    hits = [i for i, l in enumerate(lines) if head.match(l)]
    if len(hits) != 1:
        sys.exit(f"ERROR: {fn}: expected one heading for {crit}, found {len(hits)}")
    i = hits[0]
    j = next((k for k in range(i + 1, len(lines)) if re.match(r"^#{1,4} ", lines[k])), len(lines))
    return "\n".join(lines[i:j])


ASSERTED = []


def assert_phrase(fn, locator, phrases):
    hay = norm(text(fn) if locator == "document" else section(fn, locator))
    for p in phrases:
        if norm(p) not in hay:
            sys.exit(f"ERROR: phrase not found in {fn} [{locator}]: {p!r}")
        ASSERTED.append((fn, locator, p))


def literal(fn, name):
    for node in ast.parse(text(fn)).body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            return ast.literal_eval(node.value)
    sys.exit(f"ERROR: {name} is not a literal assignment in {fn}")


# ------------------------------------------------------------------ scope (D8, D17)
ARCH1 = (DOC["OS"], "document", "Commons governance joins archetype 1, narrow single-mechanism systems, as its fifth "
         "member after Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism and Islamic finance.")
ARCH4 = (DOC["QA"], "document", "Qatar is the third instance of the fourth Step 1b archetype, \"configured national "
         "political economy\" (confirmed in Session 20), after China and Singapore.")
POP = {
    "QA": (DOC["QA"], "document", "Population scope: everyone who lives and works in Qatar, non-citizens included."),
    "SG": (DOC["SG"], "document", "This evaluation counts everyone who lives and works inside the system, "
           "non-residents included,"),
    "IF": (DOC["IF"], "document", "Score the mechanism, not a country."),
    "OS": (DOC["OS"], "document", "The convention applied throughout is generalisation, not best-casing: the mechanism "
           "is scored as though every common-pool resource in an economy were governed by an Ostrom-principled "
           "institution, and the population-scope thresholds are then applied to the resulting economy-wide"),
}
SCOPE = {c: ("mechanism", "stated", ARCH1) for c in ("GEO", "MC", "SWF", "IF", "OS")}
SCOPE.update({c: ("configured_national_economy", "stated", ARCH4) for c in ("CN", "SG", "QA")})
SCOPE.update({"UBS": ("mechanism", "proposed", None), "DE": ("comprehensive_system", "proposed", None)})
SCOPE.update({c: ("configured_national_economy", "proposed", None) for c in ("SQ", "NSD", "CPS")})
SCOPE.update({c: ("mechanism", "proposed", None) for c in ("MMT", "UBI")})
SCOPE.update({c: ("comprehensive_system", "proposed", None) for c in ("MS", "LM", "DG", "SC", "FALC", "PE", "CCO", "INT")})

# ------------------------------------------------------------------ flags stated in prose
# (criterion, alternatives, basis, reading, file, locator, phrases, tracks)
PROSE = {
    "CPS": [("C1.2b", [1.0], "stated", "the formal wealth Gini, with no private capital markets", STEP1C, "document",
             ["2.2 Centrally Planned Socialism's C1.2b", "The case for 1.0."], None)],
    "MMT": [("C1.2b", [0.5], "stated", "C4.4's reduction of capital power read as sufficient", STEP1C, "document",
             ["2.1 MMT + Job Guarantee's C1.2b", "override this call to 0.5"], None)],
    "INT": [("C2.2", [0.0, 1.0], "stated", "essentials unconditional (1.0) or contribution-dependent (0.0)", PAPER,
             "document", ["Unconditional Essentials (would score 1.0)", "Contribution-Dependent (would score 0.0)"], None)],
    "GEO": [("C4.3", [0.0, 1.0], "both-directions", None, DOC["GEO"], "C4.3",
             ["flagged as a genuinely contestable score", "a different reasoner could defensibly land elsewhere"], None)],
    "MC": [("C4.3", [0.0, 1.0], "both-directions", None, DOC["MC"], "C4.3",
            ["flagged as a genuinely contestable score", "a different reasoner could defensibly land elsewhere"], None),
           ("C5.2", [0.0], "direction-stated", "the staged design effort is untested at scale", DOC["MC"], "C5.2",
            ["flagged as more contestable toward 0.0"], None)],
    "DE": [("C1.2a", [0.5], "stated", "endorsing named accumulation vehicles read as commitment", DOC["DE"], "C1.2a",
            ["Flagged as contestable", "warrant the 0.5 band"], None),
           ("C1.2b", [0.5], "stated", "the 'harness the commons' language weighted more heavily", DOC["DE"], "C1.2b",
            ["Flagged as contestable", "could land at 0.5 instead"], None)],
    "UBS": [("C1.2b", [0.5], "stated", "the housing plank's pressure on land and rental values", DOC["UBS"], "C1.2b",
             ["could defensibly land at 0.5 instead"], None),
            ("C4.3", [1.0], "direction-stated", "the universalist equity evidence weighted more heavily", DOC["UBS"],
             "C4.3", ["flagged as a genuinely contestable score", "In favor of a stronger score:"], None),
            ("C5.1", [0.5], "stated", "the untested comprehensive integration emphasised", DOC["UBS"], "document",
             ["C5.1 (flagged as a confident but not unanimous 1.0", "could reasonably land at 0.5 instead"], None)],
    "SWF": [("C1.2a", [0.0], "stated", "only individually titled net worth counts", DOC["SWF"], "C1.2a",
             ["Flagged as contestable:", "would score this 0.0"], None),
            ("C1.5", [0.0], "stated", "follows C1.2a", DOC["SWF"], "C1.5",
             ["if C1.2a resolves to 0.0, this criterion follows to 0.0"], "C1.2a"),
            ("C4.3", [0.0, 1.0], "both-directions", None, DOC["SWF"], "C4.3",
             ["Flagged as contestable", "could reasonably land on a different score"], None),
            ("C5.4", [1.0], "stated", "the pre-existing anchor text read in isolation", DOC["SWF"], "C5.4",
             ["Flagged explicitly", "would point toward 1.0"], None)],
}

REGISTER = {  # code: (verifier, vector literal, flag literal)
    "CN": ("verify_china.py", "CHINA", "FLAGGED"), "SG": ("verify_singapore.py", "SG", "FLAGGED"),
    "QA": ("verify_qatar.py", "QA", "FLAGGED"), "IF": ("verify_islamicfinance.py", "SCORE", "FLAGGED"),
    "OS": ("verify_ostrom.py", "OSTROM", "FLAGS"),
}

# ------------------------------------------------------------------ stated joint readings (D6) and scenarios
IF_A, IF_C = literal("verify_islamicfinance.py", "READING_A"), literal("verify_islamicfinance.py", "READING_C")
OS_FLAGS = literal("verify_ostrom.py", "FLAGS")
OS_A = {c: a for c, a in OS_FLAGS.items() if a > SCORES[KEY["OS"]][c]}
OS_C = {c: a for c, a in OS_FLAGS.items() if a < SCORES[KEY["OS"]][c]}
STATED = {
    "IF": [("A", "as designed", IF_A, "15.5/26 (59.6%), 2 failures, Potentially Adequate."),
           ("B", "as practised, scored here", {}, "13.5/26 (51.9%), 5 structural failures, Partially Adequate."),
           ("C", "strict form-over-substance", IF_C, "10.5/26 (40.4%), 11 failures, Structurally Inadequate.")],
    "OS": [("A", "the long-enduring case (all eleven upward flags resolved up)", OS_A,
            "| A — the long-enduring case (all eleven upward flags resolved up) | 19.5/26 | 75.0 | 0 | Potentially Adequate |"),
           ("B", "as scored", {}, "| B — as scored | 14.0/26 | 53.8 | 4 | Partially Adequate |"),
           ("C", "strict population scope (all nine downward flags resolved down)", OS_C,
            "| C — strict population scope (all nine downward flags resolved down) | 9.5/26 | 36.5 | 11 | Structurally Inadequate |")],
}
SCENARIOS = {
    "QA": [("citizens-only", "citizens only; the scored scope counts every resident", "scope",
            literal("verify_qatar.py", "CITIZENS_ONLY"), "and gives 13.0/26 with 6 failures")],
    "SG": [("citizens-and-PRs-only", "citizens and permanent residents only; the scored scope counts every resident",
            "scope", literal("verify_singapore.py", "RESIDENT_ONLY"),
            "raises C1.5 to 1.0 and C4.5 to 0.5, giving 15.0/26 with 3 failures")],
    "IF": [("social-finance-layer", "the Islamic social-finance layer (zakat, waqf, takaful) counted in", "scope",
            literal("verify_islamicfinance.py", "BROAD_SCOPE"), "giving 14.5/26 (55.8%), 4 failures, Partially Adequate")],
    "OS": [("knowledge-commons", "the knowledge and digital commons counted in", "scope",
            literal("verify_ostrom.py", "SCENARIO"),
            "The result is 15.0/26 with 3 structural failures — still Partially Adequate")],
}


def numbers_agree(phrase, res):
    """The phrase's own total and failure count must equal the computed result."""
    t = re.search(r"(\d+\.\d)/26", phrase)
    f = re.search(r"(\d+) (?:structural )?failures|\| (\d+) \| (?:Potentially|Partially|Structurally)", phrase)
    fails = int(next(g for g in f.groups() if g)) if f else None
    return t and abs(float(t.group(1)) - res["total"]) < 1e-9 and fails == res["failures"]


# ------------------------------------------------------------------ assemble
rows = list(csv.DictReader(open(locate("neec_scores.csv"), encoding="utf-8", newline="")))
blocks = []
for code, row in zip(CODES, rows):
    key = KEY[code]
    v = {c: SCORES[key][c] for c in CRITS}
    pub = NE.CANON.PUBLISHED[key]
    summary = {f"D{i}": pub[f"D{i}"] for i in range(1, 6)}
    summary.update(total=pub["Total"], failures=int(row["failures"]), tier=row["adequacy_tier"])
    if code in LEGACY:
        docs = ([PAPER] if code == "INT" else []) + [REPORT, STEP1C]
        scored = ("NEEC v1 (" + ("Paper Appendix E" if code == "INT" else "Report Part I")
                  + "), legacy 25-criterion structure; retrofitted to v2 in Session 8 (Step 1c)")
        structure = "retrofit-step1c"
    else:
        docs = [DOC[code]]
        assert_phrase(DOC[code], "document", [f"Session {SESSION[code]}"])
        scored = f"Session {SESSION[code]}, natively on the v2 structure"
        structure = "native-v2"
    cls, basis, src = SCOPE[code]
    scope = {"class": cls, "basis": basis}
    if code in POP:
        fn, loc, ph = POP[code]
        assert_phrase(fn, loc, [ph])
        scope["population"] = norm(ph)
    if src:
        assert_phrase(src[0], src[1], [src[2]])
        scope["source"] = {"file": src[0], "locator": src[1], "phrase": norm(src[2])}
    flags = []
    if code in REGISTER:
        vf, vname, fname = REGISTER[code]
        if literal(vf, vname) != v:
            sys.exit(f"ERROR: {code}: {vf}:{vname} differs from the canonical vector")
        for c, alt in literal(vf, fname).items():
            a, note = (alt if isinstance(alt, tuple) else (alt, None))
            flags.append({"criterion": c, "scored": v[c], "alternatives": [a], "basis": "register",
                          "reading": note, "tracks": None, "source": {"file": vf, "locator": fname}})
    for (c, alts, fb, reading, fn, loc, phrases, tracks) in PROSE.get(code, []):
        assert_phrase(fn, loc, phrases)
        flags.append({"criterion": c, "scored": v[c], "alternatives": alts, "basis": fb, "reading": reading,
                      "tracks": tracks, "source": {"file": fn, "locator": loc, "phrase": norm(phrases[-1])}})
    flags.sort(key=lambda f: CRITS.index(f["criterion"]))
    b = {"schema": NE.SCHEMA_ID, "key": key, "code": code, "display_name": row["system"],
         "record": {"documents": docs, "scored": scored, "structure": structure},
         "scope": scope, "vector": v, "summary": summary, "flags": flags, "joint_readings": [], "scenarios": []}
    if code in STATED:
        for rid, label, ch, phrase in STATED[code]:
            res = NE.result(NE.applied(v, ch))
            assert_phrase(DOC[code], "document", [phrase])
            if not numbers_agree(phrase, res):
                sys.exit(f"ERROR: {code} reading {rid}: document states {phrase!r}, computed {res}")
            b["joint_readings"].append({"id": rid, "label": label, "basis": "scored" if not ch else "stated",
                                        "resolve": dict(sorted(ch.items(), key=lambda t: CRITS.index(t[0]))),
                                        "result": res})
    else:
        b["joint_readings"].append({"id": "scored", "label": "as scored", "basis": "scored", "resolve": {},
                                    "result": NE.result(v)})
        if flags:
            up, down = NE.extremes(b)
            for rid, label, ch in (("up", "every flagged call resolved upward", up),
                                   ("down", "every flagged call resolved downward", down)):
                b["joint_readings"].append({"id": rid, "label": label, "basis": "extremes",
                                            "resolve": dict(sorted(ch.items(), key=lambda t: CRITS.index(t[0]))),
                                            "result": NE.result(NE.applied(v, ch))})
    for sid, label, kind, ch, phrase in SCENARIOS.get(code, []):
        res = NE.result(NE.applied(v, ch))
        assert_phrase(DOC[code], "document", [phrase])
        if not numbers_agree(phrase, res):
            sys.exit(f"ERROR: {code} scenario {sid}: document states {phrase!r}, computed {res}")
        b["scenarios"].append({"id": sid, "label": label, "kind": kind,
                               "changes": dict(sorted(ch.items(), key=lambda t: CRITS.index(t[0]))), "result": res})
    blocks.append(b)

# ------------------------------------------------------------------ validate and write
bad = {b["code"]: NE.validate(b) for b in blocks}
bad = {k: e for k, e in bad.items() if e}
if bad:
    for k, errs in bad.items():
        print(f"INVALID {k}: " + "; ".join(errs))
    sys.exit(1)
body = "[\n" + ",\n".join("  " + NE.dump_block(b).replace("\n", "\n  ") for b in blocks) + "\n]\n"
with open(os.path.join(os.getcwd(), OUT), "w", encoding="utf-8") as fh:
    fh.write(body)

print("build_summary_blocks.py -- the 23 summary blocks, staged (D3(a); embedded with D14 in one later pass)")
print("=" * 92)
print(f"{len(ASSERTED)} verbatim phrases asserted in their documents; every block validates against neec_entry.py.")
print(f"  {'code':5} {'scope class':28} {'basis':9} {'flags':>5}  {'flag bases':34} {'readings':9} scenarios")
for b in blocks:
    fb = {}
    for f in b["flags"]:
        fb[f["basis"]] = fb.get(f["basis"], 0) + 1
    rb = sorted({r["basis"] for r in b["joint_readings"]} - {"scored"}) or ["-"]
    print(f"  {b['code']:5} {b['scope']['class']:28} {b['scope']['basis']:9} {len(b['flags']):5d}  "
          f"{', '.join(f'{k} {n}' for k, n in fb.items()) or '-':34} {'/'.join(rb):9} "
          f"{', '.join(x['id'] for x in b['scenarios']) or '-'}")
n_prop = sum(1 for b in blocks if b["scope"]["basis"] == "proposed")
n_both = sum(1 for b in blocks for f in b["flags"] if f["basis"] == "both-directions")
n_ext = sum(1 for b in blocks if any(r["basis"] == "extremes" for r in b["joint_readings"]))
print(f"\nOpen decisions this staging depends on:")
print(f"  D16: {n_both} flags encoded both-directions as [0.0, 1.0]; {n_ext} entries carry the extremes as their "
      f"joint readings.")
print(f"  D17: {n_prop} scope classes proposed rather than stated.")
sg = next(b for b in blocks if b["code"] == "SG")
alt = dict(sg, flags=[f for f in sg["flags"] if f["criterion"] != "C1.5"])
up, down = NE.extremes(alt)
alt["joint_readings"] = [sg["joint_readings"][0]] + [
    {"id": i, "label": i, "basis": "extremes", "resolve": ch, "result": NE.result(NE.applied(alt["vector"], ch))}
    for i, ch in (("up", up), ("down", down))]
for label, blk in (("as staged (C1.5 flagged)", sg), ("D18 variant (C1.5 scope call moved to the scenario)", alt)):
    m, en = NE.d13(blk), NE.enumerate_register(blk)
    print(f"  D18 preview, Singapore {label}: {len(blk['flags'])} flags, {en['combinations']:,} combinations, "
          f"keep tier {100 * en['keep_share']:.1f}%; readings reach {'/'.join(NE.TIER_ABBR[t] for t in m['reach'])}, "
          f"span {m['span_points']:.1f} / {m['span_failures']}")
print(f"\nWrote {OUT}: {len(blocks)} blocks, md5 {hashlib.md5(body.encode('utf-8')).hexdigest()[:8]}.")
