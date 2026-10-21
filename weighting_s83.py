#!/usr/bin/env python3
"""
weighting_s83.py -- NEEC: the weighting robustness of the v2.0 standing, after the adjudication (Session 83, ledger S65)
=====================================================================================================================
STATE.md (Next work, item 11) asks for the weighting robustness analysis to be rerun on the final scores before they are
frozen, since first place rests on a margin of 0.5. The canonical script, neec_weighting_robustness_analysis_v2.py, is the
v1 analysis (26 criteria, its own transcribed scores) and stays as published; this companion applies the same four weighting
schemes (equal; Domain 1 doubled; Domain 5 halved; C1.4 and C4.2 tripled) to the v2.0 corpus on the 29 criteria, and adds
two tests of first place: dropping each criterion in turn, and resolving every registered close call against the leader and
for the runner-up.

Four states (since Session 84): Session 79 (neec_corpus_v2_s79_snapshot.json), the adjudicated scores of Session 83
(neec_corpus_v2_s83_snapshot.json), the scores of Session 84 with the owner's items applied (neec_corpus_v2.json), and the
Session 84 scores on the readings alone, with the owner's raises (decisions 58.1, 79.1 to 79.4) reversed
(apply_owner_s84.READINGS; never written). Session 83's third state, the four owner items applied as the adjudication reads
them, is now written: it is the Session 84 state less Participatory Economics' C1.2b (decision 84.4).

Usage: python3 weighting_s83.py   (prints the tables; writes nothing). Deterministic.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402


def load(name):
    return json.load(open(os.path.join(HERE, name), encoding="utf-8"))


CRIT = load("criteria.json")
DOMAINS = {d["id"]: d["criteria"] for d in CRIT["domains"]}
ORDER = [c for d in CRIT["domains"] for c in d["criteria"]]


def schemes():
    eq = {c: 1.0 for c in ORDER}
    d1 = dict(eq, **{c: 2.0 for c in DOMAINS["D1"]})
    d5 = dict(eq, **{c: 0.5 for c in DOMAINS["D5"]})
    cr = dict(eq, **{"C1.4": 3.0, "C4.2": 3.0})
    return {"Equal (baseline)": eq, "Material security (D1 x2)": d1, "Feasibility discounted (D5 x0.5)": d5,
            "Crisis risk (C1.4, C4.2 x3)": cr}


def vectors(name):
    return {e["code"]: e["vector"] for e in load(name)["entries"]}, {e["code"]: e["display_name"] for e in load(name)["entries"]}


def readings_alone(vec):
    with open(os.devnull, "w") as dn:
        stdout, sys.stdout = sys.stdout, dn
        try:
            a84 = pc.load("apply_owner_s84", "apply_owner_s84.py")
        finally:
            sys.stdout = stdout
    return a84.without(vec, a84.READINGS)


def ranked(vec, w):
    tot = {c: sum(v[k] * w[k] for k in ORDER) for c, v in vec.items()}
    mx = sum(w.values())
    order = sorted(tot, key=lambda c: (-tot[c], c))
    return tot, mx, order


def main():
    v79, names = vectors("neec_corpus_v2_s79_snapshot.json")
    vadj, _ = vectors("neec_corpus_v2_s83_snapshot.json")
    v84, _ = vectors("neec_corpus_v2.json")
    valone = readings_alone(v84)
    b83 = {b["code"]: b for b in load("summary_blocks_v2_s83_snapshot.json")}
    b84 = {b["code"]: b for b in load("summary_blocks_v2.json")}
    states = [("Session 79", v79), ("Adjudicated (Session 83)", vadj), ("Session 84, the owner's items applied", v84),
              ("Session 84, on the readings alone", valone)]
    blocks_of = {"Adjudicated (Session 83)": b83}
    print("weighting_s83.py: the four weighting schemes on the v2.0 corpus (29 criteria), four states\n")
    firsts = {}
    for label, vec in states:
        print(f"== {label}")
        for sname, w in schemes().items():
            tot, mx, order = ranked(vec, w)
            top = order[:6]
            lead = [c for c in order if tot[c] == tot[order[0]]]
            margin = tot[order[0]] - max(tot[c] for c in order if c not in lead) if len(lead) < len(order) else 0.0
            firsts[(label, sname)] = (tuple(lead), margin)
            print(f"  {sname:<34} first {' and '.join(lead)} by {margin:.2f}; top six: "
                  + ", ".join(f"{c} {100 * tot[c] / mx:.1f}%" for c in top))
        print()
    print("== First place under each scheme")
    for label, _ in states:
        leads = {firsts[(label, s)][0] for s in schemes()}
        print(f"  {label}: " + ("the same entry first under all four schemes: " + " and ".join(next(iter(leads)))
                                if len(leads) == 1 else "first place changes with the scheme: "
                                + "; ".join(f"{s} {' and '.join(firsts[(label, s)][0])}" for s in schemes())))
    print("\n== Dropping one criterion at a time (equal weights): where first place changes")
    for label, vec in states:
        w = schemes()["Equal (baseline)"]
        tot, _, order = ranked(vec, w)
        base = [c for c in order if tot[c] == tot[order[0]]]
        moved = []
        for k in ORDER:
            ww = dict(w, **{k: 0.0})
            tot, _, order = ranked(vec, ww)
            lead = [c for c in order if tot[c] == tot[order[0]]]
            if lead != base:
                moved.append(f"{k} ({' and '.join(lead)})")
        print(f"  {label}: first {' and '.join(base)}{' alone' if len(base) == 1 else ''} in {29 - len(moved)} of 29; "
              + ("otherwise " + ", ".join(moved) if moved else "never changes"))
    print("\n== Close calls (equal weights): the leader's flagged calls all resolved down, the runner-up's all up")
    for label, vec in states[1:]:
        blocks = blocks_of.get(label, b84)
        tot, _, order = ranked(vec, schemes()["Equal (baseline)"])
        lead = [c for c in order if tot[c] == tot[order[0]]]
        if len(lead) > 1:
            print(f"  {label}: first place is shared ({' and '.join(lead)} at {tot[lead[0]]:.1f}); no single leader to test")
            continue
        a = lead[0]
        down = sum(min(f["alternatives"] + [f["scored"]]) - f["scored"] for f in blocks[a]["flags"]
                   if vec[a].get(f["criterion"]) == f["scored"])
        up = {b: sum(max(f["alternatives"] + [f["scored"]]) - f["scored"] for f in blocks[b]["flags"]
                     if vec[b].get(f["criterion"]) == f["scored"]) for b in order if b != a and tot[b] == tot[order[1]]}
        b = max(up, key=lambda x: (up[x], -order.index(x)))
        print(f"  {label}: {a} {tot[a]:.1f} to {tot[a] + down:.1f}; {b} {tot[b]:.1f} to {tot[b] + up[b]:.1f}"
              + (f" (the most of the {len(up)} level at {tot[b]:.1f})" if len(up) > 1 else "") + ": "
              + (f"{b} first" if tot[b] + up[b] > tot[a] + down else (f"{a} first" if tot[a] + down > tot[b] + up[b] else "tied")))
    print("\nSUMMARY: " + "; ".join(f"{label}: first {' and '.join(firsts[(label, 'Equal (baseline)')][0])} by "
                                    f"{firsts[(label, 'Equal (baseline)')][1]:.1f} on equal weights" for label, _ in states))
    return 0


if __name__ == "__main__":
    sys.exit(main())
