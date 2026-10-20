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

Three states: Session 79 (neec_corpus_v2_s79_snapshot.json), the adjudicated scores (neec_corpus_v2.json), and the
adjudicated scores with the four owner items applied as the adjudication reads them (adjudicate_s83.OWNER; never written).

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


def owner_applied(vec):
    with open(os.devnull, "w") as dn:
        stdout, sys.stdout = sys.stdout, dn
        try:
            adj = pc.load("adjudicate_s83", "adjudicate_s83.py")
        finally:
            sys.stdout = stdout
    out = {c: dict(v) for c, v in vec.items()}
    for (c, k), it in adj.OWNER.items():
        out[c][k] = it["proposed"]
    return out


def ranked(vec, w):
    tot = {c: sum(v[k] * w[k] for k in ORDER) for c, v in vec.items()}
    mx = sum(w.values())
    order = sorted(tot, key=lambda c: (-tot[c], c))
    return tot, mx, order


def main():
    v79, names = vectors("neec_corpus_v2_s79_snapshot.json")
    vadj, _ = vectors("neec_corpus_v2.json")
    vown = owner_applied(vadj)
    blocks = {b["code"]: b for b in load("summary_blocks_v2.json")}
    states = [("Session 79", v79), ("Adjudicated (Session 83)", vadj), ("Adjudicated, with the four owner items", vown)]
    print("weighting_s83.py: the four weighting schemes on the v2.0 corpus (29 criteria), three states\n")
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
        base = ranked(vec, w)[2][0]
        moved = []
        for k in ORDER:
            ww = dict(w, **{k: 0.0})
            tot, _, order = ranked(vec, ww)
            lead = [c for c in order if tot[c] == tot[order[0]]]
            if lead != [base]:
                moved.append(f"{k} ({' and '.join(lead)})")
        print(f"  {label}: first {base} alone in {29 - len(moved)} of 29; " + ("otherwise " + ", ".join(moved) if moved else
                                                                               "never changes"))
    print("\n== Close calls (equal weights): the leader's flagged calls all resolved down, the runner-up's all up")
    for label, vec in states[1:]:
        tot, _, order = ranked(vec, schemes()["Equal (baseline)"])
        a, b = order[0], order[1]
        down = sum(min(f["alternatives"] + [f["scored"]]) - f["scored"] for f in blocks[a]["flags"]
                   if vec[a].get(f["criterion"]) == f["scored"])
        up = sum(max(f["alternatives"] + [f["scored"]]) - f["scored"] for f in blocks[b]["flags"]
                 if vec[b].get(f["criterion"]) == f["scored"])
        print(f"  {label}: {a} {tot[a]:.1f} to {tot[a] + down:.1f}; {b} {tot[b]:.1f} to {tot[b] + up:.1f}: "
              + (f"{b} first" if tot[b] + up > tot[a] + down else (f"{a} first" if tot[a] + down > tot[b] + up else "tied")))
    print("\nSUMMARY: " + "; ".join(f"{label}: first {' and '.join(firsts[(label, 'Equal (baseline)')][0])} by "
                                    f"{firsts[(label, 'Equal (baseline)')][1]:.1f} on equal weights" for label, _ in states))
    return 0


if __name__ == "__main__":
    sys.exit(main())
