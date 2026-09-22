#!/usr/bin/env python3
"""
run_a4_full_rerun_23.py -- Session 25
=====================================
Re-runs the Paper's Appendix A.4 weighting-robustness check on the complete
canonical corpus (23 systems after the Session 25 insertion). It is Session
20's run_a4_full_rerun_20.py (20 systems) -- itself a generalization of
Session 12's run_a4_full_rerun.py (15 systems) -- with its corpus-specific
assertions updated to the 23-system corpus. Every count is computed from the
corpus; the expected values are written in so that any change to the data
fails loudly (decision D3(b)). run_a4_full_rerun_20.py stays on file,
unedited, and runs against the pinned Session 20 snapshot.

It re-derives no scores. SCORES, SCHEMES, and the helper functions are
imported from the unmodified canonical neec_weighting_robustness_analysis_v2.py,
and both of that script's self-checks must pass first. Session 12 had to skip
verify_unchanged_from_legacy(); baseline_weighting_script.py (reconstructed
in Session 12) is now on the mount, so this run includes it.

Beyond Session 12's ranking, tier, and spot-check tables, this run adds:
  * how every exact equal-weighting tie behaves under each alternative scheme,
    with a one-line algebraic reason for each (the "single-factor identity"
    below, checked for every ordered pair);
  * an exhaustive Theorem 5 confirmation: every strict-dominance pair in the
    corpus, under every scheme, not only the spot-checked pairs;
  * the dominance flag for Paper v1.4's spot-check table, recomputed.

Each alternative scheme multiplies one criterion set K by a factor k and
leaves the rest at 1: Material-Security (K = Domain 1, k = 2),
Feasibility-Discounted (K = Domain 5, k = 0.5), Crisis-Risk (K = {C1.4,
C4.2}, k = 3). For any two systems a and b, with D the difference of their
equal-weighted totals and D_K the difference of their sums over K,
    weighted(a) - weighted(b) = D + (k - 1) * D_K.
For a tied pair (D = 0) the tie survives exactly when D_K = 0; otherwise it
breaks toward the system stronger on K when k > 1, and toward the system
weaker on K when k < 1.

Run: python3 run_a4_full_rerun_23.py   (portable; prints file names only)
"""
import importlib.util
import os
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = (HERE, os.getcwd(), "/home/claude", "/home/claude/neec",
               "/mnt/user-data/outputs", "/mnt/project")


def locate(name):
    for d in SEARCH_DIRS:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: could not locate {name} in {SEARCH_DIRS}")


spec = importlib.util.spec_from_file_location("v2script", locate("neec_weighting_robustness_analysis_v2.py"))
v2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v2)

SCORES, SCHEMES, ALL_CRITS = v2.SCORES, v2.SCHEMES, v2.ALL_CRITS
weighted_total, max_possible = v2.weighted_total, v2.max_possible
failure_count, tier, dominates = v2.failure_count, v2.tier, v2.dominates
SYSTEMS = list(SCORES)
N = len(SYSTEMS)
EQ = 'Equal (baseline)'
ALTS = [n for n in SCHEMES if n != EQ]
SHORT = {EQ: 'Equal', ALTS[0]: 'Material-Security x2',
         ALTS[1]: 'Feasibility-Discounted x0.5', ALTS[2]: 'Crisis-Risk x3'}
SINGLE_FACTOR = {ALTS[0]: (v2.D1_CRITS, 2.0), ALTS[1]: (v2.D5_CRITS, 0.5),
                 ALTS[2]: (['C1.4', 'C4.2'], 3.0)}

assert v2.verify_transcription(verbose=False), "Transcription check failed -- STOP"
assert v2.verify_unchanged_from_legacy(locate("baseline_weighting_script.py"), verbose=False), \
    "Legacy-unchanged check failed -- STOP"
print(f"Loaded {N} systems from neec_weighting_robustness_analysis_v2.py.")
print("verify_transcription(): PASS.  verify_unchanged_from_legacy(): PASS (baseline_weighting_script.py present).")

CHECKS = []


def check(label, cond):
    CHECKS.append((label, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


def wt(s, name):
    return weighted_total(SCORES[s], SCHEMES[name])


def pct(s, name):
    return wt(s, name) / max_possible(SCHEMES[name]) * 100


# ---------------------------------------------------------------------------
# 1. Scheme definitions check (every alternative is single-factor)
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("1. SCHEMES")
print("=" * 100)
for name in SCHEMES:
    print(f"  {name:<40} max possible = {max_possible(SCHEMES[name]):.1f}")
for name, (K, k) in SINGLE_FACTOR.items():
    w = SCHEMES[name]
    check(f"{SHORT[name]} is single-factor: {len(K)} criteria x{k:g}, all others x1",
          all(w[c] == (k if c in K else 1.0) for c in ALL_CRITS))

# ---------------------------------------------------------------------------
# 2. Rankings under each scheme (ordinal; ties keep canonical order, marked '=')
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print(f"2. RANKINGS UNDER EACH SCHEME, ALL {N} SYSTEMS")
print("   Ordinal positions; equal weighted totals keep canonical order and are marked '='.")
print("   'comp' is the competition rank (tied systems share the best position), used for movements.")
print("=" * 100)
ORDER, COMP, TIED = {}, {}, {}
for name in SCHEMES:
    rows = sorted(SYSTEMS, key=lambda s: -wt(s, name))
    ORDER[name] = {s: i for i, s in enumerate(rows, 1)}
    COMP[name] = {s: 1 + sum(wt(t, name) > wt(s, name) for t in SYSTEMS) for s in SYSTEMS}
    TIED[name] = {s: sum(wt(t, name) == wt(s, name) for t in SYSTEMS) > 1 for s in SYSTEMS}
    print(f"\n--- {name} (max possible = {max_possible(SCHEMES[name]):.1f}) ---")
    for s in rows:
        f = failure_count(SCORES[s])
        print(f"  {ORDER[name][s]:2d}{'=' if TIED[name][s] else ' '} (comp {COMP[name][s]:2d}) "
              f"{s:<36} {wt(s, name):6.2f}  ({pct(s, name):5.1f}%)  [{f} fail, {tier(f)}]")

# ---------------------------------------------------------------------------
# 3. Rank movements (competition ranks, so ties create no artificial movement)
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("3. RANK MOVEMENT vs. EQUAL WEIGHTING (competition ranks; + means a worse position)")
print("=" * 100)
for name in ALTS:
    moves = sorted(((COMP[name][s] - COMP[EQ][s], s) for s in SYSTEMS),
                   key=lambda m: (-abs(m[0]), ORDER[EQ][m[1]]))
    print(f"\n--- {SHORT[name]}: every system that moves ---")
    for d, s in moves:
        if d:
            print(f"  {s:<36} {COMP[EQ][s]:2d} -> {COMP[name][s]:2d}  ({d:+d})")
    top2 = [s for s in SYSTEMS if COMP[name][s] <= 2]
    print(f"  Positions 1-2 under this scheme: {sorted(top2, key=lambda s: COMP[name][s])}")
check("CCO-PTF-CIP-SZH and Participatory Economics hold positions 1 and 2 under all four schemes",
      all(COMP[n]['CCO-PTF-CIP-SZH'] == 1 and COMP[n]['Participatory Economics'] == 2 for n in SCHEMES))
check("Libertarian Minarchism is last under all four schemes",
      all(COMP[n]['Libertarian Minarchism'] == N for n in SCHEMES))

# ---------------------------------------------------------------------------
# 4. Tier invariance
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("4. ADEQUACY TIER (failure-count based; invariant to any weighting by construction)")
print("=" * 100)
for s in sorted(SYSTEMS, key=lambda s: (failure_count(SCORES[s]), ORDER[EQ][s])):
    f = failure_count(SCORES[s])
    print(f"  {s:<36} {f:2d} failures -> {tier(f)}")

# ---------------------------------------------------------------------------
# 5. Single-factor identity, checked for every ordered pair and scheme
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("5. SINGLE-FACTOR IDENTITY: weighted(a) - weighted(b) = D + (k - 1) * D_K")
print("=" * 100)


def delta(a, b, crits):
    return sum(SCORES[a][c] - SCORES[b][c] for c in crits)


ok = True
for name, (K, k) in SINGLE_FACTOR.items():
    for a in SYSTEMS:
        for b in SYSTEMS:
            lhs = wt(a, name) - wt(b, name)
            rhs = delta(a, b, ALL_CRITS) + (k - 1) * delta(a, b, K)
            ok = ok and abs(lhs - rhs) < 1e-9
check(f"Identity holds exactly for all {N * N} ordered pairs under all three alternative schemes", ok)

# ---------------------------------------------------------------------------
# 6. Every exact equal-weighting tie, under every scheme
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("6. EXACT EQUAL-WEIGHTING TIES UNDER EACH ALTERNATIVE SCHEME")
print("=" * 100)
TIE_PAIRS = [(a, b) for a, b in combinations(SYSTEMS, 2)
             if abs(wt(a, EQ) - wt(b, EQ)) < 1e-9]
survivals = {}
for a, b in TIE_PAIRS:
    print(f"\n  {a}  vs  {b}   (both {wt(a, EQ):.1f}/26; failures "
          f"{failure_count(SCORES[a])} vs {failure_count(SCORES[b])})")
    for name, (K, k) in SINGLE_FACTOR.items():
        dk = delta(a, b, K)
        wa, wb = wt(a, name), wt(b, name)
        if abs(wa - wb) < 1e-9:
            verdict = "TIE SURVIVES"
        else:
            verdict = f"{a if wa > wb else b} ahead"
        survivals[(a, b, name)] = abs(wa - wb) < 1e-9
        print(f"    {SHORT[name]:<28} {wa:6.2f} vs {wb:6.2f}   D_K = {dk:+.1f}   {verdict}")
check("A tie survives a scheme exactly when D_K = 0 (all tied pairs, all schemes)",
      all(survivals[(a, b, n)] == (abs(delta(a, b, SINGLE_FACTOR[n][0])) < 1e-9)
          for a, b in TIE_PAIRS for n in ALTS))
check(f"{len(TIE_PAIRS)} tied pairs in the corpus (Session 20: 7)", len(TIE_PAIRS) == 11)
SWF, SG, CN = 'Sovereign Wealth Fund Statism', 'State Capitalism / Singapore', 'State Capitalism / China'
QA, IF, OS = 'State Capitalism / Qatar', 'Islamic Finance / Profit-Sharing Banking', 'Ostrom-Style Commons Governance'
GEO, UBS = 'Georgism / Land Value Tax', 'Universal Basic Services'
check("SWF Statism / Singapore tie: breaks only under Material-Security (Singapore ahead); "
      "survives Feasibility-Discounted and Crisis-Risk",
      not survivals[(SWF, SG, ALTS[0])] and wt(SG, ALTS[0]) > wt(SWF, ALTS[0])
      and survivals[(SWF, SG, ALTS[1])] and survivals[(SWF, SG, ALTS[2])])
check("UBI / Mutual Credit-LETS tie: breaks under all three alternatives, UBI ahead each time "
      "(Session 12's finding, unchanged)",
      all(not survivals[('Universal Basic Income', 'Mutual Credit / LETS', n)]
          and wt('Universal Basic Income', n) > wt('Mutual Credit / LETS', n) for n in ALTS))
check("Georgism / UBS tie: Georgism ahead under Material-Security and Feasibility-Discounted; "
      "survives Crisis-Risk",
      all(wt('Georgism / Land Value Tax', n) > wt('Universal Basic Services', n) for n in ALTS[:2])
      and survivals[('Georgism / Land Value Tax', 'Universal Basic Services', ALTS[2])])
check("China / Centrally Planned Socialism tie survives Material-Security only",
      survivals[('Centrally Planned Socialism', CN, ALTS[0])]
      and not survivals[('Centrally Planned Socialism', CN, ALTS[1])]
      and not survivals[('Centrally Planned Socialism', CN, ALTS[2])])
check("The three-way 10.0 tie fully separates under Feasibility-Discounted and Crisis-Risk",
      all(len({wt(s, n) for s in ('Centrally Planned Socialism', 'Stakeholder Capitalism', CN)}) == 3
          for n in ALTS[1:]))
check("Singapore ranks strictly above SWF Statism only under Material-Security",
      [n for n in SCHEMES if wt(SG, n) > wt(SWF, n)] == [ALTS[0]])
# Session 25: the two three-way ties the insertion created (13.5 and 14.0).
check("Georgism / Islamic finance tie: survives Material-Security (D_K = 0); Georgism ahead under "
      "Feasibility-Discounted and Crisis-Risk",
      survivals[(GEO, IF, ALTS[0])] and all(wt(GEO, n) > wt(IF, n) for n in ALTS[1:]))
check("UBS / Islamic finance tie: Islamic finance ahead under Material-Security only; UBS ahead under "
      "Feasibility-Discounted and Crisis-Risk",
      wt(IF, ALTS[0]) > wt(UBS, ALTS[0]) and all(wt(UBS, n) > wt(IF, n) for n in ALTS[1:]))
check("Three-way 13.5 tie: Material-Security leaves Georgism = IF (15.50) above UBS; Feasibility-Discounted "
      "separates it fully (Georgism > UBS > IF); Crisis-Risk leaves Georgism = UBS (15.50) above IF",
      wt(GEO, ALTS[0]) == wt(IF, ALTS[0]) == 15.5 > wt(UBS, ALTS[0])
      and wt(GEO, ALTS[1]) > wt(UBS, ALTS[1]) > wt(IF, ALTS[1])
      and wt(GEO, ALTS[2]) == wt(UBS, ALTS[2]) == 15.5 > wt(IF, ALTS[2]))
check("SWF Statism / Ostrom and Singapore / Ostrom ties break under all three alternatives: Ostrom behind under "
      "Material-Security and Feasibility-Discounted, ahead under Crisis-Risk",
      all(not survivals[(x, OS, n)] for x in (SWF, SG) for n in ALTS)
      and all(wt(x, n) > wt(OS, n) for x in (SWF, SG) for n in ALTS[:2])
      and all(wt(OS, ALTS[2]) > wt(x, ALTS[2]) for x in (SWF, SG)))
check("Three-way 14.0 tie: Material-Security Singapore > SWF > Ostrom (18.00, 16.50, 16.00); Feasibility-"
      "Discounted SWF = Singapore (12.25) > Ostrom; Crisis-Risk Ostrom (16.00) > SWF = Singapore (15.00)",
      (wt(SG, ALTS[0]), wt(SWF, ALTS[0]), wt(OS, ALTS[0])) == (18.0, 16.5, 16.0)
      and wt(SWF, ALTS[1]) == wt(SG, ALTS[1]) == 12.25 > wt(OS, ALTS[1])
      and wt(OS, ALTS[2]) == 16.0 > wt(SWF, ALTS[2]) == wt(SG, ALTS[2]) == 15.0)

SCHEME_TIES = [(n, a, b) for n in ALTS for a, b in combinations(SYSTEMS, 2)
               if abs(wt(a, n) - wt(b, n)) < 1e-9 and abs(wt(a, EQ) - wt(b, EQ)) > 1e-9]
print("\n  Ties that exist only under an alternative scheme:")
for n, a, b in SCHEME_TIES:
    print(f"    {SHORT[n]:<28} {a} = {b}  ({wt(a, n):.2f}; equal-weighted {wt(a, EQ):.1f} vs {wt(b, EQ):.1f})")
check("Exactly eight scheme-specific ties (Session 20: four): Status Quo/Doughnut, FALC/Ostrom and Mutual "
      "Credit/SWF Statism (Material-Security); Status Quo/China and Georgism/Ostrom (Feasibility-Discounted); "
      "Market Socialism/MMT+JG, Stakeholder/Qatar and Doughnut/IF (Crisis-Risk)",
      [(SHORT[n], a, b) for n, a, b in SCHEME_TIES] == [
          (SHORT[ALTS[0]], 'Status Quo Market Capitalism', 'Doughnut Economics'),
          (SHORT[ALTS[0]], 'Fully Automated Luxury Communism', OS),
          (SHORT[ALTS[0]], 'Mutual Credit / LETS', SWF),
          (SHORT[ALTS[1]], 'Status Quo Market Capitalism', CN),
          (SHORT[ALTS[1]], GEO, OS),
          (SHORT[ALTS[2]], 'Market Socialism', 'MMT + Job Guarantee'),
          (SHORT[ALTS[2]], 'Stakeholder Capitalism', QA),
          (SHORT[ALTS[2]], 'Doughnut Economics', IF)])

# ---------------------------------------------------------------------------
# 7. Theorem 5, exhaustively: every dominance pair under every scheme
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("7. THEOREM 5, EXHAUSTIVE: every strict-dominance pair, every scheme")
print("=" * 100)
DOM_PAIRS = [(a, b) for a in SYSTEMS for b in SYSTEMS if a != b and dominates(a, b)]
for a, b in DOM_PAIRS:
    print(f"  {a}  >  {b}   " + "  ".join(f"{wt(a, n):5.2f}>{wt(b, n):5.2f}" for n in SCHEMES))
check(f"All {len(DOM_PAIRS)} dominance pairs keep a strictly higher weighted total under all four schemes",
      all(wt(a, n) > wt(b, n) for a, b in DOM_PAIRS for n in SCHEMES))
check("14 dominance pairs in the corpus (Session 20: 11)", len(DOM_PAIRS) == 14)

# ---------------------------------------------------------------------------
# 8. Spot-check table (Paper v1.4 pairs, dominance flag recomputed, plus new pairs)
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("8. DOMINANCE-PAIR SPOT CHECK (flag recomputed; True = guaranteed by Theorem 5)")
print("=" * 100)
V14_PAIRS = [  # (pair, flag as printed in Paper v1.4's Appendix A.4 table)
    (('CCO-PTF-CIP-SZH', 'Status Quo Market Capitalism'), True),
    (('CCO-PTF-CIP-SZH', 'MMT + Job Guarantee'), True),
    (('CCO-PTF-CIP-SZH', 'Georgism / Land Value Tax'), True),
    (('Participatory Economics', 'Stakeholder Capitalism'), True),
    (('CCO-PTF-CIP-SZH', 'Nordic Social Democracy'), False),
    (('Mutual Credit / LETS', 'Georgism / Land Value Tax'), False),
]
NEW_PAIRS = [('CCO-PTF-CIP-SZH', 'Doughnut Economics'), ('CCO-PTF-CIP-SZH', 'Universal Basic Services'),
             ('CCO-PTF-CIP-SZH', SWF), ('CCO-PTF-CIP-SZH', CN), ('CCO-PTF-CIP-SZH', SG),
             (SG, CN), (SG, SWF), ('Universal Basic Services', 'Georgism / Land Value Tax'),
             # Session 25 additions (the canonical script's new spot-check pairs)
             ('CCO-PTF-CIP-SZH', QA), ('CCO-PTF-CIP-SZH', IF), ('CCO-PTF-CIP-SZH', OS), (SG, QA), (CN, QA),
             (IF, 'Stakeholder Capitalism'), (IF, GEO), (IF, UBS), (OS, SWF), (OS, SG), (OS, IF)]
for (a, b), printed in V14_PAIRS + [(p, None) for p in NEW_PAIRS]:
    d = dominates(a, b)
    note = "" if printed is None else ("  (v1.4 label agrees)" if printed == d else
                                       f"  <<< Paper v1.4 prints {printed}")
    print(f"  {a}  vs  {b}   dominance: {d}{note}")
    print("    " + "   ".join(f"{SHORT[n]}: {wt(a, n):.2f} {'>' if wt(a, n) > wt(b, n) else ('=' if wt(a, n) == wt(b, n) else '<')} {wt(b, n):.2f}"
                              for n in SCHEMES))
mismatch = [(a, b) for (a, b), printed in V14_PAIRS if printed != dominates(a, b)]
pe, sh = SCORES['Participatory Economics'], SCORES['Stakeholder Capitalism']
blockers = [c for c in ALL_CRITS if sh[c] > pe[c]]
print(f"\n  Paper v1.4 table rows whose dominance label disagrees with the computation: {mismatch}")
print(f"  Criteria where Stakeholder Capitalism outscores Participatory Economics: "
      f"{[(c, pe[c], sh[c]) for c in blockers]}  (ParEcon, Stakeholder)")
check("Exactly one v1.4 label is wrong: Participatory Economics does NOT dominate Stakeholder Capitalism",
      mismatch == [('Participatory Economics', 'Stakeholder Capitalism')] and blockers == ['C4.5', 'C5.2', 'C5.3'])
check("The v1.4 row's weighted comparisons are nonetheless right (ParEcon ahead under all four schemes)",
      all(wt('Participatory Economics', n) > wt('Stakeholder Capitalism', n) for n in SCHEMES))

# ---------------------------------------------------------------------------
# 9. Nordic / Integral (continuity with Section 12.5 and Session 12)
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("9. NORDIC vs INTEGRAL under all four schemes")
print("=" * 100)
for n in SCHEMES:
    a, b = pct('Nordic Social Democracy', n), pct('Integral', n)
    print(f"  {SHORT[n]:<28} Nordic {a:5.1f}%   Integral {b:5.1f}%   "
          f"{'Integral ahead' if b > a else ('Nordic ahead' if a > b else 'TIE')}")
check("Nordic ahead only under Material-Security; Integral ahead under the other two alternatives",
      pct('Nordic Social Democracy', ALTS[0]) > pct('Integral', ALTS[0])
      and all(pct('Integral', n) > pct('Nordic Social Democracy', n) for n in ALTS[1:]))

# ---------------------------------------------------------------------------
# 10. Markdown tables for the scratch write-up
# ---------------------------------------------------------------------------
print("\n" + "=" * 100)
print("10. MARKDOWN TABLES (generated; pasted into the scratch document verbatim)")
print("=" * 100)
print("<<<RANK_TABLE")
print("| System | " + " | ".join(SHORT[n] for n in SCHEMES) + " | Failures | Tier |")
print("|---|" + "---|" * (len(SCHEMES) + 2))
for s in sorted(SYSTEMS, key=lambda s: ORDER[EQ][s]):
    cells = [f"{ORDER[n][s]}{'=' if TIED[n][s] else ''} ({pct(s, n):.1f}%)" for n in SCHEMES]
    f = failure_count(SCORES[s])
    print(f"| {s} | " + " | ".join(cells) + f" | {f} | {tier(f)} |")
print(">>>")
print("<<<TIE_TABLE")
print("| Tied pair (equal-weighted total) | " + " | ".join(SHORT[n] for n in ALTS) + " |")
print("|---|" + "---|" * len(ALTS))
for a, b in TIE_PAIRS:
    cells = []
    for n in ALTS:
        wa, wb = wt(a, n), wt(b, n)
        dk = delta(a, b, SINGLE_FACTOR[n][0])
        cells.append(f"tie holds ({wa:.2f}); D_K = 0" if abs(wa - wb) < 1e-9 else
                     f"{(a if wa > wb else b).split(' (')[0]} ahead ({max(wa, wb):.2f} vs {min(wa, wb):.2f}); D_K = {dk:+.1f}")
    print(f"| {a} vs. {b} ({wt(a, EQ):.1f}) | " + " | ".join(cells) + " |")
print(">>>")
print("<<<PAIR_TABLE")
print("| Pair | Dominance | " + " | ".join(SHORT[n] for n in SCHEMES) + " |")
print("|---|---|" + "---|" * len(SCHEMES))
for (a, b) in [p for p, _ in V14_PAIRS] + NEW_PAIRS:
    d = dominates(a, b)
    lab = "**True** (guaranteed)" if d else ("False (tie)" if wt(a, EQ) == wt(b, EQ) else "False (non-dominated)")
    cells = [f"{wt(a, n):.2f} {'>' if wt(a, n) > wt(b, n) else ('=' if wt(a, n) == wt(b, n) else '<')} {wt(b, n):.2f}"
             for n in SCHEMES]
    print(f"| {a} vs. {b} | {lab} | " + " | ".join(cells) + " |")
print(">>>")

print("\n" + "=" * 100)
bad = [label for label, ok in CHECKS if not ok]
print(f"SUMMARY: {len(CHECKS) - len(bad)}/{len(CHECKS)} checks pass.")
if bad:
    for label in bad:
        print(f"  FAILED: {label}")
    sys.exit(1)
