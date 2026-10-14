#!/usr/bin/env python3
"""
pass_common.py -- NEEC rescoring pass: the shared module (decision 52.5, W2)
============================================================================
Session 52. Until Session 51 every group of the rescoring pass was a script of 500 to 750 lines that re-implemented the
loading, the cumulative state and the consequence tables of the group before it and imported its predecessors one by
one. This module is the one copy of what every group shares, so that a later group is a short file of readings (a
`UNITS` dictionary in the form of rescoring_s37.U) plus a short script that calls `run_group`. Nothing here changes a
score or a file; the existing scripts and their captured outputs are untouched, and --selftest proves this module
reproduces group 2.1's published tables and the rules (D28) as rescoring_s37.py and rescoring_s51.py established them.

WHAT IT HOLDS
  PARTS            every part of the pass in order: (tag, module, file, session). A new group adds one line.
  Pass             the cumulative state: the v2.0 criteria, the published 26-criterion vectors, every re-estimated unit
                   (merged, with the part that last set it), the vector after each part, the totals and failures.
  run_group(...)   for a group's readings: records complete, the D28 rule, consequences, dominance, the ledger, the
                   anchor examples moved, and the record file containing every generated table verbatim.
  helpers          read, load, f1, tier, verdict_of, ranks, dominance, order_codes, summ.
Session 53 (decision 53.2): a class M re-read may hold or set 0.0 on a unit's stated whole-criterion reason (`zero`,
protocol 2.1), never with its clause cleared; check_rule and the dominance line allow for it, and print what they
printed before for every group without such a unit.

Usage: python3 pass_common.py --selftest   (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                            neec_scores.csv, r4_audit_s35.py, the scripts of PARTS and the files they
                                            read, NEEC_Rescoring_s51.md; writes nothing)
Prints file names only. Deterministic.
"""
import csv
import importlib.util
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CRIT44, CORPUS, CSV = "criteria.json", "criteria_s44_snapshot.json", "neec_corpus.json", "neec_scores.csv"
PARTS = (("(a)", "rescoring_s37", "rescoring_s37.py", 37), ("(b1)", "rescoring_s38", "rescoring_s38.py", 38),
         ("(b2)", "rescoring_s39", "rescoring_s39.py", 39), ("(b3)", "rescoring_s40", "rescoring_s40.py", 40),
         ("(b4)", "rescoring_s41", "rescoring_s41.py", 41), ("(b5)", "rescoring_s42", "rescoring_s42.py", 42),
         ("(b6)", "rescoring_s43", "rescoring_s43.py", 43), ("(b7)", "rescoring_s47", "rescoring_s47.py", 47),
         ("48.3", "rescoring_s48", "rescoring_s48.py", 48), ("(b8)", "rescoring_s49", "rescoring_s49.py", 49),
         ("(b9)", "rescoring_s50", "rescoring_s50.py", 50), ("(2.1)", "rescoring_s51", "rescoring_s51.py", 51),
         ("(2.2)", "rescoring_s53", "rescoring_s53.py", 53))
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}


def read(name):
    path = os.path.join(HERE, name)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: missing input {name}")
    with open(path, encoding="utf-8") as f:
        return f.read()


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def f1(x):
    return f"{x:.1f}"


def tier(failures):
    return "Potentially Adequate" if failures <= 2 else ("Partially Adequate" if failures <= 5
                                                         else "Structurally Inadequate")


def verdict_of(clauses):
    """D28: 1.0 only if every clause is cleared or moot; otherwise 0.5 (never 0.0 in the pass's re-estimates)."""
    return 1.0 if all(st in "CM" for st, _, _ in clauses) else 0.5


def ranks(totals):
    order = sorted(totals.values(), reverse=True)
    return {k: 1 + sum(1 for x in order if x > v) for k, v in totals.items()}


def dominance(vecs, cids):
    pairs = []
    for a in vecs:
        for b in vecs:
            if a != b and all(vecs[a][c] >= vecs[b][c] for c in cids) and any(vecs[a][c] > vecs[b][c] for c in cids):
                pairs.append((a, b))
    frontier = [a for a in vecs if not any(p[1] == a for p in pairs)]
    return pairs, frontier


def order_codes(names, base):
    return sorted(names, key=lambda c: (-base["total"][c], list(names).index(c)))


def summ(v, cids):
    return {"total": {c: sum(v[c][k] for k in cids) for c in v},
            "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}


class Pass:
    """The pass's cumulative state, read once. `upto` limits the parts included (default: all of PARTS)."""

    def __init__(self, upto=None):
        parts = PARTS if upto is None else PARTS[:upto]
        self.mods = [load(mod, path) for _, mod, path, _ in parts]
        self.tags = [t for t, _, _, _ in parts]
        self.crit44 = json.loads(read(CRIT44))["criteria"]
        self.cids = [c["id"] for c in self.crit44]
        self.v2 = {c["id"]: c for c in json.loads(read(CRITERIA))["criteria"]}
        self.v2ids = list(self.v2)
        self.corpus = json.loads(read(CORPUS))["entries"]
        self.names = {e["code"]: e["display_name"] for e in self.corpus}
        self.order = list(self.names)
        self.vec = {e["code"]: dict(e["vector"]) for e in self.corpus}
        self.merged, self.part_of, self.steps_units = {}, {}, []
        for tag, m in zip(self.tags, self.mods):
            self.merged.update(m.UNITS)
            self.part_of.update({k: tag for k in m.UNITS})
            self.steps_units.append(m.UNITS)
        self.vsteps = self.vectors(self.steps_units)
        self.steps = [summ(v, self.cids) for v in self.vsteps]

    def vectors(self, parts, start=None):
        """The vector after each part of `parts` (a sequence of UNITS dicts), from `start` (default: the published one)."""
        out = [{c: dict(v) for c, v in (self.vec if start is None else start).items()}]
        for part in parts:
            v = {c: dict(x) for c, x in out[-1].items()}
            for (c, k), r in part.items():
                if k in self.cids:
                    v[c][k] = r["verdict"]
            out.append(v)
        return out


def check_records(p, units, ok_print):
    """Every unit has one status per v2.0 clause, each with an estimate and a source, and no stray markup."""
    bad = []
    for key, rec in units.items():
        n = len(p.v2[key[1]]["definition"]["clauses"])
        if len(rec["clauses"]) != n:
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {n}")
        for i, (st, est, src) in enumerate(rec["clauses"]):
            if st not in STATUS or not est.strip() or not src.strip():
                bad.append(f"{key} clause {i + 1}: status {st!r}, or an empty estimate or source")
            if "|" in est + src + rec["note"] + (rec.get("zero") or "") or "{" in est:
                bad.append(f"{key} clause {i + 1}: a pipe character or an unfilled field")
    return ok_print(not bad, "every unit has one status per v2.0 clause, each with its estimate and its source",
                    "; ".join(bad[:3]))


def check_rule(units, ok_print):
    """D28 for every unit. A class M re-read (decision 53.2) may also hold or set 0.0, but only on a stated whole-
    criterion reason under protocol 2.1 (the unit's `zero`) and never with a clause cleared: D28(f), a clause-level
    gap alone never makes 0.0. Groups without such a unit print the rule as parts (a) to group 2.1 stated it."""
    def right(r):
        if r.get("zero"):
            return r["verdict"] == 0.0 and not any(st in "CM" for st, _, _ in r["clauses"])
        return r["verdict"] in (0.5, 1.0) and verdict_of(r["clauses"]) == r["verdict"]
    wrong = [k for k, r in units.items() if not right(r)]
    if not any(r.get("zero") for r in units.values()):
        return ok_print(not wrong, "every verdict follows D28 (1.0 only if every clause is cleared or moot), and none "
                        "is 0.0", str(wrong))
    return ok_print(not wrong, "every verdict follows D28 (1.0 only if every clause is cleared or moot, otherwise 0.5), "
                    "and each 0.0 rests on its stated whole-criterion reason (protocol 2.1) with no clause cleared",
                    str(wrong))


def consequences_table(p, steps, ranks_now, prev_label, this_label):
    """Totals, ranks, failures and tiers: published, before this group, after it (steps = p.steps incl. this group)."""
    base, mp, after = steps[0], steps[-2], steps[-1]
    rb, rp, rn = ranks(base["total"]), ranks(mp["total"]), ranks_now
    rows = [f"| Entry | Published (rank) | {prev_label} (rank) | {this_label} (rank) | Change here | Failures | Tier |",
            "|---|---:|---:|---:|---:|---:|---|"]
    for c in order_codes(p.names, base):
        rows.append(f"| {c} | {f1(base['total'][c])} ({rb[c]}) | {f1(mp['total'][c])} ({rp[c]}) | "
                    f"{f1(after['total'][c])} ({rn[c]}) | {f1(after['total'][c] - mp['total'][c])} | "
                    f"{after['fail'][c]} | {tier(after['fail'][c])} |")
    return "\n".join(rows)


def ledger_table(p, tags, steps, merged):
    """Published total, each part's change, the total now, units re-estimated and at 0.5. tags exclude 'published'."""
    base, after = steps[0], steps[-1]
    rows = ["| Entry | Published | " + " | ".join(tags) + " | Now | Re-estimated | At 0.5 |",
            "|---|---:|" + "---:|" * len(tags) + "---:|---:|---:|"]
    sums_ok = True
    for c in order_codes(p.names, base):
        deltas = [steps[i + 1]["total"][c] - steps[i]["total"][c] for i in range(len(tags))]
        mine = [k for k in merged if k[0] == c]
        low = [k for k in mine if merged[k]["verdict"] == 0.5]
        sums_ok = sums_ok and abs(sum(deltas) - (after["total"][c] - base["total"][c])) < 1e-9
        rows.append(f"| {c} | {f1(base['total'][c])} | " + " | ".join("" if d == 0 else f1(d) for d in deltas)
                    + f" | {f1(after['total'][c])} | {len(mine)} | {len(low)} |")
    return "\n".join(rows), sums_ok


def dominance_line(p, vp, vn, steps, merged, prev_label):
    pp, fp = dominance(vp, p.cids)
    pn, fn = dominance(vn, p.cids)
    order = p.order
    gained = sorted(set(pn) - set(pp), key=lambda x: (order.index(x[0]), order.index(x[1])))
    lost = sorted(set(pp) - set(pn), key=lambda x: (order.index(x[0]), order.index(x[1])))
    mp, after = steps[-2], steps[-1]
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    second = sorted((c for c in order if c not in first), key=lambda c: -after["total"][c])[0]
    n_all = len(merged)
    st_all = sum(1 for r in merged.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for r in merged.values())
    pub = {k: p.vec[k[0]][k[1]] for k in merged}
    if all(v == 1.0 for v in pub.values()):
        tail = f"{st_all} stand and {n_all - st_all} are at 0.5 ({f1(pts_all)} points)."
    else:
        at = {x: sum(1 for r in merged.values() if r["verdict"] == x) for x in (1.0, 0.5, 0.0)}
        up = sum(1 for k, r in merged.items() if r["verdict"] > pub[k])
        down = sum(1 for k, r in merged.items() if r["verdict"] < pub[k])
        net = sum(r["verdict"] - pub[k] for k, r in merged.items())
        tail = (f"{at[1.0]} are at 1.0, {at[0.5]} at 0.5 and {at[0.0]} at 0.0; against their published scores {down} "
                f"fell, {up} rose and {n_all - up - down} are unchanged (net {f1(net)} points).")
    return (f"After this group the corpus has {len(pn)} dominance pairs against {len(pp)} after {prev_label} (new: " +
            (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
            (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
            f"against {len(fp)} (" + ", ".join(c for c in order if c in fn) + f"). First place: {first[0]}, "
            f"{f1(mp['total'][first[0]])} after {prev_label}, {f1(after['total'][first[0]])} now, ahead of "
            + ", ".join(c for c in order if after["total"][c] == after["total"][second])
            + f" at {f1(after['total'][second])}. Across the pass so far {n_all} units have been re-estimated, each "
            f"counted once: " + tail)


def anchors_line(p, merged, part_of, vn):
    """Published anchor examples whose cited unit the pass moves; bands left with no corpus unit at their value."""
    code_of = {v: k for k, v in p.names.items()}
    hits, empty = [], []
    for c in p.crit44:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                cd = code_of.get(ex["system"])
                if cd and (cd, c["id"]) in merged and merged[(cd, c["id"])]["verdict"] != ex["cited"]:
                    hits.append(f"{c['id']}'s {band} example, {cd} (part {part_of[(cd, c['id'])]})")
                    if not any(vn[x][c["id"]] == float(band) for x in vn):
                        empty.append((c["id"], band))
    return hits, empty, ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) + ". Bands whose example the "
                         "pass moves and which no corpus unit then scores at their value: "
                         + ", ".join(f"{c}'s {b}" for c, b in empty) + ".")


def run_group(p, tag, units, record, prev_label, this_label, out=print):
    """A new group's generic checks and tables. `p` is Pass(upto=len(PARTS)-1)-like state of the parts before the group;
    `units` the group's readings. Returns (ok, tables). Group-specific checks (its scan, its simulation runs, its
    reopening conditions) stay in the group's own script."""
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        out(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond
    check_records(p, units, check)
    check_rule(units, check)
    merged, part_of = dict(p.merged), dict(p.part_of)
    merged.update(units)
    part_of.update({k: tag for k in units})
    vsteps = p.vsteps + p.vectors([units], start=p.vsteps[-1])[1:]
    steps = p.steps + [summ(vsteps[-1], p.cids)]
    vp, vn = vsteps[-2], vsteps[-1]
    t = {"consequences": consequences_table(p, steps, ranks(steps[-1]["total"]), prev_label, this_label),
         "dominance": dominance_line(p, vp, vn, steps, merged, prev_label.replace("After ", ""))}
    t["ledger"], sums_ok = ledger_table(p, p.tags + [tag], steps, merged)
    check(sums_ok, "each entry's changes, part by part, sum to the difference between its published total and its total now")
    t["anchors"] = anchors_line(p, merged, part_of, vn)[2]
    text = read(record) if os.path.isfile(os.path.join(HERE, record)) else ""
    missing = [k for k, v in t.items() if v not in text]
    check(not missing, f"{record} contains all {len(t)} generated tables", ", ".join(missing))
    return ok, t


def selftest():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
    print("pass_common.py --selftest: the shared module reproduces the pass's established rules and group 2.1's tables")
    print(f"inputs: {CRITERIA}, {CRIT44}, {CORPUS}, {CSV}, r4_audit_s35.py, " + ", ".join(p for _, _, p, _ in PARTS)
          + ", NEEC_Rescoring_s51.md\n")
    s37 = load("rescoring_s37_ref", "rescoring_s37.py")
    check(all(tier(n) == s37.tier(n) for n in range(0, 30)), "tier() equals rescoring_s37.tier for 0 to 29 failures")
    check(ranks({"a": 3.0, "b": 3.0, "c": 1.0}) == s37.ranks({"a": 3.0, "b": 3.0, "c": 1.0}), "ranks() equals the pass's")
    check(f1(0.25) == s37.f1(0.25) and f1(10.5) == s37.f1(10.5), "f1() equals the pass's")
    probe = [("C", "", ""), ("M", "", "")], [("C", "", ""), ("S", "", "")], [("U", "", "")]
    check([verdict_of(x) for x in probe] == [s37.verdict_of(x) for x in probe] == [1.0, 0.5, 0.5],
          "verdict_of() applies D28: 1.0 only if every clause is cleared or moot, else 0.5")
    p_all = Pass()
    check(len(PARTS) >= 12 and all(t in p_all.part_of.values() for t in p_all.tags if p_all.steps_units[p_all.tags.index(t)]),
          f"all {len(PARTS)} parts load; {len(p_all.merged)} units are re-estimated")
    check(sum(1 for k in p_all.merged if k[1] not in p_all.cids) == 0,
          "every re-estimated unit lies on a criterion of the published 26-criterion structure")
    check(len(p_all.v2) == 29 and len(p_all.cids) == 26 and len(p_all.corpus) == 23 and len(p_all.v2ids) == 29,
          "29 v2.0 criteria, 26 published criteria, 23 entries")
    csv_rows = list(csv.DictReader(read(CSV).splitlines()))
    csv_tot = {r["system"]: (float(r["total_score"]), int(r["failures"])) for r in csv_rows}
    base = p_all.steps[0]
    check(all(csv_tot[p_all.names[c]] == (base["total"][c], base["fail"][c]) for c in p_all.names),
          f"published totals and failure counts equal {CSV}'s for all 23 entries")
    # regression on group 2.1: rebuild its generic tables from the parts before it and compare with the script's
    i51 = p_all.tags.index("(2.1)")
    s51 = p_all.mods[i51]
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = s51.main()
    check(rc == 0, "rescoring_s51.py's own run still passes")
    prior = Pass(upto=i51)
    lines = []
    ok2, t = run_group(prior, "(2.1)", s51.UNITS, "NEEC_Rescoring_s51.md", "After part (b)", "After group 2.1", out=lines.append)
    check(ok2, "run_group on group 2.1's readings: records complete, the rule, the ledger sums, the record's tables",
          "; ".join(l for l in lines if "FAIL" in l)[:200])
    same = {k: t[k] == s51.GENERATED[k] for k in t}
    check(all(same.values()), "its consequences table, ledger, dominance line and anchors line equal group 2.1's verbatim",
          ", ".join(k for k, v in same.items() if not v))
    print("\nPASS COMMON MODULE SELFTEST: ALL CHECKS PASSED." if ok else "\nPASS COMMON MODULE SELFTEST: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit("usage: python3 pass_common.py --selftest")
