#!/usr/bin/env python3
"""
Independent verification of the State Capitalism / Singapore score vector
(Step 1b, Session 19) BEFORE it is spliced into any canonical file.
Mirrors verify_china.py (Session 18), per this project's methodology:
"Programmatic verification over visual checking" and "Dominance checks are
programmatic."

Five check groups:
  (1) Self-consistency: re-sum the 26-criterion vector against the scratch
      document's stated domain totals, total, distribution, failure count,
      and tier.
  (2) Transcription: parse NEEC_StateCapitalism_Singapore_scoring_scratch.md's
      own criterion headings (scores AND flag markers), domain-sum lines,
      overall-score line, failure line, distribution line, and sensitivity
      table, and confirm each matches this script -- so the vector is
      checked against the document rather than trusted as retyped.
  (3) Contestable-call sensitivity: every flagged call is re-scored alone
      and jointly. Because this evaluation's tier can move in BOTH
      directions, all 64 combinations of the six tier-relevant calls are
      enumerated and the stated rule is checked, not asserted. China's own
      flagged calls (AST-extracted from verify_china.py) go through the
      same joint test for the sibling comparison.
  (4) Population scope: the citizen-and-PR-only reading the document
      discloses is re-scored, alone and with every upward flag.
  (5) Corpus comparison: the REAL canonical SCORES dict is imported from the
      unmodified neec_weighting_robustness_analysis_v2.py (not retyped);
      the pending Sovereign Wealth Fund Statism and China vectors are
      extracted from verify_swf.py and verify_china.py by AST parsing (not
      retyped, not executed), giving the prospective 20-system corpus.
      Every comparative claim in the document's Final Assessment is checked.

PORTABILITY: like verify_china.py, this script looks beside itself first,
then in the conventional working locations, and prints only file names, so
its captured output reproduces byte-for-byte from any directory holding the
companion files (the canonical v2 script, verify_swf.py, verify_china.py,
and the scratch document).
"""

import ast
import importlib.util
import os
import re
import sys
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = (HERE, os.getcwd(), "/home/claude", "/home/claude/neec",
               "/mnt/user-data/outputs", "/mnt/project")
SCRATCH_DOC = "NEEC_StateCapitalism_Singapore_scoring_scratch.md"


def find(filename):
    for d in SEARCH_DIRS:
        p = os.path.join(d, filename)
        if os.path.isfile(p):
            return p
    return None


def locate(filename):
    p = find(filename)
    if p is None:
        sys.exit(f"ERROR: could not locate {filename} in {SEARCH_DIRS}")
    return p


def ast_literal(path, name):
    """Return the literal assigned to `name` in a Python file, without executing it."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(tg, "id", None) == name for tg in node.targets):
            return ast.literal_eval(node.value)
    return None


ALL_CRITS = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5'] + \
            [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
DOMAINS = {
    'D1': ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5'],
    'D2': [f'C2.{i}' for i in range(1, 6)],
    'D3': [f'C3.{i}' for i in range(1, 6)],
    'D4': [f'C4.{i}' for i in range(1, 6)],
    'D5': [f'C5.{i}' for i in range(1, 6)],
}
DOMAIN_MAX = {'D1': 6, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 5}
TIERS = ('Potentially Adequate', 'Partially Adequate', 'Structurally Inadequate')
CRIT_RE = r'C[1-5]\.[1-6][ab]?'

SG_NAME = 'State Capitalism / Singapore'
SWF_NAME = 'Sovereign Wealth Fund Statism'
CHINA_NAME = 'State Capitalism / China'
PENDING = ' [pending]'

SG = {
    'C1.1': 0.5, 'C1.2a': 1.0, 'C1.2b': 0.5, 'C1.3': 1.0, 'C1.4': 0.5, 'C1.5': 0.5,
    'C2.1': 0.5, 'C2.2': 0.0, 'C2.3': 0.5, 'C2.4': 0.5, 'C2.5': 0.5,
    'C3.1': 0.5, 'C3.2': 1.0, 'C3.3': 0.5, 'C3.4': 1.0, 'C3.5': 0.5,
    'C4.1': 0.5, 'C4.2': 0.0, 'C4.3': 0.5, 'C4.4': 0.0, 'C4.5': 0.0,
    'C5.1': 1.0, 'C5.2': 0.5, 'C5.3': 1.0, 'C5.4': 0.5, 'C5.5': 0.5,
}
PUBLISHED = {'D1': 4.0, 'D2': 2.0, 'D3': 3.5, 'D4': 1.0, 'D5': 3.5,
             'Total': 14.0, 'Percent': 54, 'Failures': 4, 'Tier': 'Partially Adequate'}
PASSES = {'C1.2a', 'C1.3', 'C3.2', 'C3.4', 'C5.1', 'C5.3'}

# Every contestable call flagged inline in the scratch document.
FLAGGED = {
    'C1.1':  (1.0, 'extreme-line / CPS-precedent reading'),
    'C1.2a': (0.5, 'lease-decay / illiquidity / excluded-fifth reading'),
    'C1.5':  (1.0, 'citizen-and-PR-only population scope'),
    'C2.1':  (0.0, 'permit regime plus political constraints as comparable coercion'),
    'C2.4':  (0.0, 'no alternation since 1959 as foreclosing participation'),
    'C3.2':  (0.5, 'headline-inflation stress-test reading (6.1% in 2022)'),
    'C3.4':  (0.5, 'slow social-protection reform / dominant-party governance'),
    'C3.5':  (0.0, 'POFMA and unmeasured poverty as active suppression'),
    'C4.2':  (0.5, 'carbon-price / Nordic-analogy reading'),
    'C4.3':  (0.0, 'literal reading of the H.7 0.0 anchor'),
    'C4.4':  (0.5, 'broad ownership plus elections as partial diffusion'),
    'C5.4':  (1.0, 'six decades of contested majorities as cross-spectrum support'),
}
UNCONTESTED_FAILURES = {'C2.2', 'C4.5'}
FLAGGED_FAILURES = {'C4.2', 'C4.4'}                        # 0.0 now, flagged upward
DOWNWARD_FAILURE_FLAGS = {'C2.1', 'C2.4', 'C3.5', 'C4.3'}  # 0.5 now, flagged to 0.0
TIER_RELEVANT = sorted(FLAGGED_FAILURES | DOWNWARD_FAILURE_FLAGS)
RESIDENT_ONLY = {'C1.5': 1.0, 'C4.5': 0.5}
STEP1B_KEYS = ('Georgism', 'Mutual Credit', 'Doughnut', 'Universal Basic Services')


def dsums(v):
    return {d: sum(v[c] for c in cs) for d, cs in DOMAINS.items()}


def total(v):
    return sum(v[c] for c in ALL_CRITS)


def fails(v):
    return [c for c in ALL_CRITS if v[c] == 0.0]


def tier(n):
    return ('Potentially Adequate' if n <= 2 else
            'Partially Adequate' if n <= 5 else 'Structurally Inadequate')


def dominates(a, b):
    return all(a[c] >= b[c] for c in ALL_CRITS) and any(a[c] > b[c] for c in ALL_CRITS)


def key_like(corpus, fragment):
    hits = [k for k in corpus if fragment in k]
    assert len(hits) == 1, f"expected one key containing {fragment!r}, got {hits}"
    return hits[0]


def moved(v, changes):
    out = dict(v)
    out.update(changes)
    return out


def describe(v):
    n = len(fails(v))
    return f"{total(v):.1f}/26, {n} failure{'' if n == 1 else 's'}, {tier(n)}"


RESULTS = []


def check(label, cond):
    RESULTS.append((label, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


print("=" * 90)
print("verify_singapore.py -- NEEC Step 1b, Session 19 (State Capitalism / Singapore)")
print("=" * 90)

# ---------------------------------------------------------------- (1)
print("\n(1) SELF-CONSISTENCY")
assert set(SG) == set(ALL_CRITS) and all(x in (0.0, 0.5, 1.0) for x in SG.values())
ds = dsums(SG)
for d, cs in DOMAINS.items():
    print(f"  {d} = {' + '.join(f'{SG[c]:.1f}' for c in cs)} = {ds[d]:.1f}/{DOMAIN_MAX[d]}")
    check(f"{d} equals stated {PUBLISHED[d]}", abs(ds[d] - PUBLISHED[d]) < 1e-9)
t, f = total(SG), fails(SG)
pct = round(t / 26 * 100)
print(f"  Total = {' + '.join(f'{ds[d]:.1f}' for d in DOMAINS)} = {t:.1f}/26 ({pct}%)")
check("Total equals stated 14.0/26 (54%)", abs(t - PUBLISHED['Total']) < 1e-9 and pct == PUBLISHED['Percent'])
check("Failure count equals stated 4", len(f) == PUBLISHED['Failures'])
check("Tier equals stated 'Partially Adequate'", tier(len(f)) == PUBLISHED['Tier'])
n1 = sum(SG[c] == 1.0 for c in ALL_CRITS)
nh = sum(SG[c] == 0.5 for c in ALL_CRITS)
print(f"  Distribution: {n1} at 1.0, {nh} at 0.5, {len(f)} at 0.0 -> {n1}(1.0) + {nh}(0.5) = {n1 + 0.5 * nh:.1f}")
check("Distribution (6 / 16 / 4) re-derives the total",
      (n1, nh, len(f)) == (6, 16, 4) and abs(n1 + 0.5 * nh - t) < 1e-9)
check("The six Passes are exactly C1.2a, C1.3, C3.2, C3.4, C5.1, C5.3",
      {c for c in ALL_CRITS if SG[c] == 1.0} == PASSES)
print(f"  Failures: {f}")
check("Failures = 2 undisputed (C2.2, C4.5) + 2 flagged (C4.2, C4.4)",
      set(f) == UNCONTESTED_FAILURES | FLAGGED_FAILURES)
check("Every flagged alternative differs from its primary score by exactly 0.5",
      all(abs(alt - SG[c]) == 0.5 for c, (alt, _) in FLAGGED.items()))
check("Flagged calls that would CREATE a failure are exactly C2.1, C2.4, C3.5, C4.3",
      {c for c, (alt, _) in FLAGGED.items() if alt == 0.0} == DOWNWARD_FAILURE_FLAGS)
check("Flagged calls that would REMOVE a failure are exactly C4.2, C4.4",
      {c for c in FLAGGED if SG[c] == 0.0} == FLAGGED_FAILURES)

# ---------------------------------------------------------------- (2)
print("\n(2) TRANSCRIPTION CHECK AGAINST THE SCRATCH DOCUMENT ITSELF")
doc_path = find(SCRATCH_DOC)
if doc_path is None:
    print(f"  SKIPPED: {SCRATCH_DOC} not found beside this script or in working dirs.")
else:
    text = open(doc_path, encoding="utf-8").read()
    heads = {}
    for m in re.finditer(r'^####\s+(' + CRIT_RE + r')\s([^\n]*)$', text, re.M):
        sm = re.search(r':\s*(0\.0|0\.5|1\.0)\s*\(', m.group(2))
        heads.setdefault(m.group(1), []).append(
            (float(sm.group(1)) if sm else None, 'flagged as contestable' in m.group(2)))
    dupes = {k: v for k, v in heads.items() if len(v) > 1}
    check("Document has exactly one scored heading per criterion (26, no duplicates)",
          set(heads) == set(ALL_CRITS) and not dupes
          and all(h[0][0] is not None for h in heads.values()))
    mism = [c for c in ALL_CRITS if c in heads and heads[c][0][0] != SG[c]]
    if mism:
        print(f"  Heading/vector mismatches: {[(c, heads[c][0][0], SG[c]) for c in mism]}")
    check("Every heading score matches this script's vector", not mism)
    flagged_in_doc = {c for c, h in heads.items() if h[0][1]}
    if flagged_in_doc != set(FLAGGED):
        print(f"  Flag mismatch: doc-only {sorted(flagged_in_doc - set(FLAGGED))}, "
              f"script-only {sorted(set(FLAGGED) - flagged_in_doc)}")
    check("Headings marked 'flagged as contestable' are exactly this script's 12 flagged calls",
          flagged_in_doc == set(FLAGGED) and len(FLAGGED) == 12)

    dom_re = re.compile(r'^\*\*Domain ([1-5]) = ([0-9. +]+?) = (\d\.\d)/(\d)', re.M)
    dom_found = {}
    for m in dom_re.finditer(text):
        addends = [float(x) for x in m.group(2).split('+')]
        dom_found[f"D{m.group(1)}"] = (sum(addends), float(m.group(3)), int(m.group(4)), addends)
    check("Document states all five domain-sum lines", set(dom_found) == set(DOMAINS))
    for d, (s, stated, mx, addends) in sorted(dom_found.items()):
        ok = (abs(s - stated) < 1e-9 and abs(stated - ds[d]) < 1e-9 and mx == DOMAIN_MAX[d]
              and addends == [SG[c] for c in DOMAINS[d]])
        check(f"{d} line: addends in criterion order re-sum to stated {stated}/{mx}", ok)

    om = re.search(r'\*\*Overall Score:\s*(\d+\.\d)/26\s*\((\d+)%\)', text)
    check("Document's Overall Score line states 14.0/26 (54%)",
          om is not None and float(om.group(1)) == t and int(om.group(2)) == pct)

    fm = re.search(r'\*\*Structural Failures:\*\*\s*(\d+)\s+criteria\s+at\s+0\.0\s+—\s+([^\n]+?)\.\s*$',
                   text, re.M)
    listed = set(re.findall(CRIT_RE, fm.group(2))) if fm else set()
    check("Document's failure line lists exactly the vector's 4 failures",
          fm is not None and int(fm.group(1)) == len(f) and listed == set(f))

    dm = re.search(r'Score distribution:\s*(\d+)\s+criteria\s+at\s+1\.0\s+\(([^)]*)\),\s+'
                   r'(\d+)\s+at\s+0\.5,\s+and\s+(\d+)\s+at\s+0\.0', text)
    check("Document's distribution line (6 / 16 / 4, Passes named) matches",
          dm is not None
          and (int(dm.group(1)), int(dm.group(3)), int(dm.group(4))) == (n1, nh, len(f))
          and set(re.findall(CRIT_RE, dm.group(2))) == PASSES)

    row_re = re.compile(r'^\|\s*(' + CRIT_RE + r')\s*\|\s*(\d\.\d)\s*\|\s*(\d\.\d)\s*—[^|]*\|'
                        r'\s*(\d+\.\d)\s*\|\s*(\d+)\s*\|\s*([A-Za-z ]+?)\s*\|\s*$', re.M)
    row_list = list(row_re.finditer(text))
    rows = {m.group(1): m for m in row_list}
    check("Sensitivity table has exactly one row per flagged call (12)",
          set(rows) == set(FLAGGED) and len(row_list) == len(FLAGGED))
    bad_rows = []
    for c, m in rows.items():
        v = moved(SG, {c: FLAGGED[c][0]})
        expected = (SG[c], FLAGGED[c][0], total(v), len(fails(v)), tier(len(fails(v))))
        got = (float(m.group(2)), float(m.group(3)), float(m.group(4)), int(m.group(5)), m.group(6))
        if expected != got:
            bad_rows.append((c, expected, got))
    if bad_rows:
        print(f"  Table mismatches: {bad_rows}")
    check("Every table row (primary, alternative, total, failures, tier) matches a fresh computation",
          rows and not bad_rows)

# ---------------------------------------------------------------- (3)
print("\n(3) CONTESTABLE-CALL SENSITIVITY")
print(f"  {'crit':6}{'primary':>8}{'alt':>6}{'total':>8}{'fails':>7}  {'tier':25} reading")
crossers = []
for c, (alt, label) in FLAGGED.items():
    v = moved(SG, {c: alt})
    nf = len(fails(v))
    if tier(nf) != PUBLISHED['Tier']:
        crossers.append(c)
    print(f"  {c:6}{SG[c]:>8.1f}{alt:>6.1f}{total(v):>8.1f}{nf:>7}  {tier(nf):25} {label}")
check("No single flagged call, resolved alone, changes the tier", not crossers)

up = moved(SG, {c: a for c, (a, _) in FLAGGED.items() if a > SG[c]})
down = moved(SG, {c: a for c, (a, _) in FLAGGED.items() if a < SG[c]})
print(f"\n  All upward readings together:   {describe(up)}")
print(f"  All downward readings together: {describe(down)}")
check("Joint upward reading = 16.5/26 with 2 failures (Potentially Adequate)",
      abs(total(up) - 16.5) < 1e-9 and len(fails(up)) == 2)
check("Joint downward reading = 10.5/26 with 8 failures (Structurally Inadequate)",
      abs(total(down) - 10.5) < 1e-9 and len(fails(down)) == 8)

pair_up = moved(SG, {'C4.2': 0.5, 'C4.4': 0.5})
print(f"  C4.2 and C4.4 both upward, nothing else moved: {describe(pair_up)}")
check("Both flagged failures upward alone = 15.0/26 with 2 failures (Potentially Adequate)",
      abs(total(pair_up) - 15.0) < 1e-9 and len(fails(pair_up)) == 2)
pair_results = []
for pair in combinations(sorted(DOWNWARD_FAILURE_FLAGS), 2):
    v = moved(SG, {c: 0.0 for c in pair})
    pair_results.append((pair, total(v), len(fails(v))))
    print(f"  {pair[0]} and {pair[1]} at 0.0: {describe(v)}")
check("Any two of C2.1 / C2.4 / C3.5 / C4.3 at 0.0 = 13.0/26 with 6 failures (Structurally Inadequate)",
      len(pair_results) == 6
      and all(abs(tt - 13.0) < 1e-9 and nf == 6 for _, tt, nf in pair_results))

rule_ok = True
counts = {name: 0 for name in TIERS}
for states in product((0.0, 0.5), repeat=len(TIER_RELEVANT)):
    v = moved(SG, dict(zip(TIER_RELEVANT, states)))
    j = sum(s == 0.0 for s in states)
    expected = ('Potentially Adequate' if j == 0 else
                'Partially Adequate' if j <= 3 else 'Structurally Inadequate')
    got = tier(len(fails(v)))
    counts[got] += 1
    if got != expected or len(fails(v)) != 2 + j:
        rule_ok = False
print(f"  Exhaustive check over {TIER_RELEVANT}: {2 ** len(TIER_RELEVANT)} combinations -> {counts}")
check("All 64 combinations: failures = 2 + j, and Partially Adequate exactly when 1 <= j <= 3 (primary j = 2)",
      rule_ok and sum(SG[c] == 0.0 for c in TIER_RELEVANT) == 2)
check("This evaluation's joint readings reach all three tiers",
      {tier(len(fails(up))), PUBLISHED['Tier'], tier(len(fails(down)))} == set(TIERS))

china_path = locate("verify_china.py")
CHINA = ast_literal(china_path, 'CHINA')
CHINA_FLAGGED = ast_literal(china_path, 'FLAGGED')
check("China vector and flagged calls extracted from verify_china.py (10.0/26, 8 failures, 9 flags)",
      CHINA is not None and CHINA_FLAGGED is not None
      and abs(total(CHINA) - 10.0) < 1e-9 and len(fails(CHINA)) == 8 and len(CHINA_FLAGGED) == 9)
c_up = moved(CHINA, {c: a for c, (a, _) in CHINA_FLAGGED.items() if a > CHINA[c]})
c_down = moved(CHINA, {c: a for c, (a, _) in CHINA_FLAGGED.items() if a < CHINA[c]})
china_tiers = {tier(len(fails(c_up))), tier(len(fails(CHINA))), tier(len(fails(c_down)))}
print(f"  China, for comparison -- joint upward: {describe(c_up)}; joint downward: {describe(c_down)}")
check("China's joint readings span two tiers (Partially Adequate, Structurally Inadequate)",
      china_tiers == {'Partially Adequate', 'Structurally Inadequate'})

# ---------------------------------------------------------------- (4)
print("\n(4) POPULATION-SCOPE SENSITIVITY (citizen-and-PR-only reading)")
scope = moved(SG, RESIDENT_ONLY)
changed = [c for c in ALL_CRITS if scope[c] != SG[c]]
print(f"  Criteria changed: {[(c, SG[c], scope[c]) for c in changed]}")
check("Scope reading changes exactly C1.5 (0.5 -> 1.0) and C4.5 (0.0 -> 0.5)",
      changed == ['C1.5', 'C4.5'] and scope['C1.5'] == 1.0 and scope['C4.5'] == 0.5)
print(f"  Scope reading alone: {describe(scope)}")
check("Scope reading alone = 15.0/26 with 3 failures (Partially Adequate)",
      abs(total(scope) - 15.0) < 1e-9 and len(fails(scope)) == 3
      and tier(3) == 'Partially Adequate')
scope_up = moved(up, RESIDENT_ONLY)
print(f"  Scope reading plus every upward flag: {describe(scope_up)}")
check("Scope reading plus every upward flag = 17.0/26 with 1 failure (Potentially Adequate)",
      abs(total(scope_up) - 17.0) < 1e-9 and len(fails(scope_up)) == 1)
check("C4.5 is disputed only by the scope reading, never by a flagged call",
      'C4.5' not in FLAGGED and scope['C4.5'] != SG['C4.5'])

# ---------------------------------------------------------------- (5)
print("\n(5) CORPUS COMPARISON (canonical SCORES imported; SWF and China AST-extracted)")
canon = locate("neec_weighting_robustness_analysis_v2.py")
spec = importlib.util.spec_from_file_location("neec_v2", canon)
neec_v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(neec_v2)
if hasattr(neec_v2, "verify_transcription"):
    neec_v2.verify_transcription(verbose=False)
SCORES = neec_v2.SCORES
print(f"  Loaded {len(SCORES)} canonical systems from {os.path.basename(canon)}")
check("Canonical corpus still holds exactly 17 systems", len(SCORES) == 17)
check("Singapore is not already in the canonical corpus", not any('Singapore' in k for k in SCORES))
SWF = ast_literal(locate("verify_swf.py"), 'SWF')
check("SWF vector extracted from verify_swf.py (14.0/26, 3 failures)",
      SWF is not None and abs(total(SWF) - 14.0) < 1e-9 and len(fails(SWF)) == 3)
corpus = dict(SCORES)
corpus[SWF_NAME + PENDING] = SWF
corpus[CHINA_NAME + PENDING] = CHINA
corpus[SG_NAME + PENDING] = SG
check("Prospective corpus holds 20 systems", len(corpus) == 20)

print("\n  -- Exact ties --")
canon_ties = sorted(n for n, s in SCORES.items() if abs(total(s) - t) < 1e-9)
print(f"  Canonical systems at exactly {t:.1f}/26: {canon_ties or 'none'}")
check("No canonical system scores exactly 14.0", not canon_ties)
check("Singapore ties the pending SWF Statism row exactly (14.0), and not China",
      abs(total(SWF) - t) < 1e-9 and abs(total(CHINA) - t) > 1e-9)
diff_swf = [c for c in ALL_CRITS if SWF[c] != SG[c]]
print(f"  vs SWF Statism: differs on {len(diff_swf)} criteria: "
      f"{[(c, SWF[c], SG[c]) for c in diff_swf]}  (SWF, Singapore)")
check("Singapore and SWF differ on exactly 7 criteria: C1.2a, C1.3, C2.2, C2.5, C3.2, C4.1, C4.4",
      diff_swf == ['C1.2a', 'C1.3', 'C2.2', 'C2.5', 'C3.2', 'C4.1', 'C4.4'])
check("Shared failures with SWF are exactly C4.2 and C4.5",
      set(f) & set(fails(SWF)) == {'C4.2', 'C4.5'})
check("Same tier, different failure counts (SWF 3, Singapore 4)",
      len(fails(SWF)) == 3 and tier(len(fails(SWF))) == tier(len(f)))
dswf = dsums(SWF)
deltas_swf = tuple(ds[d] - dswf[d] for d in DOMAINS)
print(f"  Domain deltas (Singapore minus SWF): {dict(zip(DOMAINS, deltas_swf))}")
check("Domain deltas vs SWF: D1 +1.5, D2 -1.0, D3 +0.5, D4 -1.0, D5 0.0",
      deltas_swf == (1.5, -1.0, 0.5, -1.0, 0.0))

print("\n  -- The state-capitalism sibling: China --")
higher = [c for c in ALL_CRITS if SG[c] > CHINA[c]]
dch = dsums(CHINA)
deltas_ch = tuple(ds[d] - dch[d] for d in DOMAINS)
print(f"  Singapore higher than China on {len(higher)}: {higher}; lower on "
      f"{[c for c in ALL_CRITS if SG[c] < CHINA[c]] or 'none'}")
print(f"  Domain deltas (Singapore minus China): {dict(zip(DOMAINS, deltas_ch))}")
check("Singapore strictly dominates China", dominates(SG, CHINA))
check("Higher than China on exactly 8 criteria: C1.2a, C1.3, C2.1, C2.4, C3.4, C3.5, C4.3, C5.3",
      higher == ['C1.2a', 'C1.3', 'C2.1', 'C2.4', 'C3.4', 'C3.5', 'C4.3', 'C5.3'])
check("Every domain higher than China: +1.0, +1.0, +1.0, +0.5, +0.5",
      deltas_ch == (1.0, 1.0, 1.0, 0.5, 0.5))
check("Singapore's 4 failures are a strict subset of China's 8", set(f) < set(fails(CHINA)))
check("The 4 China failures Singapore avoids are exactly its 4 downward-flagged calls",
      set(fails(CHINA)) - set(f) == DOWNWARD_FAILURE_FLAGS)

print("\n  -- Dominance against all 19 other systems --")
dom_by, dom_over = [], []
for n, s in corpus.items():
    if n.startswith(SG_NAME):
        continue
    if dominates(s, SG):
        dom_by.append(n)
        rel = "DOMINATES Singapore"
    elif dominates(SG, s):
        dom_over.append(n)
        rel = "is DOMINATED by Singapore"
    else:
        rel = "non-dominated pair"
    print(f"  {n:58} {rel}")
check("Singapore is dominated only by CCO-PTF-CIP-SZH", dom_by == ['CCO-PTF-CIP-SZH'])
check("Singapore strictly dominates only China", dom_over == [CHINA_NAME + PENDING])

print("\n  -- Ranking in the prospective 20-system corpus --")
order = list(corpus)
ranked = sorted(corpus.items(), key=lambda kv: (-total(kv[1]), order.index(kv[0])))
for i, (n, s) in enumerate(ranked, 1):
    tag = "   <==" if n.startswith(SG_NAME) else ""
    print(f"  {i:>2}. {n:58} {total(s):>5.1f}/26 ({round(total(s) / 26 * 100):>2}%)  "
          f"fails={len(fails(s)):>2}{tag}")
above = [n for n, s in corpus.items() if total(s) > t]
tied = [n for n, s in corpus.items() if abs(total(s) - t) < 1e-9 and not n.startswith(SG_NAME)]
below = [n for n, s in corpus.items() if total(s) < t]
print(f"  Strictly above: {len(above)}; tied with: {tied}; strictly below: {len(below)}")
check("Tied for 10th-11th of 20: 9 above, tied only with SWF Statism, 9 below",
      len(above) == 9 and tied == [SWF_NAME + PENDING] and len(below) == 9)

print("\n  -- Step 1b-cohort facts cited in the Final Assessment --")
cohort = {k: SCORES[key_like(SCORES, k)] for k in STEP1B_KEYS}
cohort[SWF_NAME] = SWF
cohort[CHINA_NAME] = CHINA
cohort[SG_NAME] = SG
for n, s in cohort.items():
    print(f"  {n:34} D1 {dsums(s)['D1']:.1f}/6   C1.2a {s['C1.2a']:.1f}   C1.3 {s['C1.3']:.1f}")
check("Singapore's Domain 1 (4.0) is the highest of the seven Step 1b systems",
      all(dsums(s)['D1'] < ds['D1'] for n, s in cohort.items() if n != SG_NAME))
check("Singapore is the first Step 1b system to score 1.0 on C1.2a, and on C1.3",
      [n for n, s in cohort.items() if s['C1.2a'] == 1.0] == [SG_NAME]
      and [n for n, s in cohort.items() if s['C1.3'] == 1.0] == [SG_NAME])

d4 = sorted((dsums(s)['D4'], n) for n, s in corpus.items())
print(f"  Lowest Domain 4 totals: {d4[:5]}")
at_half = {n for v, n in d4 if v == 0.5}
at_one = {n for v, n in d4 if v == 1.0}
check("Singapore's Domain 4 (1.0) ties Stakeholder Capitalism for third-lowest, above only China and Status Quo",
      not [n for v, n in d4 if v < 0.5]
      and at_half == {CHINA_NAME + PENDING, key_like(SCORES, 'Status Quo')}
      and at_one == {SG_NAME + PENDING, key_like(SCORES, 'Stakeholder')})
pct_by_domain = {d: ds[d] / DOMAIN_MAX[d] for d in DOMAINS}
check("Domain 4 is Singapore's weakest domain (by percentage)",
      min(pct_by_domain, key=pct_by_domain.get) == 'D4')

# ----------------------------------------------------------------------------
print("\n" + "=" * 90)
bad = [lbl for lbl, ok in RESULTS if not ok]
print(f"SUMMARY: {len(RESULTS) - len(bad)}/{len(RESULTS)} checks pass.")
if bad:
    for lbl in bad:
        print(f"  FAILED: {lbl}")
    sys.exit(1)
print("ALL CHECKS PASS. Nothing is inserted anywhere (scratch-before-insert discipline);")
print("this verifies the scratch document's arithmetic, its transcription, its disclosed")
print("two-directional sensitivity, its population-scope reading, and every comparative")
print("claim against the real canonical corpus.")
