#!/usr/bin/env python3
"""
rescoring_s54.py -- NEEC rescoring pass, stage 2, group 2.3: C1.3 Housing Security, class M
===========================================================================================
Session 54. The second group written on the shared module (pass_common.py, decision 52.5): the 20 units of C1.3 the
pass had not re-estimated are re-read clause by clause against v2.0's text (Appendix V of NEEC_Criteria_v2_s45.md;
criteria.json), whose restatement (K6, R2) states affordability as housing costs of at most 30% of disposable income
for a household at 80% of the regional median household disposable income. Nordic Social Democracy's, MMT + Job
Guarantee's and Singapore's units (parts (b1) and (a)) are not re-read. Readings: NEEC_Rescoring_s54.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry not yet re-estimated on C1.3, each against its published score; which rise, fall
      or hold; the 0.0s and their reasons; which units stand at 1.0
  [2] the figures the readings derive (the bound on the historical record, the US income band) recomputed here from
      the figures held, each appearing in its unit's estimate
  [3] the design's model: cco_c13_checks_s54_output.txt by digest, and every figure the readings quote from it
  [4] the flags
Sources not in this repository are named with their identifiers; every figure used from them is held below.

Usage: python3 rescoring_s54.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, cco_c13_checks_s54_output.txt,
                                             NEEC_Rescoring_s54.md; writes nothing)
       python3 rescoring_s54.py --tables   (prints the generated tables as JSON, for the record)
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

TAG, RECORD, CRIT = "(2.3)", "NEEC_Rescoring_s54.md", "C1.3"
SIMOUT, SIMMD5 = "cco_c13_checks_s54_output.txt", "30d131f050d17ff80e2388876b183842"
UNITS = {}
GENERATED = {}


def U(code, verdict, c1, c2, flag=None, note="", zero=None):
    """One unit of C1.3. c1, c2: (status, estimate, source) for the two v2.0 clauses. flag: (alternative, reading).
    zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[c1, c2], flag=flag, note=note, zero=zero)


# ---- figures held (reading 3.1 to 3.5) -----------------------------------------------------------------------------
US = {"median_2023": 80610, "band": (45000, 74999), "burden_band": 45, "burden_all": 50, "burdened_m": 22.6,
      "filings_m": 3.6, "filed_hh_m": 2.7}
SU = {"fees_1990": 2.5, "hostels_1989": 6, "communal_1989": 5, "q1_1995": 18.6}
SIM_FIG = {"all16": "86.4%", "low": "78.5%", "base16": "51.1%", "pth16": "96.8%", "pthlow": "93.6%", "out16": "83.7%",
           "outlow": "74.7%", "pth": "20.1%", "adv16": "63.5%", "seeds": "83 of 500"}


def usd(x):
    return f"${round(x):,}"


FIGS = {"us80": usd(0.8 * US["median_2023"]), "su_bound": f"{100 - SU['hostels_1989']}%"}

# ---- sources -------------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
JCHS_SRC = ("Joint Center for Housing Studies of Harvard University, The State of the Nation's Housing 2025 (2023 data; "
            "cost burden: 30% or more of pre-tax household income on housing and utilities), as summarised by the "
            "National Low Income Housing Coalition, Memo to Members, 30 June 2025")
CEN_SRC = ("US Census Bureau, Income in the United States: 2023 (P60-282), real median household income $80,610, "
           "pre-tax money income")
EVL_SRC = "Eviction Lab (Princeton University), national data update of 11 July 2022, figures for 2018"
LTC_SRC = ("Childress, Kutuzov and Haase, A Decade of Housing Reform in Russia (Land Tenure Center, University of "
           "Wisconsin-Madison, draft of 26 July 2001; md5 babfbd70), sections 3, 6, 7 and 10")
IMF_SRC = ("IMF, World Bank, OECD and EBRD, A Study of the Soviet Economy (1991), vol. 3, chapter V.9 Housing, citing "
           "the 1989 census (read from the publisher's catalogue excerpt; the chapter's text refused retrieval)")
SIM_SRC = ("Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); "
           "cco_c13_checks_s54_output.txt; the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), the "
           "extreme-poverty overlay")
HUB_SRC = "research hub at 8e8a6ba, cco-ptf-integrated-framework.html (md5 10ab8364)"
SILENT1 = "no stability rate, documented or designed, is stated, and no source the unit cites gives one"
SILENT2 = "no housing cost, and no share of income at 80% of the median, is stated or projected"

# ---- the units (readings in NEEC_Rescoring_s54.md, section 3) --------------------------------------------------------
U("SQ", 0.5,
  ("U", f"no national measure of 5-year involuntary displacement exists; in 2018 landlords filed {US['filings_m']} "
        f"million eviction cases against {US['filed_hh_m']} million households, and renters, about a third of "
        "households, carry most of the exposure; the published 72%, for market-rate rental only, has no located "
        "source (reading 3.5)", f"{EVL_SRC}; {REP}System 1, C1.3"),
  ("S", f"80% of the 2023 median household income ({usd(US['median_2023'])}) is {FIGS['us80']}, inside the "
        f"$45,000 to $74,999 band, where {US['burden_band']}% of renter households pay 30% or more of pre-tax income "
        f"on housing and utilities; on disposable income, the clause's basis, the share is larger; half of all renter "
        f"households, a record {US['burdened_m']} million, are cost-burdened", f"{JCHS_SRC}; {CEN_SRC}"),
  note="the published rationale's 72% is replaced by sourced figures; the verdict is unchanged")
U("CPS", 1.0,
  ("C", "no 5-year rate is documented, but the three causes of displacement the measure names were closed to state "
        "tenants: no mortgages, rents and fees unchanged since 1928, and eviction 'virtually unheard "
        f"of in public housing'; the exposed segment, workers' hostels whose places went with the job, held "
        f"{SU['hostels_1989']}% of households in the 1989 census; counting every hostel household as displaced within "
        f"five years leaves {FIGS['su_bound']} stable; through the collapse, flats passed to their occupants "
        "practically free of charge (reading 3.4)", f"{LTC_SRC}; {IMF_SRC}"),
  ("C", f"housing fees, communal services included, were about {SU['fees_1990']}% of an average worker's or "
        "employee's income in 1990, so a household at 80% of the median paid of the order of "
        f"3%; after the system ended, the poorest Russian quintile's rent-to-income ratio reached {SU['q1_1995']}% in "
        "1995, still under 30%", LTC_SRC),
  flag=("0.5: the clause is cleared by a bound on the late-Soviet record, not by a measured rate, and the bound does "
        "not cover the deportations of the 1930s and 1940s or the configuration's other states", "3.4"),
  note="the 1.0 band's anchor example; it holds")
U("MS", 0.5,
  ("U", "housing cooperatives exist within the cooperative movement, but the market still allocates most housing; "
        + SILENT1, f"{REP}System 4, C1.3"),
  ("U", SILENT2 + "; cooperative housing is a minority tenure", f"{REP}System 4, C1.3"))
U("LM", 0.0,
  ("U", "pure market allocation with no stabilizing mechanism; no rate is stated", f"{REP}System 5, C1.3"),
  ("U", "no affordability instrument of any kind; housing costs are whatever the market sets", f"{REP}System 5, C1.3"),
  zero="no structural mechanism addresses the criterion: pure market allocation with no stabilizing mechanism (the "
       "0.0 band's anchor)")
U("UBI", 0.5,
  ("U", "stable income improves housing security for many; " + SILENT1, f"{REP}System 7, C1.3"),
  ("U", "the transfer raises income, but without housing policy landlords can capture it through rent increases; "
        + SILENT2, f"{REP}System 7, C1.3; Paper v1.4, Appendix H.7"),
  note="the 0.5 band's anchor example; it holds")
U("DG", 0.5,
  ("U", "community land trusts, housing cooperatives and rent controls are named as the design's housing "
        "mechanism; " + SILENT1, f"{REP}System 8, C1.3"),
  ("U", SILENT2 + "; the design names decommodification, not a cost", f"{REP}System 8, C1.3"),
  note="published 1.0 read in the D28 form (silence is not clearance, protocol 2.3(b)): neither clause is estimated, "
       "so the unit falls to 0.5 (reading 3.2)")
U("SC", 0.5,
  ("U", "the host economy's housing (Status Quo's) with some employer housing assistance; no national measure of "
        "5-year displacement exists, as for Status Quo", f"{REP}System 9, C1.3; {EVL_SRC}"),
  ("S", f"housing remains market-allocated; at 80% of the US median, {FIGS['us80']}, {US['burden_band']}% of renter "
        "households in the $45,000 to $74,999 band pay 30% or more of pre-tax income, and no source shows the reform "
        "changing it", f"{REP}System 9, C1.3; {JCHS_SRC}; {CEN_SRC}"))
U("FALC", 0.5,
  ("U", "automated construction and universal provision are projected to achieve complete housing security; "
        + SILENT1, f"{REP}System 10, C1.3"),
  ("U", SILENT2 + "; provision is described as universal, not costed", f"{REP}System 10, C1.3"),
  note="published 1.0 read in the D28 form: neither clause is estimated, so the unit falls to 0.5 (reading 3.2)")
U("PE", 0.5,
  ("U", "housing is allocated by consumption councils on needs and effort and described as decommodified and stable; "
        + SILENT1, f"{REP}System 11, C1.3"),
  ("U", SILENT2 + "; allocation by effort rating sets no housing charge that can be read against income",
   f"{REP}System 11, C1.3"),
  note="published 1.0 read in the D28 form: neither clause is estimated, so the unit falls to 0.5 (reading 3.2)")
U("CCO", 0.5,
  ("U", f"the engine models no housing tenure, so it computes no stability rate; on its nearest measure, a year in "
        f"which cash income and savings cannot cover the basket, {SIM_FIG['all16']} of agents pass years 16 to 20 "
        f"with no such year ({SIM_FIG['seeds']} seeds at 88% or more) and {SIM_FIG['low']} the weakest 5-year window, "
        f"against {SIM_FIG['base16']} in the matched Baseline; inside Public Trust Housing, which holds "
        f"{SIM_FIG['pth']} of agents, {SIM_FIG['pthlow']} to {SIM_FIG['pth16']} pass every window, outside it "
        f"{SIM_FIG['outlow']} to {SIM_FIG['out16']}; the papers' 94% has no published model behind it (reading 3.3)",
   f"{SIM_SRC}; {HUB_SRC}, sections 4 and 5; {REP}System 12, C1.3"),
  ("U", "the engine carries no housing-cost line (Public Trust Housing scales the whole basket by 0.65); the papers' "
        "average housing cost reduction of 60% against market rents applies to Public Trust Housing residents, "
        f"{SIM_FIG['pth']} of agents in the reference run, and no cost share at 80% of the median is stated",
   f"{SIM_SRC}; {HUB_SRC}, sections 4 and 5"),
  note="published 1.0 read in the D28 form: neither clause is shown on the published model, and its nearest measure "
       "falls short of 88% in every window for the population the design serves; Public Trust Housing residents clear "
       "it, a narrower population, which is a scope matter (protocol 3.4), not a flag")
U("INT", 0.5,
  ("U", "community-controlled allocation and cooperative ownership; the rationale cites the criterion's own benchmark, "
        "community land trusts' foreclosure rate of 0.46% against 3.26% in 2008-2010, as making 90%+ plausible; a "
        "crisis foreclosure rate for trust homeowners is not a 5-year stability rate for the system's population, and "
        + SILENT1, f"{REP}System 13, C1.3"),
  ("U", SILENT2, f"{REP}System 13, C1.3"),
  note="published 1.0 read in the D28 form: neither clause is estimated, so the unit falls to 0.5 (reading 3.2)")
U("GEO", 0.5,
  ("U", "the tax discourages land-banking and raises construction density, but addresses neither eviction nor rental "
        "stability; Estonia's land tax did not prevent the Tallinn housing bubble of about 2003 to 2008",
   f"NEEC_Georgism_LVT_scoring_scratch.md, C1.3; {REP}System 14, C1.3"),
  ("U", "supply effects are measured in housing-unit growth, not in housing costs against income; no affordability "
        "figure for households at 80% of the median is located", "NEEC_Georgism_LVT_scoring_scratch.md, C1.3"))
U("MC", 0.0,
  ("R", "no housing-specific design element, volatility buffer or stability outcome in any source reviewed (WIR, "
        "Sardex, LETS, time banking, Trueque, Grassroots Economics)", f"{REP}System 15, C1.3"),
  ("R", "the instrument governs no housing cost", f"{REP}System 15, C1.3"),
  zero="no structural mechanism addresses the criterion: no housing channel of any kind")
U("DE", 0.5,
  ("U", "housing is one of the twelve social-foundation dimensions and City Portraits track it; the one located "
        "policy output (Portland's 'From Excess to Access') is narrow; " + SILENT1,
   "NEEC_DoughnutEconomics_scoring_scratch.md, C1.3"),
  ("U", "affordability is tracked as an indicator, not set by a mechanism of the framework's own",
   "NEEC_DoughnutEconomics_scoring_scratch.md, C1.3"),
  flag=("0.0, the reading of the framework's C1.2a: no housing mechanism of its own", "3.6"),
  note="held at 0.5 on the published reading, which credits the diagnostic process and its one policy output; the "
       "reading that gave the framework's C1.2a 0.0 (no vehicle of its own) would give 0.0 here, and is flagged")
U("UBS", 0.5,
  ("U", "zero-rent social housing on a needs basis, 1.5 million new units; Vienna's municipal and cooperative "
        "housing, the closest analogue, is durable at population scale; " + SILENT1,
   "NEEC_UniversalBasicServices_scoring_scratch.md, C1.3"),
  ("U", "zero rent clears the clause for the households the shelter sector houses, but that design has not been "
        "implemented at the scale proposed, Vienna charges modest rents and new cooperative entrants pay an upfront "
        "sum of the order of $38,000; no cost share at 80% of the median is stated for the economy",
   "NEEC_UniversalBasicServices_scoring_scratch.md, C1.3"))
U("SWF", 0.0,
  ("R", "the fund touches neither exemplar's housing market, both ordinary private mortgage-based systems; no "
        "housing allocation, land trust or tenancy protection is located",
   "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.3"),
  ("R", "the mechanism governs no housing cost", "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.3"),
  zero="no structural mechanism addresses the criterion: no housing channel of any kind")
U("CN", 0.5,
  ("U", "about 12.6 million households were moved as their dwellings were demolished in 2008-2012; by 2022 more than "
        "85% of homes were sold before completion, and mortgage boycotts spread to over 300 stalled developments; "
        "about 300 million migrant workers were historically shut out of city housing support; no 5-year stability "
        "rate is reported", "NEEC_StateCapitalism_China_scoring_scratch.md, C1.3"),
  ("U", "ownership is broad and lightly leveraged (about 18% of owners with a mortgage in 2022), but no housing cost "
        "share for households at 80% of the median is located, for owners or for the migrant renters",
   "NEEC_StateCapitalism_China_scoring_scratch.md, C1.3"))
U("QA", 0.5,
  ("U", "for citizens housing is largely decommodified (free plots, long-term loans); for non-citizens, the large "
        "majority of residents, housing and residence depend on continuous employment with a cooperating employer, "
        "who can cancel the visa; no 5-year rate is reported for either", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.3"),
  ("U", "low-wage workers are housed by the employer or paid a housing allowance of at least QAR 500 a month; no "
        "housing cost share at 80% of the median is located", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.3"),
  note="the citizens-only scenario (1.0) stays a scenario (protocol 3.2)")
U("IF", 0.5,
  ("U", "diminishing partnership (musharakah mutanaqisah) is a real housing product: the financier bears ownership "
        "risk and a markup price cannot grow after default; allocation remains market-based and " + SILENT1,
   "NEEC_IslamicFinance_scoring_scratch.md, C1.3"),
  ("U", "profit rates are competitive with conventional mortgages, not below them; no affordability floor, and no "
        "cost share at 80% of the median is stated", "NEEC_IslamicFinance_scoring_scratch.md, C1.3"))
U("OS", 0.5,
  ("U", "community land trusts are the commons' housing form (counted in, decision D31, with a scenario counting them "
        "out); no 5-year stability series for commons-governed housing was retrieved",
   "NEEC_Ostrom_Commons_scoring_scratch.md, C1.3; SCORING_PROTOCOL.md 3.2"),
  ("U", "nothing in the mechanism targets households at 80% of the median; no cost share is stated",
   "NEEC_Ostrom_Commons_scoring_scratch.md, C1.3"),
  note="the scope scenario counting community land trusts out (0.0) stands")

EXPECT = {"fall": ["DG", "FALC", "PE", "CCO", "INT"], "rise": [], "zero": ["LM", "MC", "SWF"], "ones": ["CPS"],
          "flags": {"CPS": "3.4", "DE": "3.6"}, "before": ["NSD", "MMT", "SG"]}


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
    print(f"NEEC rescoring pass, stage 2, group 2.3: C1.3 Housing Security, class M ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{SIMOUT}, {RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(p.part_of[(c, CRIT)] for c in before)}) and are not re-read")
    check(p.v2[CRIT]["revision"]["cls"] == "M" and len(p.v2[CRIT]["definition"]["clauses"]) == 2,
          f"{CRIT} is class M with two clauses in v2.0")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group lowers {len(fall)} ({', '.join(fall)}), raises {len(rise)} and holds {len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 == pub[c] for c in zeros),
          f"{len(zeros)} units are 0.0, as published, each on a stated whole-criterion reason (protocol 2.1); no "
          "failure count changes")
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    check(ones == EXPECT["ones"], f"one unit clears both clauses: {', '.join(ones)}, the 1.0 band's anchor; after this "
          f"group it is the only entry at 1.0 on {CRIT}")

    print("\n[2] THE FIGURES THE READINGS DERIVE")
    lo, hi = US["band"]
    check(lo <= 0.8 * US["median_2023"] <= hi and FIGS["us80"] == "$64,488" and FIGS["us80"] in
          UNITS[("SQ", CRIT)]["clauses"][1][1] and FIGS["us80"] in UNITS[("SC", CRIT)]["clauses"][1][1],
          f"80% of the US median household income is {FIGS['us80']}, inside the ${lo:,} to ${hi:,} band whose renter "
          f"cost burden ({US['burden_band']}%) the US units quote")
    check(100 - SU["hostels_1989"] >= 88 and FIGS["su_bound"] in UNITS[("CPS", CRIT)]["clauses"][0][1],
          f"the historical bound: with every hostel household ({SU['hostels_1989']}% in 1989) counted as displaced, "
          f"{FIGS['su_bound']} remain stable, at or above 88%")
    check(SU["fees_1990"] <= 30 and SU["q1_1995"] <= 30, f"Soviet housing fees, {SU['fees_1990']}% of income in 1990, "
          f"and the poorest Russian quintile's {SU['q1_1995']}% in 1995 are under 30%")

    print("\n[3] THE DESIGN'S MODEL (reading 3.3)")
    raw = open(os.path.join(HERE, SIMOUT), "rb").read() if os.path.isfile(os.path.join(HERE, SIMOUT)) else b""
    check(hashlib.md5(raw).hexdigest() == SIMMD5, f"{SIMOUT} md5 {hashlib.md5(raw).hexdigest()[:8]} "
          f"(node cco_c13_checks_s54.js on harness.js and index.html at 5a7a7b1)")
    txt = raw.decode("utf-8")
    check("ALL PASSED" in txt and "FAIL" not in txt, "the runs' own checks all passed, the runner reproducing "
          "runScenario()'s year-20 housing distress on every seed")
    cco = " ".join(x[1] for x in UNITS[("CCO", CRIT)]["clauses"])
    lost = [f for f in SIM_FIG.values() if f not in txt]
    check(not lost and all(f in cco for f in SIM_FIG.values() if f != SIM_FIG["adv16"]),
          "every figure the CCO unit quotes appears in the runs' output", ", ".join(lost))
    check(float(SIM_FIG["all16"][:-1]) < 88 and float(SIM_FIG["pthlow"][:-1]) >= 88,
          f"on the engine's nearest measure the design's population falls short of 88% in every 5-year window "
          f"(best {SIM_FIG['all16']}); Public Trust Housing residents, {SIM_FIG['pth']} of agents, clear it in every "
          f"window (lowest {SIM_FIG['pthlow']})")

    print("\n[4] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.2", "After group 2.3")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    f1 = pc.f1
    rows = ["| Entry | Published | Clause 1 | Clause 2 | Verdict | Flag |", "|---|---:|---|---|---:|---|"]
    for c in mine:
        r = UNITS[(c, CRIT)]
        rows.append(f"| {c} | {f1(pub[c])} | {pc.STATUS[r['clauses'][0][0]]} | {pc.STATUS[r['clauses'][1][0]]} | "
                    f"{f1(r['verdict'])} | {('toward ' + r['flag'][0]) if r['flag'] else ''} |")
    t["summary"] = "\n".join(rows)
    for c in mine:
        r = UNITS[(c, CRIT)]
        lines = [f"#### {c} {CRIT} {p.v2[CRIT]['name']}: {f1(pub[c])} → {f1(r['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (st, est, src) in enumerate(r["clauses"]):
            lines.append(f"| {i + 1} | {p.v2[CRIT]['definition']['clauses'][i]} | {pc.STATUS[st]} | {est} | {src} |")
        if r["zero"]:
            lines += ["", f"*0.0 (protocol 2.1):* {r['zero']}."]
        if r["flag"]:
            lines += ["", f"*Flag (reading {r['flag'][1]}):* toward {r['flag'][0]}."]
        if r["note"]:
            lines += ["", f"*Note:* {r['note']}."]
        t[f"unit {c}"] = "\n".join(lines)
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
    print("\nRESCORING STAGE 2, GROUP 2.3, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.3: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
