#!/usr/bin/env python3
"""
Independent verification of the State Capitalism / China score vector
(Step 1b, Session 18) BEFORE it is spliced into any canonical file.
Mirrors verify_swf.py (Session 17), per this project's methodology:
"Programmatic verification over visual checking" and "Dominance checks are
programmatic."

Four checks:
  (1) Self-consistency: re-sum the 26-criterion vector against the scratch
      document's stated domain totals, total, failure count, and tier.
  (2) Transcription: parse NEEC_StateCapitalism_China_scoring_scratch.md's
      own criterion headings, domain-sum lines, and overall-score line, and
      confirm they match the vector below -- so the vector is checked
      against the document rather than trusted as retyped.
  (3) Sensitivity: every contestable call the scratch document flags is
      re-scored individually and jointly; the exact consequence for total,
      failure count, and adequacy tier is printed -- checked, not asserted.
  (4) Corpus comparison: the REAL canonical SCORES dict is imported from the
      unmodified neec_weighting_robustness_analysis_v2.py (not retyped), and
      the pending Sovereign Wealth Fund Statism vector is extracted from
      verify_swf.py by AST parsing (not retyped, not executed), giving the
      prospective 19-system corpus. Every comparative claim in the scratch
      document's Final Assessment is checked here.

PORTABILITY (new this session): verify_swf.py and verify_ubs.py hard-code
/home/claude/ as the canonical script's location. This script looks beside
itself first, then in the conventional working locations, so it runs
unchanged from a cloned GitHub repository.
"""

import ast
import importlib.util
import os
import re
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = (HERE, os.getcwd(), "/home/claude", "/home/claude/neec",
               "/mnt/user-data/outputs", "/mnt/project")
SCRATCH_DOC = "NEEC_StateCapitalism_China_scoring_scratch.md"


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

CHINA_NAME = 'State Capitalism / China'
CHINA = {
    'C1.1': 0.5, 'C1.2a': 0.5, 'C1.2b': 0.5, 'C1.3': 0.5, 'C1.4': 0.5, 'C1.5': 0.5,
    'C2.1': 0.0, 'C2.2': 0.0, 'C2.3': 0.5, 'C2.4': 0.0, 'C2.5': 0.5,
    'C3.1': 0.5, 'C3.2': 1.0, 'C3.3': 0.5, 'C3.4': 0.5, 'C3.5': 0.0,
    'C4.1': 0.5, 'C4.2': 0.0, 'C4.3': 0.0, 'C4.4': 0.0, 'C4.5': 0.0,
    'C5.1': 1.0, 'C5.2': 0.5, 'C5.3': 0.5, 'C5.4': 0.5, 'C5.5': 0.5,
}
PUBLISHED = {'D1': 3.0, 'D2': 1.0, 'D3': 2.5, 'D4': 0.5, 'D5': 3.0,
             'Total': 10.0, 'Failures': 8, 'Tier': 'Structurally Inadequate'}

# Every contestable call flagged inline in the scratch document.
FLAGGED = {
    'C1.1':  (1.0, 'extreme-line / CPS-precedent reading'),
    'C1.2a': (1.0, 'middle-income-adjusted threshold reading'),
    'C2.3':  (0.0, 'CPS state-control-of-culture precedent'),
    'C3.2':  (0.5, 'symmetric price-stability (deflation) reading'),
    'C3.4':  (1.0, 'reform-era-only (1978-2012) reading'),
    'C3.5':  (0.5, 'CPS legible-dysfunction / central-correction reading'),
    'C4.2':  (0.5, 'emissions-plateau / Nordic-analogy reading'),
    'C4.3':  (0.5, 'preferential-policy-weighted reading'),
    'C5.4':  (0.0, 'structural-repulsion reading'),
}
UNCONTESTED_FAILURES = {'C2.1', 'C2.2', 'C2.4', 'C4.4', 'C4.5'}
FLAGGED_FAILURES = {'C3.5', 'C4.2', 'C4.3'}
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


RESULTS = []


def check(label, cond):
    RESULTS.append((label, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


print("=" * 90)
print("verify_china.py -- NEEC Step 1b, Session 18 (State Capitalism / China)")
print("=" * 90)

# ---------------------------------------------------------------- (1)
print("\n(1) SELF-CONSISTENCY")
assert set(CHINA) == set(ALL_CRITS) and all(x in (0.0, 0.5, 1.0) for x in CHINA.values())
ds = dsums(CHINA)
for d, cs in DOMAINS.items():
    print(f"  {d} = {' + '.join(f'{CHINA[c]:.1f}' for c in cs)} = {ds[d]:.1f}/{DOMAIN_MAX[d]}")
    check(f"{d} equals stated {PUBLISHED[d]}", abs(ds[d] - PUBLISHED[d]) < 1e-9)
t, f = total(CHINA), fails(CHINA)
print(f"  Total = {' + '.join(f'{ds[d]:.1f}' for d in DOMAINS)} = {t:.1f}/26 ({round(t / 26 * 100)}%)")
check("Total equals stated 10.0", abs(t - PUBLISHED['Total']) < 1e-9)
check("Failure count equals stated 8", len(f) == PUBLISHED['Failures'])
check("Tier equals stated 'Structurally Inadequate'", tier(len(f)) == PUBLISHED['Tier'])
n1 = sum(CHINA[c] == 1.0 for c in ALL_CRITS)
nh = sum(CHINA[c] == 0.5 for c in ALL_CRITS)
print(f"  Distribution: {n1} at 1.0, {nh} at 0.5, {len(f)} at 0.0 -> {n1}(1.0) + {nh}(0.5) = {n1 + 0.5 * nh:.1f}")
check("Distribution (2 / 16 / 8) re-derives the total",
      (n1, nh, len(f)) == (2, 16, 8) and abs(n1 + 0.5 * nh - t) < 1e-9)
print(f"  Failures: {f}")
check("Failures = 5 uncontested + 3 flagged", set(f) == UNCONTESTED_FAILURES | FLAGGED_FAILURES)

# ---------------------------------------------------------------- (2)
print("\n(2) TRANSCRIPTION CHECK AGAINST THE SCRATCH DOCUMENT ITSELF")
doc_path = find(SCRATCH_DOC)
if doc_path is None:
    print(f"  SKIPPED: {SCRATCH_DOC} not found beside this script or in working dirs.")
else:
    text = open(doc_path, encoding="utf-8").read()
    head_re = re.compile(r'^####\s+(C[1-5]\.[1-6][ab]?)\s[^\n]*?:\s*(0\.0|0\.5|1\.0)\s*\(', re.M)
    parsed = {}
    for m in head_re.finditer(text):
        parsed.setdefault(m.group(1), []).append(float(m.group(2)))
    dupes = {k: v for k, v in parsed.items() if len(v) > 1}
    check("Document has exactly one scored heading per criterion (26, no duplicates)",
          set(parsed) == set(ALL_CRITS) and not dupes)
    mism = [c for c in ALL_CRITS if c in parsed and parsed[c][0] != CHINA[c]]
    if mism:
        print(f"  Heading/vector mismatches: {[(c, parsed[c][0], CHINA[c]) for c in mism]}")
    check("Every heading score matches this script's vector", not mism)
    dom_re = re.compile(r'^\*\*Domain ([1-5]) = ([0-9. +]+?) = (\d\.\d)/(\d)', re.M)
    dom_found = {}
    for m in dom_re.finditer(text):
        addends = [float(x) for x in m.group(2).split('+')]
        dom_found[f"D{m.group(1)}"] = (sum(addends), float(m.group(3)), int(m.group(4)), addends)
    check("Document states all five domain-sum lines", set(dom_found) == set(DOMAINS))
    for d, (s, stated, mx, addends) in sorted(dom_found.items()):
        ok = (abs(s - stated) < 1e-9 and abs(stated - ds[d]) < 1e-9 and mx == DOMAIN_MAX[d]
              and addends == [CHINA[c] for c in DOMAINS[d]])
        check(f"{d} line: addends in criterion order re-sum to stated {stated}/{mx}", ok)
    om = re.search(r'\*\*Overall Score:\s*(\d+\.\d)/26\s*\((\d+)%\)', text)
    check("Document's Overall Score line states 10.0/26 (38%)",
          om is not None and float(om.group(1)) == t and int(om.group(2)) == round(t / 26 * 100))

# ---------------------------------------------------------------- (3)
print("\n(3) CONTESTABLE-CALL SENSITIVITY")
print(f"  {'crit':6}{'primary':>8}{'alt':>6}{'total':>8}{'fails':>7}  {'tier':25} reading")
crossers = []
for c, (alt, label) in FLAGGED.items():
    v = dict(CHINA); v[c] = alt
    tt, nf = total(v), len(fails(v))
    if tier(nf) != PUBLISHED['Tier']:
        crossers.append(c)
    print(f"  {c:6}{CHINA[c]:>8.1f}{alt:>6.1f}{tt:>8.1f}{nf:>7}  {tier(nf):25} {label}")
check("No single flagged call, resolved alone, changes the tier", not crossers)
v = dict(CHINA); v['C4.3'] = 1.0
print(f"  C4.3 at the CPS precedent's own 1.0: total {total(v):.1f}, {len(fails(v))} failures, {tier(len(fails(v)))}")
check("C4.3 at the CPS precedent's 1.0, alone, does not change the tier",
      tier(len(fails(v))) == PUBLISHED['Tier'] and abs(total(v) - 11.0) < 1e-9)

up, down = dict(CHINA), dict(CHINA)
for c, (alt, _) in FLAGGED.items():
    (up if alt > CHINA[c] else down)[c] = alt
up_cps = dict(up); up_cps['C4.3'] = 1.0
print(f"\n  All upward readings together:   {total(up):.1f}/26, {len(fails(up))} failures, {tier(len(fails(up)))}")
print(f"  All downward readings together: {total(down):.1f}/26, {len(fails(down))} failures, {tier(len(fails(down)))}")
print(f"  Upward, with C4.3 at 1.0:       {total(up_cps):.1f}/26, {len(fails(up_cps))} failures, {tier(len(fails(up_cps)))}")
check("Joint upward reading = 13.0/26 with 5 failures (Partially Adequate) -- disclosed",
      abs(total(up) - 13.0) < 1e-9 and len(fails(up)) == 5 and tier(5) == 'Partially Adequate')
check("Joint downward reading = 8.5/26 with 10 failures",
      abs(total(down) - 8.5) < 1e-9 and len(fails(down)) == 10)
needed = next(k for k in range(4)
              if all(tier(len(UNCONTESTED_FAILURES) + k) == 'Structurally Inadequate'
                     for _ in combinations(sorted(FLAGGED_FAILURES), k)))
print(f"  Structurally Inadequate holds whenever at least {needed} of C3.5 / C4.2 / C4.3 holds at 0.0.")
check("Tier requires at least one of the three flagged failures to hold", needed == 1)

# ---------------------------------------------------------------- (4)
print("\n(4) CORPUS COMPARISON (canonical SCORES imported; SWF vector AST-extracted)")
canon = locate("neec_weighting_robustness_analysis_v2.py")
spec = importlib.util.spec_from_file_location("neec_v2", canon)
neec_v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(neec_v2)
if hasattr(neec_v2, "verify_transcription"):
    neec_v2.verify_transcription(verbose=False)
SCORES = neec_v2.SCORES
print(f"  Loaded {len(SCORES)} canonical systems from {os.path.basename(canon)}")
check("Canonical corpus still holds exactly 17 systems", len(SCORES) == 17)
check("China is not already in the canonical corpus", not any('China' in k for k in SCORES))

SWF = None
for node in ast.walk(ast.parse(open(locate("verify_swf.py"), encoding="utf-8").read())):
    if isinstance(node, ast.Assign) and any(getattr(tg, 'id', None) == 'SWF' for tg in node.targets):
        SWF = ast.literal_eval(node.value)
check("SWF vector extracted from verify_swf.py (14.0/26, 3 failures)",
      SWF is not None and abs(total(SWF) - 14.0) < 1e-9 and len(fails(SWF)) == 3)
SWF_NAME = 'Sovereign Wealth Fund Statism'
corpus = dict(SCORES)
corpus[SWF_NAME + ' [pending]'] = SWF
corpus[CHINA_NAME + ' [pending]'] = CHINA
CPS = SCORES[key_like(SCORES, 'Centrally Planned')]
SH = SCORES[key_like(SCORES, 'Stakeholder')]
SQ = SCORES[key_like(SCORES, 'Status Quo')]

print("\n  -- Exact ties --")
ties = sorted(n for n, s in SCORES.items() if abs(total(s) - t) < 1e-9)
print(f"  Canonical systems at exactly {t:.1f}/26: {ties}")
check("China ties exactly CPS and Stakeholder Capitalism",
      len(ties) == 2 and any('Centrally Planned' in n for n in ties) and any('Stakeholder' in n for n in ties))
check("China does not tie the pending SWF row", abs(total(SWF) - t) > 1e-9)
for name, s in (('Centrally Planned Socialism', CPS), ('Stakeholder Capitalism', SH)):
    shared = [c for c in f if s[c] == 0.0]
    differ = [c for c in ALL_CRITS if s[c] != CHINA[c]]
    print(f"  vs {name}: {len(fails(s))} failures {fails(s)}")
    print(f"     shared with China ({len(shared)}): {shared}; vectors differ on {len(differ)} of 26")
check("China shares exactly C2.1, C2.2, C2.4, C4.4 with CPS",
      {c for c in f if CPS[c] == 0.0} == {'C2.1', 'C2.2', 'C2.4', 'C4.4'})
check("China shares exactly C2.2, C3.5, C4.2, C4.4 with Stakeholder Capitalism",
      {c for c in f if SH[c] == 0.0} == {'C2.2', 'C3.5', 'C4.2', 'C4.4'})
check("China and CPS differ on 15 of 26 criteria",
      sum(CPS[c] != CHINA[c] for c in ALL_CRITS) == 15)
check("The three tied systems have three different failure counts (8, 12, 9), one shared tier",
      (len(f), len(fails(CPS)), len(fails(SH))) == (8, 12, 9)
      and len({tier(8), tier(12), tier(9)}) == 1)

print("\n  -- Domain profile: China vs CPS (the system China reformed away from) --")
dc = dsums(CPS)
for d in DOMAINS:
    print(f"  {d}: China {ds[d]:.1f}  CPS {dc[d]:.1f}  difference {ds[d] - dc[d]:+.1f}")
check("Identical D1 (3.0) and D3 (2.5) totals, reached through different criteria",
      ds['D1'] == dc['D1'] == 3.0 and ds['D3'] == dc['D3'] == 2.5
      and any(CPS[c] != CHINA[c] for c in DOMAINS['D1'])
      and any(CPS[c] != CHINA[c] for c in DOMAINS['D3']))
check("Net shifts vs CPS: D2 +0.5, D4 -2.5, D5 +2.0",
      (ds['D2'] - dc['D2'], ds['D4'] - dc['D4'], ds['D5'] - dc['D5']) == (0.5, -2.5, 2.0))

print("\n  -- Dominance against all 18 other systems --")
dom_by, dom_over = [], []
for n, s in corpus.items():
    if n.startswith(CHINA_NAME):
        continue
    rel = ("DOMINATES China" if dominates(s, CHINA) else
           "is DOMINATED by China" if dominates(CHINA, s) else "non-dominated pair")
    (dom_by if dominates(s, CHINA) else dom_over if dominates(CHINA, s) else []).append(n)
    print(f"  {n:58} {rel}")
check("China is dominated only by CCO-PTF-CIP-SZH", dom_by == ['CCO-PTF-CIP-SZH'])
check("China strictly dominates no system", dom_over == [])
check("China vs CPS, Status Quo, Stakeholder, Nordic, SWF: all non-dominated pairs",
      all(not dominates(a, CHINA) and not dominates(CHINA, a)
          for a in (CPS, SQ, SH, SCORES[key_like(SCORES, 'Nordic')], SWF)))

print("\n  -- Ranking in the prospective 19-system corpus --")
order = list(corpus)
ranked = sorted(corpus.items(), key=lambda kv: (-total(kv[1]), order.index(kv[0])))
for i, (n, s) in enumerate(ranked, 1):
    tag = "   <==" if n.startswith(CHINA_NAME) else ""
    print(f"  {i:>2}. {n:58} {total(s):>5.1f}/26 ({round(total(s) / 26 * 100):>2}%)  fails={len(fails(s)):>2}{tag}")
below = [n for n, s in corpus.items() if total(s) < t]
above = [n for n, s in corpus.items() if total(s) > t]
print(f"  Strictly above China: {len(above)}; tied (incl. China): 3; strictly below: {below}")
check("China is tied for 16th-18th of 19 (15 above, 2 tied, 1 below: Libertarian Minarchism)",
      len(above) == 15 and below == ['Libertarian Minarchism'])

print("\n  -- Step 1b-cohort facts cited in the Final Assessment --")
cohort = {k: SCORES[key_like(SCORES, k)] for k in STEP1B_KEYS}
cohort[SWF_NAME] = SWF
cohort[CHINA_NAME] = CHINA
for n, s in cohort.items():
    d1f = [c for c in DOMAINS['D1'] if s[c] == 0.0]
    print(f"  {n:34} D1 {dsums(s)['D1']:.1f}/6  D1 failures: {d1f or 'none'}")
check("China has the highest Domain 1 score of the six Step 1b systems",
      all(dsums(s)['D1'] < ds['D1'] for n, s in cohort.items() if n != CHINA_NAME))
check("China is the first Step 1b system with zero Domain 1 failures",
      [n for n, s in cohort.items() if not any(s[c] == 0.0 for c in DOMAINS['D1'])] == [CHINA_NAME])
check("China ties Doughnut Economics for the most failures among the six Step 1b systems (8 each)",
      len(fails(cohort["Doughnut"])) == len(f) == 8
      and all(len(fails(s)) < 8 for n, s in cohort.items() if n not in ("Doughnut", CHINA_NAME)))

d2 = sorted((dsums(s)['D2'], n) for n, s in corpus.items())
d4 = sorted((dsums(s)['D4'], n) for n, s in corpus.items())
print(f"  Lowest Domain 2: {d2[:3]}")
print(f"  Lowest Domain 4: {d4[:3]}")
check("China's Domain 2 (1.0) is the second-lowest in the corpus, above only CPS (0.5)",
      'Centrally Planned' in d2[0][1] and d2[1][1].startswith(CHINA_NAME) and d2[2][0] > 1.0)
check("China's Domain 4 (0.5) ties Status Quo for the lowest Domain 4 in the corpus",
      d4[0][0] == d4[1][0] == 0.5 and d4[2][0] > 0.5
      and {d4[0][1][:10], d4[1][1][:10]} == {CHINA_NAME[:10], 'Status Quo'})
c32 = [n for n, s in corpus.items() if s['C3.2'] == 1.0]
check("China joins Status Quo and CPS at C3.2 = 1.0 (the two existing-system precedents its rationale cites)", all(any(k in n for n in c32) for k in ('Status Quo', 'Centrally Planned')))
up_ties = [n for n, s in corpus.items() if abs(total(s) - total(up)) < 1e-9 and not n.startswith(CHINA_NAME)]
print(f"  (Disclosure) Systems at the joint-upward total of {total(up):.1f}: {up_ties}")

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
print("sensitivity, and every comparative claim against the real canonical corpus.")
