#!/usr/bin/env python3
"""
rescoring_s40.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), third group: C1.1 Poverty Elimination
Capacity, its nine part (b) units
==============================================================================================================
Session 40. Parts (a), (b1) and (b2) are NEEC_Rescoring_s37.md, NEEC_Rescoring_s38.md and NEEC_Rescoring_s39.md
(rescoring_s37.py, rescoring_s38.py, rescoring_s39.py). This script holds the third group: C1.1's nine 1.0s, whose
stress clause (">=85% under stress testing") the R4 audit coded silent on every unit. CCO-PTF-CIP-SZH's base clause
is tested against the design's own published model (part (b1), decision 3.2), whose runs are
cco_simulation_checks_s40.js and its captured output. It changes no file and no score: the pass's changes are applied
by generator when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). A clause the audit coded A is
carried as cleared on the unit's own text, except where listed in EXCEPT with its reason; the script asserts that
every departure from the audit's A codes is listed, and every listed one occurs.

CHECKS: the group against the audit's register (C1.1's nine part (b) units); every record complete; the rule; the
audit's codes carried or excepted; reach; flags against the summary blocks, cumulatively with parts (a), (b1) and
(b2); the consequences of the pass so far (totals, ranks, failures, tiers, dominance, frontier, what remains, the
C1.1 1.0s left); the anchor examples the pass so far moves; the pinned simulation runs the record quotes; and that
NEEC_Rescoring_s40.md contains every generated table verbatim.

Usage: python3 rescoring_s40.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, rescoring_s37.py,
                                   rescoring_s38.py, rescoring_s39.py and the files they read,
                                   cco_simulation_checks_s40_output.txt and NEEC_Rescoring_s40.md beside itself;
                                   writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, AUDIT = "criteria.json", "neec_corpus.json", "r4_audit_s35.py"
PART_A, PART_B1, PART_B2, RECORD = "rescoring_s37.py", "rescoring_s38.py", "rescoring_s39.py", "NEEC_Rescoring_s40.md"
SIMOUT = "cco_simulation_checks_s40_output.txt"
SIM_MD5 = "035d1be82ab497e76a234615a04c0ce9"     # harness.js at BetterToBest/compassionism-simulation cd0ceec (v4.15)
IDX_MD5 = "1c8273b13b2c22763a44c051ca7bd882"     # index.html at the same commit (the two recession functions)
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
HUB = "research-hub at 8e8a6ba (2026-09-21), "
SIM = "compassionism-simulation at cd0ceec (v4.15), harness.js and index.html; " + SIMOUT
RB1, RB2 = "NEEC_Rescoring_s38.md, ", "NEEC_Rescoring_s39.md, "

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in Appendix B's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- departures from the audit's A codes, each with its reason (asserted both ways) ------------------------------
EXCEPT = {
    ("CCO", "C1.1", 0): "the design's own published model contradicts the text's 98% (reading 3.3)",
}

# ---- C1.1 Poverty Elimination Capacity (readings 3.1-3.4) -------------------------------------------------------
U("NSD", "C1.1", 0.5, [
    ("C", "Achieves 94-96% poverty elimination", AUD),
    ("U", "Finland's 1991-93 depression is the documented stress episode (GDP down about 10% in three years, "
          "unemployment from about 3% to 16%): relative poverty did not rise and fell slightly, partly because the "
          "median and so the line fell, while social-assistance receipt doubled, the lowest decile's real income fell "
          "and in real terms poverty increased; C1.1 measures absolute poverty against a basket of necessities, and no "
          "reduction rate on that measure is located for the stress years (readings 3.1, 3.2)",
     "Uusitalo, Social policy in a deep economic recession and after: the case of Finland, ISSA Research "
     "Conference, Helsinki (2000); Uusitalo, Economic Crisis and Social Policy in Finland in the 1990s, SPRC "
     "Discussion Paper 70, UNSW (1996)")],
  flag=([1.0], "on the relative measure, which the unit's own 94-96% figure appears to use, poverty held through "
               "the deepest downturn a Nordic economy has had, as transfers absorbed the fall in factor incomes"),
  note="Report v1.6's 94-96% is unsourced and does not state its measure; it is C1.1's 1.0 anchor example "
       "(section 6)")
U("CPS", "C1.1", 0.5, [
    ("C", "near-universal elimination of absolute poverty", AUD),
    ("S", "Cuba's Special Period (1990-95), after the loss of Soviet support, is a documented stress episode in a "
          "centrally planned economy with universal rationing: per capita daily energy intake fell from 2,899 to "
          "1,863 kcal and average adult weight by 4-5 kg, a neuropathy outbreak, possibly due to vitamin "
          "deficiencies, affected about 50,000 people in 1992-93, and the decline in infant mortality reversed in "
          "1990-93; a special rationing system shielded children, elderly people and pregnant women from the "
          "outbreak, but a basic necessity, food, fell short for the adult population at large",
     "Franco, Ordunez, Caballero and Cooper, CMAJ 178(8) (2008); Franco et al., American Journal of Epidemiology "
     "166 (2007)")])
U("MS", "C1.1", 0.5, [
    ("C", "demonstrate poverty elimination capacity", AUD),
    ("U", "the documented stress episode is Spain's 2008-13 crisis: Fagor Electrodomesticos, the group's founding "
          "cooperative, failed in 2013 with about 5,700 employees; the group's mechanisms (relocation, early "
          "retirement, Lagun-Aro) covered its 1,898 members, of whom 417 were relocated within two months with "
          "solutions aimed at 1,000-1,200, while non-member employees of its subsidiaries were outside them; no "
          "poverty-reduction figure under stress is located for members or for the wider workforce (reading 3.1)",
     "The Local (14 November 2013); CECOP, relaying Mondragon Corporation (2014); Learning from the Bankruptcy of "
     "Fagor Electrodomesticos, reflections at the 2015 CIRIEC conference")])
U("MMT", "C1.1", 0.5, [
    ("C", "Near-universal poverty elimination achievable", AUD),
    ("U", "no estimate of poverty reduction under stress is stated or cited; the guarantee is specified as "
          "countercyclical, which is a mechanism, not an estimate of the level (reading 3.1); the one crisis-tested "
          "precedent of the component, Argentina's Plan Jefes y Jefas in the 2002 crisis, in which poverty rose from "
          "37% to 58%, cut the share of participants falling into indigence from an estimated 40% to 30%",
     REP + "MMT C1.1 and C3.1; Galasso and Ravallion, World Bank Economic Review 18(3) (2004)")],
  note="Jefes targeted unemployed heads of households with dependents, so it calibrates confidence in the "
       "component (protocol 4.1) rather than estimating the design")
U("UBI", "C1.1", 0.5, [
    ("C", "would achieve 95%+ elimination", AUD),
    ("U", "no estimate under stress is stated or cited; the payment is specified as unconditional and fixed, part "
          "(b2) found no rule raising it with crisis severity, and Alaska's dividend, the long-running precedent, is "
          "set on an annual cycle (reading 3.1)",
     REP + "UBI C1.1; " + RB2 + "UBI C3.1; " + RB1 + "UBI C3.4")])
U("DG", "C1.1", 0.5, [
    ("C", "could eliminate poverty", AUD),
    ("U", "the rationale names instruments (wealth caps, maximum income ratios, universal basic services) that "
          "could eliminate poverty; no stress scenario or estimate is stated or cited (reading 3.1)",
     REP + "DG C1.1")])
U("FALC", "C1.1", 0.5, [
    ("C", "Theoretical capacity for 100% poverty elimination", AUD),
    ("U", "the rationale conditions its figure on technological assumptions proving correct; no scenario in which "
          "they fall short, this entry's stress case, is estimated (reading 3.1)",
     REP + "FALC C1.1")])
U("PE", "C1.1", 0.5, [
    ("C", "would eliminate poverty", AUD),
    ("U", "remuneration by effort and sacrifice and universal access to consumption councils are specified; no "
          "stress scenario or estimate is stated or cited (reading 3.1)",
     REP + "PE C1.1")])
U("CCO", "C1.1", 0.5, [
    ("S", "on the design's own published model (reference preset, 20 years, 100 seeds), wealth poverty falls 78.5% "
          "and BLEI poverty 82.1% against the paired Baseline, and no seed reaches 90% on either; against year 0 "
          "wealth poverty falls 59.3% and BLEI poverty rises; the engine's lowest tier, BLEI Crisis, gives 87.4%; "
          "the rationale's 98% is the design's parameter file's stated outcome for a Basic Unit of $1,200, octave "
          "6, 78% participation and 20% PTH uptake, the engine's own reference settings; the model that produced it "
          "is not published in runnable form, the modelling paper measures poverty below 60% of median income, and "
          "the engine carries the papers' headline median wealth, $82,000, as a target (reading 3.3)",
     SIM + "; " + HUB + "data/optimal-parameters.json (v1.0.0, 2025-09-18), economic-modeling-simulation.html "
     "and cco-ptf-integrated-framework.html"),
    ("S", "with the engine's adverse channels on at the reference settings (recessions, AI automation and 2% "
          "inflation, paired with the Baseline as the engine pairs them) the reductions are 56.4% and 60.0%; "
          "recessions alone give 77.8% and 81.6%, automation alone 69.4% and 72.3%, and the engine's own Stress "
          "Test preset 31.0% and 32.6%; at most 4 of 100 seeds reach 85% on a documented measure in any stress run "
          "(reading 3.4)",
     SIM)],
  flag=([1.0], "the design's hub papers' modelled figures credited at the modelling tier instead of the published "
               "engine: 98% reduction in the base case, and poverty below 3% in 87% of recession scenarios"),
  note="neither of the engine's headcounts is C1.1's basket measure; they are read as the model presents them. The "
       "unit reopens if a later version of the simulation reaches 90% in the reference run and 85% in the stress "
       "run on its documented measures, or if the model behind the papers' figures is published and reproduces them")

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 9, "stand": [], "points": 4.5, "flags_added": [("NSD", "C1.1"), ("CCO", "C1.1")],
          "flags_removed": [], "remaining": 58, "dominance_b2": 18, "frontier_b2": 12, "anchors_moved": 6,
          "c11_left": 0}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables(rs, r4, cdef, order, names, base, ma, mb, m2, after, left):
    t = {}
    f1, fmt = rs.f1, rs.fmt_alts
    rows = ["| Entry | Criterion | Clauses | Verdict | Flag |", "|---|---|---|---|---|"]
    for key in order:
        rec = UNITS[key]
        fl = f"alternative {fmt(rec['flag'][0])}" if rec["flag"] else ""
        rows.append(f"| {key[0]} | {key[1]} | {' '.join(st for st, _, _ in rec['clauses'])} | "
                    f"1.0 → {f1(rec['verdict'])} | {fl} |")
    t["summary"] = "\n".join(rows)
    for key in order:
        rec, (code, crit) = UNITS[key], key
        head = f"#### {code} {crit} {cdef[crit]['name']}: 1.0 → {f1(rec['verdict'])}"
        if rec["flag"]:
            head += " — flagged as contestable"
        lines = [head, "", "| # | Clause | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for k, (st, est, src) in enumerate(rec["clauses"]):
            lines.append(f"| {k + 1} | {r4.CLAUSES[crit][k][0]} | {STATUS[st]} | {est} | {src or '—'} |")
        if rec["flag"]:
            lines += ["", f"*Flag:* alternative {fmt(rec['flag'][0])}: {rec['flag'][1]}."]
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {code} {crit}"] = "\n".join(lines)
    rb, rn = rs.ranks(base["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After (a) | After (b1) | After (b2) | After this group (rank) | Change here | "
            "Failures | Tier | D28 units left | Floor if all fall |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|"]
    for code in rs.order_codes(names, base):
        lf = left.get(code, 0)
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(ma['total'][code])} | "
                    f"{f1(mb['total'][code])} | {f1(m2['total'][code])} | {f1(after['total'][code])} ({rn[code]}) | "
                    f"{f1(after['total'][code] - m2['total'][code])} | {after['fail'][code]} | "
                    f"{rs.tier(after['fail'][code])} | {lf} | {f1(after['total'][code] - 0.5 * lf)} |")
    t["consequences"] = "\n".join(rows)
    return t


def sim_tables(text):
    """The Markdown tables of the simulation runs, as printed."""
    blocks, cur = [], []
    for line in text.split("\n"):
        if line.startswith("|"):
            cur.append(line)
        elif cur:
            blocks.append("\n".join(cur))
            cur = []
    if cur:
        blocks.append("\n".join(cur))
    return blocks


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    r4 = load("r4_audit_s35", AUDIT)
    rs = load("rescoring_s37", PART_A)
    rb = load("rescoring_s38", PART_B1)
    rc = load("rescoring_s39", PART_B2)
    crit = json.loads(rs.read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}
    prior = (rs.UNITS, rb.UNITS, rc.UNITS)

    print(f"NEEC rescoring pass, part (b), third group: C1.1 ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {AUDIT}, {PART_A}, {PART_B1}, {PART_B2}, {SIMOUT}, {RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    done = set(rs.UNITS) | set(rb.UNITS) | set(rc.UNITS)
    partb = [k for k in d28 if k not in rs.UNITS]
    c11 = [k for k in partb if k[1] == "C1.1" and k not in done]
    check(len(d28) == 134 and len(partb) == 101 and not (set(rb.UNITS) | {k for k in rc.UNITS if k[1] == "C3.1"})
          - set(partb), "D28's population 134; part (b) 101; parts (b1) and (b2)'s D28 units inside it")
    check(sorted(UNITS) == sorted(c11) and len(c11) == EXPECT["units"] and all(vec[c][k] == 1.0 for c, k in UNITS)
          and not set(UNITS) & done,
          f"this group holds exactly C1.1's {len(c11)} part (b) units, every one a corpus 1.0 and none re-estimated "
          f"before")
    print("  C1.1: " + ", ".join(c for c, _ in c11))

    # [2] records --------------------------------------------------------------------------------------------------
    print("\n[2] THE RECORDS")
    bad, tally = [], {k: 0 for k in STATUS}
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(r4.CLAUSES[key[1]]):
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {len(r4.CLAUSES[key[1]])}")
        for k, (st, est, src) in enumerate(rec["clauses"]):
            tally[st] = tally.get(st, 0) + 1
            if st not in STATUS or not est.strip():
                bad.append(f"{key} clause {k + 1}: status {st!r} or empty estimate")
            if st in "CSRM" and not src.strip():
                bad.append(f"{key} clause {k + 1}: {STATUS.get(st, st)} without a source or reason")
            if "|" in est + src + (rec["flag"][1] if rec["flag"] else "") + rec["note"]:
                bad.append(f"{key} clause {k + 1}: a pipe character would break the table")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per clause, in Appendix B's order; every cleared, short, out-of-reach "
                   "and moot clause carries its source or reason")
    print("  clause statuses: " + ", ".join(f"{STATUS[k]} {v}" for k, v in tally.items()))

    # [3] the rule -------------------------------------------------------------------------------------------------
    print("\n[3] THE RULE (D28)")
    wrong = [k for k, r in UNITS.items() if rs.verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong, "every verdict follows D28: 1.0 only if every clause is cleared or moot, otherwise 0.5",
          str(wrong))
    check(all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()), "no unit is scored 0.0 in this pass (D28(f))")
    stand = sorted(k for k, r in UNITS.items() if r["verdict"] == 1.0)
    points = sum(1.0 - r["verdict"] for r in UNITS.values())
    check(stand == sorted(EXPECT["stand"]) and points == EXPECT["points"],
          f"{len(stand)} of {len(UNITS)} stand; {len(UNITS) - len(stand)} become 0.5 ({rs.f1(points)} points)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    departs = {(k[0], k[1], i) for k, r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"])
               if (reg[k][i] == "A" and st != "C") or (reg[k][i] == "N" and st != "M")}
    listed_a = {x for x in EXCEPT if reg[(x[0], x[1])][x[2]] == "A"}
    check(departs == set(EXCEPT) == listed_a,
          f"every departure from the audit's A codes is listed with its reason ({len(departs)} departure, "
          f"{len(EXCEPT)} listed); every other A clause is carried as cleared")
    for (c, k, i), why in sorted(EXCEPT.items()):
        print(f"  {c} {k} clause {i + 1}: {STATUS[UNITS[(c, k)]['clauses'][i][0]]} ({why})")
    silent = {(k[0], k[1], i) for k in UNITS for i, ch in enumerate(reg[k]) if ch == "S"}
    check(len(silent) == 9 and all(i == 1 for _, _, i in silent),
          "the audit coded the stress clause silent on all nine units, and each is estimated here")

    # [4] reach ----------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = {x for x in r4.REACH if (x[0], x[1]) in UNITS}
    check(now_r == was_r == set(), "no clause of this group is out of reach, and none was coded so")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a), (b1) and (b2))")
    blocks = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}

    def changes(units):
        add = sorted(k for k, r in units.items() if r["flag"] and k not in had)
        rem = sorted(k for k, r in units.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
        return add, rem
    added, removed = changes(UNITS)
    kept = sorted(k for k in UNITS if k in had and k not in removed)
    check(added == sorted(EXPECT["flags_added"]) and removed == sorted(EXPECT["flags_removed"]) and not kept,
          f"flags added {len(added)} (" + ", ".join(" ".join(k) for k in added) + f"); removed {len(removed)}")
    adds, rems = list(added), list(removed)
    for part in prior:
        a, r = changes(part)
        adds += a
        rems += r
    moved = sorted({k[0] for k in adds + rems})
    for code in moved:
        n0 = len(blocks[code]["flags"])
        n1 = n0 + sum(1 for k in adds if k[0] == code) - sum(1 for k in rems if k[0] == code)
        print(f"  {code}: {n0} flags -> {n1} after parts (a), (b1), (b2) and (b3)")
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Across the pass so far, "
                 f"{len(moved)} entries' flag registers change ({', '.join(moved)}).")
    print("  " + flag_line)

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    steps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in steps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        steps.append(v)
    vec0, va, vb, v2, vn = steps

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    base, ma, mb, m2, after = (summ(x) for x in steps)
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    left_units = [k for k in partb if k not in done and k not in UNITS]
    left, per = {}, {}
    for c, k in left_units:
        left[c] = left.get(c, 0) + 1
        per[k] = per.get(k, 0) + 1
    check(len(left_units) == EXPECT["remaining"], f"{len(left_units)} D28 units remain for part (b)")
    rem_line = (f"Left for part (b): {len(left_units)} D28 units (" +
                ", ".join(f"{k} {per[k]}" for k in cids if k in per) + ").")
    print("  " + rem_line)
    c11_left = sorted(c for c in vn if vn[c]["C1.1"] == 1.0)
    check(len(c11_left) == EXPECT["c11_left"],
          f"entries scoring 1.0 on C1.1 after this group: {len(c11_left)} (published: "
          f"{sum(1 for c in vec if vec[c]['C1.1'] == 1.0)})")
    p2, f2 = rs.dominance(v2, cids)
    pn, fn = rs.dominance(vn, cids)
    check(len(p2) == EXPECT["dominance_b2"] and len(f2) == EXPECT["frontier_b2"],
          f"part (b2)'s result reproduced: {len(p2)} dominance pairs, frontier {len(f2)}")
    order = list(names)
    gained = sorted(set(pn) - set(p2), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(p2) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    allparts = prior + (UNITS,)
    n_all = sum(len(p) for p in allparts)
    st_all = sum(1 for p in allparts for r in p.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for p in allparts for r in p.values())
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(p2)} after part (b2) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(f2)} (" + ", ".join(c for c in order if c in fn) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(m2['total'][first[0]])} after part (b2), "
                f"{rs.f1(after['total'][first[0]])} now. Across parts (a), (b1), (b2) and (b3), {n_all} units have been "
                f"re-estimated: {st_all} stand and {n_all - st_all} become 0.5 ({rs.f1(pts_all)} points). No entry "
                f"now scores 1.0 on C1.1.")
    print("  " + dom_line)

    # [7] anchors --------------------------------------------------------------------------------------------------
    print("\n[7] ANCHOR EXAMPLES THE PASS SO FAR MOVES (build_criteria.py checks examples against published scores)")
    code_of = {v: k for k, v in names.items()}
    allu, part_of = {}, {}
    for tag, p in zip(("(a)", "(b1)", "(b2)", "(b3)"), allparts):
        allu.update(p)
        part_of.update({k: tag for k in p})
    hits = []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                code = code_of.get(ex["system"])
                if code and (code, c["id"]) in allu and allu[(code, c["id"])]["verdict"] != ex["cited"]:
                    hits.append(f"{c['id']}'s {band} example, {code} (part {part_of[(code, c['id'])]}, to "
                                f"{rs.f1(allu[(code, c['id'])]['verdict'])})")
    check(len(hits) == EXPECT["anchors_moved"], f"{len(hits)} anchor examples cite a unit the pass moves")
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) +
                   ". When the pass is applied, each band needs an example the corpus then scores at that value; "
                   "C1.1's 1.0 band has none left (reading 3.5).")
    print("  " + anchor_line)

    # [8] the simulation runs --------------------------------------------------------------------------------------
    print(f"\n[8] THE SIMULATION RUNS ({SIMOUT})")
    sim = rs.read(SIMOUT)
    check(f"harness.js md5 {SIM_MD5}" in sim and f"index.html md5 {IDX_MD5}" in sim,
          f"runs made on the pinned engine: harness.js md5 {SIM_MD5}, index.html md5 {IDX_MD5} "
          f"(compassionism-simulation cd0ceec, v4.15)")
    check("median BLEI 1965 d, wealth poverty 16.6%, Gini 0.534, System Stability 88.5%" in sim
          and "  FAIL" not in sim and "ALL CHECKS PASSED" in sim,
          "the captured run reproduced the documented seed-42 reference run and passed its own checks")
    simt = sim_tables(sim)
    check(len(simt) == 2, "two run tables read (poverty reduction by scenario; temporal tracking)")

    # [9] the record -----------------------------------------------------------------------------------------------
    print(f"\n[9] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    t = tables(rs, r4, cdef, unit_order, names, base, ma, mb, m2, after, left)
    t["dominance"], t["remaining"], t["flags"], t["anchors"] = dom_line, rem_line, flag_line, anchor_line
    t["simulation run 1"], t["simulation run 2"] = simt[0], simt[1]
    GENERATED.clear()
    GENERATED.update(t)
    record = rs.read(RECORD) if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING PART (B), THIRD GROUP, COMPUTED." if ok else "\nRESCORING PART (B), THIRD GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
