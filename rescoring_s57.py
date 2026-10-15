#!/usr/bin/env python3
"""
rescoring_s57.py -- NEEC rescoring pass, stage 2, group 2.5: CCO-PTF-CIP-SZH's simulation units on v5.6.0
=========================================================================================================
Session 57. The owner's message of 2026-10-14 (decision 57.3) directs the pass to read the overhauled Compassionism
Simulation now, superseding decision 52.9's freeze at 5a7a7b1 (v4.20). This group re-reads, on the design's published
model at d10ed6e (v5.6.0), the nine units of CCO-PTF-CIP-SZH whose estimate rests on the simulation or which the
simulation could now decide: C1.1, C1.2a, C1.2b, C1.3, C1.4, C3.2, C3.3, C3.4 and C5.3. Readings: NEEC_Rescoring_s57.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: the nine units, each against the unit it supersedes; which change
  [2] the design's model: cco_sim_v56_checks_s57_output.txt by digest, its own checks passed (the engine is the v5.6
      release's and reproduces the release's published figures), and every figure the readings quote found there
  [3] the reopening conditions recorded before v5.6.0 existed (STATE.md; Handoff 43, 9.3), evaluated from the figures
  [4] the flags
Sources not in this repository are named with their identifiers; every figure used from them is held below.

Usage: python3 rescoring_s57.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, cco_sim_v56_checks_s57_output.txt,
                                             NEEC_Rescoring_s57.md; writes nothing)
       python3 rescoring_s57.py --tables   (prints the generated tables as JSON, for the record)
Prints file names and summaries only. Deterministic.
"""
import hashlib
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD, CODE = "(2.5)", "NEEC_Rescoring_s57.md", "CCO"
SIMOUT, SIMMD5 = "cco_sim_v56_checks_s57_output.txt", "cd2ec0c978e68aeffaf57029bd12932a"
GROUP = ("C1.1", "C1.2a", "C1.2b", "C1.3", "C1.4", "C3.2", "C3.3", "C3.4", "C5.3")
UNITS = {}
GENERATED = {}

SIM = ("Compassionism Simulation at d10ed6e (v5.6.0), harness.js (md5 84be3bc9) and index.html (md5 2e1cc8c7), the "
       "v5.6 release's engine; cco_sim_v56_checks_s57_output.txt")
REL = ("the simulation's v5.6 release, data/releases/v5.6.json and dev/reports/v5-34-v56-release.md at d10ed6e; "
       "MODEL_SPEC.md at d10ed6e, sections 6.12 and 9")
WB = ("Foster, Jolliffe, Lara Ibarra, Lakner and Tetteh-Baah, Global Poverty Revisited Using 2021 PPPs and New Data on "
      "Consumption, World Bank Policy Research Working Paper 11137 (June 2025), section 3.4.1 (PDF md5 1128f547)")
HUB = "research hub at 8e8a6ba"
FRAME = HUB + ", cco-ptf-integrated-framework.html (md5 10ab8364)"
INFL = HUB + ", dual-currency-inflation.html (md5 329235ce)"
ROAD = HUB + ", integrated-implementation-roadmap.html (Appendix G)"
MODEL = HUB + ", economic-modeling-simulation.html (md5 86dda39b)"
AUD = "as audited (the unit's own text)"
CPI = {2019: 255.657, 2025: 321.943}   # CPI-U annual averages, BLS (CUUR0000SA0); 2025 as the simulation's sources cite it

# Every figure the readings quote, each as it appears in the runs' output (checked in [2]).
FIG = {
    "spl_b20": "7.9%", "spl_r0": "7.3%", "spl_r20": "7.7%", "spl_h20": "9.5%", "splx_r20": "4.6%",
    "spl_vs_r": "SPL 1.5%", "best": "largest 74.5%", "col_r": "60.3%", "col_h": "70.7%", "adv_col_r": "52.9%",
    "adv_spl_r": "8.3%", "adv_spl_h": "9.7%", "adv_b20": "7.3%",
    "bar": "$75,557", "part_r": "13.9%", "part_h": "91.1%", "bar_base": "61.2%", "seeds_h": "500 of 500",
    "seeds_r": "0 of 500", "adv_part_r": "1.7%", "adv_part_h": "77.9%", "med_r": "$30,728", "med_h": "$437,409",
    "gini_b": "0.755", "gini_r": "0.492", "gini_h": "0.602", "gini_re": "0.477",
    "win_r": "78.0%", "win_h": "86.1%", "win_b": "70.1%", "pth": "20.0%", "pthwin_r": "79.4%", "pthwin_h": "87.3%",
    "infl_r": "50.8%", "infl_h": "0.1%", "plev_r": "2440.74", "infl_adv_r": "60.9%", "infl_st_r": "27.4%",
    "deg_col_r": "28.6%", "deg_col_h": "40.0%", "deg_dis_r": "28.7%", "deg_dis_h": "14.7%", "deg_spl_r": "0.6%",
    "c07_r": "339 of 500", "c08_r": "43 of 500", "c07_h": "97 of 500", "c08_h": "1 of 500", "xp_r": "16.6",
    "xp_h": "14.0", "xprice_r": "6.8",
}
REL_FIG = {"hrs": "-8.3", "hrs_adv": "-11.3", "auto_adv": "2.377", "out_adv": "3.587", "part19_st": "43.7",
           "tax_f0": "68.9", "base_f0": "49.2"}   # from data/releases/v5.6.json, held here


def U(crit, verdict, clauses, flag=None, note=""):
    """One unit of the design. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    UNITS[(CODE, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note, zero=None)


F = FIG
U("C1.1", 0.5, [
    ("S", f"on the design's published model at v5.6.0 (500 seeds, 20 years, the Reference environment), poverty on the "
          f"Societal Poverty Line, v2.0's indicator, computed from the engine's disposable income per adult, is "
          f"{F['spl_r20']} at year 20 in the release row (nothing the Source pays backed by new output, the model's "
          f"main reading) against {F['spl_b20']} in the paired run with no programme and today's safety net, a "
          f"reduction of 1.5%, and {F['spl_h20']} at full backing; with the in-kind value of price cuts counted, "
          f"{F['splx_r20']}; it was {F['spl_r0']} at adoption, so it rises over the run; the largest reduction on "
          f"any measure the engine reports is 74.5% (below 30 days of basic living, at full backing), and the "
          f"release's own measure, adults below their cost of living, falls {F['col_r']} (release row) and "
          f"{F['col_h']} (full backing) against no programme (readings 3.3, 3.4)", f"{SIM}; {REL}; {WB}"),
    ("S", f"in the Adverse environment (recessions, an automation wave and 2% outside inflation), poverty on the "
          f"Societal Poverty Line is {F['adv_spl_r']} at year 20 in the release row and {F['adv_spl_h']} at full "
          f"backing, against {F['adv_b20']} with no programme, higher in both; the share below the cost of living "
          f"falls {F['adv_col_r']} against no programme; no measure falls 85% (reading 3.4)", f"{SIM}; {REL}; {WB}")],
  note="re-read on v5.6.0 (decision 57.3); both clauses stay short at either end of the backing sweep, and the unit "
       "stays 0.5. The reopening condition (90% in the reference run and 85% in the Adverse environment on the "
       "Societal Poverty Line) is not met")
U("C1.2a", 0.5, [
    ("U", f"on the design's published model at v5.6.0 (500 seeds, Reference), which spends by a sourced rule (a share "
          f"0.593 of the surplus, graded by income from the BLS Consumer Expenditure Survey), {F['part_r']} of "
          f"participants reach net wealth with Acre Equity of $60,000 in 2019 dollars ({F['bar']} in the engine's "
          f"2025 dollars) at year 20 in the release row, {F['seeds_r']} seeds at 70%, median {F['med_r']}, against "
          f"{F['bar_base']} of adults with no programme; at full backing (every dollar the Source pays backed by new "
          f"output) {F['part_h']} do, in {F['seeds_h']} seeds, median {F['med_h']}; the design's sources state no "
          f"backing share, and the model's main reading takes none; in the Adverse environment {F['adv_part_r']} and "
          f"{F['adv_part_h']} (reading 3.5)", f"{SIM}; {REL}; Report v1.6, System 12, C1.2a")],
  flag=("1.0: at full backing the engine's figure clears the bar in every seed", "3.5"),
  note="re-read on v5.6.0 (decision 57.3): the clause holds only if new output backs what the Source pays, a "
       "condition the design's sources do not state (protocol 2.1, reading 3.3), so it is not shown and the unit "
       "stays 0.5; the reopening condition (a sourced consumption rule that still shows 70% in the reference run) "
       "is not met, since the reference run, the release row, shows 13.9%")
U("C1.2b", 0.5, [
    ("S", f"on the design's published model at v5.6.0 (500 seeds, Reference), the wealth Gini at year 20, as the "
          f"engine reports it (debts as zero), is {F['gini_r']} in the release row ({F['gini_re']} with Acre Equity) "
          f"and {F['gini_h']} at full backing, against {F['gini_b']} with no programme; no seed is below 0.35 in any "
          f"run or environment; the design narrows the distribution, but not to the bar (reading 3.6)",
     f"{SIM}; {REL}")],
  note="re-read on v5.6.0 (decision 57.3); short at either end of the backing sweep. The design's mechanisms lower "
       "the Gini against no programme, so the unit is 0.5, not 0.0")
U("C1.3", 0.5, [
    ("U", f"the engine still models no housing tenure, eviction or rent line (Public Trust Housing enters from the "
          f"member's side only: a 35% cut in the housing component and Acre Equity), so it computes no stability rate; "
          f"on its nearest measure, a year in which cash income and savings cannot cover the year's cost, "
          f"{F['win_r']} of adults pass the weakest 5-year window with no such year in the release row and "
          f"{F['win_h']} at full backing, against {F['win_b']} with no programme; inside Public Trust Housing "
          f"({F['pth']} of adults) {F['pthwin_r']} and {F['pthwin_h']}; every figure is under 88%; the tenure forms "
          f"the owner describes (selling in, buying in, earning in, renting, moving within the system and keeping "
          f"Acre Equity) are design features the model does not yet carry (reading 3.7)", f"{SIM}; {REL}; "
     "the owner's note in the Project ledger, d29 (2026-10-14)"),
    ("U", "the engine carries no housing-cost line: Public Trust Housing cuts the housing component by 35% for its "
          f"members ({F['pth']} of adults), and no cost share at 80% of the median is stated or computed (reading 3.7)",
     f"{SIM}; MODEL_SPEC.md at d10ed6e, sections 6.10 and 11")],
  note="re-read on v5.6.0 (decision 57.3); neither clause is shown and the nearest measure is under 88% at either end "
       "of the backing sweep. The reopening condition (housing tenure and a housing-cost line) is not met")
U("C1.4", 0.5, [
    ("U", "v2.0 names the design's own model of three scenarios displacing 30%, 50% and 70% of paid hours; the model "
          "at v5.6.0 still cannot run them: its automation wave slows wages and, since v5.4, ends jobs, at "
          f"{REL_FIG['auto_adv']} automation job losses per 100 adult-years in the Adverse environment, with "
          f"{REL_FIG['out_adv']}% of adult-years out of work, and its labour response lowers paid hours by "
          f"{REL_FIG['hrs'].lstrip('-')}% in the Reference and {REL_FIG['hrs_adv'].lstrip('-')}% in the Adverse "
          f"environment, far from a 30% displacement; in the Adverse environment poverty on the Societal Poverty "
          f"Line is {F['adv_spl_r']} (release row) and {F['adv_spl_h']} (full backing) at year 20, above 8% in both "
          "(reading 3.8)", f"{SIM}; {REL}"),
    ("U", "the model computes no final consumption expenditure and no aggregate demand against a pre-displacement "
          "baseline (reading 3.8)", f"{SIM}; MODEL_SPEC.md at d10ed6e, section 9")],
  note="re-read on v5.6.0 (decision 57.3); the reopening condition (an hours-displacement lever) is not met")
U("C3.2", 0.5, [
    ("U", f"the design's published model now computes prices (since v5.0): what the Source pays out, less output "
          f"that backs it, is new money that moves the price level; in the release row, its main reading, the "
          f"programme raises the basket index {F['infl_r']} a year over 20 years in the Reference environment "
          f"(median price level {F['plev_r']} times its start), {F['infl_adv_r']} in the Adverse and "
          f"{F['infl_st_r']} in the Stress Test, in no seed at or under 3%; at full backing it raises it "
          f"{F['infl_h']} a year, in every seed under 3%; financed by a flat wage contribution instead, prices hold "
          f"but {REL_FIG['tax_f0']}% of adults are below the cost of living, against {REL_FIG['base_f0']}% with no "
          f"programme; the design states no backing share, so the clause rests on a condition its sources do not "
          f"establish (readings 3.3, 3.9)", f"{SIM}; {REL}; {INFL}, sections 5.2 and 5.4"),
    ("U", "the model's environments carry 0% and 2% outside inflation; no 8% scenario is modelled, and the "
          "framework paper's 8% scenario (local inflation 3.2% while national inflation reaches 8.1%) comes from a "
          "model not published in runnable form (reading 3.9)", f"{SIM}; {FRAME}, section 5.2"),
    ("U", "the one automatic adjustment the model carries, the Inflation Surge Protocol's indexation of the Basic Unit "
          "when prices rise faster than 5%, raises the payout with prices (in the release row the indexed and "
          "unindexed readings give the same figures, since prices always rise faster than 5%); no adjustment that "
          "restrains issuance or conversion is modelled, so the model does not show adjustment preventing runaway "
          "inflation (reading 3.9)", f"{SIM}; {REL}; {ROAD}")],
  flag=("1.0: if the design's supply response is read as backing every dollar the Source pays, the model's inflation "
        "is 0.1% a year and the papers' own modelling carries the other clauses, as reading 3.8 of group 2.1 did",
        "3.9"),
  note="re-read on v5.6.0 under reading 3.2 of group 2.1 (a published 1.0 resting on the design's own modelling is "
       "re-read where the published model computes the quantity): group 2.1 carried the unit because the model then "
       "computed no price; it now does, and its main reading shows inflation far above 3% a year. The design's "
       "mechanisms (spending limited to essentials, expiring units, supply response) are genuine, so the unit is 0.5, "
       "not 0.0. A CCO-PTF-CIP-SZH score change: it waits on the owner's confirmation (decision 57.2)")
U("C3.3", 0.5, [
    ("U", f"the design's published model at v5.6.0 runs one compound scenario, the Adverse environment (recessions, "
          f"an automation wave and 2% outside inflation at the reference settings), milder than C3.3's "
          f"recession-and-automation scenario, and a weaker-settings variant of it, the Stress Test; against the "
          f"Reference environment on the same seeds at year 20, the share of adults not below the cost of living "
          f"degrades {F['deg_col_r']} (release row) and {F['deg_col_h']} (full backing), and the share not in "
          f"housing distress {F['deg_dis_r']} and {F['deg_dis_h']}; the share above the Societal Poverty Line "
          f"degrades under 1%; essential-service and democratic-function capacity are not modelled, and the other "
          f"three compound scenarios are not modelled (reading 3.10)", f"{SIM}; {REL}")],
  note="re-read on v5.6.0 (decision 57.3); one of four scenarios is modelled, and in it two measured functions degrade "
       "by more than 20% at either end of the backing sweep. The reopening condition (three of four compound "
       "scenarios under 20%) is not met")
U("C3.4", 0.5, [
    ("C", "octave caps, basic amounts (5-20% of GDP per capita), conversion multipliers and the phi-rate adjustable",
     AUD),
    ("C", "the design's crisis protocol schedules parameter recalibration within one to six months, and monthly "
          "cost-of-living adjustments in an inflation surge", ROAD),
    ("C", "CIP enables democratic parameter adjustment", AUD),
    ("S", f"the design's published model now has an endogenous price channel and a labour response, so the scorer's "
          f"adjustment run was repeated (the Basic Unit multiplied by 0.7, 0.8, 1.2 or 1.3 from year 10, each seed "
          f"against the unadjusted run, Reference): on the test fixed before the run (in a year from year 10, the "
          f"share below the cost of living 10 points or more above the unadjusted run's, or the price rise 10 points "
          f"or more above it), the 0.7 step collapses in {F['c07_r']} seeds and the 0.8 step in {F['c08_r']} in the "
          f"release row, and in {F['c07_h']} and {F['c08_h']} at full backing (largest excess {F['xp_r']} and "
          f"{F['xp_h']} points); the 1.2 and 1.3 steps collapse in none, adding at most {F['xprice_r']} points to a "
          f"year's price rise (reading 3.11)", f"{SIM}")],
  flag=("1.0: if a collapse is read as a breakdown the step causes (runaway prices, a run that fails), not the cut's own "
        "effect on poverty, no step collapses at either backing", "3.11"),
  note="part (b1)'s reopening condition is met (an endogenous price and behavioural channel, the run repeated); the "
       "clause moves from not shown to short on the test fixed before the run, and the unit stays 0.5. The test counts "
       "the direct effect of a 20-30% cut in the allowance on the share below the cost of living, which is why the "
       "flag toward 1.0 is kept on another reading")
U("C5.3", 1.0, [
    ("C", "Viable at 30%+ participation", AUD),
    ("C", "Can coexist with traditional markets", AUD),
    ("C", "Scaling pathway validated through modeling", AUD),
    ("C", "Inter-jurisdictional coordination protocols specified", AUD)],
  note="re-read on v5.6.0 and carried (reading 3.12): the model still reads no aggregate participation threshold (the "
       "55% minimum is a run warning), computes no economic activity or scaling path, and its Stress Test, at 40% "
       f"taking part ({REL_FIG['part19_st']}% by year 19), still lowers the share below the cost of living against "
       "no programme, so it neither supports nor contradicts the rationale's figures; its labour response lowers paid "
       f"hours by {REL_FIG['hrs'].lstrip('-')}% to {REL_FIG['hrs_adv'].lstrip('-')}%, while the projects' output, "
       "which it values separately, is not an economic-activity measure")

# The unit each re-read supersedes, and what changes (checked in [1]).
EXPECT = {"prior": {"C1.1": "(2.1)", "C1.2a": "(2.2)", "C1.2b": "(2.1)", "C1.3": "(2.3)", "C1.4": "(2.1)",
                    "C3.2": "(2.1)", "C3.3": "(2.1)", "C3.4": "(b1)", "C5.3": "(2.1)"},
          "fall": ["C3.2"], "rise": [], "flags": {"C1.2a": "3.5", "C3.2": "3.9", "C3.4": "3.11"}}


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    with redirect_stdout(io.StringIO()):
        idx = [t for t, _, _, _ in pc.PARTS].index(TAG)
        p = pc.Pass(upto=idx)
    print(f"NEEC rescoring pass, stage 2, group 2.5: CCO-PTF-CIP-SZH's simulation units on v5.6.0 ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{SIMOUT}, {RECORD}\n")

    print("[1] THE GROUP")
    prior = {k: p.part_of.get((CODE, k)) for k in GROUP}
    check(sorted(k for _, k in UNITS) == sorted(GROUP) and prior == EXPECT["prior"],
          f"nine units of {CODE}, each superseding the unit an earlier part set: " +
          ", ".join(f"{k} {prior[k]}" for k in GROUP))
    old = {k: p.merged[(CODE, k)]["verdict"] for k in GROUP}
    fall = [k for k in GROUP if UNITS[(CODE, k)]["verdict"] < old[k]]
    rise = [k for k in GROUP if UNITS[(CODE, k)]["verdict"] > old[k]]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"against the units they supersede, this group lowers {len(fall)} ({', '.join(fall)}), raises "
          f"{len(rise)} and holds {len(GROUP) - len(fall) - len(rise)}; a change to {CODE}'s score waits on the "
          "owner (decision 57.2)")
    check(all(p.v2[k]["revision"]["cls"] for k in GROUP),
          "classes in v2.0: " + ", ".join(f"{k} {p.v2[k]['revision']['cls']}" for k in GROUP))

    print("\n[2] THE DESIGN'S MODEL (readings 3.2, 3.3)")
    raw = open(os.path.join(HERE, SIMOUT), "rb").read() if os.path.isfile(os.path.join(HERE, SIMOUT)) else b""
    check(hashlib.md5(raw).hexdigest() == SIMMD5, f"{SIMOUT} md5 {hashlib.md5(raw).hexdigest()[:8]} (node "
          "cco_sim_v56_checks_s57.js, four parts of 125 seeds, on harness.js and index.html at d10ed6e)")
    txt = raw.decode("utf-8")
    check("SUMMARY: all checks pass; 500 seeds." in txt and "FAIL" not in txt and txt.count("PASS  ") == 7,
          "the runs' own checks all passed: the engine is the v5.6 release's, and it reproduces the release's "
          "published figures for the no-programme run, the release row and full backing in all three environments")
    lost = [k for k, v in FIG.items() if v not in txt]
    quoted = " ".join(c[1] for r in UNITS.values() for c in r["clauses"]) + " ".join(r["note"] for r in UNITS.values())
    unq = [k for k, v in FIG.items() if v.replace("SPL ", "").replace("largest ", "") not in quoted and
           not v.replace("SPL ", "").replace("largest ", "").rstrip("%") in quoted]
    check(not lost and not unq, f"each of the {len(FIG)} figures the readings quote appears in the runs' output and in "
          "the readings", ", ".join(lost + unq))
    bar = 60000 * CPI[2025] / CPI[2019]
    check(f"${round(bar):,}" == FIG["bar"], f"$60,000 in 2019 dollars is {FIG['bar']} in 2025 dollars (CPI-U "
          f"{CPI[2025]} / {CPI[2019]})")

    print("\n[3] THE REOPENING CONDITIONS (recorded before v5.6.0; STATE.md, Handoff 43, 9.3)")
    pct = lambda k: float(FIG[k].rstrip("%"))  # noqa: E731
    cond = [("C1.1: 90% in the reference run and 85% in the Adverse on the Societal Poverty Line",
             False, "the release row's reduction against no programme is 1.5%, and poverty rises in the Adverse"),
            ("C1.2a: a sourced consumption rule still showing 70% in the reference run", pct("part_r") >= 70,
             f"the reference run shows {FIG['part_r']}"),
            ("C1.3: housing tenure and a housing-cost line", False, "neither is modelled"),
            ("C1.4: an hours-displacement lever", False, "none is modelled"),
            ("C3.3: three of four compound scenarios under 20%", False, "one is modelled, degrading over 20%"),
            ("C3.4: an endogenous price or behavioural channel, with the adjustment run repeated", True,
             "both, so the unit is re-read (reading 3.11)")]
    for name, met, why in cond:
        print(f"    {'met    ' if met else 'not met'}  {name}: {why}")
    check([m for _, m, _ in cond] == [False, False, False, False, False, True],
          "one condition is met (C3.4's); the others are not, so no unit rises")

    print("\n[4] FLAGS")
    fl = {k: UNITS[(CODE, k)]["flag"][1] for k in GROUP if UNITS[(CODE, k)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{k} toward {UNITS[(CODE, k)]['flag'][0][:3]} (reading {r})"
                                                       for k, r in fl.items()))

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.4", "After group 2.5")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    f1 = pc.f1
    rows = ["| Criterion | Class | Before (part) | Clauses | Verdict | Flag |", "|---|---|---:|---|---:|---|"]
    for k in GROUP:
        r = UNITS[(CODE, k)]
        rows.append(f"| {k} | {p.v2[k]['revision']['cls']} | {f1(old[k])} {prior[k]} | "
                    + " ".join(x[0] for x in r["clauses"]) + f" | {f1(r['verdict'])} | "
                    + (f"toward {r['flag'][0][:3]}" if r["flag"] else "") + " |")
    t["summary"] = "\n".join(rows)
    for k in GROUP:
        r = UNITS[(CODE, k)]
        lines = [f"#### {CODE} {k} {p.v2[k]['name']}: {f1(p.vec[CODE][k])} (published), {f1(old[k])} {prior[k]} "
                 f"→ {f1(r['verdict'])}", "", "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (st, est, src) in enumerate(r["clauses"]):
            lines.append(f"| {i + 1} | {p.v2[k]['definition']['clauses'][i]} | {pc.STATUS[st]} | {est} | {src} |")
        if r["flag"]:
            lines += ["", f"*Flag (reading {r['flag'][1]}):* toward {r['flag'][0]}."]
        if r["note"]:
            lines += ["", f"*Note:* {r['note']}."]
        t[f"unit {k}"] = "\n".join(lines)
    GENERATED.clear()
    GENERATED.update(t)
    if "--tables" in sys.argv[1:]:
        sys.stdout = sys.__stdout__
        print(json.dumps(t, ensure_ascii=False))
        return 0
    rec = open(os.path.join(HERE, RECORD), encoding="utf-8").read() if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in rec]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING STAGE 2, GROUP 2.5, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.5: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
