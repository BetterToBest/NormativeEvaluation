#!/usr/bin/env python3
"""
triage_s52.py -- NEEC rescoring pass, stage 2: the consequence triage (decision 52.7, W6)
=========================================================================================
Session 52. Which of the units the pass has not yet read could, on its own, change an entry's failure count, its
adequacy tier or its rank? Written as a script so that groups can be read in that order and any unit carried forward
unread can be named and disclosed. It changes no file and no score. State: the pass cumulatively through group 2.1
(pass_common.Pass), on the published 26-criterion structure; the 69 new units (C2.6, C3.6, C4.6) have no score and are
counted apart.

THE REACH OF A UNIT (the widest the pass's rules allow; a screen, not a forecast; the triage's own assumption, 52.7)
  already re-estimated by the pass, or class W or U     fixed
  class D, score s                                       any score above s (D units can only keep or rise)
  class I or M, score 0.5 or 0.0                         any other score (v2.0 can change failure counts and tiers)
  class I or M, score 1.0 (published, not yet read)      0.5 only (D28(f): a 1.0 that does not stand becomes 0.5)
A unit is CONSEQUENTIAL if some score in its reach, with every other score held as it is now, changes its entry's
  failure count (a score of 0.0 gained or lost),
  adequacy tier (Potentially Adequate to 2 failures, Partially to 5, Structurally from 6; as the harness and the
  published corpus define them, here applied to the 26 published criteria),
  or rank (rank = 1 + the entries with a higher total; ties share a rank, as the pass's ranks()).
RANK DISPLACEMENT is the most places the unit's entry can move that way. Because a 0.5 or 0.0 can reach a 0.0 or a 1.0,
almost every in-play unit is failure-capable and rank-capable; what separates them is the tier and the displacement,
so groups are ordered by (tier-capable units, rank displacement, units), and the units that can change none of the
three are the only ones a carry-forward could skip without a stated reason.

Usage: python3 triage_s52.py   (reads what pass_common.py reads; writes nothing)
Prints file names only. Deterministic.
"""
import sys

import pass_common as pc

NEW = ("C2.6", "C3.6", "C4.6")
READ = {"I": "evidence re-check (class I; the evidence cache of W5)", "M": "judgment re-read (class M)",
        "D": "rises only (class D)"}


def reach(p, v, cls, c, k):
    s = v[c][k]
    if (c, k) in p.merged or cls[k] in "WU":
        return []
    if cls[k] == "D":
        return [x for x in (0.0, 0.5, 1.0) if x > s]
    return [x for x in (0.0, 0.5, 1.0) if x != s and not (s == 1.0 and x == 0.0)]


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
    p = pc.Pass()
    v, T, F = p.vsteps[-1], p.steps[-1]["total"], p.steps[-1]["fail"]
    R = pc.ranks(T)
    cls = {k: p.v2[k]["revision"]["cls"] for k in p.v2ids}
    print(f"NEEC rescoring pass, stage 2: the consequence triage (W6, decision 52.7); state through group 2.1")
    print("inputs: " + ", ".join((pc.CRITERIA, pc.CRIT44, pc.CORPUS)) + ", " + ", ".join(m for _, _, m, _ in pc.PARTS) + "\n")

    # [1] population ------------------------------------------------------------------------------------------------
    print("[1] POPULATION (units = 23 entries x 29 v2.0 criteria)")
    counts = {c: sum(1 for k in p.v2ids if cls[k] == c) * len(p.order) for c in "WDIMUN"}
    check(counts == {"W": 115, "D": 46, "I": 161, "M": 184, "U": 92, "N": 69} and sum(counts.values()) == 667,
          "classes by units: W 115, D 46, I 161, M 184, U 92, N 69 (667), as the criteria record's section 7")
    units = [(c, k) for c in p.order for k in p.cids]
    inplay = [(c, k) for c, k in units if reach(p, v, cls, c, k)]
    done = [x for x in units if x in p.merged]
    check(len(done) == len(p.merged) == 152 and len(units) == 598,
          f"{len(done)} of the 598 units on the published 26 criteria are re-estimated; the other {598 - len(done)} are not")
    fixed = 598 - len(done) - len(inplay)
    print(f"  not yet read: {len(inplay)} in play (class D {sum(1 for _, k in inplay if cls[k] == 'D')}, "
          f"I {sum(1 for _, k in inplay if cls[k] == 'I')}, M {sum(1 for _, k in inplay if cls[k] == 'M')}); "
          f"{fixed} fixed by class (W or U); and the {counts['N']} new units, unscored")

    # [2] consequence of each unit ----------------------------------------------------------------------------------
    print("\n[2] WHAT EACH UNIT COULD CHANGE ON ITS OWN (all other scores held)")
    info = {}
    for c, k in inplay:
        s, vs = v[c][k], reach(p, v, cls, c, k)
        d_fail = {x: (x == 0.0) - (s == 0.0) for x in vs}
        tier_ch = any(pc.tier(F[c] + d_fail[x]) != pc.tier(F[c]) for x in vs)
        fail_ch = any(d_fail[x] != 0 for x in vs)
        disp = max(abs(1 + sum(1 for d in p.order if d != c and T[d] > T[c] - s + x) - R[c]) for x in vs)
        info[(c, k)] = (tier_ch, fail_ch, disp)
    n_tier = sum(1 for t in info.values() if t[0])
    n_fail = sum(1 for t in info.values() if t[1])
    n_rank = sum(1 for t in info.values() if t[2] > 0)
    none = sorted(x for x, t in info.items() if not t[0] and not t[1] and t[2] == 0)
    print(f"  of {len(inplay)}: {n_fail} could change a failure count, {n_tier} an adequacy tier, {n_rank} a rank; "
          f"{len(none)} could change none of the three")
    brute = sum(1 for (c, k) in inplay for x in reach(p, v, cls, c, k)
                if pc.tier(F[c] + (x == 0.0) - (v[c][k] == 0.0)) != pc.tier(F[c]))
    check(n_tier == sum(1 for (c, k) in inplay if any(
        pc.tier(F[c] + (x == 0.0) - (v[c][k] == 0.0)) != pc.tier(F[c]) for x in reach(p, v, cls, c, k))) and brute >= n_tier,
          "the tier screen reproduced by a second computation")
    first = [c for c in p.order if T[c] == max(T.values())]
    lead = [x for x in inplay if any(
        [d for d in p.order if (T[d] if d != x[0] else T[d] - v[x[0]][x[1]] + y) == max(
            T[e] if e != x[0] else T[e] - v[x[0]][x[1]] + y for e in p.order)] != first
        for y in reach(p, v, cls, *x))]
    check(len(first) == 1, f"first place is {first[0]} at {pc.f1(T[first[0]])}; the next total is "
                          f"{pc.f1(sorted(T.values())[-2])}")
    print(f"  units that alone could change who is first: {len(lead)}" + (f" ({', '.join(c + ' ' + k for c, k in lead)})" if lead else ""))
    print("  the units that could change none of the three (the only candidates to carry forward without a reason): "
          + (", ".join(f"{c} {k}" for c, k in none) or "none"))

    # [3] entries -----------------------------------------------------------------------------------------------------
    print("\n[3] ENTRIES (published structure; total, failures, tier now; units in play; those that could change the tier)")
    rows = ["| Entry | Total (rank) | Failures | Tier | In play | Tier-capable alone | To a worse tier: needs / can | "
            "To a better tier: needs / can |", "|---|---:|---:|---|---:|---:|---|---|"]
    stuck, stuck_all = [], []
    for c in pc.order_codes(p.names, p.steps[-1]):
        mine = [x for x in inplay if x[0] == c]
        fall = sum(1 for x in mine if v[c][x[1]] > 0.0 and 0.0 in reach(p, v, cls, *x))
        rise = sum(1 for x in mine if v[c][x[1]] == 0.0)
        f = F[c]
        down = 3 - f if f <= 2 else (6 - f if f <= 5 else None)
        up = f - 2 if 3 <= f <= 5 else (f - 5 if f >= 6 else None)
        if not any(info[x][0] for x in mine):
            stuck.append(c)
        if not ((down is not None and fall >= down) or (up is not None and rise >= up)):
            stuck_all.append(c)
        rows.append(f"| {c} | {pc.f1(T[c])} ({R[c]}) | {f} | {pc.tier(f)} | {len(mine)} | "
                    f"{sum(1 for x in mine if info[x][0])} | {'' if down is None else f'{down} / {fall}'} | "
                    f"{'' if up is None else f'{up} / {rise}'} |")
    print("\n".join(rows))
    print(f"  entries with no tier-capable unit alone: {', '.join(stuck) or 'none'}; entries whose tier cannot change "
          f"even if every unit in play moved the worst way for it: {', '.join(stuck_all) or 'none'}")

    # [4] criteria: the order of groups ------------------------------------------------------------------------------
    print("\n[4] GROUPS BY CRITERION, IN THE ORDER TO READ THEM (tier-capable units, then rank displacement, then units)")
    crit_rows = []
    for k in p.cids:
        mine = [x for x in inplay if x[1] == k]
        if mine:
            crit_rows.append((k, cls[k], len(mine), sum(1 for x in mine if info[x][0]), sum(info[x][2] for x in mine),
                              sum(1 for x in mine if info[x][1])))
    crit_rows.sort(key=lambda r: (-r[3], -r[4], -r[2], p.cids.index(r[0])))
    rows = ["| Order | Criterion | Class | Reading | Units in play | Tier-capable | Rank displacement (sum) | Failure-capable |",
            "|---:|---|---|---|---:|---:|---:|---:|"]
    for i, (k, cl, n, t, d, f) in enumerate(crit_rows, 1):
        rows.append(f"| {i} | {k} {p.v2[k]['name']} | {cl} | {READ[cl]} | {n} | {t} | {d} | {f} |")
    print("\n".join(rows))
    check(sum(r[2] for r in crit_rows) == len(inplay) and sum(r[3] for r in crit_rows) == n_tier,
          "the criteria's units and tier-capable units sum to the totals above")
    print(f"\n[5] THE {counts['N']} NEW UNITS (C2.6, C3.6, C4.6; 23 each): no score exists, so none can be carried forward; each "
          "entry gains three criteria, so every entry's failure count and total on the 29 can change by up to 3 failures "
          "and 3.0 points. They are the one certain change to the corpus' results.")
    check(all(k in p.v2 and cls[k] == "N" for k in NEW) and not any(k in p.cids for k in NEW),
          "the new criteria are class N and outside the published 26")
    top = crit_rows[0]
    print(f"\nNEXT GROUP FROM THE TRIAGE: {top[0]} {p.v2[top[0]]['name']} ({top[1]}, {top[2]} units, {top[3]} tier-capable); "
          f"model by the reading: {'Opus 5.5 high' if top[1] == 'M' else 'Sonnet 5.5 for the evidence, Opus 5.5 high for the readings'}.")
    print("\nCONSEQUENCE TRIAGE COMPUTED." if ok else "\nCONSEQUENCE TRIAGE: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
