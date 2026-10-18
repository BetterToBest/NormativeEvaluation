#!/usr/bin/env python3
"""
blind_s71.py -- NEEC stage 3b, the blind re-read: C4.5 and C3.4 (ledger S54; decisions 69.1, 69.2)
====================================================================================================
Session 71, on Opus 5.5. Every unit a Sonnet 5.5 session read in Sessions 63 to 65 is re-read on Opus, blind to the
earlier reading, before the Report or Paper prose describes it (ledger D52, D53). This group re-reads the two
criteria that decide first place: C4.5 Exploitation Elimination (17 units, part (2.11)) and C3.4 Epistemic
Adaptability (7 units, part (2.11)).

THE BLIND STEP. The readings below (NEW) were written from blind_review.blind_view() -- the v2.0 clause text and the
evidence_cache/ file names -- and from the sources this session cached (evidence_cache_s71.py) or names
(evidence_cache/C4.5/sources_s71.md, evidence_cache/C3.4/sources_s71.md), and committed to the branch as a checkpoint
before part (2.11)'s readings of these units, or the published (v1) scores and rationales of these units on these two
criteria, were opened. What the session had seen before recording is stated in the record
(NEEC_BlindReview_s71.md, section 2): criteria.json's anchors for both criteria (published examples), STATE.md's
summary of two prior moves (Participatory Economics' C4.5, Integral's C3.4), and the peers' readings in the Opus-read
parts ((a), (b1), (b8), (2.5)), which are calibration (protocol 5), not the prior reading of these units.

READINGS (the method each unit applies; the record states them in full)
  C4.5  4.5.1 clause 1: extraction is the transfer to owners of capital, landlords and lenders as a share of GDP; a
              configured economy on the broad count (one minus the labour share, Penn World Table 10.01) and, for the
              United States, the narrow count (corporate profits, rental income and net interest, BEA); a design or
              mechanism from its own sources; state appropriation is extraction relocated, not removed (parts (a) and
              (b8), Centrally Planned Socialism); public capture of land rent removes the landlord's share of that flow.
        4.5.2 clause 2: shown when a person can leave an employment, tenancy or credit relationship without losing
              subsistence -- an unconditional floor or an assured alternative that is not itself extractive -- for each
              such relationship the system keeps (part (b8)'s readings 3.6); the formal right to quit one employer for
              another is the minimum, not genuine exit.
        4.5.3 0.0 (protocol 2.1, decision 53.2): far below on both clauses, every relationship type in place and exit
              no more than the formal right to quit, with no rule or instrument in the system that removes one; a
              structural mechanism removing one relationship type for a large part of the population, or a substantial
              if conditional floor, is 0.5 (the 0.5 band: elimination in one relationship type).
        4.5.4 a mechanism is scored generalised (protocol 3.2): a flow it removes is credited, the flows it does not
              govern stay the host economy's, so clause 1 is short unless it governs all three.
  C3.4  3.4.1 clause 1: a core parameter moved by at least 30% of its value without redesign (part (a), Sovereign
              Wealth Fund Statism; part (b1), Market Socialism).
        3.4.2 clause 2: an update timed against the evidence that called for it (part (b1), MMT + Job Guarantee and
              Universal Basic Income); for a design, a stated rule of review within six months.
        3.4.3 clause 3 (v2.0's contestability): those affected can challenge a change and have it reversed through a
              process independent of the officials who made it -- independent courts, free elections, or, in a design
              with no officials, a participatory process any participant can open.
        3.4.4 clause 4: a systemic crisis caused by changes to the configuration's own parameters is a collapse (part
              (b1), Nordic Social Democracy); a design with no implementation and no modelling of its parameter
              adjustments does not show the clause (part (b1), reading 3.1).
        3.4.5 0.0 on a stated whole-criterion reason under protocol 2.1, never with a clause cleared (decision 53.2).

Usage: python3 blind_s71.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts
                               pass_common.PARTS names and the files they read, blind_review.py and the evidence_cache/
                               files below; writes nothing)
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
C45, C34 = "C4.5", "C3.4"
EC = "evidence_cache/"
PWT = EC + "C4.5/pwt1001_labsh_selected_economies.csv"
BEA = EC + "C4.5/fred_us_national_income_components.csv"
RENTS = EC + "C4.5/wb_natural_resource_rents_pct_gdp.json"
SDG = EC + "C4.5/un_sdg_10_4_1_labour_share.json"
SE43B = EC + "C4.5/se_lag_1997_238_43b.txt"
ATC = EC + "C4.5/hahnel_wright_2016_extract.txt"
HUB = EC + "C4.5/research_hub_8e8a6ba_cco_extract.txt"
NOTES45 = EC + "C4.5/sources_s71.md"
WPX = EC + "C3.4/integral_wp_v01_c34_extract.txt"
FEDX = EC + "C3.4/fred_cpi_fedfunds_2019_2023.csv"
NOTES34 = EC + "C3.4/sources_s71.md"
NEW = {}


def U(code, cid, verdict, clauses, flag=None, note="", zero=None):
    """One blind reading. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    NEW[(code, cid)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note, zero=zero)


def path(name):
    return os.path.join(HERE, name)


# ---- figures, recomputed from the cache -------------------------------------------------------------------------
def pwt_nonlabour(year=2019):
    rows = list(csv.DictReader(open(path(PWT), encoding="utf-8")))
    return {r["countrycode"]: 100 * (1 - float(r["labsh"])) for r in rows if int(float(r["year"])) == year}


def bea(year):
    rows = {r["year"]: r for r in csv.DictReader(open(path(BEA), encoding="utf-8"))}
    r = {k: float(v) for k, v in rows[str(year)].items() if k != "year"}
    g = r["GDPA"]
    return {"profits": 100 * r["A051RC1A027NBEA"] / g, "rent": 100 * r["A048RC1A027NBEA"] / g,
            "interest": 100 * r["W255RC1A027NBEA"] / g,
            "narrow": 100 * (r["A051RC1A027NBEA"] + r["A048RC1A027NBEA"] + r["W255RC1A027NBEA"]) / g}


def rents(iso, year):
    return json.load(open(path(RENTS), encoding="utf-8"))[iso][str(year)]


def sdg_labour(area, year):
    return float(json.load(open(path(SDG), encoding="utf-8"))[area][str(year)])


def fed():
    rows = list(csv.DictReader(open(path(FEDX), encoding="utf-8")))
    cpi = {r["date"]: float(r["CPIAUCSL"]) for r in rows}
    ff = {r["date"]: float(r["FEDFUNDS"]) for r in rows}
    yoy = {d: 100 * (cpi[d] / cpi[f"{int(d[:4]) - 1}{d[4:]}"] - 1) for d in cpi if d >= "2020-01-01"}
    first4 = min(d for d in yoy if yoy[d] > 4.0)
    rise = min(d for d in ff if d >= "2021-01-01" and ff[d] >= 0.15)
    return first4, yoy[first4], rise, ff[rise]


def f1(x):
    return f"{x:.1f}"


NL = pwt_nonlabour()
B25, B00 = bea(2025), bea(2000)
FIRST4, YOY4, RISE, FFRISE = fed()
MONTHS = (int(RISE[:4]) - int(FIRST4[:4])) * 12 + int(RISE[5:7]) - int(FIRST4[5:7])
FIG = {
    "US non-labour share of GDP, 2019 (PWT)": f1(NL["USA"]), "China": f1(NL["CHN"]), "Singapore": f1(NL["SGP"]),
    "Qatar": f1(NL["QAT"]), "Denmark": f1(NL["DNK"]), "Finland": f1(NL["FIN"]), "Norway": f1(NL["NOR"]),
    "Sweden": f1(NL["SWE"]),
    "US narrow count 2025 (BEA)": f1(B25["narrow"]), "US narrow count 2000": f1(B00["narrow"]),
    "US corporate profits 2025": f1(B25["profits"]), "US rental income 2025": f1(B25["rent"]),
    "US net interest 2025": f1(B25["interest"]),
    "Qatar resource rents 2019 (WB)": f1(rents("QAT", 2019)), "Norway resource rents 2019": f1(rents("NOR", 2019)),
    "Qatar non-labour share net of resource rents 2019": f1(NL["QAT"] - rents("QAT", 2019)),
    "Norway non-labour share net of resource rents 2019": f1(NL["NOR"] - rents("NOR", 2019)),
    "Denmark labour share 2024 (SDG 10.4.1)": f1(sdg_labour("Denmark", 2024)),
    "Finland labour share 2024": f1(sdg_labour("Finland", 2024)),
    "Sweden labour share 2024": f1(sdg_labour("Sweden", 2024)),
    "US CPI-U first above 4% year on year": f"{FIRST4[:7]} ({f1(YOY4)}%)",
    "US first federal funds rise": f"{RISE[:7]} ({FFRISE:.2f}%)", "months between": str(MONTHS),
}

PWT_S = "Penn World Table 10.01, labsh (" + PWT + ")"
BEA_S = "BEA national income through FRED (" + BEA + ")"

# ---- C4.5 Exploitation Elimination: the 17 units of part (2.11) --------------------------------------------------
NORDIC = (f"one minus the labour share of GDP is {FIG['Denmark']}% in Denmark, {FIG['Finland']}% in Finland, "
          f"{FIG['Norway']}% in Norway ({FIG['Norway non-labour share net of resource rents 2019']}% net of resource "
          f"rents) and {FIG['Sweden']}% in Sweden (2019), and the labour share in the SDG series is "
          f"{FIG['Denmark labour share 2024 (SDG 10.4.1)']}%, {FIG['Finland labour share 2024']}% and "
          f"{FIG['Sweden labour share 2024']}% in 2024 (Denmark, Finland, Sweden): around the United States' "
          f"{FIG['US non-labour share of GDP, 2019 (PWT)']}%, Denmark a little below and the others above; collective bargaining, codetermination "
          f"and tenant law regulate the terms of the three relationships, none is removed")
U("NSD", C45, 0.5,
  [("S", "far short: " + NORDIC + " (reading 4.5.1)", f"{PWT_S}; {SDG}; {RENTS}"),
   ("S", "short, but near: universal health care and social assistance do not depend on a job, unemployment "
         "insurance pays a voluntary quitter after a bounded suspension (in Sweden 45 benefit days, Lag 1997:238, "
         "43 b), and tenants hold security of tenure; the floor is conditional on seeking work, so leaving wage "
         "employment as such carries a penalty (reading 4.5.2)", f"{SE43B}; {NOTES45}")],
  note="0.5: a substantial if conditional floor on clause 2 is a genuine, non-trivial mechanism; clause 1 is far short "
       "and the welfare state does not change it (reading 4.5.3)")

SQ1 = (f"far short: one minus the labour share is {FIG['US non-labour share of GDP, 2019 (PWT)']}% of GDP (2019); on "
       f"the narrow count corporate profits, rental income and net interest are {FIG['US narrow count 2025 (BEA)']}% "
       f"of GDP in 2025 ({FIG['US corporate profits 2025']}%, {FIG['US rental income 2025']}% and "
       f"{FIG['US net interest 2025']}%), up from {FIG['US narrow count 2000']}% in 2000; each of the three "
       f"relationships is in place and none is removed (reading 4.5.1)")
SQ2 = ("far short: at-will employment gives the formal right to quit, but leaving is not survivable without another "
       "job: every state disqualifies a voluntary quit from unemployment insurance, 53.5% of people hold "
       "employment-based health insurance (2025), and tenancy and consumer credit carry no exit beyond the market's "
       "(reading 4.5.2)")
U("SQ", C45, 0.0,
  [("S", SQ1, f"{PWT_S}; {BEA_S}"),
   ("S", SQ2, f"US DOL, Comparison of State UI Laws, nonmonetary eligibility; Census P60-291 ({NOTES45})")],
  flag=("0.5: counting at-will exit with Medicaid, SNAP and the Affordable Care Act's subsidies as a partial floor, a "
        "genuine non-trivial mechanism on clause 2", "4.5.3"),
  zero="protocol 2.1, third condition: performance far below the threshold on both clauses -- extraction four times "
       "the bar on the broad count and nearly twice on the narrow, and rising; exit no more than the formal right to "
       "quit -- with no rule or instrument in the configuration that removes an extractive relationship or moves the "
       "rate toward 10% (reading 4.5.3)")

U("SC", C45, 0.0,
  [("S", "far short: the entry keeps shareholder ownership and wage employment and adds voluntary consideration of "
         "stakeholders and ESG metrics, which change neither the transfer to owners nor rent or interest; in the "
         "market economy it reforms the narrow count is " + FIG["US narrow count 2025 (BEA)"] + "% of GDP (reading "
         "4.5.1)", f"Report v1.6, SC overview; {BEA_S}"),
   ("S", "far short: exit is the host market economy's, the formal right to quit with no floor added; the entry "
         "specifies no exit from employment, tenancy or credit (reading 4.5.2)", "Report v1.6, SC overview")],
  flag=("0.5: reading stakeholder governance, where it gives workers board seats, as a structural mechanism on the "
        "power asymmetry clause 2 measures", "4.5.3"),
  zero="protocol 2.1, third condition: far below on both clauses with no pathway under the system's own logic -- the "
       "entry is voluntary corporate responsibility within the market framework, which leaves every extractive "
       "relationship in place, and Bebchuk and Tallarita (2020) found the 2019 Business Roundtable statement "
       "largely unaccompanied by changes in its signatories' corporate governance (reading 4.5.3)")

U("CN", C45, 0.5,
  [("S", f"far short: one minus the labour share is {FIG['China']}% of GDP (2019); urban land is state-owned and "
         f"rural land collective, so the land rent is captured publicly (land-use right sales to developers) and "
         f"rural households farm contracted land with no landlord; profit, interest to state banks and private "
         f"housing rent remain, and the state's share of the surplus is extraction relocated (readings 4.5.1, as "
         f"parts (a) and (b8) read the planned economy)", f"{PWT_S}"),
   ("S", "far short: a worker may quit, but unemployment insurance covers about a third of the employed (245.89 "
         "million insured, end of 2024), the minimum living guarantee is means-tested and thin, household "
         "registration ties services to place, and no union independent of the Party may organise (reading 4.5.2)",
         f"MOHRSS 2024 statistical bulletin, as reported ({NOTES45})")],
  flag=("0.0: weighting the non-labour share and the absent exit as performance far below both clauses, and the "
        "public capture of land rent as passed into housing prices rather than removing the household's payment",
        "4.5.3"),
  note="0.5: public and collective ownership of land is a structural mechanism on the landlord's share of the land "
       "flow, as a land value tax is for Georgism (reading 4.5.3)")

U("SG", C45, 0.5,
  [("S", f"far short: one minus the labour share is {FIG['Singapore']}% of GDP (2019), the highest of the configured "
         f"economies after Qatar; the state owns most land and sells 99-year HDB leases at subsidised prices, so "
         f"77.2% of resident households (2025) pay no private landlord, while the transfer to the owners of "
         f"government-linked and foreign firms and to lenders remains (reading 4.5.1)", f"{PWT_S}; {NOTES45}"),
   ("S", "short: residents may quit, with a jobseeker support scheme since 2025 for involuntary job loss only; Work "
         "Permit holders, about a quarter of the workforce, need the current employer's consent to transfer outside a "
         "window before the permit expires, and are outside HDB (reading 4.5.2)", f"MOM, hiring an existing worker; "
         f"TWC2 ({NOTES45})")],
  flag=("0.0: weighting the non-labour share, the highest among market economies in the corpus, and the employer-tied "
        "permits of about a quarter of the workforce as performance far below on both clauses", "4.5.3"),
  note="0.5: HDB removes the private landlord for most residents, a structural mechanism on one relationship type "
       "(reading 4.5.3)")

U("QA", C45, 0.0,
  [("S", f"far short: one minus the labour share is {FIG['Qatar']}% of GDP (2019); net of natural-resource rents "
         f"({FIG['Qatar resource rents 2019 (WB)']}% of GDP) it is still "
         f"{FIG['Qatar non-labour share net of resource rents 2019']}%; the migrant majority's wages are set by a "
         f"sponsorship market, and the rent the state captures is distributed to citizens, about an eighth of "
         f"residents (reading 4.5.1)", f"{PWT_S}; {RENTS}; {NOTES45}"),
   ("S", "far short for the population the protocol counts (residents, non-citizens included, protocol 3.2): since "
         "2020 a migrant worker may change employer without a No Objection Certificate (348,450 changes, November "
         "2020 to August 2022, against about 18,000 in 2019), but residence depends on employment, recruitment debt "
         "is widespread and the ILO records retaliation by employers; citizens' floor (public employment, housing "
         "loans) covers about 12% of residents (reading 4.5.2)", f"ILO (2022), as reported; Law No. 17 of 2020 "
         f"({NOTES45})")],
  flag=("0.5: counting the 2020 reforms' right to change employer, used in some 350,000 changes, as a genuine "
        "non-trivial mechanism on clause 2", "4.5.3"),
  zero="protocol 2.1, third condition: far below on both clauses for the residents the configuration counts -- the "
       "non-labour share is the corpus's highest even net of resource rents, the low-wage migrant majority is "
       "load-bearing for the configuration, and its exit stops at changing sponsor -- with no rule or instrument "
       "in the configuration that removes an extractive relationship (reading 4.5.3)")

U("GEO", C45, 0.5,
  [("S", "short: generalised, the land value tax captures land rent up to its full rental value, removing the "
         "landlord's share of the land flow, but rent on buildings, profit and interest, which George's design "
         "treats as earned returns, stay at the host economy's level, far above 10% of GDP (readings 4.5.1, 4.5.4)",
         "Report v1.6, GEO overview"),
   ("S", "short: the citizen's dividend is unconditional, but the transfers located are a small fraction of a "
         "basic-needs budget, so leaving an employer, landlord or lender is not made survivable by it (reading "
         "4.5.2)", "Report v1.6, GEO C2.2")],
  note="0.5: elimination in one relationship type, the landlord's land rent (reading 4.5.3)")

U("MC", C45, 0.5,
  [("S", "short: generalised, credit created at zero balance and zero interest between members removes the "
         "lender's interest on the credit it replaces; the transfer to employers and landlords is not governed by "
         "the mechanism and stays the host's (readings 4.5.1, 4.5.4)", "Report v1.6, MC overview"),
   ("S", "short: an interest-free credit line is an assured alternative to borrowing from a lender, within its "
         "limit, but it gives no exit from employment or tenancy (reading 4.5.2)", "Report v1.6, MC overview")],
  note="0.5: elimination in one relationship type, creditor-debtor (reading 4.5.3)")

U("IF", C45, 0.5,
  [("S", "short: generalised, the prohibition of interest replaces the loan with profit-and-loss sharing and "
         "sale-based contracts, but wage employment and rent (ijara) are permitted, and the fixed-return "
         "modes (markup sale, tawarruq) are more than 70% of financing in Malaysia and the Middle East, so the "
         "lender's return continues in another form (readings 4.5.1, 4.5.4)",
         "NEEC_IslamicFinance_scoring_scratch.md, Overview"),
   ("S", "short: a debtor in hardship is owed respite and late-payment charges go to charity, a real limit on the "
         "creditor's hold; exit from employment and tenancy is the host's (reading 4.5.2)",
         "NEEC_IslamicFinance_scoring_scratch.md, Overview")],
  flag=("0.0: weighting murabaha's dominance across independent implementations (protocol 4.1, D29(a)) as showing "
        "the creditor-debtor transfer replicated rather than removed, so that no relationship type is eliminated",
        "4.5.3"),
  note="0.5: profit-and-loss sharing is a genuine mechanism on the creditor-debtor relationship (reading 4.5.3)")

U("OS", C45, 0.5,
  [("S", "short: generalised, appropriators governing a common-pool resource pay no rent to an outside owner, and "
         "community land trusts (in scope, D31) remove the landlord's land rent for residents; the transfer to "
         "employers and lenders elsewhere in the economy is not governed (readings 4.5.1, 4.5.4)",
         "NEEC_Ostrom_Commons_scoring_scratch.md, Overview; SCORING_PROTOCOL.md 3.2"),
   ("S", "short: a land-trust resident holds a long ground lease and leaves with a share of the equity; commoners "
         "hold membership; no floor or alternative for employment or credit (reading 4.5.2)",
         "NEEC_Ostrom_Commons_scoring_scratch.md, Overview")],
  note="0.5: elimination in one relationship type for those under commons or trust tenure (reading 4.5.3)")

U("SWF", C45, 0.5,
  [("S", f"short: the fund holds a share of the capital stock and returns its income to the public, by budget rule "
         f"or dividend, so part of the transfer to owners is publicly appropriated; the relationships in the "
         f"economy it is layered onto and in the firms it owns are unmodified, and Norway's non-labour share is "
         f"{FIG['Norway']}% of GDP ({FIG['Norway non-labour share net of resource rents 2019']}% net of resource "
         f"rents, 2019) (readings 4.5.1, 4.5.4)", f"NEEC_SovereignWealthFundStatism_scoring_scratch.md, Overview; "
         f"{PWT_S}; {RENTS}"),
   ("S", "short: Alaska's dividend is universal but small, Norway's model pays none; no exit from employment, tenancy "
         "or credit follows (reading 4.5.2)", "NEEC_SovereignWealthFundStatism_scoring_scratch.md, Overview")],
  flag=("0.0: reading the fund as an owner whose returns are its investee firms' extraction, relocated rather than "
        "removed, so that no relationship type is eliminated (as parts (a) and (b8) read state appropriation)",
        "4.5.3"),
  note="0.5: public appropriation of part of the capital income is a genuine, if partial, mechanism (reading 4.5.3)")

U("MMT", C45, 0.5,
  [("S", "short: the job guarantee's living wage sets a floor under private wages and raises workers' bargaining "
         "power; ownership, rent and lending stay the host's (readings 4.5.1, 4.5.4)", "Report v1.6, MMT overview"),
   ("S", "short: the guaranteed public job is an assured alternative to an extractive employer that is not itself "
         "extractive; tenancy and credit have none (reading 4.5.2)", "Report v1.6, MMT overview")],
  note="0.5: an assured alternative to private employment is a structural mechanism on one relationship type "
       "(reading 4.5.3)")

U("UBS", C45, 0.5,
  [("S", "short: generalised, housing, health, education and transport provided free or decommodified remove the "
         "landlord's rent for those housed and much borrowing for education and health; the transfer to employers "
         "is not governed (readings 4.5.1, 4.5.4)", "NEEC_UniversalBasicServices_scoring_scratch.md, Overview"),
   ("S", "short: services in kind make losing a job less ruinous but give no income, so leaving wage employment is "
         "not survivable on them alone (reading 4.5.2)",
         "NEEC_UniversalBasicServices_scoring_scratch.md, Overview")],
  note="0.5: decommodified housing removes one relationship type for those it houses (reading 4.5.3)")

U("DE", C45, 0.5,
  [("U", "not shown: the framework's 'design to distribute' names redistribution of land, enterprise, money "
         "creation, technology and knowledge, with land value taxes, employee ownership and commons as examples, "
         "but fixes no mechanism and projects no rate (reading 4.5.1)",
         "NEEC_DoughnutEconomics_scoring_scratch.md, Overview; Raworth (2017), ch. 5"),
   ("U", "not shown: no floor or assured alternative is specified (reading 4.5.2)",
    "NEEC_DoughnutEconomics_scoring_scratch.md, Overview")],
  flag=("0.0: reading a framework that names directions but specifies no structural mechanism as 2.1's first "
        "condition", "4.5.3"),
  note="0.5: the framework addresses extraction in principle, by name, without a mechanism of its own")

U("MS", C45, 0.5,
  [("U", "not shown: in worker cooperatives the surplus goes to the worker-members, removing the employer-employee "
         "transfer for them; rent to private landlords and interest to banks remain, which on US proportions would "
         "be about " + f1(B25["rent"] + B25["interest"]) + "% of GDP, but the exemplar hires non-member workers in "
         "its subsidiaries, and the design projects no economy-wide rate (readings 4.5.1, 2.3(b))",
         f"Report v1.6, MS overview; {BEA_S}"),
   ("S", "short: a member may leave with the capital account repaid, and the group's mutual insurance pays "
         "unemployment support and relocates members between cooperatives; tenancy and credit have no exit beyond "
         "the market's (reading 4.5.2)", "Report v1.6, MS overview")],
  note="0.5: elimination in one relationship type, capital-labour, for members (reading 4.5.3)")

U("PE", C45, 1.0,
  [("C", "cleared, projected: no private ownership of productive assets, so no profit, rent or interest income "
         "accrues to owners; households' budgets are an effort rating plus any allowance, and production and "
         "investment are set in the participatory plan (reading 4.5.1)", f"Report v1.6, PE overview; {ATC}"),
   ("C", "cleared: the design keeps no employer, landlord or creditor; besides the effort-rated budget it provides "
         "allowances for those excused from production and a consumption allowance for people who do not want to "
         "work, in effect an unconditional basic income (Wright's statement of the procedure, which Hahnel's reply "
         "keeps as effort rating plus any allowance), so subsistence does not depend on any relationship (reading "
         "4.5.2, as part (b8) read Integral and FALC)", ATC)],
  flag=("0.5: reading the allowance for those who do not want to work as a level the councils set, not one the "
        "design fixes at basic needs (Wright: presumably set to fully meet them), so that refusing participation "
        "may still carry a penalty", "4.5.2"))

U("CCO", C45, 0.5,
  [("S", "short: Public Trust Housing turns 70-80% of a renter's payment into equity and Public Trust Foundations "
         "run essential businesses on a not-for-profit model, removing the owner's and landlord's share where they "
         "operate; the design coexists with private markets ('without ... the dismantling of private markets'), "
         "projects Public Trust Housing at 15-20% of the market within a decade, and taxes labour exploitation at a "
         "higher corporate rate rather than removing it (reading 4.5.1)", HUB),
   ("S", "short: Basic Units, about $1,200 an adult a month, opt-in and restricted to essentials, and the pay-in "
         "pathway out of renting with no deposit or credit check, are real exits where they reach; at the "
         "projected reach of the housing trusts and with a floor near the poverty line, leaving an employer, "
         "landlord or lender is not assured for the population the design serves (reading 4.5.2)", HUB)],
  note="0.5: elimination of the landlord and owner where the trusts operate, within a mixed economy (reading 4.5.3)")

# ---- C3.4 Epistemic Adaptability: the 7 units of part (2.11) ------------------------------------------------------
U("SQ", C34, 0.5,
  [("C", "cleared: core parameters move far beyond 30% without redesign: the federal funds rate from 0.08% to "
         "5.33% in 2022-23, the corporate tax rate from 35% to 21% in 2017 (reading 3.4.1)", f"{FEDX}; {NOTES34}"),
   ("S", f"short: some updates are fast (the CARES Act within a week of the jump in claims), but the "
         f"central bank's first rise came in {FIG['US first federal funds rise']}, {MONTHS} months after CPI-U "
         f"inflation first exceeded 4% ({FIG['US CPI-U first above 4% year on year']}), and much legislation "
         f"waits on divided government (reading 3.4.2)", f"{FEDX}; {NOTES34}"),
   ("C", "cleared: agency rules can be set aside by independent courts at the suit of those affected (5 U.S.C. "
         "706), statutes reviewed for constitutionality, and their authors removed in free elections (reading "
         "3.4.3)", NOTES34),
   ("S", "short: the deregulation of thrifts in 1980 and 1982 preceded the savings and loan crisis, at about $124 "
         "billion to taxpayers, and the financial crisis of 2007-09 followed decades of deregulation the Financial "
         "Crisis Inquiry Commission named among its causes: systemic banking crises caused by changes to the "
         "configuration's own credit parameters (reading 3.4.4, as part (b1) read the Nordic crises)", NOTES34)])

U("CN", C34, 0.5,
  [("C", "cleared: the birth limit moved from one child to two (2016) and three (2021), and monetary, credit and "
         "registration parameters are adjusted often, without redesign (reading 3.4.1)", NOTES34),
   ("S", "short: the 2008 stimulus came within two months, but zero-COVID was held for about a year after the "
         "evidence on Omicron and vaccines and the one-child rule for decades after fertility fell below "
         "replacement (reading 3.4.2)", NOTES34),
   ("S", "short: administrative suits exist, but the courts answer to the Party's political-legal commissions and "
         "no election is free, so no route to reversal is independent of those who made the change (reading "
         "3.4.3)", NOTES34),
   ("S", "short: the abrupt end of zero-COVID on 7 December 2022 was followed by about 1.87 million excess deaths "
         "among those aged 30 and over within two months, and the 'three red lines' (August 2020) by the "
         "developers' defaults from December 2021 (reading 3.4.4)", NOTES34)])

U("QA", C34, 0.5,
  [("C", "cleared: in 2020 the labour market's core parameters were reset without redesigning the state: a minimum "
         "wage where none existed and employer consent removed from job changes, which rose about tenfold a "
         "year (reading 3.4.1)", f"{NOTES34}; {NOTES45}"),
   ("S", "short: the labour reforms came six years after the 2014 complaint to the ILO and seven after the 2013 "
         "reporting on migrant workers' deaths and unpaid wages (reading 3.4.2)", NOTES34),
   ("S", "short: the Emir holds executive and legislative power, judges are appointed by Emiri order, and the "
         "elected seats of the Shura Council were abolished by the referendum of November 2024; the migrant "
         "majority has labour dispute committees, not a route to reversing a law (reading 3.4.3)", NOTES34),
   ("C", "cleared: stated search: no collapse caused by a parameter adjustment located; the 2015-17 fiscal "
         "adjustment to the oil price fall and the 2017-21 blockade were absorbed (reading 3.4.4)", NOTES34)])

U("CPS", C34, 0.0,
  [("S", "short: state retail prices of staple foods were held from 1962 to 1991 against "
         "mounting shortage; each substantive change to allocation rules came as a reorganisation (the regional "
         "councils of 1957, undone in 1965; the 1965 reform, wound back; the Law on State Enterprise, 1987), so "
         "the range adjustable without redesign was narrow (reading 3.4.1)", NOTES34),
   ("S", "short: Lysenko's doctrine governed Soviet biology from 1948 to 1964 against the evidence of genetics, and "
         "price reform waited decades on the evidence of shortage (reading 3.4.2)", NOTES34),
   ("S", "short: no route to reversal ran outside the Party: no independent courts, no free elections; challenge "
         "took the form of strikes met with force (Novocherkassk, 1962; the Baltic coast, 1970) (reading 3.4.3)",
         NOTES34),
   ("S", "short: Poland's food price rises of 1970, 1976 and 1980 each brought strikes, the first two were reversed "
         "and the third produced Solidarity; the Soviet reforms of 1987-88 preceded the collapse of 1989-91 "
         "(reading 3.4.4)", NOTES34)],
  flag=("0.5: counting the plan's capacity to move administrative parameters (investment shares, procurement "
        "prices) as clause 1 cleared, and Hungary's New Economic Mechanism of 1968 as adjustment without collapse",
        "3.4.5"),
  zero="protocol 2.1, third condition, with D29(a): performance far below the threshold on every clause, documented "
       "in several independent implementations (the Soviet Union, Poland), with no credible pathway under the "
       "system's own logic -- its adjustments of core parameters ended in unrest or collapse (reading 3.4.5)")

U("FALC", C34, 0.0,
  [("U", "not shown: the design names no parameters of its own or a procedure to adjust them (reading 3.4.1)",
    f"Report v1.6, FALC overview, C2.4 and C4.4; {NOTES34}"),
   ("U", "not shown: no rule of review or update is stated (reading 3.4.2)", "Report v1.6, FALC C2.4"),
   ("U", "not shown: who controls production and decides priorities is left unresolved, so no route to challenge a "
         "change is specified (reading 3.4.3)", "Report v1.6, FALC C2.4 and C4.4"),
   ("U", "not shown: no implementation and no modelling of an adjustment (reading 3.4.4)", "Report v1.6, FALC C5.1")],
  flag=("0.5: reading the programme as enacted through the democratic institutions it assumes (Bastani's luxury "
        "populism), whose legislatures and courts would supply clauses 1 to 3 slowly, the 0.5 band", "3.4.5"),
  zero="protocol 2.1, first condition: no structural mechanism addresses the criterion -- the design specifies no "
       "procedure by which its rules or parameters are adjusted, by whom, or how a change is contested; its own "
       "scoring records its governance as largely unspecified (Report v1.6, FALC C2.4 and C4.4) (reading 3.4.5)")

U("INT", C34, 0.5,
  [("C", "cleared: ITC's weighting bands, scarcity coefficients and access-valuation parameters are recalibrated "
         "within democratically approved bounds; the white paper's example raises an ecological weight to 1.7-1.8 "
         "in drought, a move of 70-80% (reading 3.4.1)", WPX),
   ("C", "cleared, as designed: ITC parameters are recalibrated continuously, and CDS Module 10 opens a review "
         "when FRS signals or new evidence show outcomes diverging, its example acting on detection six months "
         "after a decision (reading 3.4.2)", WPX),
   ("C", "cleared, as designed: Module 1 takes proposals and objections from participants, decisions are reached "
         "by participants' weighted consensus with blocking objections detected, and Module 10 can amend, revoke "
         "or reopen a decision: there are no officials on whom the route depends (reading 3.4.3)", WPX),
   ("U", "not shown: no implementation record of a parameter adjustment and no modelling of the design's own "
         "adjustments in operation; the white paper describes drift detection, not a test (reading 3.4.4, as part "
         "(b1) read Participatory Economics and Degrowth)", WPX)],
  flag=("1.0: reading the design's bounded recalibration, review loop and early drift detection as the 1.0 band's "
        "clearly-designed capacity for adjustment without destabilisation, so clause 4 is cleared as designed",
        "3.4.4"),
  note="0.5: clause 4 not shown (reading 3.4.4)")

U("LM", C34, 0.5,
  [("S", "short: the state's scope is fixed on principle to protecting property, enforcing contracts and defence; "
         "money, regulation and transfers are not parameters it may adjust, so moving them is redesign (reading "
         "3.4.1)", "Report v1.6, LM overview"),
   ("S", "short: evidence of a market failure does not call for a policy update under the entry's principles "
         "(reading 3.4.2)", "Report v1.6, LM overview; criteria.json, C3.4 anchors"),
   ("C", "cleared: independent courts under a constitution of limited powers, the minimal state's core function, "
         "let those affected challenge a change and have it set aside (reading 3.4.3)", "Report v1.6, LM overview"),
   ("U", "not shown: no implementation of the design and no modelling of an adjustment (reading 3.4.4)",
    "Report v1.6, LM overview")],
  flag=("0.0: reading the rights-fixed scope as excluding evidence-based adjustment of the system's rules as "
        "illegitimate, 2.1's second condition", "3.4.5"),
  note="0.5: clause 3 is cleared, so 2.1's 0.0 cannot hold with it (decision 53.2)")


# ---- the blind record --------------------------------------------------------------------------------------------
def blind_table(p):
    rows = ["| Unit | Criterion | Clause statuses | Verdict | Flag |", "|---|---|---|---|---|"]
    for (code, cid) in sorted(NEW, key=lambda k: (k[1] != C45, p.names[k[0]])):
        r = NEW[(code, cid)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        rows.append(f"| {p.names[code]} | {cid} | {sts} | {pc.f1(r['verdict'])}{' (0.0 reason stated)' if r['zero'] else ''} "
                    f"| {flag} |")
    return "\n".join(rows)


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s71.py -- the blind re-read of C4.5 and C3.4 (ledger S54; decisions 69.1, 69.2)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    prior_mod = p.mods[p.tags.index(br.PRIOR[C45])]
    print("inputs: blind_review.py, pass_common.py and its parts, " + ", ".join(
        sorted({PWT, BEA, RENTS, SDG, SE43B, ATC, HUB, WPX, FEDX})) + "\n")

    print("[1] the blind readings are complete and follow the rules")
    keys = {k for k in prior_mod.UNITS if k[1] in (C45, C34)}
    ok_print(set(NEW) == keys, f"one blind reading for each of part (2.11)'s {len(keys)} units of C4.5 and C3.4, "
             f"no more", str(sorted(set(NEW) ^ keys)))
    ok_print(br.PRIOR[C45] == br.PRIOR[C34] == "(2.11)", "both criteria's prior units are part (2.11)'s")
    pc.check_records(p, NEW, ok_print)
    pc.check_rule(NEW, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in NEW.values()), "each flag names an alternative score other than the verdict")
    ok_print(all(all(st not in "CM" for st, _, _ in r["clauses"]) for r in NEW.values() if r["verdict"] == 0.0),
             "no 0.0 has a cleared or moot clause")
    for (code, cid) in sorted(NEW):
        view = br.blind_view(p, (code, cid))
        if len(view["clauses_v2"]) != len(NEW[(code, cid)]["clauses"]):
            ok_print(False, f"{code} {cid}: clause count differs from blind_view")
    ok_print(all(EC + cid + "/" + f in (PWT, BEA, RENTS, SDG, SE43B, ATC, HUB, NOTES45, WPX, FEDX, NOTES34)
                 for cid in (C45, C34) for f in br.blind_view(p, ("SQ", cid))["cache_files"]),
             "every file blind_view lists for the two criteria is one this script reads or names")

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG.items():
        print(f"    {k}: {v}")

    print("\n[3] the blind readings (verdicts, clause statuses, flags)")
    print(blind_table(p))
    n45 = [r["verdict"] for (c, cid), r in NEW.items() if cid == C45]
    n34 = [r["verdict"] for (c, cid), r in NEW.items() if cid == C34]
    print(f"\nC4.5: {n45.count(1.0)} at 1.0, {n45.count(0.5)} at 0.5, {n45.count(0.0)} at 0.0; "
          f"C3.4: {n34.count(1.0)} at 1.0, {n34.count(0.5)} at 0.5, {n34.count(0.0)} at 0.0; "
          f"{sum(1 for r in NEW.values() if r['flag'])} flagged")
    print("\nBLIND READINGS RECORDED." if ok else "\nBLIND READINGS: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
