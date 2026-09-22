#!/usr/bin/env python3
"""
regen_analysis_paper.py
========================
Session 10. Rebuilds the ALL_15 (Paper) analysis that Session 9's own
regen_analysis.py (Report-side, REPORT_14 only) explicitly flagged as
incomplete: "Other criteria not re-verified against Integral's addition
this session -- a quick re-run of the reproduction script would confirm
before quoting an ALL_15 figure for any criterion not listed here."

Imports SCORES/PUBLISHED directly from neec_weighting_robustness_analysis_v2.py
(the same source of truth Session 8/9 used) rather than retyping any score.
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
try:
    assert v2script.verify_unchanged_from_legacy(verbose=False), "Legacy-unchanged check failed -- STOP"
except FileNotFoundError:
    print("SKIPPED verify_unchanged_from_legacy() -- baseline_weighting_script.py not mounted this session.")

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

print("=" * 100)
print("1. RANKING TABLE, ALL 15 SYSTEMS (26-criterion structure)")
print("=" * 100)
rows = []
for s in systems:
    total = PUBLISHED[s]['Total']
    pct = round(total / 26 * 100)
    f = failure_count(s)
    rows.append((s, total, pct, f, tier(f)))
rows.sort(key=lambda r: (-r[1], r[3]))  # by total desc, then failures asc as tiebreak
for i, r in enumerate(rows, 1):
    print(f"{i:2d}. {r[0]:<42} {r[1]:5.1f}/26  {r[2]:3d}%  {r[3]:2d} fail  {r[4]}")

print()
print("Tier membership counts:")
tiers = {}
for r in rows:
    tiers.setdefault(r[4], []).append(r[0])
for t, members in tiers.items():
    print(f"  {t}: {len(members)} -- {members}")

print()
print("=" * 100)
print("2. FULL PAIRWISE STRICT-DOMINANCE / PARETO FRONTIER (all 26 criteria, 15 systems)")
print("=" * 100)
frontier = []
for a in systems:
    dominated = False
    for b in systems:
        if a == b:
            continue
        if dominates(b, a):
            dominated = True
            break
    if not dominated:
        frontier.append(a)
print(f"Full frontier ({len(frontier)} systems): {frontier}")

adequate = [s for s in systems if tier(failure_count(s)) != 'Structurally Inadequate']
print(f"\nAdequate-tier subset ({len(adequate)} systems): {adequate}")
frontier_adequate = []
for a in adequate:
    dominated = False
    for b in adequate:
        if a == b:
            continue
        if dominates(b, a):
            dominated = True
            break
    if not dominated:
        frontier_adequate.append(a)
print(f"Frontier restricted to adequate systems ({len(frontier_adequate)}): {frontier_adequate}")

print()
print("=" * 100)
print("3. CCO-PTF-CIP-SZH's non-domination pattern across all 14 other systems")
print("=" * 100)
cco = 'CCO-PTF-CIP-SZH'
for s in systems:
    if s == cco:
        continue
    d = dominates(cco, s)
    if not d:
        # find which criteria break it
        breaks = [c for c in ALL_CRITS if SCORES[cco][c] < SCORES[s][c]]
        print(f"  CCO-PTF does NOT dominate {s:<32} -- escapes via: {breaks}")
    else:
        print(f"  CCO-PTF DOMINATES {s}")

print()
print("=" * 100)
print("4. DOMAIN EXCELLENCE TABLES (top 5 per domain, all ties shown)")
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
    top_val = vals[0][1]
    print(f"\n{d} (max {6.0 if d=='D1' else 5.0}):")
    shown = 0
    prev_val = None
    for s, v in vals:
        if shown >= 5 and v != prev_val:
            break
        print(f"    {s:<36} {v}")
        prev_val = v
        shown += 1

print()
print("=" * 100)
print("5. CRITERION-LEVEL FAILURE COUNTS (0.0), ALL 26 CRITERIA, 15 SYSTEMS")
print("=" * 100)
crit_fails = []
for c in ALL_CRITS:
    failing = [s for s in systems if SCORES[s][c] == 0.0]
    crit_fails.append((c, len(failing), failing))
crit_fails.sort(key=lambda x: -x[1])
for c, n, failing in crit_fails:
    print(f"  {c:<7} {n:2d}/15  {failing}")

print()
print("=" * 100)
print("6. SPOT-CHECK: Nordic vs Integral (tied total) -- confirm neither dominates")
print("=" * 100)
print(f"  Nordic dominates Integral: {dominates('Nordic Social Democracy', 'Integral')}")
print(f"  Integral dominates Nordic: {dominates('Integral', 'Nordic Social Democracy')}")
nd_breaks = [c for c in ALL_CRITS if SCORES['Nordic Social Democracy'][c] < SCORES['Integral'][c]]
int_breaks = [c for c in ALL_CRITS if SCORES['Integral'][c] < SCORES['Nordic Social Democracy'][c]]
print(f"  Criteria where Integral > Nordic: {nd_breaks}")
print(f"  Criteria where Nordic > Integral: {int_breaks}")

print()
print("=" * 100)
print("7. Domain sums for Integral (cross-check against PUBLISHED)")
print("=" * 100)
i = SCORES['Integral']
print("D1:", sum(i[c] for c in D1_CRITS), "vs published", PUBLISHED['Integral']['D1'])
print("D2:", sum(i[f'C2.{k}'] for k in range(1,6)), "vs published", PUBLISHED['Integral']['D2'])
print("D3:", sum(i[f'C3.{k}'] for k in range(1,6)), "vs published", PUBLISHED['Integral']['D3'])
print("D4:", sum(i[f'C4.{k}'] for k in range(1,6)), "vs published", PUBLISHED['Integral']['D4'])
print("D5:", sum(i[f'C5.{k}'] for k in range(1,6)), "vs published", PUBLISHED['Integral']['D5'])
print("Total:", sum(i[c] for c in ALL_CRITS), "vs published", PUBLISHED['Integral']['Total'])
print("Failures:", failure_count('Integral'), "-- criteria:", [c for c in ALL_CRITS if i[c]==0.0])
