#!/usr/bin/env python3
"""
Session 16. Full 17-system corpus analysis, mirroring regen_analysis_paper.py's
approach (correctly -- failure_count(s) takes a name, not a score dict) but run
fresh against the Session-16-updated neec_weighting_robustness_analysis_v2.py.
This does NOT edit the Report or Paper -- it is analysis output only, to inform
whoever next does the "Step 5 (expanded)" regeneration pass for these two systems.
"""
import importlib.util

spec = importlib.util.spec_from_file_location("v2script", "neec_weighting_robustness_analysis_v2.py")
v2script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2script)

SCORES = v2script.SCORES
PUBLISHED = v2script.PUBLISHED
ALL_CRITS = v2script.ALL_CRITS
D1_CRITS = v2script.D1_CRITS

assert v2script.verify_transcription(verbose=False), "Transcription check failed -- STOP"
assert v2script.verify_unchanged_from_legacy(verbose=False), "Legacy-unchanged check failed -- STOP"

def failure_count(s):
    return sum(1 for c in ALL_CRITS if SCORES[s][c] == 0.0)

def tier(f):
    if f < 3: return 'Potentially Adequate'
    elif f <= 5: return 'Partially Adequate'
    return 'Structurally Inadequate'

def dominates(a, b):
    ge_all = all(SCORES[a][c] >= SCORES[b][c] for c in ALL_CRITS)
    gt_some = any(SCORES[a][c] > SCORES[b][c] for c in ALL_CRITS)
    return ge_all and gt_some

systems = list(SCORES.keys())
print(f"Corpus size: {len(systems)} systems\n")

print("=" * 100)
print("1. RANKING TABLE, ALL 17 SYSTEMS (26-criterion structure)")
print("=" * 100)
rows = []
for s in systems:
    total = PUBLISHED[s]['Total']
    pct = round(total / 26 * 100)
    f = failure_count(s)
    rows.append((s, total, pct, f, tier(f)))
rows.sort(key=lambda r: (-r[1], r[3]))
for i, r in enumerate(rows, 1):
    print(f"{i:2d}. {r[0]:<42} {r[1]:5.1f}/26  {r[2]:3d}%  {r[3]:2d} fail  {r[4]}")

print()
tiers = {}
for r in rows:
    tiers.setdefault(r[4], []).append(r[0])
for t, members in tiers.items():
    print(f"  {t}: {len(members)} systems")

print()
print("=" * 100)
print("2. FULL PAIRWISE STRICT-DOMINANCE / PARETO FRONTIER (all 26 criteria, 17 systems)")
print("=" * 100)
frontier = []
for a in systems:
    dominated = any(dominates(b, a) for b in systems if b != a)
    if not dominated:
        frontier.append(a)
print(f"Full frontier ({len(frontier)} of {len(systems)} systems): {frontier}")

adequate = [s for s in systems if tier(failure_count(s)) != 'Structurally Inadequate']
print(f"\nAdequate-tier subset ({len(adequate)} systems): {adequate}")
frontier_adequate = []
for a in adequate:
    dominated = any(dominates(b, a) for b in adequate if b != a)
    if not dominated:
        frontier_adequate.append(a)
print(f"Frontier restricted to adequate systems ({len(frontier_adequate)}): {frontier_adequate}")

print()
print("=" * 100)
print("3. WHERE DO THE TWO NEW SYSTEMS SIT RELATIVE TO EVERY OTHER SYSTEM (full pairwise)")
print("=" * 100)
for new_sys in ['Doughnut Economics', 'Universal Basic Services']:
    print(f"\n--- {new_sys} ---")
    dominates_others = [s for s in systems if s != new_sys and dominates(new_sys, s)]
    dominated_by = [s for s in systems if s != new_sys and dominates(s, new_sys)]
    print(f"  Dominates: {dominates_others if dominates_others else '(none)'}")
    print(f"  Dominated by: {dominated_by}")
    non_dominated_peers = [s for s in systems if s != new_sys and not dominates(new_sys, s) and not dominates(s, new_sys)]
    print(f"  Non-dominated peers ({len(non_dominated_peers)}): {non_dominated_peers}")

print()
print("=" * 100)
print("4. CRITERION-LEVEL FAILURE COUNTS (0.0), ALL 26 CRITERIA, 17 SYSTEMS")
print("=" * 100)
crit_fails = []
for c in ALL_CRITS:
    failing = [s for s in systems if SCORES[s][c] == 0.0]
    crit_fails.append((c, len(failing), failing))
crit_fails.sort(key=lambda x: -x[1])
for c, n, failing in crit_fails:
    print(f"  {c:<7} {n:2d}/17  {failing}")

print()
print("=" * 100)
print("5. DOMAIN EXCELLENCE TABLES (top 5 per domain, all ties shown)")
print("=" * 100)
domain_crits = {
    'D1': D1_CRITS,
    'D2': [f'C2.{i}' for i in range(1,6)],
    'D3': [f'C3.{i}' for i in range(1,6)],
    'D4': [f'C4.{i}' for i in range(1,6)],
    'D5': [f'C5.{i}' for i in range(1,6)],
}
for d, crits in domain_crits.items():
    vals = sorted(((s, round(sum(SCORES[s][c] for c in crits),4)) for s in systems), key=lambda x: -x[1])
    print(f"\n{d} (max {6.0 if d=='D1' else 5.0}):")
    shown = 0
    prev_val = None
    for s, v in vals:
        if shown >= 5 and v != prev_val:
            break
        print(f"    {s:<38} {v}")
        prev_val = v
        shown += 1

print()
print("=" * 100)
print("6. SPOT-CHECK: Georgism vs UBS exact tie -- confirm neither dominates (13.5/26 each)")
print("=" * 100)
print(f"  Georgism dominates UBS: {dominates('Georgism / Land Value Tax', 'Universal Basic Services')}")
print(f"  UBS dominates Georgism: {dominates('Universal Basic Services', 'Georgism / Land Value Tax')}")
g_breaks = [c for c in ALL_CRITS if SCORES['Georgism / Land Value Tax'][c] > SCORES['Universal Basic Services'][c]]
u_breaks = [c for c in ALL_CRITS if SCORES['Universal Basic Services'][c] > SCORES['Georgism / Land Value Tax'][c]]
print(f"  Criteria where Georgism > UBS: {g_breaks}")
print(f"  Criteria where UBS > Georgism: {u_breaks}")

print()
print("=" * 100)
print("7. Domain sums for both new systems (cross-check against PUBLISHED)")
print("=" * 100)
for s in ['Doughnut Economics', 'Universal Basic Services']:
    v = SCORES[s]
    print(f"--- {s} ---")
    print("D1:", sum(v[c] for c in D1_CRITS), "vs published", PUBLISHED[s]['D1'])
    print("D2:", sum(v[f'C2.{k}'] for k in range(1,6)), "vs published", PUBLISHED[s]['D2'])
    print("D3:", sum(v[f'C3.{k}'] for k in range(1,6)), "vs published", PUBLISHED[s]['D3'])
    print("D4:", sum(v[f'C4.{k}'] for k in range(1,6)), "vs published", PUBLISHED[s]['D4'])
    print("D5:", sum(v[f'C5.{k}'] for k in range(1,6)), "vs published", PUBLISHED[s]['D5'])
    print("Total:", sum(v[c] for c in ALL_CRITS), "vs published", PUBLISHED[s]['Total'])
    print("Failures:", failure_count(s), "--", [c for c in ALL_CRITS if v[c]==0.0])
    print()
