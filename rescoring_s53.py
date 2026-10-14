#!/usr/bin/env python3
"""
rescoring_s53.py -- NEEC rescoring pass, stage 2, group 2.2: C1.2a Wealth Building for Resilience, class M
==========================================================================================================
Session 53. The first group written on the shared module (pass_common.py, decision 52.5) and the first class M
re-read of a whole criterion: all 23 units of C1.2a are re-read clause by clause against v2.0's text (Appendix V of
NEEC_Criteria_v2_s45.md; criteria.json), whose restatement (K6, R2) sets the bar in constant 2019 US dollars at
purchasing-power parity and removes the Cultural/Geographic Adaptation field. Readings: NEEC_Rescoring_s53.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry on C1.2a, each against its published score; which rise, fall or hold
  [2] the price basis: every 2019-PPP figure the readings quote is recomputed here from the series it holds (World
      Bank WDI, BLS CPI-U) and must appear in the unit's estimate
  [3] the design's model: cco_c12a_checks_s53_output.txt by digest, and every figure the readings quote from it
  [4] the corrections (reading 3.6) and the flags (reading 3.1)
Sources not in this repository (the SCF 2025 extract, Statistics Norway's tables, the UBS figures the scoring
documents cite) are named with their identifiers; every figure used from them is held below.

Usage: python3 rescoring_s53.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, cco_c12a_checks_s53_output.txt,
                                             NEEC_Rescoring_s53.md; writes nothing)
       python3 rescoring_s53.py --tables   (prints the generated tables as JSON, for the record)
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

TAG, RECORD, CRIT = "(2.2)", "NEEC_Rescoring_s53.md", "C1.2a"
SIMOUT, SIMMD5 = "cco_c12a_checks_s53_output.txt", "197a5c016745eb9dea094a5b36a56c6e"
UNITS = {}
GENERATED = {}


def U(code, verdict, status, est, src, flag=None, note="", zero=None):
    """One unit of C1.2a (one clause). flag: (alternative, reading). zero: protocol 2.1's whole-criterion reason."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[(status, est, src)], flag=flag, note=note, zero=zero)


# ---- the price basis (reading 3.3): series held, figures recomputed in check [2] --------------------------------------
CPIU = {2019: 255.657, 2023: 304.702}
CPIU_2025_MONTHS = (317.671, 319.082, 319.799, 320.795, 321.465, 322.561, 323.048, 323.976, 324.800, 324.122, 324.054)
WDI = {  # PA.NUS.PRVT.PP 2019 (LCU per international $), FP.CPI.TOTL (2010 = 100), PA.NUS.FCRF (LCU per US$)
    "NOR": {"ppp": 10.1439, "cpi": {2019: 120.3067, 2024: 145.1758}},
    "SGP": {"ppp": 1.0697, "cpi": {2019: 114.438, 2025: 134.3596}, "fx": {2025: 1.3075}},
    "QAT": {"ppp": 2.7226, "cpi": {2019: 115.3808, 2024: 126.022}, "fx": {2024: 3.64}},
    "CHN": {"ppp": 4.045, "cpi": {2019: 125.0832, 2022: 131.9194}, "fx": {2022: 6.7372}},
}
SCF = {"all": 66.3, "45-54": 71.6, "p30_2025": 55200, "med_2025": 216100}      # computed from SCFP2025.csv, weighted
SSB = {"d4": 390300, "d5": 1131000, "neg": 15.8}                                # NOK, 2024, households


def cpiu2025():
    return sum(CPIU_2025_MONTHS) / len(CPIU_2025_MONTHS)


def to2019(country, value_usd_or_lcu, year, lcu=False):
    w = WDI[country]
    lcu_v = value_usd_or_lcu if lcu else value_usd_or_lcu * w["fx"][year]
    return lcu_v / (w["cpi"][year] / w["cpi"][2019]) / w["ppp"]


def usd(x):
    return f"${round(x):,}"


FIGS = {
    "us_bar": usd(60000 * cpiu2025() / CPIU[2019]),
    "us_p30": usd(SCF["p30_2025"] * CPIU[2019] / cpiu2025()),
    "us_med": usd(SCF["med_2025"] * CPIU[2019] / cpiu2025()),
    "no_bar": f"NOK {round(60000 * WDI['NOR']['ppp'] * WDI['NOR']['cpi'][2024] / WDI['NOR']['cpi'][2019]):,}",
    "no_p30": usd(to2019("NOR", SSB["d4"], 2024, lcu=True)),
    "no_p40": usd(to2019("NOR", SSB["d5"], 2024, lcu=True)),
    "sg_med": usd(to2019("SGP", 96434, 2025)),
    "qa_med": usd(to2019("QAT", 95499, 2024)),
    "cn_med": usd(to2019("CHN", 27273, 2022)),
}

# ---- sources -------------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
RETRO = "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md"
WDI_SRC = ("World Bank WDI, PPP conversion factor for private consumption 2019 (PA.NUS.PRVT.PP), CPI (FP.CPI.TOTL) "
           "and official exchange rate (PA.NUS.FCRF), retrieved 2026-10-14")
CPI_SRC = ("BLS CPI-U, US city average (CUUR0000SA0; FRED CPIAUCNS), annual averages 2019 and 2023, 2025 the mean of "
           "its eleven published months")
SCF_SRC = ("Federal Reserve Board, 2025 Survey of Consumer Finances, summary extract SCFP2025.csv in scfp2025excel.zip "
           "(md5 c938318c), 2025 dollars, weighted, all five implicates")
SSB_SRC = ("Statistics Norway, Income and wealth statistics for households 2024, Table 4 (StatBank 10318, deciles of net "
           "wealth) and Table 3 (10315); students excluded, pension wealth not included")
SIM_SRC = ("Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); "
           "cco_c12a_checks_s53_output.txt; the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73), NEEC note 1")
SIM_FIG = {"share": "76.6%", "share_a": "77.4%", "seeds": "500 of 500", "med": "$382,005", "p30": "$141,971",
           "base": "41.4%", "save": "47.2%", "adv": "46.6%", "bar23": "$71510"}
ALT = ("1.0 on the engaged-participants reading (reading 3.1): the median accumulation of those who use the economy's "
       "accumulation vehicles, with breadth left to C1.5")

# ---- the units (readings in NEEC_Rescoring_s53.md, section 3) --------------------------------------------------------
U("SQ", 0.5, "S",
  f"on v2.0's price basis the bar is {FIGS['us_bar']} in 2025 dollars; in the 2025 Survey of Consumer Finances 66.3% of "
  f"US families hold net worth at or above it, a lifetime stock that overstates 20 years' accumulation, so fewer than "
  f"70% reach the figure; the 30th percentile is {FIGS['us_p30']} and the median {FIGS['us_med']} (2019 dollars); among "
  "families whose head is 45 to 54, about 20 to 30 years into working life, 71.6% hold the bar's figure, before "
  "subtracting what they held at the start (reading 3.5); homeownership and retirement accounts are genuine vehicles, "
  "so the unit is 0.5, not 0.0",
  f"{SCF_SRC}; {CPI_SRC}; {REP}System 1, C1.2a", flag=(ALT, "3.1"),
  note="the published rationale's bottom-half figure (~$3,200, from the Paper's calibration of 2019) is replaced by "
       "the 2025 survey's distribution, which v2.0's measure names; the verdict is unchanged")
U("NSD", 0.5, "S",
  f"no figure in the published rationale, which credited the vehicles for those who use them and left breadth to "
  f"C1.5; on Norway's register data for 2024 the bar is {FIGS['no_bar']}, and the 30th percentile of household net "
  f"wealth is NOK 390,300 ({FIGS['no_p30']} in 2019 dollars at PPP) while the 40th is NOK 1,131,000 "
  f"({FIGS['no_p40']}): between 60% and 70% of households hold the bar's figure, and 15.8% hold negative net wealth; "
  "the register excludes pension wealth, so collective and public pension entitlements are not counted (reading 3.5)",
  f"{SSB_SRC}; {WDI_SRC}; {REP}System 2, C1.2a", flag=(ALT, "3.1"),
  note="published 1.0 read in the D28 form: the clause is short on the one Nordic register that publishes the "
       "distribution, so the unit falls to 0.5; Sweden publishes no household wealth statistics, and no Nordic "
       "source located shows 70% of households at the figure")
U("CPS", 0.0, "S",
  "no accumulation vehicle beyond minimal personal property; the savings-bank deposits households did hold were "
  "frozen and then erased by the price liberalisation of 1992, so the historical record shows no buffer that "
  "survived; far below the bar for any share of participants",
  f"{REP}System 3, C1.2a; {RETRO}, System 3",
  zero="no structural mechanism addresses the criterion, and the historical record, collapse included (protocol 4.1), "
       "shows no credible pathway under the system's own logic")
U("MS", 0.5, "U",
  "the rationale's evidence is qualitative: Mondragón members 'accumulate substantial wealth through capital accounts "
  "and profit distribution'; no source the unit cites states an accumulation figure, or the share of participants "
  "whose capital accounts and other net worth reach $60,000 (2019 dollars) over 20 years; a genuine, individually "
  "held vehicle, not shown at the bar for 70% of participants",
  f"{REP}System 4, C1.2a; Paper v1.4, Appendix H.8a",
  note="published 1.0 read in the D28 form (silence is not clearance, protocol 2.3(b)): the unit falls to 0.5; it is "
       "the 1.0 band's anchor example, which the anchors line reports")
U("LM", 0.5, "U",
  "the system's own markets are its accumulation vehicles (property, ownership of enterprises, private saving), the "
  "same vehicles Status Quo Market Capitalism's unit credits at 0.5; the published 0.0 rested on their reach ('those "
  "born poor cannot accumulate initial capital'), which is the 0.5 band's partial coverage, not the absence of a "
  "mechanism; no source shows 70% of participants at the bar",
  f"{REP}System 5, C1.2a; {RETRO}, System 5", flag=("0.0, the published reading", "3.6"),
  note="a correction (reading 3.6): a reach shortfall is a 0.5 under protocol 2.1, as for Status Quo, Stakeholder "
       "Capitalism and China; one failure fewer, no tier change")
U("MMT", 0.0, "R",
  "the Job Guarantee pays a wage and benefits; it holds no asset for its participants; the published 0.5 credited "
  "'traditional markets', the host economy's vehicles, which the reach rule does not credit to a mechanism (protocol "
  "3.2, D28(c)); generalised over the economy, the mechanism governs income, not accumulation",
  f"{REP}System 6, C1.2a; {RETRO}, System 6; SCORING_PROTOCOL.md 3.2", flag=("0.5, the published reading", "3.6"),
  note="a correction (reading 3.6): income without an accumulation vehicle is the 0.0 band, as for Universal Basic "
       "Income and Georgism's dividend; one failure more, no tier change",
  zero="no structural mechanism addresses the criterion: income only, the 0.0 band's own description (Appendix H.7v2)")
U("UBI", 0.0, "R",
  "an income transfer; no accumulation vehicle; the 0.0 band's own anchor case",
  f"{REP}System 7, C1.2a; Paper v1.4, Appendix H.7v2",
  zero="no structural mechanism addresses the criterion: income only (the band's anchor)")
U("DG", 0.5, "U",
  "community land trusts and cooperatives give real, collectively held security; individual accumulation is "
  "discouraged by design, and no source states a household figure; the 0.5 band's anchor case",
  f"{REP}System 8, C1.2a; Paper v1.4, Appendix H.7v2")
U("SC", 0.5, "S",
  "the vehicles are Status Quo's (homeownership, retirement accounts) with incremental stock options and "
  f"profit-sharing; on the 2025 Survey of Consumer Finances 66.3% of families hold the bar's figure, short of 70%, "
  "and no source shows the reform raising it",
  f"{REP}System 9, C1.2a; {SCF_SRC}")
U("FALC", 0.0, "S",
  "no vehicle of any kind, individual or collective, is specified; 'abundance makes accumulation less relevant' "
  "describes consumption access, not a buffer",
  f"{REP}System 10, C1.2a; {RETRO}, System 10",
  zero="no structural mechanism addresses the criterion")
U("PE", 0.5, "U",
  "no private accumulation; named community investment councils can build collective wealth; no figure or "
  "household buffer is stated; the 0.5 band's collectively held case",
  f"{REP}System 11, C1.2a; {RETRO}, System 11")
U("CCO", 0.5, "U",
  f"on the design's published model at v4.20 (500 seeds, the reference settings, prices constant), "
  f"{SIM_FIG['share']} of agents accumulate $60,000 or more in 2019 dollars over 20 years ({SIM_FIG['share_a']} "
  f"with acre equity), {SIM_FIG['seeds']} seeds at 70% or more, median {SIM_FIG['med']}, against {SIM_FIG['base']} in "
  f"the matched Baseline; but the engine adds wage income less the basket's cost to wealth, so an agent saves every "
  f"dollar above its basket, and agents keep {SIM_FIG['save']} of 20 years' cash income as net worth, more than five "
  "times the US personal saving rate of 3.4% to 5.6% (2022-2025); acre equity adds little; in the Adverse Environment "
  f"{SIM_FIG['adv']} reach the figure; the rationale's $70,000+ is the papers', and the engine's documentation states "
  "that the papers' wealth figure is not produced by the engine (reading 3.4)",
  f"{SIM_SRC}; {REP}System 12, C1.2a",
  flag=("1.0: the engine's own figure clears the bar in every seed", "3.4"),
  note="published 1.0 read in the D28 form: the projection holds only under the engine's saving rule, a favourable "
       "and untested condition (protocol 2.1, 0.5), so the clause is not shown; for version 2.1, a version of the "
       "model with a sourced consumption rule that still shows 70% at the bar would clear it")
U("INT", 0.0, "S",
  "Integral Time Credits cannot be saved or accumulated by design; no other vehicle; the 0.0 band's anchor case",
  f"{REP}System 13, C1.2a; Paper v1.4, Appendix E",
  zero="the system excludes accumulation by design (the band's anchor)")
U("GEO", 0.0, "R",
  "the citizen's dividend is an annual pass-through of land rent, income rather than a held corpus; lower taxes on "
  "income and capital raise saving capacity in the host economy, which the reach rule does not credit",
  "NEEC_Georgism_LVT_scoring_scratch.md, C1.2a; SCORING_PROTOCOL.md 3.2",
  zero="no structural mechanism addresses the criterion: the mechanism's payment is income only")
U("MC", 0.0, "S",
  "credit balances are claims on other members in a non-convertible unit, capped and in some designs subject to "
  "demurrage; no store of value usable as a buffer, for any participant",
  "NEEC_MutualCredit_LETS_scoring_scratch.md, C1.2a",
  zero="no structural mechanism addresses the criterion: the instrument has no accumulation function by design")
U("DE", 0.0, "S",
  "the framework names the categories of wealth and cites others' vehicles as compatible, but adopts none as its "
  "own; no implementation reviewed established an accumulation vehicle",
  "NEEC_DoughnutEconomics_scoring_scratch.md, C1.2a",
  zero="no structural mechanism of the system's own addresses the criterion (the published flag toward 0.5 stands)")
U("UBS", 0.0, "R",
  "in-kind services, among them zero-rent social housing, reduce expenses but create no asset, deed or account",
  "NEEC_UniversalBasicServices_scoring_scratch.md, C1.2a",
  zero="no structural mechanism addresses the criterion: services, not assets")
U("SWF", 0.5, "S",
  "a large, growing, professionally invested corpus held collectively; no individual holds a titled or severable "
  "claim, so no household's net worth includes it; the 0.5 band's collectively held case",
  "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.2a",
  note="the published flag toward 0.0 stands")
U("CN", 0.5, "S",
  f"UBS's median wealth per adult, $27,273 at end-2022, is {FIGS['cn_med']} in 2019 dollars at PPP, under the bar, so "
  "fewer than half of adults hold the figure; v2.0 removes the middle-income adjustment on which the published "
  "rationale judged the magnitude likely to clear; homeownership near 90% is a genuine, individually titled vehicle, "
  "impaired by falling prices and restricted rural land rights",
  f"NEEC_StateCapitalism_China_scoring_scratch.md, C1.2a; {WDI_SRC}",
  note="the published flag toward 1.0, a magnitude-first reading of the adjusted bar, is removed: the adjustment no "
       "longer exists and the median is below the bar")
U("SG", 0.5, "U",
  f"UBS's median wealth per adult, $96,434 at end-2025, is {FIGS['sg_med']} in 2019 dollars at PPP, above the bar; "
  "but the clause asks for 70% of participants, and the scoring document estimates that about 75% of the population "
  "has a genuine vehicle, Work Permit holders (about a fifth) having none; no published distribution shows 70% of all "
  "who live and work in the economy at the figure, and 20-year accumulation, lease decay aside, is not reported",
  f"NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.2a; {WDI_SRC}", flag=(ALT, "3.1"),
  note="published 1.0 read in the D28 form: the median alone does not show the 70% clause, so the unit falls to 0.5")
U("QA", 0.5, "S",
  f"for citizens a generous vehicle (free plots, near-interest-free housing loans, a pension); UBS's median wealth per "
  f"adult, $95,499, is {FIGS['qa_med']} in 2019 dollars at PPP, a figure the scoring document could not reconcile "
  "with the wage structure; citizens are 9% to 13% of residents, migrant workers have no pension and restricted "
  "ownership, and well under half of residents have a vehicle reaching the figure",
  f"NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.2a; {WDI_SRC}", flag=(ALT, "3.1"))
U("IF", 0.5, "U",
  "profit-sharing investment accounts are a genuine, individually held, accumulating vehicle; returns are smoothed "
  "to market benchmarks, so accumulation is indistinguishable from bank saving in the host economy, which the reach "
  "rule does not credit; nothing shows 70% of participants at the bar through the mechanism",
  "NEEC_IslamicFinance_scoring_scratch.md, C1.2a; SCORING_PROTOCOL.md 3.2",
  note="the published flag toward 1.0 (PSIAs treated as reaching most participants) is removed: reach alone does not "
       "show the bar's figure, and the figure the host economy produces is not the mechanism's")
U("OS", 0.0, "S",
  "a member's claim on the commons is a use-right, non-severable and extinguished on exit; no individual balance "
  "grows; no case reports household accumulation of the bar's order",
  "NEEC_Ostrom_Commons_scoring_scratch.md, C1.2a",
  zero="no structural mechanism addresses the criterion: use-rights, not assets (the published flag toward 0.5 stands)")

EXPECT = {"fall": ["NSD", "MS", "MMT", "CCO", "SG"], "rise": ["LM"], "corrections": ["LM", "MMT"],
          "alt_flags": ["SQ", "NSD", "SG", "QA"], "zero": ["CPS", "MMT", "UBI", "FALC", "INT", "GEO", "MC", "DE", "UBS",
                                                            "OS"]}


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
    print(f"NEEC rescoring pass, stage 2, group 2.2: C1.2a Wealth Building for Resilience, class M ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{SIMOUT}, {RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    check(sorted(c for c, _ in UNITS) == sorted(p.order) and not any(k in p.merged for k in UNITS),
          f"one unit per entry on {CRIT}, {len(UNITS)} in all, none re-estimated before this group")
    check(p.v2[CRIT]["revision"]["cls"] == "M" and len(p.v2[CRIT]["definition"]["clauses"]) == 1,
          f"{CRIT} is class M with one clause in v2.0")
    fall = [c for c in p.order if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in p.order if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores 1.0 x{sum(v == 1.0 for v in pub.values())}, 0.5 x{sum(v == 0.5 for v in pub.values())}, "
          f"0.0 x{sum(v == 0.0 for v in pub.values())}; this group lowers {len(fall)} ({', '.join(fall)}), raises "
          f"{len(rise)} ({', '.join(rise)}) and holds {len(UNITS) - len(fall) - len(rise)}")
    zeros = [c for c in p.order if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 for c in zeros),
          f"{len(zeros)} units are 0.0, each on a stated whole-criterion reason (protocol 2.1), never on the clause "
          "alone (D28(f))")
    ones = [c for c in p.order if UNITS[(c, CRIT)]["verdict"] == 1.0]
    check(not ones, "no unit clears the clause on v2.0's reading: no entry is at 1.0 on C1.2a after this group")

    print("\n[2] THE PRICE BASIS (reading 3.3): figures recomputed from the series held here")
    c25 = cpiu2025()
    check(len(CPIU_2025_MONTHS) == 11 and round(c25, 3) == 321.943 and FIGS["us_bar"] == "$75,557",
          f"CPI-U 2025 from its eleven published months, {c25:.3f}; the bar is {FIGS['us_bar']} in 2025 dollars and "
          f"${round(60000 * CPIU[2023] / CPIU[2019]):,} in 2023 dollars, the engine's")
    where = {"us_bar": "SQ", "us_p30": "SQ", "us_med": "SQ", "no_bar": "NSD", "no_p30": "NSD", "no_p40": "NSD",
             "sg_med": "SG", "qa_med": "QA", "cn_med": "CN"}
    miss = [k for k, c in where.items() if FIGS[k] not in UNITS[(c, CRIT)]["clauses"][0][1]]
    check(not miss, "every converted figure appears in its unit's estimate: " +
          ", ".join(f"{where[k]} {FIGS[k]}" for k in where), ", ".join(miss))
    check(round(to2019("CHN", 27273, 2022)) < 60000 and round(to2019("NOR", SSB["d4"], 2024, lcu=True)) < 60000 <
          round(to2019("NOR", SSB["d5"], 2024, lcu=True)) and SCF["all"] < 70,
          "China's median, Norway's 30th percentile and the US share fall short of the bar; Norway's 40th percentile "
          "clears it, so between 60% and 70% of Norwegian households hold the figure")
    check(to2019("SGP", 96434, 2025) > 60000 and to2019("QAT", 95499, 2024) > 60000,
          "Singapore's and Qatar's medians clear the bar's figure, which the 70% clause does not settle (reading 3.5)")

    print("\n[3] THE DESIGN'S MODEL (reading 3.4)")
    raw = open(os.path.join(HERE, SIMOUT), "rb").read() if os.path.isfile(os.path.join(HERE, SIMOUT)) else b""
    check(hashlib.md5(raw).hexdigest() == SIMMD5, f"{SIMOUT} md5 {hashlib.md5(raw).hexdigest()[:8]} "
          f"(node cco_c12a_checks_s53.js on harness.js and index.html at 5a7a7b1)")
    txt = raw.decode("utf-8")
    check("ALL PASSED" in txt and "FAIL" not in txt, "the runs' own checks all passed, the runner reproducing "
          "runScenario() on every seed")
    lost = [f for f in SIM_FIG.values() if f not in txt]
    cco = UNITS[("CCO", CRIT)]["clauses"][0][1]
    check(not lost and all(SIM_FIG[k] in cco for k in ("share", "share_a", "seeds", "med", "base", "save", "adv")),
          "every figure the CCO unit quotes appears in the runs' output", ", ".join(lost))

    print("\n[4] CORRECTIONS AND FLAGS")
    corr = [c for c in p.order if "a correction" in UNITS[(c, CRIT)]["note"]]
    check(corr == EXPECT["corrections"], f"corrections (reading 3.6): {', '.join(corr)}")
    alt = [c for c in p.order if (UNITS[(c, CRIT)]["flag"] or ("", ""))[1] == "3.1"]
    check(alt == EXPECT["alt_flags"] and all(UNITS[(c, CRIT)]["verdict"] == 0.5 for c in alt),
          f"units the engaged-participants reading would raise to 1.0, each flagged: {', '.join(alt)}")

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.1", "After group 2.2")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    f1 = pc.f1
    rows = ["| Entry | Published | Clause | Verdict | Flag |", "|---|---:|---|---:|---|"]
    for c in p.order:
        r = UNITS[(c, CRIT)]
        rows.append(f"| {c} | {f1(pub[c])} | {pc.STATUS[r['clauses'][0][0]]} | {f1(r['verdict'])} | "
                    f"{('toward ' + r['flag'][0]) if r['flag'] else ''} |")
    t["summary"] = "\n".join(rows)
    for c in p.order:
        r = UNITS[(c, CRIT)]
        st, est, src = r["clauses"][0]
        lines = [f"#### {c} {CRIT} {p.v2[CRIT]['name']}: {f1(pub[c])} → {f1(r['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|",
                 f"| 1 | {p.v2[CRIT]['definition']['clauses'][0]} | {pc.STATUS[st]} | {est} | {src} |"]
        if r["zero"]:
            lines += ["", f"*0.0 (protocol 2.1):* {r['zero']}."]
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
    print("\nRESCORING STAGE 2, GROUP 2.2, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.2: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
