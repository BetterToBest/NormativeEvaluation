#!/usr/bin/env python3
"""
rescoring_s38.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), first group: the criteria whose
clause readings part (a) fixed (C3.4, C5.3, C2.4, C1.3, C2.3)
==============================================================================================================
Session 38. Part (a) (NEEC_Rescoring_s37.md, rescoring_s37.py) re-estimated the 33 stated-shortfall 1.0s and fixed
the readings of eight clauses for the rest of the pass (its section 3.4). Part (b) re-estimates the other 101 units
of D28's population criterion by criterion, so that one criterion's clauses are read alike across the corpus
(protocol 5). This script holds its first group: every part (b) unit on the five criteria whose readings are fixed,
29 units. It changes no file and no score: the pass's changes are applied by generator when it ends (protocol 10.2,
10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). A clause the audit coded A (or N)
is carried as cleared (or moot) on the unit's own text unless the entry's or design's own sources contradict it;
this group has no such exception, and the script asserts so.

CHECKS: the group against the audit's register (exactly the part (b) units of the five criteria); every record
complete; the rule; the audit's A and N codes carried; reach (no revision in this group); flags against the summary
blocks, cumulatively with part (a); the consequences of parts (a) and (b) so far (totals, ranks, failures, tiers,
dominance, frontier, what remains); the pinned simulation runs quoted by the record; and that NEEC_Rescoring_s38.md
contains every generated table verbatim.

Usage: python3 rescoring_s38.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, rescoring_s37.py, the
                                   eleven scoring documents, cco_simulation_checks_s38_output.txt and
                                   NEEC_Rescoring_s38.md beside itself; writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, AUDIT, PART_A = "criteria.json", "neec_corpus.json", "r4_audit_s35.py", "rescoring_s37.py"
RECORD, SIMOUT = "NEEC_Rescoring_s38.md", "cco_simulation_checks_s38_output.txt"
SIM_MD5 = "035d1be82ab497e76a234615a04c0ce9"   # harness.js at BetterToBest/compassionism-simulation cd0ceec (v4.15)
GROUP = ("C3.4", "C5.3", "C2.4", "C1.3", "C2.3")
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
NE = "not estimated in this pass; the verdict is fixed by another clause"
HUB = "research-hub at 8e8a6ba (2026-09-21), "
SIM = "compassionism-simulation at cd0ceec (v4.15), harness.js; cco_simulation_checks_s38_output.txt"
DOC = {"MC": "NEEC_MutualCredit_LETS_scoring_scratch.md", "DE": "NEEC_DoughnutEconomics_scoring_scratch.md",
       "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md", "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md"}

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in Appendix B's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- C3.4 Epistemic Adaptability (readings: part (a) 3.4, clauses 2 and 4; this part 3.1, 3.2) ------------------
U("NSD", "C3.4", 0.5, [
    ("C", "willing to adjust parameters based on research and outcomes", AUD),
    ("C", "frequent policy experimentation and evaluation", AUD),
    ("C", "parameter changes are enacted by elected parliaments (the national turnouts of part (a), NSD C2.4)",
     "IDEA Voter Turnout Database; Valmyndigheten, 2022 results"),
    ("S", "the financial liberalisation of the 1980s led to systemic banking crises in Finland, Norway and Sweden, "
          "among the deepest in advanced economies since the Second World War, with Finland's output falling nearly "
          "15%; Denmark, whose supervision was tightened, avoided a systemic crisis",
     "Honkapohja, Bank of Finland Research Discussion Paper 36/2012; Anderson, Federal Reserve Bank of St. Louis "
     "Economic Synopses 2009, no. 10")],
  note="the liberalisation changed the configuration's own credit parameters (lending ceilings, interest and "
       "capital controls), which is what clause 4 asks about; the welfare state's functions continued, but the "
       "clause asks for zero collapses, and a systemic banking crisis is one")
U("MS", "C3.4", 1.0, [
    ("C", "the pay-ratio cap, a core distributive parameter, moved from 1:3 at founding to 1:4.5 in the 1970s and "
          "1:6 in 1988, a 100% range", "Co-operative News, Co-operative approaches to pay (thenews.coop)"),
    ("C", "democratic governance enables rapid adaptation to evidence", AUD),
    ("C", "the pay-ratio changes were decided at the cooperatives' General Assemblies",
     "Co-operative News (thenews.coop); " + REP + "MS C3.4"),
    ("C", "stated search: no collapse caused by a parameter adjustment located; Fagor Electrodomesticos, the "
          "founding cooperative, failed in 2013 after heavy losses in the euro-area and Spanish real-estate crises, "
          "carrying debt from its 2005 Brandt acquisition, causes that clear it of an adjustment",
     "Fortune (27 November 2013); The Local (14 November 2013); Mondragon Annual Report 2013")],
  note="clause 2 rests on the unit's own text, as part (a)'s convention carries an addressed clause; Report v2.0's "
       "clause-level Part I should time an update against the evidence that called for it")
U("MMT", "C3.4", 0.5, [
    ("C", "adjust job guarantee wage, spending levels and taxation", AUD),
    ("U", "spending and taxation are adjusted through the legislative budget, and no update timed against the "
          "evidence that called for it was located; the one national precedent, Argentina's Jefes de Hogar, paid a "
          "fixed 150 pesos per beneficiary under decree 565/2002, the sum still stated in a 2003 amendment bill, "
          "while the programme was extended by statute to 2007",
     "Decreto 565/2002; Camara de Diputados bill 2938-D-03 (2003); Ley 26204; CELS, Plan Jefes y Jefas"),
    ("U", NE, ""),
    ("U", NE, "")])
U("UBI", "C3.4", 0.5, [
    ("C", "simple parameter adjustment (benefit level, taxation rates)", AUD),
    ("S", "the longest-running precedent, Alaska's dividend, is set once a year; since the 2017 Supreme Court "
          "ruling it competes for annual funding like other programmes; the 2018 percent-of-market-value law came in "
          "the third budget year of the deficit that prompted the 2016 veto: annual cycles fall short",
     "Alaska Public Media (6 May 2022); Anchorage Daily News (4 October 2018; 11 October 2022); Petroleum News "
     "(13 May 2018)"),
    ("C", "changes enacted by the legislature and governor and tested in the state Supreme Court",
     "Courthouse News (2017); Alaska Public Media (6 May 2022)"),
    ("U", NE, "")])
U("DG", "C3.4", 0.5, [
    ("C", "democratic governance allows evidence-based adjustments", AUD),
    ("C", "decentralised experimentation enables rapid learning and adaptation", AUD),
    ("C", "democratic governance allows evidence-based adjustments", AUD),
    ("U", "no implementation record, and no modelling of adjustments to the design's parameters in operation "
          "located in its sources (reading 3.1)", "")])
U("SC", "C3.4", 0.5, [
    ("C", "easier to adjust metrics and targets than restructure the system", AUD),
    ("U", NE, ""),
    ("S", "firms' metrics and targets are changed by boards under one-share-one-vote; the entry's own scoring "
          "records plutocratic control and token stakeholder voice: governed, not democratic (as Islamic finance's "
          "C3.4 in part (a))", REP + "SC C2.4 and C4.4"),
    ("U", NE, "")])
U("PE", "C3.4", 0.5, [
    ("C", "councils adjust proposals based on feedback", AUD),
    ("C", "democratic structure enables rapid evidence-based changes", AUD),
    ("C", "democratic structure enables rapid evidence-based changes", AUD),
    ("U", "no implementation record, and no modelling of adjustments to the design's parameters in operation "
          "located (reading 3.1)", "")])
U("CCO", "C3.4", 0.5, [
    ("C", "octave caps, basic amounts (5-20% of GDP per capita), conversion multipliers and the phi-rate "
          "adjustable", AUD),
    ("C", "the design's crisis protocol schedules parameter recalibration within one to six months, and monthly "
          "cost-of-living adjustments in an inflation surge",
     HUB + "integrated-implementation-roadmap.html (Appendix G)"),
    ("C", "CIP enables democratic parameter adjustment", AUD),
    ("U", "the design's own engine was run by the scorer with the Basic Unit stepped by 0.7 to 1.3 from year 10: "
          "no collapse; but prices are an exogenous input and agents do not respond to the change, so no "
          "adjustment could cause a collapse in the model, and the run cannot show the clause (readings 3.1, 3.2)",
     SIM)],
  flag=([1.0], "the design's modelled stability across adjustments accepted at the modelling tier without "
               "requiring a channel by which an adjustment could fail"),
  note="reopens if the simulation adds an endogenous price or behavioural channel and the adjustment run is repeated")
U("MC", "C3.4", 0.5, [
    ("C", "clearing and settlement mechanisms adapted over nine decades", AUD),
    ("U", "the adaptations the unit cites run over decades (WIR) and years (the Credit Commons redesign, documented "
          "through 2024-2025); no update timed against the evidence that called for it located",
     DOC["MC"] + ", C3.4"),
    ("U", NE, ""),
    ("C", "nine decades of continuous operation", AUD)])
U("UBS", "C3.4", 0.5, [
    ("C", "the framework's authors revising scope, framing and emphasis", AUD),
    ("S", "the unit's own record is revision by the framework's authors at intervals of one to three years (2017, "
          "2019, 2020, 2023): cycles longer than six months, as for Doughnut Economics in part (a)",
     DOC["UBS"] + ", C3.4"),
    ("U", NE, ""),
    ("U", NE, "")])

# ---- C5.3 Partial and Parallel Deployability (readings 3.3, 3.4) ------------------------------------------------
U("MS", "C5.3", 0.5, [
    ("C", "cooperatives function well in mixed economies", AUD),
    ("C", "can coexist with traditional firms", AUD),
    ("U", "no modelling of a scaling pathway cited; observed cooperative scale peaks at a regional federation "
          "(Mondragon: about 70,000 workers in 92 cooperatives), short of the national stage the Measurement line "
          "describes (reading 3.4)", "Reasons to Be Cheerful, via DailyGood (2026); criteria.json C5.3 (measurement)"),
    ("U", NE, "")])
U("SC", "C5.3", 0.5, [
    ("C", "partial deployment proven viable through existing examples", AUD),
    ("C", "stakeholder firms coexist easily with traditional corporations", AUD),
    ("U", "the unit cites existing examples (B Corps competing in the same markets); no modelled or observed "
          "pathway from pilots to national scale located (reading 3.4)", REP + "SC C5.3"),
    ("U", NE, "")])
U("MC", "C5.3", 0.5, [
    ("C", "can begin with as few as a handful of participants", AUD),
    ("C", "operates alongside conventional currency", AUD),
    ("S", "the entry's own document records a practical trust ceiling of 100-200 members per LETS node and WIR's "
          "centralisation under scale; the federated redesign meant to pass them is not yet validated",
     DOC["MC"] + ", C3.4 and sources"),
    ("M", "no case of adoption requiring or attempting multi-jurisdiction coordination", AUD)])
U("DE", "C5.3", 0.5, [
    ("C", "adopted piecemeal by voluntarily participating jurisdictions", AUD),
    ("C", "coexists with the ordinary market economy", AUD),
    ("C", "the scaling record is concrete and dated", AUD),
    ("U", "no inter-jurisdictional coordination protocol located in the entry's document; cities adopt the "
          "framework independently, but its ecological ceiling is planetary, so the text does not establish that "
          "coordination is unneeded and Mutual Credit's moot reading does not transfer (reading 3.3)",
     DOC["DE"] + ", C5.3")])
U("UBS", "C5.3", 1.0, [
    ("C", "each of its sectors adopted independently", AUD),
    ("C", "Quebec's universal low-fee childcare raised mothers' employment by nearly 70,000 (3.8% of women's "
          "employment) and provincial GDP by about 1.7% in 2008: market activity grew",
     "Fortin, Godbout and St-Cerny (2012), Universite de Sherbrooke Working Paper 2012/02"),
    ("C", "universal childcare scaled from Quebec to all of Canada", AUD),
    ("C", "Canada-wide Early Learning and Child Care agreements signed by the federal government with every "
          "province and territory by March 2022, including an asymmetrical agreement with Quebec (reading 3.3)",
     "Employment and Social Development Canada, Question Period Notes (June 2022; June 2023)")],
  flag=([0.5], "coordination protocols shown for one sector, childcare, and none for the seven-sector package"))
U("SG", "C5.3", 0.5, [
    ("C", "the state's share can be dialled down", AUD),
    ("C", "coexists with private and foreign firms by design", AUD),
    ("U", "the record is of one city-state; the entry's own text says components transplanted abroad worked less "
          "well (China's Housing Provident Fund; the Temasek model's limited influence); no modelled pathway "
          "(reading 3.4)", DOC["SG"] + ", C5.3"),
    ("C", "enterprises operate on an equal basis with local and foreign businesses", AUD)])

# ---- C2.4 Democratic Participation (readings: part (a) 3.4; this part 3.5) --------------------------------------
U("MS", "C2.4", 0.5, [
    ("C", "75-85% participation in cooperative governance", AUD),
    ("U", "no adoption share of member-initiated proposals located for Mondragon or other cooperative networks", ""),
    ("U", NE, "")])
U("MMT", "C2.4", 0.5, [
    ("R", "participation in democratic processes is a property of the political system; no source located in the "
          "job-guarantee literature places democratic institutions inside the guarantee's design (D31)",
     "Session 35 reach reason, confirmed"),
    ("R", "the adoption of citizen proposals is a property of the political system",
     "Session 35 reach reason, confirmed"),
    ("R", "satisfaction with responsiveness is a property of the political system",
     "Session 35 reach reason, confirmed")])
U("DG", "C2.4", 0.5, [
    ("C", "participatory democracy core principle", AUD),
    ("U", "the design specifies assemblies and consensus processes, not an estimate of the share of citizen "
          "proposals adopted; none located (reading 3.5)", ""),
    ("U", NE, "")])
U("PE", "C2.4", 0.5, [
    ("C", "everyone participates in planning affecting them", AUD),
    ("U", "the plan is assembled from council proposals revised through iteration until feasible; no estimate of "
          "the share adopted, and no implementation (reading 3.5)", REP + "PE C2.4"),
    ("U", NE, "")])
U("CCO", "C2.4", 0.5, [
    ("C", "as audited; the design's documents give 15-25% as the portal's pilot success metric and model "
          "participation rising from 55% to 85% at maturity",
     HUB + "citizens-internet-portal.html; integrated-digital-governance.html"),
    ("U", "any citizen may submit proposals above a signature threshold, and binding changes need a 60-67% "
          "supermajority with a geographic distribution requirement; no estimate of the share adopted (reading 3.5)",
     HUB + "citizens-internet-portal.html"),
    ("U", "satisfaction with democratic processes is named as a metric, with no estimate",
     HUB + "risk-mitigation-framework.html")])
U("INT", "C2.4", 0.5, [
    ("C", "plausibly match or exceed the best documented cooperative precedents", AUD),
    ("U", "weighted consensus and objection mapping specified; no estimate of the share of proposals adopted "
          "(reading 3.5)", ""),
    ("U", NE, "")])

# ---- C1.3 Housing Security (reading: part (a) 3.4, clause 2) ----------------------------------------------------
U("NSD", "C1.3", 0.5, [
    ("C", "about 90% or more housing stability", AUD),
    ("S", "housing cost overburden (housing costs above 40% of disposable income) in 2024: Denmark 14.6% and Sweden "
          "10.6%, among the highest rates in the EU; in Denmark's lowest income quintile, whose incomes fall below "
          "80% of the median, the rate ranges from 44.6% to 60.4% across the EU-SILC series",
     "Eurostat, Living conditions in Europe: housing (2024 data, ilc_lvho07a); Eurostat ilc_lvho07b, via DBnomics")])

# ---- C2.3 Creative Development Opportunities (readings: part (a) 3.4, clause 1; this part 3.5) -------------------
U("MS", "C2.3", 0.5, [
    ("U", "Mondragon's training and education time bears on opportunity; no weekly creative-engagement figure "
          "located (reading 3.5)", ""),
    ("C", "sabbaticals and education time", AUD),
    ("U", NE, "")])
U("DG", "C2.3", 0.5, [
    ("U", "the design reduces working hours to 20 a week and programmes community culture; no estimate of weekly "
          "creative engagement (reading 3.5)", ""),
    ("C", "prioritises creative and social time", AUD),
    ("U", "no meaning or purpose satisfaction estimate in the design's sources", "")])
U("FALC", "C2.3", 0.5, [
    ("C", "humans pursue art, science, philosophy and relationships", AUD),
    ("C", "unlimited time and resources for creative pursuits", AUD),
    ("U", "no meaning or purpose satisfaction estimate; the design's sources state the aim, not a level "
          "(reading 3.5)", "")])
U("PE", "C2.3", 0.5, [
    ("U", "no estimate of weekly creative engagement (reading 3.5)", ""),
    ("C", "reduced hours (20-30 a week) leave substantial time for self-directed pursuits", AUD),
    ("U", NE, "")])
U("CCO", "C2.3", 0.5, [
    ("U", "the design projects relative increases for its case studies (60% more cultural-event participation; "
          "32% more creative output), not a level of weekly engagement (reading 3.5)",
     HUB + "cultural-value-integration.html (section 6)"),
    ("C", "time and resources for non-subsistence activities", AUD),
    ("U", "no meaning or purpose satisfaction estimate located in the design's documents", "")])
U("INT", "C2.3", 0.5, [
    ("C", "could exceed the 35-55% range; the comparison it rests on is unsourced (part (a), correction 3)", AUD),
    ("C", "space for arts, culture and personal development", AUD),
    ("U", "no meaning or purpose satisfaction estimate (reading 3.5)", "")])

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 29, "stand": [("MS", "C3.4"), ("UBS", "C5.3")], "points": 13.5,
          "flags_added": [("CCO", "C3.4"), ("UBS", "C5.3")], "remaining": 72, "c51": 11,
          "dominance_a": 15, "frontier_a": 11}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables(rs, r4, cdef, order, names, base, mid, after, left, c51):
    t = {}
    f1, fmt = rs.f1, rs.fmt_alts
    rows = ["| Entry | Criterion | Clauses | Verdict | Flag |", "|---|---|---|---|---|"]
    for key in order:
        rec = UNITS[key]
        fl = f"alternative {fmt(rec['flag'][0])}" if rec["flag"] else ""
        rows.append(f"| {key[0]} | {key[1]} | {' '.join(st for st, _, _ in rec['clauses'])} | "
                    f"1.0 → {f1(rec['verdict'])} | {fl} |")
    t["summary"] = "\n".join(rows)
    for key in order:
        rec, (code, crit) = UNITS[key], key
        head = f"#### {code} {crit} {cdef[crit]['name']}: 1.0 → {f1(rec['verdict'])}"
        if rec["flag"]:
            head += " — flagged as contestable"
        lines = [head, "", "| # | Clause | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for k, (st, est, src) in enumerate(rec["clauses"]):
            lines.append(f"| {k + 1} | {r4.CLAUSES[crit][k][0]} | {STATUS[st]} | {est} | {src or '—'} |")
        if rec["flag"]:
            lines += ["", f"*Flag:* alternative {fmt(rec['flag'][0])}: {rec['flag'][1]}."]
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {code} {crit}"] = "\n".join(lines)
    rb, rm, ra = rs.ranks(base["total"]), rs.ranks(mid["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After part (a) (rank) | After this group (rank) | Change here | Failures | "
            "Tier | D28 units left | C5.1 clause 2 | Floor if all fall |",
            "|---|---:|---:|---:|---:|---:|---|---:|---:|---:|"]
    for code in rs.order_codes(names, base):
        lf, cf = left.get(code, 0), c51.get(code, 0)
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(mid['total'][code])} ({rm[code]}) | "
                    f"{f1(after['total'][code])} ({ra[code]}) | {f1(after['total'][code] - mid['total'][code])} | "
                    f"{after['fail'][code]} | {rs.tier(after['fail'][code])} | {lf} | {cf} | "
                    f"{f1(after['total'][code] - 0.5 * (lf + cf))} |")
    t["consequences"] = "\n".join(rows)
    return t


def sim_tables(text):
    """The two Markdown tables of the simulation runs, as printed."""
    blocks, cur = [], []
    for line in text.split("\n"):
        if line.startswith("|"):
            cur.append(line)
        elif cur:
            blocks.append("\n".join(cur))
            cur = []
    if cur:
        blocks.append("\n".join(cur))
    return blocks


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    r4 = load("r4_audit_s35", AUDIT)
    rs = load("rescoring_s37", PART_A)
    crit = json.loads(rs.read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}

    print(f"NEEC rescoring pass, part (b), first group: {', '.join(GROUP)} ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {AUDIT}, {PART_A}, {len(rs.DOCUMENTS)} scoring documents, {SIMOUT}, "
          f"{RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    partb = [k for k in d28 if k not in rs.UNITS]
    group = [k for k in partb if k[1] in GROUP]
    check(len(d28) == 134 and len(rs.UNITS) == 33 and len(partb) == 101,
          "D28's population 134; part (a) 33; part (b) 101")
    check(sorted(UNITS) == sorted(group) and len(UNITS) == EXPECT["units"] and all(vec[c][k] == 1.0 for c, k in UNITS),
          f"this group holds exactly the part (b) units of {', '.join(GROUP)}: {len(UNITS)}, every one a corpus 1.0")
    print("  per criterion: " + ", ".join(f"{g} {sum(1 for k in UNITS if k[1] == g)}" for g in GROUP))
    c51 = [(u[0], u[1]) for u in r4.UNITS if u[1] == "C5.1" and (u[0], u[1]) not in rs.UNITS]
    check(len(c51) == EXPECT["c51"] and not set(c51) & set(d28),
          f"C5.1's second clause remains to be tested on {len(c51)} 1.0s outside D28's population")

    # [2] records --------------------------------------------------------------------------------------------------
    print("\n[2] THE RECORDS")
    bad, tally = [], {k: 0 for k in STATUS}
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(r4.CLAUSES[key[1]]):
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {len(r4.CLAUSES[key[1]])}")
        for k, (st, est, src) in enumerate(rec["clauses"]):
            tally[st] = tally.get(st, 0) + 1
            if st not in STATUS or not est.strip():
                bad.append(f"{key} clause {k + 1}: status {st!r} or empty estimate")
            if st in "CSRM" and not src.strip():
                bad.append(f"{key} clause {k + 1}: {STATUS.get(st, st)} without a source or reason")
            if "|" in est + src:
                bad.append(f"{key} clause {k + 1}: a pipe character would break the table")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per clause, in Appendix B's order; every cleared, short, out-of-reach "
                   "and moot clause carries its source or reason")
    print("  clause statuses: " + ", ".join(f"{STATUS[k]} {v}" for k, v in tally.items()))

    # [3] the rule -------------------------------------------------------------------------------------------------
    print("\n[3] THE RULE (D28)")
    wrong = [k for k, r in UNITS.items() if rs.verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong, "every verdict follows D28: 1.0 only if every clause is cleared or moot, otherwise 0.5",
          str(wrong))
    check(all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()), "no unit is scored 0.0 in this pass (D28(f))")
    stand = sorted(k for k, r in UNITS.items() if r["verdict"] == 1.0)
    points = sum(1.0 - r["verdict"] for r in UNITS.values())
    check(stand == sorted(EXPECT["stand"]) and points == EXPECT["points"],
          f"{len(stand)} of {len(UNITS)} stand ({', '.join(' '.join(k) for k in stand)}); "
          f"{len(UNITS) - len(stand)} become 0.5 ({rs.f1(points)} points)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    carried = [(k, i) for k, r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"])
               if (reg[k][i] == "A" and st != "C") or (reg[k][i] == "N" and st != "M")]
    check(not carried, "every clause the audit coded A is cleared and every N moot: no own-source exception in "
                       "this group", str(carried))

    # [4] reach ----------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = {x for x in r4.REACH if (x[0], x[1]) in UNITS}
    check(now_r == was_r, "out of reach: " + (", ".join(f"{c} {k} clause {i + 1}" for c, k, i in sorted(now_r))
                                              or "none") + "; no reach coding revised in this group")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with part (a))")
    blocks = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}
    added = sorted(k for k, r in UNITS.items() if r["flag"] and k not in had)
    removed = sorted(k for k, r in UNITS.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
    kept = sorted(k for k, r in UNITS.items() if k in had and k not in removed)
    check(added == sorted(EXPECT["flags_added"]) and not removed and not kept,
          f"flags added {len(added)} (" + ", ".join(" ".join(k) for k in added) + "); none removed")
    a_add = sorted(k for k, r in rs.UNITS.items() if r["flag"] and k not in had)
    a_rem = sorted(k for k, r in rs.UNITS.items() if k in had and r["verdict"] in had[k]["alternatives"]
                   and not r["flag"])
    for code in sorted({k[0] for k in added + a_add + a_rem}):
        n0 = len(blocks[code]["flags"])
        n1 = (n0 + sum(1 for k in added + a_add if k[0] == code) - sum(1 for k in a_rem if k[0] == code))
        print(f"  {code}: {n0} flags -> {n1} after parts (a) and (b) so far")

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    mid = {c: dict(v) for c, v in vec.items()}
    for (c, k), r in rs.UNITS.items():
        mid[c][k] = r["verdict"]
    new = {c: dict(v) for c, v in mid.items()}
    for (c, k), r in UNITS.items():
        new[c][k] = r["verdict"]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v}, "fail": {c: sum(v[c][k] == 0.0 for k in cids)
                                                                             for c in v}}
    base, m1, after = summ(vec), summ(mid), summ(new)
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    left_units = [k for k in partb if k not in UNITS]
    left, c51n = {}, {}
    for c, _ in left_units:
        left[c] = left.get(c, 0) + 1
    for c, _ in c51:
        c51n[c] = c51n.get(c, 0) + 1
    check(len(left_units) == EXPECT["remaining"],
          f"{len(left_units)} D28 units remain for part (b), plus C5.1's second clause on {len(c51)} 1.0s")
    per = {}
    for _, k in left_units:
        per[k] = per.get(k, 0) + 1
    rem_line = (f"Left for part (b): {len(left_units)} D28 units (" +
                ", ".join(f"{k} {per[k]}" for k in cids if k in per) +
                f") and C5.1's second clause on {len(c51)} 1.0s (" + ", ".join(c for c, _ in c51) + ").")
    print("  " + rem_line)
    mp, mf = rs.dominance(mid, cids)
    ap, af = rs.dominance(new, cids)
    check(len(mp) == EXPECT["dominance_a"] and len(mf) == EXPECT["frontier_a"],
          f"part (a)'s result reproduced: {len(mp)} dominance pairs, frontier {len(mf)}")
    order = list(names)
    gained = sorted(set(ap) - set(mp), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(mp) - set(ap), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    dom_line = (f"After this group the corpus has {len(ap)} dominance pairs against {len(mp)} after part (a) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(af)} entries "
                f"against {len(mf)} (" + ", ".join(c for c in order if c in af) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(m1['total'][first[0]])} after part (a), "
                f"{rs.f1(after['total'][first[0]])} now.")
    print("  " + dom_line)

    # [7] the simulation runs --------------------------------------------------------------------------------------
    print(f"\n[7] THE SIMULATION RUNS ({SIMOUT})")
    sim = rs.read(SIMOUT)
    check(SIM_MD5 in sim.split("\n")[0], "runs made on the pinned engine: harness.js md5 " + SIM_MD5 +
          " (compassionism-simulation cd0ceec, v4.15)")
    check("median BLEI 1965 d, wealth poverty 16.6%, Gini 0.534, System Stability 88.5%" in sim,
          "the engine reproduces the simulation's documented seed-42 reference run")
    simt = sim_tables(sim)
    check(len(simt) == 2, "two run tables read (participation; Basic Unit adjustment)")

    # [8] the record -----------------------------------------------------------------------------------------------
    print(f"\n[8] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    t = tables(rs, r4, cdef, unit_order, names, base, m1, after, left, c51n)
    t["dominance"] = dom_line
    t["remaining"] = rem_line
    t["simulation run 1"], t["simulation run 2"] = simt[0], simt[1]
    GENERATED.clear()
    GENERATED.update(t)
    record = rs.read(RECORD)
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING PART (B), FIRST GROUP, COMPUTED." if ok else "\nRESCORING PART (B), FIRST GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
