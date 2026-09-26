#!/usr/bin/env python3
"""
rescoring_s51.py -- NEEC rescoring pass (decisions D28, D29, D31), stage 2, group 2.1: CCO-PTF-CIP-SZH's units that
rest on the design's own modelling, read on its published model at v4.20
==================================================================================================================
Session 51. Parts (a) and (b) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s50.md (rescoring_s37.py to rescoring_s50.py;
rescoring_s48.py re-read C4.4 on decision 48.3). The owner announced version 4.20 of the Compassionism Simulation, the
design's published model, on 2026-09-26. This group moves the pass's pin to it (reading 3.1), re-reads the published
1.0s whose rationale rests on a figure from the entry's own modelling (reading 3.2: a scan of every published 1.0 finds
them among CCO-PTF-CIP-SZH's units only), re-checks the design's C1.1 as class I on the Societal Poverty Line (readings
3.3 and 3.4), and checks against v4.20 the reopening condition or the model reading of every other unit of the design
that the pass re-estimated (reading 3.9). It changes no file and no score: the pass's changes are applied by generator
when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). The clauses are v2.0's
(criteria.json). C1.2b and C3.3 have one clause each and lie outside D28's population; the other four criteria map
their v2.0 clauses to the Session 44 clauses the audit coded. Class U A codes are carried as cleared on the unit's own
text (C3.2, C5.3); C1.4's two A codes are departed from, each with its reason (reading 3.6).

CHECKS: the group against a scan of every published 1.0's rationale; the v2.0 clauses and classes; the simulation runs
(cco_simulation_checks_s51_output.txt: its digest, its checks, every figure this record quotes); every record complete;
the rule; the audit's codes carried or departed from; reach; flags against the summary blocks, cumulatively with parts
(a) and (b); the reopening conditions of the design's other re-estimated units; the consequences of the pass so far on
the published 26-criterion structure (totals, ranks, failures, tiers, dominance, frontier, the criteria left with no
1.0), the score ledger, the anchor examples the pass so far moves; and that NEEC_Rescoring_s51.md contains every
generated table, and every table of the simulation runs, verbatim.

Usage: python3 rescoring_s51.py   (reads criteria.json (v2.0), criteria_s44_snapshot.json, neec_corpus.json,
                                   neec_scores.csv, NEEC_Report_v1_6.md and the ten scoring documents r4_audit_s35.py
                                   names, r4_audit_s35.py, rescoring_s37.py to rescoring_s50.py and the files they
                                   read, cco_simulation_checks_s51_output.txt and NEEC_Rescoring_s51.md beside itself;
                                   writes nothing)
       python3 rescoring_s51.py --tables   (prints the generated tables as JSON, for assembling the record)
Prints file names only. Deterministic.
"""
import csv
import hashlib
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CRIT44, CORPUS, CSV, AUDIT = ("criteria.json", "criteria_s44_snapshot.json", "neec_corpus.json",
                                        "neec_scores.csv", "r4_audit_s35.py")
PRIOR = (("(a)", "rescoring_s37", "rescoring_s37.py", 37), ("(b1)", "rescoring_s38", "rescoring_s38.py", 38),
         ("(b2)", "rescoring_s39", "rescoring_s39.py", 39), ("(b3)", "rescoring_s40", "rescoring_s40.py", 40),
         ("(b4)", "rescoring_s41", "rescoring_s41.py", 41), ("(b5)", "rescoring_s42", "rescoring_s42.py", 42),
         ("(b6)", "rescoring_s43", "rescoring_s43.py", 43), ("(b7)", "rescoring_s47", "rescoring_s47.py", 47),
         ("48.3", "rescoring_s48", "rescoring_s48.py", 48), ("(b8)", "rescoring_s49", "rescoring_s49.py", 49),
         ("(b9)", "rescoring_s50", "rescoring_s50.py", 50))
THIS = ("(2.1)", 51)
RECORD = "NEEC_Rescoring_s51.md"
SIMOUT, SIMOUT_MD5 = "cco_simulation_checks_s51_output.txt", "b4f481e70166f2f01d1a294765984e14"
PINS = {"harness.js": "fe6fa4a3f82a2d572c5e6914cc2345f2", "index.html": "c333b6326b95586515743dba6647ca2a"}
GROUP = ("C1.1", "C1.2b", "C1.4", "C3.2", "C3.3", "C5.3")
CLS = {"C1.1": "I", "C1.2b": "W", "C1.4": "I", "C3.2": "U", "C3.3": "W", "C5.3": "U"}
# v2.0 clause index -> the Session 44 clause the audit coded (multi-clause criteria; every clause verbatim, none deleted)
MAP = {"C1.1": (0, 1), "C1.4": (0, 1), "C3.2": (0, 1, 2), "C5.3": (0, 1, 2, 3)}
SINGLE = ("C1.2b", "C3.3")
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
SIM = ("Compassionism Simulation at 5a7a7b1 (v4.20), harness.js (md5 fe6fa4a3) and index.html (md5 c333b632); "
       + SIMOUT)
CONTRIB = "the simulation's CONTRIBUTING.md at 5a7a7b1 (md5 bba4ef73)"
HUB = "research hub at 8e8a6ba"
MODEL = HUB + ", economic-modeling-simulation.html (md5 86dda39b)"
FRAME = HUB + ", cco-ptf-integrated-framework.html (md5 10ab8364)"
BLEI = HUB + ", basic-living-economic-index.html (md5 0d1481fb)"
INFL = HUB + ", dual-currency-inflation.html (md5 329235ce)"
WB = ("Foster, Jolliffe, Lara Ibarra, Lakner and Tetteh-Baah, Global Poverty Revisited Using 2021 PPPs and New Data on "
      "Consumption, World Bank Policy Research Working Paper 11137 (June 2025), section 3.4.1 (PDF md5 1128f547)")
PAPER_G = "NEEC_Paper_v1_4.md, Appendix G (G.2, G.7)"
REOPEN_TAG = "reading 3.9"

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in v2.0's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- the figures this record quotes from the simulation runs (each must appear verbatim in SIMOUT) ------------------
FIG = {
    "c11_spl": "| Reference (Full Integration) | Societal Poverty Line, cash income | 9.0% | 11.5% | none (27.9% higher) | "
               "0 of 500 at 90% | 9.6% | none (19.2% higher) |",
    "c11_splx": "| Reference (Full Integration) | Societal Poverty Line, incl. in-kind relief | 9.0% | 8.4% | 6.8% |",
    "c11_rel": "| Reference (Full Integration) | Relative income poverty (60% of median), cash | 15.3% | 18.1% | "
               "none (18.6% higher) |",
    "c11_bsk": "| Reference (Full Integration) | Basket poverty, net | 66.3% | 9.9% | 85.0% | 2 of 500 at 90% | 81.9% | "
               "87.9% |",
    "c11_adv_spl": "| Stress: Adverse Environment | Societal Poverty Line, cash income | 9.0% | 15.4% | none (71.7% higher) "
                   "| 0 of 500 at 85% | 17.2% | 10.5% |",
    "c11_largest": "(largest 87.9%) or 85% in the Adverse Environment (largest 57.9%)",
    "c11_adv_blei": "| Stress: Adverse Environment | BLEI poverty | 10.3% | 34.9% | none (238.5% higher) | 0 of 500 at 85% | "
                    "82.9% | 57.9% |",
    "gini_e": "| Reference (Full Integration) | EDC-adjusted (the engine's KPI) | 0.702 | 0.573 | 0.518 | 0 of 500 |",
    "gini_p": "| Reference (Full Integration) | net wealth, negatives at zero | 0.601 | 0.557 | 0.510 | 0 of 500 |",
    "c14_20": "| 20 | 11.5% / 8.4% | 15.1% / 9.4% | 15.3% / 27.1% | 9.9% / 40.9% | 56.2% | 57.7% |",
    "c14_25": "| 25 | 12.1% / 9.4% | 18.0% / 10.6% | 10.9% / 29.2% | 6.8% / 48.6% | 46.2% | 47.8% |",
    "c14_seeds": "seeds with SPL poverty (cash) below 8%: 0 of 500.",
    "c14_cap": "reaches its 0.10 cap in simulated year 13 (0-indexed); the year-15 branch computes 0.142",
    "c33_spl": "| above the Societal Poverty Line (cash income) | 20 | 88.5% | 84.6% | 4.4% |",
    "c33_dis": "| not in housing distress (the nearest measure to housing stability) | 20 | 90.4% | 64.4% | 28.8% |",
    "c31_part": "77.9% of the population at year 0 and 77.9% at year 20",
    "regression": "median BLEI 1975 d, BLEI poverty 13.2%, median wealth $570661, wealth poverty 15.8%, Gini 0.518, "
                  "System Stability 88.8%",
    "runner": "the runner reproduces runScenario() on all 500 seeds of all 8 scenarios",
    "sweep": "v4.20's automation sweep reproduced",
    "headline": "v4.20's refreshed headline reproduced",
}

# ---- C1.1 Poverty Elimination Capacity: part (b3)'s unit re-checked as class I (readings 3.3 and 3.4) --------------
U("CCO", "C1.1", 0.5, [
    ("S", "on the design's published model at v4.20, at the Full Integration settings its parameter file credits with "
          "98% (500 seeds, 20 years), poverty on the Societal Poverty Line, v2.0's indicator, computed from the engine's "
          "own cash incomes, is 9.0% at adoption and 11.5% at year 20, 27.9% higher, and 8.4% (6.8% lower) with the "
          "in-kind value of cost relief counted as income; on the modelling paper's own measure, income below 60% of the "
          "median, it rises from 15.3% to 18.1%; the largest reduction on any measure the engine reports is net basket "
          "poverty's, 85.0% against year 0 and 87.9% against the paired Baseline, on which 2 of 500 seeds reach 90% "
          "against year 0; the simulation's own documentation states that the papers' 98% is not produced by the engine "
          "and that the model behind it is not in its repository (readings 3.3 and 3.4)",
     SIM + "; " + WB + "; " + CONTRIB + ", v4.17 Release Notes (NEEC note 1)"),
    ("S", "in the Adverse Environment, the preset the engine's documentation names for stress criteria (recessions, AI "
          "automation and 2% inflation at the reference settings), no measure falls 85% against either comparator: the "
          "largest reduction is BLEI poverty's, 57.9% against the paired Baseline; poverty on the Societal Poverty Line "
          "rises from 9.0% to 15.4%, 71.7% above its level at adoption, and is 10.5% below the Baseline's; no seed "
          "reaches 85% against year 0 on any measure, and the Stress Test preset, which also weakens the settings, "
          "gives less (reading 3.3)", SIM + "; " + CONTRIB + ", v4.17 Release Notes (NEEC notes 5 and 6)")],
  note="part (b3)'s unit re-checked as class I: its record read the engine's two headcounts, not v2.0's indicator, so "
       "it is re-read on the Societal Poverty Line (reading 3.3); both clauses stay short and the unit stays 0.5. Part "
       "(b3)'s flag toward 1.0, the papers' figures credited at the modelling tier, is removed: the engine now carries "
       "the papers' own measure and shows no reduction on it (reading 3.4). The unit reopens if the model behind the "
       "papers' 98% is published and reproduces it, or if a later version of the simulation reaches 90% in the "
       "reference run and 85% in the Adverse Environment on the Societal Poverty Line")

# ---- C1.2b Prevention of Exploitative Accumulation (reading 3.5) --------------------------------------------------
U("CCO", "C1.2b", 0.5, [
    ("S", "on the design's published model at v4.20, at the reference settings (500 seeds), the wealth Gini at year 20 "
          "is 0.518 on the engine's EDC-adjusted net wealth, the figure it reports, and 0.510 on net wealth with negative "
          "holdings counted as zero; no seed is below 0.35 on either; the Gini falls from 0.601 at adoption, so the "
          "design's mechanisms narrow the distribution, but not to the bar; the rationale's projection under 0.35 is the "
          "modelling paper's 0.28 (the median of its runs), from a model not published in runnable form, and the design's "
          "BLEI paper states that the simulation measures 0.518 (N = 5,000, v4.4), more than double its stated target of "
          "0.25 (the engine's TARGET_GINI constant), a gap it calls large and honestly disclosed (reading 3.5)",
     SIM + "; " + MODEL + ", section 5.1; " + BLEI + ", section 9")],
  note="C1.2b is class W and single-clause, outside D28's population; it is re-read because its rationale's figure is "
       "a modelled projection and the design's published model computes the quantity (reading 3.2). The design's "
       "mechanisms (conversion limits, expiring units, distributed acre equity) are genuine and lower the Gini from its "
       "level at adoption, so the unit is 0.5, not 0.0")

# ---- C1.4 Automation Resilience: class I, the design's own model of the scenarios (reading 3.6) -------------------
U("CCO", "C1.4", 0.5, [
    ("U", "the rationale's figures (poverty below 5% and aggregate demand at 90-110% of baseline across the 30%, 50% and "
          "70% scenarios) are Paper v1.4's own C1.4 measurement text for its 30% scenario, restated as a result, and no "
          "design source states them; v2.0 names the design's own model of the three scenarios as the indicator, and the "
          "published model cannot run them: its automation channel slows each agent's wage growth by at most 0.10 times "
          "the agent's automation risk a year and displaces no hours (Appendix G's standing mismatch); at its closest "
          "analogue, High Automation over 25 years, milder than the 30% scenario, poverty on the Societal Poverty Line "
          "is 15.1% at year 20 and 18.0% at year 25 (9.4% and 10.6% with in-kind relief counted as income), against "
          "11.5% and 12.1% with automation off, and no seed is below 8% (reading 3.6)",
     SIM + "; " + PAPER_G + "; Report v1.6, CCO C1.4; NEEC_Paper_v1_4.md, section 6 (C1.4 measurement)"),
    ("U", "the published model computes no final consumption; Appendix G's proxy, aggregate wage income, falls to 46.2% "
          "of the automation-off run by year 25, and aggregate cash income, which adds CCO conversion proceeds, to "
          "47.8% (reading 3.6)", SIM + "; " + PAPER_G)],
  note="the audit coded both clauses A on the rationale's figures; they are located in no design source, and the "
       "design's own model contradicts them at its nearest scenario, so both A codes are departed from (reading 3.6). "
       "Paper v1.4's Appendix G found the same in kind at v3.9 to v4.2 and changed no score, because no score was then "
       "read from simulation output; C1.4 is class I, and v2.0 names the design's own model as its indicator")

# ---- C3.2 Inflation Control Mechanisms: class U, the model silent (reading 3.8) -----------------------------------
U("CCO", "C3.2", 1.0, [
    ("C", "inflation contained ≤3% long-term", AUD),
    ("C", "≤5% during external 8% shock", AUD),
    ("C", "automatic parameter adjustment", AUD)],
  note="re-read under reading 3.2 and carried (reading 3.8): the rationale's figures are the design's modelling, the "
       "dual-currency inflation paper's numerical simulations (0.95% a year overall in its baseline scenario, a 95% "
       "interval of 0.6% to 1.4% across 10,000 runs; " + INFL + ", sections 5.2 and 5.4) and the framework paper's 8% "
       "scenario (local inflation held to 3.2% while national inflation reaches 8.1%; " + FRAME + ", section 5.2); the "
       "published model computes no price, since inflation is an input rate there, and its documentation states that it "
       "assumes rather than tests that the framework is non-inflationary (" + CONTRIB + ", Model Architecture "
       "Feedback), so it neither supports nor contradicts them")

# ---- C3.3 Multi-Failure Resistance (reading 3.7) ------------------------------------------------------------------
U("CCO", "C3.3", 0.5, [
    ("U", "the design's published model runs one compound scenario, the Adverse Environment (recessions, AI automation and "
          "2% inflation at the reference settings), milder than C3.3's recession-and-automation scenario (a 30% GDP "
          "decline, 15% unemployment and 40% business closures); in it, at year 20, the share above the Societal Poverty "
          "Line is 4.4% lower than in the paired run without the shocks, under 20%, but the share not in housing "
          "distress, the engine's nearest measure to housing stability, is 28.8% lower, and essential-service and "
          "democratic-function capacity are not modelled; the other three compound scenarios are not modelled; the "
          "design's papers report single-shock stress tests (a recession of 8% of GDP, a 6% inflation surge, unemployment "
          "of 12%, a climate crisis, a cyber attack) and no compound scenario or degradation figure; the rationale's "
          "degradation under 15% in all scenarios is located in no design source (reading 3.7)",
     SIM + "; " + MODEL + ", section 5.3; " + FRAME + ", sections 4.3 and 5.3")],
  note="C3.3 is class W and single-clause, outside D28's population; it is re-read because its rationale's figure is a "
       "stress-test result from the design's modelling (reading 3.2). The design's distributed architecture is a genuine "
       "mechanism, so the unit is 0.5, not 0.0")

# ---- C5.3 Partial and Parallel Deployability: class U, the model silent (reading 3.8) -----------------------------
U("CCO", "C5.3", 1.0, [
    ("C", "Viable at 30%+ participation", AUD),
    ("C", "Can coexist with traditional markets", AUD),
    ("C", "Scaling pathway validated through modeling", AUD),
    ("C", "Inter-jurisdictional coordination protocols specified", AUD)],
  note="re-read under reading 3.2 and carried (reading 3.8): the rationale's figures are the design's modelling (the "
       "framework paper: viability at 30% participation, merchant revenue at 98-102% of pre-implementation levels; " +
       FRAME + ", sections 5.2 and 5.3; the modelling paper's pilot, regional and national phases, " + MODEL +
       ", section 10.1); the published model reads no aggregate participation, its 55% threshold being a run warning "
       "since v4.17, and computes neither economic activity nor a scaling path, so it neither supports nor contradicts "
       "them")

REREAD = {("CCO", "C1.1"): 3}          # the part (index into PRIOR) whose record this group's supersedes
EXCEPT = {("CCO", "C1.4", 0): "located in no design source; the design's model shows poverty above 8% at its nearest "
                              "scenario (reading 3.6)",
          ("CCO", "C1.4", 1): "located in no design source; the design's model shows its demand proxy far below 85% at "
                              "its nearest scenario (reading 3.6)"}

# ---- the scan (reading 3.2): every published 1.0 whose rationale names modelling, simulation, a stress test or a
# projection, and why each is or is not a figure from the entry's own model ------------------------------------------
KW = re.compile(r"model|simulat|stress[- ]?test|projected|projection", re.I)
WHY = {
    "own": "a figure from the design's own modelling",
    "system": "the word names the system or its framework, not a model's output",
    "observed": "the text contrasts an observed record with projection or modelling",
    "real": "the stress test is a real-world episode",
    "revision": "the entry's revision of its own model is the clause's evidence, not a modelled figure",
    "review": "the estimates are NEEC's own review of a design that publishes no model",
}
SCAN = {("NSD", "C5.4"): "system", ("CCO", "C1.1"): "own", ("CCO", "C1.2b"): "own", ("CCO", "C1.4"): "own",
        ("CCO", "C2.1"): "own", ("CCO", "C3.2"): "own", ("CCO", "C3.3"): "own", ("CCO", "C4.2"): "own",
        ("CCO", "C4.4"): "own", ("CCO", "C5.3"): "own", ("INT", "C3.3"): "review", ("GEO", "C3.4"): "observed",
        ("GEO", "C5.3"): "observed", ("MC", "C3.4"): "observed", ("MC", "C5.3"): "observed", ("DE", "C2.5"): "system",
        ("DE", "C3.4"): "revision", ("DE", "C5.3"): "observed", ("UBS", "C3.4"): "revision",
        ("SWF", "C5.3"): "observed", ("CN", "C3.2"): "real", ("CN", "C5.1"): "system", ("SG", "C5.1"): "system",
        ("SG", "C5.3"): "system", ("IF", "C5.2"): "system", ("IF", "C5.3"): "observed", ("OS", "C4.1"): "observed"}

# ---- reading 3.9: the design's other re-estimated units, against v4.20 ----------------------------------------------
REOPEN = [
    ("C2.3", "no estimate of the level of creative engagement or of meaning scores was located",
     "computes neither"),
    ("C2.4", "no estimate of the share of proposals adopted or of satisfaction with responsiveness",
     "the CIP democratic rate is an input (65%), not an output; computes neither"),
    ("C3.4", "reopens if the simulation adds an endogenous price or behavioural channel and the adjustment run is repeated",
     "prices remain an exogenous input rate, damped only by realised PTF and PTH membership (Known Limitations, v4.17); "
     "no behavioural response is added, and v4.19's rule scaling cost relief with the Basic Unit is mechanical: not met"),
    ("C5.1", "the components' records decide; no model is read", "does not bear"),
    ("C2.1", "the model computes no autonomy or coercion measure", "still none"),
    ("C2.5", "the model does not simulate an exit from Public Trust Housing",
     "Public Trust Housing membership is still fixed at construction"),
    ("C3.5", "no share of failures diagnosed or corrected, and no externalised cost, in the model",
     "still none"),
    ("C4.1", "no resource use against regeneration and no debt ratio in the model",
     "still none; v4.19 states that the engine has no budget constraint"),
    ("C4.2", "the model represents neither emissions nor biodiversity", "still neither"),
    ("C4.4", "no simulation run is used: the model represents no governance of decisions", "still none"),
    ("C4.3", "the model represents no groups", "agents still carry no group attribute"),
    ("C5.2", "the model represents no deployment pathway", "still none: the population is fixed from year 0"),
    ("C5.4", "no projection of opposition to repeal or of survival across administrations", "still none"),
    ("C3.1", "clause 3 (coverage) not shown: participation is opt-in",
     "v4.19 adds automatic stabilizers built on the Research Hub's crisis protocols, off in every preset (the hub's "
     "x1.20 rule, a shock-neutral default of x1.35 and a scaled option of +2.8% per 1% of income lost); clause 2 on the "
     "design's stated rules is unchanged (the roadmap's fixed 20%); CCO participants, who receive Basic Units, are "
     "77.9% of the reference population, and emergency enrollment extends cost relief, not a cash benefit, at a "
     "placeholder 50% take-up: clause 3 still fixes 0.5"),
]

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 6, "stand": [("CCO", "C3.2"), ("CCO", "C5.3")], "fall": [("CCO", "C1.2b"), ("CCO", "C1.4"),
                                                                            ("CCO", "C3.3")],
          "points": 1.5, "scan": 27, "own": 9, "done_own": [("CCO", "C1.1"), ("CCO", "C2.1"), ("CCO", "C4.2"),
                                                            ("CCO", "C4.4")],
          "flags_added": [], "flags_removed": [("CCO", "C1.1")], "first": ("CCO", 17.0, 15.5), "emptied": 9,
          "anchors_here": ["C1.2b's 1.0 example, CCO (part (2.1))", "C1.4's 1.0 example, CCO (part (2.1))"],
          "anchors_all": 17}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def rationales(r4, rs, corpus, cids):
    """The rationale of every published 1.0, from the texts the audit read (Report v1.6 or the scoring document)."""
    rep = rs.read(r4.REPORT).split("\n")
    starts = [i for i, l in enumerate(rep) if re.match(r"^## \*\*(\d+)\\?\. ", l)][:15]
    natives = {code: rs.read(doc).split("\n") for code, doc in r4.NATIVE.items()}
    out, bad = {}, []
    for e in corpus:
        code = e["code"]
        for c in cids:
            if e["vector"][c] != 1.0:
                continue
            if code in r4.NATIVE:
                lines = natives[code]
                hits = [i for i, l in enumerate(lines) if re.match(r"^#### " + re.escape(c) + r" [^:]*: ([0-9.]+) \(", l)]
                if len(hits) != 1:
                    bad.append((code, c))
                    continue
                j = hits[0] + 1
                while j < len(lines) and not re.match(r"^#{1,4} ", lines[j]):
                    j += 1
                out[(code, c)] = "\n".join(lines[hits[0] + 1:j])
            else:
                k = r4.V1.index(code)
                hits = [i for i in range(starts[k], starts[k + 1])
                        if re.match(r"^## \*\*" + re.escape(c) + r" [^*]*: 1\.0\*\*", rep[i])]
                if len(hits) != 1:
                    bad.append((code, c))
                    continue
                out[(code, c)] = rep[hits[0]]
    return out, bad


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

    print(f"NEEC rescoring pass, stage 2, group 2.1: the design's modelled units on its published model, v4.20 ({RECORD})")
    print(f"inputs: {CRITERIA}, {CRIT44}, {CORPUS}, {CSV}, {AUDIT}, " + ", ".join(p for _, _, p, _ in PRIOR)
          + f", {SIMOUT}, {RECORD}\n")

    # [1] the group ------------------------------------------------------------------------------------------------
    print("[1] THE GROUP: A SCAN OF EVERY PUBLISHED 1.0, AND THE v2.0 CLAUSES")
    text, bad = rationales(r4, rs, corpus, cids)
    ones = sum(1 for c in vec for k in cids if vec[c][k] == 1.0)
    check(not bad and len(text) == ones == 184, f"the rationale of each of the corpus's {ones} published 1.0s is read "
          f"from the text the audit read (Report v1.6's Part I line, or the entry's scoring document)", str(bad))
    hits = sorted(k for k, t in text.items() if KW.search(t))
    order = list(names)
    hits.sort(key=lambda k: (order.index(k[0]), cids.index(k[1])))
    check(sorted(hits) == sorted(SCAN) and len(hits) == EXPECT["scan"],
          f"{len(hits)} rationales name modelling, a simulation, a stress test or a projection; each is classified")
    tally = {}
    for k in hits:
        tally[SCAN[k]] = tally.get(SCAN[k], 0) + 1
    print("  " + "; ".join(f"{WHY[w]}: " + ", ".join(f"{c} {k}" for c, k in hits if SCAN[(c, k)] == w)
                           for w in WHY))
    own = [k for k in hits if SCAN[k] == "own"]
    merged0 = {}
    for part in prior:
        merged0.update(part)
    done_own = sorted(k for k in own if k in merged0)
    new = sorted(k for k in own if k not in merged0)
    check(len(own) == EXPECT["own"] and all(c == "CCO" for c, _ in own) and done_own == sorted(EXPECT["done_own"])
          and sorted(set(UNITS) - set(REREAD)) == new and sorted(REREAD) == [("CCO", "C1.1")],
          f"the {len(own)} that rest on a figure from the entry's own model are all CCO-PTF-CIP-SZH's; the pass re-estimated "
          f"{len(done_own)} ({', '.join(k for _, k in done_own)}); the other {len(new)} ({', '.join(k for _, k in new)}) "
          "are this group's, with C1.1 re-checked as class I (reading 3.2)")
    check(all(vec[c][k] == 1.0 for c, k in UNITS) and all(merged0[k]["verdict"] == 0.5 for k in REREAD)
          and not any(k in merged0 for k in new),
          "every unit of the group is a published 1.0; the five new ones were never re-estimated, and C1.1 stands at "
          "0.5 from part (b3)")
    reg = {(u[0], u[1]): u for u in r4.UNITS}
    check(all((("CCO", g) in reg) == (g not in SINGLE) for g in GROUP)
          and [reg[("CCO", g)][2] for g in ("C1.1", "C1.4", "C3.2", "C5.3")] == ["AS", "AA", "AAA", "AAAA"]
          and all(g in r4.SINGLE for g in SINGLE),
          "the audit's codes: C1.1 AS (part (b3) re-estimated it), C1.4 AA, C3.2 AAA, C5.3 AAAA; C1.2b and C3.3 have "
          "one clause each and are outside the audit and D28's population")

    def words(t):
        return t[:1].lower() + t[1:]
    same = all(words(v2[g]["definition"]["clauses"][i]) == words(r4.CLAUSES[g][MAP[g][i]][0])
               for g in MAP for i in range(len(MAP[g])))
    whole = all(len(r4.CLAUSES[g]) == len(MAP[g]) == len(v2[g]["definition"]["clauses"]) for g in MAP)
    single = all(v2[g]["definition"]["clauses"] == [v2[g]["definition"]["pass_threshold"]] for g in SINGLE)
    check(same and whole and single and all(v2[g]["revision"]["cls"] == CLS[g] for g in GROUP)
          and v2["C1.4"]["definition"].get("clause_scope") == "in each of the 30%, 50% and 70% displacement scenarios"
          and "its own model of the three scenarios" in v2["C1.4"]["definition"]["indicators"]
          and "Societal Poverty Line" in v2["C1.1"]["definition"]["indicators"]
          and "above the C1.1 poverty line" in v2["C3.3"]["definition"]["measurement"],
          "v2.0's clauses: C1.1 and C1.4 (class I), C3.2 and C5.3 (class U) keep their Session 44 clauses verbatim; C1.4's "
          "scope names the 30%, 50% and 70% scenarios and its indicator for a design is its own model of them; C1.1's "
          "indicator is the Societal Poverty Line, and C3.3 (class W) measures poverty on it; C1.2b (class W) and C3.3 "
          "keep one clause")
    for g in GROUP:
        for i, t in enumerate(v2[g]["definition"]["clauses"]):
            print(f"  {g} ({i + 1}) {t}  [class {CLS[g]}]")

    # [2] the simulation runs ----------------------------------------------------------------------------------------
    print(f"\n[2] THE SIMULATION RUNS ({SIMOUT})")
    raw = open(os.path.join(HERE, SIMOUT), "rb").read() if os.path.isfile(os.path.join(HERE, SIMOUT)) else b""
    out = raw.decode("utf-8")
    lines = out.split("\n")
    check(hashlib.md5(raw).hexdigest() == SIMOUT_MD5, f"{SIMOUT} md5 {hashlib.md5(raw).hexdigest()}")
    check(all(f"{f} md5 {m}" in out for f, m in PINS.items()) and "compassionism-simulation 5a7a7b1, v4.20" in out
          and not [l for l in lines if l.strip().startswith("FAIL")]
          and sum(1 for l in lines if l.strip().startswith("PASS")) == 16
          and lines[-2] == "CCO SIMULATION CHECKS S51: ALL CHECKS PASSED.",
          "the captured run pins harness.js and index.html at 5a7a7b1 by digest, and its 16 checks pass")
    missing = [k for k, v in FIG.items() if v not in out]
    check(not missing, f"every figure this record quotes from the runs is in the capture ({len(FIG)} passages)",
          ", ".join(missing))
    blocks, cur = [], []
    for l in lines:
        if l.startswith("|"):
            cur.append(l)
        elif cur:
            blocks.append("\n".join(cur))
            cur = []
    check(len(blocks) == 5, f"the capture holds {len(blocks)} tables (C1.1, its 5-year tracking, C1.2b, C1.4, C3.3)")

    # [3] records ----------------------------------------------------------------------------------------------------
    print("\n[3] THE RECORDS")
    bad, tally = [], {k: 0 for k in STATUS}
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(v2[key[1]]["definition"]["clauses"]):
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {len(v2[key[1]]['definition']['clauses'])}")
        for k, (st, est, src) in enumerate(rec["clauses"]):
            tally[st] = tally.get(st, 0) + 1
            if st not in STATUS or not est.strip() or not src.strip():
                bad.append(f"{key} clause {k + 1}: status {st!r}, or an empty estimate or source")
            if "|" in est + src + (rec["flag"][1] if rec["flag"] else "") + rec["note"] or "{" in est:
                bad.append(f"{key} clause {k + 1}: a pipe character or an unfilled field")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per v2.0 clause, in the Pass Threshold's order, each with its estimate "
                   "and its source")
    print("  clause statuses: " + ", ".join(f"{STATUS[k]} {v}" for k, v in tally.items()))

    # [4] the rule ---------------------------------------------------------------------------------------------------
    print("\n[4] THE RULE (D28) AND THE AUDIT'S CODES")
    wrong = [k for k, r in UNITS.items() if rs.verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong and all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()),
          "every verdict follows D28 (1.0 only if every clause is cleared or moot), and none is 0.0 (D28(f))",
          str(wrong))
    stand = sorted(k for k in new if UNITS[k]["verdict"] == 1.0)
    fall = sorted(k for k in new if UNITS[k]["verdict"] == 0.5)
    points = sum(1.0 - UNITS[k]["verdict"] for k in new)
    check(stand == sorted(EXPECT["stand"]) and fall == sorted(EXPECT["fall"]) and points == EXPECT["points"]
          and all(UNITS[k]["verdict"] == merged0[k]["verdict"] for k in REREAD),
          f"of the five new units {len(stand)} stand ({', '.join(k for _, k in stand)}) and {len(fall)} become 0.5 "
          f"({', '.join(k for _, k in fall)}; {f1(points)} points); C1.1, re-checked as class I, stays 0.5")
    code = {(c, k, i): reg[(c, k)][2][MAP[k][i]] for (c, k) in UNITS if k in MAP for i in range(len(MAP[k]))}
    departs = sorted(x for x, ch in code.items() if ch == "A" and x[:2] in new
                     and UNITS[x[:2]]["clauses"][x[2]][0] != "C")
    carried = sorted(x for x, ch in code.items() if ch == "A" and x[:2] in new and CLS[x[1]] == "U")
    phrases = {(u[0], u[1]): list(u[3]) for u in r4.UNITS}
    as_phrase = all(UNITS[x[:2]]["clauses"][x[2]][1] in phrases[x[:2]] and UNITS[x[:2]]["clauses"][x[2]][2] == AUD
                    and UNITS[x[:2]]["clauses"][x[2]][0] == "C" for x in carried)
    check(departs == sorted(EXCEPT) and as_phrase and len(carried) == 7,
          f"the audit's A codes: {len(carried)} on C3.2 and C5.3 (class U) carried as cleared on the unit's own text, each "
          f"with the audit's phrase; {len(departs)} departed from, C1.4's two, each with its reason (reading 3.6)")
    for x in departs:
        print(f"  {x[0]} {x[1]} clause {x[2] + 1}: {EXCEPT[x]}")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag and not any(r["flag"] for r in UNITS.values()), "no unit of this group is flagged")

    # [5] reach ------------------------------------------------------------------------------------------------------
    print("\n[5] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = sorted((c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R")
    was_r = sorted(x for x in r4.REACH if (x[0], x[1]) in UNITS)
    check(now_r == was_r == [], "no clause of this group is out of reach, and the audit coded none so")

    # [6] flags ------------------------------------------------------------------------------------------------------
    print("\n[6] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) and (b) and 48.3)")
    blocks_ = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks_.items() for f in b["flags"]}

    def changes(units):
        add = sorted(k for k, r in units.items() if r["flag"] and k not in had)
        rem = sorted(k for k, r in units.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
        return add, rem
    merged, part_of = {}, {}
    for (tag, _, _, sess), part in zip(PRIOR, prior):
        merged.update(part)
        part_of.update({k: (tag, sess) for k in part})
    before = dict(merged)
    merged.update(UNITS)
    part_of.update({k: THIS for k in UNITS})
    a0, r0 = changes(before)
    adds, rems = changes(merged)
    dropped = sorted(k for k in UNITS if k in before and before[k]["flag"] and not UNITS[k]["flag"])
    added_here = sorted(k for k in UNITS if UNITS[k]["flag"] and not (k in before and before[k]["flag"]))
    cco_before = sorted(k for c, k in a0 if c == "CCO")
    cco_after = sorted(k for c, k in adds if c == "CCO")
    check(added_here == EXPECT["flags_added"] and dropped == sorted(EXPECT["flags_removed"])
          and len(adds) == len(a0) - 1 and rems == r0 and ("CCO", "C1.1") not in had,
          f"flags added here: {len(added_here)}; removed: {len(dropped)} (CCO C1.1, which part (b3) added; reading 3.4). "
          f"Flags added by the pass so far: {len(adds)} (against {len(a0)} before this group); removed from the "
          f"published registers: {len(rems)}")
    flag_line = (f"Flags added in this group: none; removed: 1 (CCO C1.1, the flag toward 1.0 that part (b3) added; "
                 f"reading 3.4). Flags added by the pass so far: {len(adds)} (against {len(a0)} before this group); removed "
                 f"from the published registers: {len(rems)}. CCO-PTF-CIP-SZH's published register holds no flag; the "
                 f"pass's flags on it are now on " + ", ".join(cco_after) + " (before this group: "
                 + ", ".join(cco_before) + ").")
    print("  " + flag_line)

    # [7] reopening conditions -----------------------------------------------------------------------------------------
    print("\n[7] THE DESIGN'S OTHER RE-ESTIMATED UNITS, AGAINST v4.20 (" + REOPEN_TAG + ")")
    cco_done = sorted(k for c, k in before if c == "CCO" and (c, k) not in UNITS)
    check(sorted(k for k, _, _ in REOPEN) == cco_done and len(cco_done) == 14
          and all(before[("CCO", k)]["verdict"] == 0.5 for k in cco_done),
          f"every other unit of the design the pass re-estimated ({len(cco_done)}, all at 0.5) is checked against v4.20; "
          "none reopens")
    rows = ["| Unit | Part | Verdict | What the record read from the model, or its reopening condition | At v4.20 | "
            "Outcome |", "|---|---|---|---|---|---|"]
    for k, cond, now in REOPEN:
        tag = part_of[("CCO", k)][0]
        fl = " (flagged)" if before[("CCO", k)]["flag"] else ""
        rows.append(f"| CCO {k} | {tag} | {f1(before[('CCO', k)]['verdict'])}{fl} | {cond} | {now} | stands |")
    reopen_table = "\n".join(rows)
    print(reopen_table)

    # [8] consequences -------------------------------------------------------------------------------------------------
    print("\n[8] CONSEQUENCES (computed here on the published 26-criterion structure; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            if k in cids:
                v[c][k] = r["verdict"]
        vsteps.append(v)
    vp, vn = vsteps[-2], vsteps[-1]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, mp, after = steps[0], steps[-2], steps[-1]
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    ones_now = {g: [c for c in order if vn[c][g] == 1.0] for g in GROUP}
    tags = ["published"] + [t for t, _, _, _ in PRIOR] + [THIS[0]]
    emptied = {}
    for tag, v in zip(tags, vsteps):
        for k in cids:
            if k not in emptied and not any(v[c][k] == 1.0 for c in v):
                emptied[k] = tag
    check(len(emptied) == EXPECT["emptied"] and not [k for k in emptied if emptied[k] == THIS[0]],
          f"no entry scores 1.0 on {len(emptied)} criteria after this group, as before it: each criterion of the group "
          "keeps a 1.0 or had none left")
    ones_line = ("After this group " + "; ".join(
        f"{g} keeps {len(ones_now[g])} score{'s' if len(ones_now[g]) != 1 else ''} of 1.0 ("
        + (", ".join(ones_now[g]) or "none") + ")" for g in GROUP) + ". After parts (a), (b) and this group no entry "
        "scores 1.0 on " + str(len(emptied)) + " criteria: " + ", ".join(
        f"{k} (emptied in part {emptied[k]})" for k in cids if k in emptied) + ".")
    print("  " + ones_line)
    rb, rp, rn = rs.ranks(base["total"]), rs.ranks(mp["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After part (b) (rank) | After group 2.1 (rank) | Change here | Failures | Tier |",
            "|---|---:|---:|---:|---:|---:|---|"]
    for c in rs.order_codes(names, base):
        rows.append(f"| {c} | {f1(base['total'][c])} ({rb[c]}) | {f1(mp['total'][c])} ({rp[c]}) | "
                    f"{f1(after['total'][c])} ({rn[c]}) | {f1(after['total'][c] - mp['total'][c])} | "
                    f"{after['fail'][c]} | {rs.tier(after['fail'][c])} |")
    cons_table = "\n".join(rows)
    pp, fp = rs.dominance(vp, cids)
    pn, fn = rs.dominance(vn, cids)
    gained = sorted(set(pn) - set(pp), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(pp) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    second = sorted((c for c in order if c not in first), key=lambda c: -after["total"][c])[0]
    n_all = len(merged)
    st_all = sum(1 for r in merged.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for r in merged.values())
    check(len(first) == 1 and (first[0], mp["total"][first[0]], after["total"][first[0]]) == EXPECT["first"],
          f"first place: {first[0]}, {f1(mp['total'][first[0]])} after part (b), {f1(after['total'][first[0]])} now; "
          f"next, {second} at {f1(after['total'][second])}")
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(pp)} after part (b) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(fp)} (" + ", ".join(c for c in order if c in fn) + f"). First place: {first[0]}, "
                f"{f1(mp['total'][first[0]])} after part (b), {f1(after['total'][first[0]])} now, ahead of "
                + ", ".join(c for c in order if after["total"][c] == after["total"][second])
                + f" at {f1(after['total'][second])}. Across the pass so far {n_all} units have been re-estimated, each "
                f"counted once: {st_all} stand and {n_all - st_all} are at 0.5 ({f1(pts_all)} points).")
    print("  " + dom_line)

    # [9] the ledger ---------------------------------------------------------------------------------------------------
    print("\n[9] THE SCORE LEDGER (published total, each part's change, the total now; 26 criteria)")
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

    # [10] anchors -----------------------------------------------------------------------------------------------------
    print("\n[10] ANCHOR EXAMPLES THE PASS SO FAR MOVES (the published anchors, criteria_s44_snapshot.json)")
    code_of = {v: k for k, v in names.items()}
    hits_a, empty = [], []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                cd = code_of.get(ex["system"])
                if cd and (cd, c["id"]) in merged and merged[(cd, c["id"])]["verdict"] != ex["cited"]:
                    hits_a.append(f"{c['id']}'s {band} example, {cd} (part {part_of[(cd, c['id'])][0]})")
                    if not any(vn[x][c["id"]] == float(band) for x in vn):
                        empty.append((c["id"], band))
    here = [h for h in hits_a if f"part {THIS[0]}" in h]
    check(here == EXPECT["anchors_here"] and len(hits_a) == EXPECT["anchors_all"] and len(empty) == 9
          and not [e for e in empty if e[0] in ("C1.2b", "C1.4")],
          f"this group moves two anchor examples, C1.2b's and C1.4's 1.0 (CCO-PTF-CIP-SZH), {len(hits_a)} across the "
          f"pass; each band keeps a corpus unit at its value (Integral and three others on C1.2b, Universal Basic Income on "
          f"C1.4), so the {len(empty)} bands left with none are unchanged")
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits_a) + ". Bands whose example the "
                   "pass moves and which no corpus unit then scores at their value: "
                   + ", ".join(f"{c}'s {b}" for c, b in empty) + ".")
    print("  " + anchor_line)

    # [11] the record --------------------------------------------------------------------------------------------------
    print(f"\n[11] THE RECORD'S TABLES (generated here; {RECORD} must contain them, and the runs' tables, verbatim)")
    unit_order = [("CCO", g) for g in GROUP]

    def was(key):
        return f"{f1(merged0[key]['verdict'])} (part (b3))" if key in REREAD else "1.0"
    t = {}
    rows = ["| Entry | Criterion | Class | Clauses | Verdict | Flag |", "|---|---|---|---|---|---|"]
    for key in unit_order:
        rec = UNITS[key]
        fl = "removed (part (b3)'s, toward 1.0)" if key in dropped else ""
        rows.append(f"| {key[0]} | {key[1]} | {CLS[key[1]]} | {' '.join(s for s, _, _ in rec['clauses'])} | "
                    f"{was(key)} → {f1(rec['verdict'])} | {fl} |")
    t["summary"] = "\n".join(rows)
    for key in unit_order:
        rec, (cd, k) = UNITS[key], key
        head = f"#### {cd} {k} {v2[k]['name']}: {was(key)} → {f1(rec['verdict'])}"
        lines_ = [head, "", "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (st, est, src) in enumerate(rec["clauses"]):
            lines_.append(f"| {i + 1} | {v2[k]['definition']['clauses'][i]} | {STATUS[st]} | {est} | {src} |")
        if rec["note"]:
            lines_ += ["", f"*Note:* {rec['note']}."]
        t[f"unit {cd} {k}"] = "\n".join(lines_)
    scan_rows = ["| Why the word appears | Units |", "|---|---|"]
    for w in WHY:
        us = [f"{c} {k}" for c, k in hits if SCAN[(c, k)] == w]
        scan_rows.append(f"| {WHY[w]} | {', '.join(us)} ({len(us)}) |")
    t["scan"] = "\n".join(scan_rows)
    t["reopen"], t["consequences"], t["dominance"], t["flags"] = reopen_table, cons_table, dom_line, flag_line
    t["ledger"], t["ones"], t["anchors"] = ledger, ones_line, anchor_line
    GENERATED.clear()
    GENERATED.update(t)
    if "--tables" in sys.argv[1:]:
        sys.stdout = sys.__stdout__
        print(json.dumps(t, ensure_ascii=False))
        return 0
    record = rs.read(RECORD) if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    missing_b = [i for i, b in enumerate(blocks) if b not in record]
    check(not missing_b, f"{RECORD} contains the {len(blocks)} tables of the simulation runs verbatim", str(missing_b))
    print()
    print(t["summary"])
    print()
    print(cons_table)
    print()
    print(ledger)
    print("\nRESCORING STAGE 2, GROUP 2.1, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.1: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
