#!/usr/bin/env python3
"""
jev_pilot_check.py -- the Jev pilot of 2026-09-25: an automated interpretation check (label adopted by the owner)
================================================================================================================
Jev (TypeSafe AI's System One model, jev-1.13.0) was asked, clause by clause, whether a text meets a NEEC clause,
and its answers were compared with the rescoring pass's clause statuses. This script reads the recorded requests and
responses (jev_pilot_2026-09-25.json); it makes no network call, so it is deterministic and can join the harness.

CHECKS: every record is present and answered by jev-1.13.0; every state the pilot drew from Report v1.6 equals the
Report's text with the score removed; every evidence state drawn from a pass record is contained in that record, except
the two edits the record declares; each part's comparison with the pass statuses (UNITS in rescoring_s37.py to
rescoring_s48.py, the latest record of each unit governing). Prints the tables. Writes nothing.

Usage: python3 jev_pilot_check.py   (reads jev_pilot_2026-09-25.json, NEEC_Report_v1_6.md, rescoring_s37.py to
                                     rescoring_s48.py and the files they read, beside itself)
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA, REPORT = "jev_pilot_2026-09-25.json", "NEEC_Report_v1_6.md"
PASS = (37, 38, 39, 40, 41, 42, 43, 47, 48)
ORDER = ["SQ", "NSD", "CPS", "MS", "LM", "MMT", "UBI", "DG", "SC", "FALC", "PE", "CCO", "INT", "GEO", "MC"]
C21_UNITS = ["CCO", "DG", "FALC", "INT", "MS", "NSD", "PE", "UBI"]
C44_UNITS = ["CCO", "INT", "MS", "NSD", "PE", "DG"]
MAP1 = {"C": "asserted_met", "S": "asserted_short", "U": "not_asserted"}
MAP2 = {"C": "shown", "U": "not_shown"}
# Declared edits to evidence states (pilot record, section 2): the pass's wording states the verdict, or joins
# evaluation to the evidence, so the state keeps the facts only.
EDITED = {("p2a", "NSD"): "fact kept, verdict phrase ('parliamentary removal functions') and cross-reference removed",
          ("p2b", "CCO"): "OpenResearch findings kept; the pass's evaluative clauses and citations removed"}
FAILS = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAILS.append(msg)


def report_texts(crit, name_re):
    lines = open(os.path.join(HERE, REPORT), encoding="utf-8").read().split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("## **%s " % crit)]
    out = {}
    for code, i in zip(ORDER, idx):
        body, j = [lines[i]], i + 1
        while j < len(lines) and not lines[j].startswith("## ") and not re.match(r"^\d+\. ##", lines[j]):
            body.append(lines[j])
            j += 1
        m = re.match(r"## \*\*%s %s: ([0-9.]+)\*\*\s*(.*)" % (re.escape(crit), name_re), "\n".join(body).strip(), re.S)
        out[code] = m.group(2).strip()
    return len(idx), out


def pass_units():
    units = {}
    for n in PASS:
        spec = importlib.util.spec_from_file_location("rescoring_s%d" % n, os.path.join(HERE, "rescoring_s%d.py" % n))
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        units.update(mod.UNITS)
    return units


def rng(vals):
    lo, hi = min(vals), max(vals)
    return "%.2f" % lo if lo == hi else "%.2f-%.2f" % (lo, hi)


def compare(title, recs, units, key, mapping, status_of):
    print("\n" + title)
    print("  %-5s %-14s %-15s %-13s %-12s %s" % ("unit", "pass", "Jev (modal)", "P(choice)", "confidence", "agree"))
    agree = n = 0
    for u in units:
        rs = [r for r in recs if r["unit"] == u]
        choices = {r["response"]["answers"][key]["choice"] for r in rs}
        check(len(choices) == 1, "%s %s: the same choice in all %d runs" % (u, key, len(rs)))
        ch = choices.pop()
        probs = [r["response"]["answers"][key]["probabilities"][ch] for r in rs]
        conf = [r["response"]["answers"][key]["confidence"] for r in rs]
        st = status_of(u)
        ok = mapping[st] == ch
        agree += ok
        n += 1
        print("  %-5s %-14s %-15s %-13s %-12s %s" % (u, st + " " + mapping[st], ch, rng(probs), rng(conf),
                                                    "yes" if ok else "NO"))
    print("  agreement: %d of %d" % (agree, n))
    return agree, n


def main():
    d = json.load(open(os.path.join(HERE, DATA), encoding="utf-8"))
    recs = d["records"]
    check(d["label"] == "automated interpretation check", "the pilot carries the adopted label")
    check(len(recs) == 54, "54 records (pilot 1: 3 runs x 8; pilot 2: 2 runs x 15)")
    check(all(r["error"] is None and r["response"]["model"] == "jev-1.13.0" for r in recs),
          "every record answered, by jev-1.13.0")
    part = lambda p: [r for r in recs if r["part"] == p]

    n21, c21 = report_texts("C2.1", "Freedom from Coercion")
    n44, c44 = report_texts("C4.4", r"[^:]*")
    check(n21 == 15 and n44 == 15, "Report v1.6: 15 C2.1 and 15 C4.4 rationales, in system order")
    check(all(r["request"]["state"]["rationale"] == c21[r["unit"]] for r in part("p1") + part("p2c")),
          "pilot 1 and part (c) states equal Report v1.6's C2.1 rationales, score removed")
    dg = [r for r in part("p2a") if r["unit"] == "DG"]
    check(all(r["request"]["state"]["evidence"] == c44["DG"] for r in dg),
          "part (a) DG state equals Report v1.6's DG C4.4 rationale, score removed")

    units = pass_units()
    norm = lambda s: re.sub(r"\s+", " ", s).strip().rstrip(".").lower()
    for u in ["CCO", "INT", "MS", "PE"]:
        ev = {r["request"]["state"]["evidence"] for r in part("p2a") if r["unit"] == u}
        src = units[(u, "C4.4")]["clauses"][1][1]
        check(len(ev) == 1 and norm(ev.pop()) in norm(src), "part (a) %s state is contained in the pass's C4.4 clause 2 "
                                                             "record" % u)
    for k, why in sorted(EDITED.items()):
        print("NOTE declared edit, %s %s: %s" % (k[0], k[1], why))

    s = lambda crit, i: (lambda u: units[(u, crit)]["clauses"][i][0])
    a1 = compare("PILOT 1, C2.1 clause 1 (Report v1.6 rationale; 3 runs)", part("p1"), C21_UNITS, "clause1", MAP1,
                 s("C2.1", 0))
    a2 = compare("PILOT 1, C2.1 clause 2 (Report v1.6 rationale; 3 runs)", part("p1"), C21_UNITS, "clause2", MAP2,
                 s("C2.1", 1))
    a3 = compare("PILOT 2 (a), C4.4 clause 2 (evidence; 2 runs)", part("p2a"), C44_UNITS, "clause2", MAP2,
                 s("C4.4", 1))
    a4 = compare("PILOT 2 (c), C2.1 clause 1, revised wording (Report v1.6 rationale; 2 runs)", part("p2c"), C21_UNITS,
                 "clause1", MAP1, s("C2.1", 0))
    b = part("p2b")
    print("\nPILOT 2 (b), C2.1 clause 2 decomposed (CCO component evidence; 2 runs)")
    print("  behaviour reported:              noul %s" % rng([r["response"]["answers"]["behaviour"]["noul"] for r in b]))
    print("  self-report compared:            noul %s" % rng([r["response"]["answers"]["self_report_compared"]["noul"]
                                                             for r in b]))
    print("  clause 2:                        %s" % sorted({r["response"]["answers"]["clause2"]["choice"] for r in b}))
    print("  pass status (CCO C2.1 clause 2): %s" % units[("CCO", "C2.1")]["clauses"][1][0])
    check(all(r["response"]["answers"]["clause2"]["choice"] == "not_shown" for r in b),
          "part (b) agrees with the pass (not shown)")

    carried = [u for u in C21_UNITS if units[(u, "C2.1")]["clauses"][0][2].startswith("as audited")]
    print("\nC2.1 clause 1 statuses carried 'as audited' (rescoring s37, section 2): %s" % ", ".join(carried))
    print("SUMMARY: pilot 1 %d of %d; part (a) %d of %d; part (b) 1 of 1; part (c) %d of %d; %d checks failed"
          % (a1[0] + a2[0], a1[1] + a2[1], a3[0], a3[1], a4[0], a4[1], len(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
