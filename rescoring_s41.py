#!/usr/bin/env python3
"""
rescoring_s41.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), fourth group: C1.4 Automation
Resilience, C2.1 Freedom from Coercion and C3.2 Inflation Control Mechanisms, their eleven part (b) units
==============================================================================================================
Session 41. Parts (a), (b1), (b2) and (b3) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s40.md (rescoring_s37.py to
rescoring_s40.py). This script holds the fourth group: C1.4's two part (b) units (both clauses levels under
displacement scenarios), C2.1's five (the revealed-preference clause, a method clause) and C3.2's four (the stress
clause, and for two configured national economies the automatic-adjustment clause). It changes no file and no
score: the pass's changes are applied by generator when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). A clause the audit coded A is
carried as cleared on the unit's own text, except where listed in EXCEPT with its reason (none in this group); the
script asserts that every departure from the audit's A codes is listed, and every listed one occurs. A clause
marked "not estimated in this pass" is allowed only where another clause of the same unit already fixes the verdict.

CHECKS: the group against the audit's register (the part (b) units of C1.4, C2.1 and C3.2); every record complete;
the rule; the audit's codes carried or excepted; every silent clause estimated or validly left; reach; flags
against the summary blocks, cumulatively with parts (a) to (b3); the consequences of the pass so far (totals,
ranks, failures, tiers, dominance, frontier, what remains, the 1.0s each of the group's criteria keeps); the anchor
examples the pass so far moves and the bands left with no corpus unit; and that NEEC_Rescoring_s41.md contains
every generated table verbatim.

Usage: python3 rescoring_s41.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, rescoring_s37.py to
                                   rescoring_s40.py and the files they read, and NEEC_Rescoring_s41.md beside
                                   itself; writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, AUDIT = "criteria.json", "neec_corpus.json", "r4_audit_s35.py"
PRIOR = (("(a)", "rescoring_s37", "rescoring_s37.py"), ("(b1)", "rescoring_s38", "rescoring_s38.py"),
         ("(b2)", "rescoring_s39", "rescoring_s39.py"), ("(b3)", "rescoring_s40", "rescoring_s40.py"))
RECORD = "NEEC_Rescoring_s41.md"
GROUP = ("C1.4", "C2.1", "C3.2")
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
NOTEST = "not estimated in this pass"
IMF = "IMF, World Economic Outlook Update (July 2023)"

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in Appendix B's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- departures from the audit's A codes, each with its reason (asserted both ways) ------------------------------
EXCEPT = {}

# ---- C1.4 Automation Resilience (reading 3.2) -------------------------------------------------------------------
U("FALC", "C1.4", 0.5, [
    ("U", "the rationale states the design's premise, an economy in which human labour is optional; no poverty level "
          "under a 30%, 50% or 70% displacement scenario is stated or cited, and none is located in the design's "
          "literature (reading 3.2)",
     REP + "FALC C1.4"),
    ("U", "no level of aggregate demand under any displacement scenario is stated or cited (reading 3.2)",
     REP + "FALC C1.4")])
U("PE", "C1.4", 0.5, [
    ("C", "while maintaining consumption access", AUD),
    ("U", "remuneration by effort and sacrifice, with an average income for those who cannot work, is specified, and "
          "the rationale says the gains of automation could be distributed through reduced hours; no level of "
          "consumption or demand under a 30%, 50% or 70% displacement scenario is stated or cited, and none is "
          "located in the model's literature (reading 3.2)",
     REP + "PE C1.4; Albert, Summarizing Participatory Economics, ZNetwork (31 August 2022)")],
  note="the audit read the rationale's \"consumption access\" as its poverty clause; read as demand instead, it is a "
       "design statement, not a level under a stated scenario, so the verdict is the same")

# ---- C2.1 Freedom from Coercion (reading 3.3) -------------------------------------------------------------------
U("DG", "C2.1", 0.5, [
    ("C", "provide genuine autonomy in how to spend time", AUD),
    ("U", "universal basic services, reduced working hours and commons access are specified; no observed behaviour "
          "of a population the design serves, or of one a component serves, is compared with self-reported autonomy "
          "(reading 3.3)",
     REP + "DG C2.1")])
U("FALC", "C2.1", 0.5, [
    ("C", "Post-scarcity eliminates economic coercion entirely", AUD),
    ("U", "the rationale rests on post-scarcity abundance, which has no implementation whose participants' behaviour "
          "could be observed; no behavioural validation is stated or located (reading 3.3)",
     REP + "FALC C2.1")])
U("PE", "C2.1", 0.5, [
    ("C", "eliminates both market and state coercion", AUD),
    ("U", "consumption councils and democratic planning are specified; no implementation of the model as specified is "
          "cited or located, so no participants' behaviour validates the self-reports (reading 3.3)",
     REP + "PE C2.1")])
U("CCO", "C2.1", 0.5, [
    ("C", "Modeling shows 75%+ report genuine autonomy", AUD),
    ("U", "no validation of the design's self-reported share by observed behaviour is stated or cited; the closest "
          "component evidence, OpenResearch's randomised study of $1,000 a month for three years to 1,000 low-income "
          "adults (control group $50 a month), found recipients' unemployment spells about a month longer with fewer "
          "applications, job seekers 5.5 points more likely to require interesting or meaningful work, and more moves "
          "of home and neighbourhood, which is behaviour of the kind the Paper's method names, but it reports no "
          "self-reported autonomy share and no correlation between self-report and behaviour (reading 3.3)",
     REP + "CCO C2.1; Vivalt et al., The Employment Effects of a Guaranteed Income, NBER Working Paper 32719 "
     "(2024); OpenResearch, Key Findings: Employment (2024)")],
  note="the pilot calibrates confidence in the unconditional component (protocol 4.1); it does not estimate the design. "
       "The rationale's 75% figure is stated neither by the design's published model, which computes no autonomy "
       "measure, nor by any research-hub document (section 6)")
U("INT", "C2.1", 0.5, [
    ("C", "70%+ genuine autonomy in major life decisions is plausible", AUD),
    ("U", "democratic governance, cooperative production and transparent reciprocity are specified; no "
          "implementation's observed behaviour is cited or located (reading 3.3)",
     REP + "INT C2.1")])

# ---- C3.2 Inflation Control Mechanisms (reading 3.4) ------------------------------------------------------------
U("SQ", "C3.2", 0.5, [
    ("C", "maintains long-term inflation around 2-3% target", AUD),
    ("S", "the 2021-23 shock is the documented stress episode, with global inflation averaging 8.7% in 2022: US "
          "consumer prices rose 7.0% over 2021, 8.5% in the year to March 2022 and 9.1% in the year to June 2022, the "
          "largest twelve-month rise since 1981; prices excluding food and energy rose 6.6% in the year to September "
          "2022, so the bar is missed on the core measure as well (reading 3.4)",
     IMF + "; BLS, CPI news releases for March and June 2022; BLS, The Economics Daily, CPI 2021 in review "
     "(14 January 2022) and CPI to September 2022"),
    ("U", NOTEST + "; the verdict is fixed by clause 2 (whether rate-setting by the Federal Open Market Committee is "
          "automatic adjustment is left to Report v2.0)", "")])
U("NSD", "C3.2", 0.5, [
    ("C", "Successfully maintained low inflation (2-3%) over decades", AUD),
    ("S", "in the same episode every Nordic economy ran HICP inflation above 5% in every month from May to October "
          "2022; in October Denmark stood at 11.4%, Sweden 9.8%, Finland 8.4%, Norway 8.4% and Iceland 6.4%, against "
          "10.6% in the euro area and 2.9% in Switzerland, which shows the 5% bar was attainable in that environment "
          "(reading 3.4)",
     "Eurostat, euro indicators release 130/2022 (17 November 2022); " + IMF),
    ("U", NOTEST + "; the verdict is fixed by clause 2", "")])
U("PE", "C3.2", 0.5, [
    ("C", "prevents systemic price instability", AUD),
    ("U", "facilitation boards adjusting indicative prices through the iteration process are specified; no estimate of "
          "inflation under an external 8% scenario is stated or cited, and the clause applies because the design keeps "
          "indicative prices (reading 3.4)",
     REP + "PE C3.2"),
    ("C", "adjusting indicative prices to balance supply/demand", AUD)])
U("INT", "C3.2", 0.5, [
    ("C", "there is no money supply to inflate", AUD),
    ("U", "the rationale's structural claim (no currency; demand matched to capacity by assessment) is not an estimate "
          "under an external 8% scenario; the corpus's own review of Integral records that nodes procure from "
          "traditional markets during transition and asserts that external inflation is isolated through sectoral "
          "boundaries, a mechanism the design does not specify and no source estimates; read alike with Fully "
          "Automated Luxury Communism's clause 2 in part (a) (reading 3.4)",
     REP + "INT C3.2; Integral_NEEC_Review.md, C3.2; NEEC_Rescoring_s37.md, FALC C3.2"),
    ("C", "matched to capacity through COS", AUD)])

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 11, "per_criterion": {"C1.4": 2, "C2.1": 5, "C3.2": 4}, "stand": [], "points": 5.5,
          "silent": 14, "not_estimated": [("SQ", "C3.2", 2), ("NSD", "C3.2", 2)], "flags_added": [],
          "flags_removed": [], "remaining": 47, "dominance_b3": 18, "frontier_b3": 12, "anchors_moved": 7,
          "bands_empty": [("C1.1", "1.0"), ("C2.1", "1.0"), ("C2.3", "1.0"), ("C2.4", "1.0"), ("C3.1", "1.0")],
          "emptied": {"C2.3": "(b1)", "C2.4": "(b1)", "C3.1": "(b2)", "C1.1": "(b3)", "C2.1": "(b4)"},
          "ones_left": {"C1.4": ["UBI", "CCO"], "C2.1": [], "C3.2": ["CCO", "CN", "SG"]}}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables(rs, r4, cdef, order, names, steps, left):
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
    base, ma, mb, m2, m3, after = steps
    rb, rn = rs.ranks(base["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After (a) | After (b1) | After (b2) | After (b3) | After this group (rank) | "
            "Change here | Failures | Tier | D28 units left | Floor if all fall |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|"]
    for code in rs.order_codes(names, base):
        lf = left.get(code, 0)
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(ma['total'][code])} | "
                    f"{f1(mb['total'][code])} | {f1(m2['total'][code])} | {f1(m3['total'][code])} | "
                    f"{f1(after['total'][code])} ({rn[code]}) | {f1(after['total'][code] - m3['total'][code])} | "
                    f"{after['fail'][code]} | {rs.tier(after['fail'][code])} | {lf} | "
                    f"{f1(after['total'][code] - 0.5 * lf)} |")
    t["consequences"] = "\n".join(rows)
    return t


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    r4 = load("r4_audit_s35", AUDIT)
    mods = [load(mod, path) for _, mod, path in PRIOR]
    rs = mods[0]
    crit = json.loads(rs.read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}
    prior = tuple(m.UNITS for m in mods)

    print(f"NEEC rescoring pass, part (b), fourth group: C1.4, C2.1, C3.2 ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {AUDIT}, " + ", ".join(p for _, _, p in PRIOR) + f", {RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    done = set().union(*(set(p) for p in prior))
    partb = [k for k in d28 if k not in prior[0]]
    grp = [k for k in partb if k[1] in GROUP and k not in done]
    check(len(d28) == 134 and len(partb) == 101, "D28's population 134; part (b) 101")
    per = {g: sum(1 for k in grp if k[1] == g) for g in GROUP}
    check(sorted(UNITS) == sorted(grp) and per == EXPECT["per_criterion"] and all(vec[c][k] == 1.0 for c, k in UNITS)
          and not set(UNITS) & done,
          f"this group holds exactly the part (b) units of C1.4, C2.1 and C3.2 ({len(grp)}: "
          + ", ".join(f"{g} {per[g]}" for g in GROUP) + "), every one a corpus 1.0 and none re-estimated before")
    for g in GROUP:
        print(f"  {g}: " + ", ".join(c for c, k in grp if k == g))

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
            if st == "U" and not est.startswith(NOTEST) and not src.strip():
                bad.append(f"{key} clause {k + 1}: an estimated clause without the source searched")
            if "|" in est + src + (rec["flag"][1] if rec["flag"] else "") + rec["note"]:
                bad.append(f"{key} clause {k + 1}: a pipe character would break the table")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per clause, in Appendix B's order; every cleared, short, out-of-reach "
                   "and moot clause, and every clause estimated as not shown, carries its source")
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
    check(departs == set(EXCEPT) == set(),
          "no departure from the audit's A codes: every clause the audit coded A is carried as cleared")
    silent = {(k[0], k[1], i) for k in UNITS for i, ch in enumerate(reg[k]) if ch == "S"}
    notest = sorted((k[0], k[1], i) for k, r in UNITS.items() for i, (st, est, _) in enumerate(r["clauses"])
                    if est.startswith(NOTEST))
    fixed = all(UNITS[(c, k)]["clauses"][i][0] == "U" and any(
        j != i and st in "SUR" and not est.startswith(NOTEST)
        for j, (st, est, _) in enumerate(UNITS[(c, k)]["clauses"])) for c, k, i in notest)
    check(len(silent) == EXPECT["silent"] and set(notest) <= silent and notest == sorted(EXPECT["not_estimated"])
          and fixed,
          f"the audit coded {len(silent)} clauses of this group silent; {len(silent) - len(notest)} are estimated here, "
          f"and {len(notest)} are left not estimated, each in a unit whose verdict another clause already fixes")
    for c, k, i in notest:
        print(f"  {c} {k} clause {i + 1}: not estimated in this pass (verdict fixed by another clause)")

    # [4] reach ----------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = {x for x in r4.REACH if (x[0], x[1]) in UNITS}
    check(now_r == was_r == set(), "no clause of this group is out of reach, and none was coded so")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b3))")
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
          f"flags added {len(added)}; removed {len(removed)}; no unit of this group carried a flag before")
    adds, rems = list(added), list(removed)
    for part in prior:
        a, r = changes(part)
        adds += a
        rems += r
    moved = sorted({k[0] for k in adds + rems})
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Across the pass so far, "
                 f"{len(moved)} entries' flag registers change ({', '.join(moved)}).")
    print("  " + flag_line)

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        vsteps.append(v)
    v3, vn = vsteps[-2], vsteps[-1]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, m3, after = steps[0], steps[-2], steps[-1]
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    left_units = [k for k in partb if k not in done and k not in UNITS]
    left, perc = {}, {}
    for c, k in left_units:
        left[c] = left.get(c, 0) + 1
        perc[k] = perc.get(k, 0) + 1
    check(len(left_units) == EXPECT["remaining"], f"{len(left_units)} D28 units remain for part (b)")
    rem_line = (f"Left for part (b): {len(left_units)} D28 units (" +
                ", ".join(f"{k} {perc[k]}" for k in cids if k in perc) + ").")
    print("  " + rem_line)
    order = list(names)
    ones = {g: [c for c in order if vn[c][g] == 1.0] for g in GROUP}
    check(ones == EXPECT["ones_left"],
          "1.0s each of this group's criteria keeps: " + "; ".join(
              f"{g} {len(ones[g])} (published {sum(1 for c in vec if vec[c][g] == 1.0)})" for g in GROUP))
    tags = ("published", "(a)", "(b1)", "(b2)", "(b3)", "(b4)")
    emptied = {}
    for tag, v in zip(tags, vsteps):
        for k in cids:
            if k not in emptied and not any(v[c][k] == 1.0 for c in v):
                emptied[k] = tag
    check(all(any(vsteps[0][c][k] == 1.0 for c in vec) for k in cids) and emptied == EXPECT["emptied"],
          "every criterion had a 1.0 in the published corpus; the pass so far leaves " + str(len(emptied)) +
          " with none: " + ", ".join(f"{k} (part {emptied[k]})" for k in emptied))
    ones_line = ("After this group, the entries scoring 1.0 on this group's criteria are: " + "; ".join(
        f"{g}, {len(ones[g])}" + (f" ({', '.join(ones[g])})" if ones[g] else "") for g in GROUP) +
        ". Every criterion had a 1.0 in the published corpus; after the pass so far no entry scores 1.0 on " +
        str(len(emptied)) + " of them: " + ", ".join(f"{k} (emptied in part {emptied[k]})" for k in cids
                                                     if k in emptied) + ".")
    print("  " + ones_line)
    p3, f3 = rs.dominance(v3, cids)
    pn, fn = rs.dominance(vn, cids)
    check(len(p3) == EXPECT["dominance_b3"] and len(f3) == EXPECT["frontier_b3"],
          f"part (b3)'s result reproduced: {len(p3)} dominance pairs, frontier {len(f3)}")
    gained = sorted(set(pn) - set(p3), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(p3) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    allparts = prior + (UNITS,)
    n_all = sum(len(p) for p in allparts)
    st_all = sum(1 for p in allparts for r in p.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for p in allparts for r in p.values())
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(p3)} after part (b3) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(f3)} (" + ", ".join(c for c in order if c in fn) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(m3['total'][first[0]])} after part (b3), "
                f"{rs.f1(after['total'][first[0]])} now. Across parts (a) and (b1) to (b4), {n_all} units have been "
                f"re-estimated: {st_all} stand and {n_all - st_all} become 0.5 ({rs.f1(pts_all)} points).")
    print("  " + dom_line)

    # [7] anchors --------------------------------------------------------------------------------------------------
    print("\n[7] ANCHOR EXAMPLES THE PASS SO FAR MOVES (build_criteria.py checks examples against published scores)")
    code_of = {v: k for k, v in names.items()}
    allu, part_of = {}, {}
    for tag, p in zip(("(a)", "(b1)", "(b2)", "(b3)", "(b4)"), allparts):
        allu.update(p)
        part_of.update({k: tag for k in p})
    hits, empty = [], []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                code = code_of.get(ex["system"])
                if code and (code, c["id"]) in allu and allu[(code, c["id"])]["verdict"] != ex["cited"]:
                    hits.append(f"{c['id']}'s {band} example, {code} (part {part_of[(code, c['id'])]}, to "
                                f"{rs.f1(allu[(code, c['id'])]['verdict'])})")
                    if not any(vn[x][c["id"]] == float(band) for x in vn):
                        empty.append((c["id"], band))
    check(len(hits) == EXPECT["anchors_moved"], f"{len(hits)} anchor examples cite a unit the pass moves")
    check(empty == EXPECT["bands_empty"],
          "bands left with no corpus unit at their value: " + ", ".join(f"{c}'s {b}" for c, b in empty))
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) +
                   ". When the pass is applied, each band needs an example the corpus then scores at that value; " +
                   ", ".join(f"{c}'s {b}" for c, b in empty) + " bands have none left (reading 3.5; section 6).")
    print("  " + anchor_line)

    # [8] the record -----------------------------------------------------------------------------------------------
    print(f"\n[8] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    t = tables(rs, r4, cdef, unit_order, names, steps, left)
    t["dominance"], t["remaining"], t["flags"], t["anchors"], t["ones"] = (dom_line, rem_line, flag_line,
                                                                          anchor_line, ones_line)
    GENERATED.clear()
    GENERATED.update(t)
    record = rs.read(RECORD) if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING PART (B), FOURTH GROUP, COMPUTED." if ok else "\nRESCORING PART (B), FOURTH GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
