#!/usr/bin/env python3
"""
blind_review.py -- the blind re-read's shared module (ledger D52, D53; Session 69)
====================================================================================
Before the Report and Paper v2.0 (stage 4), every unit a Sonnet 5.5 session read in Sessions 63 to 65 (parts
(2.9) C3.1, (2.10) C4.2, (2.11) the accelerated groups: C4.1, C4.4, C3.4, C4.5, C2.5, C1.1, C2.6, C3.6, C4.6) is
re-read in an Opus 5.5 session, blind to the earlier reading (ledger D53): the session is shown the v2.0 clause
text and the cached sources first, records its own clause statuses and verdict, and only then sees the Sonnet
reading, so the record can mark each unit agree or revise. The 8 C4.1 design units and 10 C2.5 units that still
carry a pre-v2.0 clause list are re-read on v2.0's clauses in the same pass (ledger D54). C2.1, C2.4 and C2.3's
clause 1 was never read on Sonnet (decision 65.2 held it); its first reading in a blind-review group (S58 of the
ledger) is an ordinary reading, not a comparison, and this module's comparison functions do not apply to it.

This module holds the machinery every blind-review group's script shares, the way pass_common.py holds the
rescoring pass's. A group's script is two UNITS-shaped dictionaries (`pass_common.py`'s format: {(code, cid):
{"verdict": v, "clauses": [(status, estimate, source), ...], "note": ..., "zero": optional}}) -- the prior,
Sonnet-read units for its criteria, and the new, blind units the Opus session records -- plus a call to
compare_group(). Nothing here changes a score: applying a "revise" is reserved for the generator session (S61
of the ledger), never by hand, and a change to CCO-PTF-CIP-SZH's units waits for the owner (decision 57.2).

WHAT IT HOLDS
  PRIOR            which pass_common.py part (its PARTS tag) a v2.0 criterion's Sonnet-read units came from.
  blind_view(p, key)   the v2.0 clause text and the evidence_cache/ file names for one unit -- no verdict, no
                        clause status, no estimate, no source text. What the Opus session is shown before it
                        records its own reading; it never names the prior part or its UNITS dictionary.
  compare_unit(prior, new)   per-clause and per-verdict comparison between the prior reading and the new, blind
                        one: "agree" if every clause status and the verdict match, else "revise" with the
                        differing clause indices and the verdict change named.
  compare_group(prior_units, new_units)   one row per unit (compare_unit), a tally, and the keys present on only
                        one side (every key must be read on both; a missing one is reported, not silently skipped).
  record_table(rows)   the markdown table a group's record embeds, in run_group()'s convention (pass_common.py).

Usage: python3 blind_review.py --selftest   (reads criteria.json, neec_corpus.json, neec_scores.csv and the
                                             scripts pass_common.PARTS names; writes nothing; proves compare_unit's
                                             agree/revise rule on synthetic fixtures and that blind_view exposes no
                                             verdict, status, estimate or source for a real unit of each prior part)
Prints file names only. Deterministic.
"""
import glob
import os
import sys

import pass_common as pc

HERE = os.path.dirname(os.path.abspath(__file__))

# Which pass_common.py part a v2.0 criterion's units were read in, for the three Sonnet-run sessions (63 to 65).
# C2.1, C2.4 and C2.3 are not here: their clause 1 was held, not read, by decision 65.2 (STATE.md, Position).
PRIOR = {
    "C3.1": "(2.9)", "C4.2": "(2.10)",
    "C4.1": "(2.11)", "C4.4": "(2.11)", "C3.4": "(2.11)", "C4.5": "(2.11)", "C2.5": "(2.11)",
    "C1.1": "(2.11)", "C2.6": "(2.11)", "C3.6": "(2.11)", "C4.6": "(2.11)",
}


def blind_view(p, key):
    """What a blind reader is shown for unit `key` = (code, cid): the display name, the v2.0 clause text in
    order, and the evidence_cache/ file names for the criterion, if a cache exists. No verdict, clause status,
    estimate or source: that is the reading still to be made."""
    code, cid = key
    cache_dir = os.path.join(HERE, "evidence_cache", cid)
    cache_files = sorted(os.path.basename(f) for f in glob.glob(os.path.join(cache_dir, "*"))) \
        if os.path.isdir(cache_dir) else []
    return {"unit": p.names.get(code, code), "clauses_v2": list(p.v2[cid]["definition"]["clauses"]),
            "cache_files": cache_files}


def compare_unit(prior, new):
    """True/False (agree) and a list of differences, comparing clause statuses and the verdict only -- never the
    estimate or source text, which may be worded differently while describing the same reading."""
    diffs = []
    pc_clauses, nc_clauses = prior["clauses"], new["clauses"]
    if len(pc_clauses) != len(nc_clauses):
        diffs.append(f"clause count {len(pc_clauses)} (prior) vs {len(nc_clauses)} (new)")
    else:
        for i, ((pst, _, _), (nst, _, _)) in enumerate(zip(pc_clauses, nc_clauses)):
            if pst != nst:
                diffs.append(f"clause {i + 1}: {pst} (prior) vs {nst} (new)")
    if prior["verdict"] != new["verdict"]:
        diffs.append(f"verdict: {pc.f1(prior['verdict'])} (prior) vs {pc.f1(new['verdict'])} (new)")
    return (not diffs), diffs


def compare_group(prior_units, new_units):
    """One result per key in either dict: (agree: bool, diffs: list[str]); a key on only one side gets
    ["missing prior reading"] or ["missing blind reading"], never silently skipped. `tally` counts agree/revise
    among keys present on both sides."""
    results = {}
    for key in sorted(set(prior_units) | set(new_units)):
        if key not in prior_units:
            results[key] = (False, ["missing prior reading"])
        elif key not in new_units:
            results[key] = (False, ["missing blind reading"])
        else:
            results[key] = compare_unit(prior_units[key], new_units[key])
    both = [k for k in results if k in prior_units and k in new_units]
    tally = {"agree": sum(1 for k in both if results[k][0]), "revise": sum(1 for k in both if not results[k][0])}
    return results, tally


def record_table(names, results):
    """The markdown table a group's record embeds: one row per unit, its criterion, agree or revise, and why."""
    rows = ["| Unit | Criterion | Result | Notes |", "|---|---|---|---|"]
    for code, cid in sorted(results, key=lambda k: (k[1], k[0])):
        agree, diffs = results[(code, cid)]
        rows.append(f"| {names.get(code, code)} | {cid} | {'agree' if agree else 'revise'} | "
                    f"{'; '.join(diffs) if diffs else '—'} |")
    return "\n".join(rows)


def selftest():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)

    print("blind_review.py --selftest: the blind re-read's comparison rule, and blind_view's non-disclosure")
    print("inputs: criteria.json, neec_corpus.json, neec_scores.csv, " + ", ".join(p for _, _, p, _ in pc.PARTS) + "\n")

    p = pc.Pass()
    check(all(cid in p.v2 for cid in PRIOR), "every PRIOR criterion is one of the 29 v2.0 criteria", str(PRIOR))
    check(all(tag in p.tags for tag in set(PRIOR.values())), "every PRIOR tag is a loaded part of the pass",
          str(set(PRIOR.values()) - set(p.tags)))

    # blind_view discloses no verdict, status, estimate or source, for one real unit of each prior part.
    for cid, tag in (("C3.1", "(2.9)"), ("C4.2", "(2.10)"), ("C1.1", "(2.11)")):
        mod = p.mods[p.tags.index(tag)]
        key = next(k for k in mod.UNITS if k[1] == cid)
        view = blind_view(p, key)
        check(set(view) == {"unit", "clauses_v2", "cache_files"},
              f"blind_view({key}) returns only unit, clauses_v2 and cache_files", str(set(view)))
        check(len(view["clauses_v2"]) == len(p.v2[cid]["definition"]["clauses"]) > 0,
              f"blind_view({key}) carries every one of {cid}'s v2.0 clauses, and at least one")
        blob = repr(view)
        prior_rec = mod.UNITS[key]
        check(pc.f1(prior_rec["verdict"]) not in blob, f"blind_view({key}) does not print the prior verdict")
        check(not any(est in blob for st, est, src in prior_rec["clauses"] if est),
              f"blind_view({key}) does not print a prior clause's estimate text")

    # compare_unit: agreement (estimate and source text may differ; status and verdict do not).
    prior = {"verdict": 1.0, "clauses": [("C", "old estimate 1", "old source 1"), ("C", "old estimate 2", "old source 2")]}
    agreeing = {"verdict": 1.0, "clauses": [("C", "new estimate 1", "new source 1"), ("C", "new estimate 2", "new source 2")]}
    agree, diffs = compare_unit(prior, agreeing)
    check(agree and not diffs, "compare_unit agrees when every clause status and the verdict match, reworded text aside",
          str(diffs))

    # compare_unit: a clause status change and a verdict change are both caught.
    revising = {"verdict": 0.5, "clauses": [("C", "new estimate 1", "new source 1"), ("S", "new estimate 2", "new source 2")]}
    agree2, diffs2 = compare_unit(prior, revising)
    check(not agree2 and len(diffs2) == 2, "compare_unit revises on a changed clause status and a changed verdict, "
          "one difference each", str(diffs2))
    check("clause 2" in diffs2[0] and "verdict" in diffs2[1], "the differences name the clause index and the verdict",
          str(diffs2))

    # compare_group: tallies agree/revise among shared keys, and reports a key missing on either side.
    prior_units = {("aa", "C9.9"): prior, ("bb", "C9.9"): prior}
    new_units = {("aa", "C9.9"): agreeing, ("bb", "C9.9"): revising, ("cc", "C9.9"): agreeing}
    results, tally = compare_group(prior_units, new_units)
    check(tally == {"agree": 1, "revise": 1}, "compare_group tallies one agree and one revise among the shared keys",
          str(tally))
    check(results[("cc", "C9.9")] == (False, ["missing prior reading"]),
          "compare_group reports a key with no prior reading, rather than skipping it", str(results[("cc", "C9.9")]))

    table = record_table({"aa": "Alpha", "bb": "Beta", "cc": "Gamma"}, results)
    check(all(s in table for s in ("Alpha", "Beta", "Gamma", "agree", "revise", "missing prior reading")),
          "record_table's markdown names every unit and its result")

    print("\nBLIND REVIEW MODULE SELFTEST: ALL CHECKS PASSED." if ok else "\nBLIND REVIEW MODULE SELFTEST: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(selftest())
    sys.exit("usage: python3 blind_review.py --selftest")
