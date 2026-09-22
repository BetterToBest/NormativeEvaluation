#!/usr/bin/env python3
"""
Independent re-verification of the Sovereign Wealth Fund Statism score
vector against its own scratch document's stated totals, before it is
spliced into any canonical file. Per this project's own methodology.md:
"Programmatic verification over visual checking" and "Dominance checks
are programmatic: any formal dominance claim... is verified by script
against published score vectors before being written into prose."

Two independent checks:
  (1) Self-consistency: re-sum SWF's own 26-criterion vector, transcribed
      fresh from NEEC_SovereignWealthFundStatism_scoring_scratch.md's own
      prose, against that document's own stated domain totals / overall
      total / failure count / tier -- including the disclosed alternate
      reading of the flagged C1.2a/C1.5 contestable call.
  (2) Corpus comparison: import the REAL canonical SCORES dict from the
      actual, unmodified neec_weighting_robustness_analysis_v2.py (not
      hand-retyped from memory) and check every specific comparative
      claim the Final Assessment makes.

PORTABILITY FIX (Session 20): this script originally hard-coded
/home/claude/ as the canonical script's location. It now looks beside
itself first, then in the working directory and the conventional working
locations, as verify_china.py does; nothing it prints has changed.

CORPUS NOTE (Session 20): the corpus claims below were written against the
17-system canonical corpus of Session 16. Sovereign Wealth Fund Statism was
inserted in Session 20, so run this script beside that corpus (the pinned
snapshot neec_weighting_robustness_analysis_v2_s16_snapshot.py, copied
under the canonical file name); run_all_checks.py does this automatically.
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

ALL_CRITS = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5'] + \
            [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
D1_CRITS = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5']

# Transcribed criterion-by-criterion from NEEC_SovereignWealthFundStatism_
# scoring_scratch.md's own prose (fresh transcription).
SWF = {
    'C1.1': 0.5, 'C1.2a': 0.5, 'C1.2b': 0.5, 'C1.3': 0.0, 'C1.4': 0.5, 'C1.5': 0.5,
    'C2.1': 0.5, 'C2.2': 0.5, 'C2.3': 0.5, 'C2.4': 0.5, 'C2.5': 1.0,
    'C3.1': 0.5, 'C3.2': 0.5, 'C3.3': 0.5, 'C3.4': 1.0, 'C3.5': 0.5,
    'C4.1': 1.0, 'C4.2': 0.0, 'C4.3': 0.5, 'C4.4': 0.5, 'C4.5': 0.0,
    'C5.1': 1.0, 'C5.2': 0.5, 'C5.3': 1.0, 'C5.4': 0.5, 'C5.5': 0.5,
}
SWF_PUBLISHED = {'D1': 2.5, 'D2': 3.0, 'D3': 3.0, 'D4': 2.0, 'D5': 3.5, 'Total': 14.0}

# The scratch document's own disclosed alternate reading of its single most
# consequential contestable call (C1.2a and C1.5 both resolved to 0.0).
SWF_ALT = dict(SWF)
SWF_ALT['C1.2a'] = 0.0
SWF_ALT['C1.5'] = 0.0
SWF_ALT_PUBLISHED = {'D1': 1.5, 'D2': 3.0, 'D3': 3.0, 'D4': 2.0, 'D5': 3.5, 'Total': 13.0}


def failure_count(vec):
    return sum(1 for c in ALL_CRITS if vec[c] == 0.0)


def tier(fails):
    if fails < 3:
        return 'Potentially Adequate'
    elif fails <= 5:
        return 'Partially Adequate'
    return 'Structurally Inadequate'


def check_self_consistency(name, vec, published):
    assert len(vec) == 26, f"{name}: vector has {len(vec)} criteria, not 26"
    d1 = sum(vec[c] for c in D1_CRITS)
    d2 = sum(vec[f'C2.{i}'] for i in range(1, 6))
    d3 = sum(vec[f'C3.{i}'] for i in range(1, 6))
    d4 = sum(vec[f'C4.{i}'] for i in range(1, 6))
    d5 = sum(vec[f'C5.{i}'] for i in range(1, 6))
    total = d1 + d2 + d3 + d4 + d5
    fails = failure_count(vec)
    t = tier(fails)
    print(f"--- {name} ---")
    print(f"  Recomputed: D1={d1}/6 D2={d2}/5 D3={d3}/5 D4={d4}/5 D5={d5}/5  "
          f"Total={total}/26 ({round(total/26*100)}%)")
    print(f"  Stated:     D1={published['D1']} D2={published['D2']} D3={published['D3']} "
          f"D4={published['D4']} D5={published['D5']}  Total={published['Total']}")
    ok = (abs(d1 - published['D1']) < 1e-9 and abs(d2 - published['D2']) < 1e-9
          and abs(d3 - published['D3']) < 1e-9 and abs(d4 - published['D4']) < 1e-9
          and abs(d5 - published['D5']) < 1e-9 and abs(total - published['Total']) < 1e-9)
    print(f"  Domain/total match: {'PASS' if ok else 'FAIL <<<<<'}")
    fail_list = [c for c in ALL_CRITS if vec[c] == 0.0]
    print(f"  Failures: {fails} -- {fail_list}  ->  Tier: {t}")
    print()
    return ok, total, fails, t, fail_list


print("=" * 88)
print("PART 1: SELF-CONSISTENCY CHECK")
print("=" * 88)
ok, total, fails, t, fail_list = check_self_consistency(
    "Sovereign Wealth Fund Statism (primary reading: C1.2a=C1.5=0.5)", SWF, SWF_PUBLISHED)
ok_alt, total_alt, fails_alt, t_alt, fail_list_alt = check_self_consistency(
    "Sovereign Wealth Fund Statism (disclosed alternate: C1.2a=C1.5=0.0)", SWF_ALT, SWF_ALT_PUBLISHED)

consequence_ok = (t == t_alt)
print(f"Scratch doc's claim: resolving the flagged C1.2a/C1.5 call does NOT move the "
      f"adequacy tier either way.")
print(f"Checked: primary tier = '{t}' ({fails} failures); alternate tier = '{t_alt}' "
      f"({fails_alt} failures).")
print(f"Claim verified: {'PASS -- tier unchanged, as claimed' if consequence_ok else 'FAIL <<<<<'}")
print()

# --- Corpus-comparison check against the REAL canonical vectors.
print("=" * 88)
print("PART 2: CORPUS-COMPARISON CHECK AGAINST THE REAL CANONICAL SCORES")
print("=" * 88)
spec = importlib.util.spec_from_file_location(
    "neec_v2", locate("neec_weighting_robustness_analysis_v2.py"))
neec_v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(neec_v2)

assert neec_v2.verify_transcription(verbose=False), "Canonical corpus transcription check failed -- STOP"
print("Canonical 17-system corpus loaded and self-verified (verify_transcription() PASS).\n")


def dominates(a, b, scores):
    ge_all = all(scores[a][c] >= scores[b][c] for c in ALL_CRITS)
    gt_some = any(scores[a][c] > scores[b][c] for c in ALL_CRITS)
    return ge_all and gt_some


combined = dict(neec_v2.SCORES)
combined['Sovereign Wealth Fund Statism'] = SWF

print("-- No-exact-tie check --")
existing_totals = {name: neec_v2.PUBLISHED[name]['Total'] for name in neec_v2.PUBLISHED}
ties = [name for name, tot in existing_totals.items() if abs(tot - total) < 1e-9]
print(f"  SWF total = {total}/26. Existing systems at the exact same total: {ties if ties else 'none'}")
print(f"  Claim (no exact tie): {'PASS' if not ties else 'FAIL <<<<<'}")
print()

print("-- Failure-set overlap check (Final Assessment's claims) --")
mc_fails = set(c for c in ALL_CRITS if neec_v2.SCORES['Mutual Credit / LETS'][c] == 0.0)
ubs_fails = set(c for c in ALL_CRITS if neec_v2.SCORES['Universal Basic Services'][c] == 0.0)
swf_fails = set(fail_list)
mc_overlap = swf_fails & mc_fails
ubs_overlap = swf_fails & ubs_fails
print(f"  SWF fails:                {sorted(swf_fails)}")
print(f"  Mutual Credit/LETS fails: {sorted(mc_fails)}  -> overlap: {sorted(mc_overlap)}")
print(f"  UBS fails:                {sorted(ubs_fails)}  -> overlap: {sorted(ubs_overlap)}")
mc_claim_ok = (mc_overlap == {'C1.3'})
ubs_claim_ok = (ubs_overlap == set())
print(f"  Claim (overlaps MC/LETS on exactly {{C1.3}}): {'PASS' if mc_claim_ok else 'FAIL <<<<<'}")
print(f"  Claim (overlaps UBS on nothing):              {'PASS' if ubs_claim_ok else 'FAIL <<<<<'}")
print()

print("-- Wealth-cluster clearance check (C1.2a, C1.2b, C1.5) --")
wealth_crits = ['C1.2a', 'C1.2b', 'C1.5']
comparators = ['Georgism / Land Value Tax', 'Mutual Credit / LETS', 'Doughnut Economics',
               'Universal Basic Services']
for sysname in comparators:
    zeros = [c for c in wealth_crits if neec_v2.SCORES[sysname][c] == 0.0]
    print(f"  {sysname:<28} wealth-cluster zeros: {zeros if zeros else 'NONE'}")
swf_wealth_zeros = [c for c in wealth_crits if SWF[c] == 0.0]
print(f"  {'Sovereign Wealth Fund Statism':<28} wealth-cluster zeros: "
      f"{swf_wealth_zeros if swf_wealth_zeros else 'NONE (clears all three)'}")
first_to_clear = all(
    any(neec_v2.SCORES[s][c] == 0.0 for c in wealth_crits) for s in comparators
) and not swf_wealth_zeros
print(f"  Claim (SWF is first of the four new Step 1b systems to clear all three): "
      f"{'PASS' if first_to_clear else 'FAIL <<<<<'}")
print()

print("-- Dominance checks --")
for other in ['CCO-PTF-CIP-SZH', 'Georgism / Land Value Tax', 'Mutual Credit / LETS',
              'Universal Basic Services', 'Nordic Social Democracy']:
    fwd = dominates('Sovereign Wealth Fund Statism', other, combined)
    back = dominates(other, 'Sovereign Wealth Fund Statism', combined)
    rel = ("SWF strictly DOMINATES " + other if fwd else
           (other + " strictly DOMINATES SWF" if back else "non-dominated pair"))
    print(f"  Sovereign Wealth Fund Statism  vs  {other:<32} {rel}")
print()

print("-- Ranking among the (prospective) 18-system corpus --")
all_totals = [(s, neec_v2.PUBLISHED[s]['Total']) for s in neec_v2.PUBLISHED]
all_totals.append(('Sovereign Wealth Fund Statism [scratch, not yet inserted]', total))
all_totals.sort(key=lambda x: -x[1])
for i, (s, v) in enumerate(all_totals, 1):
    marker = "  <==" if 'Sovereign Wealth Fund' in s else ""
    print(f"  {i:2d}. {s:<55} {v:5.1f}/26 ({round(v/26*100)}%){marker}")
print()

print("=" * 88)
print("SUMMARY")
print("=" * 88)
all_ok = ok and ok_alt and consequence_ok and not ties and mc_claim_ok and ubs_claim_ok and first_to_clear
if all_ok:
    print("ALL CHECKS PASS. Self-consistency confirmed (both the primary reading and the")
    print("disclosed alternate reading); every comparative claim in the Final Assessment is")
    print("independently verified against the real canonical corpus, loaded rather than")
    print("retyped. Consistent with this project's scratch-before-insert discipline, this")
    print("does not insert the system anywhere -- it only confirms the scratch document's")
    print("own arithmetic and comparative claims ahead of that later, separate pass.")
else:
    raise SystemExit("MISMATCH FOUND -- see FAIL lines above.")
