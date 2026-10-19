#!/usr/bin/env python3
"""
final_pass.py -- NEEC stage 3b: the final readings of the seven blind groups, laid over the rescoring pass (Session 78, ledger S61)
================================================================================================================================
The rescoring pass (pass_common.PARTS, parts (a) to (2.11)) read every unit in play once; Sessions 71 to 77 then re-read the units
of seven groups blind (blind_review.py), each script ending in a FINAL dictionary of the readings that stand (the blind reading,
or the prior where the comparison restored it, decision 71.x to 77.3). This module holds the one list of those dictionaries, in
the order of the sessions, and lays them over the pass. It changes no file. It is used by apply_final_s78.py (which writes the
v2 files from it) and by build_evidence.py (which reports each unit's final reading and where it was read).

  GROUPS          (tag, session, script, record, attributes): one line per blind group, in the order the sessions read them.
  load_groups()   the groups' FINAL dictionaries, loaded from the scripts (not run).
  final_state(p)  from a pass_common.Pass: (units, part_of, new_units, new_part_of), where `units` is p.merged with every
                  blind unit of the 26 published criteria replaced, `new_units` is rescoring_s65.NEW_UNITS (C2.6, C3.6,
                  C4.6) with theirs replaced, and the part_of maps hold the tag of the part or group that read each unit last.
  owner_state(p)  final_state(p) with the owner's decisions 79.1 to 79.4 (owner_s79.py, Session 79) laid over it: seven units,
                  each re-reading one clause of its final reading; plus the part map before that layer. apply_owner_s79.py
                  writes the v2 files from it; apply_final_s78.py keeps writing the Session 78 state, now as snapshots.

The three class N criteria (C2.6, C3.6, C4.6) are not in the pass's merged units, which hold the 26 published criteria, so the
groups of Sessions 76 and 77 land in new_units and the others in units. Later groups replace earlier ones where they overlap;
none does (final_state checks it).

Usage: python3 final_pass.py --selftest   (loads the groups; checks every unit, the overlap, the counts; writes nothing)
Prints file names and summaries only. Deterministic.
"""
import io
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

GROUPS = (("blind s71", 71, "blind_s71.py", "NEEC_BlindReview_s71.md", ("FINAL",)),
          ("blind s72", 72, "blind_s72.py", "NEEC_BlindReview_s72.md", ("FINAL",)),
          ("blind s73", 73, "blind_s73.py", "NEEC_BlindReview_s73.md", ("FINAL",)),
          ("blind s74", 74, "blind_s74.py", "NEEC_BlindReview_s74.md", ("FINAL", "EXTRA_FINAL")),
          ("blind s75", 75, "blind_s75.py", "NEEC_BlindReview_s75.md", ("FINAL", "FIRST_FINAL")),
          ("blind s76", 76, "blind_s76.py", "NEEC_BlindReview_s76.md", ("FINAL",)),
          ("blind s77", 77, "blind_s77.py", "NEEC_BlindReview_s77.md", ("FINAL",)))
# units each group is expected to carry (decisions 71.1 to 77.3, the sessions' handoffs)
COUNTS = {"blind s71": 24, "blind s72": 23, "blind s73": 33, "blind s74": 31, "blind s75": 41, "blind s76": 51,
          "blind s77": 18}


def tag_label(tag):
    return f"the blind re-read of Session {tag.split()[1][1:]}"


def load_groups():
    """[(tag, session, record, units)], units the union of the group's FINAL dictionaries."""
    out = []
    for tag, sess, script, record, attrs in GROUPS:
        with redirect_stdout(io.StringIO()):
            mod = pc.load("final_" + script[:-3], script)
        units = {}
        for a in attrs:
            part = getattr(mod, a)
            assert not set(part) & set(units), f"{script}: {a} overlaps another dictionary of the group"
            units.update(part)
        out.append((tag, sess, record, units))
    return out


def final_state(p):
    """(units, part_of, new_units, new_part_of): the pass's units with the blind groups' final readings laid over them."""
    with redirect_stdout(io.StringIO()):
        new0 = dict(p.mods[-1].NEW_UNITS)
    units, part_of = dict(p.merged), dict(p.part_of)
    new_units, new_part_of = new0, {k: p.mods[-1].TAG for k in new0}
    seen = {}
    for tag, sess, record, fin in load_groups():
        for k, u in fin.items():
            assert k not in seen, f"{k} is read blind in {seen[k]} and in {tag}"
            seen[k] = tag
            if k in new_units:
                new_units[k], new_part_of[k] = dict(u), tag
            else:
                assert k in units, f"{k}: a blind reading of a unit the pass did not read"
                units[k], part_of[k] = dict(u), tag
    return units, part_of, new_units, new_part_of


def owner_units(units, new_units):
    """The owner's revised units (owner_s79.CHANGES), each built from the final reading of the same cell: the clause the
    decision re-reads is replaced, every other clause is carried, and the verdict follows D28."""
    with redirect_stdout(io.StringIO()):
        ow = pc.load("owner_s79", "owner_s79.py")
    out = {}
    for k, ch in ow.CHANGES.items():
        prior = new_units[k] if k in new_units else units[k]
        cl = [tuple(c) for c in prior["clauses"]]
        cl[ch["clause"] - 1] = tuple(ch["new"])
        out[k] = {"verdict": pc.verdict_of(cl), "clauses": cl, "flag": ch["flag"], "note": ch["note"], "zero": None}
    return ow, out


def owner_state(p):
    """final_state(p) with the owner's decisions of Session 79 laid over it, and the part map of the final readings:
    (units, part_of, new_units, new_part_of, final_part_of), where final_part_of is the part or blind group that read each
    unit before the owner's layer."""
    units, part_of, new_units, new_part_of = final_state(p)
    final_part_of = {**part_of, **new_part_of}
    ow, rev = owner_units(units, new_units)
    for k, u in rev.items():
        if k in new_units:
            new_units[k], new_part_of[k] = u, ow.TAG
        else:
            units[k], part_of[k] = u, ow.TAG
    return units, part_of, new_units, new_part_of, final_part_of


def selftest():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
    print("final_pass.py --selftest: the seven blind groups' final readings laid over the rescoring pass\n")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    groups = load_groups()
    check([t for t, _, _, _ in groups] == list(COUNTS) and all(len(u) == COUNTS[t] for t, _, _, u in groups),
          "each of the seven groups carries its units: " + ", ".join(f"{t.split()[1]} {len(u)}" for t, _, _, u in groups))
    units, part_of, new_units, new_part_of = final_state(p)
    allf = {k: u for _, _, _, fin in groups for k, u in fin.items()}
    check(len(allf) == sum(COUNTS.values()) and len(new_units) == 69 and len(units) == len(p.merged),
          f"{len(allf)} blind units, no overlap; the pass's {len(p.merged)} merged units and 69 class N units keep their keys")
    check(all(units[k] == allf[k] for k in allf if k in units) and all(new_units[k] == allf[k] for k in allf if k in new_units),
          "every blind unit replaces the pass's reading of the same cell")
    lines = []
    ok1 = pc.check_records(p, allf, lambda c, t, d="": lines.append(f"{'PASS' if c else 'FAIL'} {t} {d}") or c)
    ok2 = pc.check_rule(allf, lambda c, t, d="": lines.append(f"{'PASS' if c else 'FAIL'} {t} {d}") or c)
    check(ok1 and ok2, "every blind unit has one status per v2.0 clause with estimate and source, and follows D28 (0.0 only on "
                       "a stated whole-criterion reason)", "; ".join(l for l in lines if l.startswith("FAIL"))[:200])
    # the owner's layer (Session 79): each revised unit replaces a final unit, re-reads one clause, carries the others
    ow, rev = owner_units(units, new_units)
    prior = {**units, **new_units}
    check(len(rev) == 7 and all(k in prior for k in rev)
          and all(sum(a != b for a, b in zip(prior[k]["clauses"], rev[k]["clauses"])) == 1 for k in rev),
          f"the owner's layer (owner_s79.py, decisions 79.1 to 79.4) revises {len(rev)} final units, one clause each, "
          "carrying every other clause")
    check(all(prior[k]["verdict"] == 0.5 and rev[k]["verdict"] == 1.0 and rev[k]["flag"] for k in rev),
          "each revised unit moves from 0.5 to 1.0 by D28 and keeps the prior reading as its flag")
    lines = []
    ok3 = pc.check_records(p, rev, lambda c, t, d="": lines.append(f"{'PASS' if c else 'FAIL'} {t} {d}") or c)
    ok4 = pc.check_rule(rev, lambda c, t, d="": lines.append(f"{'PASS' if c else 'FAIL'} {t} {d}") or c)
    check(ok3 and ok4, "every revised unit has one status per v2.0 clause with estimate and source, and follows D28",
          "; ".join(l for l in lines if l.startswith("FAIL"))[:200])
    print("\nFINAL PASS MODULE SELFTEST: ALL CHECKS PASSED." if ok else "\nFINAL PASS MODULE SELFTEST: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit("usage: python3 final_pass.py --selftest")
