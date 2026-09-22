#!/usr/bin/env python3
"""
verify_doughnut.py -- Doughnut Economics: the entry arithmetic (reconstructed, Session 30)
=========================================================================================
RECONSTRUCTION. In Session 14 this entry's arithmetic was checked by an ad hoc script of this name
that was never added to the project files. This script is not that script. It was written in
Session 30, at the project owner's request, from the scoring document's Verification section, which
describes the two checks the Session 14 script made and records its output:
  (1) the five domain totals and the overall total are the literal arithmetic sum of the 26 discrete
      criterion scores (Appendix H.4; SCORING_PROTOCOL.md 2.4);
  (2) the failure count and the adequacy tier follow from those scores (protocol 2.5) and match what
      the document states in Summary Scores.
It repeats both on the vector as the document states it -- its 26 criterion headings, read here, never
retyped -- and reproduces the transcript recorded in the Verification section byte for byte. It adds
three checks the Session 14 script could not make, since the entry joined the canonical corpus only in
Session 16: the vector against the canonical SCORES (loaded from the unmodified canonical script, whose
own transcription self-check must pass), the domain totals, total, percent, failure count and tier
against the entry's row of neec_scores.csv, and the vector, summary and flagged criteria against the
document's summary block (which neec_entry.py also validates in full).

Usage:   python3 verify_doughnut.py
Inputs (beside this script, else the working directory): NEEC_DoughnutEconomics_scoring_scratch.md,
neec_weighting_robustness_analysis_v2.py, neec_scores.csv. Prints file names only; writes nothing;
deterministic. Exit status 0 only if every check passes.
"""
import contextlib
import csv
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = "NEEC_DoughnutEconomics_scoring_scratch.md"
CANON_FILE = "neec_weighting_robustness_analysis_v2.py"
CSV_FILE = "neec_scores.csv"
KEY = "Doughnut Economics"
DOMAIN_NAMES = ("Material Security", "Human Autonomy", "System Resilience", "Ethical Integrity",
                "Implementation Viability")
LABEL = {1.0: "Pass", 0.5: "Partial", 0.0: "Structural Failure"}
BEGIN, END = "<!-- NEEC-SUMMARY-BLOCK -->", "<!-- /NEEC-SUMMARY-BLOCK -->"
EPS = 1e-9


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name} beside this script or in the working directory")


def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()


def pct(x, of):
    """Whole percent, half up (protocol 2.4, decision D21)."""
    return int(100.0 * x / of + 0.5)


RESULTS = []


def check(group, label, cond, detail=""):
    RESULTS.append((group, label, bool(cond), detail))


# ------------------------------------------------------------------ inputs
RAW = open(locate(DOC), encoding="utf-8").read()
TEXT = norm(RAW)
spec = importlib.util.spec_from_file_location("_neec_canon", locate(CANON_FILE))
canon = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(canon)
    try:
        SELF_CHECK = canon.verify_transcription()
    except AssertionError:
        SELF_CHECK = False
CRITS = list(canon.ALL_CRITS)
DOMAINS = [[c for c in CRITS if c.startswith(f"C{d}.")] for d in range(1, 6)]
MAXES = [len(cs) for cs in DOMAINS]
ROWS = {r["system"]: r for r in csv.DictReader(open(locate(CSV_FILE), encoding="utf-8", newline=""))}

# ------------------------------------------------------------------ [1] the vector as the document states it
HEAD = re.compile(r"^#### (C[1-5]\.[1-6][ab]?) (.+?): (0\.0|0\.5|1\.0) \((Pass|Partial|Structural Failure)\)"
                  r"( — flagged as a contestable score)?$")
heads = [HEAD.match(line) for line in RAW.split("\n") if line.startswith("#### C")]
check(1, "every criterion heading has the form '#### <ID> <Name>: <score> (<label>)'",
      all(heads), f"{sum(1 for h in heads if not h)} heading(s) do not parse")
heads = [h for h in heads if h]
ids = [h.group(1) for h in heads]
check(1, "26 criterion headings, in the canonical order", ids == CRITS, f"found {ids}")
VEC = {h.group(1): float(h.group(3)) for h in heads}
check(1, "each heading's label is the one its score carries (1.0 Pass, 0.5 Partial, 0.0 Structural Failure)",
      all(LABEL[float(h.group(3))] == h.group(4) for h in heads))
FLAGGED = [h.group(1) for h in heads if h.group(5)]
if ids != CRITS:
    print("\n".join(f"FAIL [{g}] {lab}  {d}" for g, lab, ok, d in RESULTS if not ok))
    sys.exit(1)

# ------------------------------------------------------------------ [2] check (1): the arithmetic
dsum = [sum(VEC[c] for c in cs) for cs in DOMAINS]
tot = sum(VEC[c] for c in CRITS)
for i, name in enumerate(DOMAIN_NAMES):
    phrase = f"- {name}: {dsum[i]:.1f}/{MAXES[i]} ({pct(dsum[i], MAXES[i])}%)"
    check(2, f"Summary Scores states {name} as the sum of its {MAXES[i]} criteria: {dsum[i]:.1f}/{MAXES[i]}",
          phrase in RAW, f"not found: {phrase!r}")
check(2, f"Summary Scores states the overall score as the sum of the 26 criteria: {tot:.1f}/26 ({pct(tot, 26)}%)",
      f"**Overall Score: {tot:.1f}/26 ({pct(tot, 26)}%)**" in RAW)
explicit = "Explicit sum, per Appendix H.4: " + " + ".join(f"{d:.1f}" for d in dsum) + f" = {tot:.1f}."
check(2, "the explicit sum of the five domain totals is stated and correct", norm(explicit) in TEXT,
      f"not found: {explicit!r}")
check(2, "the five domain totals sum to the overall total", abs(sum(dsum) - tot) < EPS)

# ------------------------------------------------------------------ [3] check (2): failures and tier
fails = [c for c in CRITS if VEC[c] == 0.0]
tier = canon.tier(len(fails))
at = {v: [c for c in CRITS if VEC[c] == v] for v in (1.0, 0.5, 0.0)}
dist = (f"Score distribution: {len(at[1.0])} criteria at 1.0 ({', '.join(at[1.0])}), {len(at[0.5])} criteria at "
        f"0.5, {len(at[0.0])} criteria at 0.0 ({', '.join(at[0.0])}).")
check(3, "the score distribution (count and list at each value) is stated and correct", norm(dist) in TEXT,
      f"not found: {dist!r}")
m = re.search(r"\*\*Structural Failures: (\d+)\*\* \(([^)]*)\)", RAW)
listed = re.findall(r"\b(C[1-5]\.[1-6][ab]?)\b", m.group(2)) if m else []
check(3, f"Summary Scores states {len(fails)} structural failures and names exactly the criteria scored 0.0",
      m is not None and int(m.group(1)) == len(fails) and listed == fails, f"stated {m and m.group(1)}: {listed}")
check(3, f"the adequacy classification is the one {len(fails)} failures give: {tier}",
      f"**Adequacy Classification: {tier}** ({len(fails)} failures" in RAW)

# ------------------------------------------------------------------ [4] the recorded transcript
TRANSCRIPT = [f"{f'D{i + 1} ({name}):':<31}{dsum[i]:.1f}/{MAXES[i]}" for i, name in enumerate(DOMAIN_NAMES)]
TRANSCRIPT += [f"Total: {tot:.1f}/26 ({pct(tot, 26)}%)",
               f"Failures: {len(fails)} -- {fails}",
               f"Tier: {tier}",
               "",
               f"Cross-check: sum of five domain totals equals total: {abs(sum(dsum) - tot) < EPS}"]
vsec = RAW[RAW.index("\n## Verification\n"):] if "\n## Verification\n" in RAW else ""
mt = re.search(r"\n```\n(.*?)\n```\n", vsec, re.S)
recorded = mt.group(1).split("\n") if mt else []
check(4, "the Verification section records one transcript (a fenced block)", mt is not None)
check(4, "this script reproduces the recorded transcript byte for byte", recorded == TRANSCRIPT,
      f"{sum(1 for a, b in zip(recorded, TRANSCRIPT) if a != b)} line(s) differ; lengths {len(recorded)}, "
      f"{len(TRANSCRIPT)}")

# ------------------------------------------------------------------ [5] the canonical corpus (since Session 16)
check(5, f"{CANON_FILE}: its own transcription self-check passes", SELF_CHECK is not False)
check(5, f"the document's vector is the canonical SCORES['{KEY}'], criterion by criterion",
      KEY in canon.SCORES and all(abs(canon.SCORES[KEY][c] - VEC[c]) < EPS for c in CRITS),
      "differs at " + ", ".join(c for c in CRITS if KEY in canon.SCORES and abs(canon.SCORES[KEY][c] - VEC[c]) > EPS))
pub = canon.PUBLISHED.get(KEY, {})
check(5, "the canonical PUBLISHED totals are the document's",
      all(abs(pub.get(f"D{i + 1}", -1) - dsum[i]) < EPS for i in range(5)) and abs(pub.get("Total", -1) - tot) < EPS)
row = ROWS.get(KEY)
cols = ("domain1_material_security", "domain2_human_autonomy", "domain3_system_resilience",
        "domain4_ethical_integrity", "domain5_implementation_viability")
check(5, f"{CSV_FILE}: the row's domain totals, total, percent, failures and tier are the document's",
      row is not None and all(abs(float(row[c]) - dsum[i]) < EPS for i, c in enumerate(cols))
      and abs(float(row["total_score"]) - tot) < EPS and row["total_percent"] == f"{pct(tot, 26)}%"
      and int(row["failures"]) == len(fails) and row["adequacy_tier"] == tier)

# ------------------------------------------------------------------ [6] the summary block in the document
blocks = [json.loads(x) for x in re.findall(re.escape(BEGIN) + r"\s*```json\n(.*?)\n```\s*" + re.escape(END), RAW, re.S)]
b = blocks[0] if len(blocks) == 1 else {}
check(6, "the document carries exactly one summary block, for this entry", len(blocks) == 1 and b.get("key") == KEY)
check(6, "the block's vector is the vector of the criterion headings",
      isinstance(b.get("vector"), dict) and list(b["vector"]) == CRITS
      and all(abs(b["vector"][c] - VEC[c]) < EPS for c in CRITS))
s = b.get("summary", {})
check(6, "the block's summary is the arithmetic of that vector",
      all(abs(s.get(f"D{i + 1}", -1) - dsum[i]) < EPS for i in range(5)) and abs(s.get("total", -1) - tot) < EPS
      and s.get("failures") == len(fails) and s.get("tier") == tier)
check(6, "the block flags exactly the criteria whose headings are marked contestable",
      [f.get("criterion") for f in b.get("flags", [])] == FLAGGED, f"headings mark {FLAGGED}")

# ------------------------------------------------------------------ report
TITLES = {1: "THE VECTOR AS THE DOCUMENT STATES IT (ITS 26 CRITERION HEADINGS)",
          2: "SESSION 14 CHECK (1): DOMAIN TOTALS AND TOTAL ARE THE SUM OF THE CRITERIA",
          3: "SESSION 14 CHECK (2): FAILURE COUNT AND TIER",
          4: "THE TRANSCRIPT RECORDED IN THE VERIFICATION SECTION",
          5: "THE CANONICAL CORPUS (THE ENTRY JOINED IT IN SESSION 16)",
          6: "THE SUMMARY BLOCK IN THE DOCUMENT"}
print("=" * 96)
print("verify_doughnut.py -- Doughnut Economics: the entry arithmetic (reconstructed in Session 30)")
print("=" * 96)
print(f"document: {DOC}; canonical corpus: {CANON_FILE} ({len(canon.SCORES)} systems), {CSV_FILE}")
print(f"vector read from the document's criterion headings; flagged as contestable: {', '.join(FLAGGED) or 'none'}")
print("\nThe transcript, as this script reproduces it:\n")
for line in TRANSCRIPT:
    print(("    " + line).rstrip())
for g, title in TITLES.items():
    rows = [r for r in RESULTS if r[0] == g]
    print(f"\n[{g}] {title} ({len(rows)} checks)")
    for _g, label, ok, detail in rows:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok and detail:
            print(f"        {detail}")
npass = sum(1 for r in RESULTS if r[2])
print("\n" + "=" * 96)
print(f"SUMMARY: {npass} passed, {len(RESULTS) - npass} failed (of {len(RESULTS)}).")
print("=" * 96)
sys.exit(0 if npass == len(RESULTS) else 1)
