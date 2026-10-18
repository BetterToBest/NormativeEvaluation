#!/usr/bin/env python3
"""
blind_s72.py -- NEEC stage 3b, the blind re-read: C4.1 (ledger S55; decisions 69.1, 69.2)
==========================================================================================
Session 72, on Opus 5.5. Every unit a Sonnet 5.5 session read in Sessions 63 to 65 is re-read on Opus, blind to the
earlier reading, before the Report or Paper prose describes it (ledger D52, D53). This group re-reads C4.1
Intergenerational Justice: the 15 units part (2.11) read, and the 8 designs part (b6) read on the pre-v2.0
four-clause list (decision 69.2, ledger D54), all 23 on v2.0's two clauses ("Debt-to-GDP <80%", "positive wealth
transfer to next generation").

THE BLIND STEP. The readings below (NEW) were written from blind_review.blind_view() -- the v2.0 clause text and the
evidence_cache/C4.1/ file names -- and from the sources this session cached (evidence_cache_s72.py) or names
(evidence_cache/C4.1/sources_s72.md), and committed to the branch as a checkpoint before part (2.11)'s or part
(b6)'s readings of these units, or their published (v1) scores and rationales on C4.1, were opened, except as the
record discloses (NEEC_BlindReview_s72.md, section 2).

READINGS (the method each unit applies; the record states them in full)
  4.1.1 clause 1, debt below 80% of GDP. A configured economy: general government gross debt (IMF World Economic
        Outlook, the cached datamapper vintage, to 2031), cleared if below 80% in every year of the ten to the stated
        date (2016 to 2025) and on the WEO's projection to 2031, short if above 80% at the stated date; a
        configuration of several economies clears only if each does (as Sessions 50 and 64 read the four Nordic
        economies).
        The historical configuration (Centrally Planned Socialism) is read on the late-Soviet record, its level and
        its path. A design: its projected debt path from its own sources -- cleared where they state a rule or a
        construction that keeps public borrowing below the bar, short where they reject the bound or keep a host
        economy's public finances unmodified (that economy's figure is then the design's, as part (2.11) and Session
        71 read Stakeholder Capitalism's exit), not shown where they are silent. A mechanism: out of reach (D28(c))
        unless it governs public borrowing itself.
  4.1.2 clause 2, positive wealth transfer: net national saving (gross national saving less consumption of fixed
        capital, % of GNI; World Bank WDI, to 2021) positive in every year of the latest ten years of the accounts
        (2012 to 2021), the United States carried to 2025 on BEA's net saving (2016 to 2025); the World Bank's adjusted
        net savings (less resource depletion and pollution damage) as the check for the resource economies, a sign
        disagreement to be flagged. A design: cleared where its sources state a rule that retains net surplus as
        capital, short where they state an end to net accumulation (a steady state, sufficiency in place of
        accumulation), not shown where silent. A mechanism: out of reach unless it accumulates or decumulates national
        wealth itself.
  4.1.3 0.0 (protocol 2.1, decision 53.2): far below on both clauses -- debt above the bar and net saving negative
        over the window -- with no rule or instrument that corrects either, or a system whose own logic rejects the
        criterion's concern on both clauses; never with a clause cleared. A mechanism that governs neither quantity
        holds at 0.5 (D28(c); the precedent of decision 64.5). On this reading no unit is 0.0: every configured economy
        saves positively over the window, and no design rejects both concerns.
  4.1.4 the ecological transfer is C4.2's (v2.0's requirement); the anchors' band texts on climate debt and resource
        depletion describe v1.4's threshold and do not govern (protocol 2.3(g)).

THE COMPARISON (written after the checkpoint, 4c8bc9f). compare_group() sets each blind reading against the prior's --
part (2.11)'s for its 15 units, part (b6)'s for the 8 designs, whose four pre-v2.0 clauses compare_unit reports as a
clause-count difference (decision 69.2) -- agree only if every clause status and the verdict match. The record then
reconciles each verdict difference (protocol 5.3, under Session 71's rule: a blind verdict stands unless the prior
shows evidence it did not weigh, or the blind reading departs from its own stated reading). Both differences here
stand (RECONCILE is empty), so FINAL is NEW with one flag added (FLAGS), and it is what the generator session (ledger S61) applies. A change to
CCO-PTF-CIP-SZH's units waits for the owner (decisions 57.2, 69.4); this group changes none of its verdicts.

Usage: python3 blind_s72.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, blind_s71.py, the evidence_cache/C4.1/
                               files, neec_corpus_v2.json, neec_scores_v2.csv and NEEC_BlindReview_s72.md; writes
                               nothing)
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
C41 = "C4.1"
EC = "evidence_cache/C4.1/"
DEBT = EC + "imf_weo_gross_debt_pct_gdp.json"
GNS = EC + "wb_gross_savings_pct_gni.json"
CFC = EC + "wb_consumption_fixed_capital_pct_gni.json"
BEA = EC + "fred_us_net_saving_gni.csv"
ANS = EC + "wb_adjusted_net_savings_pct_gni.json"
OFER = EC + "ofer_1990_extract.txt"
D400 = EC + "programme_400_days_1990_extract.txt"
LPX = EC + "lp_platform_extract.txt"
ATC = EC + "hahnel_wright_2016_c41_extract.txt"
WPX = EC + "integral_wp_v01_c41_extract.txt"
HUB = EC + "research_hub_8e8a6ba_c41_extract.txt"
NOTES = EC + "sources_s72.md"
READ = (DEBT, GNS, CFC, BEA, ANS, OFER, D400, LPX, ATC, WPX, HUB, NOTES)
NEW = {}


def U(code, verdict, clauses, flag=None, note="", zero=None):
    """One blind reading of C4.1. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    NEW[(code, C41)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note, zero=zero)


def path(name):
    return os.path.join(HERE, name)


def jload(name):
    return json.load(open(path(name), encoding="utf-8"))


# ---- figures, recomputed from the cache -------------------------------------------------------------------------
DEBT_D, GNS_D, CFC_D, ANS_D = jload(DEBT), jload(GNS), jload(CFC), jload(ANS)
WIN_DEBT = [str(y) for y in range(2016, 2026)]
WIN_NNS = [str(y) for y in range(2012, 2022)]


def debt(iso, year):
    return float(DEBT_D[iso][str(year)])


def debt_range(iso, years):
    v = [debt(iso, y) for y in years]
    return min(v), max(v)


def nns(iso, year):
    return float(GNS_D[iso][str(year)]) - float(CFC_D[iso][str(year)])


def nns_range(iso):
    v = [nns(iso, y) for y in WIN_NNS]
    return min(v), max(v)


def ans_range(iso):
    v = [float(ANS_D[iso][y]) for y in WIN_NNS]
    return min(v), max(v)


def bea():
    rows = list(csv.DictReader(open(path(BEA), encoding="utf-8")))
    return {r["year"]: 100 * float(r["W201RC1A027NBEA"]) / float(r["A023RC1A027NBEA"]) for r in rows}


def f1(x):
    return f"{x:.1f}"


US_NS = bea()
PROJ = [str(y) for y in range(2026, 2032)]
FIG = {}
for iso in ("USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE"):
    lo, hi = debt_range(iso, WIN_DEBT)
    plo, phi = debt_range(iso, PROJ)
    nlo, nhi = nns_range(iso)
    alo, ahi = ans_range(iso)
    FIG[iso] = dict(d25=f1(debt(iso, 2025)), dlo=f1(lo), dhi=f1(hi), d31=f1(debt(iso, 2031)), phi=f1(phi),
                    nlo=f1(nlo), nhi=f1(nhi), alo=f1(alo), ahi=f1(ahi))
F = FIG
US_LO = min(US_NS[str(y)] for y in range(2016, 2026))
US_NEG = [y for y in range(2000, 2026) if US_NS[str(y)] < 0]
FIN_CROSS = min(y for y in range(2016, 2026) if debt("FIN", y) >= 80)
QA_14, QA_20 = debt("QAT", 2014), debt("QAT", 2020)
CN_CROSS = min(y for y in range(2016, 2026) if debt("CHN", y) >= 80)
FIG_PRINT = {
    "US gross debt 2025 / range 2016-2025 / 2031 (WEO)": f"{F['USA']['d25']} / {F['USA']['dlo']}-{F['USA']['dhi']} / {F['USA']['d31']}",
    "US net national saving 2012-2021 (WDI), range": f"{F['USA']['nlo']}-{F['USA']['nhi']}",
    "US net saving 2016-2025 (BEA), lowest": f1(US_LO),
    "US years of negative net saving 2000-2025 (BEA)": ", ".join(str(y) for y in US_NEG),
    "China gross debt 2025 / first year above 80 / 2031": f"{F['CHN']['d25']} / {CN_CROSS} / {F['CHN']['d31']}",
    "China net national saving 2012-2021, range": f"{F['CHN']['nlo']}-{F['CHN']['nhi']}",
    "Singapore gross debt 2025 / range 2016-2025": f"{F['SGP']['d25']} / {F['SGP']['dlo']}-{F['SGP']['dhi']}",
    "Singapore net national saving 2012-2021, range": f"{F['SGP']['nlo']}-{F['SGP']['nhi']}",
    "Qatar gross debt 2025 / range 2016-2025 / highest 2026-2031": f"{F['QAT']['d25']} / {F['QAT']['dlo']}-{F['QAT']['dhi']} / {F['QAT']['phi']}",
    "Qatar gross debt 2014 and 2020": f"{f1(QA_14)} and {f1(QA_20)}",
    "Qatar net national saving / adjusted net savings 2012-2021, ranges": f"{F['QAT']['nlo']}-{F['QAT']['nhi']} / {F['QAT']['alo']}-{F['QAT']['ahi']}",
    "Finland gross debt 2025 / first year above 80 / 2031": f"{F['FIN']['d25']} / {FIN_CROSS} / {F['FIN']['d31']}",
    "Denmark, Norway, Sweden gross debt, highest 2016-2025": f"{F['DNK']['dhi']}, {F['NOR']['dhi']}, {F['SWE']['dhi']}",
    "Nordic net national saving 2012-2021, lowest (DNK, FIN, NOR, SWE)": f"{F['DNK']['nlo']}, {F['FIN']['nlo']}, {F['NOR']['nlo']}, {F['SWE']['nlo']}",
    "Norway adjusted net savings 2012-2021, range": f"{F['NOR']['alo']}-{F['NOR']['ahi']}",
}
WEO = f"IMF WEO, general government gross debt ({DEBT})"
WDI = f"World Bank WDI, gross national saving less consumption of fixed capital ({GNS}; {CFC})"

# ---- configured economies -----------------------------------------------------------------------------------------
U("SQ", 0.5,
  [("S", f"far short: general government gross debt is {F['USA']['d25']}% of GDP in 2025, between {F['USA']['dlo']}% "
         f"and {F['USA']['dhi']}% in every year from 2016, and {F['USA']['d31']}% on the WEO's projection to 2031; no "
         f"rule bounds it (reading 4.1.1)", WEO),
   ("C", f"cleared, narrowly: net national saving is positive in every year of 2012 to 2021 ({F['USA']['nlo']}% to "
         f"{F['USA']['nhi']}% of GNI) and, on BEA's net saving, of 2016 to 2025 (lowest {f1(US_LO)}%) (reading 4.1.2)",
    f"{WDI}; BEA net saving through FRED ({BEA})")],
  flag=("0.0: reading the window as the 20 years to the stated date, net saving is negative in "
        + ", ".join(str(y) for y in US_NEG) + ", so neither clause is shown, with debt far above the bar and rising "
        "and no rule or instrument that corrects it (protocol 2.1)", "4.1.2"),
  note="0.5: debt is far above the bar; the positive transfer is small but positive in every year of the window")

NSD_D = (f"Denmark {F['DNK']['d25']}%, Norway {F['NOR']['d25']}% and Sweden {F['SWE']['d25']}% of GDP in 2025, each "
         f"below 80% in every year from 2016 (highest {F['DNK']['dhi']}%, {F['NOR']['dhi']}%, {F['SWE']['dhi']}%); Finland "
         f"{F['FIN']['d25']}%, above 80% since {FIN_CROSS} and {F['FIN']['d31']}% on the WEO's projection to 2031")
U("NSD", 0.5,
  [("S", "short: " + NSD_D + "; the configuration clears only if each economy does (reading 4.1.1)", WEO),
   ("C", f"cleared: net national saving is positive in every year of 2012 to 2021 in all four (lowest "
         f"{F['DNK']['nlo']}%, {F['FIN']['nlo']}%, {F['NOR']['nlo']}% and {F['SWE']['nlo']}% of GNI, Denmark, Finland, "
         f"Norway, Sweden); Norway's adjusted net savings, net of oil and gas depletion, is {F['NOR']['alo']}% to "
         f"{F['NOR']['ahi']}% (reading 4.1.2)", f"{WDI}; World Bank adjusted net savings ({ANS})")],
  flag=("1.0: reading the configuration on its fiscal frameworks rather than on its weakest member: three of the four "
        "economies stand far below the bar and Finland crossed it only in " + str(FIN_CROSS), "4.1.1"),
  note="0.5: one of the four economies is above the bar at the stated date and projected to rise")

U("CPS", 0.5,
  [("S", "short, on the path: the rouble state debt the USSR Ministry of Finance reported was to reach 470 billion "
         "roubles by the end of 1990, 74% of 1989's net material product and about half of the 930 billion roubles of "
         "GDP Ofer gives for 1989, so the level was below the bar; but the budget deficit, 2.3% of GDP in 1981-85, was "
         "13.3% in the original plan for 1989 and 10.1% in the revised one, and a debt growing by a tenth of GDP a "
         "year is not kept below the bar by any rule of the configuration (reading 4.1.1)", f"{D400}; Ofer (1990), table 1 ({OFER})"),
   ("C", "cleared: investment rose from 22% of GNP in 1960 to 33% in 1987 and the capital stock grew faster than "
         "output under extensive growth, so net accumulation was positive throughout; Ofer counts the backlog of "
         "infrastructure, technology and services and the obsolete equipment never retired as an internal debt in "
         "real terms, which the measure's depreciation does not see (reading 4.1.2)", OFER)],
  flag=("1.0: reading the clause on the level at each documented date, below the bar to the end of 1990, rather than "
        "on the path", "4.1.1"),
  note="0.5: positive net accumulation, a debt below the bar in level but on a path through it")

U("CN", 0.5,
  [("S", f"short: general government gross debt is {F['CHN']['d25']}% of GDP in 2025, above 80% since {CN_CROSS}, and "
         f"{F['CHN']['d31']}% on the WEO's projection to 2031 (reading 4.1.1)", WEO),
   ("C", f"cleared: net national saving is positive in every year of 2012 to 2021, {F['CHN']['nlo']}% to "
         f"{F['CHN']['nhi']}% of GNI (reading 4.1.2)", WDI)],
  note="0.5: a large positive transfer through saving; debt above the bar and rising")

U("SG", 0.5,
  [("S", f"short: general government gross debt is {F['SGP']['d25']}% of GDP in 2025 and between {F['SGP']['dlo']}% and "
         f"{F['SGP']['dhi']}% in every year from 2016; the securities are issued to develop the debt market and their "
         f"proceeds invested, and the government's assets exceed its debt, but v2.0's measure is gross debt and governs "
         f"(reading 4.1.1)", f"{WEO}; {NOTES}"),
   ("C", f"cleared: net national saving is positive in every year of 2012 to 2021, {F['SGP']['nlo']}% to "
         f"{F['SGP']['nhi']}% of GNI (reading 4.1.2)", WDI)],
  note="0.5: the gross measure is above the bar; the transfer through saving is among the largest in the corpus")

U("QA", 1.0,
  [("C", f"cleared: general government gross debt is {F['QAT']['d25']}% of GDP in 2025, between {F['QAT']['dlo']}% and "
         f"{F['QAT']['dhi']}% in every year from 2016, and at most {F['QAT']['phi']}% on the WEO's projection to 2031 "
         f"(reading 4.1.1)", WEO),
   ("C", f"cleared: net national saving is positive in every year of 2012 to 2021, {F['QAT']['nlo']}% to "
         f"{F['QAT']['nhi']}% of GNI, and stays positive net of gas and oil depletion (adjusted net savings "
         f"{F['QAT']['alo']}% to {F['QAT']['ahi']}%), so the check finds no sign disagreement (reading 4.1.2)",
    f"{WDI}; World Bank adjusted net savings ({ANS})")],
  flag=(f"0.5: reading 'robustly' against the debt's path: with no fiscal rule, debt rose from {f1(QA_14)}% of GDP in "
        f"2014 to {f1(QA_20)}% in 2020 as gas prices fell, so the bar held under that stress by about seven points and "
        "on the hydrocarbon price, not on a rule of the configuration", "4.1.1"),
  note="1.0: both clauses are shown on the measures v2.0 names, net of resource depletion as well")

# ---- comprehensive systems ----------------------------------------------------------------------------------------
U("MS", 0.5,
  [("U", "not shown: the design's sources (worker cooperatives in competitive markets, Mondragon and the cooperative "
         "movements) state no public-finance rule or projected debt path (reading 4.1.1)",
    f"Report v1.6, MS overview; {NOTES}"),
   ("C", "cleared, by rule: the cooperatives retain their net surplus as capital -- at least 20% to an indivisible "
         "collective reserve and the rest, after the social fund, to members' capital accounts that stay invested "
         "until the member leaves (Mondragon), at least 30% to an indivisible legal reserve (Italian Civil Code, art. "
         "2545-quater) -- so the productive sector's net saving is positive whenever it earns a surplus (reading "
         "4.1.2)", NOTES)],
  note="0.5: a structural retention rule for the transfer; nothing on public debt")

U("LM", 0.5,
  [("C", "cleared, by stated rule: 'Government should not incur debt, which burdens future generations without their "
         "consent', with a balanced-budget amendment balanced by cutting expenditure, in a state confined to "
         "protecting rights (reading 4.1.1)", f"Libertarian Party platform ({LPX}); Report v1.6, LM overview"),
   ("U", "not shown: the design replaces defined-benefit with defined-contribution pensions 'so as not to impose debt "
         "on future generations', a funded saving channel, but states no projection of net national saving (reading "
         "4.1.2)", LPX)],
  note="0.5: a stated no-debt rule; the saving clause is not projected")

U("MMT", 0.5,
  [("S", "short: functional finance sets the deficit by employment and inflation, not by a debt ratio, and the "
         "framework's own account holds the debt's burden on the next generation to be a myth (Kelton, 2020, the "
         "third of six); the job guarantee is financed by the currency issuer's spending, so no rule bounds the ratio "
         "(reading 4.1.1)", f"Report v1.6, MMT overview; {NOTES}"),
   ("U", "not shown: the sectoral balances let public deficits meet private saving desires; no projection of net "
         "national saving is stated (reading 4.1.2)", NOTES)],
  flag=("0.0: reading the framework as excluding the criterion's fiscal concern as illegitimate (protocol 2.1), "
        "which its own account states for clause 1", "4.1.3"),
  note="0.5: clause 1 rejected by the framework's logic, clause 2 not addressed; 4.1.3 asks both for 0.0")

U("DG", 0.5,
  [("U", "not shown: the degrowth literature argues against growth that is driven by debt and for audits of "
         "illegitimate debt, but states no projected path of the public debt ratio (reading 4.1.1)",
    f"Report v1.6, DG overview; {NOTES}"),
   ("S", "short, by the design's logic: the transition its literature describes ends in a steady state, constant "
         "stocks of people and artifacts maintained by a low throughput (Daly, 1991; Kerschner, 2010), in which "
         "net accumulation is zero rather than positive; preservation of the natural stock is C4.2's (readings "
         "4.1.2, 4.1.4)", NOTES)],
  note="0.5: preservation, not a positive transfer, on the measure v2.0 names; nothing on the debt path")

SQH = (f"the entry keeps the host market economy's public finances unmodified and adds voluntary stakeholder "
       f"governance and ESG metrics: in the economy it reforms gross debt is {F['USA']['d25']}% of GDP in 2025, "
       f"{F['USA']['d31']}% on the WEO's projection to 2031")
U("SC", 0.5,
  [("S", "far short: " + SQH + " (reading 4.1.1)", f"Report v1.6, SC overview; {WEO}"),
   ("C", f"cleared, narrowly, on the host's figures: net saving is positive in every year of 2016 to 2025 (lowest "
         f"{f1(US_LO)}% of GNI, BEA); the reform adds no saving rule (reading 4.1.2)", f"{BEA}; {WDI}")],
  flag=("0.0: the host economy's alternative reading (Status Quo's flag, 4.1.2), which this unit tracks", "4.1.2"),
  note="0.5: the host's readings, which the reform does not change")

U("FALC", 0.5,
  [("U", "not shown: the design's sources call for public investment in energy and automation and an end to "
         "austerity, but state no projected path of the public debt ratio (reading 4.1.1)",
    f"Report v1.6, FALC overview; {NOTES}"),
   ("U", "not shown: the investment programme is stated, net national saving is not projected (reading 4.1.2)", NOTES)],
  note="0.5: genuine investment aims, neither clause projected")

U("PE", 0.5,
  [("U", "not shown: there is no state borrowing in the market sense, but neighbourhood consumption councils "
         "authorise households' borrowing and saving, and consumers, councils and federations carry the year's "
         "differences as debt or savings; no rule bounds the federations' debts and no path is projected (reading "
         "4.1.1)", ATC),
   ("U", "not shown: each year's plan runs inside an investment plan that sets the capacity added to each industry, "
         "but the design states no net accumulation rule or projection (reading 4.1.2)", ATC)],
  note="0.5: the planning procedure carries both quantities; neither is bounded or projected")

U("CCO", 0.5,
  [("S", "far short, on the host's figures: Basic Units are pegged 1:1 to the primary currency and the deployment is "
         "self-funding through a 12% conversion tax at 60-65% participation, so the design adds no public debt, but "
         "it keeps the host's public finances and their debt, " + F["USA"]["d25"] + "% of GDP in 2025 in the economy "
         "it is proposed for (reading 4.1.1)", f"{HUB}; {WEO}"),
   ("C", f"cleared: Public Trust Housing and Foundations hold property in public trust and build Acre Equity, a "
         f"collective stock carried forward, on top of the host's positive net saving (lowest {f1(US_LO)}% of GNI, "
         f"2016 to 2025) (reading 4.1.2)", f"{HUB}; {BEA}")],
  note="0.5: a structural collective holding for the transfer; the host's debt is unchanged")

U("INT", 0.5,
  [("C", "cleared, by construction: the design has no instrument of borrowing -- time credits are non-transferable, "
         "decay over time and are extinguished on use, so nothing can be lent or owed -- and no public debt arises "
         "within it (reading 4.1.1)", WPX),
   ("S", "short, by the design's logic: success is measured 'rather than growth or capital accumulation', and "
         "'prosperity is defined by sufficiency and reliability, not surplus accumulation'; the design sustains its "
         "material cycles but states no net accumulation (reading 4.1.2)", WPX)],
  note="0.5: no debt by construction; sufficiency in place of a positive transfer")

DE_SRC = f"Raworth (2017) ({NOTES})"
U("DE", 0.5,
  [("U", "not shown: the design is agnostic about growth and proposes redesigning money and finance, but states no "
         "projected path of the public debt ratio (reading 4.1.1)", DE_SRC),
   ("U", "not shown: regenerative design concerns the natural stock, which is C4.2's; no net national saving is "
         "projected (readings 4.1.2, 4.1.4)", DE_SRC)],
  note="0.5: a design framework with neither quantity stated")

# ---- mechanisms (generalised, protocol 3.2) -------------------------------------------------------------------------
R1 = "out of reach: the mechanism governs no public borrowing, so the debt ratio is the host economy's (reading 4.1.1)"
U("GEO", 0.5,
  [("R", R1 + "; the dividend is paid only from revenue left after public goods, which bounds the dividend, not the "
              "debt", "NEEC_Georgism_LVT_scoring_scratch.md, overview"),
   ("R", "out of reach: the tax captures land rent and the dividend distributes it rather than investing it (the "
         "scoring document's own contrast with a held corpus); national saving is the host's (reading 4.1.2)",
    "NEEC_Georgism_LVT_scoring_scratch.md, overview")],
  note="0.5: a fiscal mechanism that governs neither quantity (D28(c))")

U("MC", 0.5,
  [("R", R1, "NEEC_MutualCredit_LETS_scoring_scratch.md, overview"),
   ("R", "out of reach: balances sum to exactly zero by construction, so the mechanism creates no net financial "
         "saving and does not govern real saving (reading 4.1.2)", "NEEC_MutualCredit_LETS_scoring_scratch.md, overview")],
  note="0.5: a clearing mechanism that governs neither quantity (D28(c))")

U("IF", 0.5,
  [("R", R1 + "; sovereign sukuk are market practice outside the profit-sharing contract set the scoring document "
              "scores", "NEEC_IslamicFinance_scoring_scratch.md, overview"),
   ("R", "out of reach: profit-sharing accounts are an accumulating household corpus, a channel for saving, not a "
         "rule that raises net national saving (reading 4.1.2)", "NEEC_IslamicFinance_scoring_scratch.md, overview")],
  note="0.5: a financing mechanism that governs neither quantity (D28(c))")

U("UBI", 0.5,
  [("R", R1 + "; the funding (income taxation in the leading design, other variants not fixed by the mechanism) is "
              "a choice the transfer does not make", f"Report v1.6, UBI overview; {NOTES}"),
   ("R", "out of reach: an income transfer, which governs neither saving nor investment (reading 4.1.2)",
    "Report v1.6, UBI overview")],
  note="0.5: a transfer mechanism that governs neither quantity (D28(c))")

U("UBS", 0.5,
  [("R", R1 + "; the services are costed at about 2.3% of GDP and funded from taxation, so they add no debt by "
              "design", NOTES),
   ("R", "out of reach: service provision governs neither national saving nor investment beyond its own stock "
         "(reading 4.1.2)", NOTES)],
  note="0.5: a tax-funded provision mechanism that governs neither quantity (D28(c))")

U("SWF", 0.5,
  [("R", R1 + "; the withdrawal rule governs what the fund pays into the budget, not the rest of the government's "
              "borrowing (Norway's gross debt, " + F["NOR"]["d25"] + "% of GDP in 2025, is the host's)",
    f"NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview; {WEO}"),
   ("S", "short: the mechanism converts a non-recurring revenue into a held fund, a positive transfer while "
         "withdrawals stay within the return, as under Norway's rule; Timor-Leste withdrew above its Estimated "
         "Sustainable Income in 2008-12 and every year from 2014, and the IMF (2017) projects the fund's depletion, so "
         "the transfer rests on the rule's observance, not on the mechanism (reading 4.1.2)",
    f"NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview; {NOTES}")],
  note="0.5: a positive transfer where the rule holds, a drawdown where it does not")

U("OS", 0.5,
  [("R", R1, "NEEC_Ostrom_Commons_scoring_scratch.md, overview"),
   ("R", "out of reach: sustained yield preserves a local resource stock, which is the ecological transfer (C4.2's), "
         "not national saving (readings 4.1.2, 4.1.4)", "NEEC_Ostrom_Commons_scoring_scratch.md, overview")],
  note="0.5: a local governance mechanism that governs neither quantity (D28(c))")


# ---- the blind record ----------------------------------------------------------------------------------------------
def blind_table(p):
    rows = ["| Unit | Clause statuses | Verdict | Flag |", "|---|---|---|---|"]
    for (code, cid) in sorted(NEW, key=lambda k: p.names[k[0]]):
        r = NEW[(code, cid)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        rows.append(f"| {p.names[code]} | {sts} | {pc.f1(r['verdict'])}{' (0.0 reason stated)' if r['zero'] else ''} "
                    f"| {flag} |")
    return "\n".join(rows)


# ---- the comparison (written after the checkpoint) ------------------------------------------------------------------
PRIOR_TAGS = ("(2.11)", "(b6)")
RECONCILE = {}   # both verdict differences stand (NEEC_BlindReview_s72.md, section 6)
# A standing blind verdict keeps the prior's verdict as its flag where it has none (section 6, as Session 71 did).
FLAGS = {("LM", C41): ("0.0: reading the design as the Report specifies it, a minimal state with no fiscal rule, so that "
                       "no structural mechanism addresses debt or saving (protocol 2.1, first condition), the "
                       "prior's reading; the platform's rule is a party programme's, not the design's founding "
                       "literature's", "4.1.3")}
FINAL = {k: dict(v, flag=FLAGS.get(k, v["flag"])) for k, v in NEW.items()}


def prior_units(p):
    out = {}
    for t in PRIOR_TAGS:
        out.update({k: v for k, v in p.mods[p.tags.index(t)].UNITS.items() if k[1] == C41})
    return out


def prior_tag(p, key):
    return next(t for t in PRIOR_TAGS if key in p.mods[p.tags.index(t)].UNITS)


def comparison_table(p, prior, units, label):
    res, tally = br.compare_group(prior, units)
    rows = [f"| Unit | Prior part | Prior | {label} | Result | Differences |", "|---|---|---|---|---|---|"]
    for (code, cid) in sorted(res, key=lambda k: p.names[k[0]]):
        agree, diffs = res[(code, cid)]
        pr, nw = prior[(code, cid)], units[(code, cid)]
        ps = " ".join(st for st, _, _ in pr["clauses"]) + " / " + pc.f1(pr["verdict"])
        ns = " ".join(st for st, _, _ in nw["clauses"]) + " / " + pc.f1(nw["verdict"])
        kind = "agree" if agree else ("revise (verdict)" if pr["verdict"] != nw["verdict"] else "revise (clauses)")
        rows.append(f"| {p.names[code]} | {prior_tag(p, (code, cid))} | {ps} | {ns} | {kind} | "
                    f"{'; '.join(diffs) if diffs else '—'} |")
    return "\n".join(rows), res, tally


def standings(changes):
    """Totals on the 29 criteria (neec_scores_v2.csv) and failures, with the verdict changes in `changes`
    ({(code, cid): (prior verdict, final verdict)}) applied on top; nothing is written."""
    v2 = {e["code"]: e for e in json.load(open(path("neec_corpus_v2.json"), encoding="utf-8"))["entries"]}
    rows29 = {r["system"]: r for r in csv.DictReader(open(path("neec_scores_v2.csv"), encoding="utf-8"))}
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
    """This group's verdict changes, alone and on top of Session 71's final ones (blind_s71.FINAL), on the 29."""
    import blind_s71 as b71
    mine = {k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items() if prior[k]["verdict"] != u["verdict"]}
    p71 = b71.prior_units(p)
    s71 = {k: (p71[k]["verdict"], u["verdict"]) for k, u in b71.FINAL.items() if p71[k]["verdict"] != u["verdict"]}
    v2, alone = standings(mine)
    _, both = standings({**s71, **mine})
    held = all(v2[k[0]]["vector"][k[1]] == prior[k]["verdict"] for k in prior)
    base = standings({})[1]
    lines = ["| Entry | Total on 29 | After this group | After Sessions 71 and 72 | Failures | After both | Tier after "
             "both |", "|---|---:|---:|---:|---:|---:|---|"]
    for code in v2:
        if alone[code] != base[code] or both[code] != base[code]:
            lines.append(f"| {v2[code]['display_name']} | {base[code][0]:.1f} | {alone[code][0]:.1f} | "
                         f"{both[code][0]:.1f} | {base[code][1]} | {both[code][1]} | {pc.tier(both[code][1])} |")
    def first(st):
        top = max(t for t, _, _ in st.values())
        return " and ".join(sorted(v2[c]["display_name"] for c, (t, _, _) in st.items() if t == top)), top
    tiers = [v2[c]["display_name"] for c, (t, f, tr) in both.items() if pc.tier(f) != tr]
    return "\n".join(lines), held, first(alone), first(both), tiers, mine


def flag_effects(p, prior, units):
    """Each flagged final reading's alternative taken alone, on top of both groups' final verdicts: total, failures,
    tier, and whether first place or the tier would change."""
    import blind_s71 as b71
    p71 = b71.prior_units(p)
    changes = {k: (p71[k]["verdict"], u["verdict"]) for k, u in b71.FINAL.items() if p71[k]["verdict"] != u["verdict"]}
    changes.update({k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items()
                    if prior[k]["verdict"] != u["verdict"]})
    _, base = standings(changes)
    lines = ["| Unit | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |",
             "|---|---:|---:|---:|---:|---|---|"]
    movers = []
    for (code, cid) in sorted((k for k in units if units[k]["flag"]), key=lambda k: p.names[k[0]]):
        u = units[(code, cid)]
        alt = float(u["flag"][0][:3])
        t, f, _ = base[code]
        t2, f2 = t + alt - u["verdict"], f + (alt == 0.0) - (u["verdict"] == 0.0)
        top = max(tt for tt, _, _ in base.values())
        others = max(tt for c, (tt, _, _) in base.items() if c != code)
        changes_ = []
        if pc.tier(f2) != pc.tier(f):
            changes_.append(f"tier: {pc.tier(f)} to {pc.tier(f2)}")
        if (t >= others) != (t2 >= others) or (t == others) != (t2 == others):
            changes_.append("first place: " + ("shared" if t2 == others else "alone" if t2 > others else "lost"))
        elif t2 > top:
            changes_.append("first place: alone")
        if changes_:
            movers.append((code, cid))
        lines.append(f"| {p.names[code]} | {pc.f1(u['verdict'])} | {alt:.1f} | {t2:.1f} | {f2} | {pc.tier(f2)} | "
                     f"{'; '.join(changes_) if changes_ else '—'} |")
    return "\n".join(lines), movers


def record_check(tables, ok_print):
    rec = os.path.join(HERE, "NEEC_BlindReview_s72.md")
    if not os.path.isfile(rec):
        return ok_print(False, "NEEC_BlindReview_s72.md exists", "missing")
    text = open(rec, encoding="utf-8").read()
    missing = [name for name, t in tables if t not in text]
    return ok_print(not missing, "NEEC_BlindReview_s72.md carries every generated table verbatim (" +
                    ", ".join(name for name, _ in tables) + ")", ", ".join(missing))


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s72.py -- the blind re-read of C4.1 (ledger S55; decisions 69.1, 69.2)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    print("inputs: blind_review.py, pass_common.py and its parts, " + ", ".join(sorted(READ)) + "\n")

    print("[1] the blind readings are complete and follow the rules")
    keys = {k for t in (br.PRIOR[C41], "(b6)") for k in p.mods[p.tags.index(t)].UNITS if k[1] == C41}
    ok_print(set(NEW) == keys and len(keys) == 23, f"one blind reading for each of the {len(keys)} C4.1 units of parts "
             f"(2.11) and (b6), no more", str(sorted(set(NEW) ^ keys)))
    pc.check_records(p, NEW, ok_print)
    pc.check_rule(NEW, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in NEW.values()), "each flag names an alternative score other than the verdict")
    bad = [k for k in sorted(NEW) if len(br.blind_view(p, k)["clauses_v2"]) != len(NEW[k]["clauses"])]
    ok_print(not bad, "each reading has one status per clause blind_view shows", str(bad))
    listed = {EC + f for f in br.blind_view(p, ("SQ", C41))["cache_files"]}
    ok_print(listed <= set(READ), "every file blind_view lists for C4.1 is one this script reads or names",
             str(sorted(listed - set(READ))))

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG_PRINT.items():
        print(f"    {k}: {v}")

    print("\n[3] the blind readings (verdicts, clause statuses, flags)")
    print(blind_table(p))
    v = [r["verdict"] for r in NEW.values()]
    print(f"\nC4.1: {v.count(1.0)} at 1.0, {v.count(0.5)} at 0.5, {v.count(0.0)} at 0.0; "
          f"{sum(1 for r in NEW.values() if r['flag'])} flagged")
    btable = blind_table(p)

    print("\n[4] the comparison with parts (2.11) and (b6) (compare_group on the readings as recorded at the checkpoint)")
    prior = prior_units(p)
    t_cmp, res, tally = comparison_table(p, prior, NEW, "Blind (Session 72)")
    print(t_cmp)
    vd = sorted((k for k in res if prior[k]["verdict"] != NEW[k]["verdict"]), key=lambda k: k[0])
    cc = [k for k in res if len(prior[k]["clauses"]) != len(NEW[k]["clauses"])]
    print(f"\nblind: {tally['agree']} agree, {tally['revise']} revise; {len(cc)} on the pre-v2.0 clause list (clause "
          f"count 4 vs 2); {len(vd)} verdicts differ: " + ", ".join(
              f"{p.names[k[0]]} {pc.f1(prior[k]['verdict'])} to {pc.f1(NEW[k]['verdict'])}" for k in vd))
    ok_print(set(cc) == {k for k in prior if prior_tag(p, k) == "(b6)"},
             "the clause-count differences are exactly part (b6)'s 8 designs (decision 69.2)")

    print("\n[5] the reconciliation (protocol 5.3) and the final readings")
    ok_print(set(RECONCILE) <= set(vd), "every reconciled unit is one whose blind verdict differs from the prior's")
    ok_print(all(FINAL[k]["verdict"] == NEW[k]["verdict"] and FINAL[k]["clauses"] == NEW[k]["clauses"] for k in NEW)
             and all(NEW[k]["flag"] is None and k in vd for k in FLAGS),
             "no verdict or clause status is reconciled to the prior's: both differences stand, and FINAL differs "
             "from the blind reading only by the prior's verdict kept as a flag on a standing unit without one")
    pc.check_rule(FINAL, ok_print)
    cco = [k for k in vd if k[0] == "CCO"]
    ok_print(not cco, "no CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4: a rise is applied, a fall held)",
             str(cco))

    print("\n[6] consequences once applied (by generator in ledger S61, not here), alone and with Session 71's")
    t_cons, held, (f1n, f1t), (f2n, f2t), tiers, mine = consequence_table(p, prior, FINAL)
    ok_print(held, "neec_corpus_v2.json carries the prior's verdict for each of the 23 units (the published "
             "provisional scores are the prior's)")
    print(t_cons)
    print(f"\nfirst place on the 29 after this group alone: {f1n} at {f1t:.1f}; after Sessions 71 and 72: {f2n} at "
          f"{f2t:.1f}; tier changes: {', '.join(tiers) if tiers else 'none'}")
    t_flags, movers = flag_effects(p, prior, FINAL)
    print(f"\nthe final readings' {sum(1 for u in FINAL.values() if u['flag'])} flags, each taken alone (on both "
          "groups' final verdicts):")
    print(t_flags)
    print("flags that would change a tier or first place: " + (", ".join(p.names[c] for c, _ in movers) or "none"))

    print("\n[7] the record")
    record_check([("blind readings", btable), ("comparison", t_cmp), ("consequences", t_cons),
                  ("flag effects", t_flags)], ok_print)
    print("\nBLIND RE-READ OF C4.1 CHECKED." if ok else "\nBLIND RE-READ: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
