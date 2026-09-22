#!/usr/bin/env python3
"""
run_a4_full_rerun.py
=====================
Session 12. Executes the FULL Appendix A.4 (Paper) weighting-robustness
check against the complete 15-system, 26-criterion corpus -- the item
Paper Section 12.5 explicitly flagged as "not re-run... remains a
candidate for a future revision" and Session 11's own handoff listed as
Remaining Scope item 2.

This does NOT re-derive any scoring logic. It imports SCORES/PUBLISHED/
SCHEMES/weighted_total/max_possible/failure_count/tier/dominates directly
from the already-canonical, already-cross-validated
neec_weighting_robustness_analysis_v2.py (unmodified copy) and simply
DRIVES the computation that script's own run_full_report() function
already assembles, with one deliberate omission: verify_unchanged_from_
legacy() is skipped here, not because it doesn't matter, but because (a)
baseline_weighting_script.py remains absent from the project mount (a
known, separately-tracked standing issue -- see handoff Remaining Scope
item 8) and (b) that specific check tests something orthogonal to this
task's own scope (whether Step 1c's retrofit touched only the wealth
criteria -- already independently confirmed clean in Sessions 8-10 when
the baseline file WAS available). verify_transcription() -- the check
that actually matters for trusting THIS output -- is run and required to
pass before anything below it executes.
"""
import importlib.util

spec = importlib.util.spec_from_file_location("v2script", "neec_weighting_robustness_analysis_v2.py")
v2script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2script)

assert v2script.verify_transcription(verbose=False), "Transcription check failed -- STOP"
print("verify_transcription(): PASS -- all 15 systems' 26-criterion vectors sum to their")
print("published domain/overall totals exactly. (verify_unchanged_from_legacy() skipped")
print("this run -- baseline_weighting_script.py still absent from the mount; see handoff.)")
print()

SCORES = v2script.SCORES
PUBLISHED = v2script.PUBLISHED
SCHEMES = v2script.SCHEMES
ALL_CRITS = v2script.ALL_CRITS
weighted_total = v2script.weighted_total
max_possible = v2script.max_possible
failure_count = v2script.failure_count
tier = v2script.tier
dominates = v2script.dominates

systems = list(SCORES.keys())

# ---------------------------------------------------------------------
# 1. RANKINGS UNDER EACH SCHEME, ALL 15 SYSTEMS
# ---------------------------------------------------------------------
print("=" * 100)
print(f"RANKINGS UNDER EACH SCHEME, ALL {len(SCORES)} SYSTEMS (by weighted %, descending)")
print("=" * 100)
results = {}
for name, w in SCHEMES.items():
    mx = max_possible(w)
    rows = sorted(((s, weighted_total(c, w), weighted_total(c, w) / mx * 100)
                    for s, c in SCORES.items()), key=lambda r: -r[1])
    results[name] = rows
    print(f"\n--- {name} (max possible = {mx:.1f}) ---")
    for i, (sys, wt, pct) in enumerate(rows, 1):
        print(f"  {i:2d}. {sys:<38} {wt:6.2f}  ({pct:5.1f}%)  [{failure_count(SCORES[sys])} fail, {tier(failure_count(SCORES[sys]))}]")

# ---------------------------------------------------------------------
# 2. RANK-POSITION TABLE ACROSS ALL FOUR SCHEMES (for the write-up table)
# ---------------------------------------------------------------------
print("\n" + "=" * 100)
print("RANK POSITION BY SYSTEM, ACROSS ALL FOUR SCHEMES (1 = highest)")
print("=" * 100)
rank_lookup = {}
for name, rows in results.items():
    for i, (sys, wt, pct) in enumerate(rows, 1):
        rank_lookup.setdefault(sys, {})[name] = (i, pct)

# order by equal-weighted rank
eq_order = [s for s, wt, pct in results['Equal (baseline)']]
header = f"{'System':<38}" + "".join(f"{n[:14]:>16}" for n in SCHEMES.keys())
print(header)
for s in eq_order:
    row = f"{s:<38}"
    for n in SCHEMES.keys():
        i, pct = rank_lookup[s][n]
        row += f"{i:>10d} ({pct:4.1f}%)"
    print(row)

# ---------------------------------------------------------------------
# 3. MAX RANK MOVEMENT PER SYSTEM (equal vs each alt scheme)
# ---------------------------------------------------------------------
print("\n" + "=" * 100)
print("RANK MOVEMENT: equal-weighted rank vs. each alternative scheme")
print("=" * 100)
eq_rank = {s: i for i, (s, wt, pct) in enumerate(results['Equal (baseline)'], 1)}
for name in SCHEMES.keys():
    if name == 'Equal (baseline)':
        continue
    alt_rank = {s: i for i, (s, wt, pct) in enumerate(results[name], 1)}
    moves = [(s, eq_rank[s], alt_rank[s], alt_rank[s] - eq_rank[s]) for s in systems]
    moves.sort(key=lambda x: -abs(x[3]))
    print(f"\n--- {name}: largest rank movements ---")
    for s, er, ar, delta in moves[:6]:
        if delta != 0:
            print(f"  {s:<38} equal-rank {er:2d} -> {name[:20]}-rank {ar:2d}  (delta {delta:+d})")

# ---------------------------------------------------------------------
# 4. ADEQUACY TIER (invariant to weighting by construction) -- confirm for all 15
# ---------------------------------------------------------------------
print("\n" + "=" * 100)
print("ADEQUACY TIER (failure-count based) -- confirm invariant across all 4 schemes, all 15 systems")
print("=" * 100)
for s in systems:
    f = failure_count(SCORES[s])
    print(f"  {s:<38} {f:2d} failures -> {tier(f)}")

# ---------------------------------------------------------------------
# 5. DOMINANCE-PAIR SPOT CHECK, extended for the 15-system corpus
# ---------------------------------------------------------------------
print("\n" + "=" * 100)
print("DOMINANCE-PAIR SPOT CHECK (Theorem 5 guarantees positive under ANY positive weighting")
print("wherever strict dominance holds; confirmatory, not exploratory)")
print("=" * 100)
pairs = [
    ('CCO-PTF-CIP-SZH', 'Status Quo Market Capitalism'),
    ('CCO-PTF-CIP-SZH', 'Nordic Social Democracy'),
    ('CCO-PTF-CIP-SZH', 'MMT + Job Guarantee'),
    ('CCO-PTF-CIP-SZH', 'Georgism / Land Value Tax'),
    ('Participatory Economics', 'Stakeholder Capitalism'),
    ('Mutual Credit / LETS', 'Georgism / Land Value Tax'),
]
for a, b in pairs:
    strict = dominates(a, b)
    print(f"\n  {a}  vs  {b}   (strict formal dominance: {strict})")
    for name, w in SCHEMES.items():
        wa, wb = weighted_total(SCORES[a], w), weighted_total(SCORES[b], w)
        rel = ">" if wa > wb else ("=" if wa == wb else "<=")
        print(f"    {name:<38} {wa:6.2f} {rel} {wb:6.2f}")

# ---------------------------------------------------------------------
# 6. Nordic/Integral spot-check, confirmed once more against fresh computation
# ---------------------------------------------------------------------
print("\n" + "=" * 100)
print("NORDIC vs INTEGRAL under all 4 schemes (Section 12.5's own flagged spot-check, re-confirmed)")
print("=" * 100)
for name, w in SCHEMES.items():
    wn = weighted_total(SCORES['Nordic Social Democracy'], w)
    wi = weighted_total(SCORES['Integral'], w)
    mx = max_possible(w)
    print(f"  {name:<38} Nordic {wn/mx*100:5.1f}%   Integral {wi/mx*100:5.1f}%   "
          f"{'Integral ahead' if wi>wn else ('Nordic ahead' if wn>wi else 'TIE')}")
