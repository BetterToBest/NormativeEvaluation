#!/usr/bin/env python3
"""
rescoring_s43.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), sixth group: C3.5 Failure-Mode
Transparency and C4.1 Intergenerational Justice, their ten part (b) units
==============================================================================================================
Session 43. Parts (a) and (b1) to (b5) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s42.md (rescoring_s37.py to
rescoring_s42.py). This script holds the sixth group: C3.5's two part (b) units and C4.1's eight, taken together
as Handoff 42 proposed, since both criteria set outcome levels (rates, a share of costs, an emissions cut, a debt
ratio) that the group's designs must estimate rather than specify. It changes no file and no score: the pass's
changes are applied by generator when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). A clause the audit coded A is
carried as cleared on the unit's own text, except where listed in EXCEPT with its reason (none in this group); the
script asserts that no clause departs from the audit's A codes. A clause marked "not estimated in this pass" is
allowed only where another clause of the same unit already fixes the verdict. The audit's four out-of-reach codes
in this group are asserted unchanged (D31 search, reading 3.6).

CHECKS: the group against the audit's register (the part (b) units of C3.5 and C4.1); every record complete; the
rule; the audit's codes carried; every silent clause estimated or validly left; reach; flags against the summary
blocks, cumulatively with parts (a) to (b5); the consequences of the pass so far (totals, ranks, failures, tiers,
dominance, frontier, what remains, the criteria left with no 1.0); the anchor examples the pass so far moves and
the bands left with no corpus unit; and that NEEC_Rescoring_s43.md contains every generated table verbatim.

Usage: python3 rescoring_s43.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, rescoring_s37.py to
                                   rescoring_s42.py and the files they read, and NEEC_Rescoring_s43.md beside
                                   itself; writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, AUDIT = "criteria.json", "neec_corpus.json", "r4_audit_s35.py"
PRIOR = (("(a)", "rescoring_s37", "rescoring_s37.py"), ("(b1)", "rescoring_s38", "rescoring_s38.py"),
         ("(b2)", "rescoring_s39", "rescoring_s39.py"), ("(b3)", "rescoring_s40", "rescoring_s40.py"),
         ("(b4)", "rescoring_s41", "rescoring_s41.py"), ("(b5)", "rescoring_s42", "rescoring_s42.py"))
RECORD = "NEEC_Rescoring_s43.md"
GROUP = ("C3.5", "C4.1")
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
NOTEST = "not estimated in this pass"
HUB = "research hub at 8e8a6ba"
SIM = "harness.js and index.html at cd0ceec"
INTEGRAL = "integralcollective.io, accessed 2026-09-23"
DOC = {"DE": "NEEC_DoughnutEconomics_scoring_scratch.md", "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
       "OS": "NEEC_Ostrom_Commons_scoring_scratch.md"}
REACH_SRC = "r4_audit_s35.py, REACH; reading 3.6"

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in Appendix B's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- departures from the audit's A codes, each with its reason (asserted both ways) ------------------------------
EXCEPT = {}

# ---- C3.5 Failure-Mode Transparency (reading 3.2) ---------------------------------------------------------------
U("CCO", "C3.5", 0.5, [
    ("C", "Failures legible and diagnosable", AUD),
    ("C", "Failures legible and diagnosable", AUD),
    ("U", "the design specifies monitoring institutions (real-time anomaly detection, AI risk models whose lowest alert "
          "level triggers enhanced monitoring with weekly human review, democratic review of major security changes, "
          "and a CIP dashboard) but states no share of identified failures successfully corrected; the nearest figure, "
          "the CIP paper's conviction probability of 0.62 for detected corruption, is an illustrative input to an "
          "expected-cost calculation for one class of failure, and below the bar in any case; the published model "
          "represents no detection, diagnosis or correction of failures (reading 3.2)",
     HUB + ": risk-mitigation-framework.html, sections 4.3, 10 and 12; citizens-internet-portal.html, section 8.2; "
     + SIM + " (searched)"),
    ("U", "no share of total costs externalised is stated or estimated; the rationale's grounds (flows visible on a "
          "ledger, member monitoring, a dashboard) concern the visibility of the system's own operations, not costs "
          "borne outside it; no design source located prices an environmental cost (none names a carbon tax), and the "
          "dashboard lists carbon emissions, energy use and waste reduction as metrics to display, not costs "
          "internalised (reading 3.2)",
     REP + "CCO C3.5; " + HUB + ": integrated-implementation-roadmap.html, Real-Time Dashboard Metrics; "
     "economic-modeling-simulation.html, section 9.1")],
  note="clauses 1 and 2 are carried as audited: the CIP paper's detection probability of 0.75 for corruption is "
       "neither a detection time nor a diagnosis share, and it covers one class of failure, so it does not contradict "
       "the rationale (section 7)")

U("INT", "C3.5", 0.5, [
    ("C", "triggers alarms", AUD),
    ("U", "FRS-2 analyses incoming signals against expected ranges, stated principles and prior baselines, and FRS-4 "
          "routes recommendations stating the observed problem and its likely cause to CDS; no share of failures whose "
          "cause is correctly identified is stated or modelled, the system has no implementation, and the corpus's own "
          "review sets a mechanism (system-dynamics modelling and historical comparison) beside the bar, not an "
          "estimate (reading 3.2)",
     INTEGRAL + ", The System: FRS (modules FRS-1 to FRS-7); Integral_NEEC_Review.md, C3.5"),
    ("U", "recommendations go to democratic deliberation in CDS, and FRS-6 keeps time series to evaluate whether past "
          "decisions achieved their stated outcomes; no share of identified failures successfully corrected is stated "
          "or modelled, and the review sets democratic deliberation and adaptive implementation beside the bar, not a "
          "level (reading 3.2)",
     INTEGRAL + ", The System: FRS (modules FRS-4 to FRS-6); Integral_NEEC_Review.md, C3.5"),
    ("C", "tendency to externalize costs", AUD)])

# ---- C4.1 Intergenerational Justice (readings 3.3 to 3.7) -------------------------------------------------------
U("DG", "C4.1", 0.5, [
    ("C", "Absolute reduction in resource extraction and emissions", AUD),
    ("C", "Absolute reduction in resource extraction", AUD),
    ("S", "the two stock-flow-consistent models of the post-growth and degrowth literature located both show the "
          "public debt ratio worsening once growth ends: in LowGrow SFC's Sustainable Prosperity scenario for Canada, "
          "public debt of about 55% of GDP in 2017 rises slowly but steadily to more than 80% of GDP by 2067, as GDP "
          "stabilises while government keeps borrowing and carbon-tax revenue falls to zero, against a peak of about "
          "66% in the growth scenarios; EUROGREEN's degrowth scenario for France reports the deficit, not the debt "
          "level, below 3% of GDP until 2040 and rising steeply after 2040 as GDP contracts, even with a wealth tax "
          "introduced to offset the rising deficit and debt ratios; so the modelled ratio crosses 80% within the "
          "modelled horizon and does not stabilise (reading 3.5)",
     "Jackson and Victor, The Transition to a Sustainable Prosperity, Ecological Economics 177 (2020) 106787, "
     "section 5.3 and Fig. 11; D'Alessandro, Cieplinski, Distefano and Dittmer, Feasible alternatives to green growth, "
     "Nature Sustainability 3 (2020) 329-335, Fig. 3d and Methods; How to pay for saving the world: Modern Monetary "
     "Theory for a degrowth transition, Ecological Economics (2023)"),
    ("C", "preservation for future generations", AUD)],
  flag=([1.0], "read at the horizon of the threshold's own carbon clause (2030), or at mid-century, the one modelled "
               "debt level located is below 80%, since LowGrow SFC's ratio crosses the bar only late in its fifty-year "
               "run; and LowGrow SFC models a post-growth rather than a degrowth design, while the degrowth model "
               "located reports no debt level (reading 3.5)"))

U("FALC", "C4.1", 0.5, [
    ("U", "the rationale says renewable energy and circular economy principles would preserve resources; the design's "
          "premise, energy abundance from renewables, is stated without an emissions path, and its reviewers describe "
          "the case as conditional on renewable and other technologies advancing faster than climate and ecological "
          "breakdown; no carbon reduction by 2030, or on any dated path, is stated or cited, and none is located "
          "(reading 3.3)",
     REP + "FALC C4.1; Bastani, Fully Automated Luxury Communism (2019); Mariqueo-Russell and Read, Fully automated "
     "luxury barbarism, Radical Philosophy (2019)"),
    ("C", "circular economy principles would preserve resources", AUD),
    ("U", NOTEST + "; the verdict is fixed by clause 1", ""),
    ("C", "eliminates the need to exploit the future", AUD)])

U("PE", "C4.1", 0.5, [
    ("U", "the model's pollution damage revealing mechanism prices pollution inside the annual planning procedure and, "
          "under the model's assumptions, reduces it to efficient levels with the polluter paying and victims "
          "compensated; an efficient level is not a stated reduction, and no carbon path by 2030 or on any dated path "
          "is stated or cited for the model, which has no implementation (reading 3.3)",
     REP + "PE C4.1; Hahnel, Participatory Economics and the Next System (2017); Hahnel, Wanted: A Pollution Damage "
     "Revealing Mechanism, Review of Radical Political Economics (2017)"),
    ("C", "can incorporate long-term ecological preservation", AUD),
    ("U", NOTEST + "; the verdict is fixed by clauses 1 and 4", ""),
    ("U", "the rationale says future generations are represented through explicit councils; the model's literature "
          "states intergenerational equity and efficiency as goals that imply environmental sustainability and "
          "specifies long-run investment planning, but no council representing future generations is located in it, "
          "and no transfer to the next generation is estimated (reading 3.3; section 6)",
     REP + "PE C4.1; Hahnel, A Participatory Economy (2022); Hahnel and Kerkhoff, Integrating Investment and Annual "
     "Planning, Review of Radical Political Economics 52:2 (2020)")])

U("CCO", "C4.1", 0.5, [
    ("C", "35-45% trajectory achievable", AUD),
    ("U", "no comparison of resource use with regeneration is stated; the roadmap's resource table projects 60-90% "
          "reductions in the paper, energy and water use it lists (50 million reams, 500 GWh and 2 billion gallons a "
          "year) without saying whose use they are, and the implementation framework names regeneration among the "
          "environmental-health dimensions to monitor; the published model represents no resource flows (reading 3.3)",
     HUB + ": integrated-implementation-roadmap.html, Appendix D; universal-implementation-framework.html "
     "(environmental health); " + SIM + " (searched)"),
    ("U", "the design states a five-year implementation budget of $54.1 billion, fiscal break-even by year 6 through "
          "conversion fees, PTF rental revenues and reduced social-service costs, and a projected annual surplus of "
          "$89 billion by year 10; that is a fiscal flow, not a debt level, no debt-to-GDP ratio under the design is "
          "stated for any economy it serves, and the published model has no public-finance side (reading 3.4)",
     HUB + ": integrated-digital-governance.html, section 6.3; " + SIM + " (searched)"),
    ("C", "Positive intergenerational wealth transfer", AUD)],
  note="clause 1 is carried as audited, although no research-hub source names a carbon tax as CCO's funding, as the "
       "rationale does (section 6); the design's own carbon figures are a roadmap target of 35-45% by year 3, in a "
       "table that does not say whose footprint it covers, and a modelled 45% below baseline trajectory over 20 "
       "years, neither dated to 2030 (reading 3.7)")

U("INT", "C4.1", 0.5, [
    ("U", "the design treats ecological sustainability as a structural requirement, with FRS monitoring ecological "
          "thresholds and OAD assessing ecological and lifecycle impacts; no emissions path is stated or modelled, and "
          "the corpus's own review reaches a plausible 35%+ reduction by 2030 by inference from the post-growth design, "
          "not from a design source (reading 3.3)",
     REP + "INT C4.1; Integral_NEEC_Review.md, C4.1; " + INTEGRAL + ", The System: FRS; White Paper v0.1, contents "
     "(OAD-3, OAD-4)"),
    ("C", "Ecological sustainability is treated as", AUD),
    ("U", NOTEST + "; the verdict is fixed by clause 1 (whether a debt-to-GDP clause applies to a post-monetary design "
          "is left to Report v2.0, reading 3.4)", ""),
    ("C", "enables intergenerational transfer of knowledge", AUD)])

U("DE", "C4.1", 0.5, [
    ("U", "the ecological ceiling includes climate change among nine planetary boundaries, a boundary the economy "
          "should respect rather than a reduction the framework delivers; by the entry's own scope decision the "
          "framework commits to no redistributive, ownership or monetary mechanism, and emission cuts in the "
          "jurisdictions that adopt it are those jurisdictions' own policies, not credited to a comprehensive system "
          "whose sources do not specify them; its authors' 2025 update finds that overshoot must reverse at nearly "
          "twice its current rate to safeguard Earth-system stability by 2050, a finding about the world, not a "
          "reduction achieved (reading 3.3)",
     DOC["DE"] + ", scope decision and C4.1; Raworth, Doughnut Economics (2017); Fanning and Raworth, Nature (2025); "
     "protocol 3.2 and D29(c)"),
    ("C", "an intergenerational-preservation device", AUD),
    ("U", "by the same scope decision the framework commits to no fiscal rule or monetary mechanism, and no debt path "
          "under it is stated or located (reading 3.4)",
     DOC["DE"] + ", scope decision"),
    ("U", "the ecological ceiling preserves Earth-system conditions for future generations as a goalpost; no transfer "
          "of wealth or assets to the next generation is estimated for the framework or its adopters (reading 3.3)",
     DOC["DE"] + ", C4.1")])

U("SWF", "C4.1", 0.5, [
    ("R", "economy-wide carbon emissions are not governed by the fund; the audit's code is confirmed, since the "
          "fund's ethics-based exclusions reach coal, tar sands and the highest-emitting oil-sands producers in its "
          "own portfolio while the state that owns it continues to license new oil and gas production, so the fund's "
          "climate rules govern what it holds, not the economy's emissions, and neither the entry's document "
          "nor the fund designs it scores place an emissions trajectory inside the fund (reading 3.6)",
     REACH_SRC + "; " + DOC["SWF"] + ", C4.1 and C4.2"),
    ("R", "the rate of resource extraction is not governed by the fund, which invests its proceeds; the audit's code "
          "is confirmed, since the extraction rate is set by the state's petroleum licensing, which the entry's own "
          "document records expanding in 2026, not by the fund or its spending rule (reading 3.6)",
     REACH_SRC + "; " + DOC["SWF"] + ", C4.2"),
    ("U", NOTEST + "; the verdict is fixed by clauses 1 and 2", ""),
    ("C", "explicitly-designed intergenerational wealth-transfer mechanism", AUD)],
  note="Qatar's C4.1 flag (alternative 1.0) names this unit as its precedent; when the pass is applied and the flag "
       "registers are recomputed, that flag's basis needs restating (section 6)")

U("OS", "C4.1", 0.5, [
    ("R", "economy-wide carbon reduction is not governed by resource-commons institutions; the audit's code is "
          "confirmed under D31, since the transfer of the design to global commons is disputed within the mechanism's "
          "own literature: Ostrom's 2009 World Bank paper finds solutions much easier to craft for smaller-scale "
          "common-pool resources than for the global commons, and Stern (2011) concludes that design principle 7 must "
          "be rewritten for them; the carbon storage the entry credits is resource use at or below regeneration, "
          "clause 2's subject (reading 3.6)",
     REACH_SRC + "; " + DOC["OS"] + ", C4.1 and C4.2 (Ostrom, World Bank, 2009; Stern, International Journal of the "
     "Commons, 2011)"),
    ("C", "Resource use at or below regeneration is the mechanism", AUD),
    ("R", "public debt is not governed by commons institutions; the audit's code is confirmed, since the entry's own "
          "flag records that the mechanism does not address the debt-to-GDP clause, and none of the design principles "
          "concerns public finance (reading 3.6)",
     REACH_SRC + "; " + DOC["OS"] + ", C4.1"),
    ("C", "Positive intergenerational transfer is not a projection", AUD)],
  note="the document's flag, whose alternative was 0.5, is removed: the unit is 0.5 on reach")

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 10, "per_criterion": {"C3.5": 2, "C4.1": 8}, "stand": [], "points": 5.0,
          "silent": 18, "not_estimated": [("FALC", "C4.1", 2), ("INT", "C4.1", 2), ("PE", "C4.1", 2),
                                          ("SWF", "C4.1", 2)],
          "reach": [("OS", "C4.1", 0), ("OS", "C4.1", 2), ("SWF", "C4.1", 0), ("SWF", "C4.1", 1)],
          "flags_added": [("DG", "C4.1")], "flags_removed": [("OS", "C4.1")],
          "remaining": 27, "dominance_b5": 18, "frontier_b5": 13, "anchors_moved": 10,
          "bands_empty": [("C1.1", "1.0"), ("C2.1", "1.0"), ("C2.3", "1.0"), ("C2.4", "1.0"), ("C3.1", "1.0"),
                          ("C3.5", "1.0"), ("C4.1", "1.0")],
          "emptied": {"C2.3": "(b1)", "C2.4": "(b1)", "C3.1": "(b2)", "C1.1": "(b3)", "C2.1": "(b4)",
                      "C3.5": "(b6)", "C4.1": "(b6)"},
          "ones_left": {"C3.5": [], "C4.1": []}, "published_ones": {"C3.5": 3, "C4.1": 8}}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables(rs, r4, cdef, order, names, steps, left):
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
    base, prev, after = steps[0], steps[-2], steps[-1]
    rb, rp, rn = rs.ranks(base["total"]), rs.ranks(prev["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After (b5) (rank) | After this group (rank) | Change here | Failures | Tier | "
            "D28 units left | Floor if all fall |",
            "|---|---:|---:|---:|---:|---:|---|---:|---:|"]
    for code in rs.order_codes(names, base):
        lf = left.get(code, 0)
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(prev['total'][code])} ({rp[code]}) | "
                    f"{f1(after['total'][code])} ({rn[code]}) | {f1(after['total'][code] - prev['total'][code])} | "
                    f"{after['fail'][code]} | {rs.tier(after['fail'][code])} | {lf} | "
                    f"{f1(after['total'][code] - 0.5 * lf)} |")
    t["consequences"] = "\n".join(rows)
    return t


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    r4 = load("r4_audit_s35", AUDIT)
    mods = [load(mod, path) for _, mod, path in PRIOR]
    rs = mods[0]
    crit = json.loads(rs.read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}
    prior = tuple(m.UNITS for m in mods)

    print(f"NEEC rescoring pass, part (b), sixth group: C3.5, C4.1 ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {AUDIT}, " + ", ".join(p for _, _, p in PRIOR) + f", {RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    done = set().union(*(set(p) for p in prior))
    partb = [k for k in d28 if k not in prior[0]]
    grp = [k for k in partb if k[1] in GROUP and k not in done]
    check(len(d28) == 134 and len(partb) == 101, "D28's population 134; part (b) 101")
    per = {g: sum(1 for k in grp if k[1] == g) for g in GROUP}
    check(sorted(UNITS) == sorted(grp) and per == EXPECT["per_criterion"] and all(vec[c][k] == 1.0 for c, k in UNITS)
          and not set(UNITS) & done,
          f"this group holds exactly the part (b) units of C3.5 and C4.1 ({len(grp)}: "
          + ", ".join(f"{g} {per[g]}" for g in GROUP) + "), every one a corpus 1.0 and none re-estimated before")
    pub = {g: sorted(c for c in vec if vec[c][g] == 1.0) for g in GROUP}
    in_a = {g: sorted(c for (c, k) in prior[0] if k == g) for g in GROUP}
    check({g: len(v) for g, v in pub.items()} == EXPECT["published_ones"]
          and all(sorted([c for c, k in UNITS if k == g] + in_a[g]) == pub[g] for g in GROUP),
          "with part (a)'s, they are all of the two criteria's published 1.0s (" + "; ".join(
              f"{g} {len(pub[g])}" + (f", of which part (a) took {', '.join(in_a[g])}" if in_a[g] else "")
              for g in GROUP) + ")")
    for g in GROUP:
        print(f"  {g}: " + ", ".join(c for c, k in grp if k == g))

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
            if st == "U" and not est.startswith(NOTEST) and not src.strip():
                bad.append(f"{key} clause {k + 1}: an estimated clause without the source searched")
            if "|" in est + src + (rec["flag"][1] if rec["flag"] else "") + rec["note"]:
                bad.append(f"{key} clause {k + 1}: a pipe character would break the table")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per clause, in Appendix B's order; every cleared, short, out-of-reach "
                   "and moot clause, and every clause estimated as not shown, carries its source")
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
          f"{len(stand)} of {len(UNITS)} stand; {len(UNITS) - len(stand)} become 0.5 ({rs.f1(points)} points)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    departs = {(k[0], k[1], i) for k, r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"])
               if (reg[k][i] == "A" and st != "C") or (reg[k][i] == "N" and st != "M")}
    check(departs == set(EXCEPT) == set(),
          "no departure from the audit's A codes: every clause the audit coded A is carried as cleared")
    silent = {(k[0], k[1], i) for k in UNITS for i, ch in enumerate(reg[k]) if ch == "S"}
    notest = sorted((k[0], k[1], i) for k, r in UNITS.items() for i, (st, est, _) in enumerate(r["clauses"])
                    if est.startswith(NOTEST))
    fixed = all(UNITS[(c, k)]["clauses"][i][0] == "U" and any(
        j != i and st in "SUR" and not est.startswith(NOTEST)
        for j, (st, est, _) in enumerate(UNITS[(c, k)]["clauses"])) for c, k, i in notest)
    check(len(silent) == EXPECT["silent"] and set(notest) <= silent and notest == sorted(EXPECT["not_estimated"])
          and fixed,
          f"the audit coded {len(silent)} clauses of this group silent; {len(silent) - len(notest)} are estimated here, "
          f"and {len(notest)} are left not estimated, each in a unit whose verdict another clause already fixes")
    for c, k, i in notest:
        print(f"  {c} {k} clause {i + 1}: not estimated in this pass (verdict fixed by another clause)")
    est_status = {}
    for c, k, i in sorted(silent):
        if (c, k, i) not in notest:
            st = UNITS[(c, k)]["clauses"][i][0]
            est_status[st] = est_status.get(st, 0) + 1
    print("  silent clauses estimated here: " + ", ".join(f"{STATUS[s]} {n}" for s, n in sorted(est_status.items())))

    # [4] reach ----------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = {x for x in r4.REACH if (x[0], x[1]) in UNITS}
    check(now_r == was_r == set(EXPECT["reach"]),
          f"the audit's {len(was_r)} out-of-reach codes in this group are confirmed and no other clause is out of reach "
          f"(no D31 source places the economy's emissions, its extraction rate or public debt inside the fund or the "
          f"commons institution)")
    for c, k, i in sorted(now_r):
        print(f"  {c} {k} clause {i + 1}: {r4.REACH[(c, k, i)]}")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b5))")
    blocks = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}

    def changes(units):
        add = sorted(k for k, r in units.items() if r["flag"] and k not in had)
        rem = sorted(k for k, r in units.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
        return add, rem
    added, removed = changes(UNITS)
    kept = sorted(k for k in UNITS if k in had and k not in removed)
    check(added == sorted(EXPECT["flags_added"]) and removed == sorted(EXPECT["flags_removed"]) and not kept,
          f"flags added {len(added)} ({', '.join(c for c, _ in added)}); removed {len(removed)} "
          f"({', '.join(c for c, _ in removed)}, now scored at its own alternative); no other unit of this group "
          f"carried a flag")
    adds, rems = list(added), list(removed)
    for part in prior:
        a, r = changes(part)
        adds += a
        rems += r
    moved = sorted({k[0] for k in adds + rems})
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Across the pass so far, "
                 f"{len(moved)} entries' flag registers change ({', '.join(moved)}).")
    print("  " + flag_line)
    # a flag outside the group whose stated reading rests on a unit this group moves (restated when applied)
    prec = {("QA", "C4.1"): ("SWF", "C4.1", "SWF Statism precedent", [1.0])}
    check(all(k in had and had[k]["reading"] == why and had[k]["alternatives"] == alts
              and UNITS[(u, c)]["verdict"] == 0.5 and vec[u][c] == 1.0 for k, (u, c, why, alts) in prec.items()),
          "a flag outside this group rests on a unit it moves: " + "; ".join(
              f"{k[0]} {k[1]} (alternative {rs.fmt_alts(a)}, reading '{w}') cites {u} {c}, 1.0 to 0.5"
              for k, (u, c, w, a) in prec.items()))

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        vsteps.append(v)
    v5, vn = vsteps[-2], vsteps[-1]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, m5, after = steps[0], steps[-2], steps[-1]
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    left_units = [k for k in partb if k not in done and k not in UNITS]
    left, perc = {}, {}
    for c, k in left_units:
        left[c] = left.get(c, 0) + 1
        perc[k] = perc.get(k, 0) + 1
    check(len(left_units) == EXPECT["remaining"], f"{len(left_units)} D28 units remain for part (b)")
    rem_line = (f"Left for part (b): {len(left_units)} D28 units (" +
                ", ".join(f"{k} {perc[k]}" for k in cids if k in perc) + ").")
    print("  " + rem_line)
    order = list(names)
    ones = {g: [c for c in order if vn[c][g] == 1.0] for g in GROUP}
    check(ones == EXPECT["ones_left"],
          "1.0s each of this group's criteria keeps: " + "; ".join(
              f"{g} {len(ones[g])} (published {len(pub[g])})" for g in GROUP))
    tags = ("published", "(a)", "(b1)", "(b2)", "(b3)", "(b4)", "(b5)", "(b6)")
    emptied = {}
    for tag, v in zip(tags, vsteps):
        for k in cids:
            if k not in emptied and not any(v[c][k] == 1.0 for c in v):
                emptied[k] = tag
    check(all(any(vsteps[0][c][k] == 1.0 for c in vec) for k in cids) and emptied == EXPECT["emptied"],
          "every criterion had a 1.0 in the published corpus; the pass so far leaves " + str(len(emptied)) +
          " with none: " + ", ".join(f"{k} (part {emptied[k]})" for k in emptied))
    ones_line = ("After this group, the entries scoring 1.0 on this group's criteria are: " + "; ".join(
        f"{g}, {len(ones[g])}" + (f" ({', '.join(ones[g])})" if ones[g] else "") for g in GROUP) +
        ", against " + " and ".join(f"{len(pub[g])} published" for g in GROUP) +
        ". Every criterion had a 1.0 in the published corpus; after the pass so far no entry scores 1.0 on " +
        str(len(emptied)) + " of them: " + ", ".join(f"{k} (emptied in part {emptied[k]})" for k in cids
                                                     if k in emptied) + ".")
    print("  " + ones_line)
    p5, f5 = rs.dominance(v5, cids)
    pn, fn = rs.dominance(vn, cids)
    check(len(p5) == EXPECT["dominance_b5"] and len(f5) == EXPECT["frontier_b5"],
          f"part (b5)'s result reproduced: {len(p5)} dominance pairs, frontier {len(f5)}")
    gained = sorted(set(pn) - set(p5), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(p5) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    allparts = prior + (UNITS,)
    n_all = sum(len(p) for p in allparts)
    st_all = sum(1 for p in allparts for r in p.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for p in allparts for r in p.values())
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(p5)} after part (b5) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(f5)} (" + ", ".join(c for c in order if c in fn) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(m5['total'][first[0]])} after part (b5), "
                f"{rs.f1(after['total'][first[0]])} now. Across parts (a) and (b1) to (b6), {n_all} units have been "
                f"re-estimated: {st_all} stand and {n_all - st_all} become 0.5 ({rs.f1(pts_all)} points).")
    print("  " + dom_line)

    # [7] anchors --------------------------------------------------------------------------------------------------
    print("\n[7] ANCHOR EXAMPLES THE PASS SO FAR MOVES (build_criteria.py checks examples against published scores)")
    code_of = {v: k for k, v in names.items()}
    allu, part_of = {}, {}
    for tag, p in zip(("(a)", "(b1)", "(b2)", "(b3)", "(b4)", "(b5)", "(b6)"), allparts):
        allu.update(p)
        part_of.update({k: tag for k in p})
    hits, empty = [], []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                code = code_of.get(ex["system"])
                if code and (code, c["id"]) in allu and allu[(code, c["id"])]["verdict"] != ex["cited"]:
                    hits.append(f"{c['id']}'s {band} example, {code} (part {part_of[(code, c['id'])]}, to "
                                f"{rs.f1(allu[(code, c['id'])]['verdict'])})")
                    if not any(vn[x][c["id"]] == float(band) for x in vn):
                        empty.append((c["id"], band))
    check(len(hits) == EXPECT["anchors_moved"], f"{len(hits)} anchor examples cite a unit the pass moves")
    check(empty == EXPECT["bands_empty"],
          "bands left with no corpus unit at their value: " + ", ".join(f"{c}'s {b}" for c, b in empty))
    keeps = [c for c in order if vn[c]["C2.5"] == 1.0]
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) +
                   ". When the pass is applied, each band needs an example the corpus then scores at that value; " +
                   ", ".join(f"{c}'s {b}" for c, b in empty) + " bands have none left (part (b4), reading 3.5; "
                   "reading 3.8 here); C2.5's 1.0 band keeps one (" + ", ".join(keeps) + ", flagged; part (b5), "
                   "reading 3.7).")
    print("  " + anchor_line)

    # [8] the record -----------------------------------------------------------------------------------------------
    print(f"\n[8] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    t = tables(rs, r4, cdef, unit_order, names, steps, left)
    t["dominance"], t["remaining"], t["flags"], t["anchors"], t["ones"] = (dom_line, rem_line, flag_line,
                                                                          anchor_line, ones_line)
    GENERATED.clear()
    GENERATED.update(t)
    record = rs.read(RECORD) if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING PART (B), SIXTH GROUP, COMPUTED." if ok else "\nRESCORING PART (B), SIXTH GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
