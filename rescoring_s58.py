#!/usr/bin/env python3
"""
rescoring_s58.py -- NEEC rescoring pass, stage 2, group 2.6: C5.2 Staged Transition Pathways, class M
=====================================================================================================
Session 58. The 16 units of C5.2 the pass had not re-estimated are re-read clause by clause against v2.0's text
(criteria.json; NEEC_Criteria_v2_s45.md, Appendix V), which keeps the five Session 44 clauses and places all five under
the scope "each shown feasible by precedent or component evidence". Part (b9) (rescoring_s50.py, NEEC_Rescoring_s50.md)
read the seven published 1.0s and set the reading of that scope (its reading 3.2(b)); this group applies it to the
13 units at 0.5 and the three at 0.0. Before the group, the owner's decision 58.1 (ledger d37) restores CCO-PTF-CIP-SZH's
C3.2 to 1.0 as its own part of the pass (owner_s58.py, part "58.1"); this script checks that part too. Readings:
NEEC_Rescoring_s58.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [0] the owner's part 58.1: its place in the pass, its one unit, the unit it supersedes, its figures in the runs'
      capture, and what it changes
  [1] the group: one unit per entry not yet re-estimated on C5.2, each against its published score; which rise, fall
      or hold; the 0.0s and their reasons; the units at 1.0; the clauses not estimated and the clause that fixes each
  [2] the dates and figures the readings derive (the precedents' stages and their spans), recomputed from those held
  [3] the flags
Sources not in this repository are named with their identifiers; every figure used from them is held below.

Usage: python3 rescoring_s58.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, cco_sim_v56_checks_s57_output.txt,
                                             NEEC_Rescoring_s58.md; writes nothing)
       python3 rescoring_s58.py --tables   (prints the generated tables as JSON, for the record)
Prints file names and summaries only. Deterministic.
"""
import datetime
import hashlib
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD, CRIT, OWNER_TAG = "(2.6)", "NEEC_Rescoring_s58.md", "C5.2", "58.1"
SIMOUT, SIMMD5 = "cco_sim_v56_checks_s57_output.txt", "cd2ec0c978e68aeffaf57029bd12932a"
UNITS = {}
GENERATED = {}


def U(code, verdict, clauses, flag=None, note="", zero=None):
    """One unit of C5.2. clauses: five (status, estimate, source) in v2.0's order. flag: (alternative, reading).
    zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note, zero=zero)


def notest(n):
    """A clause not estimated because clause(s) n fix the verdict (part (b9)'s form, NEEC_Rescoring_s50.md section 2)."""
    return ("U", f"not estimated in this pass; the verdict is fixed by clause {n}", f"this unit's clause {n}")


# ---- dates and figures held (readings 3.2 to 3.6) --------------------------------------------------------------------
D = datetime.date
TIMOR = {"comments_due": D(2004, 11, 30), "law": D(2005, 8, 3), "first_investment": D(2005, 9, 9),
         "independence": D(2002, 5, 20), "first_usd_m": 79.6, "norad_nok_m": 56}
NORWAY = {"act": 1990, "first_transfer": 1996, "equities_40": (1997, 1998), "nbim": 1998, "fiscal_rule": 2001,
          "ethics": 2004, "equities_60": (2007, 2009), "rule_3pct": 2017}
QUEBEC = (1997, 1998, 1999, 2000)                 # $5-a-day places: age 4, age 3, age 2, all under 5 not in kindergarten
CANADA_NATIONAL = 2021
ACT = {"start": 2012, "deadline": 2032, "conveyance_share_2029_30": 10, "rates_share_from_2025_26": 29}
KERALA = {"launch": "August 1996", "share": "35 to 40%", "wards": 14147, "people_m": 31}
INT_SITE = {"registered": 4, "phase": "Phase 1"}
INT_STAGES = ("marginal experiment", "supplementary alternative", "essential support layer", "dominant substrate")


def months(a, b):
    return (b.year - a.year) * 12 + (b.month - a.month)


FIGS = {"timor_months": months(TIMOR["comments_due"], TIMOR["first_investment"]),
        "timor_law_months": months(TIMOR["law"], TIMOR["first_investment"]),
        "norway_stages": len([NORWAY["act"], NORWAY["first_transfer"], NORWAY["nbim"], NORWAY["fiscal_rule"]])}

# ---- sources -------------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
SCOPE = "(reading 3.2)"
WP = ("Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; PDF md5 a6defc9a, "
      "retrieved 2026-10-15)")
SITE = "integralcollective.io, home and community pages, retrieved 2026-10-15"
REVIEW = "Integral_NEEC_Review.md, C5.2"
KORNAI = ("Kornai, The Socialist System: The Political Economy of Communism (Princeton, 1992), chapter 2, the "
          "revolutionary-transitional system")
NBIM = "Norges Bank Investment Management, The history (nbim.no, retrieved 2026-10-15)"
FISCAL = ("Ministry of Finance, The Norwegian Fiscal Policy Framework (regjeringen.no, retrieved 2026-10-15), and its "
          "press release of 16 February 2017 on the expected rate of return")
TL_LAW = ("Timor-Leste, Petroleum Fund Law No. 9/2005, promulgated 3 August 2005; Petroleum Fund of Timor-Leste, Annual "
          "Report 2008 (first investments of 9 September 2005); La'o Hamutuk, the Ministry of Planning and Finance's "
          "public consultation on the fund (comments due 30 November 2004)")
NORAD = ("Norad, Review of TIM 2010: Assistance in developing the management of the petroleum sector in Timor-Leste "
         "(2007), on Norway's assistance since 2002 (about NOK 56 million, 2002-2007)")
RSIS = "RSIS Commentary CO18026, Timor-Leste's Oil: Blessing or Curse? (15 February 2018)"
SWFDOC = "NEEC_SovereignWealthFundStatism_scoring_scratch.md, "
QC_SRC = ("Baker, Gruber and Milligan, Universal Child Care, Maternal Labor Supply, and Family Well-Being, NBER Working "
          "Paper 11832 (2005; Journal of Political Economy, 2008), as summarised in the NBER Digest, June 2006")
UBSDOC = "NEEC_UniversalBasicServices_scoring_scratch.md, "
BRITAIN = "the British National Insurance Act 1946 and National Health Service Act 1946, in force 5 July 1948"
GEODOC = "NEEC_Georgism_LVT_scoring_scratch.md, "
ACT_SRC = ("ACT Treasury, Tax Reform (treasury.act.gov.au/taxreform, retrieved 2026-10-15); Pegasus Economics' review for "
           "the Legislative Assembly's estimates committee, as reported in The Canberra Times, 3 July 2026")
MCDOC = "NEEC_MutualCredit_LETS_scoring_scratch.md, "
DEDOC = "NEEC_DoughnutEconomics_scoring_scratch.md, "
CNDOC = "NEEC_StateCapitalism_China_scoring_scratch.md, "
SGDOC = "NEEC_StateCapitalism_Singapore_scoring_scratch.md, "
QADOC = "NEEC_StateCapitalism_Qatar_scoring_scratch.md, "
OSDOC = "NEEC_Ostrom_Commons_scoring_scratch.md, "
KER_SRC = ("Isaac with Franke, Local Democracy and Development: The People's Campaign for Decentralized Planning in "
           "Kerala (LeftWord, 2000; Rowman and Littlefield, 2002)")

# ---- the units (readings in NEEC_Rescoring_s58.md, section 3) --------------------------------------------------------
U("CPS", 0.0, [
    ("U", "no gradual transition to comprehensive central planning in a stable context is located: every transition to "
          "the configuration followed a seizure of power by force, by revolution and civil war (Russia, 1917-1921; "
          "China, 1949), by occupation (Eastern Europe, 1945-1949) or by a coup (Czechoslovakia, February 1948); the "
          "later stages of each, the five-year plans and collectivisation, rest on it (readings 3.2(a), 3.5)",
     f"{REP}System 3, C5.2; {KORNAI}"),
    ("U", "the configuration was imposed within 36 months more than once (Soviet collectivisation from 1929; the "
          "nationalisations in Eastern Europe after 1945), but each deployment rested on a seizure of power by force, "
          "which the criterion's rationale names as what a pathway is to avoid, and none was a deployment a polity "
          "could adopt by its own procedures (readings 3.2(a), 3.5)", f"{REP}System 3, C5.2; {KORNAI}"),
    ("U", "the five-year plans set dated targets, but in deployments that rest on force; no milestone of a pathway the "
          "criterion credits is located (reading 3.5)", f"{REP}System 3, C5.2; {KORNAI}"),
    ("U", "no statement of what a transition into the configuration takes, other than the seizure of power, is "
          "located (reading 3.5)", f"{REP}System 3, C5.2"),
    ("U", "the entry's record shows rapid implementation 'invariably chaotic', and no mitigation of a transition's "
          "risks is stated or located (reading 3.5)", f"{REP}System 3, C5.2")],
  flag=("0.5: read as counting a deployment by any means, the rapid clause is cleared by the Soviet and Eastern "
        "European nationalisations, each within 36 months", "3.5"),
  zero="every transition to the configuration located required non-gradual means, revolution, civil war, a coup or "
       "occupation (the 0.0 band's own example); no pathway the criterion credits exists to be shown feasible",
  note="the 0.0 band's anchor example; it holds")

U("MS", 0.5, [
    ("U", "the entry's pathway is incremental cooperative development; its component has grown in stages at a region's "
          "scale (Mondragón from 1956), but no stage beyond a niche is located from a market economy, and the one "
          "economy-wide deployment of worker self-management in markets, Yugoslavia's (in stages from 1950 to 1976), "
          "began from capital nationalised after a revolution (readings 3.2(a), 3.6)", f"{REP}System 4, C5.2"),
    ("U", "the entry states no rapid pathway, and no deployment of a cooperative sector at an economy's scale within 36 "
          "months is located (reading 3.6)", f"{REP}System 4, C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="the 0.5 band's anchor example; it holds: a pathway is sketched and its first stage has deployments of its kind, "
       "so the unit is not 0.0 (reading 3.2(f))")

U("UBI", 0.5, [
    ("U", "the entry's pathway is to begin with a partial basic income and scale it upward; no such scaling in stages is "
          "located: the one long-running universal payment, Alaska's dividend (paid every year since 1982), follows "
          "the fund's earnings and the legislature's appropriation, not a schedule toward a full basic income "
          "(reading 3.6)", f"{REP}System 7, C5.2; {SWFDOC}overview"),
    notest(1), notest(1), notest(1), notest(1)],
  note="a pathway is sketched and its first stage, a universal payment, has been deployed, so the unit is not 0.0 "
       "(reading 3.2(f)); clause 2 is not estimated (section 8)")

U("DG", 0.5, [
    ("U", "the entry names municipal experiments, bioregional organisation and voluntary simplicity as pathways; no "
          "polity located has deployed a planned contraction of output in stages, and the experiments named are "
          "local (reading 3.6)", f"{REP}System 8, C5.2"),
    ("U", "the entry states no rapid pathway, and the transition it describes faces 'massive political and economic "
          "disruption'; none is located (reading 3.6)", f"{REP}System 8, C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="a pathway is sketched and its first stage has deployments of its kind, so the unit is not 0.0 (reading 3.2(f))")

U("FALC", 0.0, [
    ("U", "no pathway is specified: the entry's destination rests on technologies not yet developed (general artificial "
          "intelligence, abundant clean energy and storage) together with a political transformation, and no stage of "
          "deployment of that destination is located or possible before they exist (reading 3.5)",
     f"{REP}System 10, C5.2"),
    ("U", "no rapid pathway is stated, and none can be deployed before the technologies exist (reading 3.5)",
     f"{REP}System 10, C5.2"),
    ("U", "no milestones are stated (reading 3.5)", f"{REP}System 10, C5.2"),
    ("U", "no resource requirements are stated (reading 3.5)", f"{REP}System 10, C5.2"),
    ("U", "no risk mitigation for a transition is stated (reading 3.5)", f"{REP}System 10, C5.2")],
  zero="no structural mechanism addresses the criterion: 'fully automated' is a destination without a roadmap, whose "
       "defining condition cannot be deployed by any pathway until technologies not yet developed exist",
  note="one of the 0.0s the published C5.2 count names; it holds")

U("PE", 0.5, [
    ("S", "three levels, municipal, regional and national, against at least four, stated as a theoretical possibility; "
          "no deployment of participatory planning of production is located at any level; its nearest components have "
          "deployments at the first levels' scale only: participatory budgeting of a share of municipal investment "
          "(Porto Alegre from 1989) and the Kerala People's Campaign, which devolved 35 to 40% of a state's plan funds "
          "to local planning from August 1996 (reading 3.6)", f"{REP}System 11, C5.2; {KER_SRC}"),
    ("U", "the entry states no rapid pathway, and holds that coordination complexity makes partial implementation "
          "difficult and that planning needs critical mass; no deployment within 36 months is located (reading 3.6)",
     f"{REP}System 11, C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="read closely, since with first place shared Participatory Economics' C5.2 could decide it; a pathway is "
       "sketched in levels and its first stage's components have deployments at municipal and state scale, so the unit "
       "holds at 0.5 and is not 0.0 (reading 3.2(f))")

U("INT", 0.5, [
    ("U", "the design's white paper, published after the corpus scored it, now states a staged pathway: proto-nodes "
          "grown from existing mutual aid networks, timebanks, tool libraries and repair cafés, each of the five "
          "systems formalised in three steps, and an arc of four stages, from marginal experiment to supplementary "
          "alternative, essential support layer and dominant substrate, 'inherently generational' and undated; its "
          "first stage's kind is deployed, but no node operating the design's systems is located: the project's site "
          "registers four communities in its own Phase 1, the building of its software (reading 3.3)",
     f"{WP}, sections 11.1 to 11.4 and 11.11; {SITE}"),
    ("U", "the white paper sets aside direct implementation in a nation-state as 'highly unlikely' and states no rapid "
          "pathway; none is located (reading 3.3)", f"{WP}, section 11.1"),
    ("U", "no milestones are stated: the transition's markers are 'incremental and often unremarkable' (reading 3.3)",
     f"{WP}, section 11.11"),
    ("U", "no resource requirements are stated; interface cooperatives take in external resources, without a figure "
          "(reading 3.3)", f"{WP}, sections 11.5 and 11.6"),
    ("C", "section 11.10 specifies safeguards of kinds in use elsewhere: no single point of failure, peer-to-peer and "
          "federated infrastructure with replicated data, grounded in deployed technologies (decentralised identifiers, "
          "content-addressed storage, federated messaging); no central treasury; commons assets that cannot be "
          "pledged or sold; legal compliance as the default; and interface cooperatives with capped market exposure "
          "and sunset rules; component evidence in the sense of reading 3.2, as CCO-PTF-CIP-SZH's risk mitigation was "
          "cleared in part (b9) (reading 3.3)", f"{WP}, sections 11.6 and 11.10")],
  flag=("0.0: read on the source the corpus scored, the review's document, whose stated pathway is 'starts small and "
        "expands' (the 0.0 band's example), and setting aside a design document published after the scoring", "3.3"),
  note="re-read on the design's own white paper (v0.1, December 2025), as parts (b5) and (b8) read the design's own "
       "pages; the published 0.0's reason, that the source provides no phased pathway, no longer describes the design, "
       "and a clause is cleared, so 0.0 cannot hold (decision 53.2); read closely, since Integral's C5.2 could decide "
       "who is first")

U("GEO", 0.5, [
    ("S", "the precedent the entry cites, the Australian Capital Territory's 20-year shift from conveyance duty to "
          "general rates, has run in annual budget steps since 2012 with published evaluations, but it is not shown "
          "to completion: a review for the Legislative Assembly's estimates committee finds abolition by the 2032 "
          "deadline 'extremely unlikely', the substitution having come to 'a complete stop', with conveyance duty "
          "still about 10% of own-source revenue in 2029-30 (reading 3.6)", f"{GEODOC}C5.2; {ACT_SRC}"),
    ("U", "no rapid pathway is located, and the one fast introduction, Britain's of 1910, is the entry's clearest "
          "failure case (reading 3.6)", f"{GEODOC}C5.2; {REP}System 14, C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="the staged clause, which the published rationale credited, is now short on the precedent's own record")

U("MC", 0.5, [
    ("U", "no deployment in dated stages is located: classic LETS, WIR, Sardex and Grassroots Economics each started "
          "small and grew without a multi-phase design; the Credit Commons federation effort is a design, early-stage "
          "and untested at scale, and a plan shows nothing under the scope (reading 3.6)", f"{MCDOC}C5.2"),
    ("U", "Argentina's barter networks scaled within months in the 2001-2002 crisis and then collapsed: the pace is "
          "shown, not the feasibility of a deployment that reaches stable operation (reading 3.2(c))",
     f"{MCDOC}C5.2 and C3.1"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  flag=("0.0: the register's flag, since the staged design effort has not been tested against the failure modes it is "
        "meant to solve", "3.6"),
  note="the mechanism has operated for decades in its networks (WIR since 1934), so the unit is not 0.0 (reading "
       "3.2(f)); the register's flag toward 0.0 is kept")

U("DE", 0.5, [
    ("U", "a first-stage methodology, the City Portrait process, has been followed in dozens of jurisdictions, but no "
          "stage beyond the initial portrait and strategy is specified or located (reading 3.6)", f"{DEDOC}C5.2"),
    ("U", "no rapid pathway exists: Amsterdam's adoption in the pandemic reused an existing planning process (reading "
          "3.6)", f"{DEDOC}C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="a first stage is deployed in many places, so the unit is not 0.0 (reading 3.2(f))")

U("UBS", 0.5, [
    ("C", f"component evidence: Quebec's universal childcare was deployed in four dated stages, to four-year-olds in "
          f"{QUEBEC[0]}, three-year-olds in {QUEBEC[1]}, two-year-olds in {QUEBEC[2]} and all children under five not "
          f"in kindergarten in {QUEBEC[3]}, and was the model for Canada's national programme from {CANADA_NATIONAL}; "
          "the entry's pathway is sector by sector (reading 3.6)", f"{UBSDOC}C5.2; {QC_SRC}"),
    ("U", "the entry states no rapid pathway; one sector has a precedent of rapid deployment (Britain's national health "
          "service, legislated in 1946 and in force by July 1948), but no deployment of the package of universal "
          "services within 36 months is located (reading 3.6)", f"{UBSDOC}C5.2; {BRITAIN}"),
    notest(2), notest(2), notest(2)],
  note="the staged clause is cleared on one sector's staged deployment, as part (b9) cleared Stakeholder Capitalism's "
       "on one component's; the rapid clause fixes the verdict")

U("SWF", 1.0, [
    ("C", f"the mechanism's own deployment, in at least four dated stages in Norway: the fund's law ({NORWAY['act']}), "
          f"its first capital transfer ({NORWAY['first_transfer']}), the investment manager and a 40% equity share "
          f"({NORWAY['nbim']}), and the fiscal rule tying spending to the fund's expected real return "
          f"({NORWAY['fiscal_rule']}) (reading 3.4)", f"{NBIM}; {FISCAL}"),
    ("C", f"a precedent of the same kind in a post-crisis context: Timor-Leste, independent in 2002 after the violence of "
          f"1999, put its petroleum fund out to public consultation (comments due 30 November 2004), promulgated its "
          f"law on 3 August 2005 and made the fund's first investments on 9 September 2005, "
          f"{FIGS['timor_months']} months from the consultation's close (reading 3.4)", f"{TL_LAW}; {SWFDOC}C5.2"),
    ("C", f"dated targets were set and met: a 40% equity share decided in {NORWAY['equities_40'][0]} and reached in the "
          f"first half of {NORWAY['equities_40'][1]}; 60% decided in {NORWAY['equities_60'][0]} and reached in June "
          f"{NORWAY['equities_60'][1]}; the fiscal rule's expected return revised from 4% to 3% in "
          f"{NORWAY['rule_3pct']} (reading 3.4)", f"{NBIM}; {FISCAL}"),
    ("C", f"what the deployments took is documented: the capital, the revenue stream transferred into the fund (in "
          f"Timor-Leste, USD {TIMOR['first_usd_m']} million from the Timor Gap Account at the first investment), and "
          f"the institution to manage it, built in Timor-Leste with Norway's assistance from 2002, about NOK "
          f"{TIMOR['norad_nok_m']} million to 2007, whose advisers were 'instrumental to the establishment of the "
          f"petroleum fund and its operations' (reading 3.4)", f"{TL_LAW}; {NORAD}"),
    ("C", "the deployments' mitigations operated: assets invested abroad only, a spending rule tying transfers to the "
          "expected real return (Norway) or to 3% of petroleum wealth (Timor-Leste), ethical guidelines from 2004; "
          "Norway's fund has been kept and has grown to more than four times mainland GDP under the rule, though "
          "Timor-Leste's parliament approved withdrawals above its rule in most years from 2008 (reading 3.4)",
     f"{NBIM}; {FISCAL}; {RSIS}; {SWFDOC}overview")],
  flag=("0.5: read as requiring the pathway to be shown feasible where no large non-recurring revenue exists, the "
        "resource clause is not shown (New Zealand's budget-funded fund suspended its contributions from 2009 to "
        "2017), and Timor-Leste's repeated withdrawals above its rule leave the risk clause resting on Norway alone",
        "3.4"),
  note="every clause is shown by deployments of the mechanism itself, which the published 0.5, judged on the absence "
       "of a phase-by-phase plan, did not credit; under v2.0's scope a precedent, not a plan, is the test (part (b9), "
       "reading 3.2)")

U("CN", 0.5, [
    ("U", "the reform sequence is one of the best-documented staged transitions, local experiments first and national "
          "policy after, sector by sector from 1978, and Vietnam adapted it; but each runs from a party-state that came "
          "to power by revolution and civil war, which the entry names as defining, and no polity located has reached "
          "the configuration by stages from a pluralist starting point (readings 3.2(a), 3.6)", f"{CNDOC}C5.2"),
    ("U", "no rapid pathway is stated or located (reading 3.6)", f"{CNDOC}C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="a staged sequence of the configuration's market components is real and replicated, so the unit is not 0.0 "
       "(reading 3.2(f))")

U("SG", 0.5, [
    ("U", "parts of the model have documented, sequenced histories (Temasek's incorporation in 1974 from existing state "
          "holdings, the privatisation programme of 1985-1987, the transfer of administrative know-how to Suzhou), "
          "but they are stages of components, not four stages of the configuration, and its political precondition "
          "was secured by Operation Coldstore's detentions without trial in 1963, an episode whose purpose historians "
          "contest (reading 3.6)", f"{SGDOC}C5.2"),
    ("U", "no rapid pathway is stated or located; the pathway unfolded over decades in a city-state (reading 3.6)",
     f"{SGDOC}C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="documented sequences and a demonstrated transfer method, so the unit is not 0.0 (reading 3.2(f))")

U("QA", 0.5, [
    ("U", "Qatar's multi-phase plans (the National Vision 2030 and three national development strategies, the third for "
          "2024-2030) develop a configuration already in place; they are not a pathway into it, and its precondition, "
          "large resource rents per citizen, cannot be deployed (reading 3.6)", f"{QADOC}C5.2"),
    ("U", "no rapid pathway exists (reading 3.6)", f"{QADOC}C5.2"),
    notest("1 and 2"), notest("1 and 2"), notest("1 and 2")],
  note="documented staged planning of the configuration itself, so the unit is not 0.0 (reading 3.2(f))")

U("OS", 0.5, [
    notest(2),
    ("U", "the framework declines to be a deployment plan; the national programmes that handed resources to commons "
          "did so over decades (Nepal's community forestry under the Forest Act 1993 and Regulation 1995, to more than "
          "22,000 groups; India's Joint Forest Management), and no deployment within 36 months is located (reading "
          "3.6)", f"{OSDOC}C5.2"),
    notest(2), notest(2), notest(2)],
  flag=("0.0: the register's flag, on the reading that the framework's own refusal to specify a pathway governs, and "
        "that national forestry statutes implement policy rather than the scored mechanism", "3.6"),
  note="national programmes deployed the mechanism in stages, so the unit is not 0.0 (reading 3.2(f)); clause 1, "
       "which those programmes bear on, is not estimated, since clause 2 fixes the verdict; the register's flag toward "
       "0.0 is kept")

EXPECT = {"rise": ["INT", "SWF"], "fall": [], "zero": ["CPS", "FALC"], "ones": ["SWF"],
          "flags": {"CPS": "3.5", "INT": "3.3", "MC": "3.6", "SWF": "3.4", "OS": "3.6"},
          "before": ["SQ", "NSD", "LM", "MMT", "SC", "CCO", "IF"], "notest": 38}


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    tags = [t for t, _, _, _ in pc.PARTS]
    idx, io_ = tags.index(TAG), tags.index(OWNER_TAG)
    with redirect_stdout(io.StringIO()):
        p = pc.Pass(upto=idx)
        p_before = pc.Pass(upto=io_)
    print(f"NEEC rescoring pass, stage 2, group 2.6: C5.2 Staged Transition Pathways, class M ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{SIMOUT}, {RECORD}\n")

    print("[0] THE OWNER'S DECISION 58.1 (ledger d37), PART 58.1")
    om = p.mods[io_]
    key = ("CCO", "C3.2")
    old = p_before.merged[key]
    check(tags[io_ - 1] == "(2.5)" and io_ + 1 == idx and list(om.UNITS) == [key],
          f"part {OWNER_TAG} follows group 2.5 and precedes this group, with one unit, {key[0]} {key[1]}")
    new = om.UNITS[key]
    check(p_before.part_of[key] == "(2.5)" and old["verdict"] == 0.5 and new["verdict"] == 1.0
          and all(st == "C" for st, _, _ in new["clauses"]) and len(new["clauses"]) == len(old["clauses"]) == 3
          and p.part_of[key] == OWNER_TAG and p.merged[key] is new,
          "it restores the published 1.0 (every clause cleared on the owner's reading) and supersedes group 2.5's 0.5 "
          "(decision 57.7), whose script and record are unchanged")
    raw = open(os.path.join(HERE, SIMOUT), "rb").read() if os.path.isfile(os.path.join(HERE, SIMOUT)) else b""
    txt = raw.decode("utf-8")
    rows = (f"| Reference | 0% | Compassionism, H1 (a = 1) | {om.FIG['full']} |",
            f"| Reference | 0% | Compassionism, release row (a = 0) | {om.FIG['main']} |")
    check(hashlib.md5(raw).hexdigest() == SIMMD5 and all(r in txt for r in rows)
          and om.FIG["full"] in new["clauses"][0][1] and om.FIG["main"] in new["flag"][0],
          f"{SIMOUT} md5 {hashlib.md5(raw).hexdigest()[:8]}: the full-backing figure the unit quotes "
          f"({om.FIG['full']} a year) and the main reading its flag quotes ({om.FIG['main']}) are the runs' Reference rows")
    sb, sa = p_before.steps[-1], p.steps[-1]
    moved = {c: sa["total"][c] - sb["total"][c] for c in p.order if sa["total"][c] != sb["total"][c]}
    first = [c for c in p.order if sa["total"][c] == max(sa["total"].values())]
    check(moved == {"CCO": 0.5} and sa["fail"] == sb["fail"] and first == ["CCO"],
          f"it moves CCO from {pc.f1(sb['total']['CCO'])} to {pc.f1(sa['total']['CCO'])}, no failure count, and "
          f"CCO holds first place alone before this group")

    print("\n[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(sorted(set(p.part_of[(c, CRIT)] for c in before)))}) and are "
          "not re-read")
    check(p.v2[CRIT]["revision"]["cls"] == "M" and len(p.v2[CRIT]["definition"]["clauses"]) == 5
          and p.v2[CRIT]["definition"]["clause_scope"] == "each shown feasible by precedent or component evidence",
          f"{CRIT} is class M with five clauses in v2.0, all under the scope 'each shown feasible by precedent or "
          "component evidence'")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group raises {len(rise)} ({', '.join(rise)}), lowers {len(fall)} and holds {len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 == pub[c] for c in zeros)
          and [c for c in mine if pub[c] == 0.0] == ["CPS", "FALC", "INT"],
          f"{len(zeros)} units are 0.0, as published, each on a stated whole-criterion reason (protocol 2.1); the third "
          "published 0.0, Integral's, rises with a clause cleared")
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    after1 = [c for c in p.order if (UNITS.get((c, CRIT)) or p.merged.get((c, CRIT)) or {}).get("verdict") == 1.0]
    check(ones == EXPECT["ones"] and after1 == ["SQ", "SWF"],
          f"one unit clears all five clauses: {', '.join(ones)}; after this group the entries at 1.0 on {CRIT} are "
          f"{' and '.join(after1)} (Status Quo's with every clause moot)")
    nt = [(c, i + 1, src) for c in mine for i, (st, est, src) in enumerate(UNITS[(c, CRIT)]["clauses"])
          if est.startswith("not estimated in this pass")]
    fixed = all(any(UNITS[(c, CRIT)]["clauses"][int(n) - 1][0] in "US" for n in src.split("clause ")[1].split(" and "))
                for c, _, src in nt)
    check(len(nt) == EXPECT["notest"] and fixed and not any(c in zeros or UNITS[(c, CRIT)]["verdict"] == 1.0
                                                           for c, _, _ in nt),
          f"{len(nt)} clauses are not estimated (part (b9)'s form), each in a 0.5 unit whose named clause is short or "
          "not shown, none in a 0.0 or a 1.0 unit; listed for Report v2.0's clause-level estimate")

    print("\n[2] THE DATES AND FIGURES THE READINGS DERIVE")
    swf = UNITS[("SWF", CRIT)]["clauses"]
    check(FIGS["timor_months"] <= 36 and f"{FIGS['timor_months']} months" in swf[1][1]
          and TIMOR["comments_due"] < TIMOR["law"] < TIMOR["first_investment"]
          and months(TIMOR["independence"], TIMOR["first_investment"]) > 36,
          f"Timor-Leste: {FIGS['timor_months']} months from the consultation's close to the fund's first investments "
          f"({FIGS['timor_law_months']} from the law), within 36; the clause counts the deployment, not the "
          f"{months(TIMOR['independence'], TIMOR['first_investment'])} months since independence")
    nst = [NORWAY["act"], NORWAY["first_transfer"], NORWAY["nbim"], NORWAY["fiscal_rule"]]
    check(FIGS["norway_stages"] >= 4 and nst == sorted(set(nst)) and all(str(y) in swf[0][1] for y in nst),
          f"Norway: {FIGS['norway_stages']} dated stages of the mechanism's deployment, {', '.join(map(str, nst))}")
    check(all(a < b for a, b in (NORWAY["equities_40"], NORWAY["equities_60"])) and str(NORWAY["equities_60"][1])
          in swf[2][1], "each equity target was reached after the year it was set (1997 to 1998, 2007 to 2009)")
    ubs = UNITS[("UBS", CRIT)]["clauses"][0][1]
    check(len(QUEBEC) >= 4 and list(QUEBEC) == sorted(set(QUEBEC)) and all(str(y) in ubs for y in QUEBEC),
          f"Quebec: {len(QUEBEC)} dated stages of universal childcare, {QUEBEC[0]} to {QUEBEC[-1]}")
    geo = UNITS[("GEO", CRIT)]["clauses"][0]
    check(geo[0] == "S" and ACT["start"] + 20 == ACT["deadline"] and f"{ACT['conveyance_share_2029_30']}%" in geo[1],
          f"the ACT: a 20-year transition from {ACT['start']} to {ACT['deadline']}, with conveyance duty still "
          f"{ACT['conveyance_share_2029_30']}% of own-source revenue projected for 2029-30: short of a staged deployment "
          "shown to completion")
    intc = UNITS[("INT", CRIT)]["clauses"]
    check(len(INT_STAGES) >= 4 and all(s in intc[0][1] for s in INT_STAGES) and "four communities" in intc[0][1]
          and [st for st, _, _ in intc] == ["U", "U", "U", "U", "C"],
          f"Integral: the white paper names {len(INT_STAGES)} stages with no dates; {INT_SITE['registered']} "
          f"communities registered in the project's {INT_SITE['phase']}; one clause, risk mitigation, cleared")
    pe = UNITS[("PE", CRIT)]["clauses"][0][1]
    check(KERALA["share"] in pe and KERALA["launch"] in pe, "Participatory Economics: the Kerala campaign's devolved "
          f"share ({KERALA['share']} of plan funds, from {KERALA['launch']}) as its clause quotes it")

    print("\n[3] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))

    print("\n[4] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After decision 58.1", "After group 2.6")
    ok = ok and good

    print(f"\n[5] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    f1 = pc.f1
    t["owner"] = "\n".join([f"#### CCO C3.2 Inflation Control Mechanisms: {f1(old['verdict'])} → {f1(new['verdict'])} "
                            f"(part {OWNER_TAG})", "", "| # | Clause (v2.0) | Status | Estimate | Source |",
                            "|---:|---|---|---|---|"]
                           + [f"| {i + 1} | {p.v2['C3.2']['definition']['clauses'][i]} | {pc.STATUS[st]} | {est} | "
                              f"{src} |" for i, (st, est, src) in enumerate(new["clauses"])]
                           + ["", f"*Flag (reading {new['flag'][1]}):* toward {new['flag'][0]}.", "",
                              f"*Note:* {new['note']}."])
    rows = ["| Entry | Published | Staged | Rapid | Milestones | Resources | Risk | Verdict | Flag |",
            "|---|---:|---|---|---|---|---|---:|---|"]
    for c in mine:
        r = UNITS[(c, CRIT)]
        sts = [("not estimated" if est.startswith("not estimated") else pc.STATUS[st]) for st, est, _ in r["clauses"]]
        rows.append(f"| {c} | {f1(pub[c])} | " + " | ".join(sts) + f" | {f1(r['verdict'])} | "
                    f"{('toward ' + r['flag'][0][:3]) if r['flag'] else ''} |")
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
    print("\nRESCORING STAGE 2, GROUP 2.6, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.6: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
