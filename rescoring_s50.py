#!/usr/bin/env python3
"""
rescoring_s50.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), ninth and last group: C5.2 Staged
Transition Pathways, C5.4 Political Coalition Potential and C5.5 Cultural Adaptability, on the v2.0 clauses
==============================================================================================================
Session 50. Parts (a) to (b8) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s49.md (rescoring_s37.py to
rescoring_s49.py; rescoring_s48.py re-read C4.4 on decision 48.3). This script holds the ninth group, scored on the
v2.0 criteria as parts (b7) and (b8) were (decision 7.1 of the Session 44 review): the eight part (b) units of C5.2,
C5.4 and C5.5, which finish part (b); the two units of C5.2 that part (a) re-estimated on the Session 44 clauses
(MMT + Job Guarantee's and CCO-PTF-CIP-SZH's), re-read here on the v2.0 clauses; and Status Quo's C5.2, the one
published C5.2 1.0 outside D28's population, re-checked as class M (reading 3.7). It changes no file and no score:
the pass's changes are applied by generator when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). The clauses are v2.0's
(criteria.json). C5.2 (class M) keeps its five Session 44 clauses verbatim and places all five under a new scope,
"each shown feasible by precedent or component evidence", so the audit's A codes on it are re-read against the
scope (reading 3.2), as rescoring_s49.py re-read C4.3's. C5.4 and C5.5 are class U: their clauses are the Session 44
clauses, and the audit's A codes on them are carried as cleared on the unit's own text. A clause marked "not
estimated in this pass" is allowed only where another clause of the same unit fixes its verdict (part (b7)'s rule).
A re-read unit of part (a) can keep its verdict, rise or fall (class M), and its record here supersedes part (a)'s.

CHECKS: the group against the audit's register and against part (a); the v2.0 clauses, scope and classes; every
record complete; the rule; the audit's codes carried or re-read; every silent clause estimated or fixed by another;
reach; Nordic Social Democracy's C5.4 clause 2 computed from the ISSP 2016 figures held below; flags against the
summary blocks, cumulatively with parts (a) to (b8) and decision 48.3; the consequences of the pass so far on the
published 26-criterion structure (totals, ranks, failures, tiers, dominance, frontier, what remains, the criteria
left with no 1.0), the score ledger, the anchor examples the pass so far moves; and that NEEC_Rescoring_s50.md
contains every generated table verbatim.

Usage: python3 rescoring_s50.py   (reads criteria.json (v2.0), criteria_s44_snapshot.json (the published structure
                                   and anchors), criteria_s47_snapshot.json, neec_corpus.json, neec_scores.csv,
                                   NEEC_Report_v1_6.md, r4_audit_s35.py, rescoring_s37.py to rescoring_s49.py and the
                                   files they read, and NEEC_Rescoring_s50.md beside itself; writes nothing)
       python3 rescoring_s50.py --tables   (prints the generated tables as JSON, for assembling the record)
Prints file names only. Deterministic.
"""
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CRIT44, CORPUS, CSV, AUDIT = ("criteria.json", "criteria_s44_snapshot.json", "neec_corpus.json",
                                        "neec_scores.csv", "r4_audit_s35.py")
PRIOR = (("(a)", "rescoring_s37", "rescoring_s37.py", 37), ("(b1)", "rescoring_s38", "rescoring_s38.py", 38),
         ("(b2)", "rescoring_s39", "rescoring_s39.py", 39), ("(b3)", "rescoring_s40", "rescoring_s40.py", 40),
         ("(b4)", "rescoring_s41", "rescoring_s41.py", 41), ("(b5)", "rescoring_s42", "rescoring_s42.py", 42),
         ("(b6)", "rescoring_s43", "rescoring_s43.py", 43), ("(b7)", "rescoring_s47", "rescoring_s47.py", 47),
         ("48.3", "rescoring_s48", "rescoring_s48.py", 48), ("(b8)", "rescoring_s49", "rescoring_s49.py", 49))
THIS = ("(b9)", 50)
RECORD = "NEEC_Rescoring_s50.md"
GROUP = ("C5.2", "C5.4", "C5.5")
# v2.0 clause index -> the Session 44 clause it continues (the audit's index). Every v2.0 clause here is verbatim and
# none is deleted. SCOPED: clauses v2.0 places under a new scope, whose A codes are re-read (reading 3.2).
MAP = {"C5.2": (0, 1, 2, 3, 4), "C5.4": (0, 1, 2), "C5.5": (0, 1, 2, 3)}
SCOPED = {"C5.2": (0, 1, 2, 3, 4), "C5.4": (), "C5.5": ()}
CLS = {"C5.2": "M", "C5.4": "U", "C5.5": "U"}
SCOPE = "each shown feasible by precedent or component evidence"
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
NOTEST = "not estimated in this pass"
S37 = "rescoring_s37.py, "
IFDOC = "NEEC_IslamicFinance_scoring_scratch.md, "
MCDOC = "NEEC_MutualCredit_LETS_scoring_scratch.md, "
ISSP = ("ISSP 2016, Role of Government V, GESIS ZA6900 v2.0.0 (doi 10.4232/1.13052), Variable Report 2018/09, tables "
        "v14, v18, v23 and v24 by country, row percentages of those choosing an answer ('can't choose' and no answer "
        "excluded), retrieved 2026-09-25 (PDF md5 9f3ca6fd)")
JEFES = ("Tcherneva, Beyond Full Employment: The Employer of Last Resort as an Institution for Change, Levy Economics "
         "Institute Working Paper 732 (2012), sections 2 and 3 (PDF md5 10f781d2)")
HUB = "research hub at 8e8a6ba"
ROADMAP = HUB + ", integrated-implementation-roadmap.html (md5 97f61b28)"
MODEL = HUB + ", economic-modeling-simulation.html (md5 86dda39b), section 10"
RISK = HUB + ", risk-mitigation-framework.html (md5 b83ad1d5)"
PLAN = "compassionate-meritocracy-plan at e03d115, index.html (md5 8b2eee2f)"
SIM = "Compassionism Simulation at cd0ceec, harness.js (md5 035d1be8), searched 2026-09-25"
SWEDEN = ("the Saltsjöbaden Agreement (1938); the Swedish national pension act (1946), child allowance act (1947), "
          "health insurance act (1947, in force 1955), supplementary pension act (1959), parental insurance (1974) and "
          "Co-determination Act (1976)")
GERMANY = ("Montan-Mitbestimmungsgesetz (1951), Betriebsverfassungsgesetz (1952, revised 1972), Mitbestimmungsgesetz "
           "(1976)")
BRITAIN = "the British National Insurance Act 1946 and National Health Service Act 1946, in force 5 July 1948"
MALAYSIA = ("Malaysia's Islamic Banking Act 1983, Bank Negara Malaysia's interest-free banking scheme (1993), its "
            "Shariah Advisory Council (1997) and the Islamic Financial Services Act 2013")
PAKISTAN = ("ProPakistani, Pakistan Plans Full Shift To Islamic, Interest-Free Financing From 2028 (1 July 2026), on the "
            "Ministry of Finance's Strategy Paper Post 2027 Financial System in Pakistan")

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in v2.0's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- Nordic Social Democracy, C5.4 clause 2: the ISSP 2016 Role of Government module (reading 3.5) --------------
# Row percentages by answer, of those choosing an answer. v14 and v18: "would you like to see more or less government
# spending" on health and on old age pensions (much more, more, the same as now). v23 and v24: "should or should not
# be the government's responsibility to" provide health care for the sick, and a decent standard of living for the
# old (definitely should be, probably should be).
ISSP_ITEMS = {"v14": ("spending on health", 3), "v18": ("spending on old age pensions", 3),
              "v23": ("responsibility: health care for the sick", 2),
              "v24": ("responsibility: a decent standard of living for the old", 2)}
ISSP_PCT = {
    "v14": {"Denmark": (25.3, 48.3, 23.8), "Finland": (20.3, 43.9, 32.6), "Norway": (19.9, 54.5, 23.5),
            "Sweden": (33.9, 50.9, 14.5)},
    "v18": {"Denmark": (10.0, 31.2, 53.8), "Finland": (15.8, 37.6, 43.0), "Norway": (9.0, 34.6, 53.5),
            "Sweden": (27.7, 43.6, 26.9)},
    "v23": {"Denmark": (78.8, 19.3), "Finland": (76.1, 21.0), "Norway": (87.4, 12.3), "Sweden": (68.8, 27.0)},
    "v24": {"Denmark": (61.0, 34.5), "Finland": (67.6, 29.6), "Norway": (80.0, 19.3), "Sweden": (68.6, 28.7)},
}
REPEAL = 65.0   # C5.4 clause 2's bar


# ---- C5.2 Staged Transition Pathways, part (b) units (readings 3.2 and 3.3) --------------------------------------
U("NSD", "C5.2", 0.5, [
    ("C", "the audited phrase, occurred gradually over 40+ years, names the configuration's own deployment, a precedent "
          "in the sense of the scope; it was built in successive stages in each country, in Sweden alone at least four: "
          "crisis policy and the Saltsjöbaden Agreement (1932-1938), the universal pension and child allowance "
          "(1946-1948), compulsory health insurance and the earnings-related pension (1955-1960), and parental "
          "insurance and the Co-determination Act (1974-1976) (reading 3.2)", REP + "NSD C5.2; " + SWEDEN),
    ("U", "the entry states no rapid pathway, and its own history is a build of four decades; its universal social "
          "insurance has a precedent of rapid deployment elsewhere (Britain's, legislated in 1946 and in force by July "
          "1948), but the entry names strong labor unions as defining, and no deployment of encompassing unions and "
          "centralised bargaining within 36 months is located: Sweden's took from the December Compromise of 1906 to "
          "the Saltsjöbaden Agreement of 1938 (reading 3.3)", REP + "NSD overview and C5.2; " + BRITAIN),
    ("U", NOTEST + "; the verdict is fixed by clause 2", ""),
    ("U", NOTEST + "; the verdict is fixed by clause 2", ""),
    ("U", NOTEST + "; the verdict is fixed by clause 2", "")],
  note="the audit coded clause 1 A and the other four silent; clause 1 is re-read against the scope v2.0 adds "
       "(reading 3.2)")

U("LM", "C5.2", 0.5, [
    ("U", "the audited phrase, could be implemented gradually, is a claim, and deregulation, welfare elimination and tax "
          "reduction is a sequence, not a deployment that took place: no state located has been reduced, in stages or "
          "otherwise, to the minimal functions the design specifies; component evidence covers deregulation, "
          "privatisation and tax cuts singly, but not the step the entry names as its own, the elimination of social "
          "programmes (reading 3.3)", REP + "LM C5.2 and C5.4"),
    ("U", "the entry states no rapid pathway, and no deployment of a minimal state within 36 months, or at any pace, is "
          "located (reading 3.3)", REP + "LM C5.2"),
    ("U", NOTEST + "; the verdict is fixed by clauses 1 and 2", ""),
    ("U", NOTEST + "; the verdict is fixed by clauses 1 and 2", ""),
    ("U", NOTEST + "; the verdict is fixed by clauses 1 and 2", "")],
  note="the audit coded clause 1 A and the other four silent; clause 1 is re-read against the scope v2.0 adds "
       "(reading 3.2)")

U("SC", "C5.2", 0.5, [
    ("C", "the audited phrase names corporate governance reforms, tax incentives and regulatory requirements, and the "
          "entry's governance reform includes worker representation on boards; component evidence: that component has "
          "been deployed in stages, in Germany in four: the Coal and Steel Codetermination Act (1951), the Works "
          "Constitution Act (1952), its revision (1972) and the Codetermination Act (1976) (reading 3.3)",
     REP + "SC overview, C2.4 and C5.2; " + GERMANY),
    ("U", "the entry states only an incremental pathway with minimal disruption, and no deployment of stakeholder "
          "governance across an economy within 36 months is located: Germany's took a quarter-century, from 1951 to "
          "1976 (reading 3.3)", REP + "SC C5.2; " + GERMANY),
    ("U", NOTEST + "; the verdict is fixed by clause 2", ""),
    ("U", NOTEST + "; the verdict is fixed by clause 2", ""),
    ("U", NOTEST + "; the verdict is fixed by clause 2", "")],
  note="the audit coded clause 1 A and the other four silent; clause 1 is re-read against the scope v2.0 adds "
       "(reading 3.2)")

U("IF", "C5.2", 0.5, [
    ("C", "the audited phrase, forty-year build, from the first Islamic bank in 1983, names a precedent: Malaysia's dual "
          "system was built in dated stages, among them the Islamic Banking Act and the first Islamic bank (1983), the "
          "interest-free banking scheme for conventional banks (1993), the Shariah Advisory Council (1997) and the "
          "Islamic Financial Services Act (2013) (reading 3.3)", IFDOC + "C5.2; " + MALAYSIA),
    ("C", "the audited phrase names a precedent within the window: Iran legislated the conversion of its banking "
          "system in 1983 and operated the converted system from March 1984 (reading 3.3)", IFDOC + "C5.2"),
    ("C", "the audited phrase, milestones are real enough to be missed, is the precedent's milestone record: Malaysia "
          "set a 50% Islamic share by 2025 and measured 48%, so its milestones were dated and checked (reading 3.3)",
     IFDOC + "C5.2"),
    ("U", "the entry states no resource requirement for either pathway, and the precedents it cites document laws, "
          "dates and shares, not the resources the conversions took (capital, trained staff, liquidity instruments); "
          "reports of Pakistan's 2026 roadmap say that banks' Islamic windows already hold the technology and that "
          "staff training is under way, but give no estimate of cost, capital or staff (reading 3.3)",
     IFDOC + "C5.2; " + PAKISTAN),
    ("C", "the audited phrase, explicit grandfathering of existing conventional contracts, is Pakistan's measure, "
          "announced for 2028 and not yet in force; mitigation of the same kind has worked in the staged precedent: "
          "Malaysia's dual system required no forced conversion of existing contracts, running Islamic and "
          "conventional banking side by side for four decades (reading 3.3)", IFDOC + "C5.2 and C5.3")],
  flag=([1.0], "read as satisfied wherever a precedent was completed, whatever resources it took, the national "
               "conversions of Iran (1983-1984) and Malaysia's build show that the resources were found, and the "
               "clause is cleared (reading 3.3)"),
  note="the audit coded four clauses A and resource requirements silent; the four are re-read against the scope and "
       "carried, and the silent clause decides; the register's flag toward 0.5 is resolved by the verdict and "
       "replaced by one toward 1.0")

# ---- part (a)'s units of C5.2, re-read on v2.0 (reading 3.4) ---------------------------------------------------------
U("MMT", "C5.2", 0.5, [
    ("S", "three stages (pilot, regional, national) against at least four, as part (a) found; the one national "
          "precedent of its kind located was also phased in fewer: India's rural employment guarantee, extended to all "
          "districts in three phases between 2006 and 2008 (reading 3.4)",
     REP + "MMT C5.2; " + S37 + "MMT C5.2; National Rural Employment Guarantee Act 2005, phases of 2006, 2007 and 2008"),
    ("C", "a precedent of the same kind: Argentina's Plan Jefes y Jefas de Hogar, a public employment programme begun "
          "in April 2002 in the crisis, whose payrolls ballooned quickly, against a government estimate of 500,000, to "
          "nearly 2 million participants, 13% of the labour force, at a cost peaking at 1% of GDP (reading 3.4)",
     JEFES),
    ("U", NOTEST + "; the verdict is fixed by clause 1 (part (a) located none)", ""),
    ("U", NOTEST + "; the verdict is fixed by clause 1 (part (a) located none)", ""),
    ("U", NOTEST + "; the verdict is fixed by clause 1 (part (a) located none)", "")],
  note="part (a)'s unit re-read on v2.0's clauses: clause 1 stays short, so the unit stays 0.5; clause 2, which part (a) "
       "read as a plan and found not shown, is cleared on v2.0's precedent test")

U("CCO", "C5.2", 0.5, [
    ("U", "the roadmap specifies seven phases over seven years, but its second phase launches the dual currency for all "
          "Americans in year 2, and its phases deploy components of which no deployment at comparable scale is "
          "located, a national complementary currency whose units expire monthly and convert at merit-based rates, and "
          "a national portal for blockchain-verified voting and direct policy proposals (the nearest located are local, "
          "Wörgl's stamp scrip of 1932-1933, or partial, Estonia's internet voting in national elections since 2007); "
          "the modelling paper's pilot-first pathway has three phases, municipal pilots, regional expansion and "
          "national implementation, and concludes that the computational evidence supports proceeding with municipal "
          "pilot programs to begin empirical validation (reading 3.4)", ROADMAP + "; " + MODEL),
    ("U", "the three-month national launch plan and the Report's 18-36 months are plans; the precedents the entry "
          "cites, the New Deal's and the Marshall Plan's three years, are programmes of other kinds cited for their "
          "speed; component evidence covers the design's universal distribution (Alaska's dividend, paid to residents "
          "every year since 1982), but no deployment of a national expiring currency or of binding national digital "
          "democracy, within 36 months or at any pace, is located (reading 3.4)", REP + "CCO C5.2; " + PLAN),
    ("U", "the milestones (poverty below 10% in year 1 and below 2% by year 7, enrolment of 80% in year 1, 10,000 "
          "Creator Collectives in year 1; the launch-phase KPIs) are the design's own targets; no precedent or "
          "component evidence is cited or located for them, and the modelling paper's phase success probabilities "
          "(84%, 78% and 71%) come from its own parameter sensitivity, a model outcome (reading 3.4)",
     ROADMAP + ", Appendix I; " + PLAN + "; " + MODEL),
    ("U", "the resources are stated ($500 billion over five years for Public Trust Foundations; in the three-month plan, "
          "$950 billion of federal allocations and some 190,000 staff and coordinators), but no precedent or component "
          "evidence shows them sufficient for the deployment: the documents cite none, and the modelling paper's "
          "fiscal break-even is a model outcome (reading 3.4)", ROADMAP + ", Appendix A; " + PLAN + "; " + MODEL),
    ("C", "the plan's risk section and the Risk Mitigation Framework specify mitigations of kinds in use elsewhere "
          "(redundant systems and manual backups, audits, independent oversight bodies, algorithmic transparency), and "
          "the modelling paper's mitigation of transition disruption is the parallel operation of existing systems: "
          "component evidence in the sense of reading 3.2 (reading 3.4)", PLAN + "; " + RISK + "; " + MODEL)],
  flag=([1.0], "read as part (a) read the Session 44 clause, on the plans' specificity, with the precedents the entry "
               "cites for their timing (the New Deal, the Marshall Plan) and the modelling paper's success "
               "probabilities as evidence of feasibility, every clause is cleared and the unit stays 1.0 (reading 3.4)"),
  note="part (a)'s unit re-read on v2.0's clauses: part (a) judged the plans' specification, as the Session 44 clause "
       "asked; v2.0 asks that each element be shown feasible by precedent or component evidence (R4), and C5.2 is "
       "class M, so the unit can fall; the documents are the owner's (section 7)")

REREAD = [("MMT", "C5.2"), ("CCO", "C5.2")]

# ---- C5.2's one published 1.0 outside D28's population, re-checked as class M (reading 3.7) -----------------------
MOOT = ("moot: the entry is the existing system and requires no transition, as audited (code N), and v2.0's scope, "
        "which asks that a transition's elements be shown feasible, leaves nothing to show (reading 3.7)")
U("SQ", "C5.2", 1.0, [("M", MOOT, REP + "SQ C5.2")] + [("M", "moot, as clause 1 (reading 3.7)", REP + "SQ C5.2")] * 4,
  note="the one C5.2 1.0 outside D28's population (the audit coded every clause N); C5.2 is class M, so it is "
       "re-checked here with the rest of C5.2 rather than left for stage 2, as part (b8)'s reading 3.8 did for C4.3")
CLASSM = [("SQ", "C5.2")]

# ---- C5.4 Political Coalition Potential (reading 3.5) -------------------------------------------------------------
U("NSD", "C5.4", 1.0, [
    ("C", "High public satisfaction (70-85%)", AUD),
    ("C", "in the ISSP's 2016 Role of Government module, {SPEND} of those answering in each of the four countries "
          "wanted government spending on health, and on old age pensions, kept at its level or raised, and {RESP} held "
          "that health care for the sick and a decent standard of living for the old should be the government's "
          "responsibility; wanting the system's core provision kept or raised opposes its repeal a fortiori "
          "(reading 3.5)", ISSP),
    ("C", "the configuration's universal social insurance and public services have been kept through every change of "
          "government since they were built, including centre-right governments in all four countries: Sweden "
          "1976-1982, 1991-1994, 2006-2014 and from 2022; Denmark 1982-1993, 2001-2011 and 2015-2019; Norway "
          "1981-1986, 1989-1990, 1997-2000, 2001-2005 and 2013-2021; Finland 1991-1995, 2015-2019 and from 2023 "
          "(reading 3.5)", REP + "NSD C5.4; the four countries' records of governments")],
  flag=([0.5], "read as requiring a record for every institution the entry names as defining, strong labor unions and "
               "progressive taxation as well as the social programmes, clause 3 is not shown on the evidence located; the "
               "interpretation check read the record so (reading 3.8)"),
  note="the audit coded clause 1 A and clauses 2 and 3 silent; both are estimated on the configuration's record")

U("CCO", "C5.4", 0.5, [
    ("C", "Alaska PFD demonstrates 80%+ approval across the spectrum", AUD),
    ("U", "the design's documents state no projection of opposition to its repeal; its roadmap assumes full bipartisan "
          "political support with legislative supermajorities and a public mandate through 70%+ approval ratings, an "
          "assumption, not an estimate; the Alaska dividend's record is one component's, and the design's other "
          "components (the expiring currency, Public Trust Foundations, the portal, the zones) have none "
          "(reading 3.5)", REP + "CCO C5.4; " + ROADMAP + "; " + MODEL),
    ("U", "no record or projection of the design's survival across changes of administration is stated; the modelling "
          "paper puts political resistance in 34% of its scenarios and national implementation's success at 71%, "
          "neither of which is survival across administrations (reading 3.5)", REP + "CCO C5.4; " + MODEL + "; " + SIM)],
  note="clause 1 is carried as audited on the unit's own text (section 2's rule), although the phrase is a component's "
       "approval; the interpretation check tests the carry (reading 3.8)")

# ---- C5.5 Cultural Adaptability (reading 3.6) ----------------------------------------------------------------------
U("PE", "C5.5", 0.5, [
    ("U", "the entry's text addresses cultural variation only (different communities could have different consumption "
          "patterns, work structures) and states no viability across high-, middle- and low-income economies "
          "(reading 3.6)", REP + "PE C5.5"),
    ("C", "Councils respect cultural variation", AUD),
    ("C", "Flexible system accommodating diverse values", AUD),
    ("U", "no economy has been organised on the design: its councils, balanced job complexes and participatory planning "
          "have not operated as a system anywhere, so there is no operation across diverse implementations to "
          "validate; the corpus scores CCO-PTF-CIP-SZH's C5.5 0.5 on the same ground (comprehensive implementation "
          "validation is limited to modeling), applied alike (reading 3.6)", REP + "PE C5.5 and CCO C5.5")],
  note="the audit coded clauses 2 and 3 A and clauses 1 and 4 silent")

U("MC", "C5.5", 1.0, [
    ("C", "and low-income context", AUD),
    ("C", "at least five cultural contexts", AUD),
    ("C", "the design fixes no parameter centrally: each network sets its members' credit limits on their demonstrated "
          "capacity to contribute and adjusts its own rules, and its implementations differ in kind, most with no "
          "interest or fee on balances and some with demurrage; parameters that each network sets, with no common "
          "value, meet a 40% adjustment range by construction (reading 3.6)", MCDOC + "C1.2a, C1.2b and C2.4"),
    ("C", "a genuinely broad implementation record", AUD)],
  flag=([0.5], "read as requiring a documented range of at least 40% in a named parameter, the entry gives no figure, "
               "and clause 3 is not shown (reading 3.6)"),
  note="the audit coded clause 3 silent and the other three A")

# ---- A codes on scoped clauses: carried after re-reading (reading 3.2), or estimated --------------------------------
REREAD_CARRIED = [("IF", "C5.2", 0), ("IF", "C5.2", 1), ("IF", "C5.2", 2), ("IF", "C5.2", 4), ("NSD", "C5.2", 0),
                  ("SC", "C5.2", 0)]
REREAD_ESTIMATED = [("LM", "C5.2", 0)]

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 11, "per_criterion": {"C5.2": 4, "C5.4": 2, "C5.5": 2}, "reread": 2,
          "stand": [("MC", "C5.5"), ("NSD", "C5.4"), ("SQ", "C5.2")], "points_b": 3.0, "rise": [],
          "fall": [("CCO", "C5.2")], "silent": 20,
          "not_estimated": [("LM", "C5.2", 2), ("LM", "C5.2", 3), ("LM", "C5.2", 4), ("NSD", "C5.2", 2),
                            ("NSD", "C5.2", 3), ("NSD", "C5.2", 4), ("SC", "C5.2", 2), ("SC", "C5.2", 3),
                            ("SC", "C5.2", 4)],
          "flags_added": [("MC", "C5.5"), ("NSD", "C5.4")], "flags_removed": [], "flags_replaced": [("IF", "C5.2")],
          "remaining": 0, "published_ones": {"C5.2": 7, "C5.4": 2, "C5.5": 4},
          "ones_left": {"C5.2": ["SQ"], "C5.4": ["NSD"], "C5.5": ["MC", "IF", "OS"]}, "first": ("CCO", 18.0, 17.0)}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    r4 = load("r4_audit_s35", AUDIT)
    mods = [load(mod, path) for _, mod, path, _ in PRIOR]
    rs = mods[0]
    f1 = rs.f1
    crit = json.loads(rs.read(CRIT44))["criteria"]
    cids = [c["id"] for c in crit]
    v2 = {c["id"]: c for c in json.loads(rs.read(CRITERIA))["criteria"]}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}
    prior = tuple(m.UNITS for m in mods)

    print(f"NEEC rescoring pass, part (b), ninth group: C5.2, C5.4, C5.5 on the v2.0 clauses ({RECORD})")
    print(f"inputs: {CRITERIA}, {CRIT44}, {CORPUS}, {CSV}, {AUDIT}, " + ", ".join(p for _, _, p, _ in PRIOR)
          + f", {RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION AND THE v2.0 CLAUSES")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    done = set().union(*(set(p) for p in prior))
    partb = [k for k in d28 if k not in prior[0]]
    grp = [k for k in partb if k[1] in GROUP and k not in done]
    new = {k: r for k, r in UNITS.items() if k not in REREAD and k not in CLASSM}
    check(len(d28) == 134 and len(partb) == 101, "D28's population 134; part (b) 101")
    per = {g: sum(1 for k in grp if k[1] == g) for g in GROUP}
    check(sorted(new) == sorted(grp) and per == EXPECT["per_criterion"] and all(vec[c][k] == 1.0 for c, k in new)
          and not set(new) & done,
          f"this group holds exactly the part (b) units of C5.2, C5.4 and C5.5 ({len(grp)}: "
          + ", ".join(f"{g} {per[g]}" for g in GROUP) + "), every one a corpus 1.0 and none re-estimated before")
    pub = {g: sorted(c for c in vec if vec[c][g] == 1.0) for g in GROUP}
    in_a = {g: sorted(c for (c, k) in prior[0] if k == g) for g in GROUP}
    outside = {g: sorted(c for c in pub[g] if (c, g) not in d28) for g in GROUP}
    check({g: len(v) for g, v in pub.items()} == EXPECT["published_ones"]
          and all(sorted([c for c, k in new if k == g] + in_a[g] + outside[g]) == pub[g] for g in GROUP)
          and sorted(REREAD) == sorted((c, g) for g in GROUP for c in in_a[g])
          and [prior[0][k]["verdict"] for k in REREAD] == [0.5, 1.0] and len(REREAD) == EXPECT["reread"]
          and outside == {"C5.2": ["SQ"], "C5.4": [], "C5.5": ["IF", "OS"]}
          and sorted(CLASSM) == [(c, g) for g in GROUP if CLS[g] == "M" for c in outside[g]]
          and all(ch == "N" for ch in dict(((u[0], u[1]), u[2]) for u in r4.UNITS)[("SQ", "C5.2")])
          and not any((c, "C5.5") in done for c in outside["C5.5"]) and len(UNITS) == EXPECT["units"],
          "with part (a)'s, they are every published 1.0 of the three criteria in D28's population (" + "; ".join(
              f"{g} {len(pub[g])} published, part (a) took " + (", ".join(in_a[g]) or "none") for g in GROUP) +
          "); outside it, Status Quo's C5.2, which the audit coded N on every clause, re-checked here as class M "
          "(reading 3.7), and Islamic Finance's and Ostrom's C5.5, class U, coded A on every clause and carried; "
          f"part (a)'s {len(REREAD)} (MMT at 0.5, CCO at 1.0 there) are re-read here on the v2.0 clauses")
    for g in GROUP:
        print(f"  {g}: " + ", ".join(c for c, k in grp if k == g) + "; re-read from part (a): "
              + (", ".join(c for c, k in REREAD if k == g) or "none"))

    def words(t):  # a clause moved to the head of its threshold gains a capital; the words are what must match
        return t[:1].lower() + t[1:]
    same = all(words(v2[g]["definition"]["clauses"][i]) == words(r4.CLAUSES[g][MAP[g][i]][0])
               for g in GROUP for i in range(len(MAP[g])))
    whole = all(len(r4.CLAUSES[g]) == len(MAP[g]) == len(v2[g]["definition"]["clauses"]) for g in GROUP)
    d52 = v2["C5.2"]["definition"]
    check(same and whole and all(v2[g]["revision"]["cls"] == CLS[g] for g in GROUP)
          and d52.get("clause_scope") == SCOPE and d52["pass_threshold"].endswith(SCOPE)
          and "shown feasible rather than only planned" in d52["requirement"]
          and v2["C5.2"]["revision"]["codes"] == ["R4"]
          and all("clause_scope" not in v2[g]["definition"] and not v2[g]["revision"]["codes"] for g in ("C5.4", "C5.5")),
          "v2.0's clauses: C5.2 (class M, R4) keeps its five Session 44 clauses verbatim under the new scope, each "
          "shown feasible by precedent or component evidence, and its requirement asks that each be shown feasible "
          "rather than only planned; C5.4 and C5.5 (class U) keep theirs verbatim, with no scope")
    for g in GROUP:
        for i, t in enumerate(v2[g]["definition"]["clauses"]):
            print(f"  {g} ({i + 1}) {t}  [verbatim; Session 44 clause {MAP[g][i] + 1}]")
    print(f"  C5.2 scope: {SCOPE}")

    # [2] Nordic Social Democracy's C5.4 clause 2 ------------------------------------------------------------------
    print("\n[2] NORDIC SOCIAL DEMOCRACY, C5.4 CLAUSE 2: THE ISSP 2016 ROLE OF GOVERNMENT MODULE (reading 3.5)")
    countries = ("Denmark", "Finland", "Norway", "Sweden")
    rows = ["| Item (ISSP 2016) | Answers counted | Denmark | Finland | Norway | Sweden |", "|---|---|---:|---:|---:|---:|"]
    share = {}
    for v, (label, k) in ISSP_ITEMS.items():
        counted = "much more, more, the same" if k == 3 else "definitely or probably should be"
        share[v] = {c: sum(ISSP_PCT[v][c]) for c in countries}
        rows.append(f"| {v}, {label} | {counted} | " + " | ".join(f"{share[v][c]:.1f}%" for c in countries) + " |")
    issp_table = "\n".join(rows)
    print(issp_table)
    spend = [share[v][c] for v in ("v14", "v18") for c in countries]
    resp = [share[v][c] for v in ("v23", "v24") for c in countries]
    check(all(len(ISSP_PCT[v][c]) == ISSP_ITEMS[v][1] and all(0 < x < 100 for x in ISSP_PCT[v][c])
              for v in ISSP_ITEMS for c in countries)
          and min(spend) >= REPEAL and min(resp) >= REPEAL,
          f"in each country at least {min(spend):.1f}% wanted spending on health and on pensions kept or raised, and at "
          f"least {min(resp):.1f}% held both to be the government's responsibility: every figure clears the {REPEAL:.0f}% "
          "bar, compared here in code")
    rng = lambda xs: f"{min(xs):.1f} to {max(xs):.1f}%"
    st, est, src = UNITS[("NSD", "C5.4")]["clauses"][1]
    UNITS[("NSD", "C5.4")]["clauses"][1] = (st, est.format(SPEND=rng(spend), RESP=rng(resp)), src)

    # [3] records --------------------------------------------------------------------------------------------------
    print("\n[3] THE RECORDS")
    bad, tally = [], {k: 0 for k in STATUS}
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(v2[key[1]]["definition"]["clauses"]):
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {len(v2[key[1]]['definition']['clauses'])}")
        for k, (st, est, src) in enumerate(rec["clauses"]):
            tally[st] = tally.get(st, 0) + 1
            if st not in STATUS or not est.strip() or (not src.strip() and not est.startswith(NOTEST)):
                bad.append(f"{key} clause {k + 1}: status {st!r}, or an empty estimate or source")
            if "|" in est + src + (rec["flag"][1] if rec["flag"] else "") + rec["note"] or "{" in est:
                bad.append(f"{key} clause {k + 1}: a pipe character or an unfilled field")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per v2.0 clause, in the Pass Threshold's order, each with its estimate "
                   "and, unless it is left not estimated, its source")
    print("  clause statuses: " + ", ".join(f"{STATUS[k]} {v}" for k, v in tally.items()))

    # [4] the rule -------------------------------------------------------------------------------------------------
    print("\n[4] THE RULE (D28) AND THE AUDIT'S CODES")
    wrong = [k for k, r in UNITS.items() if rs.verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong and all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()),
          "every verdict follows D28 (1.0 only if every clause is cleared or moot), and none is 0.0 (D28(f))",
          str(wrong))
    stand = sorted(k for k, r in UNITS.items() if r["verdict"] == 1.0)
    points_b = sum(1.0 - r["verdict"] for r in new.values())
    rise = sorted(k for k in REREAD if UNITS[k]["verdict"] > prior[0][k]["verdict"])
    fall = sorted(k for k in REREAD if UNITS[k]["verdict"] < prior[0][k]["verdict"])
    check(stand == sorted(EXPECT["stand"]) and points_b == EXPECT["points_b"] and rise == EXPECT["rise"]
          and fall == EXPECT["fall"],
          f"of the part (b) units {sum(1 for k in new if k in stand)} stand ("
          + ", ".join(f"{c} {k}" for c, k in stand if (c, k) in new) + f") and {sum(1 for k in new if k not in stand)} "
          f"become 0.5 ({f1(points_b)} points); of part (a)'s re-read units MMT's stays 0.5 and CCO-PTF-CIP-SZH's falls "
          "from 1.0 to 0.5 (class M)")
    check(all(UNITS[k]["verdict"] == 1.0 == vec[k[0]][k[1]] and all(s == "M" for s, _, _ in UNITS[k]["clauses"])
              for k in CLASSM),
          "Status Quo's C5.2, re-checked as class M, stands: every clause moot, as audited (reading 3.7)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    code = {(c, k, i): reg[(c, k)][MAP[k][i]] for (c, k) in UNITS for i in range(len(MAP[k]))}
    departs = sorted(x for x, ch in code.items() if x[2] not in SCOPED[x[1]] and x[:2] in new
                     and ch == "A" and UNITS[x[:2]]["clauses"][x[2]][0] != "C")
    carried_u = sorted(x for x, ch in code.items() if not SCOPED[x[1]] and x[:2] in new and ch == "A")
    phrases = {(u[0], u[1]): [p for p in u[3]] for u in r4.UNITS}
    as_phrase = all(UNITS[x[:2]]["clauses"][x[2]][1] in phrases[x[:2]] for x in carried_u)
    check(not departs and carried_u and as_phrase
          and all(UNITS[x[:2]]["clauses"][x[2]][2] == AUD for x in carried_u),
          f"no departure from the audit's A codes on C5.4 and C5.5 (class U): their {len(carried_u)} A codes in this "
          "group's part (b) units are carried as cleared on the unit's own text, each with the audit's phrase")
    re_a = sorted(x for x, ch in code.items() if x[2] in SCOPED[x[1]] and x[:2] in new and ch == "A")
    carried = sorted(x for x in re_a if UNITS[x[:2]]["clauses"][x[2]][0] == "C")
    estimated = sorted(x for x in re_a if x not in carried)
    check(carried == sorted(REREAD_CARRIED) and estimated == sorted(REREAD_ESTIMATED)
          and all(UNITS[x[:2]]["clauses"][x[2]][2] != AUD for x in re_a),
          f"the audit coded A {len(re_a)} clauses v2.0 places under C5.2's scope: {len(carried)} cleared after "
          f"re-reading against it, with the precedent named, and {len(estimated)} estimated (reading 3.2)")
    silent = {(c, k, i) for (c, k) in new for i in range(len(MAP[k])) if code[(c, k, i)] == "S"}
    notest = sorted((k[0], k[1], i) for k, r in UNITS.items() for i, (st, est, _) in enumerate(r["clauses"])
                    if est.startswith(NOTEST))
    fixed = all(UNITS[(c, k)]["clauses"][i][0] == "U" and any(
        j != i and st in "SUR" and not est.startswith(NOTEST)
        for j, (st, est, _) in enumerate(UNITS[(c, k)]["clauses"])) for c, k, i in notest)
    notest_b = [x for x in notest if x[:2] in new]
    est_status = {}
    for c, k, i in sorted(silent):
        if (c, k, i) in notest:
            continue
        st = UNITS[(c, k)]["clauses"][i][0]
        est_status[st] = est_status.get(st, 0) + 1
    check(len(silent) == EXPECT["silent"] and set(notest_b) <= silent and notest_b == sorted(EXPECT["not_estimated"])
          and fixed,
          f"the audit coded {len(silent)} v2.0 clauses of this group's part (b) units silent; "
          f"{len(silent) - len(notest_b)} are estimated here (" + ", ".join(
              f"{STATUS[s]} {n}" for s, n in sorted(est_status.items())) + f"), and {len(notest_b)} are left not "
          "estimated, each in a unit whose verdict another clause fixes (clause 2 of C5.2, or clauses 1 and 2)")
    print(f"  also left not estimated: {len(notest) - len(notest_b)} clauses of part (a)'s re-read MMT unit, which "
          "clause 1 fixes (part (a) recorded them not shown, with no source)")
    rapid = [k for k in new if k[1] == "C5.2"]
    check(all(UNITS[k]["verdict"] == 0.5 for k in rapid)
          and sorted(k for k in rapid if UNITS[k]["clauses"][1][0] != "C") == [("LM", "C5.2"), ("NSD", "C5.2"),
                                                                               ("SC", "C5.2")],
          "every part (b) unit of C5.2 becomes 0.5: Nordic Social Democracy, Libertarian Minarchism and Stakeholder "
          "Capitalism on the rapid clause, Islamic Finance on resource requirements (reading 3.3)")

    # [5] reach ----------------------------------------------------------------------------------------------------
    print("\n[5] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = sorted((c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R")
    was_r = sorted(x for x in r4.REACH if (x[0], x[1]) in UNITS)
    check(now_r == was_r == [], "no clause of this group is out of reach, and the audit coded none so")

    # [6] flags ----------------------------------------------------------------------------------------------------
    print("\n[6] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b8) and 48.3)")
    blocks = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}

    def changes(units):
        add = sorted(k for k, r in units.items() if r["flag"] and k not in had)
        rem = sorted(k for k, r in units.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
        return add, rem
    added, removed = changes(new)
    replaced = sorted(k for k, r in new.items() if k in had and r["verdict"] in had[k]["alternatives"] and r["flag"]
                      and not set(r["flag"][0]) & set(had[k]["alternatives"]))
    kept = sorted(k for k in new if k in had and k not in replaced)
    kept_a = not prior[0][("MMT", "C5.2")]["flag"] and not UNITS[("MMT", "C5.2")]["flag"] \
        and not prior[0][("CCO", "C5.2")]["flag"] and UNITS[("CCO", "C5.2")]["flag"]
    check(added == sorted(EXPECT["flags_added"]) and removed == sorted(EXPECT["flags_removed"])
          and replaced == sorted(EXPECT["flags_replaced"]) and not kept and kept_a,
          f"flags added {len(added)} ({', '.join(f'{c} {k}' for c, k in added)}); removed {len(removed)}; replaced "
          f"{len(replaced)} ({', '.join(f'{c} {k}' for c, k in replaced)}: its register's flag toward 0.5 is resolved "
          "by the verdict, and one toward 1.0 replaces it); of part (a)'s re-read units CCO-PTF-CIP-SZH's C5.2 gains a "
          "flag toward 1.0")
    merged, part_of = {}, {}
    for (tag, _, _, sess), part in zip(PRIOR, prior):
        merged.update(part)
        part_of.update({k: (tag, sess) for k in part})
    before = dict(merged)
    merged.update(UNITS)
    part_of.update({k: THIS for k in UNITS})
    a0, _ = changes(before)
    adds, rems = changes(merged)
    moved_e = sorted({k[0] for k in adds + rems + replaced})
    flag_line = (f"Flags added in this group: {len(added)} to part (b) units and 1 to a re-read unit (CCO C5.2); "
                 f"removed: {len(removed)}; replaced: {len(replaced)} ({', '.join(f'{c} {k}' for c, k in replaced)}, "
                 f"toward 1.0 in place of 0.5). Flags added by the pass so far: {len(adds)} (against {len(a0)} before "
                 f"this group); removed: {len(rems)}. Across the pass so far, {len(moved_e)} entries' flag registers "
                 f"change ({', '.join(moved_e)}).")
    print("  " + flag_line)

    # [7] consequences ---------------------------------------------------------------------------------------------
    print("\n[7] CONSEQUENCES (computed here on the published 26-criterion structure; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        vsteps.append(v)
    vp, vn = vsteps[-2], vsteps[-1]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, mp, after = steps[0], steps[-2], steps[-1]
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    left_units = [k for k in partb if k not in done and k not in UNITS]
    left, perc = {}, {}
    for c, k in left_units:
        left[c] = left.get(c, 0) + 1
        perc[k] = perc.get(k, 0) + 1
    check(len(left_units) == EXPECT["remaining"], f"{len(left_units)} D28 units remain for part (b)")
    rem_line = ("Left for part (b): none. This group finishes it: all 101 of part (b)'s D28 units are re-estimated."
                if not left_units else f"Left for part (b): {len(left_units)} D28 units.")
    print("  " + rem_line)
    order = list(names)
    ones = {g: [c for c in order if vn[c][g] == 1.0] for g in GROUP}
    check(ones == EXPECT["ones_left"],
          "1.0s each of this group's criteria keeps: " + "; ".join(
              f"{g} {len(ones[g])} (published {len(pub[g])})" for g in GROUP))
    tags = ["published"] + [t for t, _, _, _ in PRIOR] + [THIS[0]]
    emptied = {}
    for tag, v in zip(tags, vsteps):
        for k in cids:
            if k not in emptied and not any(v[c][k] == 1.0 for c in v):
                emptied[k] = tag
    check(all(any(vsteps[0][c][k] == 1.0 for c in vec) for k in cids) and len(emptied) == 9
          and not [k for k in emptied if emptied[k] == THIS[0]],
          f"no entry scores 1.0 on {len(emptied)} criteria after this group, as before it: each of this group's three "
          "keeps a 1.0")
    ones_line = ("After this group C5.2 keeps " + str(len(ones["C5.2"])) + " score of 1.0 (" + ", ".join(ones["C5.2"])
                 + "; 7 published), C5.4 keeps " + str(len(ones["C5.4"])) + " (" + ", ".join(ones["C5.4"])
                 + "; 2 published) and C5.5 keeps " + str(len(ones["C5.5"])) + " (" + ", ".join(ones["C5.5"])
                 + "; 4 published). Every criterion had a 1.0 in the published corpus; after part (b) no entry scores "
                 "1.0 on " + str(len(emptied)) + " of them: "
                 + ", ".join(f"{k} (emptied in part {emptied[k]})" for k in cids if k in emptied) + ".")
    print("  " + ones_line)
    rb, rp, rn = rs.ranks(base["total"]), rs.ranks(mp["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After part (b8) (rank) | After part (b) (rank) | Change here | Failures | Tier | "
            "D28 units left | Floor if all fall |",
            "|---|---:|---:|---:|---:|---:|---|---:|---:|"]
    for c in rs.order_codes(names, base):
        lf = left.get(c, 0)
        rows.append(f"| {c} | {f1(base['total'][c])} ({rb[c]}) | {f1(mp['total'][c])} ({rp[c]}) | "
                    f"{f1(after['total'][c])} ({rn[c]}) | {f1(after['total'][c] - mp['total'][c])} | "
                    f"{after['fail'][c]} | {rs.tier(after['fail'][c])} | {lf} | {f1(after['total'][c] - 0.5 * lf)} |")
    cons_table = "\n".join(rows)
    pp, fp = rs.dominance(vp, cids)
    pn, fn = rs.dominance(vn, cids)
    gained = sorted(set(pn) - set(pp), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(pp) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    n_all = len(merged)
    st_all = sum(1 for r in merged.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for r in merged.values())
    check(len(first) == 1 and (first[0], mp["total"][first[0]], after["total"][first[0]]) == EXPECT["first"],
          f"first place: {first[0]}, {f1(mp['total'][first[0]])} after part (b8), "
                                                 f"{f1(after['total'][first[0]])} now")
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(pp)} after part (b8) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(fp)} (" + ", ".join(c for c in order if c in fn) + f"). First place: {first[0]}, "
                f"{f1(mp['total'][first[0]])} after part (b8), {f1(after['total'][first[0]])} now. Across parts (a) and "
                f"(b) {n_all} units have been re-estimated, each counted once: {st_all} stand and {n_all - st_all} are "
                f"at 0.5 ({f1(pts_all)} points).")
    print("  " + dom_line)

    # [8] the ledger -----------------------------------------------------------------------------------------------
    print("\n[8] THE SCORE LEDGER (published total, each part's change, the total now; 26 criteria)")
    ltags = tags[1:]
    csv_rows = list(csv.DictReader(rs.read(CSV).splitlines()))
    csv_tot = {r["system"]: (float(r["total_score"]), int(r["failures"])) for r in csv_rows}
    check(all(csv_tot[names[c]] == (base["total"][c], base["fail"][c]) for c in names),
          f"the published totals and failure counts in {CORPUS} equal {CSV}'s for all {len(corpus)} entries")
    rows = ["| Entry | Published | " + " | ".join(ltags) + " | Now | Re-estimated | At 0.5 |",
            "|---|---:|" + "---:|" * len(ltags) + "---:|---:|---:|"]
    sums_ok = True
    for c in rs.order_codes(names, base):
        deltas = [steps[i + 1]["total"][c] - steps[i]["total"][c] for i in range(len(ltags))]
        mine = [k for k in merged if k[0] == c]
        low = [k for k in mine if merged[k]["verdict"] == 0.5]
        sums_ok = sums_ok and abs(sum(deltas) - (after["total"][c] - base["total"][c])) < 1e-9
        rows.append(f"| {c} | {f1(base['total'][c])} | " + " | ".join("" if d == 0 else f1(d) for d in deltas)
                    + f" | {f1(after['total'][c])} | {len(mine)} | {len(low)} |")
    ledger = "\n".join(rows)
    check(sums_ok, "each entry's changes, part by part, sum to the difference between its published total and its "
                   "total now")

    # [9] anchors --------------------------------------------------------------------------------------------------
    print("\n[9] ANCHOR EXAMPLES THE PASS SO FAR MOVES (the published anchors, criteria_s44_snapshot.json)")
    code_of = {v: k for k, v in names.items()}
    hits, empty = [], []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                cd = code_of.get(ex["system"])
                if cd and (cd, c["id"]) in merged and merged[(cd, c["id"])]["verdict"] != ex["cited"]:
                    hits.append(f"{c['id']}'s {band} example, {cd} (part {part_of[(cd, c['id'])][0]})")
                    if not any(vn[x][c["id"]] == float(band) for x in vn):
                        empty.append((c["id"], band))
    here = [h for h in hits if f"part {THIS[0]}" in h]
    check(here == ["C5.2's 1.0 example, CCO (part (b9))", "C5.4's 1.0 example, CCO (part (b9))",
                   "C5.5's 1.0 example, PE (part (b9))"] and len(hits) == 15 and len(empty) == 9
          and not [e for e in empty if e[0] in GROUP],
          f"this group moves three anchor examples, C5.2's and C5.4's 1.0 (CCO-PTF-CIP-SZH) and C5.5's 1.0 (Participatory "
          f"Economics), {len(hits)} across the pass; each band keeps a corpus unit at its value (Status Quo, Nordic Social "
          f"Democracy, Mutual Credit), so the {len(empty)} bands left with none are unchanged")
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) + ". Bands whose example the pass moves "
                   "and which no corpus unit then scores at their value: " + ", ".join(f"{c}'s {b}" for c, b in empty) + ".")
    print("  " + anchor_line)

    # [10] the record ----------------------------------------------------------------------------------------------
    print(f"\n[10] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in new]
    unit_order = ([k for g in GROUP for k in unit_order if k[1] == g] + REREAD + CLASSM)

    def was(key):
        if key in REREAD:
            return f"{f1(prior[0][key]['verdict'])} (part (a))"
        return "1.0 (class M)" if key in CLASSM else "1.0"
    t = {}
    rows = ["| Entry | Criterion | Clauses | Verdict | Flag |", "|---|---|---|---|---|"]
    for key in unit_order:
        rec = UNITS[key]
        fl = f"alternative {rs.fmt_alts(rec['flag'][0])}" if rec["flag"] else ""
        rows.append(f"| {key[0]} | {key[1]} | {' '.join(s for s, _, _ in rec['clauses'])} | "
                    f"{was(key)} → {f1(rec['verdict'])} | {fl} |")
    t["summary"] = "\n".join(rows)
    for key in unit_order:
        rec, (cd, k) = UNITS[key], key
        head = f"#### {cd} {k} {v2[k]['name']}: {was(key)} → {f1(rec['verdict'])}"
        if rec["flag"]:
            head += " — flagged as contestable"
        lines = [head, "", "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (st, est, src) in enumerate(rec["clauses"]):
            lines.append(f"| {i + 1} | {v2[k]['definition']['clauses'][i]} | {STATUS[st]} | {est} | {src or '—'} |")
        if rec["flag"]:
            lines += ["", f"*Flag:* alternative {rs.fmt_alts(rec['flag'][0])}: {rec['flag'][1]}."]
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {cd} {k}"] = "\n".join(lines)
    t["issp"], t["consequences"], t["dominance"], t["remaining"] = issp_table, cons_table, dom_line, rem_line
    t["flags"], t["ledger"], t["ones"], t["anchors"] = flag_line, ledger, ones_line, anchor_line
    GENERATED.clear()
    GENERATED.update(t)
    if "--tables" in sys.argv[1:]:
        sys.stdout = sys.__stdout__
        print(json.dumps(t, ensure_ascii=False))
        return 0
    record = rs.read(RECORD) if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(cons_table)
    print()
    print(ledger)
    print("\nRESCORING PART (B), NINTH GROUP, COMPUTED; PART (B) COMPLETE." if ok else
          "\nRESCORING PART (B), NINTH GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
