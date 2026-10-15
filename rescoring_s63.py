#!/usr/bin/env python3
"""
rescoring_s63.py -- NEEC rescoring pass, stage 2, group 2.9: C3.1 Crisis Response Capacity, class I
=====================================================================================================
Session 63. The 16 units of C3.1 the pass had not re-estimated are read clause by clause against v2.0's text
(criteria.json; NEEC_Criteria_v2_s45.md, Appendix V), which keeps C3.1's three clauses ("Response within 72 hours",
"scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase)", ">=90% population coverage") and names the
measure: days from a shock's trigger, the first official data showing it, to the first increased payment, with no
legislative delay (for a configured national economy, from the dated record of its response to its most recent major
shock); the percentage change in social benefits received by households (SNA item D.62) against the percentage fall in
real GDP in that shock; the share of the population covered by at least one social protection cash benefit (ILO, SDG
indicator 1.3.1). For a design the clauses are read from its rules. The seven entries whose published 1.0s the pass
read earlier (parts (a) and (b2)) hold at 0.5 and are not re-read. Readings: NEEC_Rescoring_s63.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry not yet re-estimated on C3.1, each against its published score; which rise, fall
      or hold; the 0.0 and its reason; that none is 1.0
  [2] the evidence cache (evidence_cache/C3.1/): Session 62's index and rationale digests, and the ten data files
      Session 63 added (evidence_cache_s63.py), each by digest with every passage quoted found in it
  [3] the figures the readings quote, recomputed from the cache's data files (the United States' benefits against real
      GDP; the coverage of the five economies)
  [4] the flags
Sources not in this repository are named with their identifiers; every figure used from them is held in the cache.

Usage: python3 rescoring_s63.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, the files of evidence_cache/C3.1/,
                                             the scoring documents holding the units' rationales, NEEC_Rescoring_s63.md;
                                             writes nothing)
       python3 rescoring_s63.py --tables   (prints the generated tables as JSON, for the record)
Prints file names and summaries only. Deterministic.
"""
import csv
import hashlib
import io
import json
import os
import re
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD, CRIT = "(2.9)", "NEEC_Rescoring_s63.md", "C3.1"
CACHE = "evidence_cache/C3.1/"
UNITS = {}
GENERATED = {}


def U(code, verdict, c1, c2, c3, flag=None, note="", zero=None):
    """One unit of C3.1. c1, c2, c3: (status, estimate, source) for the three v2.0 clauses. flag: (alternative,
    reading). zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[c1, c2, c3], flag=flag, note=note, zero=zero)


# ---- the cache (Session 63's data files; md5s as written by evidence_cache_s63.py) -----------------------------------
MD5 = {"fred_benefits_annual.csv": "4fd07cd0e2c379d411929947d7e5f8e0",
       "fred_realgdp_annual.csv": "d23ccfc7fe4b7d96d788af71f8586eea",
       "fred_benefits_monthly.csv": "db9a37ab5d29517f70bbf6deb416c535",
       "fred_claims_weekly.csv": "e6c1c2008b9d47374401cde830f79b2e",
       "sdg131_840.json": "a31a4ebbb59c697ded39214b3acbe601",
       "sdg131_156.json": "f605e05515a3af2b34b79e60f05134c2",
       "sdg131_702.json": "4fa1ce300bbb027338d2dfdc66305887",
       "sdg131_634.json": "445c4aa3ff7aa8ca27e63924f0d09a53",
       "sdg131_578.json": "9a6381d62c39791ceede8b90e524f2de",
       "cares_act_wikipedia_lead.txt": "087f06f3"}   # prefix: checked below against the file
QUOTES = {
    "fred_benefits_annual.csv": ["2019-01-01,3090.760", "2020-01-01,4187.512"],
    "fred_realgdp_annual.csv": ["2019-01-01,20715.671", "2020-01-01,20284.500"],
    "fred_benefits_monthly.csv": ["2020-03-01,3235.1", "2020-04-01,6397.7"],
    "fred_claims_weekly.csv": ["2020-03-14,273000", "2020-03-21,2914000"],
    "sdg131_840.json": ["ILO - Social Security Inquiry Database", "78.8"],
    "sdg131_156.json": ["ILO - Social Security Inquiry Database", "75.6"],
    "sdg131_702.json": ["ILO - Social Security Inquiry Database"],
    "sdg131_634.json": ["ILO - Social Security Inquiry Database", "4.1"],
    "sdg131_578.json": ["ILO - Social Security Inquiry Database", "99.3"],
    "cares_act_wikipedia_lead.txt": ["signed into law by President Donald Trump on March 27, 2020"],
}
# the published rationales: (file, line of the C3.1 heading), as Session 62's index holds them
RAT = {"SQ": ("NEEC_Report_v1_6.md", 318), "CPS": ("NEEC_Report_v1_6.md", 496), "MS": ("NEEC_Report_v1_6.md", 586),
       "LM": ("NEEC_Report_v1_6.md", 676), "SC": ("NEEC_Report_v1_6.md", 1036), "FALC": ("NEEC_Report_v1_6.md", 1126),
       "GEO": ("NEEC_Georgism_LVT_scoring_scratch.md", 339), "MC": ("NEEC_MutualCredit_LETS_scoring_scratch.md", 366),
       "DE": ("NEEC_DoughnutEconomics_scoring_scratch.md", 383),
       "UBS": ("NEEC_UniversalBasicServices_scoring_scratch.md", 427),
       "SWF": ("NEEC_SovereignWealthFundStatism_scoring_scratch.md", 387),
       "CN": ("NEEC_StateCapitalism_China_scoring_scratch.md", 503),
       "SG": ("NEEC_StateCapitalism_Singapore_scoring_scratch.md", 477),
       "QA": ("NEEC_StateCapitalism_Qatar_scoring_scratch.md", 539),
       "IF": ("NEEC_IslamicFinance_scoring_scratch.md", 383), "OS": ("NEEC_Ostrom_Commons_scoring_scratch.md", 416)}


def rationale_md5(f, n):
    """md5 of the rationale text as Session 62's index took it (evidence_cache_s62.unit_record)."""
    lines = open(os.path.join(HERE, f), encoding="utf-8").read().split("\n")
    if f == "NEEC_Report_v1_6.md":
        text = lines[n - 1]
    else:
        out = [lines[n - 1]]
        for t in lines[n:]:
            m = re.match(r"(#+) ", t)
            if m and len(m.group(1)) <= 4:
                break
            out.append(t)
        text = "\n".join(out).strip()
    return hashlib.md5(text.encode()).hexdigest()


def cached(name):
    return open(os.path.join(HERE, CACHE, name), encoding="utf-8").read()


# ---- the figures, computed from the cache ----------------------------------------------------------------------------
def series_csv(name):
    rows = list(csv.reader(io.StringIO(cached(name))))[1:]
    return {r[0]: float(r[1]) for r in rows}


def us_figs():
    ben, gdp = series_csv("fred_benefits_annual.csv"), series_csv("fred_realgdp_annual.csv")
    mon, clm = series_csv("fred_benefits_monthly.csv"), series_csv("fred_claims_weekly.csv")
    b19, b20, g19, g20 = ben["2019-01-01"], ben["2020-01-01"], gdp["2019-01-01"], gdp["2020-01-01"]
    pb, pg = 100.0 * (b20 / b19 - 1), 100.0 * (g20 / g19 - 1)
    return {"b19": b19, "b20": b20, "g19": g19, "g20": g20, "pb": pb, "pg": pg, "ratio": pb / -pg,
            "feb": mon["2020-02-01"], "mar": mon["2020-03-01"], "apr": mon["2020-04-01"],
            "pm_mar": 100.0 * (mon["2020-03-01"] / mon["2020-02-01"] - 1),
            "pm_apr": 100.0 * (mon["2020-04-01"] / mon["2020-03-01"] - 1),
            "c14": clm["2020-03-14"], "c21": clm["2020-03-21"], "c07": clm["2020-03-07"]}


def sdg(area):
    d = json.loads(cached(f"sdg131_{area}.json"))
    out = {}
    for r in d["data"]:
        if r["dimensions"]["Sex"] == "BOTHSEX":
            out[int(r["timePeriodStart"])] = float(r["value"])
    return out


F = us_figs()
COV = {"US": sdg(840), "CN": sdg(156), "SG": sdg(702), "QA": sdg(634), "NO": sdg(578)}


def f1(x):
    return f"{x:.1f}"


def sgn(x):
    return f"{x:+.1f}"


# ---- sources ---------------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
SDG_SRC = ("UN Statistics Division, SDG indicator database, series SI_COV_BENFTS (SDG 1.3.1, population covered by at "
           "least one social protection benefit), source ILO - Social Security Inquiry Database, estimated data, both "
           "sexes (" + CACHE + "sdg131_{}.json)")
FRED_SRC = ("U.S. Bureau of Economic Analysis through FRED: A063RC1A027NBEA (government social benefits to persons, "
            "billions of dollars, annual) and GDPCA (real gross domestic product, billions of chained 2017 dollars, "
            "annual), retrieved 2026-10-15 (" + CACHE + "fred_benefits_annual.csv, fred_realgdp_annual.csv)")
FRED_M = ("FRED: A063RC1 (monthly, seasonally adjusted annual rates) and ICSA (initial claims, weekly), retrieved "
          "2026-10-15 (" + CACHE + "fred_benefits_monthly.csv, fred_claims_weekly.csv); " + CACHE +
          "cares_act_wikipedia_lead.txt (the Act's date of signature)")
D62 = ("the series is the national accounts' government social benefits to persons, which includes Medicare and "
       "Medicaid; SNA item D.62 excludes benefits in kind, so the series is a proxy for it, and a proxy whose base is "
       "larger than D.62's, so that it understates the percentage rise in D.62")
NOLEG = ("the unit is a mechanism or a design whose rules state no payment that rises with a shock, no trigger and no "
         "number of days")
HOST = "the host economy's institutions are not credited to the mechanism (protocol 3.2)"


def sdg_src(area):
    return SDG_SRC.format(area)


# ---- the units (readings in NEEC_Rescoring_s63.md, section 3) -------------------------------------------------------
_c = COV
SQ1 = (f"the response was legislated, not triggered by rule: the weekly initial-claims series rose from "
       f"{F['c14']:,.0f} (week to 14 March 2020) to {F['c21']:,.0f} (week to 21 March), the Senate passed the CARES Act "
       f"on 25 March and the House on 26 March, and the President signed it on 27 March, six days after the week the "
       f"claims jumped; the monthly series of benefits paid rose {sgn(F['pm_mar'])}% in March and "
       f"{sgn(F['pm_apr'])}% in April ({F['feb']:,.1f}, {F['mar']:,.1f}, {F['apr']:,.1f} billion at annual rates in "
       "February, March and April), so the first large increase in payments came in April; not 72 hours, and not free "
       "of legislation (reading 3.2)")
SQ2 = (f"in 2020 government social benefits to persons rose {f1(F['pb'])}% ({F['b19']:,.1f} to {F['b20']:,.1f} billion "
       f"dollars) while real GDP fell {f1(-F['pg'])}% ({F['g19']:,.1f} to {F['g20']:,.1f} billion, chained 2017 "
       f"dollars), {f1(F['ratio'])} times the fall, far above 1:1; {D62}; the increase was legislated, which clause 1 "
       "and not this clause counts (reading 3.2)")
SQ3 = (f"{f1(_c['US'][2023])}% of the population covered by at least one benefit in 2023 ({f1(_c['US'][2015])}% in "
       "2015), against 90%: short, by 11 points (reading 3.2)")
U("SQ", 0.5, ("S", SQ1, f"{FRED_M}; {REP}SQ C3.1"), ("C", SQ2, FRED_SRC),
  ("S", SQ3, sdg_src(840)),
  flag=("0.0: reading the 0.0 band literally, response that 'requires legislative/political action': every increase "
        "in 2020 came by Act of Congress, the configuration's rules raise no payment with the shock, and the "
        "published rationale's months of delay refers to the response to the 2008 recession, which this record does "
        "not re-read", "3.2"),
  note="a correction (reading 3.2): the published 0.0 rests on 'three to six months of legislative debate', which the "
       "2020 record does not show (the Act was signed six days after the week of the claims jump), and on no automatic stabilizers scaling with severity; on the measure v2.0 names clause 2 is "
       "cleared and clause 3 is 11 points short, and under D28(f) and protocol 2.1 a unit with a cleared clause is "
       "not 0.0; the 0.0 band's own example, now held by Libertarian Minarchism alone")
U("CPS", 0.5, ("U", "the command economy could mobilise resources rapidly in WWII and disasters, by the entry's own "
                    "account, without legislative delay; no payment rule, trigger or day count is stated; " + NOLEG,
               f"{REP}CPS C3.1"),
  ("U", "chronic shortages meant perpetual intervention, not a payment that scales with a shock; no estimate of "
        "benefits against a fall in output is stated or located", f"{REP}CPS C3.1"),
  ("U", "employment is guaranteed by design, but no share of the population covered by a cash benefit is stated or "
        "located", f"{REP}CPS C3.1"),
  note="0.5 holds: a genuine capacity to mobilise without legislative delay, not shown at the clauses' levels, the "
       "0.5 band's description (reading 3.4)")
U("MS", 0.5, ("U", "cooperatives retain workers in a recession (layoff rates four to five times lower, by the entry); "
                   "no payment, trigger or day count at the level of the system", f"{REP}MS C3.1"),
  ("R", "firm-level resilience governs no social benefit; the entry's own finding is that it 'doesn't translate to "
        "system-level response'", f"{REP}MS C3.1"),
  ("R", "a firm-level mechanism reaches the members of the firms that adopt it, not the population; the economy's "
        "coverage is not credited to it (protocol 3.2)", f"{REP}MS C3.1"),
  note="0.5 holds: the 0.5 band's own anchor example, 'firm-level resilience doesn't translate to system-level "
       "response' (reading 3.4)")
U("LM", 0.0, ("S", "the design's functions exclude any crisis payment: no unemployment insurance, no disaster relief, "
                   "no crisis intervention", f"{REP}LM C3.1"),
  ("S", "no benefit exists to scale; markets are 'expected to self-correct while populations suffer'",
   f"{REP}LM C3.1"),
  ("S", "no cash benefit is paid, so coverage by one is nil by the design's rules", f"{REP}LM C3.1"),
  zero="the system is ideologically opposed to the criterion (the 0.0 band's second description) and has no "
       "mechanism that addresses it (protocol 2.1): the minimal state's functions rule out every stabilizing flow",
  note="0.0 holds; the 0.0 band's example, 'ideologically opposed to stabilization mechanisms' (reading 3.5)")
U("SC", 0.5, ("U", "stakeholder commitment could mean retaining workers rather than laying them off; no payment, "
                   "trigger or day count at the level of the system; " + HOST, f"{REP}SC C3.1"),
  ("R", "firm-level improvements govern no social benefit; the entry's own finding is that they do not translate to "
        "system-level crisis response; " + HOST, f"{REP}SC C3.1"),
  ("R", "a firm-level mechanism does not reach the population; " + HOST, f"{REP}SC C3.1"),
  note="0.5 holds, as Market Socialism's, the entry's text being the same (reading 3.4)")
U("FALC", 0.5, ("U", "automated production could respond rapidly to a crisis, by the entry; no payment, trigger or day "
                     "count is stated", f"{REP}FALC C3.1"),
  ("U", "universal provision is not a benefit that scales with a fall in output; the entry's concern is technical "
        "failure, not scaling", f"{REP}FALC C3.1"),
  ("U", "abundance is meant for everyone, but no share of the population covered by a cash benefit is stated",
   f"{REP}FALC C3.1"),
  note="0.5 holds (reading 3.4)")
U("GEO", 0.5, ("U", "the Citizen's Dividend would be an automatic annual or more frequent payment that continues "
                    "without a fresh legislative vote, as Alaska's does, so it needs no legislative delay; no payment "
                    "rises with the shock, so no response time can be counted",
               "NEEC_Georgism_LVT_scoring_scratch.md, C3.1"),
  ("S", "nothing in the design raises the dividend in a downturn; land-value revenue is prized for its stability "
        "across the cycle, so the payment does not scale with the fall in output", "NEEC_Georgism_LVT_scoring_scratch.md, C3.1"),
  ("U", "a universal flat payment reaches every resident in form, but no source states a share of the population "
        "covered", "NEEC_Georgism_LVT_scoring_scratch.md, C3.1"),
  note="0.5 holds: automatic continuity is real, automatic crisis-scaling is not part of the design (reading 3.4)")
U("MC", 0.5, ("U", "WIR credit circulation moves countercyclically (a 2009 study), Sardex was founded in response to "
                   "the credit crunch, and Argentina's Redes de Trueque grew to several million participants in 2001 "
                   "and 2002; no day count between a shock and a response is located",
              "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.1"),
  ("R", "mutual credit is not a social benefit; the countercyclical credit is a liquidity buffer for member firms",
   "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.1"),
  ("S", "self-selected networks of businesses, and a mobilisation that was 'neither universal nor centrally "
        "triggered'; far below 90% of the population", "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.1"),
  note="0.5 holds: the strongest peer-reviewed evidence in the corpus for a firm-level stabilizer, the 0.5 band's "
       "description (reading 3.4)")
U("DE", 0.5, ("U", "the model has no trigger-based disbursement; Amsterdam adopted it as a recovery strategy in April "
                   "2020, within weeks of the pandemic's onset, a response in policy framing and not a payment",
              "NEEC_DoughnutEconomics_scoring_scratch.md, C3.1"),
  ("R", "the model governs no benefit that could scale with a fall in output", "NEEC_DoughnutEconomics_scoring_scratch.md, C3.1"),
  ("R", "the model governs no cash benefit, so the share of a population covered by one is not a quantity it fixes",
   "NEEC_DoughnutEconomics_scoring_scratch.md, C3.1"),
  flag=("0.0: counting a single city's recovery framing as a crisis-response capacity at all, when the design "
        "supplies no mechanism that addresses any of the three clauses (protocol 2.1's first condition, as group "
        "2.7 read it for the same design on C1.4)", "3.4"),
  note="0.5 holds on its scoring document's finding of a real, rapid, local-level response (the 0.5 band's "
       "'local-level rather than system-wide'), flagged toward 0.0 (reading 3.4)")
U("UBS", 0.5, ("U", "services that run as a universal default need no activation in a crisis, since the 'trigger' "
                    "fired when the service became universal; no payment rises with the shock, so no response time "
                    "is counted", "NEEC_UniversalBasicServices_scoring_scratch.md, C3.1"),
  ("U", "there is no automatic benefit-scaling mechanism; government final consumption in kind is outside D.62, "
        "which counts benefits in cash", "NEEC_UniversalBasicServices_scoring_scratch.md, C3.1"),
  ("U", "universal provision covers every resident in form; no source states the share covered by a cash benefit",
   "NEEC_UniversalBasicServices_scoring_scratch.md, C3.1"),
  note="0.5 holds: a structural advantage of a different kind (permanent operation), with indirect evidence from the "
       "pandemic's essential-worker designations (reading 3.4)")
U("SWF", 0.5, ("S", "Norway's fiscal rule has a statutory escape clause for withdrawals 'to counteract economic "
                    "setbacks', used at record scale in 2020; the response took roughly two months from the pandemic's "
                    "onset to the Revised Budget of May 2020, set in a budget, not by a payment rule",
               "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.1"),
  ("U", "a 382-billion-kroner withdrawal (4.2% of the fund) scales at the level of the national budget, not at the "
        "household level, and no change in benefits against a fall in output is stated",
   "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.1"),
  ("U", f"Norway's welfare state covers {f1(_c['NO'][2023])}% of its population in 2023 on the ILO's measure, but "
        f"that is the host economy's, not the fund's (protocol 3.2); no share is stated for the fund's own payment "
        "(" + sdg_src(578) + ")", "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.1"),
  note="0.5 holds: real, rule-supported, demonstrated countercyclical capacity, budget-cycle in speed (reading 3.4)")
U("CN", 0.5, ("U", "the State Council decided on its 4-trillion-yuan stimulus on 5 November 2008 and announced it on 9 "
                   "November, without legislative delay, but the package was infrastructure-heavy and discretionary; "
                   "no dated first payment to households is located for either shock",
              "NEEC_StateCapitalism_China_scoring_scratch.md, C3.1"),
  ("U", "no series of household benefits against real GDP is located for the 2008 or the 2020 shock",
   "NEEC_StateCapitalism_China_scoring_scratch.md, C3.1"),
  ("S", f"{f1(_c['CN'][2021])}% of the population covered by at least one benefit in 2021 ({f1(_c['CN'][2015])}% in "
        f"2015, {f1(_c['CN'][2019])}% in 2019), against 90%: short, and rising "
        f"{f1(_c['CN'][2021] - _c['CN'][2015])} points in six years", sdg_src(156)),
  note="0.5 holds: fast, large, discretionary mobilisation without legislative delay, neither automatic nor "
       "household-level, and 14 points short on coverage (reading 3.3)")
U("SG", 0.5, ("S", "three budget packages in about two months in 2020, each needing a budget in Parliament and, for "
                   "reserve draws, the President's assent; wage support covered local workers; discretionary, so "
                   "not within 72 hours or free of legislation",
              "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.1"),
  ("U", "the Jobs Support Scheme raised its wage subsidy from 25% to 75%, a subsidy to employers, not a change in "
        "household benefits against a fall in real GDP (5.4% in 2020); no D.62 series is located",
   "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.1"),
  ("C", f"{f1(_c['SG'][2019])}% of the population covered by at least one benefit in 2019, 2020 and 2023 on the "
        "ILO's measure", sdg_src(702)),
  note="0.5 holds: coverage cleared, the response among the fastest and largest in the corpus but discretionary "
       "(reading 3.3)")
U("QA", 0.5, ("U", "the QR 75 billion package of March 2020 and the suspension of customs duties came without "
                   "legislative delay, because the emir holds legislative authority, but they are discretionary and "
                   "mostly to firms and banks; no dated first payment to households is located",
              "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.1"),
  ("U", "no series of household benefits against real GDP is located; the 2026 record shows spending falling 3.7% in "
        "the first quarter", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.1"),
  ("S", f"{f1(_c['QA'][2022])}% of the population covered by at least one benefit in 2022 ({f1(_c['QA'][2018])}% in "
        "2018), against 90%: non-citizens, most of the population, are outside social assistance and pensions",
   sdg_src(634)),
  flag=("0.0: reading coverage at 4% of the population, 86 points below the bar, with benefits allocated by "
        "nationality, as a system whose own logic offers no pathway to the clause (protocol 2.1)", "3.3"),
  note="0.5 holds on the speed and size of the discretionary response, flagged toward 0.0 on coverage (reading 3.3)")
U("IF", 0.5, ("U", "the resilience is a property of banks' business model, not a trigger-based payment; no day count "
                   "is located", "NEEC_IslamicFinance_scoring_scratch.md, C3.1"),
  ("R", "the mechanism governs no social benefit; " + HOST, "NEEC_IslamicFinance_scoring_scratch.md, C3.1"),
  ("R", "a bank-level property does not reach the population; " + HOST, "NEEC_IslamicFinance_scoring_scratch.md, C3.1"),
  note="0.5 holds: the 0.5 band's 'firm-level rather than system-wide', as its scoring document finds; its H.7 "
       "home is Market Socialism's (reading 3.4)")
U("OS", 0.5, ("U", "the Taos Valley acequias' rule changes in scarcity so that every member has enough to survive, "
                   "automatic and rule-based, no legislation, centuries old; no day count from a trigger is located",
              "NEEC_Ostrom_Commons_scoring_scratch.md, C3.1"),
  ("U", "the scarcity rule scales access to the resource with severity, within the resource the commons governs; no "
        "change in benefits against a fall in real GDP is stated", "NEEC_Ostrom_Commons_scoring_scratch.md, C3.1"),
  ("S", "90% of a population is unreachable for a bounded local institution, and it provides no crisis instrument "
        "outside the resource it governs", "NEEC_Ostrom_Commons_scoring_scratch.md, C3.1"),
  note="0.5 holds; the scoring document's scope scenario (D18(b): coverage read against the population the "
       "institution governs, which would raise the unit to 1.0) is a scenario and not a flag, and is kept as "
       "published (reading 3.6)")

EXPECT = {"rise": ["SQ"], "fall": [], "zero": ["LM"], "ones": [],
          "flags": {"SQ": "3.2", "DE": "3.4", "QA": "3.3"},
          "before": ["NSD", "MMT", "UBI", "DG", "PE", "CCO", "INT"]}


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
    print(f"NEEC rescoring pass, stage 2, group 2.9: C3.1 Crisis Response Capacity, class I ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{len(MD5)} data files and the index of {CACHE}, the scoring documents holding the units' rationales, "
          f"{RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(sorted(set(p.part_of[(c, CRIT)] for c in before)))}), each at "
          "0.5, and are not re-read")
    check(all(p.merged[(c, CRIT)]["verdict"] == 0.5 for c in before), "the seven earlier units stand at 0.5")
    d = p.v2[CRIT]["definition"]
    check(p.v2[CRIT]["revision"]["cls"] == "I" and len(d["clauses"]) == 3 and "SDG indicator 1.3.1" in d["measurement"]
          and "D.62" in d["measurement"] and "no legislative delay" in d["measurement"],
          f"{CRIT} is class I with three clauses in v2.0, measured as days to the first increased payment, D.62 "
          "against real GDP, and SDG 1.3.1 coverage")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group raises {len(rise)} ({', '.join(rise)}), lowers {len(fall)} and holds {len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 for c in zeros)
          and [c for c in zeros if pub[c] == 0.0] == ["LM"],
          f"{len(zeros)} unit is 0.0, on a stated whole-criterion reason (protocol 2.1): the published 0.0 of "
          "Libertarian Minarchism holds and Status Quo's does not")
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    after1 = [c for c in p.order if (UNITS.get((c, CRIT)) or p.merged.get((c, CRIT)) or {}).get("verdict") == 1.0]
    check(ones == EXPECT["ones"] and not after1,
          f"no unit clears all three clauses, so none is 1.0; after this group no entry is at 1.0 on {CRIT}")
    st = [s for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"]]
    cleared = sorted((c, i + 1) for c in mine for i, (s, _, _) in enumerate(UNITS[(c, CRIT)]["clauses"]) if s == "C")
    check(set(st) <= {"U", "S", "R", "C"} and cleared == [("SG", 3), ("SQ", 2)],
          f"{st.count('C')} clauses cleared (Singapore's coverage, Status Quo's scaling), {st.count('S')} short, "
          f"{st.count('R')} out of reach, {st.count('U')} not shown")

    print(f"\n[2] THE CACHE ({CACHE}) AND THE PUBLISHED RATIONALES")
    sess62 = json.load(open(os.path.join(HERE, CACHE, "index.json"), encoding="utf-8"))
    for name, want in MD5.items():
        path = os.path.join(HERE, CACHE, name)
        raw = open(path, "rb").read() if os.path.isfile(path) else b""
        txt = raw.decode("utf-8")
        lost = [q for q in QUOTES.get(name, []) if q not in txt]
        check(hashlib.md5(raw).hexdigest().startswith(want) and not lost,
              f"{name}: md5 {want[:8]}, {len(QUOTES.get(name, []))} passage(s) quoted found", ", ".join(lost))
    bad, moved = [], []
    for c in mine:
        f, n = RAT[c]
        lines = open(os.path.join(HERE, f), encoding="utf-8").read().split("\n")
        head = lines[n - 1].lstrip("# *")
        if not head.startswith(f"C3.1 Crisis Response Capacity: {f1(pub[c])}"):
            bad.append(c)
        u = sess62["units"][c]
        if (u["file"], u["line"]) != (f, n) or rationale_md5(f, n) != u["md5"]:
            moved.append(c)
    check(sorted(RAT) == sorted(mine) and not bad and not moved,
          f"each of the {len(mine)} published rationales is at the line held here, headed with its published score, "
          "and unchanged since Session 62's index (location and md5)", ", ".join(bad + moved))

    print("\n[3] THE FIGURES THE READINGS QUOTE (recomputed from the cache)")
    check(F["pb"] > 35 and F["pg"] < -2 and f1(F["pb"]) in UNITS[("SQ", CRIT)]["clauses"][1][1]
          and F["ratio"] > 1 and 16 < F["ratio"] < 18,
          f"United States, 2020: government social benefits {sgn(F['pb'])}% against real GDP {sgn(F['pg'])}%, "
          f"{f1(F['ratio'])} times the fall; the clause asks for at least 1:1")
    check(F["c21"] > 10 * F["c14"] and F["pm_apr"] > 90 and F["pm_mar"] < 5,
          f"United States, first months of 2020: weekly initial claims {F['c14']:,.0f} (to 14 March) and "
          f"{F['c21']:,.0f} (to 21 March); monthly benefits {sgn(F['pm_mar'])}% in March, {sgn(F['pm_apr'])}% in April")
    check(COV["US"][2023] < 90 and COV["CN"][2021] < 90 and COV["QA"][2022] < 10 and COV["SG"][2023] == 100.0
          and COV["NO"][2023] > 90,
          f"coverage on the ILO's measure: United States {f1(COV['US'][2023])}% (2023), China {f1(COV['CN'][2021])}% "
          f"(2021), Qatar {f1(COV['QA'][2022])}% (2022), Singapore {f1(COV['SG'][2023])}% (2023), Norway "
          f"{f1(COV['NO'][2023])}% (2023); the bar is 90%")
    check(f1(COV["CN"][2021]) in UNITS[("CN", CRIT)]["clauses"][2][1]
          and f1(COV["QA"][2022]) in UNITS[("QA", CRIT)]["clauses"][2][1]
          and f1(COV["US"][2023]) in UNITS[("SQ", CRIT)]["clauses"][2][1],
          "the coverage clauses of Status Quo, China and Qatar quote the recomputed figures")

    print("\n[4] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.8", "After group 2.9")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    rows_ = ["| Entry | Published | Response time | Scaling | Coverage | Verdict | Flag |", "|---|---:|---|---|---|---:|---|"]
    for c in mine:
        r = UNITS[(c, CRIT)]
        rows_.append(f"| {c} | {pc.f1(pub[c])} | " + " | ".join(pc.STATUS[x[0]] for x in r["clauses"]) +
                     f" | {pc.f1(r['verdict'])} | {('toward ' + r['flag'][0][:3]) if r['flag'] else ''} |")
    t["summary"] = "\n".join(rows_)
    for c in mine:
        r = UNITS[(c, CRIT)]
        lines = [f"#### {c} {CRIT} {p.v2[CRIT]['name']}: {pc.f1(pub[c])} → {pc.f1(r['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (s, est, src_) in enumerate(r["clauses"]):
            lines.append(f"| {i + 1} | {d['clauses'][i]} | {pc.STATUS[s]} | {est} | {src_} |")
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
    print("\nRESCORING STAGE 2, GROUP 2.9, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.9: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
