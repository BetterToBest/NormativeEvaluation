#!/usr/bin/env python3
"""
blind_s74.py -- NEEC stage 3b, the blind re-read: C1.1 and C3.1 (ledger S57; decisions 69.1, 69.2)
====================================================================================================
Session 74, on Opus 5.5. Every unit a Sonnet 5.5 session read in Sessions 63 to 65 is re-read on Opus, blind to the
earlier reading, before the Report or Paper prose describes it (ledger D52, D53). This group re-reads C1.1 Poverty
Elimination Capacity, the 14 units part (2.11) read (Session 65), on v2.0's two clauses (">=90% poverty reduction
within 20 years under base scenario", ">=85% under stress testing"), and C3.1 Crisis Response Capacity, the 16 units
part (2.9) read (Session 63), on v2.0's three ("Response within 72 hours", "scaling 1:1 with crisis severity (30% GDP
decline = 30% benefit increase)", ">=90% population coverage"). It also reads Nordic Social Democracy's C1.1, which no
Sonnet session read, on the Nordic poverty finding (STATE.md, open item (d); ledger I7): an ordinary reading, outside
the comparison (EXTRA).

THE BLIND STEP. The readings below (NEW, EXTRA) were written from blind_review.blind_view() -- the v2.0 clause text
and the evidence_cache/C1.1/ and C3.1/ file names -- from the criteria's measurement text in criteria.json, and from
the sources this session cached (evidence_cache_s74.py) or names (evidence_cache/C1.1/sources_s74.md,
C3.1/sources_s74.md), and committed to the branch as a checkpoint before part (2.11)'s or part (2.9)'s readings of
these units, Session 63's record, or their published scores and rationales on C1.1 and C3.1, were opened, except as the
record discloses (NEEC_BlindReview_s74.md, section 2).

READINGS, C1.1 (the method each unit applies; the record states them in full)
  1.1.1 clause 1, >=90% reduction within 20 years: the Societal Poverty Line headcount (World Bank WDI SI.POV.SOPO, the
        Poverty and Inequality Platform, 2021 PPP), reduction = (rate at 2005 - rate at the latest survey) / rate at
        2005, 2005 being the start of the 20-year window ending at the stated date (2025); a configuration of several
        economies clears only if each does. A design or mechanism: the rate projected at the same line in the economy
        it is proposed for, from its own sources. The line rises with half the median, so a 90% reduction needs nearly
        everyone's income or consumption held above about half the median: cleared where the sources state or project
        a floor at or above the line reaching nine in ten of the poor; short where they project or document less, or
        where a design leaves the host's transfers unmodified and the host's record shows less; not shown where silent.
  1.1.2 clause 2, >=85% under stress: a configured economy's reduction holding at 85% or more through the window's
        shocks (2008-09, 2020), short wherever clause 1's reduction is itself below 85%; a design, a stress scenario its
        sources state, not shown where none.
  1.1.3 out of reach (D28(c)): a mechanism that does not govern household income or consumption even generalised;
        it holds the criterion at 0.5.
  1.1.4 0.0 (protocol 2.1): no structural mechanism addresses poverty (a framework that names the target and adopts
        no instrument), or the system's own sources refuse poverty relief as a public function; never with a clause
        cleared (D28(f)).
  1.1.5 the anchors' band texts describe v1's level readings ("94-96% poverty elimination"), which v2.0's measurement
        replaces with the change over the window; they do not govern (protocol 2.3(g)).

READINGS, C3.1
  3.1.1 clause 1, response within 72 hours: days from the first official data showing the shock to the first
        increased payment. A configured economy: its 2020 record (the measurement's most recent major shock; in the
        United States the first data are the initial claims released on 26 March 2020); cleared only where an
        automatic rule pays more within 72 hours, short where the first increased payment waited on a legislative or
        executive decision or on processing longer than 72 hours (the criterion's comparison text puts unemployment
        insurance at two to four weeks). A design: its rules, not shown where silent.
  3.1.2 clause 2, scaling 1:1: the percentage rise of social benefits to households (SNA D.62) against the percentage
        fall of real GDP in the shock year (2020 on 2019), cleared where the rise is at least the fall; every D.62
        benefit counts, legislated or automatic (clause 1 tests automaticity); not shown where no D.62 series is at
        hand or real GDP did not fall in the year. A design: its rules; a flat payment, or one that falls with the
        shock (a dividend from a tax base or fund earnings that fall), is short.
  3.1.3 clause 3, >=90% coverage: SDG 1.3.1 (ILO) at the latest year; a design or mechanism, the share of the
        population its own cash benefit reaches, a universal cash payment to every resident counting.
  3.1.4 out of reach (D28(c)): a mechanism that pays households no benefit even generalised; it holds at 0.5.
  3.1.5 0.0 (protocol 2.1; the anchor's band text describes the same case): a response that waits on political action
        with characteristic multi-month delay, or ideological opposition to stabilisation, or performance far below the
        threshold with no credible pathway under the system's own logic (coverage structurally withheld from most of
        the population), or a framework that adopts no instrument; never with a clause cleared.
  3.1.6 the anchors' band texts describe v1.4's threshold and do not govern (protocol 2.3(g)).

THE COMPARISON (written after the checkpoint, 8962db7). compare_group() sets each blind reading against the prior's --
part (2.11)'s for C1.1, part (2.9)'s for C3.1 -- agree only if every clause status and the verdict match; the extra
reading is set against part (b3)'s (Session 40). The record then reconciles each verdict difference (protocol 5.3,
under Session 71's rule: a blind verdict stands unless the prior shows evidence it did not weigh, or the blind reading
departs from its own stated reading). One moves to the prior's (RECONCILE), three stand, each already flagged toward
the prior's verdict; FINAL is what the generator session (ledger S61) applies, with EXTRA_FINAL, Nordic Social
Democracy's C1.1 (its clause 1 short, its flag toward 1.0 withdrawn; the verdict unchanged). No CCO-PTF-CIP-SZH unit is
in this group (decisions 57.2, 69.4).

Usage: python3 blind_s74.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, blind_s71.py, blind_s72.py,
                               blind_s73.py, the evidence_cache/C1.1/ and C3.1/ files, neec_corpus_v2_s65_snapshot.json,
                               neec_scores_v2_s65_snapshot.csv and NEEC_BlindReview_s74.md; writes nothing)
Prints file names and summaries only. Deterministic.
"""
import csv
import io
import json
import os
import sys
from contextlib import redirect_stdout

import blind_review as br
import pass_common as pc

HERE = os.path.dirname(os.path.abspath(__file__))
C11, C31 = "C1.1", "C3.1"
E1, E3 = "evidence_cache/C1.1/", "evidence_cache/C3.1/"
SPR = E1 + "wb_societal_poverty_rate.json"
SPL = E1 + "pip_societal_poverty_line.json"
WP = E1 + "integral_wp_v01_c11_extract.txt"
N1 = E1 + "sources_s74.md"
LPX = E3 + "lp_platform_c11_c31_extract.txt"
BEN = E3 + "fred_benefits_annual.csv"
BEN_M = E3 + "fred_benefits_monthly.csv"
CLAIMS = E3 + "fred_claims_weekly.csv"
GDP = E3 + "fred_realgdp_annual.csv"
CARES = E3 + "cares_act_wikipedia_lead.txt"
IMF = E3 + "imf_fiscal_db.txt"
SDG = {iso: E3 + f"sdg131_{m}.json" for iso, m in (("CHN", 156), ("NOR", 578), ("QAT", 634), ("SGP", 702),
                                                     ("USA", 840))}
N3 = E3 + "sources_s74.md"
# Session 62's and 63's method pages and index, listed by blind_view; read for the measures' definitions only.
OTHER3 = [E3 + f for f in ("eurostat_gov_esms.txt", "index.json", "un_sdg_131_metadata.txt", "un_sna2008.txt",
                           "wb_final_consumption.txt", "wb_sp_coverage.txt")]
READ = (SPR, SPL, WP, N1, LPX, BEN, BEN_M, CLAIMS, GDP, CARES, IMF, *SDG.values(), N3, *OTHER3)
NEW, EXTRA = {}, {}


def U(code, cid, verdict, clauses, flag=None, note="", zero=None, into=None):
    """One blind reading. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    (NEW if into is None else into)[(code, cid)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note,
                                                       zero=zero)


def path(name):
    return os.path.join(HERE, name)


def rows(name):
    return list(csv.DictReader(open(path(name), encoding="utf-8")))


def f1(x):
    return f"{x:.1f}"


# ---- figures, recomputed from the cache -------------------------------------------------------------------------
RATE = {k: {int(y): float(v) for y, v in d.items()} for k, d in json.load(open(path(SPR), encoding="utf-8")).items()}
LINE = {(r["country_code"], r["reporting_year"]): r for r in json.load(open(path(SPL), encoding="utf-8"))}


def latest(iso):
    return max(RATE[iso])


def reduction(iso, base=2005):
    """C1.1 clause 1 (reading 1.1.1): (rate at 2005 - rate at the latest survey) / rate at 2005, in %."""
    return 100 * (RATE[iso][base] - RATE[iso][latest(iso)]) / RATE[iso][base]


def red_str(iso):
    return (f"{f1(RATE[iso][2005])}% in 2005 to {f1(RATE[iso][latest(iso)])}% in {latest(iso)}, a reduction of "
            f"{f1(reduction(iso))}%")


BEN_A = {int(r["observation_date"][:4]): float(r["A063RC1A027NBEA"]) for r in rows(BEN)}
GDP_A = {int(r["observation_date"][:4]): float(r["GDPCA"]) for r in rows(GDP)}
US_BEN = 100 * (BEN_A[2020] / BEN_A[2019] - 1)
US_GDP = 100 * (GDP_A[2020] / GDP_A[2019] - 1)
CLAIMS_R = {r["observation_date"]: int(r["ICSA"]) for r in rows(CLAIMS)}


def sdg(iso):
    """SDG 1.3.1, both sexes: {year: value}."""
    out = {}

    def walk(x):
        if isinstance(x, dict):
            if "value" in x and "timePeriodStart" in x:
                if x.get("dimensions", {}).get("Sex") == "BOTHSEX":
                    out[int(float(x["timePeriodStart"]))] = float(x["value"])
            else:
                for v in x.values():
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(json.load(open(path(SDG[iso]), encoding="utf-8")))
    return out


COV = {iso: sdg(iso) for iso in SDG}


def cov(iso):
    y = max(COV[iso])
    return f"{COV[iso][y]:.1f}% ({y})"


NORDIC = ("DNK", "FIN", "NOR", "SWE")
FIG_PRINT = {
    "Societal Poverty Line headcount, 2005 -> latest, reduction % (USA, CHN, DNK, FIN, NOR, SWE)": "; ".join(
        f"{iso} {f1(RATE[iso][2005])} -> {f1(RATE[iso][latest(iso)])} ({latest(iso)}), {f1(reduction(iso))}"
        for iso in ("USA", "CHN") + NORDIC),
    "Societal Poverty Line, 2021 PPP $ a day, 2005 -> latest (USA, CHN, DNK, FIN, NOR, SWE)": "; ".join(
        f"{iso} {LINE[(iso, 2005)]['spl']:.2f} -> {LINE[(iso, latest(iso))]['spl']:.2f}"
        for iso in ("USA", "CHN") + NORDIC),
    "PIP surveys, Qatar and Singapore": f"QAT {sorted(RATE['QAT'].items())}; SGP {sorted(RATE['SGP'].items())}",
    "US social benefits (D.62), % 2019 -> 2020; real GDP, %": f"{f1(US_BEN)}; {f1(US_GDP)}",
    "US initial claims, weeks ending 14, 21 and 28 March 2020": ", ".join(
        str(CLAIMS_R[d]) for d in ("2020-03-14", "2020-03-21", "2020-03-28")),
    "SDG 1.3.1 coverage, latest (USA, CHN, SGP, QAT, NOR)": ", ".join(
        cov(i) for i in ("USA", "CHN", "SGP", "QAT", "NOR")),
}
PIPS = f"World Bank SI.POV.SOPO ({SPR}); PIP API ({SPL})"
US_LINE = LINE[("USA", latest("USA"))]["spl"]
US_LINE_Y = 365 * US_LINE


# =================================================================================================================
# C1.1 Poverty Elimination Capacity
# =================================================================================================================
# ---- configured economies ---------------------------------------------------------------------------------------
U("SQ", C11, 0.5,
  [("S", f"short: the United States' headcount at the Societal Poverty Line went from {red_str('USA')} -- no "
         f"reduction; the line rose with the median (${LINE[('USA', 2005)]['spl']:.2f} to ${US_LINE:.2f} a day, "
         f"2021 PPP) and the headcount stayed near a fifth throughout (reading 1.1.1)", PIPS),
   ("S", f"short: the base reduction is below 85%; the 2020-21 transfers cut the rate to {f1(RATE['USA'][2021])}% in "
         f"2021, and it returned to {f1(RATE['USA'][2022])}% in 2022 when they lapsed (reading 1.1.2)", PIPS)],
  flag=("0.0: reading twenty years without reduction, against a 90% bar, as performance far below the threshold with "
        "no credible pathway under the configuration's own logic (protocol 2.1), the temporary 2021 transfers "
        "having lapsed", "1.1.4"),
  note="0.5: transfer programmes are a real mechanism (they cut the rate in 2021), but the headcount did not fall")

U("CN", C11, 0.5,
  [("S", f"short: China's headcount at the Societal Poverty Line (consumption) went from {red_str('CHN')}, a real "
         f"reduction about half the bar's; the line itself rose from ${LINE[('CHN', 2005)]['spl']:.2f} to "
         f"${LINE[('CHN', 2022)]['spl']:.2f} a day as the median grew (reading 1.1.1)", PIPS),
   ("S", f"short: the base reduction is below 85%; the rate kept falling through 2020 ({f1(RATE['CHN'][2020])}%) "
         f"and rose in 2022 ({f1(RATE['CHN'][2021])}% to {f1(RATE['CHN'][2022])}%) (reading 1.1.2)", PIPS)],
  note="0.5: a large, documented reduction, about half the 90% bar")

U("SG", C11, 0.5,
  [("U", "not shown: the Poverty and Inequality Platform holds no Singapore survey and the state publishes no "
         "poverty line; the one academic estimate (Donaldson et al., 2013) is a single basic-needs level, not a "
         "change over the window (reading 1.1.1)", f"{SPR}; {N1}"),
   ("U", "not shown: no series, so no stress reading (reading 1.1.2)", f"{SPR}; {N1}")],
  note="0.5: genuine instruments (Workfare, ComCare, the CPF and its top-ups) with no measured reduction")

U("QA", C11, 0.5,
  [("U", f"not shown: the Platform holds one Qatar survey ({RATE['QAT'][2017]}% at the line in 2017), so no "
         f"reduction can be computed (reading 1.1.1)", f"{SPR}; {N1}"),
   ("U", "not shown: no series (reading 1.1.2)", f"{SPR}; {N1}")],
  flag=("0.0: reading a configuration whose distribution reaches citizens, about a tenth of residents, and leaves "
        "the migrant majority to a minimum wage, as one whose own logic excludes most of the population's poverty "
        "from its function (protocol 2.1)", "1.1.4"),
  note="0.5: the rentier state's transfers are a real mechanism for citizens; the migrant majority is outside them")

# ---- comprehensive systems (their own sources) -------------------------------------------------------------------
U("DE", C11, 0.0,
  [("U", "not shown: the social foundation's income dimension (no one below the poverty line) is a target, and "
         "'Design to Distribute' offers land, money creation, enterprise, knowledge and basic income as options, "
         "not as an adopted design; no rate is projected (reading 1.1.1)", N1),
   ("U", "not shown: no stress scenario (reading 1.1.2)", N1)],
  zero="protocol 2.1, first condition: no structural mechanism addresses poverty -- the framework names the target "
       "and adopts no instrument to meet it (reading 1.1.4)",
  flag=("0.5: reading the distributive designs Raworth names as a mechanism that addresses the criterion in "
        "principle", "1.1.4"),
  note="0.0: a target without an adopted mechanism")

U("INT", C11, 0.5,
  [("U", "not shown: the white paper states that access to essentials is 'structurally guaranteed' and that "
         "fair-access protocols keep essentials available 'regardless of individual capacity, disability, or "
         "temporary hardship', through the ITC's fairness signal, but sets no level and projects no rate; its "
         "access is in non-transferable time credits, which the Societal Poverty Line's income or consumption "
         "measure would read only through a projection the paper does not make (reading 1.1.1)", WP),
   ("U", "not shown: no stress scenario for access to essentials (reading 1.1.2)", WP)],
  note="0.5: a stated guarantee of essentials, unquantified")

U("LM", C11, 0.0,
  [("S", "short: the platform phases out government income security and holds that 'the proper and most effective "
         "source of help for the poor is the voluntary efforts of private groups and individuals'; no public floor "
         "exists to project (reading 1.1.1)", LPX),
   ("S", "short: private charity, the only mechanism, is itself procyclical under stress (reading 1.1.2)", LPX)],
  zero="protocol 2.1, second condition: the system's own sources refuse poverty relief as a public function and "
       "leave it to private charity (reading 1.1.4)",
  note="0.0: poverty relief refused as a public function")

U("SC", C11, 0.5,
  [("S", f"short: the reform changes corporate purpose and governance (living wages and fair taxes as aims) and "
         f"leaves the host's transfers unmodified; on its principal host's record the headcount went from "
         f"{red_str('USA')} (reading 1.1.1)", f"{PIPS}; {N1}"),
   ("S", "short: below 85% on the host's record (reading 1.1.2)", PIPS)],
  note="0.5: firm-level commitments in a host whose headcount has not fallen")

# ---- mechanisms (generalised, protocol 3.2) -------------------------------------------------------------------------
U("GEO", C11, 0.5,
  [("S", f"short: the citizen's dividend governs part of household income; distributing the whole of US land rent "
         f"(on the order of 5 to 10% of GDP, Larson 2015) would pay roughly $3,000 to $6,000 a person a year, "
         f"against a line of ${US_LINE:.2f} a day (${US_LINE_Y:,.0f} a year) that itself rises by half the "
         f"median's gain; a floor that low lifts part of the poor over the line, far from nine in ten (reading "
         f"1.1.1)", f"{SPL}; {N1}"),
   ("S", "short: land rent falls in a downturn, and the dividend with it (reading 1.1.2)", N1)],
  note="0.5: a universal cash dividend, too small to clear a line at half the median")

U("SWF", C11, 0.5,
  [("S", f"short: Alaska's dividend (about $1,000 to $3,300 a person a year) is a tenth to a quarter of a line of "
         f"${US_LINE_Y:,.0f} a year; Norway's variant funds the budget, and Norway's headcount at the line rose "
         f"from {red_str('NOR').split(', a reduction')[0]} with the fund at four times mainland GDP (reading "
         f"1.1.1)", f"{PIPS}; {N1}"),
   ("S", "short: below 85% on both variants (reading 1.1.2)", PIPS)],
  note="0.5: a real transfer channel, far short of a floor at the line")

U("UBS", C11, 0.5,
  [("U", "not shown: the services are in kind, and the Societal Poverty Line counts income or consumption; the "
         "proposal's sources value the services to a low-income household (the Institute for Global Prosperity, "
         "2017) but project no headcount at any line (reading 1.1.1)", N1),
   ("U", "not shown: no stress scenario (reading 1.1.2)", N1)],
  note="0.5: a genuine mechanism against deprivation, not projected on the criterion's measure")

U("MC", C11, 0.5,
  [("U", "not shown: mutual credit lets members with skills but no money trade through interest-free credit lines; "
         "the schemes' studies report gains to participants (the UK's LETS, the Bangla-Pesa) and no headcount at a "
         "national line, and a credit line transfers no income to those who cannot supply (reading 1.1.1)", N1),
   ("U", "not shown: no stress scenario (reading 1.1.2)", N1)],
  note="0.5: a genuine but small channel, unprojected")

U("OS", C11, 0.5,
  [("R", "out of reach: the mechanism governs the appropriation and provision rules of common-pool resources, not "
         "household income or consumption at large; generalised to every commons, wage and transfer incomes stay "
         "outside it (reading 1.1.3)", N1),
   ("R", "out of reach, as clause 1 (reading 1.1.3)", N1)],
  note="0.5 held: the mechanism governs neither clause's quantity (D28(c))")

U("IF", C11, 0.5,
  [("R", "out of reach: the profit-and-loss-sharing contract set allocates finance; zakat and the social-finance "
         "layer lie outside it (the extension test, D31: the Islamic finance precedent), so the mechanism governs no "
         "floor under household income (reading 1.1.3)", N1),
   ("R", "out of reach, as clause 1 (reading 1.1.3)", N1)],
  note="0.5 held: the mechanism governs neither clause's quantity (D28(c))")

# ---- Nordic Social Democracy (EXTRA: the Nordic finding; no Sonnet reading to compare) ------------------------------
U("NSD", C11, 0.5,
  [("S", "short: the headcount at the Societal Poverty Line rose in each of the four economies over the window -- "
         + "; ".join(f"{iso} {red_str(iso)}" for iso in NORDIC)
         + "; the lines rose with the medians (Sweden's from $" + f"{LINE[('SWE', 2005)]['spl']:.2f} to "
         f"${LINE[('SWE', 2023)]['spl']:.2f} a day), and the rates, among the world's lowest, did not fall (reading "
         f"1.1.1)", PIPS),
   ("S", f"short: below 85% in every economy; the rates rose after 2008 (Sweden {f1(RATE['SWE'][2008])}% to "
         f"{f1(RATE['SWE'][2012])}% by 2012) (reading 1.1.2)", PIPS)],
  note="0.5: rates held low, 6 to 12%, by a comprehensive welfare state, with no reduction over the window",
  into=EXTRA)


# =================================================================================================================
# C3.1 Crisis Response Capacity
# =================================================================================================================
US_C1 = ("short: the first official data showing the shock were the initial claims released on 26 March 2020 "
         f"({CLAIMS_R['2020-03-21']:,} for the week to 21 March, from {CLAIMS_R['2020-03-14']:,}); regular "
         "unemployment insurance pays after a claim is processed, two to four weeks on the criterion's own "
         "comparison, and the bulk of the increase came from the CARES Act, signed on 27 March, whose first "
         "payments were deposited from 10 April (reading 3.1.1)")
US_C2 = (f"cleared on the measure: social benefits to households (D.62) rose {f1(US_BEN)}% from 2019 to 2020 while "
         f"real GDP fell {f1(-US_GDP)}% (reading 3.1.2)")
US_C3 = f"short: {cov('USA')} of the population covered by at least one cash benefit (SDG 1.3.1) (reading 3.1.3)"
U("SQ", C31, 0.5,
  [("S", US_C1, f"{CLAIMS}; {CARES}; {N3}"),
   ("C", US_C2, f"{BEN}; {GDP}"),
   ("S", US_C3, SDG["USA"])],
  flag=("0.0: reading clause 2 on the automatic benefits alone, so that no clause is cleared and the response, "
        "legislated, is the anchor's 'traditional stimulus' (protocol 2.1)", "3.1.2"),
  note="0.5: automatic insurance and a fast legislated response, not automatic, coverage below 90%")

U("CN", C31, 0.5,
  [("S", "short: the 2020 measures were State Council decisions from February to May (unemployment insurance and "
         "temporary living allowances extended to uninsured and migrant workers, dibao widened), not an automatic "
         "trigger; weeks to months, not 72 hours (reading 3.1.1)", N3),
   ("U", "not shown: real GDP grew 2.2% in 2020 (after a 6.8% fall on the year in the first quarter), and no D.62 "
         "series for China is at hand (reading 3.1.2)", N3),
   ("S", f"short: {cov('CHN')} covered by at least one cash benefit, up from {COV['CHN'][2015]:.0f}% in 2015 "
         f"(reading 3.1.3)", SDG["CHN"])],
  note="0.5: real, discretionary capacity; coverage three quarters")

U("SG", C31, 0.5,
  [("S", "short: four Budgets in 2020, each passed by Parliament (Unity 18 February, Resilience 26 March, Solidarity "
         "6 April, Fortitude 26 May); the Solidarity Payment was credited from 14 April and the Jobs Support Scheme "
         "paid employers by schedule -- weeks, by decision (reading 3.1.1)", N3),
   ("U", "not shown: real GDP fell 3.9% in 2020; no D.62 series for Singapore is at hand, and most of the support "
         "was paid to employers as wage subsidies, which are not D.62 (reading 3.1.2)", N3),
   ("C", f"cleared: {cov('SGP')} covered by at least one cash benefit (SDG 1.3.1) (reading 3.1.3)", SDG["SGP"])],
  note="0.5: large, fast, decided responses drawn from reserves; not automatic")

U("QA", C31, 0.0,
  [("S", "short: the Emir's directive of 15 March 2020 put QR 75 billion behind the private sector (guarantees, "
         "deferrals, exemptions), not into payments to households; no automatic benefit rises (reading 3.1.1)", N3),
   ("U", "not shown: no D.62 series for Qatar is at hand (reading 3.1.2)", N3),
   ("S", f"far short: {cov('QAT')} covered by at least one cash benefit; the citizens' welfare state reaches about a "
         f"tenth of residents and the migrant majority has no cash benefit (reading 3.1.3)", SDG["QAT"])],
  zero="protocol 2.1, read by reading 3.1.5: performance far below the threshold with no credible pathway under the "
       "configuration's own logic -- coverage of 4%, withheld by design from the non-citizen majority, and a crisis "
       "response directed to firms",
  flag=("0.5: reading the decree's speed, the fiscal capacity and the Workers' Support and Insurance Fund's payments "
        "of unpaid wages as genuine, partial crisis-response capacity", "3.1.5"),
  note="0.0: coverage of 4% by the configuration's design")

CPS_C1 = ("short: no automatic stabiliser; the planned economy's response to a shock is a revision of the plan, a "
          "political and administrative decision, and its record in the major shocks is of months' delay or denial: "
          "grain exports continued and relief came late in the famines of 1932-33 and 1946-47 (Davies and "
          "Wheatcroft, 2004; Ellman, 2000) (reading 3.1.1)")
U("CPS", C31, 0.0,
  [("S", CPS_C1, N3),
   ("U", "not shown: no D.62 series or shock-year benefit record for the Soviet economy is at hand; full employment "
         "and fixed prices held nominal incomes, which is not a rise in benefits (reading 3.1.2)", N3),
   ("U", "not shown: SDG 1.3.1 is not measured for the Soviet years; social insurance covered workers, and collective "
         "farmers' pensions only from 1964 (reading 3.1.3)", N3)],
  zero="protocol 2.1, read by reading 3.1.5: the response waits on political decision with a record of months' "
       "delay, or denial, in the configuration's major shocks, and no clause is cleared",
  flag=("0.5: reading guaranteed employment and fixed prices as an implicit, system-wide stabiliser of household "
        "incomes", "3.1.5"),
  note="0.0: response by political decision, delayed or denied in the famines")

# ---- comprehensive systems (their own sources) -------------------------------------------------------------------
U("DE", C31, 0.0,
  [("U", "not shown: the framework states no rule for a shock (reading 3.1.1)", N3),
   ("U", "not shown: no benefit rule to scale (reading 3.1.2)", N3),
   ("U", "not shown: basic income is among its options, not adopted (reading 3.1.3)", N3)],
  zero="protocol 2.1, first condition: no structural mechanism addresses crisis response -- the framework adopts no "
       "stabilisation instrument (reading 3.1.5)",
  flag=("0.5: reading the options Raworth names (basic income among them) as a mechanism that addresses the "
        "criterion in principle", "3.1.5"),
  note="0.0: no stabilisation instrument adopted")

U("LM", C31, 0.0,
  [("S", "short: the platform opposes 'all forms of government subsidies and bailouts to business, labor, or any "
         "other special interest' and phases out public income security; no public payment rises (reading 3.1.1)",
    LPX),
   ("S", "short: no public benefit to scale (reading 3.1.2)", LPX),
   ("S", "short: public cash benefits phased out, so coverage falls toward none (reading 3.1.3)", LPX)],
  zero="protocol 2.1, second condition: ideological opposition to stabilisation -- markets left to self-correct, "
       "bailouts and public income security refused (reading 3.1.5)",
  note="0.0: opposed to stabilisation")

U("MS", C31, 0.5,
  [("U", "not shown: market socialism's sources (Roemer, 1994; Schweickart, 2011) state no automatic stabiliser; "
         "the state's control of investment could respond, by decision (reading 3.1.1)", N3),
   ("U", "not shown: no benefit rule to scale (reading 3.1.2)", N3),
   ("U", "not shown: the designs leave social insurance to the state without specifying it (reading 3.1.3)", N3)],
  note="0.5: firm-level resilience (cooperatives share hours before they cut jobs) and social investment control, "
       "no automatic system-level response")

U("FALC", C31, 0.5,
  [("U", "not shown: the design states no shock rule; its universal basic services continue regardless of "
         "employment, which steadies access but raises no payment (reading 3.1.1)", N3),
   ("U", "not shown: no cash benefit rule to scale (reading 3.1.2)", N3),
   ("U", "not shown: services universal, cash benefits unspecified (reading 3.1.3)", N3)],
  flag=("0.0: reading a design that states no crisis instrument as one with no structural mechanism addressing the "
        "criterion (protocol 2.1, first condition)", "3.1.5"),
  note="0.5: a universal service floor that holds in a downturn, without a crisis rule")

U("SC", C31, 0.5,
  [("S", f"short: the reform leaves the host's stabilisers unmodified; on its principal host's 2020 record, "
         f"{US_C1.split('short: ')[1]}", f"{CLAIMS}; {CARES}; {N3}"),
   ("C", f"cleared on the host's record: {US_C2.split('cleared on the measure: ')[1]}", f"{BEN}; {GDP}"),
   ("S", f"short: on the host's record, {US_C3.split('short: ')[1]}", SDG["USA"])],
  note="0.5: the host's stabilisers, unmodified")

# ---- mechanisms (generalised, protocol 3.2) -------------------------------------------------------------------------
U("GEO", C31, 0.5,
  [("S", "short: the citizen's dividend is paid on a schedule and does not rise in a shock (reading 3.1.1)", N3),
   ("S", "short: land rent and land values fall in a downturn, so a dividend paid from the tax falls with the shock "
         "rather than rising (reading 3.1.2)", N3),
   ("C", "cleared: the dividend is paid to every resident, a universal cash benefit (reading 3.1.3)", N3)],
  note="0.5: a universal floor that continues through a crisis but does not scale")

U("SWF", C31, 0.5,
  [("S", "short: Alaska's dividend is annual and set by formula; Norway's fund met 2020 through the Storting's "
         "revised budgets, drawing above the 3% path by decision, in weeks (reading 3.1.1)", N3),
   ("S", "short: the Alaska formula averages five years' realised earnings, so the dividend does not rise with a "
         "shock; Norway's draw scaled by decision, not by rule (reading 3.1.2)", N3),
   ("C", "cleared on the dividend variant: every resident of a year's standing receives it (reading 3.1.3)", N3)],
  note="0.5: a large buffer, released by decision; a universal dividend that does not scale")

U("UBS", C31, 0.5,
  [("R", "out of reach: the services are in kind and pay no benefit, so there is no increased payment to time "
         "(reading 3.1.4)", N3),
   ("R", "out of reach: no cash benefit to scale (reading 3.1.4)", N3),
   ("R", "out of reach: SDG 1.3.1 counts cash benefits, which the mechanism does not pay (reading 3.1.4)", N3)],
  note="0.5 held: services in kind that continue regardless of employment, outside the clauses' quantities")

U("MC", C31, 0.5,
  [("R", "out of reach: mutual credit extends credit lines among members and pays no benefit (reading 3.1.4)", N3),
   ("R", "out of reach: no benefit to scale; the WIR network's turnover rises in downturns (Stodder, 2009), a "
         "counter-cyclical credit channel, not D.62 (reading 3.1.4)", N3),
   ("R", "out of reach: no cash benefit (reading 3.1.4)", N3)],
  note="0.5 held: a documented counter-cyclical credit channel, outside the clauses' quantities")

U("OS", C31, 0.5,
  [("R", "out of reach: commons governance sets appropriation rules and pays no benefit (reading 3.1.4)", N3),
   ("R", "out of reach (reading 3.1.4)", N3),
   ("R", "out of reach (reading 3.1.4)", N3)],
  note="0.5 held: the mechanism governs none of the clauses' quantities (D28(c))")

U("IF", C31, 0.5,
  [("R", "out of reach: profit-and-loss sharing lightens borrowers' payments automatically when their profits "
         "fall, but pays households no benefit; zakat lies outside the contract set (D31) (reading 3.1.4)", N3),
   ("R", "out of reach (reading 3.1.4)", N3),
   ("R", "out of reach (reading 3.1.4)", N3)],
  note="0.5 held: firm-level loss sharing, outside the clauses' quantities")


# ---- the blind record ----------------------------------------------------------------------------------------------
def blind_table(p, cid, units=None):
    units = NEW if units is None else units
    rows_ = ["| Unit | Clause statuses | Verdict | Flag |", "|---|---|---|---|"]
    for (code, c) in sorted((k for k in units if k[1] == cid), key=lambda k: p.names[k[0]]):
        r = units[(code, c)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        rows_.append(f"| {p.names[code]} | {sts} | {pc.f1(r['verdict'])}{' (0.0 reason stated)' if r['zero'] else ''} "
                     f"| {flag} |")
    return "\n".join(rows_)


def blind_table_final(p, cid):
    rows_ = ["| Unit | Clause statuses | Final verdict | Flag | Against the prior |", "|---|---|---|---|---|"]
    prior = prior_units(p)
    for (code, c) in sorted((k for k in FINAL if k[1] == cid), key=lambda k: p.names[k[0]]):
        r, pr = FINAL[(code, c)], prior[(code, c)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        how = ("reconciled to the prior's" if (code, c) in RECONCILE else
               f"changes, {pc.f1(pr['verdict'])} to {pc.f1(r['verdict'])}" if pr["verdict"] != r["verdict"] else
               "the prior's verdict")
        rows_.append(f"| {p.names[code]} | {sts} | {pc.f1(r['verdict'])} | {flag} | {how} |")
    return "\n".join(rows_)


# ---- the reconciliation, after the comparison (protocol 5.3; written after the checkpoint, 8962db7) -------------
# One blind verdict changes on reconciliation, toward the prior's, with the blind verdict kept as the flag; the reason
# says what the blind reading did not weigh.
RECONCILE = {
    ("CPS", C31): dict(
        verdict=0.5, clauses=None,
        flag=("0.0: reading the configuration's response to its major shocks as one that waits on political decision "
              "with months' delay, or denial, as the famines of 1932-33 and 1946-47 record it (protocol 2.1), as the "
              "blind reading did", "3.1.5"),
        zero=None,
        note="0.5: a system-wide capacity to mobilise by decision without delay (1941), with relief to households "
             "delayed or denied in the famines; a mixed record",
        reason="the prior cites the command economy's rapid mobilisation in war and disaster (the Report's own "
               "account), which the blind reading did not weigh: in 1941 the evacuation of industry was decided within "
               "days of the invasion. Reading 3.1.5's 0.0 condition is a response that waits on political action with "
               "characteristic multi-month delay; a record in which decisions came within days in one major shock and "
               "relief was delayed or denied in others is mixed, not characteristic, so the 0.0 condition is not shown "
               "and the criterion is held at 0.5 (2.1's 'genuinely ambiguous' case), flagged toward 0.0"),
}
# Each standing difference's blind reading already carries the prior's verdict as its flag.
FLAGS = {}
# Why each standing difference stands (the record, section 6, states them in full).
STAND = {
    ("DE", C11): "the prior's 0.5 rests on the City Portrait diagnostic and the programmes cities chose after it "
                 "(Portland's 'From Excess to Access'), which the blind reading did not weigh; but those programmes are "
                 "the jurisdictions' own remedies, which D29(c) does not credit to a comprehensive system, and the "
                 "scoring document itself finds 'no committed provision mechanism', so the blind reading's premise "
                 "(a target without an adopted instrument) holds; Sessions 71 and 73 read the same framework so on "
                 "C4.5 and C4.4",
    ("DE", C31): "the prior's 0.5 rests on Amsterdam's adoption of the model as a recovery strategy in April 2020, which "
                 "it calls 'a response in policy framing and not a payment' and flags toward 0.0 on 2.1's first "
                 "condition; the adoption is the city's remedy (D29(c)), so the blind 0.0 stands, on the prior's own "
                 "flag",
    ("QA", C31): "the prior's 0.5 rests on the speed and size of the March 2020 decree, which the blind reading weighed "
                 "(its flag), and flags toward 0.0 on coverage of 4% by nationality; no evidence is unweighed and the "
                 "blind 0.0 stands, on the prior's own flag",
}


def final_units():
    out = {k: dict(v) for k, v in NEW.items()}
    for k, r in RECONCILE.items():
        u = out[k]
        u.update(verdict=r["verdict"], flag=r["flag"], zero=r["zero"], note=r["note"])
        if r["clauses"] is not None:
            u["clauses"] = list(r["clauses"])
    for k, fl in FLAGS.items():
        out[k]["flag"] = fl
    return out


FINAL = final_units()
EXTRA_FINAL = {k: dict(v) for k, v in EXTRA.items()}


def prior_units(p):
    return {k: v for cid in (C11, C31) for k, v in p.mods[p.tags.index(br.PRIOR[cid])].UNITS.items() if k[1] == cid}


def extra_prior(p):
    return {("NSD", C11): p.mods[p.tags.index("(b3)")].UNITS[("NSD", C11)]}


def comparison_table(p, prior, units, cid, label):
    pk = {k: v for k, v in prior.items() if k[1] == cid}
    uk = {k: v for k, v in units.items() if k[1] == cid}
    res, tally = br.compare_group(pk, uk)
    rows_ = [f"| Unit | Prior | {label} | Result | Differences |", "|---|---|---|---|---|"]
    for (code, c) in sorted(res, key=lambda k: p.names[k[0]]):
        agree, diffs = res[(code, c)]
        pr, nw = pk[(code, c)], uk[(code, c)]
        ps = " ".join(st for st, _, _ in pr["clauses"]) + " / " + pc.f1(pr["verdict"])
        ns = " ".join(st for st, _, _ in nw["clauses"]) + " / " + pc.f1(nw["verdict"])
        kind = "agree" if agree else ("revise (verdict)" if pr["verdict"] != nw["verdict"] else "revise (clauses)")
        rows_.append(f"| {p.names[code]} | {ps} | {ns} | {kind} | {'; '.join(diffs) if diffs else '—'} |")
    return "\n".join(rows_), res, tally


def earlier_changes(p):
    """Sessions 71's to 73's final verdict changes (blind_s71.FINAL to blind_s73.FINAL) against their priors."""
    import blind_s71 as b71
    import blind_s72 as b72
    import blind_s73 as b73
    out = {}
    for mod in (b71, b72, b73):
        pr = mod.prior_units(p)
        out.update({k: (pr[k]["verdict"], u["verdict"]) for k, u in mod.FINAL.items() if pr[k]["verdict"] != u["verdict"]})
    return out


def standings(changes):
    """Totals on the 29 criteria (neec_scores_v2_s65_snapshot.csv) and failures, with the verdict changes in `changes`
    ({(code, cid): (prior verdict, final verdict)}) applied on top; nothing is written."""
    v2 = {e["code"]: e for e in json.load(open(path("neec_corpus_v2_s65_snapshot.json"), encoding="utf-8"))["entries"]}
    rows29 = {r["system"]: r for r in csv.DictReader(open(path("neec_scores_v2_s65_snapshot.csv"), encoding="utf-8"))}
    out = {}
    for code, e in v2.items():
        r = rows29[e["display_name"]]
        t, f = float(r["total_score"]), int(r["failures"])
        for (c, _), (pv, nv) in changes.items():
            if c == code:
                t += nv - pv
                f += (nv == 0.0) - (pv == 0.0)
        out[code] = (t, f, r["adequacy_tier"])
    return v2, out


def consequence_table(p, prior, units):
    """This group's verdict changes, alone and on top of Sessions 71's to 73's final ones, on the 29."""
    mine = {k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items() if prior[k]["verdict"] != u["verdict"]}
    v2, alone = standings(mine)
    _, both = standings({**earlier_changes(p), **mine})
    held = all(v2[k[0]]["vector"][k[1]] == prior[k]["verdict"] for k in prior)
    base = standings({})[1]
    lines = ["| Entry | Total on 29 | After this group | After Sessions 71 to 74 | Failures | After all four | "
             "Tier after all four |", "|---|---:|---:|---:|---:|---:|---|"]
    for code in v2:
        if alone[code] != base[code] or both[code] != base[code]:
            lines.append(f"| {v2[code]['display_name']} | {base[code][0]:.1f} | {alone[code][0]:.1f} | "
                         f"{both[code][0]:.1f} | {base[code][1]} | {both[code][1]} | {pc.tier(both[code][1])} |")

    def first(st):
        top = max(t for t, _, _ in st.values())
        return " and ".join(sorted(v2[c]["display_name"] for c, (t, _, _) in st.items() if t == top)), top
    tiers = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in both.items() if pc.tier(f) != tr]
    tiers_alone = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in alone.items() if pc.tier(f) != tr]
    return "\n".join(lines), held, first(alone), first(both), tiers, tiers_alone, mine


def flag_effects(p, prior, units):
    """Each flagged final reading's alternative taken alone, on top of all four groups' final verdicts: total,
    failures, tier, and whether first place or the tier would change."""
    changes = earlier_changes(p)
    changes.update({k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items()
                    if prior[k]["verdict"] != u["verdict"]})
    _, base = standings(changes)
    lines = ["| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |",
             "|---|---|---:|---:|---:|---:|---|---|"]
    movers = []
    for (code, cid) in sorted((k for k in units if units[k]["flag"]), key=lambda k: (k[1], p.names[k[0]])):
        u = units[(code, cid)]
        alt = float(u["flag"][0][:3])
        t, f, _ = base[code]
        t2, f2_ = t + alt - u["verdict"], f + (alt == 0.0) - (u["verdict"] == 0.0)
        others = max(tt for c, (tt, _, _) in base.items() if c != code)
        changes_ = []
        if pc.tier(f2_) != pc.tier(f):
            changes_.append(f"tier: {pc.tier(f)} to {pc.tier(f2_)}")
        if (t >= others) != (t2 >= others) or (t == others) != (t2 == others):
            changes_.append("first place: " + ("shared" if t2 == others else "alone" if t2 > others else "lost"))
        if changes_:
            movers.append((code, cid))
        lines.append(f"| {p.names[code]} | {cid} | {pc.f1(u['verdict'])} | {alt:.1f} | {t2:.1f} | {f2_} | "
                     f"{pc.tier(f2_)} | {'; '.join(changes_) if changes_ else '—'} |")
    return "\n".join(lines), movers


def record_check(tables, ok_print):
    rec = os.path.join(HERE, "NEEC_BlindReview_s74.md")
    if not os.path.isfile(rec):
        return ok_print(False, "NEEC_BlindReview_s74.md exists", "missing")
    text = open(rec, encoding="utf-8").read()
    missing = [name for name, t in tables if t not in text]
    return ok_print(not missing, "NEEC_BlindReview_s74.md carries every generated table verbatim (" +
                    ", ".join(name for name, _ in tables) + ")", ", ".join(missing))


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s74.py -- the blind re-read of C1.1 and C3.1 (ledger S57; decisions 69.1, 69.2)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    print("inputs: blind_review.py, pass_common.py and its parts, " + ", ".join(sorted(READ)) + "\n")

    print("[1] the blind readings are complete and follow the rules")
    for cid, n in ((C11, 14), (C31, 16)):
        keys = {k for k in p.mods[p.tags.index(br.PRIOR[cid])].UNITS if k[1] == cid}
        mine = {k for k in NEW if k[1] == cid}
        ok_print(mine == keys and len(keys) == n, f"one blind reading for each of the {n} {cid} units of part "
                 f"{br.PRIOR[cid]}, no more", str(sorted(mine ^ keys)))
    ok_print(set(EXTRA) == {("NSD", C11)} and not set(EXTRA) & set(NEW),
             "the one extra reading (Nordic Social Democracy's C1.1) is outside the comparison set")
    both = {**NEW, **EXTRA}
    pc.check_records(p, both, ok_print)
    pc.check_rule(both, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in both.values()), "each flag names an alternative score other than the verdict")
    bad = [k for k in sorted(both) if len(br.blind_view(p, k)["clauses_v2"]) != len(both[k]["clauses"])]
    ok_print(not bad, "each reading has one status per clause blind_view shows", str(bad))
    for cid, ec in ((C11, E1), (C31, E3)):
        key = next(k for k in sorted(NEW) if k[1] == cid)
        listed = {ec + f for f in br.blind_view(p, key)["cache_files"]}
        ok_print(listed <= set(READ), f"every file blind_view lists for {cid} is one this script reads or names",
                 str(sorted(listed - set(READ))))
    ok_print(all(os.path.isfile(path(f)) for f in READ), "every file in READ exists")

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG_PRINT.items():
        print(f"    {k}: {v}")

    print("\n[3] the blind readings (verdicts, clause statuses, flags)")
    for cid in (C11, C31):
        print(f"\n{cid}:")
        print(blind_table(p, cid))
        v = [r["verdict"] for k, r in NEW.items() if k[1] == cid]
        print(f"\n{cid}: {v.count(1.0)} at 1.0, {v.count(0.5)} at 0.5, {v.count(0.0)} at 0.0; "
              f"{sum(1 for k, r in NEW.items() if k[1] == cid and r['flag'])} flagged")
    print("\nNordic Social Democracy, C1.1 (the Nordic finding; outside the comparison):")
    print(blind_table(p, C11, EXTRA))

    btables = [blind_table(p, C11), blind_table(p, C31), blind_table(p, C11, EXTRA)]

    print("\n[4] the comparison with parts (2.11) and (2.9) (compare_group on the readings as recorded at the "
          "checkpoint), and Nordic Social Democracy's C1.1 with part (b3)")
    prior = prior_units(p)
    cmp_tables, vd = [], []
    for cid in (C11, C31):
        t_cmp, res, tally = comparison_table(p, prior, NEW, cid, "Blind (Session 74)")
        cmp_tables.append(t_cmp)
        print(f"\n{cid}, against part {br.PRIOR[cid]}:")
        print(t_cmp)
        d = sorted((k for k in res if prior[k]["verdict"] != NEW[k]["verdict"]), key=lambda k: k[0])
        vd += d
        print(f"\n{cid}: {tally['agree']} agree, {tally['revise']} revise; {len(d)} verdicts differ: " + ", ".join(
            f"{p.names[k[0]]} {pc.f1(prior[k]['verdict'])} to {pc.f1(NEW[k]['verdict'])}" for k in d))
    xp = extra_prior(p)
    t_x, res_x, _ = comparison_table(p, xp, EXTRA, C11, "Session 74")
    cmp_tables.append(t_x)
    print("\nNordic Social Democracy, C1.1, against part (b3):")
    print(t_x)
    ok_print(all(xp[k]["verdict"] == EXTRA[k]["verdict"] for k in EXTRA),
             "Nordic Social Democracy's C1.1 verdict is unchanged by the Nordic finding (clause 1 revised only)")

    print("\n[5] the reconciliation (protocol 5.3) and the final readings")
    ok_print(set(RECONCILE) <= set(vd), "every reconciled unit is one whose blind verdict differs from the prior's")
    ok_print(all(FINAL[k]["verdict"] == prior[k]["verdict"] for k in RECONCILE),
             "each reconciliation moves the verdict to the prior's, and only there")
    stand = [k for k in vd if k not in RECONCILE]
    ok_print(set(STAND) == set(stand), "every standing verdict difference has its stated reason")
    ok_print(all(NEW[k]["flag"] and NEW[k]["flag"][0][:3] == pc.f1(prior[k]["verdict"]) for k in stand),
             "each standing difference's blind reading is flagged toward the prior's verdict")
    ok_print(all(FINAL[k]["flag"] and FINAL[k]["flag"][0][:3] == pc.f1(NEW[k]["verdict"]) for k in RECONCILE),
             "each reconciled unit keeps its blind verdict as its flag")
    pc.check_rule(FINAL, ok_print)
    print("standing verdict changes: " + ", ".join(
        f"{p.names[k[0]]} {k[1]} {pc.f1(prior[k]['verdict'])} to {pc.f1(FINAL[k]['verdict'])}" for k in stand))
    cco = [k for k in vd if k[0] == "CCO"]
    ok_print(not cco, "no CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4: a rise is applied, a fall held)",
             str(cco))
    mech = {c for c, e in ((e["code"], e) for e in json.load(open(path("neec_corpus_v2_s65_snapshot.json"), encoding="utf-8"))
                           ["entries"]) if e["scope_class"] == "mechanism"}
    zero_mech = sorted(f"{k[0]} {k[1]}" for k, u in {**prior, **FINAL}.items() if k[0] in mech and u["verdict"] == 0.0)
    ok_print(not zero_mech, "no mechanism is at 0.0 in this group on either reading (Session 73's observation: "
             "the class reading holds a mechanism that governs no clause's quantity at 0.5)", ", ".join(zero_mech))
    final_tables = [blind_table_final(p, cid) for cid in (C11, C31)]
    for cid, t in zip((C11, C31), final_tables):
        print(f"\nfinal readings, {cid}:")
        print(t)

    print("\n[6] consequences once applied (by generator in ledger S61, not here), alone and with Sessions 71 to 73")
    t_cons, held, (f1n, f1t), (f2n, f2t), tiers, tiers_alone, mine = consequence_table(p, prior, FINAL)
    ok_print(held, "neec_corpus_v2_s65_snapshot.json carries the prior's verdict for each of the 30 units (the published "
             "provisional scores are the prior's)")
    print(t_cons)
    print(f"\nfirst place on the 29 after this group alone: {f1n} at {f1t:.1f}; after Sessions 71 to 74: {f2n} at "
          f"{f2t:.1f}")
    print("tier changes, this group alone: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers_alone) or "none"))
    print("tier changes, after Sessions 71 to 74: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers) or "none"))
    t_flags, movers = flag_effects(p, prior, FINAL)
    print(f"\nthe final readings' {sum(1 for u in FINAL.values() if u['flag'])} flags, each taken alone (on all four "
          "groups' final verdicts):")
    print(t_flags)
    print("flags that would change a tier or first place: " + (", ".join(f"{p.names[c]} {cid}" for c, cid in movers)
                                                                or "none"))

    print("\n[7] the record")
    record_check([("blind readings, C1.1", btables[0]), ("blind readings, C3.1", btables[1]),
                  ("blind reading, Nordic Social Democracy", btables[2]),
                  ("comparison, C1.1", cmp_tables[0]), ("comparison, C3.1", cmp_tables[1]),
                  ("comparison, Nordic Social Democracy", cmp_tables[2]),
                  ("final readings, C1.1", final_tables[0]), ("final readings, C3.1", final_tables[1]),
                  ("consequences", t_cons), ("flag effects", t_flags)], ok_print)
    print("\nBLIND RE-READ OF C1.1 AND C3.1 CHECKED." if ok else "\nBLIND RE-READ: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
