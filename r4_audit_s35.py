#!/usr/bin/env python3
"""
r4_audit_s35.py -- NEEC revision R4: every corpus 1.0 on a multi-clause Pass Threshold, audited; decision D28
==============================================================================================================
Session 35. The first blind replication (NEEC_OstromCommons_replication_record.md, 4 and 10.3) left one
question the protocol does not settle: when a Pass Threshold has several clauses, is it cleared clause by
clause, and how does a clause outside a mechanism's reach count? Revision R4 asked for an audit of every 1.0 in
the corpus that rests on such a threshold before any rule was written. This script is that audit, and the
computation of decision D28, the rule adopted after it. It changes no file and no score.

THE POPULATION. Every 1.0 in neec_corpus.json on a criterion whose Pass Threshold (criteria.json, definition)
has more than one clause: 167 units. Five criteria have one clause (C1.2a, C1.2b, C1.5, C2.2, C3.3) and are
outside the audit. Each threshold is split into clauses that are verbatim substrings of it, in order; what is
left over is asserted to be connective text only.

THE TEXT AUDITED. Each unit's rationale as scored: for the thirteen entries scored before the v2 scoring
documents, the criterion line of the entry's block in NEEC_Report_v1_6.md, Part I; for the ten entries with
their own scoring document, the criterion's section of that document. Each is located exactly once, and its
heading must state 1.0.

THE CODES. Each clause of each unit gets one code, from the unit's own text:
  A  addressed: the text claims the clause's condition holds, in terms compatible with its bar -- a figure at
     or above it, a record, or a qualitative statement that the condition holds (hedged projections for
     designs count; evidence strength is protocol 4.1's question, not this audit's).
  P  partial: the text addresses the clause, but its own claim stops short of it -- an improvement where the
     clause sets a level, "moderately", a range straddling the bar, a comparative without a level, fewer
     phases than required, a demonstrated change below the figure with no range claimed, a pathway asserted
     where validation is required, or the clause's question expressly left open or scored elsewhere.
  X  shortfall: the text gives a figure below the bar, or concedes that the condition does not hold.
  S  silent: the text makes no claim about the clause's subject (naming a mechanism without saying what it
     achieves for that subject is silence).
  N  moot: the text itself establishes that the clause cannot apply to the entry (it presupposes a
     transition, scale-up or coordination the text shows is not needed).
A lower-case code marks a clause outside the reach of a mechanism-class entry (protocol 3.1-3.2): a quantity
the mechanism does not govern even when generalised, so that crediting it would credit the host economy.
Every A, P, X and N (either case) carries a phrase from the unit's text, located after normalisation
(whitespace collapsed; markdown escapes, asterisks and curly quotes removed). Every lower-case code carries its
reason in REACH. The coding is one coder's reading of the text as written; it is not a rescoring on evidence.

THE RULES COMPUTED.
  D28 (strict, adopted):  a 1.0 stands only if every clause is A or N, in upper case.
  reach-excused:          lower-case clauses are set aside; every upper-case clause is A or N (at least one
                          clause must lie within reach).
  stated-shortfall:       a 1.0 stands unless some clause, in either case, is P or X.
A 1.0 that does not stand becomes 0.5 in the textual bound computed here: each rationale describes a working
mechanism, so protocol 2.1's 0.0 conditions are not met by a clause-level gap, and no failure count, and so no
tier, can change. Totals, ranks, dominance pairs and the frontier can. The bound counts what the text does not
show; it is not a prediction of the rescoring, which re-estimates those clauses on evidence.

Usage: python3 r4_audit_s35.py      (reads criteria.json, neec_corpus.json, neec_scores.csv,
                                     NEEC_Report_v1_6.md, the ten native scoring documents and
                                     NEEC_R4_MultiClause_Audit_s35.md beside itself; writes nothing)
Prints file names only. Deterministic.
"""
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, CSV_FILE = "criteria.json", "neec_corpus.json", "neec_scores.csv"
REPORT, RECORD = "NEEC_Report_v1_6.md", "NEEC_R4_MultiClause_Audit_s35.md"
NATIVE = {"GEO": "NEEC_Georgism_LVT_scoring_scratch.md", "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
          "DE": "NEEC_DoughnutEconomics_scoring_scratch.md", "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
          "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
          "CN": "NEEC_StateCapitalism_China_scoring_scratch.md",
          "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
          "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "IF": "NEEC_IslamicFinance_scoring_scratch.md",
          "OS": "NEEC_Ostrom_Commons_scoring_scratch.md"}
# the thirteen entries whose rationale of record is their Report v1.6 Part I block, in the Report's order
V1 = ["SQ", "NSD", "CPS", "MS", "LM", "MMT", "UBI", "DG", "SC", "FALC", "PE", "CCO", "INT"]
V1_HEADINGS = ["Status Quo", "Nordic", "Centrally Planned", "Market Socialism", "Libertarian", "Modern Monetary",
               "Universal Basic Income", "Degrowth", "Stakeholder", "Fully Automated", "Participatory", "CCO",
               "Integral"]
SINGLE = ("C1.2a", "C1.2b", "C1.5", "C2.2", "C3.3")

# ---- clauses: verbatim substrings of each definition Pass Threshold, in order, with short labels ----------
CLAUSES = {
    "C1.1": [("≥90% poverty reduction within 20 years under base scenario", "base ≥90%"),
             ("≥85% under stress testing", "stress ≥85%")],
    "C1.3": [("≥88% housing stability over 5-year periods", "stability ≥88%"),
             ("maintaining affordability at 80% area median income", "affordability 80% AMI")],
    "C1.4": [("Poverty <8%", "poverty <8%"), ("aggregate demand >85% baseline", "demand >85%")],
    "C2.1": [("≥70% report genuine autonomy in major life decisions", "autonomy ≥70%"),
             ("validated through revealed preference showing acceptance of initially refused employment/living "
              "situations when alternatives exist", "revealed preference")],
    "C2.3": [("≥50% regular creative engagement", "engagement ≥50%"),
             ("average 10+ hours weekly on non-subsistence pursuits", "10+ h/week"),
             ("meaning/purpose satisfaction scores ≥70/100", "satisfaction ≥70")],
    "C2.4": [("≥70% participation in democratic processes", "participation ≥70%"),
             ("≥35% citizen proposals adopted", "proposals ≥35%"),
             ("≥65% satisfaction with responsiveness", "responsiveness ≥65%")],
    "C2.5": [("Exit feasible within 3 months without material penalty", "exit ≤3 months"),
             ("no differential treatment", "no differential treatment"),
             ("geographic mobility maintained", "mobility"),
             ("voluntary association protected", "voluntary association")],
    "C3.1": [("Response within 72 hours", "≤72 hours"),
             ("scaling 1:1 with crisis severity (30% GDP decline = 30% benefit increase)", "1:1 scaling"),
             ("≥90% population coverage", "coverage ≥90%")],
    "C3.2": [("Long-term inflation ≤3%", "long-term ≤3%"),
             ("stress test inflation ≤5% (when external 8%)", "stress ≤5%"),
             ("automatic adjustment preventing runaway inflation", "automatic adjustment")],
    "C3.4": [("≥30% parameter adjustability range", "range ≥30%"),
             ("policy updates within 6 months of evidence", "updates ≤6 months"),
             ("democratic governance for changes", "democratic governance"),
             ("zero collapses during parameter adjustments", "zero collapses")],
    "C3.5": [("Failure detection within 1 week", "detection ≤1 week"), ("diagnosis success ≥80%", "diagnosis ≥80%"),
             ("correction success ≥70%", "correction ≥70%"),
             ("externalization <10% of total costs", "externalisation <10%")],
    "C4.1": [("35% carbon reduction by 2030", "carbon -35%"), ("resource use ≤90% regeneration", "use ≤ regeneration"),
             ("debt-to-GDP <80%", "debt <80% GDP"),
             ("positive wealth transfer to next generation", "positive transfer")],
    "C4.2": [("Absolute carbon reductions 35-45% by 2030", "carbon -35-45%"),
             ("biodiversity neutral or positive", "biodiversity"),
             ("resource extraction ≤ regeneration", "extraction ≤ regeneration"),
             ("≥7 of 9 planetary boundaries respected", "≥7/9 boundaries")],
    "C4.3": [("Disparity reduction ≥5 percentage points every 5 years", "-5pp per 5 years"),
             ("disadvantaged groups receive 150%+ proportional benefits", "150%+ benefits"),
             ("convergence trajectory toward <20% disparities within 30 years", "convergence <20%")],
    "C4.4": [("Gini <0.35 for wealth", "wealth Gini <0.35"), ("≥40% citizen proposals adopted", "proposals ≥40%"),
             ("democratic accountability for ≥80% of major decisions", "accountability ≥80%"),
             ("removal/replacement mechanisms functional", "removal mechanisms")],
    "C4.5": [("Extraction rates <10% GDP", "extraction <10% GDP"),
             ("genuine exit rights from exploitative relationships", "exit rights"),
             ("residual coercion <10% of decisions", "coercion <10%")],
    "C5.1": [("≥70% of system components proven through ≥20 years operation at scale ≥10,000 participants",
              "≥70% proven"), ("with documented outcomes matching claimed benefits", "outcomes match claims")],
    "C5.2": [("staged (≥4 phases)", "staged ≥4 phases"), ("rapid (≤36 months) deployment", "rapid ≤36 months"),
             ("specific milestones", "milestones"), ("resource requirements", "resources"),
             ("risk mitigation", "risk mitigation")],
    "C5.3": [("Viable at ≥30% participation", "viable at ≥30%"),
             ("coexistence with traditional markets maintaining ≥90% economic activity", "coexistence ≥90%"),
             ("scaling pathway validated through modeling", "scaling validated"),
             ("coordination protocols established", "coordination protocols")],
    "C5.4": [("≥60% support across political spectrum", "support ≥60%"),
             ("≥65% opposition to repeal", "repeal opposition ≥65%"),
             ("survival probability ≥80% across administration changes", "survival ≥80%")],
    "C5.5": [("Viable across ≥3 economic contexts (high/middle/low income)", "≥3 economic contexts"),
             ("≥5 cultural contexts", "≥5 cultural contexts"),
             ("parameter flexibility ≥40% adjustment range", "flexibility ≥40%"),
             ("successful operation validated across diverse implementations", "validated implementations")],
}
# connective text left once the clauses are removed (asserted, so a changed threshold stops the script)
LEFTOVER = {"C1.4": " and  across all three displacement scenarios",
            "C5.2": "Detailed implementation plan for both  and , with , , and "}

# ---- clauses outside a mechanism-class entry's reach (the lower-case codes), with the reason ------------
REACH = {
    ("MMT", "C1.3", 1): "affordability is set by housing policy and land markets, not by an employment guarantee; "
                        "the social housing the text cites is an adjacent programme (3.2)",
    ("MMT", "C2.4", 0): "participation in democratic processes is a property of the political system",
    ("MMT", "C2.4", 1): "the adoption of citizen proposals is a property of the political system",
    ("MMT", "C2.4", 2): "satisfaction with responsiveness is a property of the political system",
    ("MMT", "C4.2", 0): "economy-wide emissions are not governed by the job guarantee; the Green New Deal the text "
                        "cites is an adjacent programme (3.2)",
    ("MMT", "C4.2", 1): "biodiversity is not governed by the job guarantee",
    ("MMT", "C4.2", 2): "the economy's rate of extraction is not governed by the job guarantee",
    ("MMT", "C4.2", 3): "planetary-boundary compliance is not governed by the job guarantee",
    ("UBI", "C4.5", 0): "the economy-wide extraction share is not governed by an income transfer",
    ("GEO", "C2.5", 3): "freedom of association is not governed by a land tax",
    ("UBS", "C2.5", 3): "freedom of association is not governed by public services",
    ("SWF", "C2.5", 3): "freedom of association is not governed by a sovereign fund",
    ("SWF", "C4.1", 0): "economy-wide carbon emissions are not governed by the fund",
    ("SWF", "C4.1", 1): "the rate of resource extraction is not governed by the fund, which invests its proceeds",
    ("IF", "C2.5", 2): "geographic mobility is not governed by a financing mechanism",
    ("IF", "C2.5", 3): "freedom of association is not governed by a financing mechanism",
    ("OS", "C4.1", 0): "economy-wide carbon reduction is not governed by resource-commons institutions (the "
                       "document's own flag)",
    ("OS", "C4.1", 2): "public debt is not governed by commons institutions (the document's own flag)",
}

UNITS = []


def U(entry, crit, codes, *phrases):
    """One audited unit. Phrases are consumed, in clause order, by every code other than S and s."""
    UNITS.append((entry, crit, codes, list(phrases)))


# ---- the register: 167 units, in corpus order ----------------------------------------------------------------
U("SQ", "C3.2", "ASS", "maintains long-term inflation around 2-3% target")
U("SQ", "C5.1", "AP", "operated for centuries with an extensive empirical track record",
  "validate adequacy for contemporary challenges")
U("SQ", "C5.2", "NNNNN", *["no transition required"] * 5)
U("SQ", "C5.3", "NANN", "Currently deployed universally", "Mixed economies demonstrate coexistence",
  "Currently deployed universally", "Currently deployed universally")

U("NSD", "C1.1", "AS", "Achieves 94-96% poverty elimination")
U("NSD", "C1.3", "AS", "achieve ~90%+ housing stability")
U("NSD", "C2.1", "PS", "coercion significantly")
U("NSD", "C2.3", "XAS", "35-45% regular creative engagement", "enable non-subsistence pursuits")
U("NSD", "C2.4", "PSS", "65-75% voter turnout")
U("NSD", "C3.1", "APS", "automatically increase during downturns without legislative delay",
  "scale moderately with crisis severity")
U("NSD", "C3.2", "ASS", "Successfully maintained low inflation (2-3%) over decades")
U("NSD", "C3.4", "AASS", "Willing to adjust parameters", "Frequent policy experimentation")
U("NSD", "C4.3", "ASA", "active policies address disparities in immigrant and minority communities",
  "Strongest performance on gender equity globally")
U("NSD", "C4.4", "XSSS", "wealth Gini ~0.65-0.75")
U("NSD", "C5.1", "AA", "real-world implementation at scale", "Components thoroughly validated")
U("NSD", "C5.2", "ASSSS", "occurred gradually over 40+ years")
U("NSD", "C5.4", "ASS", "High public satisfaction (70-85%)")

U("CPS", "C1.1", "AS", "near-universal elimination of absolute poverty")
U("CPS", "C1.3", "AA", "stability was near-universal", "Universal housing provision through state allocation")
U("CPS", "C3.2", "XSS", "this created shortage inflation")
U("CPS", "C3.5", "ASXS", "Failures were highly visible", "enabling eventual collapse and reform")
U("CPS", "C4.3", "SSA", "Women achieved high labor force participation")
U("CPS", "C4.5", "XSS", "Surplus appropriated by state rather than private owners")

U("MS", "C1.1", "AS", "demonstrate poverty elimination capacity")
U("MS", "C2.1", "PS", "market pressures remain")
U("MS", "C2.3", "SAS", "sabbaticals, and education time")
U("MS", "C2.4", "ASS", "75-85% participation in cooperative governance")
U("MS", "C3.4", "SAAA", "rapid adaptation to evidence", "Democratic governance enables",
  "50+ years of continuous adaptation")
U("MS", "C4.4", "PSAS", "substantially lower than capitalist firms",
  "distributes economic power through democratic ownership")
U("MS", "C5.1", "AA", "70+ years, 80,000+ worker-owners", "97% survival rate over 5 years")
U("MS", "C5.3", "AASS", "Cooperatives function well in mixed economies", "Can coexist with traditional firms")

U("LM", "C2.3", "XPS", "this only applies to economically secure minorities",
  "For those with capital, maximum freedom to pursue interests")
U("LM", "C2.4", "XSS", "economic democracy is entirely absent")
U("LM", "C2.5", "ASAA", "Maximum exit rights and mobility", "no state restrictions on movement",
  "Freedom of contract allows voluntary communes")
U("LM", "C4.5", "SSX", "ignores economic coercion and power asymmetries")
U("LM", "C5.2", "ASSSS", "Could be implemented gradually")

U("MMT", "C1.1", "AS", "Near-universal poverty elimination achievable")
U("MMT", "C1.3", "Ps", "would substantially improve housing security")
U("MMT", "C2.4", "sss")
U("MMT", "C3.1", "AAS", "No legislative delay", "recession automatically increases enrollment")
U("MMT", "C3.4", "ASSS", "adjust job guarantee wage, spending levels, taxation")
U("MMT", "C4.2", "psss", "Theoretically compatible with absolute emissions reductions")
U("MMT", "C4.3", "AAS", "Eliminates discrimination in hiring", "could specifically target disadvantaged communities")
U("MMT", "C5.2", "PSSSS", "pilot programs → regional expansion → national implementation")

U("UBI", "C1.1", "AS", "would achieve 95%+ elimination")
U("UBI", "C1.4", "AA", "addresses income distribution as labor becomes optional",
  "Maintains aggregate demand through unconditional transfers")
U("UBI", "C2.1", "PS", "Pilots show 65-75% report increased autonomy")
U("UBI", "C3.1", "ASA", "no delay", "Immediate crisis cushion for the entire population")
U("UBI", "C3.4", "ASSS", "Simple parameter adjustment")
U("UBI", "C4.3", "ASS", "Universal provision addresses disparities without stigma")
U("UBI", "C4.5", "sAP", "providing an exit option", "Eliminates most desperate exploitation")
U("UBI", "C5.1", "AA", "Alaska Permanent Fund (40+ years, universal)", "positive outcomes documented")
U("UBI", "C5.3", "AAPS", "Can implement at various scales", "Alaska demonstrates coexistence with the market economy",
  "Gradual rollout viable")

U("DG", "C1.1", "AS", "could eliminate poverty")
U("DG", "C1.3", "AA", "Strong housing security", "treating housing as right rather than commodity")
U("DG", "C2.1", "AS", "provide genuine autonomy in how to spend time")
U("DG", "C2.3", "SAS", "prioritizes creative and social time")
U("DG", "C2.4", "ASS", "Participatory democracy core principle")
U("DG", "C3.1", "ASS", "provide automatic crisis support")
U("DG", "C3.4", "AAAS", "evidence-based adjustments", "rapid learning and adaptation", "Democratic governance allows")
U("DG", "C4.1", "AASA", "Absolute reduction in resource extraction and emissions",
  "Absolute reduction in resource extraction", "preservation for future generations")
U("DG", "C4.2", "ASSA", "designed for absolute reductions", "explicitly bounded by planetary limits")
U("DG", "C4.3", "ASS", "Explicitly confronts structural inequalities")
U("DG", "C4.4", "SSSS")
U("DG", "C4.5", "ASS", "removes profit motive for extraction")

U("SC", "C3.4", "ASSS", "Easier to adjust metrics and targets")
U("SC", "C5.2", "ASSSS", "Easily implemented incrementally")
U("SC", "C5.3", "AASS", "Partial deployment proven viable", "coexist easily with traditional corporations")

U("FALC", "C1.1", "AS", "Theoretical capacity for 100% poverty elimination")
U("FALC", "C1.3", "AA", "would achieve complete housing security", "Automated construction and universal provision")
U("FALC", "C1.4", "SS")
U("FALC", "C2.1", "AS", "Post-scarcity eliminates economic coercion entirely")
U("FALC", "C2.3", "AAS", "humans pursue art, science, philosophy, relationships",
  "Unlimited time and resources for creative pursuits")
U("FALC", "C3.2", "ASX", "eliminates inflation as a concern", "Assumes away the problem through technological solutions")
U("FALC", "C4.1", "SASA", "circular economy principles would preserve resources",
  "eliminates the need to exploit the future")
U("FALC", "C4.2", "SSAA", "automated resource optimization could achieve ecological sustainability",
  "harmonize human activity with planetary boundaries")
U("FALC", "C4.5", "ASA", "Eliminates labor exploitation", "eliminating labor necessity")

U("PE", "C1.1", "AS", "would eliminate poverty")
U("PE", "C1.3", "AA", "Stable allocation resistant to market volatility", "Decommodified and universally accessible")
U("PE", "C1.4", "AS", "while maintaining consumption access")
U("PE", "C2.1", "AS", "eliminates both market and state coercion")
U("PE", "C2.3", "SAS", "leave substantial time for self-directed pursuits")
U("PE", "C2.4", "ASS", "Everyone participates in planning affecting them")
U("PE", "C3.1", "ASS", "can rapidly shift priorities during crises")
U("PE", "C3.2", "ASA", "prevents systemic price instability", "adjusting indicative prices to balance supply/demand")
U("PE", "C3.4", "AAAS", "Councils adjust proposals based on feedback", "rapid evidence-based changes",
  "Democratic structure enables")
U("PE", "C4.1", "SASS", "can incorporate long-term ecological preservation")
U("PE", "C4.2", "SSAA", "sustainable resource use", "within ecological limits")
U("PE", "C4.3", "ASS", "addresses systematic devaluation of care work")
U("PE", "C4.4", "ASAS", "No concentrated wealth", "comprehensive economic democracy")
U("PE", "C5.5", "SAAS", "Councils respect cultural variation", "Flexible system accommodating diverse values")

U("CCO", "C1.1", "AS", "achieves 98% poverty elimination in modeling")
U("CCO", "C1.3", "AA", "PTF housing achieves 94% stability rates", "provides permanent affordability")
U("CCO", "C1.4", "AA", "maintains poverty <5%", "aggregate demand 90-110% baseline")
U("CCO", "C2.1", "AS", "Modeling shows 75%+ report genuine autonomy")
U("CCO", "C2.3", "SAS", "Time and resources for non-subsistence activities")
U("CCO", "C2.4", "ASS", "Comprehensive economic and political democracy")
U("CCO", "C2.5", "ASAS", "enabling opt-out without penalty", "Geographic mobility maintained")
U("CCO", "C3.1", "APA", "Response within 72 hours, no legislative delay",
  "CCO automatically increases by 50% during crises", "Universal coverage provides immediate stabilization")
U("CCO", "C3.2", "AAA", "inflation contained ≤3% long-term", "≤5% during external 8% shock",
  "automatic parameter adjustment")
U("CCO", "C3.4", "AAAS", "basic amounts (5-20% GDP/capita)", "System designed for continuous optimization",
  "CIP enables democratic parameter adjustment")
U("CCO", "C3.5", "AASS", "Failures legible and diagnosable", "Failures legible and diagnosable")
U("CCO", "C4.1", "ASSA", "35-45% trajectory achievable", "Positive intergenerational wealth transfer")
U("CCO", "C4.2", "ASSS", "Modeling shows 35-45% reduction trajectory achievable")
U("CCO", "C4.3", "AAA", "Universal provision addresses disparities without stigma",
  "150%+ proportional benefits during rollout", "trafficking vulnerability eliminated")
U("CCO", "C4.4", "ASAS", "Wealth Gini projected <0.35", "CIP provides direct democratic power")
U("CCO", "C5.1", "AA", "70%+ components proven through ≥20 years operation", "10x lower foreclosure")
U("CCO", "C5.2", "PASSS", "municipal pilots → regional → national", "rapid (18-36 months")
U("CCO", "C5.3", "AAAA", "Viable at 30%+ participation", "Can coexist with traditional markets",
  "Scaling pathway validated through modeling", "Inter-jurisdictional coordination protocols specified")
U("CCO", "C5.4", "ASS", "Alaska PFD demonstrates 80%+ approval across the spectrum")

U("INT", "C1.3", "AA", "supports 90%+ housing stability as plausible", "prevents landlord-tenant extraction")
U("INT", "C2.1", "AS", "70%+ genuine autonomy in major life decisions is plausible")
U("INT", "C2.3", "AAS", "could exceed the 35-55% range", "create space for arts, culture, and personal development")
U("INT", "C2.4", "ASS", "plausibly match or exceed the best documented cooperative precedents")
U("INT", "C2.5", "ASSA", "can leave the federation without penalty", "Nodes remain autonomous")
U("INT", "C3.1", "ASA", "Response within 72 hours for clearly-defined crises", "with universal coverage")
U("INT", "C3.2", "ASA", "there is no money supply to inflate", "matched to capacity through COS")
U("INT", "C3.4", "AAAA", "parameter and structural adjustment", "continuous, version-tracked design iteration",
  "integrates evidence into deliberation", "with zero collapse during adaptation")
U("INT", "C3.5", "ASSA", "triggers alarms", "tendency to externalize costs")
U("INT", "C4.1", "SASA", "Ecological sustainability is treated as", "enables intergenerational transfer of knowledge")
U("INT", "C4.2", "SSSA", "enforce planetary-boundary compliance")
U("INT", "C4.4", "AAAS", "A wealth Gini well under 0.35", "high citizen-proposal adoption",
  "broad democratic accountability")
U("INT", "C4.5", "ASA", "removes employer-employee extraction", "removes creditor-debtor subordination")
U("INT", "C5.3", "AAPS", "No requirement for universal simultaneous adoption", "coexisting with traditional markets",
  "supports starting small and expanding gradually")

U("GEO", "C2.5", "ASAs", "relocate freely without penalty", "an individual can relocate freely")
U("GEO", "C3.4", "APAA", "adopted and rescinded split-rate taxation repeatedly", "roughly every four years",
  "through ordinary democratic and administrative process", "no case of collapse-from-adjustment located")
U("GEO", "C5.3", "AAAN", "can adopt LVT independently",
  "coexisting completely normally with an ordinary market economy", "a single country (Estonia, Denmark)",
  "No case of adoption requiring, or even attempting, simultaneous multi-jurisdiction coordination")

U("MC", "C2.5", "ASSA", "carries no formal penalty beyond settling", "Participation is voluntary at every level examined")
U("MC", "C3.4", "ASSA", "clearing and settlement mechanisms have been adapted", "nine decades of continuous operation")
U("MC", "C5.1", "AA", "WIR Bank has operated continuously since 1934", "turnover in the billions of Swiss francs")
U("MC", "C5.3", "AASN", "can begin with as few as a handful of participants", "operates alongside conventional currency",
  "no case of adoption requiring or even attempting simultaneous multi-jurisdiction coordination")
U("MC", "C5.5", "AASA", "and low-income context", "at least five cultural contexts",
  "a genuinely broad implementation record")

U("DE", "C2.5", "AAAS", "both individual mobility and jurisdictional disengagement are low-cost",
  "experiences no different currency, tax base, or property regime",
  "both individual mobility and jurisdictional disengagement are low-cost")
U("DE", "C3.4", "APSS", "an ongoing adjustment mechanism", "revised each year")
U("DE", "C4.1", "SASS", "an intergenerational-preservation device")
U("DE", "C4.2", "SSSA", "incorporated as a hard structural design element")
U("DE", "C5.3", "AAAS", "adopted piecemeal by individual, voluntarily-participating jurisdictions",
  "with the ordinary market economy", "The scaling record is concrete and dated")

U("UBS", "C2.5", "ASAs", "can decline to use any or all of",
  "relocating to a different jurisdiction carries no penalty specific to UBS")
U("UBS", "C3.4", "ASSS", "revising scope, framing, and emphasis")
U("UBS", "C5.1", "AA", "Each of these clears NEEC", "with documented outcomes")
U("UBS", "C5.3", "ASAS", "each of its seven sectors has, in fact, been adopted independently",
  "Universal childcare alone: Quebec, later all of Canada")

U("SWF", "C2.5", "AAAs", "with no additional penalty, lock-in, or exit cost",
  "territorial in the same way any public benefit is", "ordinary geographic mobility")
U("SWF", "C3.4", "PSAA", "formally revised downward from 4% to 3%", "democratically-enacted parameter change",
  "without collapse")
U("SWF", "C4.1", "ssSA", "explicitly-designed intergenerational wealth-transfer mechanism")
U("SWF", "C5.1", "AA", "clears the ≥20-years/≥10,000-participants bar", "independently-documented implementations")
U("SWF", "C5.3", "AAAN", "Every implementing jurisdiction operates independently of every other",
  "coexists with, rather than displaces, an ordinary market economy", "not a projection requiring modeling",
  "operates independently of every other")

U("CN", "C3.2", "AAA", "long-run inflation has stayed", "Consumer prices rose 2.0% in 2022",
  "price-management schemes intended to keep pork and coal prices within set ranges")
U("CN", "C5.1", "AA", "operated continuously since 1978", "with extensively documented outcomes")

U("SG", "C1.3", "AP", "documented stability rate far above the threshold", "Affordability pressure is real and disclosed")
U("SG", "C3.2", "AAA", "core inflation average 0.7% in 2025", "core inflation below the 5% stress bar",
  "a policy band for the Singapore")
U("SG", "C3.4", "AXPA", "repeated, deliberate recalibration", "some evidence-based proposals have been slow or refused",
  "Changes are governed democratically, but under a dominant-party supermajority",
  "recalibration without destabilization")
U("SG", "C5.1", "AA", "operated since independence in 1965", "with extensively documented outcomes")
U("SG", "C5.3", "AASA", "share can be dialled down", "coexists with private and foreign firms by design",
  "operate on an equal basis with local and foreign businesses")

U("QA", "C5.1", "AA", "components have long records at national scale", "with documented outcomes")
U("QA", "C5.3", "AAXS", "functions at low participation", "coexists with markets", "no validated scaling pathway exists")

U("IF", "C2.5", "ASss", "In its scored form the mechanism is strictly elective")
U("IF", "C3.4", "APPA", "share of financing doubled between 2014 and 2016", "within a few years",
  "Shariah Advisory Council tightened", "without destabilisation")
U("IF", "C5.1", "AP", "Malaysia has run the mechanism since 1983", "Whether the outcomes match the design")
U("IF", "C5.2", "AAASA", "forty-year build, from the first Islamic bank in 1983",
  "operated the converted system from March 1984", "Milestones are real enough to be missed",
  "explicit grandfathering of existing conventional contracts")
U("IF", "C5.3", "AAAA", "operates at far lower shares without difficulty", "operate side by side in Malaysia",
  "The scaling pathway from a single licensed bank to near-parity is documented", "no co-mingling of funds")
U("IF", "C5.5", "AAAA", "Three income bands", "Five or more cultural contexts", "Parameter flexibility well beyond 40%",
  "Validation across diverse implementations")

U("OS", "C2.5", "ASSS", "there is no lock-in, no notice period, and no exit charge")
U("OS", "C3.4", "AAAP", "Principle 2 requires the rules to fit local conditions", "faster than any six-month window",
  "a governance procedure for changing the rules", "the only serious objection, the zero-collapse clause")
U("OS", "C4.1", "sAsA", "Resource use at or below regeneration is the mechanism",
  "Positive intergenerational transfer is not a projection")
U("OS", "C5.1", "AA", "Nepal alone involves roughly 2.9 million households", "Documented outcomes")
U("OS", "C5.3", "AAAA", "there is no version of this mechanism that requires the market to be displaced first",
  "all coexisting with markets", "validated rather than proposed", "nested enterprises")
U("OS", "C5.5", "AAAA", "across subsistence, middle-income and advanced market economies",
  "Validated implementations span", "Parameter flexibility is not a tolerance but a", "Validated implementations span")

# ---- keywords for the quoted-threshold comparison (one per clause; "a|b" accepts either) ----------------------
KEYWORDS = {
    "C1.1": ["90%", "85%"], "C1.2a": ["$60,000", "70%"], "C1.2b": ["0.35"], "C1.3": ["88%", "80%"],
    "C1.4": ["8%", "85%"], "C1.5": ["80%"], "C2.1": ["70%", "revealed preference"], "C2.2": ["100%"],
    "C2.3": ["50%", "10+", "70/100"], "C2.4": ["70%", "35%", "65%"],
    "C2.5": ["3 months", "differential", "mobility", "voluntary association"], "C3.1": ["72 hours", "1:1", "90%"],
    "C3.2": ["3%", "5%", "automatic"], "C3.3": ["3 of 4", "20%"], "C3.4": ["30%", "6 months", "democratic", "collapse"],
    "C3.5": ["1 week", "80%", "70%", "10%"], "C4.1": ["carbon", "regeneration", "debt", "transfer"],
    "C4.2": ["carbon", "biodiversity", "regeneration", "planetary boundaries"],
    "C4.3": ["5 percentage points|5pp", "150%", "20%"], "C4.4": ["0.35", "40%", "80%", "removal"],
    "C4.5": ["extraction", "exit", "coercion"], "C5.1": ["70%", "matching"],
    "C5.2": ["4 phases", "36 months", "milestones", "resource", "risk"],
    "C5.3": ["30%", "90%", "model", "coordination"], "C5.4": ["60%", "65%", "80%"],
    "C5.5": ["3 economic", "5 cultural", "40%", "diverse implementations"]}
ADDITIONS = ("partial participation", "legislative", "judge on specificity")

# ---- expected results (every computed verdict below is asserted) ---------------------------------------------
EXPECT = {
    "per_criterion": {"C1.1": 9, "C1.3": 9, "C1.4": 4, "C2.1": 8, "C2.3": 8, "C2.4": 8, "C2.5": 10, "C3.1": 7,
                      "C3.2": 9, "C3.4": 17, "C3.5": 3, "C4.1": 8, "C4.2": 7, "C4.3": 7, "C4.4": 6, "C4.5": 6,
                      "C5.1": 13, "C5.2": 7, "C5.3": 15, "C5.4": 2, "C5.5": 4},
    "units": 167, "ones": 184, "clauses": 542,
    "status": {"A": 271, "S": 207, "P": 24, "X": 11, "N": 11, "a": 0, "s": 17, "p": 1, "x": 0},
    "d28_stand": 33, "reach_stand": 35, "shortfall_fail": 33, "reach_decides": [("OS", "C4.1"), ("SWF", "C2.5")],
    "dominance_base": 14,
}


def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\\", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def read(name):
    path = os.path.join(HERE, name)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: missing input {name}")
    with open(path, encoding="utf-8") as f:
        return f.read()


def f1(x):
    return f"{x:.1f}"


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    crit = json.loads(read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(read(CORPUS))["entries"]
    codes_order = [e["code"] for e in corpus]
    ent = {e["code"]: e for e in corpus}
    rows = list(csv.DictReader(read(CSV_FILE).splitlines()))
    csv_by = {r["system"].split(" (")[0]: r for r in rows}  # the CSV adds a parenthetical to five names

    print(f"NEEC revision R4: the multi-clause audit and decision D28 ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {CSV_FILE}, {REPORT}, {len(NATIVE)} native scoring documents\n")

    # [1] clauses and population ---------------------------------------------------------------------------------
    print("[1] CLAUSES AND POPULATION")
    multi = [c for c in cids if c not in SINGLE]
    check(sorted(CLAUSES) == sorted(multi) and len(multi) == 21,
          f"{len(multi)} criteria have multi-clause Pass Thresholds; {len(SINGLE)} have one clause ({', '.join(SINGLE)})")
    for c in multi:
        pt = cdef[c]["definition"]["pass_threshold"]
        pos, rest, good = 0, "", True
        for text, _ in CLAUSES[c]:
            i = pt.find(text, pos)
            if i < 0 or pt.count(text) != 1:
                good = False
                break
            rest += pt[pos:i]
            pos = i + len(text)
        rest += pt[pos:]
        want = LEFTOVER.get(c, None)
        conn = re.sub(r"(,|\band\b|\s)", "", rest) == "" if want is None else rest == want
        if not (good and conn):
            check(False, f"{c}: clauses are verbatim, in order, and leave only connectives", repr(rest))
    check(ok, "every clause is a verbatim substring of its definition Pass Threshold, located once, in order, "
              "leaving only connective text (and C1.4's shared qualifier, C5.2's shared head)")
    nclauses = {c: len(CLAUSES[c]) for c in multi}
    print("  clauses per criterion: " + ", ".join(f"{c} {n}" for c, n in nclauses.items()))

    for e in corpus:
        vec = e["vector"]
        r = csv_by[e["key"]]
        tot = sum(vec[c] for c in cids)
        if not (f1(tot) == f1(float(r["total_score"])) and sum(vec[c] == 0.0 for c in cids) == int(r["failures"])):
            check(False, f"{e['code']}: corpus vector agrees with the CSV", f"{tot} vs {r['total_score']}")
    check(ok, f"every corpus vector's total and failure count agree with {CSV_FILE} ({len(corpus)} entries)")
    pop = [(e["code"], c) for e in corpus for c in multi if e["vector"][c] == 1.0]
    ones = sum(e["vector"][c] == 1.0 for e in corpus for c in cids)
    per = {c: sum(1 for _, cc in pop if cc == c) for c in multi}
    check(len(pop) == EXPECT["units"] and ones == EXPECT["ones"] and per == EXPECT["per_criterion"],
          f"population: {len(pop)} of the corpus's {ones} scores of 1.0 rest on a multi-clause threshold")
    print("  1.0s per criterion: " + ", ".join(f"{c} {n}" for c, n in per.items()))
    reg = {(u[0], u[1]): u for u in UNITS}
    check(len(reg) == len(UNITS) and set(reg) == set(pop),
          "the register holds exactly the population, one unit each")

    # [2] rationales ---------------------------------------------------------------------------------------------
    print("\n[2] THE RATIONALES")
    rep = read(REPORT).split("\n")
    starts = [i for i, l in enumerate(rep) if re.match(r"^## \*\*(\d+)\\?\. ", l)][:15]
    heads_ok = all(V1_HEADINGS[k] in rep[starts[k]] for k in range(len(V1)))
    check(heads_ok, f"{REPORT}: the thirteen Part I blocks are in corpus order ({', '.join(V1)})")
    natives = {code: read(doc).split("\n") for code, doc in NATIVE.items()}
    text = {}
    for (code, c) in pop:
        if code in NATIVE:
            lines = natives[code]
            hits = [i for i, l in enumerate(lines) if re.match(r"^#### " + re.escape(c) + r" [^:]*: ([0-9.]+) \(", l)]
            if len(hits) != 1:
                check(False, f"{code} {c}: one criterion heading in {NATIVE[code]}", f"{len(hits)} found")
                continue
            i = hits[0]
            score = float(re.match(r"^#### " + re.escape(c) + r" [^:]*: ([0-9.]+) \(", lines[i]).group(1))
            j = i + 1
            while j < len(lines) and not re.match(r"^#{1,4} ", lines[j]):
                j += 1
            text[(code, c)] = (score, "\n".join(lines[i + 1:j]))
        else:
            k = V1.index(code)
            hits = [i for i in range(starts[k], starts[k + 1])
                    if re.match(r"^## \*\*" + re.escape(c) + r" [^*]*: ([0-9.]+)\*\*", rep[i])]
            if len(hits) != 1:
                check(False, f"{code} {c}: one criterion line in its Report block", f"{len(hits)} found")
                continue
            m = re.match(r"^## \*\*" + re.escape(c) + r" [^*]*: ([0-9.]+)\*\* ?(.*)$", rep[hits[0]])
            text[(code, c)] = (float(m.group(1)), m.group(2))
    check(len(text) == len(pop) and all(s == 1.0 for s, _ in text.values()),
          f"all {len(pop)} rationales located exactly once; every heading states 1.0 "
          f"({sum(1 for k in text if k[0] in NATIVE)} in native documents, "
          f"{sum(1 for k in text if k[0] not in NATIVE)} in {REPORT})")

    # [3] codes ---------------------------------------------------------------------------------------------------
    print("\n[3] THE CODES")
    bad = []
    status = {k: 0 for k in "ASPXNaspx"}
    lower_seen = set()
    for (code, c, cs, phrases) in UNITS:
        if len(cs) != nclauses[c] or any(ch not in "ASPXNaspx" for ch in cs):
            bad.append(f"{code} {c}: codes {cs!r}")
            continue
        body = norm(text[(code, c)][1])
        need = [k for k, ch in enumerate(cs) if ch not in "Ss"]
        if len(need) != len(phrases):
            bad.append(f"{code} {c}: {len(phrases)} phrases for {len(need)} coded clauses")
            continue
        for k, ph in zip(need, phrases):
            if norm(ph) not in body:
                bad.append(f"{code} {c} clause {k + 1}: phrase not located: {ph!r}")
        for k, ch in enumerate(cs):
            status[ch] += 1
            if ch.islower():
                lower_seen.add((code, c, k))
                if ent[code]["scope_class"] != "mechanism":
                    bad.append(f"{code} {c}: out-of-reach code on a {ent[code]['scope_class']} entry")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one code per clause; every A, P, X and N phrase is located in its rationale; "
                   "lower-case codes occur only on mechanism-class entries")
    check(lower_seen == set(REACH), f"every out-of-reach clause has its reason stated ({len(REACH)} clauses, "
                                    f"{len({(a, b) for a, b, _ in REACH})} units)")
    total_clauses = sum(status.values())
    check(total_clauses == EXPECT["clauses"] and status == EXPECT["status"],
          f"{total_clauses} clause codes: " + ", ".join(f"{k} {v}" for k, v in status.items() if v))
    probe = norm("a phrase that appears in no rationale of the corpus")
    check(all(probe not in norm(t) for _, t in text.values()),
          "self-test: the locator rejects a phrase absent from every rationale")

    def d28(cs):
        return all(ch in "AN" for ch in cs)

    def reach(cs):
        up = [ch for ch in cs if ch.isupper()]
        return bool(up) and all(ch in "AN" for ch in up)

    def shortfall(cs):
        return not any(ch in "PXpx" for ch in cs)

    check(d28("AN") and not d28("As") and reach("As") and reach("NN") and not reach("ss") and not reach("SA")
          and shortfall("SA") and not shortfall("pA"), "self-test: the three rules behave as defined")

    # clause positions most often left unshown
    print("  clauses never shown in any audited 1.0 (every unit A-less there):")
    for c in multi:
        units_c = [u for u in UNITS if u[1] == c]
        for k, (_, lab) in enumerate(CLAUSES[c]):
            if units_c and all(u[2][k] not in "AN" for u in units_c):
                tally = "".join(sorted(u[2][k] for u in units_c))
                print(f"    {c} ({lab}): {len(units_c)} of {len(units_c)} units -- codes {tally}")

    # [4] register -------------------------------------------------------------------------------------------------
    print("\n[4] THE REGISTER (units in corpus order within each criterion; D28 / reach-excused / stated-shortfall)")
    print("  code key: A addressed  P partial  X shortfall  S silent  N moot; lower case = outside a mechanism's reach")
    for c in multi:
        print(f"  {c}  clauses: " + " | ".join(lab for _, lab in CLAUSES[c]))
        for code in codes_order:
            if (code, c) not in reg:
                continue
            cs = reg[(code, c)][2]
            v = lambda f: "stands" if f(cs) else "0.5   "
            block = [CLAUSES[c][k][1] for k, ch in enumerate(cs) if ch not in "AN"]
            print(f"    {code:5} {cs:6} {v(d28)} {v(reach)} {v(shortfall)}"
                  + (f"  not shown: {'; '.join(block)}" if block else ""))

    # [5] quoted thresholds ----------------------------------------------------------------------------------------
    print("\n[5] QUOTED THRESHOLDS AGAINST THE DEFINITIONS")

    def missing(c, t):
        tl = norm(t).lower()
        return [kw for kw in KEYWORDS[c] if not any(alt.lower() in tl for alt in kw.split("|"))]

    sane = all(not missing(c, cdef[c]["definition"]["pass_threshold"]) for c in cids)
    check(sane and not any(a in norm(cdef[c]["definition"]["pass_threshold"]).lower() for c in cids for a in ADDITIONS),
          "every clause keyword occurs in its own definition, and no added phrase does")
    anchor_gaps = {}
    for c in cids:
        at = cdef[c]["anchors"].get("threshold", "")
        m = missing(c, at)
        add = [a for a in ADDITIONS if a in norm(at).lower()]
        if m or add:
            anchor_gaps[c] = (m, add)
            print(f"  criteria.json anchor {c}: drops {m if m else '[]'}" + (f"; adds {add}" if add else ""))
    check(anchor_gaps == {"C2.5": (["voluntary association"], []), "C3.1": ([], ["legislative"]),
                          "C5.1": (["matching"], []), "C5.3": (["model", "coordination"], [])},
          "criteria.json: four anchor thresholds differ in substance from their definitions (C2.5, C3.1, C5.1, C5.3)")
    quote_gaps = {}
    for code in ("IF", "OS"):
        lines = natives[code]
        cur = None
        for i, line in enumerate(lines):
            m = re.match(r"^#### (C\d\.\d[ab]?) ", line)
            if m:
                cur = m.group(1)
            if line.startswith("*Pass threshold:"):
                j, buf = i, line
                while not buf.rstrip().endswith("*") or buf.strip() == "*Pass threshold:":
                    j += 1
                    buf += " " + lines[j]
                q = norm(buf)[len("Pass threshold:"):]
                mm = missing(cur, q)
                add = [a for a in ADDITIONS if a in q.lower()]
                if mm or add:
                    quote_gaps.setdefault(cur, {})[code] = (tuple(mm), tuple(add))
    same = all(len(v) == 2 and v["IF"] == v["OS"] for v in quote_gaps.values())
    for c, v in quote_gaps.items():
        mm, add = v.get("IF", v.get("OS"))
        lab = {kw: next(l for (t, l), k2 in zip(CLAUSES.get(c, []), KEYWORDS[c]) if k2 == kw) for kw in mm} \
            if c in CLAUSES else {}
        print(f"  IF and OS quote {c}: drops {[lab.get(k, k) for k in mm] if mm else '[]'}"
              + (f"; adds {list(add)}" if add else ""))
    check(same and sorted(quote_gaps) == ["C2.1", "C2.3", "C2.4", "C2.5", "C3.1", "C3.4", "C4.2", "C4.3", "C4.4",
                                          "C5.1", "C5.2", "C5.3"],
          "the two documents quote the same working thresholds; 12 of 26 differ in substance from the definitions")
    audited_quoted = sorted({(k, c) for c in quote_gaps for k in ("IF", "OS") if (k, c) in reg
                             and quote_gaps[c][k][0]})
    print("  audited 1.0s scored against a quotation that drops a clause: "
          + ", ".join(f"{k} {c}" for k, c in audited_quoted))
    check(audited_quoted == [("IF", "C2.5"), ("IF", "C3.4"), ("IF", "C5.1"), ("IF", "C5.3"), ("OS", "C2.5"),
                             ("OS", "C3.4"), ("OS", "C5.1"), ("OS", "C5.3")],
          "eight audited 1.0s (IF and OS: C2.5, C3.4, C5.1, C5.3) were scored against a quotation that drops a clause")

    # [6] consequences -----------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (the bound: every 1.0 a rule does not let stand becomes 0.5)")
    rules = {"D28": d28, "reach-excused": reach, "stated-shortfall": shortfall}
    fails = {r: sorted(k for k, u in reg.items() if not f(u[2])) for r, f in rules.items()}
    stand = {r: len(reg) - len(v) for r, v in fails.items()}
    for r in rules:
        print(f"  {r:17} {stand[r]:3d} of {len(reg)} stand; {len(fails[r]):3d} become 0.5 "
              f"({f1(0.5 * len(fails[r]))} points across the corpus)")
    check(stand["D28"] == EXPECT["d28_stand"] and stand["reach-excused"] == EXPECT["reach_stand"]
          and len(fails["stated-shortfall"]) == EXPECT["shortfall_fail"],
          f"D28 lets {stand['D28']} stand; reach-excused {stand['reach-excused']}; "
          f"stated-shortfall demotes {len(fails['stated-shortfall'])}")
    decides = sorted(set(fails["D28"]) - set(fails["reach-excused"]))
    check(decides == EXPECT["reach_decides"] and set(fails["stated-shortfall"]) <= set(fails["D28"]),
          "how an out-of-reach clause counts decides only " + " and ".join(f"{a} {b}" for a, b in decides)
          + "; every unit the stated-shortfall rule demotes, D28 also demotes")

    def vectors(demote):
        out = {}
        for e in corpus:
            v = dict(e["vector"])
            for (code, c) in demote:
                if code == e["code"]:
                    v[c] = 0.5
            out[e["code"]] = v
        return out

    def tot(v):
        return sum(v[c] for c in cids)

    def ranks(vs):
        t = {k: tot(v) for k, v in vs.items()}
        return {k: 1 + sum(1 for o in t.values() if o > t[k]) for k in t}

    def dom(vs):
        pairs = []
        for a in codes_order:
            for b in codes_order:
                if a != b and all(vs[a][c] >= vs[b][c] for c in cids) and any(vs[a][c] > vs[b][c] for c in cids):
                    pairs.append((a, b))
        return pairs

    base = vectors([])
    scen = {r: vectors(fails[r]) for r in rules}
    fcount = lambda v: sum(v[c] == 0.0 for c in cids)
    check(all(fcount(scen[r][k]) == fcount(base[k]) for r in rules for k in codes_order),
          "no failure count changes under any rule, so no tier changes")
    rb = ranks(base)
    rd = ranks(scen["D28"])
    rs = ranks(scen["stated-shortfall"])
    print("\n  | Entry | Audited 1.0s | Not shown (D28) | Stated shortfall | Total now (rank) | "
          "D28 bound (rank) | Stated-shortfall bound (rank) |")
    print("  |---|---:|---:|---:|---:|---:|---:|")
    table1 = ["| Entry | Audited 1.0s | Not shown (D28) | Stated shortfall | Total now (rank) | D28 bound (rank) | "
              "Stated-shortfall bound (rank) |", "|---|---:|---:|---:|---:|---:|---:|"]
    for code in sorted(codes_order, key=lambda k: (rb[k], codes_order.index(k))):
        na = sum(1 for k in reg if k[0] == code)
        nd = sum(1 for k in fails["D28"] if k[0] == code)
        ns = sum(1 for k in fails["stated-shortfall"] if k[0] == code)
        row = (f"| {code} | {na} | {nd} | {ns} | {f1(tot(base[code]))} ({rb[code]}) | "
               f"{f1(tot(scen['D28'][code]))} ({rd[code]}) | {f1(tot(scen['stated-shortfall'][code]))} ({rs[code]}) |")
        table1.append(row)
        print("  " + row)
    db = dom(base)
    dd = {r: dom(scen[r]) for r in rules}
    check(len(db) == EXPECT["dominance_base"], f"baseline dominance pairs: {len(db)} (the canonical count)")
    for r in rules:
        new = sorted(set(dd[r]) - set(db))
        gone = sorted(set(db) - set(dd[r]))
        front = [k for k in codes_order if not any(b == k for _, b in dd[r])]
        print(f"  {r:17} dominance pairs {len(dd[r]):2d} (new: {', '.join(f'{a}>{b}' for a, b in new) or 'none'}; "
              f"lost: {', '.join(f'{a}>{b}' for a, b in gone) or 'none'}); frontier {len(front)}: {', '.join(front)}")
    fb = [k for k in codes_order if not any(b == k for _, b in db)]
    print(f"  baseline          dominance pairs {len(db):2d}; frontier {len(fb)}: {', '.join(fb)}")
    top_b = [k for k in codes_order if rb[k] == 1]
    top_d = [k for k in codes_order if rd[k] == 1]
    print(f"  first place: baseline {', '.join(top_b)}; D28 bound {', '.join(top_d)}")

    # per-criterion table for the record
    table2 = ["| Criterion | Clauses | Audited 1.0s | Clause judgments | Stand under D28 | "
              "Stand if out-of-reach clauses are excused | Survive the stated-shortfall rule |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for c in multi:
        us = [u for u in UNITS if u[1] == c]
        table2.append(f"| {c} | {nclauses[c]} | {len(us)} | {nclauses[c] * len(us)} | {sum(d28(u[2]) for u in us)} | "
                      f"{sum(reach(u[2]) for u in us)} | {sum(shortfall(u[2]) for u in us)} |")
    table2.append(f"| All | | {len(reg)} | {total_clauses} | {stand['D28']} | {stand['reach-excused']} | "
                  f"{len(reg) - len(fails['stated-shortfall'])} |")

    # [7] record ---------------------------------------------------------------------------------------------------
    print("\n[7] THE RECORD'S TABLES (generated here; the record must contain them verbatim)")
    rec = read(RECORD)
    for name, tb in (("per-criterion table", table2), ("per-entry table", table1)):
        blob = "\n".join(tb)
        check(blob in rec, f"{RECORD} contains the {name} ({len(tb) - 2} rows)")
    print()
    for line in table2:
        print("  " + line)

    # [8] decision --------------------------------------------------------------------------------------------------
    print("\n[8] DECISION D28 (adopted; text in the record, section 6)")
    print(f"  A 1.0 on a multi-clause Pass Threshold requires every clause shown cleared; silence is not clearance;")
    print(f"  a clause outside a mechanism's reach cannot be credited; 0.0 stays holistic (2.1), so no tier moves.")
    print(f"  Textual bound: {len(fails['D28'])} of {len(reg)} audited 1.0s to be re-estimated "
          f"({f1(0.5 * len(fails['D28']))} points); the rescoring pass also tests C5.1's full second clause on its "
          f"{per['C5.1']} 1.0s. Applied by that pass, not here.")

    print("\nR4 AUDIT COMPUTED." if ok else "\nR4 AUDIT NOT COMPUTED: a check failed.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
