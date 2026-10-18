#!/usr/bin/env python3
"""
blind_s73.py -- NEEC stage 3b, the blind re-read: C4.4 and C4.2 (ledger S56; decisions 69.1, 69.2)
====================================================================================================
Session 73, on Opus 5.5. Every unit a Sonnet 5.5 session read in Sessions 63 to 65 is re-read on Opus, blind to the
earlier reading, before the Report or Paper prose describes it (ledger D52, D53). This group re-reads C4.4 Power
Distribution, the 17 units part (2.11) read (Session 65), on v2.0's two clauses ("Democratic accountability for >=80%
of major decisions", "removal/replacement mechanisms functional"), and C4.2 Ecological Compliance, the 16 units part
(2.10) read (Session 64), on v2.0's four ("Consumption-based carbon emissions falling >=3.8% a year", "biodiversity
neutral or positive", "resource extraction <= regeneration", "no more than two of the four nationally downscaled
planetary boundaries transgressed").

THE BLIND STEP. The readings below (NEW) were written from blind_review.blind_view() -- the v2.0 clause text and the
evidence_cache/C4.4/ and C4.2/ file names -- from the criteria's measurement text in criteria.json, and from the sources
this session cached (evidence_cache_s73.py) or names (evidence_cache/C4.4/sources_s73.md, C4.2/sources_s73.md), and
committed to the branch as a checkpoint before part (2.11)'s or part (2.10)'s readings of these units, Session 64's
record, or their published scores and rationales on C4.4 and C4.2, were opened, except as the record discloses
(NEEC_BlindReview_s73.md, section 2).

READINGS, C4.4 (the method each unit applies; the record states them in full)
  4.4.1 clause 1, democratic accountability for >=80% of major decisions, as the measurement defines it: the share of
        employment in organizations whose investment, production and employment decisions answer to those they
        affect -- public bodies only where the authority they answer to is chosen in free elections, member-governed
        organizations whose workers or members elect a majority of the governing body, and the self-employed. A
        configured economy: V-Dem's Regimes of the World at the stated date (2025) decides whether the public sector
        counts (2 or 3, an electoral or liberal democracy); the share is then counted on the most generous count
        (public employment, self-employment, cooperatives, mutuals, associations and foundations, all counted in), and
        is short where even that count cannot reach 80%. A design: its own sources, for the organizations in which it
        places the economy's work; one that coexists with owner-governed enterprises shows the clause only if its
        sources state or project 80%. A mechanism: out of reach (D28(c)) unless it governs the governance of the
        organizations in which people work; short where it governs some of them but cannot reach 80% generalised.
  4.4.2 clause 2, removal and replacement functional: the capacity of those to whom decision-makers answer to remove
        them in practice, legislators and executives included. A configured economy: V-Dem's Regimes of the World at
        the stated date, cleared at 2 or 3 (multiparty elections free and fair enough to change the government), short
        at 0 or 1. A design: its stated mechanism of removal (elections, recall, a member meeting) for the
        decision-makers it places, or the host's institutions where it leaves them unmodified (as Session 72 read
        Stakeholder Capitalism's host). A mechanism: out of reach unless it governs who holds decision posts.
  4.4.3 0.0 (protocol 2.1, decision 53.2): concentration in a narrow group with no functioning mechanism of removal --
        no free elections and no member control -- and clause 1 far short, a system whose own logic excludes the
        removal of its leadership by those it governs (a ruling party's leading role, hereditary rule); never with a
        clause cleared (D28(f)). A mechanism that governs neither quantity holds at 0.5 (D28(c)).
  4.4.4 wealth concentration and the adoption of citizen proposals are measured once, in C1.2b and C2.4 (the
        measurement's own text), and are not read here; the anchors' band texts describe v1.4's threshold and do not
        govern (protocol 2.3(g)).

READINGS, C4.2
  4.2.1 clause 1, consumption-based CO2 falling >=3.8% a year: the compound annual rate of change of consumption-based
        emissions (Global Carbon Budget, the cached OWID vintage) over the latest ten years of the accounts, 2013 to
        2023, and since 2019 (the bar "binds at any date"); a configuration of several economies clears only if each
        does. The historical configuration on territorial emissions (consumption accounts begin in 1990), the
        Soviet republics' territories summed. A design: projected on the same measure from its own sources -- cleared
        where they state an absolute cap or a rule that cuts at the bar's rate, short where they reject absolute limits
        or keep a host economy's record, not shown where silent. A mechanism: out of reach unless it governs emissions.
  4.2.2 clause 2, biodiversity neutral or positive: the Red List Index (UN SDG database, unrounded) at the stated date
        (2025) not below its level at the window's start (2016); for a design, the projected pressure on species and
        habitat.
  4.2.3 clause 3, extraction <= regeneration: the ecological footprint of consumption no greater than world biocapacity
        per person, read on Fanning et al. (2022), normalised to that boundary (<=1), latest year 2015, with O'Neill
        et al. (2018, mostly 2011) as the check.
  4.2.4 clause 4, no more than two of the four downscaled boundaries transgressed: phosphorus, nitrogen and
        land-system change on Fanning et al. (2022, 2015), blue water on O'Neill et al. (2018, 2011; Fanning et al.
        drop it); cleared at two or fewer of four, short at three or more, not shown where a missing boundary decides.
  4.2.5 0.0 (protocol 2.1; the anchor's band text describes the same case): no clause cleared, performance far below on
        the clauses read, and no absolute-reduction mechanism in the configuration at the stated date or in the
        design's sources (a target relative to business as usual, an intensity benchmark or voluntary disclosure does
        not count), or a system whose own logic rejects public limits on throughput. A mechanism that governs none of
        the four quantities holds at 0.5 (D28(c)).
  4.2.6 the anchors' band texts describe v1.4's threshold and do not govern (protocol 2.3(g)).

THE COMPARISON (written after the checkpoint, 7a6e0df). compare_group() sets each blind reading against the prior's --
part (2.11)'s for C4.4, part (2.10)'s for C4.2 -- agree only if every clause status and the verdict match. The record
then reconciles each verdict difference (protocol 5.3, under Session 71's rule: a blind verdict stands unless the prior
shows evidence it did not weigh, or the blind reading departs from its own stated reading). Three move to the prior's
(RECONCILE), eight stand, six of them keeping the prior's verdict as a flag (FLAGS); FINAL is what the generator session
(ledger S61) applies. No CCO-PTF-CIP-SZH unit is in this group (decisions 57.2, 69.4). One file was added to READ after
the checkpoint, for the reconciliation of China's C4.2 (FAN_BAU).

Usage: python3 blind_s73.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, blind_s71.py, blind_s72.py, the
                               evidence_cache/C4.4/ and C4.2/ files, neec_corpus_v2.json, neec_scores_v2.csv and
                               NEEC_BlindReview_s73.md; writes nothing)
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
C44, C42 = "C4.4", "C4.2"
E4, E2 = "evidence_cache/C4.4/", "evidence_cache/C4.2/"
ROW = E4 + "owid_vdem_regimes_of_the_world.csv"
ROW_SU = E4 + "owid_vdem_regimes_russia_1917_1992.csv"
SELF = E4 + "wb_self_employment_pct.json"
GOV = E4 + "fred_us_government_payrolls.csv"
N4 = E4 + "sources_s73.md"
CO2 = E2 + "owid_gcb_consumption_co2.csv"
RLI_OWID = E2 + "owid_iucn_red_list_index.csv"
RLI = E2 + "un_sdg_red_list_index.json"
FAN = E2 + "fanning_2022_biophysical_historical.csv"
ONE = E2 + "oneill_2018_biophysical.csv"
SU_CO2 = E2 + "owid_gcb_ussr_territorial_co2.csv"
LPX = E2 + "lp_platform_environment_extract.txt"
N2 = E2 + "sources_s73.md"
FAN_BAU = E2 + "fanning_2022_biophysical_bau.csv"   # added after the checkpoint (the reconciliation of China's C4.2)
READ = (ROW, ROW_SU, SELF, GOV, N4, CO2, RLI_OWID, RLI, FAN, ONE, SU_CO2, LPX, N2, FAN_BAU)
NEW = {}


def U(code, cid, verdict, clauses, flag=None, note="", zero=None):
    """One blind reading. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    NEW[(code, cid)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note, zero=zero)


def path(name):
    return os.path.join(HERE, name)


def rows(name):
    return list(csv.DictReader(open(path(name), encoding="utf-8")))


def f1(x):
    return f"{x:.1f}"


def f2(x):
    return f"{x:.2f}"


# ---- figures, recomputed from the cache -------------------------------------------------------------------------
REG = {(r["Code"], int(r["Year"])): int(r["Political regime"]) for r in rows(ROW)}
REG_SU = {int(r["Year"]): int(r["Political regime"]) for r in rows(ROW_SU)}
SELF_D = json.load(open(path(SELF), encoding="utf-8"))
GOV_R = rows(GOV)


def gov_share(year):
    xs = [r for r in GOV_R if r["date"][:4] == str(year)]
    return 100 * sum(float(r["USGOVT"]) for r in xs) / sum(float(r["PAYEMS"]) for r in xs)


CO2_K = "Annual consumption-based CO₂ emissions"
CO2_D = {}
for r in rows(CO2):
    CO2_D.setdefault(r["Code"], {})[int(r["Year"])] = float(r[CO2_K])


def cagr(iso, a, b):
    d = CO2_D[iso]
    return 100 * ((d[b] / d[a]) ** (1 / (b - a)) - 1)


RLI_D = {k: {int(y): float(v) for y, v in d.items()} for k, d in json.load(open(path(RLI), encoding="utf-8")).items()}
FAN_D = {(r["iso3c"], int(r["date"])): r for r in rows(FAN)}
ONE_D = {r["iso3c"]: r for r in rows(ONE)}
SU = {}
for r in rows(SU_CO2):
    if r["co2_mt"]:
        SU[int(r["year"])] = SU.get(int(r["year"]), 0.0) + float(r["co2_mt"])


def fan(iso, k):
    v = FAN_D[(iso, 2015)][k]
    return float(v) if v else None


def boundaries(iso):
    """The four clause-4 boundaries: phosphorus, nitrogen, land-system change (Fanning 2015; O'Neill's eHANPP where
    Fanning has none) and blue water (O'Neill 2011). Returns (values, transgressed count, missing count)."""
    o = ONE_D[iso]
    vals = {"P": fan(iso, "Phosphorus"), "N": fan(iso, "Nitrogen"), "LSC": fan(iso, "Land-System Change"),
            "BW": float(o["Blue Water"]) if o["Blue Water"] else None}
    for k, ok in (("P", "Phosphorus"), ("N", "Nitrogen"), ("LSC", "eHANPP")):
        if vals[k] is None and o[ok]:
            vals[k] = float(o[ok])
    over = sum(1 for v in vals.values() if v is not None and v > 1)
    miss = sum(1 for v in vals.values() if v is None)
    return vals, over, miss


def bstr(iso):
    vals, over, miss = boundaries(iso)
    names = {"P": "phosphorus", "N": "nitrogen", "LSC": "land-system change", "BW": "blue water"}
    return ", ".join(f"{names[k]} {f2(v)}" if v is not None else f"{names[k]} not in the accounts"
                     for k, v in vals.items()), over, miss


ISO = ("USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE")
FIG = {}
for iso in ISO:
    FIG[iso] = dict(c10=f2(cagr(iso, 2013, 2023)), c19=f2(cagr(iso, 2019, 2023)), r16=f"{RLI_D[iso][2016]:.5f}",
                    r25=f"{RLI_D[iso][2025]:.5f}", rise=RLI_D[iso][2025] >= RLI_D[iso][2016],
                    ef=f2(fan(iso, "Ecological Footprint")), ef11=ONE_D[iso]["Ecological Footprint"])
F = FIG
SU_80_88 = 100 * ((SU[1988] / SU[1980]) ** (1 / 8) - 1)
SU_60_88 = SU[1988] / SU[1960]
FIG_PRINT = {
    "Regimes of the World 2025 (USA, CHN, SGP, QAT)": ", ".join(str(REG[(i, 2025)]) for i in ISO[:4]),
    "Regimes of the World, Soviet years 1922-1990 (distinct values)": ", ".join(
        str(v) for v in sorted({REG_SU[y] for y in range(1922, 1991)})),
    "US government share of nonfarm payrolls 2016 / 2025 (%)": f"{f1(gov_share(2016))} / {f1(gov_share(2025))}",
    "self-employment 2025, % (USA, CHN, SGP, QAT)": ", ".join(f1(SELF_D[i]["2025"]) for i in ISO[:4]),
    "consumption CO2, % a year 2013-2023 (USA, CHN, SGP, QAT, DNK, FIN, NOR, SWE)": ", ".join(F[i]["c10"] for i in ISO),
    "consumption CO2, % a year 2019-2023 (same order)": ", ".join(F[i]["c19"] for i in ISO),
    "Red List Index 2016 -> 2025 (same order)": "; ".join(f"{F[i]['r16']} -> {F[i]['r25']}" for i in ISO),
    "ecological footprint / biocapacity per person, 2015 (same order)": ", ".join(F[i]["ef"] for i in ISO),
    "clause-4 boundaries transgressed of four, missing (same order)": ", ".join(
        f"{boundaries(i)[1]} ({boundaries(i)[2]})" for i in ISO),
    "Soviet territories' CO2, Mt: 1960, 1980, 1988, 1990; % a year 1980-1988": (
        f"{SU[1960]:.0f}, {SU[1980]:.0f}, {SU[1988]:.0f}, {SU[1990]:.0f}; {f2(SU_80_88)}"),
}
GCB = f"Global Carbon Budget consumption-based CO2 ({CO2})"
SDG = f"UN SDG database, Red List Index ({RLI})"
FANS = f"Fanning et al. (2022), 2015 ({FAN}); O'Neill et al. (2018) ({ONE})"
VDEM = f"V-Dem Regimes of the World ({ROW})"


# =================================================================================================================
# C4.4 Power Distribution
# =================================================================================================================
US_GOV = f1(gov_share(2025))
U("SQ", C44, 0.5,
  [("S", f"far short on the most generous count: the United States is an electoral democracy in 2025 (Regimes of the "
         f"World {REG[('USA', 2025)]}), so government counts, {US_GOV}% of nonfarm payrolls; self-employment is "
         f"{f1(SELF_D['USA']['2025'])}%; nonprofits (about a tenth of private employment) and cooperatives (about 2 "
         f"million jobs) counted in, the share stays near a third; the rest work in enterprises whose boards their "
         f"owners elect (reading 4.4.1)", f"{GOV}; {SELF}; {N4}"),
   ("C", f"cleared: legislators and executives are removable in free multiparty elections (Regimes of the World "
         f"{REG[('USA', 2024)]} to 2024, {REG[('USA', 2025)]} in 2025) (reading 4.4.2)", VDEM)],
  flag=("0.0: reading clause 2 as the removal of the economy's decision-makers by those they affect, which the "
        "owner-elected boards that govern most employment deny, so that neither clause is shown and power is "
        "concentrated in a narrow group (protocol 2.1)", "4.4.2"),
  note="0.5: political removal functions; economic decisions answer to owners for two thirds of employment")

U("CN", C44, 0.0,
  [("S", f"far short: China is a closed autocracy (Regimes of the World {REG[('CHN', 2025)]} throughout), so neither "
         f"public administration nor the state-owned enterprises count; self-employment is {f1(SELF_D['CHN']['2025'])}% "
         f"of employment in 2025 (falling from {f1(SELF_D['CHN']['2016'])}% in 2016), and the collectives' and "
         f"enterprises' leaders are appointed through the Party's cadre system (reading 4.4.1)", f"{SELF}; {VDEM}; {N4}"),
   ("S", "short: no free elections; the Party's leadership is constitutional (article 1), and neither legislators nor "
         "executives can be removed by those they govern (reading 4.4.2)", f"{VDEM}; {N4}")],
  zero="the Party-state concentrates decision-making in a narrow group whose removal by those it governs its own "
       "constitution excludes, with clause 1 far short (reading 4.4.3)",
  note="0.0: concentration in a narrow group, no removal mechanism")

U("SG", C44, 0.5,
  [("S", f"far short: Singapore is an electoral autocracy (Regimes of the World {REG[('SGP', 2025)]} throughout "
         f"2014 to 2025), so the public sector and the government-linked companies do not count; self-employment is "
         f"{f1(SELF_D['SGP']['2025'])}% (reading 4.4.1)", f"{SELF}; {VDEM}"),
   ("S", "short: multiparty elections are held and the opposition wins votes and seats (34.4% of the vote and the Workers' "
         "Party's 10 of 97 seats in 2025), but V-Dem does not rate them free and fair, and the party has "
         "governed since 1959 (reading 4.4.2)", f"{VDEM}; {N4}")],
  flag=("0.0: reading the dominant-party state as concentration in a narrow group in which the elections do not "
        "function as removal (protocol 2.1), the same pattern as the closed autocracies", "4.4.3"),
  note="0.5: both clauses short; competitive if unequal elections are a genuine, non-trivial removal mechanism")

U("QA", C44, 0.0,
  [("S", f"far short: Qatar is a closed autocracy (Regimes of the World {REG[('QAT', 2025)]} throughout), so the public "
         f"sector does not count; self-employment is {f1(SELF_D['QAT']['2025'])}% of employment, the migrant majority "
         f"of the workforce employed in owner-governed firms (reading 4.4.1)", f"{SELF}; {VDEM}"),
   ("S", "short: the Emir is hereditary; the Shura Council's elected seats (2021) were abolished by the 2024 "
         "referendum, so no decision-maker is removable by those governed (reading 4.4.2)", f"{VDEM}; {N4}")],
  zero="hereditary rule with no removal mechanism, and clause 1 far short (reading 4.4.3)",
  note="0.0: concentration in a narrow group, no removal mechanism")

U("CPS", C44, 0.0,
  [("S", "far short: the Soviet Union was a closed autocracy (Regimes of the World "
         + ", ".join(str(v) for v in sorted({REG_SU[y] for y in range(1922, 1991)})) + " in every year from 1922 to "
         "1990), so the state sector does not count; collective-farm chairmen were nominated by the district Party "
         "committee, enterprise directors appointed by their ministries, and private and cooperative work outside "
         "the collective farms was marginal until 1988 (reading 4.4.1)", f"{ROW_SU}; {N4}"),
   ("S", "short: no free elections; the nomenklatura appointed and removed decision-makers from above (reading 4.4.2)",
    f"{ROW_SU}; {N4}")],
  zero="the planning hierarchy concentrated decisions in the Party's nomenklatura, removable only from above, with "
       "clause 1 far short (reading 4.4.3)",
  note="0.0: concentration in a bureaucratic elite, no removal mechanism")

# ---- comprehensive systems (their own sources) -------------------------------------------------------------------
U("LM", C44, 0.5,
  [("S", "short: the minimal state places the economy's work in privately owned enterprises governed by their owners, "
         "and its sources state no share of employment in accountable organizations; public employment shrinks to "
         "protection and courts (reading 4.4.1)", f"Report v1.6, LM overview; {N4}"),
   ("C", "cleared: the minimal state remains an elected constitutional government, its legislators and executives "
         "removable at elections (reading 4.4.2)", N4)],
  note="0.5: political removal kept; economic decisions answer to owners")

U("SC", C44, 0.5,
  [("S", "short: the reform widens boards' duties to stakeholders but leaves boards elected by owners; even parity "
         "codetermination gives the shareholder-side chair the casting vote, so the board answers to owners in the "
         "definition's sense (reading 4.4.1)", f"Report v1.6, SC overview; {N4}"),
   ("C", f"cleared, on the host's institutions, which the reform leaves unmodified: free elections remove legislators "
         f"and executives (Regimes of the World {REG[('USA', 2025)]}, United States 2025) (reading 4.4.2)",
    f"{VDEM}; {N4}")],
  note="0.5: the host's political removal; boards still answer to owners")

U("FALC", C44, 0.5,
  [("U", "not shown: the design calls for public ownership of energy and data and for municipal and cooperative "
         "enterprise, but states no share of employment in accountable organizations (reading 4.4.1)",
    f"Report v1.6, FALC overview; {N4}"),
   ("C", "cleared: the design is pursued through elections ('luxury populism') within a liberal democracy, whose "
         "removal mechanisms it keeps (reading 4.4.2)", N4)],
  note="0.5: electoral removal kept; the ownership programme is not quantified")

U("DE", C44, 0.5,
  [("U", "not shown: 'Design to Distribute' offers cooperatives, commons and employee ownership as a menu, not an "
         "adopted design, and no share of employment is stated (reading 4.4.1)",
    f"NEEC_DoughnutEconomics_scoring_scratch.md, overview (scope decision); {N4}"),
   ("U", "not shown: the framework specifies no institutions of removal; its city portraits sit in elected municipal "
         "governments, which are the host's, not the design's (reading 4.4.2)",
    "NEEC_DoughnutEconomics_scoring_scratch.md, overview (scope decision)")],
  flag=("0.0: reading the scope decision strictly -- the framework adopts no ownership or governance mechanism, so no "
        "structural mechanism addresses the criterion (protocol 2.1, first condition)", "4.4.3"),
  note="0.5: a compass, not a map; the menu names accountable forms without adopting one")

# ---- mechanisms (generalised, protocol 3.2) -------------------------------------------------------------------------
R2 = "out of reach: the mechanism governs no removal of legislators, executives or managers (reading 4.4.2)"
U("MMT", C44, 0.5,
  [("R", "out of reach: the job guarantee's jobs are run by local governments, nonprofits and community bodies, but "
         "the programme employs only the buffer of those who lack work and governs no other organization's decisions "
         "(reading 4.4.1)", f"Report v1.6, MMT overview; {N4}"),
   ("R", R2, f"Report v1.6, MMT overview")],
  note="0.5: a macroeconomic and employment mechanism that governs neither quantity (D28(c))")

U("UBI", C44, 0.5,
  [("R", "out of reach: an unconditional income strengthens the power to refuse work (exit, C2.5's), but places no "
         "decision with those it affects (reading 4.4.1)", f"Report v1.6, UBI overview; {N4}"),
   ("R", R2, "Report v1.6, UBI overview")],
  note="0.5: a transfer mechanism that governs neither quantity (D28(c))")

U("UBS", C44, 0.5,
  [("S", "short: generalised to every service it provides (health, education, care, housing, transport, information), "
         "its public and community providers answer to elected authorities where the host is a democracy, but they "
         "employ a minority of the workforce, far from 80%, and participatory governance is proposed, not specified "
         "(reading 4.4.1)", f"NEEC_UniversalBasicServices_scoring_scratch.md, overview; {N4}"),
   ("R", R2 + "; the services' governance is the host's", N4)],
  note="0.5: accountable provision within the services' share of employment only")

U("GEO", C44, 0.5,
  [("R", "out of reach: the tax captures land rent and the dividend distributes it; neither governs who takes the "
         "decisions of the organizations in which people work (reading 4.4.1)",
    "NEEC_Georgism_LVT_scoring_scratch.md, overview"),
   ("R", R2, "NEEC_Georgism_LVT_scoring_scratch.md, overview")],
  note="0.5: a fiscal mechanism that governs neither quantity (D28(c))")

U("IF", C44, 0.5,
  [("R", "out of reach: the contracts set the terms of finance, not the governance of the firm; where they give voice "
         "(musharaka) it follows the capital contributed, and investment account holders have no governance rights "
         "(reading 4.4.1)", "NEEC_IslamicFinance_scoring_scratch.md, overview"),
   ("R", R2, "NEEC_IslamicFinance_scoring_scratch.md, overview")],
  note="0.5: a financing mechanism that governs neither quantity (D28(c))")

U("MC", C44, 0.5,
  [("R", "out of reach: the network's members govern the network and its credit limits, but it places no "
         "organization's investment, production or employment decisions (reading 4.4.1)",
    "NEEC_MutualCredit_LETS_scoring_scratch.md, overview"),
   ("R", R2, "NEEC_MutualCredit_LETS_scoring_scratch.md, overview")],
  note="0.5: a monetary mechanism that governs neither quantity (D28(c))")

U("OS", C44, 0.5,
  [("S", "short: within a commons the appropriators make and revise the rules (design principle 3), so its decisions "
         "are accountable; generalised to every common-pool resource it can govern, the commons employ a small share "
         "of an economy's workers and the mechanism governs no firm (reading 4.4.1)",
    "NEEC_Ostrom_Commons_scoring_scratch.md, overview"),
   ("R", "out of reach beyond the commons: within it monitors are accountable to the appropriators or drawn from them "
         "(design principle 4), but generalised it governs no removal of legislators, executives or managers "
         "(reading 4.4.2)", "NEEC_Ostrom_Commons_scoring_scratch.md, overview")],
  note="0.5: accountable governance within the commons' share of the economy only")

U("SWF", C44, 0.5,
  [("R", "out of reach: the fund manages a portfolio of minority stakes and votes as a shareholder; it governs no "
         "organization's employment decisions beyond its own (reading 4.4.1)",
    "NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview"),
   ("R", R2 + "; the fund answers to the host's parliament", "NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview")],
  note="0.5: a fiscal-investment mechanism that governs neither quantity (D28(c))")


# =================================================================================================================
# C4.2 Ecological Compliance
# =================================================================================================================
def c1(iso, extra=""):
    return (f"short: consumption-based CO2 changed by {F[iso]['c10']}% a year over 2013 to 2023 and {F[iso]['c19']}% a "
            f"year since 2019, against the bar's -3.8%{extra} (reading 4.2.1)")


def c2(iso):
    word = "cleared" if F[iso]["rise"] else "short"
    return (f"{word}: the Red List Index is {F[iso]['r25']} in 2025 against {F[iso]['r16']} in 2016 (reading 4.2.2)")


def c3(iso):
    return (f"short: the ecological footprint of consumption is {F[iso]['ef']} times world biocapacity per person in "
            f"2015 ({F[iso]['ef11']} in 2011) (reading 4.2.3)")


def c4(iso):
    s, over, miss = bstr(iso)
    if over > 2:
        return "S", f"short: {over} of the four transgressed ({s}; 1 = the boundary) (reading 4.2.4)"
    if over + miss <= 2:
        return "C", f"cleared: {over} of the four transgressed ({s}; 1 = the boundary) (reading 4.2.4)"
    return "U", (f"not shown: {over} transgressed and {miss} not in the accounts ({s}), so the missing boundary "
                 "decides (reading 4.2.4)")


def cfg(iso):
    st4, t4 = c4(iso)
    return [("S", c1(iso), GCB), ("C" if F[iso]["rise"] else "S", c2(iso), SDG), ("S", c3(iso), FANS), (st4, t4, FANS)]


U("SQ", C42, 0.0, cfg("USA"),
  zero=("far below on all four clauses -- consumption emissions falling a tenth as fast as the bar, the Red List Index "
        "declining, a footprint five times world biocapacity, all four boundaries transgressed -- with no national "
        "cap or price in the configuration at the stated date, whose federal direction in 2025 is reversal (the "
        "clean-electricity credits phased out, the Paris withdrawal); sub-national caps cover a minority of "
        "emissions (reading 4.2.5)"),
  flag=("0.5: reading the sub-national caps (California, Washington, the RGGI states) as a genuine absolute-reduction "
        "mechanism covering part of the population, and the emissions' decline since 2005 as its sign (protocol "
        "2.1, 0.5's third case)", "4.2.5"),
  note="0.0: far below on all four, no national absolute-reduction mechanism")

NSD = [("S", "short: consumption-based CO2 changed by " + ", ".join(
            f"{F[i]['c10']}%" for i in ("DNK", "FIN", "NOR", "SWE")) + " a year over 2013 to 2023 (Denmark, Finland, "
        "Norway, Sweden), none at the bar's -3.8%; the configuration clears only if each does (reading 4.2.1)", GCB),
       ("C" if all(F[i]["rise"] for i in ("DNK", "FIN", "NOR", "SWE")) else "S",
        "cleared: the Red List Index is not below its 2016 level in 2025 in all four (" + "; ".join(
            f"{F[i]['r16']} to {F[i]['r25']}" for i in ("DNK", "FIN", "NOR", "SWE")) + ") (reading 4.2.2)", SDG),
       ("S", "short: the footprint of consumption is " + ", ".join(F[i]["ef"] for i in ("DNK", "FIN", "NOR", "SWE"))
        + " times world biocapacity per person in 2015 (reading 4.2.3)", FANS),
       ("S", "short: " + "; ".join(f"{n} {boundaries(i)[1]} of four" for n, i in (
           ("Denmark", "DNK"), ("Finland", "FIN"), ("Norway", "NOR"), ("Sweden", "SWE")))
        + " transgressed (phosphorus, nitrogen and land-system change above the boundary; blue water within) "
          "(reading 4.2.4)", FANS)]
U("NSD", C42, 0.5, NSD,
  note="0.5: carbon taxes and climate acts with absolute targets; biodiversity held; carbon, footprint and boundaries "
       "short")

U("CN", C42, 0.5,
  [("S", c1("CHN", "; emissions are still rising"), GCB), ("S", c2("CHN"), SDG), ("S", c3("CHN"), FANS),
   (c4("CHN")[0], c4("CHN")[1], FANS)],
  note="0.5: within two of the four downscaled boundaries (blue water and land-system change), short on the rest; "
       "the trading scheme is intensity-based")

U("SG", C42, 0.5, cfg("SGP"),
  flag=("0.0: reading the carbon tax as too low and too narrow (territorial, S$25 a tonne in 2024 and 2025) to be an "
        "absolute-reduction mechanism for consumption emissions, which have risen since 2019, so that all four "
        "clauses are short with no corrective (protocol 2.1)", "4.2.5"),
  note="0.5: all four short, but a legislated, rising carbon tax and a net-zero target are a genuine mechanism")

U("QA", C42, 0.0, cfg("QAT"),
  zero=("far below on the three clauses read -- consumption emissions rising 4% a year, the Red List Index falling, a "
        "footprint eight times world biocapacity -- and the configuration's target is relative to business as usual "
        "while its gas capacity is to nearly double by about 2030 (reading 4.2.5)"),
  note="0.0: an expanding hydrocarbon economy with only a relative target")

SU_EST = (f"short: the Soviet territories' emissions rose from {SU[1960]:.0f} Mt in 1960 to {SU[1988]:.0f} Mt in 1988 "
          f"({f2(SU_80_88)}% a year in 1980 to 1988), {SU_60_88:.1f} times in 28 years, on the territorial measure "
          f"(consumption accounts begin in 1990) (reading 4.2.1)")
U("CPS", C42, 0.0,
  [("S", SU_EST, SU_CO2),
   ("S", "short: the irrigation plan for the Amu Darya and Syr Darya halved the Aral Sea and ended its fishery, most "
         "of its native fish species lost, the defining case of the planned economy's pressure on habitat (reading "
         "4.2.2)", N2),
   ("U", "not shown: the footprint accounts carry the USSR to 1991, but the figure was not cached (reading 4.2.3)", N2),
   ("U", "not shown: the downscaled boundary accounts begin in 1992 (reading 4.2.4)", FAN)],
  zero=("the plan's gross-output targets drove extensive growth in throughput with no absolute limit, emissions rising "
        "every decade to the collapse and the Aral Sea destroyed by the plan itself; the emission norms of 1980 were "
        "overridden by the plan (reading 4.2.5; D29(a), the same pattern across the Eastern Bloc's planned economies)"),
  flag=("0.5: reading the planner's capacity to set physical output directly, and the 1980 air-protection norms, as a "
        "mechanism the system itself provides, unused rather than absent (D29(b))", "4.2.5"),
  note="0.0: far below on the clauses read, the plan's own logic expanding throughput")

# ---- comprehensive systems (their own sources) -------------------------------------------------------------------
U("LM", C42, 0.0,
  [("S", "short: the design rejects public limits on energy ('We oppose all government control of energy pricing, "
         "allocation, and production') and offers restitution 'where damages can be proven and quantified in a court "
         "of law', which cannot reach diffuse emissions with no identifiable injurer, so no cut is projected (reading "
         "4.2.1)", LPX),
   ("U", "not shown: private landowners' and conservation groups' interest in maintaining resources is asserted, no "
         "pressure on species is projected (reading 4.2.2)", LPX),
   ("U", "not shown: no footprint is projected (reading 4.2.3)", LPX),
   ("U", "not shown: no boundary is projected (reading 4.2.4)", LPX)],
  zero=("the design's own logic rejects public limits on throughput and energy, and its one remedy, court restitution "
        "for proven and quantified damage, cannot reach diffuse emissions or habitat loss, so no structural "
        "mechanism addresses the criterion (reading 4.2.5)"),
  flag=("0.5: reading property rights and the restitution remedy as a genuine, non-trivial mechanism for local "
        "pollution and resource stewardship (protocol 2.1, 0.5's first case)", "4.2.5"),
  note="0.0: public limits rejected; the tort remedy cannot reach the criterion's quantities")

U("SC", C42, 0.0,
  [("S", c1("USA", ", on the host's record, which the reform's voluntary metrics leave unchanged"), f"{GCB}; {N2}"),
   ("S", c2("USA") + ", on the host's record", SDG), ("S", c3("USA"), FANS), (c4("USA")[0], c4("USA")[1], FANS)],
  zero=("the reform's instruments are disclosure and voluntary metrics, relative or intensity targets substituting for "
        "absolute limits, on a host far below every clause (reading 4.2.5; the anchor's 0.0 band describes the same "
        "case)"),
  flag=("0.5: reading the Science Based Targets initiative's absolute targets, adopted by some firms, as a genuine "
        "absolute-reduction mechanism within the reform's reach", "4.2.5"),
  note="0.0: voluntary, relative metrics on the host's record")

U("MS", C42, 0.5,
  [("U", "not shown: democratic firms that maximise income per worker lack capital's expansionary imperative, and "
         "social control of investment could direct it, but no cap or emissions path is stated (reading 4.2.1)",
    f"Report v1.6, MS overview; {N2}"),
   ("U", "not shown: no pressure on species is projected (reading 4.2.2)", N2),
   ("U", "not shown: no footprint is projected (reading 4.2.3)", N2),
   ("U", "not shown: no boundary is projected (reading 4.2.4)", N2)],
  flag=("0.0: reading the design as competitive markets with no absolute-reduction mechanism (protocol 2.1; the "
        "anchor's first 0.0 case), the cooperative firm's restraint being on hiring, not on throughput", "4.2.5"),
  note="0.5: a structural damper on the growth imperative, no limit stated")

# ---- mechanisms (generalised, protocol 3.2) -------------------------------------------------------------------------
def reach(why, src):
    return [("R", f"out of reach: {why}; consumption emissions are the host's (reading 4.2.1)", src),
            ("R", f"out of reach: {why}; species and habitat are the host's (reading 4.2.2)", src),
            ("R", f"out of reach: {why}; the footprint is the host's (reading 4.2.3)", src),
            ("R", f"out of reach: {why}; the boundaries are the host's (reading 4.2.4)", src)]


U("GEO", C42, 0.5,
  reach("the tax governs the use of land, encouraging compact use, and its dividend distributes rent; neither "
        "governs emissions, extraction or habitat, and pollution charges are not part of the design scored",
        f"NEEC_Georgism_LVT_scoring_scratch.md, overview; {N2}"),
  note="0.5: a land-tax mechanism that governs none of the four quantities (D28(c))")

U("IF", C42, 0.5,
  reach("the contracts set the terms of finance and exclude prohibited sectors, but govern no quantity of throughput",
        "NEEC_IslamicFinance_scoring_scratch.md, overview"),
  note="0.5: a financing mechanism that governs none of the four quantities (D28(c))")

U("MC", C42, 0.5,
  reach("a zero-sum credit network governs the medium of local exchange, not what is produced or extracted",
        "NEEC_MutualCredit_LETS_scoring_scratch.md, overview"),
  note="0.5: a monetary mechanism that governs none of the four quantities (D28(c))")

U("OS", C42, 0.5,
  [("R", "out of reach: the mechanism governs local common-pool resources, not energy or consumption emissions; "
         "Ostrom's polycentric argument for climate action is not a commons institution governing them (reading "
         "4.2.1)", f"NEEC_Ostrom_Commons_scoring_scratch.md, overview; {N2}"),
   ("U", "not shown: sustained yield preserves the habitat of the resources the commons govern, but no economy-wide "
         "pressure on species is projected (reading 4.2.2)", "NEEC_Ostrom_Commons_scoring_scratch.md, overview"),
   ("R", "out of reach: within a commons the long-enduring cases hold extraction within regeneration, but generalised "
         "the mechanism does not govern the consumption footprint, which energy and traded goods dominate (reading "
         "4.2.3)", f"NEEC_Ostrom_Commons_scoring_scratch.md, overview; {N2}"),
   ("R", "out of reach: the national boundaries are set by agriculture, water and land use beyond the commons "
         "(reading 4.2.4)", "NEEC_Ostrom_Commons_scoring_scratch.md, overview")],
  note="0.5: sustained yield within the commons; the criterion's national quantities beyond its reach")

U("SWF", C42, 0.5,
  reach("the fund invests a revenue stream and governs its portfolio (the coal exclusion, the climate action plan), "
        "not the national economy's emissions, extraction or habitat",
        f"NEEC_SovereignWealthFundStatism_scoring_scratch.md, overview; {N2}"),
  flag=("0.0: reading the mechanism in its classic form, which exists to convert the rents of non-renewable extraction "
        "into financial assets and so depends on extraction continuing (protocol 2.1)", "4.2.5"),
  note="0.5: an investment mechanism that governs none of the four quantities (D28(c))")

U("UBI", C42, 0.5,
  reach("an income transfer governs no quantity of production, extraction or emissions; a carbon fee and dividend "
        "is a different design, not the mechanism scored",
        f"Report v1.6, UBI overview; {N2}"),
  note="0.5: a transfer mechanism that governs none of the four quantities (D28(c))")

U("UBS", C42, 0.5,
  [("U", "not shown: collective provision of transport, housing and food is argued to lower consumption emissions, but "
         "no path is projected on the measure (reading 4.2.1)",
    f"NEEC_UniversalBasicServices_scoring_scratch.md, overview; {N2}"),
   ("R", "out of reach: service provision governs no pressure on species or habitat (reading 4.2.2)", N2),
   ("U", "not shown: the 'fair consumption space' argument places provision within a footprint ceiling, but no "
         "footprint is projected (reading 4.2.3)", N2),
   ("R", "out of reach: the boundaries are set by agriculture, water and land use beyond the services (reading 4.2.4)",
    N2)],
  note="0.5: a provision mechanism argued to lower footprints, none projected")


# ---- the blind record ----------------------------------------------------------------------------------------------
def blind_table(p, cid):
    rows_ = ["| Unit | Clause statuses | Verdict | Flag |", "|---|---|---|---|"]
    for (code, c) in sorted((k for k in NEW if k[1] == cid), key=lambda k: p.names[k[0]]):
        r = NEW[(code, c)]
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


# ---- the reconciliation, after the comparison (protocol 5.3; written after the checkpoint, 7a6e0df) -------------
# Three blind verdicts change on reconciliation, each toward the prior's, with the blind verdict kept as the flag; the
# reason says what the blind reading did not weigh or where it departed from its own stated reading.
RECONCILE = {
    ("DE", C44): dict(
        verdict=0.0, clauses=None,
        flag=("0.5: reading the framework's named ownership forms (cooperatives, commons, employee ownership) as a "
              "mechanism that addresses the criterion in principle, as the blind reading did", "4.4.3"),
        zero="protocol 2.1, first condition: no structural mechanism addresses the criterion -- the framework adopts "
             "no ownership or governance design and specifies no institution of removal (the scoring document's "
             "scope decision)",
        note="0.0: the blind reading's own clause estimates found no mechanism adopted, which 2.1's first condition "
             "scores 0.0",
        reason="the blind reading's clause estimates found the ownership forms offered 'as a menu, not an adopted "
               "design' and no institution of removal specified, and its own flag stated 2.1's first condition; its "
               "0.5 credited the menu as though it were a mechanism, which its estimates deny. Session 71 reconciled "
               "the same framework's C4.5 to 0.0 on the same ground (NEEC_BlindReview_s71.md, section 6)"),
    ("SG", C44): dict(
        verdict=0.0, clauses=None,
        flag=("0.5: reading multiparty elections in which the opposition wins a third of the vote and a tenth of the "
              "seats as a genuine, non-trivial removal mechanism, as the blind reading did", "4.4.3"),
        zero="protocol 2.1, read by reading 4.4.3: no free elections (V-Dem's electoral autocracy throughout 2014 to "
             "2025) and no member control, with clause 1 far short (the public sector not counted, self-employment "
             "12.7%)",
        note="0.0: the blind reading's own 4.4.3 conditions hold",
        reason="reading 4.4.3, stated before the readings, sets 0.0 where there are no free elections and no member "
               "control and clause 1 is far short, and reading 4.4.2 takes V-Dem's classification as the test of "
               "free elections; Singapore meets every condition, and the blind 0.5 rested on a judgment of the "
               "elections' competitiveness that the stated reading does not make. The prior reached 0.0 on the same "
               "evidence and flagged 0.5, as the blind reading now does"),
    ("SG", C42): dict(
        verdict=0.0, clauses=None,
        flag=("0.5: reading the legislated, rising carbon tax as a genuine absolute-reduction instrument, as the blind "
              "reading did", "4.2.5"),
        zero="protocol 2.1, read by reading 4.2.5: no clause cleared, consumption emissions up since 2019 and the "
             "decade's fall under the bar, the Red List Index falling, a footprint four times world biocapacity; and "
             "the configuration's own 2030 target lets emissions rise to their peak, so the tax is not an "
             "absolute-reduction mechanism within the window (the scoring document, as part (2.10) reads it)",
        note="0.0: the configuration's own target path rises to 2030, evidence the blind reading did not weigh",
        reason="the blind reading credited the carbon tax as an absolute-reduction mechanism; the prior cites the "
               "entry's own account that Singapore's 2030 target path rises (rated highly insufficient by the "
               "Climate Action Tracker), which the blind reading did not weigh and which its own flag anticipated "
               "(the tax 'too low and too narrow'). A tax set under a target that permits emissions to rise is, on "
               "reading 4.2.5, not an absolute-reduction mechanism in the configuration at the stated date"),
}
# A standing blind verdict keeps the prior's verdict as its flag where it has none (as Sessions 71 and 72 did).
FLAGS = {
    ("FALC", C44): ("0.0: reading the design as leaving the control of the machines unresolved and stating no "
                    "mechanism of removal of its own (protocol 2.1, first condition), the prior's reading", "4.4.3"),
    ("IF", C44): ("0.0: reading the mechanism as one no structural element of which addresses the distribution of "
                  "decision power (protocol 2.1, first condition), the prior's reading, rather than as out of reach",
                  "4.4.3"),
    ("SC", C44): ("0.0: reading the reform without its host's institutions, so that it states no mechanism of removal "
                  "and worker directors stay a minority (protocol 2.1, first condition), the prior's reading", "4.4.3"),
    ("UBI", C44): ("0.0: reading an income transfer that changes no one's decision power as no structural mechanism "
                   "(protocol 2.1, first condition), the prior's reading, rather than as out of reach", "4.4.3"),
    ("CN", C42): ("0.0: reading clause 4 as not shown at the stated date, the boundary accounts ending in 2015 and "
                  "blue water's in 2011, so that no clause is cleared and the prior's reading holds: emissions "
                  "rising, intensity targets, the index falling", "4.2.4"),
    ("IF", C42): ("0.0: reading green sukuk and value-based intermediation as allocative labels that substitute for "
                  "absolute limits (the anchor's second 0.0 case), the prior's reading, rather than as out of reach",
                  "4.2.5"),
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


def prior_units(p):
    return {k: v for cid in (C44, C42) for k, v in p.mods[p.tags.index(br.PRIOR[cid])].UNITS.items() if k[1] == cid}


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
    """Sessions 71's and 72's final verdict changes (blind_s71.FINAL, blind_s72.FINAL) against their priors."""
    import blind_s71 as b71
    import blind_s72 as b72
    out = {}
    for mod in (b71, b72):
        pr = mod.prior_units(p)
        out.update({k: (pr[k]["verdict"], u["verdict"]) for k, u in mod.FINAL.items() if pr[k]["verdict"] != u["verdict"]})
    return out


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
    """This group's verdict changes, alone and on top of Sessions 71's and 72's final ones, on the 29."""
    mine = {k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items() if prior[k]["verdict"] != u["verdict"]}
    v2, alone = standings(mine)
    _, both = standings({**earlier_changes(p), **mine})
    held = all(v2[k[0]]["vector"][k[1]] == prior[k]["verdict"] for k in prior)
    base = standings({})[1]
    lines = ["| Entry | Total on 29 | After this group | After Sessions 71 to 73 | Failures | After all three | "
             "Tier after all three |", "|---|---:|---:|---:|---:|---:|---|"]
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
    """Each flagged final reading's alternative taken alone, on top of all three groups' final verdicts: total,
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
    rec = os.path.join(HERE, "NEEC_BlindReview_s73.md")
    if not os.path.isfile(rec):
        return ok_print(False, "NEEC_BlindReview_s73.md exists", "missing")
    text = open(rec, encoding="utf-8").read()
    missing = [name for name, t in tables if t not in text]
    return ok_print(not missing, "NEEC_BlindReview_s73.md carries every generated table verbatim (" +
                    ", ".join(name for name, _ in tables) + ")", ", ".join(missing))


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s73.py -- the blind re-read of C4.4 and C4.2 (ledger S56; decisions 69.1, 69.2)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    print("inputs: blind_review.py, pass_common.py and its parts, " + ", ".join(sorted(READ)) + "\n")

    print("[1] the blind readings are complete and follow the rules")
    for cid, n in ((C44, 17), (C42, 16)):
        keys = {k for k in p.mods[p.tags.index(br.PRIOR[cid])].UNITS if k[1] == cid}
        mine = {k for k in NEW if k[1] == cid}
        ok_print(mine == keys and len(keys) == n, f"one blind reading for each of the {n} {cid} units of part "
                 f"{br.PRIOR[cid]}, no more", str(sorted(mine ^ keys)))
    pc.check_records(p, NEW, ok_print)
    pc.check_rule(NEW, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in NEW.values()), "each flag names an alternative score other than the verdict")
    bad = [k for k in sorted(NEW) if len(br.blind_view(p, k)["clauses_v2"]) != len(NEW[k]["clauses"])]
    ok_print(not bad, "each reading has one status per clause blind_view shows", str(bad))
    for cid, ec in ((C44, E4), (C42, E2)):
        key = next(k for k in sorted(NEW) if k[1] == cid)
        listed = {ec + f for f in br.blind_view(p, key)["cache_files"]}
        ok_print(listed <= set(READ), f"every file blind_view lists for {cid} is one this script reads or names",
                 str(sorted(listed - set(READ))))

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG_PRINT.items():
        print(f"    {k}: {v}")

    print("\n[3] the blind readings (verdicts, clause statuses, flags)")
    for cid in (C44, C42):
        print(f"\n{cid}:")
        print(blind_table(p, cid))
        v = [r["verdict"] for k, r in NEW.items() if k[1] == cid]
        print(f"\n{cid}: {v.count(1.0)} at 1.0, {v.count(0.5)} at 0.5, {v.count(0.0)} at 0.0; "
              f"{sum(1 for k, r in NEW.items() if k[1] == cid and r['flag'])} flagged")

    btables = [blind_table(p, C44), blind_table(p, C42)]

    print("\n[4] the comparison with parts (2.11) and (2.10) (compare_group on the readings as recorded at the "
          "checkpoint)")
    prior = prior_units(p)
    cmp_tables, vd = [], []
    for cid in (C44, C42):
        t_cmp, res, tally = comparison_table(p, prior, NEW, cid, "Blind (Session 73)")
        cmp_tables.append(t_cmp)
        print(f"\n{cid}, against part {br.PRIOR[cid]}:")
        print(t_cmp)
        d = sorted((k for k in res if prior[k]["verdict"] != NEW[k]["verdict"]), key=lambda k: k[0])
        vd += d
        print(f"\n{cid}: {tally['agree']} agree, {tally['revise']} revise; {len(d)} verdicts differ: " + ", ".join(
            f"{p.names[k[0]]} {pc.f1(prior[k]['verdict'])} to {pc.f1(NEW[k]['verdict'])}" for k in d))

    print("\n[5] the reconciliation (protocol 5.3) and the final readings")
    ok_print(set(RECONCILE) <= set(vd), "every reconciled unit is one whose blind verdict differs from the prior's")
    ok_print(all(FINAL[k]["verdict"] == prior[k]["verdict"] for k in RECONCILE),
             "each reconciliation moves the verdict to the prior's, and only there")
    ok_print(all(NEW[k]["flag"] is None and k in vd and k not in RECONCILE for k in FLAGS),
             "the prior's verdict is kept as a flag only on a standing difference whose blind reading had none")
    ok_print(all(FINAL[k]["flag"] and FINAL[k]["flag"][0][:3] == pc.f1(NEW[k]["verdict"]) for k in RECONCILE),
             "each reconciled unit keeps its blind verdict as its flag")
    pc.check_rule(FINAL, ok_print)
    stand = [k for k in vd if k not in RECONCILE]
    print("standing verdict changes: " + ", ".join(
        f"{p.names[k[0]]} {k[1]} {pc.f1(prior[k]['verdict'])} to {pc.f1(FINAL[k]['verdict'])}" for k in stand))
    cco = [k for k in vd if k[0] == "CCO"]
    ok_print(not cco, "no CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4: a rise is applied, a fall held)",
             str(cco))
    final_tables = [blind_table_final(p, cid) for cid in (C44, C42)]
    for cid, t in zip((C44, C42), final_tables):
        print(f"\nfinal readings, {cid}:")
        print(t)

    print("\n[6] consequences once applied (by generator in ledger S61, not here), alone and with Sessions 71 and 72")
    t_cons, held, (f1n, f1t), (f2n, f2t), tiers, tiers_alone, mine = consequence_table(p, prior, FINAL)
    ok_print(held, "neec_corpus_v2.json carries the prior's verdict for each of the 33 units (the published "
             "provisional scores are the prior's)")
    print(t_cons)
    print(f"\nfirst place on the 29 after this group alone: {f1n} at {f1t:.1f}; after Sessions 71 to 73: {f2n} at "
          f"{f2t:.1f}")
    print("tier changes, this group alone: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers_alone) or "none"))
    print("tier changes, after Sessions 71 to 73: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers) or "none"))
    t_flags, movers = flag_effects(p, prior, FINAL)
    print(f"\nthe final readings' {sum(1 for u in FINAL.values() if u['flag'])} flags, each taken alone (on all three "
          "groups' final verdicts):")
    print(t_flags)
    print("flags that would change a tier or first place: " + (", ".join(f"{p.names[c]} {cid}" for c, cid in movers)
                                                                or "none"))

    print("\n[7] the record")
    record_check([("blind readings, C4.4", btables[0]), ("blind readings, C4.2", btables[1]),
                  ("comparison, C4.4", cmp_tables[0]), ("comparison, C4.2", cmp_tables[1]),
                  ("final readings, C4.4", final_tables[0]), ("final readings, C4.2", final_tables[1]),
                  ("consequences", t_cons), ("flag effects", t_flags)], ok_print)
    print("\nBLIND RE-READ OF C4.4 AND C4.2 CHECKED." if ok else "\nBLIND RE-READ: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
