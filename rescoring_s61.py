#!/usr/bin/env python3
"""
rescoring_s61.py -- NEEC rescoring pass, stage 2, group 2.8: C4.3 Group Equity, class M
=========================================================================================
Session 61. The 16 units of C4.3 the pass had not re-estimated are re-read clause by clause against v2.0's text
(criteria.json; NEEC_Criteria_v2_s45.md, Appendix V), which keeps two clauses ("Disparity reduction >=5 percentage
points every 5 years", "convergence trajectory toward <20% disparities within 30 years") under the scope "on each
declared axis, non-citizen residents included", and names the measure: the gap between the median household incomes of
the least and most advantaged groups on each declared axis, as a percentage of the most advantaged group's median, from
national household surveys. Part (b8) (rescoring_s49.py, NEEC_Rescoring_s49.md) read the seven published 1.0s and set
the readings applied here (its readings 3.2 to 3.5); this group reads the 13 units at 0.5 and the three at 0.0, the four
configured national economies on their national household surveys. Readings: NEEC_Rescoring_s61.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry not yet re-estimated on C4.3, each against its published score; which rise, fall
      or hold; the 0.0s and their reasons; that none is 1.0
  [2] the evidence cache (evidence_cache/C4.3/): each file by digest, every passage quoted found in it; each unit's
      published rationale located where this script puts it, at its published score
  [3] the gaps the readings quote, recomputed from the cache's extracts (the United States and Singapore)
  [4] the flags
Sources not in this repository are named with their identifiers; every figure used from them is held below or in the
cache.

Usage: python3 rescoring_s61.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, the files of evidence_cache/C4.3/,
                                             the scoring documents holding the units' rationales, NEEC_Rescoring_s61.md;
                                             writes nothing)
       python3 rescoring_s61.py --tables   (prints the generated tables as JSON, for the record)
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

TAG, RECORD, CRIT = "(2.8)", "NEEC_Rescoring_s61.md", "C4.3"
CACHE = "evidence_cache/C4.3/"
UNITS = {}
GENERATED = {}


def U(code, verdict, c1, c2, flag=None, note="", zero=None):
    """One unit of C4.3. c1, c2: (status, estimate, source) for the two v2.0 clauses. flag: (alternative, reading).
    zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[c1, c2], flag=flag, note=note, zero=zero)


# ---- the cache (written by Session 61; md5s as written) ------------------------------------------------------------
MD5 = {"us_census_h05_extract.txt": "7d541a449432f94478b941d092e6cde7",
       "sg_ghs2025_table6_1.txt": "d709c07cf4beb297521e4711ae5bf1de",
       "integral_wp_v01_c43_extract.txt": "2292b6fb4f66ecaee14a1a70809a6df0"}
QUOTES = {
    "us_census_h05_extract.txt": ["xlsx md5 9086455a39eab2b36c90ed7c407f9819", "Black Alone (33)\t2025\t59980",
                                  "Asian Alone (34)\t2025\t126300", "White Alone, Not Hispanic (31)\t2025\t96710"],
    "sg_ghs2025_table6_1.txt": ["PDF md5 051185eeaf5e6fcc3247abb5418a8b45", "Malays                                                6,514             8,581           5.7           2.3"],
    "integral_wp_v01_c43_extract.txt": [
        "Equity is not enforced through redistribution",
        "no person or demographic group is structurally disadvantaged",
        "protected-category adjustments",
        "Social/fairness layer: accessibility impacts, protected-category considerations, distributional effects",
        "Post-decision access inequity detected.",
    ],
}
# the published rationales: (file, line of the C4.3 heading)
RAT = {"SQ": ("NEEC_Report_v1_6.md", 334), "MS": ("NEEC_Report_v1_6.md", 602), "LM": ("NEEC_Report_v1_6.md", 692),
       "SC": ("NEEC_Report_v1_6.md", 1052), "FALC": ("NEEC_Report_v1_6.md", 1142), "INT": ("NEEC_Report_v1_6.md", 1416),
       "GEO": ("NEEC_Report_v1_6.md", 1504), "MC": ("NEEC_Report_v1_6.md", 1594),
       "DE": ("NEEC_DoughnutEconomics_scoring_scratch.md", 530),
       "UBS": ("NEEC_UniversalBasicServices_scoring_scratch.md", 601),
       "SWF": ("NEEC_SovereignWealthFundStatism_scoring_scratch.md", 542),
       "CN": ("NEEC_StateCapitalism_China_scoring_scratch.md", 760),
       "SG": ("NEEC_StateCapitalism_Singapore_scoring_scratch.md", 685),
       "QA": ("NEEC_StateCapitalism_Qatar_scoring_scratch.md", 745),
       "IF": ("NEEC_IslamicFinance_scoring_scratch.md", 541), "OS": ("NEEC_Ostrom_Commons_scoring_scratch.md", 585)}


# ---- the gaps, computed from the cache (readings 3.3 and 3.4) --------------------------------------------------------
def us_series():
    path = os.path.join(HERE, CACHE, "us_census_h05_extract.txt")
    s = {}
    if not os.path.isfile(path):
        return s
    for line in open(path, encoding="utf-8").read().split("\n"):
        f = line.split("\t")
        if len(f) == 3 and f[1].split(" ")[0].isdigit() and f[2].isdigit():
            s.setdefault(f[0], {}).setdefault(int(f[1].split(" ")[0]), float(f[2]))   # the first listed: the later estimate
    return s


def gap(low, high):
    return 100.0 * (1.0 - low / high)


def rate(series):
    """Change between the three-year means 2018-2020 and 2023-2025, and the least-squares trend over the ten editions
    2016-2025 per five years (part (b8)'s reading 3.4)."""
    m1 = sum(series[y] for y in (2018, 2019, 2020)) / 3
    m2 = sum(series[y] for y in (2023, 2024, 2025)) / 3
    ys = list(range(2016, 2026))
    mx, my = sum(ys) / 10, sum(series[y] for y in ys) / 10
    slope = sum((y - mx) * (series[y] - my) for y in ys) / sum((y - mx) ** 2 for y in ys)
    return m1, m2, m2 - m1, 5 * slope


def us_figs():
    s = us_series()
    if not s:
        return {}
    b, a, w = s["Black Alone (33)"], s["Asian Alone (34)"], s["White Alone, Not Hispanic (31)"]
    b2, w2 = s["Black (32)"], s["White, Not Hispanic (32)"]
    ba = {y: gap(b[y], a[y]) for y in range(2002, 2026)}
    bw = {y: gap(b[y], w[y]) for y in range(2002, 2026)}
    long_ = {y: gap(b2[y], w2[y]) for y in b2 if y in w2 and y < 2002}
    long_.update(bw)
    return {"ba": ba, "bw": bw, "ba_rate": rate(ba), "bw_rate": rate(bw), "long": long_,
            "asian_top": all(a[y] > w[y] for y in range(2002, 2026))}


SG = {2020: {"Chinese": 9469, "Malays": 6514, "Indians": 9597}, 2025: {"Chinese": 12969, "Malays": 8581, "Indians": 13382}}
SG_PM = {2020: {"Chinese": 3164, "Malays": 1846, "Indians": 2867}, 2025: {"Chinese": 4523, "Malays": 2552, "Indians": 3968}}
QA_HIES = {"qatari": 72700, "non_qatari": 24400}   # QR a month, average household income, HIES 2012/13 (press reports)


def sg_figs():
    out = {}
    for name, t in (("hh", SG), ("pm", SG_PM)):
        for y, row in t.items():
            top = max(row, key=row.get)
            low = min(row, key=row.get)
            out[(name, y)] = (low, top, gap(row[low], row[top]))
    return out


F = us_figs()
G = sg_figs()


def f1(x):
    return f"{x:.1f}"


def sgn(x):
    return f"{x:+.1f}"


# ---- sources ---------------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
H5 = ("U.S. Census Bureau, CPS ASEC, Table H-5, median household income by race and Hispanic origin of householder, "
      "1967 to 2025 (xlsx md5 9086455a, retrieved 2026-10-15; " + CACHE + "us_census_h05_extract.txt)")
GHS = ("Department of Statistics Singapore, General Household Survey 2025 (June 2026), Table 6.1, median monthly "
       "household market income by ethnic group of the household reference person, resident households (" + CACHE +
       "sg_ghs2025_table6_1.txt)")
TTFS = ("Ministry of Education, parliamentary reply of 7 May 2026 on the Tertiary Tuition Fee Subsidy for Malays "
        "(introduced 1991, government-funded, administered by Yayasan MENDAKI, means-tested), retrieved 2026-10-15")
EO = ("Executive Order 14173 of 21 January 2025, revoking Executive Order 11246 (federal contractors' affirmative "
      "action); Students for Fair Admissions v. Harvard, 600 U.S. 181 (2023)")
QA_SRC = ("Planning and Statistics Authority, Household Income and Expenditure Survey 2012/13, as reported by The "
          "Peninsula (18 June 2014) and Doha News (average monthly household income, Qatari QR 72,700, non-Qatari QR "
          "24,400); psa.gov.qa did not answer the container, so the 2017/18 survey was not read")
WP = ("Joseph, INTEGRAL: Technical White Paper v0.1 (December 2025; PDF md5 a6defc9a), section 4.3, the contribution "
      "loop, and CDS's participant weights, Module 3's fairness layer and its review module (" + CACHE +
      "integral_wp_v01_c43_extract.txt)")
NOPROJ = ("no projection of the gap between groups' median household incomes on any axis, from a model or calibrated "
          "components, is stated or located, so neither the rate nor the convergence is shown (part (b8), reading 3.3)")
NOPROJ2 = "as for clause 1: no projection of the gap's path is stated or located (part (b8), reading 3.3)"
LAPSE = ("the published flag's 1.0 side lapses: 1.0 now needs a projection of the gap on each declared axis, which no "
         "source gives (reading 3.6)")

# ---- the units (readings in NEEC_Rescoring_s61.md, section 3) -------------------------------------------------------
if F:
    _ba, _bw = F["ba_rate"], F["bw_rate"]
    US1 = (f"on the race and Hispanic origin axis the entry's text declares, the least advantaged group is Black "
           f"households and the most advantaged Asian households, whose median exceeds the white non-Hispanic median in "
           f"every year 2002-2025; the gap is {f1(_ba[1])}% in 2023-2025 against {f1(_ba[0])}% in 2018-2020 "
           f"({sgn(_ba[2])}), trend {sgn(_ba[3])} per five years over the ten editions, and {f1(F['ba'][2025])}% in "
           f"2025 against {f1(F['ba'][2002])}% in 2002; the gap against white non-Hispanic households, the comparison "
           f"the entry's own text draws, is {f1(_bw[1])}% against {f1(_bw[0])}% ({sgn(_bw[2])}), trend {sgn(_bw[3])} "
           f"(reading 3.3)")
    US2 = (f"no trajectory toward 20%: the Black-white non-Hispanic gap has stayed between {f1(min(F['long'].values()))}% "
           f"and {f1(max(F['long'].values()))}% in all {len(F['long'])} editions since 1972 ({f1(F['long'][1972])}% in "
           f"1972, {f1(F['long'][2025])}% in 2025), and the Black-Asian gap widened by "
           f"{f1(F['ba'][2025] - F['ba'][2002])} points from 2002 to 2025; at the long-run rate the 20% level is not "
           f"reached within 30 years on either comparison (reading 3.3)")
else:
    US1 = US2 = "(the cache's extract is missing)"
_h20, _h25, _p20, _p25 = G[("hh", 2020)], G[("hh", 2025)], G[("pm", 2020)], G[("pm", 2025)]
SG1 = (f"on the ethnic axis the entry's text declares, Malay households have the lowest median household market income "
       f"and Indian households the highest: the gap is {f1(_h25[2])}% in 2025 against {f1(_h20[2])}% in 2020, "
       f"{sgn(_h25[2] - _h20[2])} points in five years; per household member, against Chinese households, the highest, "
       f"{f1(_p25[2])}% against {f1(_p20[2])}% ({sgn(_p25[2] - _p20[2])}); the gap widened, so clause 1 is short "
       f"(reading 3.4)")
SG2 = ("a gap that widened over the one five-year interval the survey gives is not on a trajectory toward 20%; the "
       "entry's own record has Malay per-member incomes growing fastest from 2010 to 2020 (census), so the decade "
       "before ran the other way, and two intervals with opposite signs establish no trajectory (reading 3.4)")

U("SQ", 0.0, ("S", US1, f"{H5}; {REP}SQ C4.3"), ("S", US2, f"{H5}; {EO}"),
  flag=("0.5: counting anti-discrimination law as a correction with partial reach, and the Hispanic gap against white "
        "non-Hispanic households, which narrows about 2 points in five years from 29% to 24%, as the axis on which the "
        "system shows some movement", "3.3"),
  zero="the best evidence shows performance far below the threshold with no credible pathway under the system's own "
       "logic (protocol 2.1): on the measure v2.0 names the gap between the least and most advantaged groups is above "
       "50% and wider than in 2002, the Black-white gap has not left the band of 35% to 45% in 53 years, and the "
       "system's group-directed remedies are being withdrawn (race-conscious admissions in 2023, federal contractors' "
       "affirmative action in 2025); the 0.0 band's own example",
  note="a correction (reading 3.3): the published 0.5 rests on 'some progress over decades', which the measure does not "
       "show; it resolves the inconsistency logged since Handoff 30, the 0.0 band's example published at 0.5")
U("MS", 0.5, ("U", "the cooperative structure's equity effects are mixed by the entry's own account (some cooperatives "
                   "prioritise equity, others replicate societal biases); pay compression within a firm bears on gaps "
                   "between groups but is not a projection of them; " + NOPROJ, f"{REP}MS C4.3"),
  ("U", NOPROJ2, f"{REP}MS C4.3"),
  note="0.5 holds: a genuine mechanism (democratic governance and pay compression) with unclear reach, the 0.5 band's "
       "second description (reading 3.2)")
U("LM", 0.0, ("U", "formal equality before the law only: the minimal state's functions exclude any corrective measure, "
                   "and no mechanism bears on a gap between groups; " + NOPROJ, f"{REP}LM C4.3"),
  ("U", NOPROJ2, f"{REP}LM C4.3"),
  zero="the system excludes the criterion's concern (protocol 2.1): its own logic confines the state to protecting "
       "rights and rules out any corrective flow, so historical disparities persist unchallenged, as its rationale says")
U("SC", 0.5, ("U", "diversity initiatives and hiring targets are group-directed but address representation, not "
                   "household income gaps, and the host economy's gaps are not credited to the mechanism (protocol "
                   "3.2); " + NOPROJ, f"{REP}SC C4.3"),
  ("U", NOPROJ2, f"{REP}SC C4.3"),
  flag=("0.0: the mechanism operates in the economy whose gap reading 3.3 finds far below the bar, and corporate "
        "diversity programmes have been withdrawn widely since 2024, so its correction may lack a credible pathway",
        "3.6"),
  note="0.5 holds: a group-directed mechanism of partial reach (reading 3.2); flagged now")
U("FALC", 0.5, ("U", "universal abundance narrows material gaps by its form, but governance and historical inequities "
                     "are unaddressed by the entry's account; " + NOPROJ, f"{REP}FALC C4.3"),
  ("U", NOPROJ2, f"{REP}FALC C4.3"),
  note="0.5 holds (reading 3.2)")
U("INT", 0.5, ("U", "the white paper, published after the corpus scored the design, adds what the review's document "
                    "lacked: the contribution system is checked so that 'no person or demographic group is "
                    "structurally disadvantaged', its rules carry 'protected-category adjustments', the deliberation "
                    "system's analysis has a fairness layer of distributional effects, and detected access inequity "
                    "amends a decision; but 'equity is not enforced through redistribution', no rule addresses a "
                    "historical disparity, and the design's income is non-monetary contribution credit; " + NOPROJ,
                    f"{WP}; {REP}INT C4.3"),
  ("U", NOPROJ2, f"{WP}"),
  note="read on the design's own white paper (v0.1, December 2025), as groups 2.6 and 2.7 read it; 0.5 holds, the "
       "band's example, now with a group-directed monitoring mechanism the published rationale did not have; read "
       "closely, since Integral's C4.3 could decide who is first (reading 3.7)")
U("GEO", 0.5, ("U", "the Citizen's Dividend is universal and flat, which narrows percentage gaps once, by its form; "
                    "land assessment carries a documented racial bias in current U.S. practice, which no Georgist "
                    "proposal located corrects; " + NOPROJ, f"{REP}GEO C4.3"),
  ("U", NOPROJ2, f"{REP}GEO C4.3"),
  flag=("0.0: weighting the documented assessment bias, which land-only valuation could amplify, as a mechanism that "
        "replicates disparity; " + LAPSE, "3.6"),
  note="0.5 holds (reading 3.2); the published flag's 0.0 side kept")
U("MC", 0.5, ("U", "time banking values care work, which bears on the gender axis, and Grassroots Economics reaches "
                   "low-income non-white communities, but a long-running UK scheme's membership was overwhelmingly white "
                   "in a diverse area; " + NOPROJ, f"{REP}MC C4.3"),
  ("U", NOPROJ2, f"{REP}MC C4.3"),
  flag=("0.0: weighting the documented participation gap as evidence that formally open schemes replicate exclusion; "
        + LAPSE, "3.6"),
  note="0.5 holds (reading 3.2); the published flag's 0.0 side kept")
U("DE", 0.5, ("U", "gender equality is one of the social foundation's twelve dimensions and unpaid care work is "
                   "engaged directly, which bears on the gender axis; no reparative mechanism for racial disparities is "
                   "located; " + NOPROJ, "NEEC_DoughnutEconomics_scoring_scratch.md, C4.3"),
  ("U", NOPROJ2, "NEEC_DoughnutEconomics_scoring_scratch.md, C4.3"),
  note="0.5 holds (reading 3.2)")
U("UBS", 0.5, ("U", "universal non-means-tested provision removes a documented channel of racially disparate stigma, "
                    "and Quebec's universal childcare raised mothers' employment, which bears on the gender axis; no "
                    "reparative mechanism and a documented rollout-equity concern in the closest precedent; " + NOPROJ,
                    "NEEC_UniversalBasicServices_scoring_scratch.md, C4.3"),
  ("U", NOPROJ2, "NEEC_UniversalBasicServices_scoring_scratch.md, C4.3"),
  note="0.5 holds (reading 3.2); the published flag, toward 1.0 only, lapses: 1.0 now needs a projection of the gap on "
       "each declared axis (reading 3.6)")
U("SWF", 0.5, ("U", "Alaska's dividend, flat per resident, reduces poverty proportionally more for rural Alaska Natives, "
                    "but the Native-non-Native poverty ratio, about 2.5, has not closed over the dividend's forty years, "
                    "and the host economy's gaps are not credited to the mechanism (protocol 3.2); " + NOPROJ,
                    "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.3"),
  ("U", NOPROJ2, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.3"),
  flag=("0.0: weighting the persistent gap and the documented adverse correlate over the disproportionate proportional "
        "benefit; " + LAPSE, "3.6"),
  note="0.5 holds (reading 3.2); the published flag's 0.0 side kept")
U("CN", 0.0, ("U", "no national household survey publishes median household income by ethnic group (the National Bureau "
                   "of Statistics publishes by urban and rural residence and by region), so no gap on the ethnic axis "
                   "can be measured, as for Centrally Planned Socialism (part (b8), reading 3.5) (reading 3.5)",
                   "NEEC_StateCapitalism_China_scoring_scratch.md, C4.3"),
  ("U", "no series exists from which a convergence on the ethnic axis could be projected; top-level gender "
        "representation has fallen since 2022 (reading 3.5)", "NEEC_StateCapitalism_China_scoring_scratch.md, C4.3"),
  flag=("0.5: weighting the preferential policies (examination bonus points, the one-child exemption) as a "
        "disproportionate-benefit mechanism; the published flag's 1.0 side, on the Centrally Planned Socialism "
        "precedent, lapses, since that unit fell to 0.5 in part (b8)", "3.5"),
  zero="the system excludes the criterion's concern for the minorities most affected (protocol 2.1): coercive state "
       "action targeting them, which the UN human rights office found may constitute crimes against humanity, and an "
       "assimilationist ethnic law of 2026, a harm beyond the formal neutrality of the 0.0 band",
  note="0.0 holds")
U("SG", 0.5, ("S", SG1, f"{GHS}; {TTFS}; NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.3"),
  ("S", SG2, f"{GHS}; NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.3"),
  flag=("0.0: on the measure the Malay gap widened from 2020 to 2025 while the system's transfers, though progressive, "
        "are not reparative; the 0.0 band read literally", "3.4"),
  note="0.5 holds: a group-directed, government-funded mechanism in force (the Tertiary Tuition Fee Subsidy for "
       "Malays, means-tested, since 1991), the 2025 Workplace Fairness Act, and a mixed record over 15 years (reading "
       "3.4); the published flag toward 0.0 kept, now on the measure")
U("QA", 0.0, ("U", f"the 2012/13 household survey reports average monthly household income of QR "
                   f"{QA_HIES['qatari']:,} for Qatari households and QR {QA_HIES['non_qatari']:,} for non-Qatari "
                   f"households, a gap of {f1(gap(QA_HIES['non_qatari'], QA_HIES['qatari']))}% on means, with workers in "
                   "collective housing outside the survey; one survey gives no rate (reading 3.5)",
                   f"{QA_SRC}; NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.3"),
  ("U", "no series is located from which a convergence on the citizenship axis could be projected (reading 3.5)",
   QA_SRC),
  zero="the system excludes the criterion's concern (protocol 2.1): rights and rent-funded benefits are allocated by "
       "nationality to the most advantaged legal group, the reverse of the flow the criterion asks for, and v2.0's scope "
       "counts the non-citizen residents, most of the population, whom the allocation excludes",
  note="0.0 holds")
U("IF", 0.5, ("U", "the contracts' terms are the same whoever signs, formal equality without a reparative mechanism; "
                   "the documented gaps are in participation (women's uptake of Islamic microfinance and wealth "
                   "management in Malaysia), not on the measure; the host economy's gaps are not credited to the "
                   "mechanism (protocol 3.2); " + NOPROJ, "NEEC_IslamicFinance_scoring_scratch.md, C4.3"),
  ("U", NOPROJ2, "NEEC_IslamicFinance_scoring_scratch.md, C4.3"),
  flag=("0.0: folding inheritance rules into the mechanism, or weighting the participation gap as evidence that formally "
        "neutral contracts replicate disparity", "3.6"),
  note="0.5 holds on the owner-confirmed scope (Session 22, D5) and the 0.5 band's 'formal equality without reparative "
       "mechanisms' (reading 3.2); the published flag kept; it alone could change the entry's tier")
U("OS", 0.5, ("U", "participatory exclusion of women, Indigenous and landless users is documented across settings, and "
                   "so are working remedies inside the mechanism (India's Joint Forest Management quotas) and collective "
                   "tenure for some 370 million Indigenous people; " + NOPROJ,
                   "NEEC_Ostrom_Commons_scoring_scratch.md, C4.3"),
  ("U", NOPROJ2, "NEEC_Ostrom_Commons_scoring_scratch.md, C4.3"),
  flag=("0.0: reading participatory exclusion as a structural property of bounded, locally governed institutions and "
        "the quotas as an external correction", "3.6"),
  note="0.5 holds (reading 3.2); the published flag kept")

EXPECT = {"rise": [], "fall": ["SQ"], "zero": ["SQ", "LM", "CN", "QA"], "ones": [],
          "flags": {"SQ": "3.3", "SC": "3.6", "GEO": "3.6", "MC": "3.6", "SWF": "3.6", "CN": "3.5", "SG": "3.4",
                    "IF": "3.6", "OS": "3.6"},
          "before": ["NSD", "CPS", "MMT", "UBI", "DG", "PE", "CCO"]}


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
    print(f"NEEC rescoring pass, stage 2, group 2.8: C4.3 Group Equity, class M ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{len(MD5)} files of {CACHE}, the scoring documents holding the units' rationales, {RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(sorted(set(p.part_of[(c, CRIT)] for c in before)))}) and are "
          "not re-read")
    d = p.v2[CRIT]["definition"]
    check(p.v2[CRIT]["revision"]["cls"] == "M" and len(d["clauses"]) == 2
          and d["clause_scope"] == "on each declared axis, non-citizen residents included"
          and "least and most advantaged groups" in d["measurement"],
          f"{CRIT} is class M with two clauses in v2.0, under the scope 'on each declared axis, non-citizen residents "
          "included', measured between the least and most advantaged groups")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group raises {len(rise)}, lowers {len(fall)} ({', '.join(fall)}) and holds {len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 for c in zeros)
          and [c for c in zeros if pub[c] == 0.0] == ["LM", "CN", "QA"],
          f"{len(zeros)} units are 0.0, each on a stated whole-criterion reason (protocol 2.1): the three published 0.0s "
          "hold (LM, CN, QA) and Status Quo falls to 0.0")
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    after1 = [c for c in p.order if (UNITS.get((c, CRIT)) or p.merged.get((c, CRIT)) or {}).get("verdict") == 1.0]
    check(ones == EXPECT["ones"] and not after1,
          f"no unit clears either clause, so none is 1.0; after this group no entry is at 1.0 on {CRIT}")
    st = [s for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"]]
    short = sorted({c for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"] if s == "S"})
    check(set(st) <= {"U", "S"} and short == ["SG", "SQ"],
          f"{st.count('S')} clauses short, on national household surveys ({', '.join(short)}); {st.count('U')} not shown")

    print(f"\n[2] THE CACHE ({CACHE}) AND THE PUBLISHED RATIONALES")
    for name, want in MD5.items():
        path = os.path.join(HERE, CACHE, name)
        raw = open(path, "rb").read() if os.path.isfile(path) else b""
        txt = raw.decode("utf-8")
        lost = [q for q in QUOTES.get(name, []) if q not in txt]
        check(hashlib.md5(raw).hexdigest() == want and not lost,
              f"{name}: md5 {want[:8]}, {len(QUOTES.get(name, []))} passage(s) quoted found", ", ".join(lost))
    bad = []
    for c in mine:
        f, n = RAT[c]
        lines = open(os.path.join(HERE, f), encoding="utf-8").read().split("\n")
        head = lines[n - 1].lstrip("# *")
        if not head.startswith(f"C4.3 Racial and Gender Equity: {f1(pub[c])}"):
            bad.append(c)
    check(sorted(RAT) == sorted(mine) and not bad,
          f"each of the {len(mine)} published rationales is at the line held here, headed with its published score",
          ", ".join(bad))

    print("\n[3] THE GAPS THE READINGS QUOTE (recomputed from the cache)")
    ba, bw = F["ba_rate"], F["bw_rate"]
    check(F["asian_top"] and F["ba"][2025] > 50 and F["ba"][2025] > F["ba"][2002] and ba[2] > -5 and ba[3] > -5,
          f"United States, Black against Asian households (least and most advantaged): {f1(F['ba'][2002])}% in 2002, "
          f"{f1(F['ba'][2025])}% in 2025; three-year means {sgn(ba[2])}, trend {sgn(ba[3])} per five years")
    check(bw[2] > -5 and bw[3] > -5 and 30 < min(F["long"].values()) and max(F["long"].values()) < 45
          and len(F["long"]) >= 50,
          f"United States, Black against white non-Hispanic: {f1(bw[0])}% to {f1(bw[1])}% ({sgn(bw[2])}), trend "
          f"{sgn(bw[3])}; between {f1(min(F['long'].values()))}% and {f1(max(F['long'].values()))}% in {len(F['long'])} "
          "editions since 1972")
    sq = UNITS[("SQ", CRIT)]["clauses"]
    check(f1(F["ba"][2025]) in sq[0][1] and f1(F["ba"][2002]) in sq[0][1] and f1(F["long"][1972]) in sq[1][1],
          "Status Quo's clauses quote the recomputed figures")
    gtxt = open(os.path.join(HERE, CACHE, "sg_ghs2025_table6_1.txt"), encoding="utf-8").read()
    rows_ok = all(f"{t[y][g]:,}" in gtxt for t in (SG, SG_PM) for y in t for g in t[y])
    check(rows_ok and _h20[0] == _h25[0] == "Malays" and _h20[1] == _h25[1] == "Indians" and _h25[2] > _h20[2]
          and _p25[2] > _p20[2] and f1(_h25[2]) in UNITS[("SG", CRIT)]["clauses"][0][1],
          f"Singapore: the twelve medians held are Table 6.1's; Malay against Indian households {f1(_h20[2])}% (2020) "
          f"to {f1(_h25[2])}% (2025); per member, against Chinese, {f1(_p20[2])}% to {f1(_p25[2])}%: both widen")
    qa = gap(QA_HIES["non_qatari"], QA_HIES["qatari"])
    check(qa > 20 and f1(qa) in UNITS[("QA", CRIT)]["clauses"][0][1],
          f"Qatar: the 2012/13 survey's means give a gap of {f1(qa)}% between non-Qatari and Qatari households")

    print("\n[4] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.7", "After group 2.8")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    rows_ = ["| Entry | Published | Rate | Convergence | Verdict | Flag |", "|---|---:|---|---|---:|---|"]
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
    print("\nRESCORING STAGE 2, GROUP 2.8, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.8: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
