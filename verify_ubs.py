#!/usr/bin/env python3
"""
verify_ubs.py
=============
Session 15, ad hoc verification (not yet folded into the project's standing
verification scripts, since Universal Basic Services is not yet in the
canonical CSV -- exactly the same status Doughnut Economics' own
verify_doughnut.py had in Session 14).

Loads the actual, canonical SCORES dict from neec_weighting_robustness_analysis_v2.py
(unmodified copy) so that every comparison system's vector used below is the
real, already-published one -- not retyped from memory -- before checking:
  1. UBS's own domain/total arithmetic and failure count/tier.
  2. Whether UBS and Georgism (which land at the identical 13.5/26 raw score)
     can possibly stand in a dominance relation (they cannot, by construction,
     since equal totals rule out strict dominance in either direction --
     confirmed here rather than merely asserted).
  3. Which specific criteria differ between UBS and Georgism, in which
     direction -- to state the comparison precisely rather than just noting
     the score tie.
  4. Whether CCO-PTF-CIP-SZH formally dominates UBS (expected, given CCO-PTF's
     near-universal high scores, but checked rather than assumed).
  5. UBS vs. Mutual Credit/LETS and UBS vs. Doughnut Economics (the latter's
     vector entered here from its own already-computed, independently
     re-verified scratch document, since it likewise isn't in the canonical
     CSV yet).

PORTABILITY FIX (Session 20): the canonical script's location was
hard-coded to /home/claude/. It is now looked up beside this script first,
then in the working directory and the conventional working locations.

CORPUS NOTE (Session 20): this script was written against the 15-system
corpus of Session 15. Universal Basic Services and Doughnut Economics were
inserted in Session 16, so against any later canonical file section 6's
prospective ranking lists both systems twice. run_all_checks.py runs this
script against a 15-system view derived from the pinned Session 16
snapshot (that snapshot minus the two Session 16 insertions).
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = (HERE, os.getcwd(), "/home/claude", "/home/claude/neec",
               "/mnt/user-data/outputs", "/mnt/project")


def locate(filename):
    for d in SEARCH_DIRS:
        p = os.path.join(d, filename)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: could not locate {filename} in {SEARCH_DIRS}")


spec = importlib.util.spec_from_file_location("v2script", locate("neec_weighting_robustness_analysis_v2.py"))
v2script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2script)

SCORES = v2script.SCORES
ALL_CRITS = v2script.ALL_CRITS
D1_CRITS = v2script.D1_CRITS

assert v2script.verify_transcription(verbose=False), "Canonical corpus transcription check failed -- STOP"
print("Canonical 15-system corpus: verify_transcription() PASS (loaded, not retyped).\n")

# ---------------------------------------------------------------------------
# Universal Basic Services -- this session's score vector
# ---------------------------------------------------------------------------
UBS = {
    'C1.1': 0.5, 'C1.2a': 0.0, 'C1.2b': 0.0, 'C1.3': 0.5, 'C1.4': 0.5, 'C1.5': 0.0,
    'C2.1': 0.5, 'C2.2': 0.5, 'C2.3': 0.5, 'C2.4': 0.5, 'C2.5': 1.0,
    'C3.1': 0.5, 'C3.2': 0.5, 'C3.3': 0.5, 'C3.4': 1.0, 'C3.5': 0.5,
    'C4.1': 0.5, 'C4.2': 0.5, 'C4.3': 0.5, 'C4.4': 0.5, 'C4.5': 0.5,
    'C5.1': 1.0, 'C5.2': 0.5, 'C5.3': 1.0, 'C5.4': 0.5, 'C5.5': 0.5,
}
assert len(UBS) == 26, f"UBS vector has {len(UBS)} criteria, not 26"

# Doughnut Economics' own vector, transcribed from its own Session 14 scratch
# document (not yet in the canonical CSV either) -- included here only for
# the UBS-vs-Doughnut comparison below, cross-checked against that
# document's own stated Summary Scores before use.
DOUGHNUT = {
    'C1.1': 0.5, 'C1.2a': 0.0, 'C1.2b': 0.0, 'C1.3': 0.5, 'C1.4': 0.0, 'C1.5': 0.0,
    'C2.1': 0.0, 'C2.2': 0.0, 'C2.3': 0.5, 'C2.4': 0.5, 'C2.5': 1.0,
    'C3.1': 0.5, 'C3.2': 0.5, 'C3.3': 0.5, 'C3.4': 1.0, 'C3.5': 0.5,
    'C4.1': 1.0, 'C4.2': 1.0, 'C4.3': 0.5, 'C4.4': 0.0, 'C4.5': 0.0,
    'C5.1': 0.5, 'C5.2': 0.5, 'C5.3': 1.0, 'C5.4': 0.5, 'C5.5': 0.5,
}
assert len(DOUGHNUT) == 26

def domain_sums(vec):
    return {
        'D1': round(sum(vec[c] for c in D1_CRITS), 4),
        'D2': round(sum(vec[f'C2.{i}'] for i in range(1, 6)), 4),
        'D3': round(sum(vec[f'C3.{i}'] for i in range(1, 6)), 4),
        'D4': round(sum(vec[f'C4.{i}'] for i in range(1, 6)), 4),
        'D5': round(sum(vec[f'C5.{i}'] for i in range(1, 6)), 4),
    }

def total(vec):
    return round(sum(vec.values()), 4)

def failure_count(vec):
    return sum(1 for c in ALL_CRITS if vec[c] == 0.0)

def tier(f):
    if f < 3:
        return 'Potentially Adequate'
    elif f <= 5:
        return 'Partially Adequate'
    return 'Structurally Inadequate'

def dominates(a_vec, b_vec):
    ge_all = all(a_vec[c] >= b_vec[c] for c in ALL_CRITS)
    gt_some = any(a_vec[c] > b_vec[c] for c in ALL_CRITS)
    return ge_all and gt_some

print("=" * 90)
print("1. UBS ARITHMETIC CHECK")
print("=" * 90)
ds = domain_sums(UBS)
t = total(UBS)
f = failure_count(UBS)
for d, v in ds.items():
    mx = 6.0 if d == 'D1' else 5.0
    print(f"  {d}: {v}/{mx}  ({round(v/mx*100)}%)")
print(f"  Total: {t}/26  ({round(t/26*100)}%)")
print(f"  Cross-check -- sum of five domain totals equals stated total: {abs(sum(ds.values()) - t) < 1e-9}")
print(f"  Failures (0.0 count): {f} -- {[c for c in ALL_CRITS if UBS[c]==0.0]}")
print(f"  Tier: {tier(f)}")

print()
print("=" * 90)
print("2. UBS vs. GEORGISM / LAND VALUE TAX -- exact-total-score comparison")
print("=" * 90)
geo = SCORES['Georgism / Land Value Tax']
geo_total = total(geo)
print(f"  Georgism total (from canonical SCORES dict, loaded not retyped): {geo_total}/26")
print(f"  UBS total (this session):                                       {t}/26")
print(f"  Exact match: {abs(geo_total - t) < 1e-9}")
print(f"  Georgism dominates UBS: {dominates(geo, UBS)}")
print(f"  UBS dominates Georgism: {dominates(UBS, geo)}")
print(f"  (Mathematically guaranteed both False whenever totals are exactly equal and vectors differ --")
print(f"   confirmed rather than merely asserted.)")
diffs_geo_higher = [c for c in ALL_CRITS if geo[c] > UBS[c]]
diffs_ubs_higher = [c for c in ALL_CRITS if UBS[c] > geo[c]]
print(f"  Criteria where Georgism > UBS: {diffs_geo_higher}")
print(f"  Criteria where UBS > Georgism: {diffs_ubs_higher}")
print(f"  (Same count on each side, since totals are equal: {len(diffs_geo_higher)} vs {len(diffs_ubs_higher)})")

print()
print("=" * 90)
print("3. CCO-PTF-CIP-SZH vs. UBS")
print("=" * 90)
cco = SCORES['CCO-PTF-CIP-SZH']
print(f"  CCO-PTF total: {total(cco)}/26   UBS total: {t}/26")
print(f"  CCO-PTF dominates UBS: {dominates(cco, UBS)}")
if not dominates(cco, UBS):
    breaks = [c for c in ALL_CRITS if cco[c] < UBS[c]]
    print(f"  Escapes via: {breaks}")

print()
print("=" * 90)
print("4. UBS vs. MUTUAL CREDIT/LETS")
print("=" * 90)
mc = SCORES['Mutual Credit / LETS']
print(f"  Mutual Credit/LETS total: {total(mc)}/26   UBS total: {t}/26")
print(f"  Mutual Credit dominates UBS: {dominates(mc, UBS)}")
print(f"  UBS dominates Mutual Credit: {dominates(UBS, mc)}")
if not dominates(mc, UBS) and not dominates(UBS, mc):
    print(f"    Criteria where Mutual Credit > UBS: {[c for c in ALL_CRITS if mc[c] > UBS[c]]}")
    print(f"    Criteria where UBS > Mutual Credit: {[c for c in ALL_CRITS if UBS[c] > mc[c]]}")

print()
print("=" * 90)
print("5. UBS vs. DOUGHNUT ECONOMICS (both not yet in canonical CSV; DOUGHNUT vector")
print("   transcribed from its own Session 14 scratch document for this comparison only)")
print("=" * 90)
print(f"  Doughnut total: {total(DOUGHNUT)}/26   UBS total: {t}/26")
print(f"  Doughnut dominates UBS: {dominates(DOUGHNUT, UBS)}")
print(f"  UBS dominates Doughnut: {dominates(UBS, DOUGHNUT)}")
if dominates(UBS, DOUGHNUT):
    print(f"    (UBS >= Doughnut on every criterion, > on at least one -- listing the strict-improvement criteria:)")
    print(f"    {[c for c in ALL_CRITS if UBS[c] > DOUGHNUT[c]]}")
    print(f"    (Any criteria where Doughnut > UBS, which would break strict dominance: "
          f"{[c for c in ALL_CRITS if DOUGHNUT[c] > UBS[c]]})")

print()
print("=" * 90)
print("6. Where does UBS rank among the (soon-to-be) 17-system corpus, by total score?")
print("=" * 90)
all_totals = [(s, total(v)) for s, v in SCORES.items()]
all_totals.append(('Universal Basic Services (this session)', t))
all_totals.append(('Doughnut Economics (Session 14, not yet inserted)', total(DOUGHNUT)))
all_totals.sort(key=lambda x: -x[1])
for i, (s, v) in enumerate(all_totals, 1):
    marker = "  <== " if 'Universal Basic Services' in s or 'Doughnut' in s else ""
    print(f"  {i:2d}. {s:<52} {v:5.1f}/26 ({round(v/26*100)}%){marker}")
