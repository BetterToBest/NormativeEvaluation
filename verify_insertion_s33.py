#!/usr/bin/env python3
"""
verify_insertion_s33.py -- NEEC Session 33: decision D26, verified against the Session 32 corpus
===============================================================================================
insert_session33.py changes one canonical cell: Ostrom-Style Commons Governance's C3.2, 0.0 -> 0.5
(decision D26). This script asserts that exactly that changed, and what follows from it, by comparing
the Session 33 files with their pinned Session 32 snapshots:

  [1] the canonical script: exactly one SCORES cell and one PUBLISHED row differ; both self-checks pass
  [2] neec_scores.csv: only Ostrom's row (Domain 3, total, percent, failures, notes) and Universal Basic
      Income's notes differ, and Ostrom's row agrees with the canonical vector
  [3] neec_corpus.json: only Ostrom's C3.2 differs
  [4] the corpus: ties, dominance, the Pareto frontier, tiers and ranks, before and after
  [5] negative tests: a second changed cell, a CSV row that disagrees with the vector, and a corpus file
      with another change are each rejected

Inputs beside this script: the Session 33 files (neec_weighting_robustness_analysis_v2.py, neec_scores.csv,
neec_corpus.json) and their *_s32_snapshot copies (pinned by MD5). Prints file names only; deterministic;
exit status 0 only if every check passes.
"""
import contextlib
import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OS = "Ostrom-Style Commons Governance"
UBI, MC = "Universal Basic Income", "Mutual Credit / LETS"
SNAP = {"canon": ("neec_weighting_robustness_analysis_v2_s32_snapshot.py", "d5041b13"),
        "csv": ("neec_scores_s32_snapshot.csv", "ca2eb1f4"), "corpus": ("neec_corpus_s32_snapshot.json", "ba3c7f70")}
NOW = {"canon": "neec_weighting_robustness_analysis_v2.py", "csv": "neec_scores.csv", "corpus": "neec_corpus.json"}
RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append((label, bool(ok), detail))


def path(name):
    p = os.path.join(HERE, name)
    if not os.path.isfile(p):
        sys.exit(f"ERROR: cannot find {name}")
    return p


def pinned(name, md5):
    got = hashlib.md5(open(path(name), "rb").read()).hexdigest()[:8]
    if got != md5:
        sys.exit(f"ERROR: {name} md5 {got}, expected {md5}")
    return path(name)


def load(modname, p):
    spec = importlib.util.spec_from_file_location(modname, p)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def self_check(m):
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            return m.verify_transcription() is not False
    except AssertionError:
        return False


def cell_diff(a, b):
    return sorted((s, c, a[s][c], b[s][c]) for s in a for c in a[s] if a[s][c] != b[s][c])


def csv_rows(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def row_agrees(row, header, vector):
    r = dict(zip(header, row))
    total = sum(vector.values())
    fails = sum(1 for x in vector.values() if x == 0.0)
    d3 = sum(v for c, v in vector.items() if c.startswith("C3."))
    return (float(r["total_score"]) == total and r["total_percent"] == f"{int(round(100 * total / 26))}%"
            and int(r["failures"]) == fails and float(r["domain3_system_resilience"]) == d3)


def corpus_diff(a, b):
    ea, eb = {e["key"]: e for e in a["entries"]}, {e["key"]: e for e in b["entries"]}
    out = [k for k in ("schema", "description", "criteria") if a.get(k) != b.get(k)]
    out += [f"{k}: entry set" for k in sorted(set(ea) ^ set(eb))]
    for k in sorted(set(ea) & set(eb)):
        out += [f"{k}: {f}" for f in ea[k] if f != "vector" and ea[k][f] != eb[k].get(f)]
        out += [f"{k}: {c} {ea[k]['vector'][c]} -> {eb[k]['vector'][c]}" for c in ea[k]["vector"]
                if ea[k]["vector"][c] != eb[k]["vector"][c]]
    return out


def main():
    old = load("_canon_s32", pinned(*SNAP["canon"]))
    new = load("_canon_s33", path(NOW["canon"]))
    S0, S1 = old.SCORES, new.SCORES
    total = lambda S, k: sum(S[k].values())
    nfail = lambda S, k: sum(1 for x in S[k].values() if x == 0.0)
    dom = lambda S, a, b: all(S[a][c] >= S[b][c] for c in S[a]) and any(S[a][c] > S[b][c] for c in S[a])
    pairs = lambda S: sorted((a, b) for a in S for b in S if a != b and dom(S, a, b))
    front = lambda S: sorted(s for s in S if not any(dom(S, t, s) for t in S if t != s))
    rank = lambda S, k: 1 + sum(1 for s in S if total(S, s) > total(S, k))
    ties = lambda S, k: sorted(s for s in S if s != k and total(S, s) == total(S, k))

    # [1] the canonical script
    check("[1] both canonical scripts pass their own transcription self-check", self_check(old) and self_check(new))
    check("[1] same 23 systems and the same 26 criteria", sorted(S0) == sorted(S1) and len(S1) == 23
          and list(old.ALL_CRITS) == list(new.ALL_CRITS) and len(new.ALL_CRITS) == 26)
    check("[1] exactly one SCORES cell differs: Ostrom-Style Commons Governance, C3.2, 0.0 -> 0.5",
          cell_diff(S0, S1) == [(OS, "C3.2", 0.0, 0.5)], f"{cell_diff(S0, S1)}")
    pub = sorted(k for k in old.PUBLISHED if old.PUBLISHED[k] != new.PUBLISHED[k])
    check("[1] exactly one PUBLISHED row differs (Ostrom: D3 2.5 -> 3.0, total 14.0 -> 14.5), and it equals the vector",
          pub == [OS] and {k: v for k, v in new.PUBLISHED[OS].items() if old.PUBLISHED[OS][k] != v} == {"D3": 3.0, "Total": 14.5}
          and new.PUBLISHED[OS]["Total"] == total(S1, OS), f"{pub}")

    # [2] the CSV
    a, b = csv_rows(pinned(*SNAP["csv"])), csv_rows(path(NOW["csv"]))
    header = a[0]
    changed = {rb[0]: [header[i] for i in range(len(header)) if ra[i] != rb[i]]
               for ra, rb in zip(a[1:], b[1:]) if ra != rb}
    check("[2] same header and row order (23 systems)", b[0] == header and [r[0] for r in a] == [r[0] for r in b]
          and len(b) == 24)
    check("[2] only two rows differ: Ostrom's (Domain 3, total, percent, failures, revision note, notes) and UBI's notes",
          changed == {UBI: ["notes"], OS: ["domain3_system_resilience", "total_score", "total_percent", "failures",
                                           "revision_note", "notes"]}, f"{changed}")
    rows = {r[0]: r for r in b[1:]}
    check("[2] Ostrom's row agrees with the canonical vector: 3.0 / 14.5 / 56% / 3 failures, Partially Adequate",
          row_agrees(rows[OS], header, S1[OS]) and dict(zip(header, rows[OS]))["adequacy_tier"] == "Partially Adequate")
    key_of = {n: next((k for k in S1 if n == k or n.startswith(k + " (")), None) for n in rows}
    check("[2] every row agrees with its canonical vector (CSV names mapped to canonical keys)",
          None not in key_of.values() and sorted(key_of.values()) == sorted(S1)
          and all(row_agrees(rows[n], header, S1[key_of[n]]) for n in rows), f"{key_of}")
    notes = dict(zip(header, rows[UBI]))["notes"]
    check("[2] UBI's notes name the three-way tie at 14.5/26", "Mutual Credit/LETS and Ostrom-Style Commons "
          "Governance at 14.5/26" in notes and "(7 failures vs. 3 and 3)" in notes)
    rev = dict(zip(header, rows[OS]))["revision_note"]
    check("[2] Ostrom's revision note records decision D26", rev.startswith("REVISED Session 33 (decision D26"))

    # [3] the corpus file
    ca, cb = json.load(open(pinned(*SNAP["corpus"]), encoding="utf-8")), json.load(open(path(NOW["corpus"]), encoding="utf-8"))
    check("[3] neec_corpus.json: only Ostrom's C3.2 differs", corpus_diff(ca, cb) == [f"{OS}: C3.2 0.0 -> 0.5"],
          f"{corpus_diff(ca, cb)}")
    check("[3] neec_corpus.json carries the canonical vectors", all(
        e["vector"] == S1[e["key"]] for e in cb["entries"]) and len(cb["entries"]) == 23)

    # [4] the corpus, before and after
    check("[4] Ostrom: 14.0/26, 4 failures -> 14.5/26, 3 failures; tier unchanged (Partially Adequate)",
          (total(S0, OS), nfail(S0, OS), total(S1, OS), nfail(S1, OS)) == (14.0, 4, 14.5, 3)
          and old.tier(4) == new.tier(3) == "Partially Adequate")
    check("[4] ties: with SWF Statism and Singapore at 14.0 -> with Mutual Credit / LETS and UBI at 14.5",
          ties(S0, OS) == ["Sovereign Wealth Fund Statism", "State Capitalism / Singapore"] and ties(S1, OS) == [MC, UBI])
    check("[4] SWF Statism and Singapore still tie each other at 14.0, and are the only entries there",
          ties(S1, "Sovereign Wealth Fund Statism") == ["State Capitalism / Singapore"])
    check("[4] no strict-dominance pair gained or lost (14 ordered pairs)", pairs(S0) == pairs(S1) and len(pairs(S1)) == 14)
    check("[4] the Pareto frontier is unchanged (12 systems, Ostrom among them)",
          front(S0) == front(S1) and len(front(S1)) == 12 and OS in front(S1))
    tiers = lambda S, m: sorted((m.tier(nfail(S, k)), k) for k in S)
    check("[4] every entry's tier is unchanged (6 Potentially, 8 Partially, 9 Structurally Inadequate)",
          tiers(S0, old) == tiers(S1, new) and sorted(t for t, _ in tiers(S1, new)).count("Partially Adequate") == 8)
    check("[4] Ostrom's competition rank 10 -> 8; SWF Statism's and Singapore's 10 -> 11", (rank(S0, OS), rank(S1, OS)) == (10, 8)
          and rank(S1, "Sovereign Wealth Fund Statism") == rank(S1, "State Capitalism / Singapore") == 11)
    check("[4] entries at 0.0 on C3.2: Ostrom alone -> none", [k for k in S0 if S0[k]["C3.2"] == 0.0] == [OS]
          and not [k for k in S1 if S1[k]["C3.2"] == 0.0])

    # [5] negative tests
    bad = copy.deepcopy(S1)
    bad["Integral"]["C1.1"] = 0.5 if bad["Integral"]["C1.1"] != 0.5 else 1.0
    check("[5] a second changed cell is rejected by the one-cell test", cell_diff(S0, bad) != [(OS, "C3.2", 0.0, 0.5)])
    r = list(rows[OS])
    r[header.index("total_score")] = "14.0"
    check("[5] a CSV row that disagrees with the vector is rejected", not row_agrees(r, header, S1[OS]))
    cbad = copy.deepcopy(cb)
    cbad["entries"][0]["vector"]["C5.5"] = 0.0 if cbad["entries"][0]["vector"]["C5.5"] else 1.0
    check("[5] a corpus file with another change is rejected", corpus_diff(ca, cbad) != [f"{OS}: C3.2 0.0 -> 0.5"])

    print("=" * 96)
    print("verify_insertion_s33.py -- decision D26 (Session 33) against the Session 32 corpus")
    print("=" * 96)
    print(f"Session 33: {NOW['canon']}, {NOW['csv']}, {NOW['corpus']}; Session 32: "
          f"{', '.join(f'{n} (md5 {m})' for n, m in SNAP.values())}")
    for label, ok, detail in RESULTS:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok and detail:
            print(f"        {detail}")
    npass = sum(1 for r in RESULTS if r[1])
    print(f"\nSUMMARY: {npass} passed, {len(RESULTS) - npass} failed (of {len(RESULTS)}).")
    return 0 if npass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
