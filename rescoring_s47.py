#!/usr/bin/env python3
"""
rescoring_s47.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), seventh group: C4.2 Ecological
Compliance and C4.4 Power Distribution, on the v2.0 clauses
==============================================================================================================
Session 47. Parts (a) and (b1) to (b6) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s43.md (rescoring_s37.py to
rescoring_s43.py). This script holds the seventh group, the first scored on the v2.0 criteria (decision 7.1 of
the Session 44 review: the pass continues on the revised clauses, so C4.2 and C4.4 are scored once): the ten
part (b) units of C4.2 and C4.4, and the three units of the same criteria that part (a) re-estimated on the
Session 44 clauses (MMT + Job Guarantee's C4.2; Nordic Social Democracy's and Market Socialism's C4.4), re-read
here on the v2.0 clauses. It changes no file and no score: the pass's changes are applied by generator when it
ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). The clauses are v2.0's
(criteria.json, the Pass Threshold's `clauses`); the R4 audit coded the Session 44 clauses, and MAP says which
Session 44 clause each v2.0 clause continues. A clause the audit coded A on a clause v2.0 keeps verbatim is
carried as cleared on the unit's own text; on a clause v2.0 restates, the audited phrase is read again against the
restated clause (reading 3.2) and either carried ("as audited, re-read") or estimated, and both lists are
asserted. A clause marked "not estimated in this pass" is allowed only where another clause of the same unit
already fixes the verdict. A re-read unit of part (a) can keep its verdict or rise (class D, NEEC_Criteria_v2_s45.md
section 7), and its record here supersedes part (a)'s.

CHECKS: the group against the audit's register (the part (b) units of C4.2 and C4.4) and against part (a); every
record complete, on v2.0's clauses; the rule; the audit's codes carried or re-read; every silent clause estimated or
validly left; reach; flags against the summary blocks, cumulatively with parts (a) to (b6); the consequences of the
pass so far on the published 26-criterion structure (totals, ranks, failures, tiers, dominance, frontier, what
remains, the criteria left with no 1.0); the anchor examples the pass so far moves and the bands left with no
corpus unit; and that NEEC_Rescoring_s47.md contains every generated table verbatim.

Usage: python3 rescoring_s47.py   (reads criteria.json (v2.0), criteria_s44_snapshot.json (the published
                                   structure and anchors), neec_corpus.json, r4_audit_s35.py, rescoring_s37.py to
                                   rescoring_s43.py and the files they read, and NEEC_Rescoring_s47.md beside
                                   itself; writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CRIT44, CORPUS, AUDIT = "criteria.json", "criteria_s44_snapshot.json", "neec_corpus.json", "r4_audit_s35.py"
PRIOR = (("(a)", "rescoring_s37", "rescoring_s37.py"), ("(b1)", "rescoring_s38", "rescoring_s38.py"),
         ("(b2)", "rescoring_s39", "rescoring_s39.py"), ("(b3)", "rescoring_s40", "rescoring_s40.py"),
         ("(b4)", "rescoring_s41", "rescoring_s41.py"), ("(b5)", "rescoring_s42", "rescoring_s42.py"),
         ("(b6)", "rescoring_s43", "rescoring_s43.py"))
RECORD = "NEEC_Rescoring_s47.md"
GROUP = ("C4.2", "C4.4")
# v2.0 clause index -> the Session 44 clause it continues (the audit's index); RESTATED: v2.0 clauses whose wording
# changed (C4.2: carbon now consumption-based and a rate, K3/G3; boundaries now four downscaled, K4). C4.4 keeps
# its third and fourth Session 44 clauses verbatim and deletes the first two (K1, K2).
MAP = {"C4.2": (0, 1, 2, 3), "C4.4": (2, 3)}
RESTATED = {"C4.2": (0, 3), "C4.4": ()}
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
AUDRE = "as audited, re-read against the v2.0 clause (the unit's own text; reading 3.2)"
NOTEST = "not estimated in this pass"
HUB = "research hub at 8e8a6ba"
SIM = "harness.js and index.html at cd0ceec"
INTEGRAL = "integralcollective.io, accessed 2026-09-24"
INTWP = "Integral white paper v0.1 (INTEGRAL-Paper-V0.1.pdf, md5 a6defc9a, accessed 2026-09-24)"
DEDOC = "NEEC_DoughnutEconomics_scoring_scratch.md"
OTERO = ("Otero, Rigal, Pereira, Kim, Gamboa, Tello and Grêt-Regamey, Degrowth scenarios for biodiversity? Key "
         "methodological steps and a call for collaboration, Sustainability Science (2024), "
         "doi:10.1007/s11625-024-01483-9, abstract and section 1; IPBES Global Assessment (2019), as cited there")
S43 = "NEEC_Rescoring_s43.md, "

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in v2.0's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- departures from the audit's A codes on verbatim clauses, each with its reason (asserted both ways) ----------
EXCEPT = {}
# ---- A codes on restated clauses: carried after re-reading (reading 3.2), or estimated -----------------------------
REREAD_CARRIED = [("DG", "C4.2", 0), ("DG", "C4.2", 3), ("FALC", "C4.2", 3), ("PE", "C4.2", 3), ("INT", "C4.2", 3),
                  ("DE", "C4.2", 3)]
REREAD_ESTIMATED = [("CCO", "C4.2", 0)]

# ---- C4.2 Ecological Compliance (readings 3.2 to 3.4) -------------------------------------------------------------
BIO = ("no projection of pressure on species or habitat under the design is stated, modelled or located (reading 3.3)")
U("DG", "C4.2", 0.5, [
    ("C", "designed for absolute reductions", AUDRE),
    ("U", "the degrowth literature's own scenario researchers write that, to date, degrowth scenarios have not been "
          "explored for biodiversity conservation and human wellbeing, and set out the steps (visions, pathways, "
          "social-ecological interactions, modelling) by which they could be; the IPBES Global Assessment, as they cite "
          "it, finds degrowth's transformative potential for biodiversity high but the evidence of its effectiveness "
          "still inconclusive; " + BIO, OTERO),
    ("U", NOTEST + "; the verdict is fixed by clause 2", ""),
    ("C", "explicitly bounded by planetary limits", AUDRE)])

U("FALC", "C4.2", 0.5, [
    ("U", "the design's premise, energy abundance from renewables, is stated without an emissions path, as part (b6) "
          "found for C4.1's carbon clause; no rate of fall in consumption-based emissions is stated, cited or located "
          "(reading 3.4)",
     REP + "FALC C4.2; " + S43 + "FALC C4.1, clause 1; Bastani, Fully Automated Luxury Communism (2019)"),
    ("U", "the design's case for food without animals argues that precision fermentation and cellular agriculture "
          "could produce meat, milk and eggs on a small fraction of the land and water livestock needs, an argument "
          "about land demand that is conditional on the technology; " + BIO,
     REP + "FALC C4.2; Bastani, Fully Automated Luxury Communism (2019), Food without Animals"),
    ("C", "automated resource optimization could achieve ecological sustainability", AUD),
    ("C", "harmonize human activity with planetary boundaries", AUDRE)])

U("PE", "C4.2", 0.5, [
    ("U", "the model's pollution damage revealing mechanism prices pollution inside annual planning and, under the "
          "model's assumptions, reduces it to efficient levels; an efficient level is not a rate of reduction, and no "
          "emissions path is stated or cited for the model, which has no implementation, as part (b6) found for "
          "C4.1's carbon clause (reading 3.4)",
     S43 + "PE C4.1, clause 1; Hahnel, Wanted: A Pollution Damage Revealing Mechanism, Review of Radical Political "
     "Economics (2017)"),
    ("U", "the planning councils can constrain production and consumption within ecological limits and price "
          "ecological damage; " + BIO,
     REP + "PE C4.2; Hahnel, Wanted: A Pollution Damage Revealing Mechanism, Review of Radical Political Economics "
     "(2017)"),
    ("C", "sustainable resource use", AUD),
    ("C", "within ecological limits", AUDRE)])

U("CCO", "C4.2", 0.5, [
    ("U", "the audited phrase, a 35-45% reduction trajectory with a carbon tax, states a size without a horizon and "
          "so no rate (reading 3.2); the design's model reports total emissions 45% below an unstated baseline "
          "trajectory over 20 years, of which consumption-driven emissions fall 24%, which fixes no absolute rate "
          "without the baseline (against a flat one it is about 2.9% a year), and the roadmap's carbon targets (15-20% "
          "in year 1 to 70-80% in year 7) are targets in a table that does not say whose emissions it covers; the "
          "published model represents no emissions (reading 3.4)",
     HUB + ": economic-modeling-simulation.html, section 9.1; integrated-implementation-roadmap.html, Appendix D and "
     "Success Metrics; " + SIM + " (searched, " + S43 + "reading 3.7)"),
    ("U", "biodiversity appears in the design's sources as a metric to monitor (environmental health: emissions, "
          "biodiversity, regeneration) and, in a glossary example, as one of the stewardship results a Public Trust "
          "Foundation may reward in Acre Equity; " + BIO,
     HUB + ": universal-implementation-framework.html, section 8.2; wiki/glossary.html (Acre Equity); " + SIM +
     " (searched)"),
    ("U", "the roadmap's resource table projects cuts of 60-90% in the paper, energy and water use it lists without "
          "saying whose use they are, and no comparison of resource use with regeneration or biocapacity is stated; "
          "the published model represents no resource flows, as part (b6) found for C4.1's regeneration clause",
     HUB + ": integrated-implementation-roadmap.html, Appendix D; " + S43 + "CCO C4.1, clause 2"),
    ("U", "no planetary boundary is named in the design's sources, which list regeneration among the environmental "
          "metrics to monitor; no boundary is assessed for the design",
     HUB + ": universal-implementation-framework.html, section 8.2 (all hub pages searched)")])

U("INT", "C4.2", 0.5, [
    ("U", "OAD computes embodied carbon and lifecycle impacts for each design, and CDS's context model carries "
          "emissions proxies into deliberation; no emissions path for the economy is stated or modelled, as part (b6) "
          "found for C4.1's carbon clause (reading 3.4)",
     INTWP + ", OAD module 3 and CDS module 3; " + S43 + "INT C4.1, clause 1"),
    ("U", "the white paper names biodiversity collapse among the crises of market systems and couples production to "
          "ecological thresholds, footprints and risk metrics in CDS, OAD and FRS; " + BIO,
     INTWP + ", introduction and section 5; " + INTEGRAL + ", The System: FRS"),
    ("U", "the design states that production stays within planetary boundaries through real-time ecological feedback, "
          "with material footprints computed for designs and FRS flagging constraint violations; no footprint of "
          "consumption against biocapacity, or other comparison of extraction with regeneration, is estimated, and "
          "the system has no implementation",
     INTWP + ", design principles (Ecological Balance) and OAD module 3; " + INTEGRAL + ", The System: FRS (FRS-3, "
     "constraint modeling); Integral_NEEC_Review.md, C4.2"),
    ("C", "enforce planetary-boundary compliance", AUDRE)])

U("DE", "C4.2", 0.5, [
    ("U", "by the entry's scope decision the framework is a compass, not a map, and commits to no mechanism, so a "
          "cut in the emissions of the places that adopt it is those places' own policy, not credited to a framework "
          "whose sources do not specify it, as part (b6) found for C4.1's carbon clause (reading 3.4)",
     DEDOC + ", scope decision and C4.2; " + S43 + "DE C4.1, clause 1; protocol 3.2 and D29(c)"),
    ("U", "biodiversity breakdown is one of the nine boundaries of the framework's ecological ceiling, and its "
          "authors' monitoring measures the world's overshoot of it; the ceiling is a goalpost the economy should "
          "respect, and " + BIO,
     DEDOC + ", C4.2; Fanning and Raworth, Nature (2025)"),
    ("U", "the national doughnut accounts compare consumption-based footprints with per-person boundaries as a "
          "diagnosis; by the scope decision no reduction of extraction to regeneration is delivered by the framework "
          "or estimated for its adopters",
     DEDOC + ", scope decision and C4.2; Fanning, O'Neill, Hickel and Roux, Nature Sustainability 5 (2022) 26-36"),
    ("C", "incorporated as a hard structural design element", AUDRE)])

# ---- C4.4 Power Distribution (readings 3.5 and 3.6) -------------------------------------------------------------
U("DG", "C4.4", 0.5, [
    ("U", "the rationale names decentralisation, wealth caps, cooperative ownership and democratic governance, "
          "mechanisms and a goal rather than a share of major decisions; degrowth research treats the forms of "
          "democracy compatible with degrowth as a subject of reflection and the conditions of its realisation as "
          "requiring additional study, and no estimate of the share of major decisions democratically accountable is "
          "stated, modelled or located (part (b1), reading 3.5)",
     REP + "DG C4.4; Kallis, Kostakis, Lange, Muraca, Paulson and Schmelzer, Research on Degrowth, Annual Review of "
     "Environment and Resources 43 (2018) 291-316, abstract"),
    ("U", "no mechanism of the entry's own for removing or replacing those who hold decision-making authority is "
          "specified or located; democratic governance named as a goal is not a mechanism, and the institutions of "
          "the polity that adopts degrowth policies are not credited to it (reading 3.5)",
     REP + "DG C4.4; Kallis et al. (2018); part (b5) reading 3.3; protocol 3.2 and D29(c)")])

U("PE", "C4.4", 1.0, [
    ("C", "comprehensive economic democracy", AUD),
    ("C", "workers' councils and consumers' councils elect recallable and rotated representatives to the federations "
          "that decide matters affecting an industry or a wider area, and the councils themselves decide by their "
          "members' votes; the iteration facilitation board applies announced adjustment rules and holds no authority "
          "over members (reading 3.5)",
     "participatoryeconomy.org, The Model: Overview (The Participatory Economy Project), accessed 2026-09-24")])

U("CCO", "C4.4", 1.0, [
    ("C", "CIP provides direct democratic power", AUD),
    ("C", "the design's governance paper gives Public Trust Housing leadership term limits and mandatory rotation, "
          "regular recall elections for underperforming leadership, and community authority over leadership selection "
          "and recall; the community juries that assess merit for conversion multipliers are selected at random and "
          "rotated to prevent capture (reading 3.5)",
     HUB + ": democratic-governance-pth.html, sections 6.2 and 6.3 and Appendix A (Community Authority); "
     "cultural-value-integration.html, section 3.3")],
  flag=([0.5], "the removal and replacement mechanisms the design specifies cover Public Trust Housing leadership and "
               "the merit juries; the governance of the other Public Trust Foundations is stated as tripartite "
               "community representation without a stated removal mechanism, and the currency's parameters are set "
               "through host institutions, so a reading that asks for a mechanism for every body the design creates "
               "leaves the clause not shown (reading 3.5)"))

U("INT", "C4.4", 1.0, [
    ("C", "broad democratic accountability", AUD),
    ("C", "the design delegates no managerial authority: decisions are taken by participants in CDS, and any decision "
          "can be reaffirmed, amended, revoked or reopened by the review module; production is coordinated by small "
          "rotating teams which, in the white paper's words, did not command but coordinated, a function COS "
          "formalises without managerial authority (reading 3.5)",
     INTWP + ", sections 5.2 and 5.5 and CDS module 10; " + INTEGRAL + ", The System: CDS and COS")],
  note="the corpus's review sets \"Removal mechanisms: Functional through democratic governance\" beside the bar, "
       "which is not a mechanism; the clause is cleared on the design's own white paper (section 6)")

# ---- part (a)'s units of the same criteria, re-read on v2.0 (reading 3.7) ----------------------------------------
U("MMT", "C4.2", 0.5, [
    ("U", "within reach under D31, as part (a) found; theoretically compatible with absolute reductions is not a "
          "rate of fall in consumption-based emissions",
     "Tcherneva, Levy WP 517 (2007); Tcherneva, La garantie d'emploi: l'arme sociale du Green New Deal (2021)"),
    ("U", "within reach under D31, as part (a) found; no estimate", "rescoring_s37.py, MMT C4.2"),
    ("U", "within reach under D31, as part (a) found; no estimate", "rescoring_s37.py, MMT C4.2"),
    ("U", "within reach under D31, as part (a) found; no estimate", "rescoring_s37.py, MMT C4.2")],
  note="part (a)'s unit re-read on v2.0's clauses: no clause was shown before and none is now, so it stays 0.5")

U("NSD", "C4.4", 0.5, [
    ("U", "the rationale names mechanisms (strong unions, proportional representation, worker board "
          "representation), not a share of major decisions; no source estimating the share of major economic and "
          "political decisions accountable to those they affect was located, and the nearest published indicator, "
          "V-Dem's power distributed by socioeconomic position, rates how far wealth and income translate into "
          "political power, not that share; public decisions answer to "
          "parliaments, while the major decisions of private firms answer to their owners, beside a minority of "
          "employee-elected board members (in Sweden two, or three at 1,000 employees, under the 1987 Board "
          "Representation Act), and whether 80% of major decisions are accountable turns on how the two are weighed, "
          "which no source measures (reading 3.6)",
     REP + "NSD C4.4; worker-participation.eu, Sweden (board-level representation); V-Dem Codebook v16, "
     "v2pepwrses"),
    ("C", "parliamentary removal functions: Sweden's prime minister lost a confidence vote on 21 June 2021, as part (a) "
          "found", "Riksdag confidence vote, 21 June 2021 (rescoring_s37.py, NSD C4.4)")],
  flag=([1.0], "read as accountability through institutions answerable to voters, with a minority employee voice on "
               "boards and collective agreements covering most employees, the Nordic economies' major decisions are "
               "democratically accountable; the clause's Measurement line, accountability of major decisions to "
               "those they affect, supports the reading applied (reading 3.6)"),
  note="part (a)'s unit re-read on v2.0's clauses: part (a) fixed it on the wealth-Gini clause, which v2.0 measures "
       "once, in C1.2b, and left this clause not estimated")

U("MS", "C4.4", 1.0, [
    ("C", "economic power distributed through democratic ownership", AUD),
    ("C", "worker cooperatives' members elect their administrators for fixed terms and can dismiss them in general "
          "assembly: under the Basque cooperatives law that governs Mondragon's cooperatives, administrators serve "
          "two to five years, the general assembly may dismiss them even when dismissal is not on the agenda (by two "
          "thirds of the votes), and elects their replacements in the same session (reading 3.5)",
     "Ley 11/2019, de 20 de diciembre, de Cooperativas de Euskadi (BOE-A-2020-615, consolidated), article 46; "
     "International Co-operative Alliance, Statement on the Cooperative Identity, principle 2")],
  note="part (a)'s unit re-read on v2.0's clauses: part (a) fixed it on the wealth-Gini clause, which v2.0 measures "
       "once, in C1.2b; both v2.0 clauses are shown, so it returns to its published 1.0")

REREAD = [("MMT", "C4.2"), ("NSD", "C4.4"), ("MS", "C4.4")]

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 13, "per_criterion": {"C4.2": 6, "C4.4": 4}, "reread": 3,
          "stand": [("CCO", "C4.4"), ("INT", "C4.4"), ("MS", "C4.4"), ("PE", "C4.4")], "points_b": 3.5,
          "rise": [("MS", "C4.4")],
          "silent": 20, "not_estimated": [("DG", "C4.2", 2)],
          "flags_added": [("CCO", "C4.4"), ("NSD", "C4.4")], "flags_removed": [],
          "remaining": 17, "dominance_b6": 18, "frontier_b6": 13, "anchors_moved": 11,
          "bands_empty": [("C1.1", "1.0"), ("C2.1", "1.0"), ("C2.3", "1.0"), ("C2.4", "1.0"), ("C3.1", "1.0"),
                          ("C3.5", "1.0"), ("C4.1", "1.0"), ("C4.2", "1.0")],
          "emptied": {"C2.3": "(b1)", "C2.4": "(b1)", "C3.1": "(b2)", "C1.1": "(b3)", "C2.1": "(b4)",
                      "C3.5": "(b6)", "C4.1": "(b6)", "C4.2": "(b7)"},
          "ones_left": {"C4.2": [], "C4.4": ["MS", "PE", "CCO", "INT"]}, "published_ones": {"C4.2": 7, "C4.4": 6}}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables(rs, v2, order, names, steps, left):
    t = {}
    f1, fmt = rs.f1, rs.fmt_alts
    rows = ["| Entry | Criterion | Clauses | Verdict | Flag |", "|---|---|---|---|---|"]
    for key in order:
        rec = UNITS[key]
        fl = f"alternative {fmt(rec['flag'][0])}" if rec["flag"] else ""
        was = "0.5 (part (a))" if key in REREAD else "1.0"
        rows.append(f"| {key[0]} | {key[1]} | {' '.join(st for st, _, _ in rec['clauses'])} | "
                    f"{was} → {f1(rec['verdict'])} | {fl} |")
    t["summary"] = "\n".join(rows)
    for key in order:
        rec, (code, crit) = UNITS[key], key
        was = "0.5 (part (a))" if key in REREAD else "1.0"
        head = f"#### {code} {crit} {v2[crit]['name']}: {was} → {f1(rec['verdict'])}"
        if rec["flag"]:
            head += " — flagged as contestable"
        lines = [head, "", "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for k, (st, est, src) in enumerate(rec["clauses"]):
            lines.append(f"| {k + 1} | {v2[crit]['definition']['clauses'][k]} | {STATUS[st]} | {est} | {src or '—'} |")
        if rec["flag"]:
            lines += ["", f"*Flag:* alternative {fmt(rec['flag'][0])}: {rec['flag'][1]}."]
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {code} {crit}"] = "\n".join(lines)
    base, prev, after = steps[0], steps[-2], steps[-1]
    rb, rp, rn = rs.ranks(base["total"]), rs.ranks(prev["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After (b6) (rank) | After this group (rank) | Change here | Failures | Tier | "
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
    crit = json.loads(rs.read(CRIT44))["criteria"]
    cids = [c["id"] for c in crit]
    v2 = {c["id"]: c for c in json.loads(rs.read(CRITERIA))["criteria"]}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}
    prior = tuple(m.UNITS for m in mods)

    print(f"NEEC rescoring pass, part (b), seventh group: C4.2, C4.4 on the v2.0 clauses ({RECORD})")
    print(f"inputs: {CRITERIA}, {CRIT44}, {CORPUS}, {AUDIT}, " + ", ".join(p for _, _, p in PRIOR) + f", {RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION AND THE v2.0 CLAUSES")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    done = set().union(*(set(p) for p in prior))
    partb = [k for k in d28 if k not in prior[0]]
    grp = [k for k in partb if k[1] in GROUP and k not in done]
    new = {k: r for k, r in UNITS.items() if k not in REREAD}
    check(len(d28) == 134 and len(partb) == 101, "D28's population 134; part (b) 101")
    per = {g: sum(1 for k in grp if k[1] == g) for g in GROUP}
    check(sorted(new) == sorted(grp) and per == EXPECT["per_criterion"] and all(vec[c][k] == 1.0 for c, k in new)
          and not set(new) & done,
          f"this group holds exactly the part (b) units of C4.2 and C4.4 ({len(grp)}: "
          + ", ".join(f"{g} {per[g]}" for g in GROUP) + "), every one a corpus 1.0 and none re-estimated before")
    pub = {g: sorted(c for c in vec if vec[c][g] == 1.0) for g in GROUP}
    in_a = {g: sorted(c for (c, k) in prior[0] if k == g) for g in GROUP}
    check({g: len(v) for g, v in pub.items()} == EXPECT["published_ones"]
          and all(sorted([c for c, k in new if k == g] + in_a[g]) == pub[g] for g in GROUP)
          and sorted(REREAD) == sorted((c, g) for g in GROUP for c in in_a[g])
          and all(prior[0][k]["verdict"] == 0.5 for k in REREAD) and len(REREAD) == EXPECT["reread"],
          "with part (a)'s, they are all of the two criteria's published 1.0s (" + "; ".join(
              f"{g} {len(pub[g])}, of which part (a) took {', '.join(in_a[g])}" for g in GROUP) + "); part (a)'s "
          f"{len(REREAD)}, each at 0.5 there, are re-read here on the v2.0 clauses")
    for g in GROUP:
        print(f"  {g}: " + ", ".join(c for c, k in grp if k == g) + "; re-read from part (a): "
              + ", ".join(c for c, k in REREAD if k == g))
    def words(t):  # a clause moved to the head of its threshold gains a capital; the words are what must match
        return t[:1].lower() + t[1:]
    same = all(words(v2[g]["definition"]["clauses"][i]) == words(r4.CLAUSES[g][MAP[g][i]][0])
               for g in GROUP for i in range(len(MAP[g])) if i not in RESTATED[g])
    restated = all(words(v2[g]["definition"]["clauses"][i]) != words(r4.CLAUSES[g][MAP[g][i]][0])
                   for g in GROUP for i in RESTATED[g])
    check(same and restated and all(len(v2[g]["definition"]["clauses"]) == len(MAP[g]) for g in GROUP)
          and all(v2[g]["revision"]["cls"] == cls for g, cls in (("C4.2", "M"), ("C4.4", "D"))),
          "v2.0's clauses: C4.2 (class M) keeps clauses 2 and 3 verbatim and restates 1 and 4; C4.4 (class D) keeps "
          "the Session 44 clauses 3 and 4 verbatim as its clauses 1 and 2 (the first now capitalised)")
    for g in GROUP:
        for i, t in enumerate(v2[g]["definition"]["clauses"]):
            tag = "restated" if i in RESTATED[g] else "verbatim"
            print(f"  {g} ({i + 1}) {t}  [{tag}; Session 44 clause {MAP[g][i] + 1}: {r4.CLAUSES[g][MAP[g][i]][0]}]")

    # [2] records --------------------------------------------------------------------------------------------------
    print("\n[2] THE RECORDS")
    bad, tally = [], {k: 0 for k in STATUS}
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(v2[key[1]]["definition"]["clauses"]):
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {len(v2[key[1]]['definition']['clauses'])}")
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
    check(not bad, "every unit has one status per v2.0 clause, in the Pass Threshold's order; every cleared, short, "
                   "out-of-reach and moot clause, and every clause estimated as not shown, carries its source")
    print("  clause statuses: " + ", ".join(f"{STATUS[k]} {v}" for k, v in tally.items()))

    # [3] the rule -------------------------------------------------------------------------------------------------
    print("\n[3] THE RULE (D28) AND THE AUDIT'S CODES")
    wrong = [k for k, r in UNITS.items() if rs.verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong, "every verdict follows D28: 1.0 only if every clause is cleared or moot, otherwise 0.5",
          str(wrong))
    check(all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()), "no unit is scored 0.0 in this pass (D28(f))")
    stand = sorted(k for k, r in UNITS.items() if r["verdict"] == 1.0)
    points_b = sum(1.0 - r["verdict"] for r in new.values())
    rise = sorted(k for k in REREAD if UNITS[k]["verdict"] > prior[0][k]["verdict"])
    fall_back = [k for k in REREAD if UNITS[k]["verdict"] < prior[0][k]["verdict"]]
    check(stand == sorted(EXPECT["stand"]) and points_b == EXPECT["points_b"] and rise == EXPECT["rise"]
          and not fall_back,
          f"of the part (b) units {sum(1 for k in new if k in stand)} stand and {sum(1 for k in new if k not in stand)} "
          f"become 0.5 ({rs.f1(points_b)} points); of part (a)'s re-read units none falls further and "
          f"{len(rise)} rises to 1.0 ({', '.join(f'{c} {k}' for c, k in rise)})")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    code = {(c, k, i): reg[(c, k)][MAP[k][i]] for (c, k) in UNITS for i in range(len(MAP[k]))}
    departs = {x for x, ch in code.items() if x[2] not in RESTATED[x[1]]
               and ((ch == "A" and UNITS[x[:2]]["clauses"][x[2]][0] != "C")
                    or (ch == "N" and UNITS[x[:2]]["clauses"][x[2]][0] != "M"))}
    check(departs == set(EXCEPT) == set(),
          "no departure from the audit's A codes: every verbatim clause the audit coded A is carried as cleared")
    re_a = sorted(x for x, ch in code.items() if x[2] in RESTATED[x[1]] and ch == "A")
    carried = sorted(x for x in re_a if UNITS[x[:2]]["clauses"][x[2]][2] == AUDRE)
    estimated = sorted(x for x in re_a if UNITS[x[:2]]["clauses"][x[2]][2] != AUDRE)
    audre_used = sorted((c, k, i) for (c, k), r in UNITS.items() for i, (_, _, src) in enumerate(r["clauses"])
                        if src == AUDRE)
    check(carried == sorted(REREAD_CARRIED) and estimated == sorted(REREAD_ESTIMATED) and audre_used == carried
          and all(UNITS[x[:2]]["clauses"][x[2]][0] == "C" for x in carried),
          f"the audit coded A {len(re_a)} clauses v2.0 restates: {len(carried)} carried after re-reading (reading 3.2), "
          f"{len(estimated)} estimated (" + ", ".join(f"{c} {k} clause {i + 1}" for c, k, i in estimated) + ")")
    silent = {(c, k, i) for (c, k) in new for i in range(len(MAP[k])) if code[(c, k, i)] == "S"}
    notest = sorted((k[0], k[1], i) for k, r in UNITS.items() for i, (st, est, _) in enumerate(r["clauses"])
                    if est.startswith(NOTEST))
    fixed = all(UNITS[(c, k)]["clauses"][i][0] == "U" and any(
        j != i and st in "SUR" and not est.startswith(NOTEST)
        for j, (st, est, _) in enumerate(UNITS[(c, k)]["clauses"])) for c, k, i in notest)
    check(len(silent) == EXPECT["silent"] and set(notest) <= silent and notest == sorted(EXPECT["not_estimated"])
          and fixed,
          f"the audit coded {len(silent)} v2.0 clauses of this group's part (b) units silent; {len(silent) - len(notest)} "
          f"are estimated here, and {len(notest)} left not estimated, in a unit whose verdict another clause fixes")
    for c, k, i in notest:
        print(f"  {c} {k} clause {i + 1}: not estimated in this pass (verdict fixed by another clause)")
    est_status = {}
    for c, k, i in sorted(silent):
        if (c, k, i) not in notest:
            st = UNITS[(c, k)]["clauses"][i][0]
            est_status[st] = est_status.get(st, 0) + 1
    print("  silent clauses estimated here: " + ", ".join(f"{STATUS[s]} {n}" for s, n in sorted(est_status.items())))
    bio = [k for k in new if k[1] == "C4.2" and UNITS[k]["clauses"][1][0] == "U"]
    check(len(bio) == EXPECT["per_criterion"]["C4.2"] and all(code[(c, k, 1)] == "S" for c, k in bio),
          "every C4.2 unit was silent on biodiversity and every one is not shown on it, so clause 2 alone fixes each "
          "C4.2 verdict (reading 3.3)")
    rm = [k for k in new if k[1] == "C4.4" and code[(k[0], k[1], 1)] == "S"]
    check(len(rm) == EXPECT["per_criterion"]["C4.4"],
          "every C4.4 unit was silent on the removal clause, and each is estimated on it (reading 3.5)")

    # [4] reach ----------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = sorted(x for x in r4.REACH if (x[0], x[1]) in UNITS)
    check(not now_r and was_r == sorted(mods[0].EXPECT["reach_revised"]),
          "no clause of this group is out of reach: the audit's only reach codes here, MMT + Job Guarantee's four on "
          "C4.2, were superseded in part (a) (within reach under D31), and the v2.0 restatement changes neither")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b6))")
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
          f"flags added {len(added)} ({', '.join(f'{c} {k}' for c, k in added)}); removed {len(removed)}; no unit of "
          "this group carried a flag")
    merged = {}
    for part in prior + (UNITS,):
        merged.update(part)
    adds, rems = changes(merged)
    moved = sorted({k[0] for k in adds + rems})
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Across the pass so far, "
                 f"{len(moved)} entries' flag registers change ({', '.join(moved)}).")
    print("  " + flag_line)

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here on the published 26-criterion structure; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        vsteps.append(v)
    v6, vn = vsteps[-2], vsteps[-1]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, m6, after = steps[0], steps[-2], steps[-1]
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
    tags = ("published", "(a)", "(b1)", "(b2)", "(b3)", "(b4)", "(b5)", "(b6)", "(b7)")
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
    p6, f6 = rs.dominance(v6, cids)
    pn, fn = rs.dominance(vn, cids)
    check(len(p6) == EXPECT["dominance_b6"] and len(f6) == EXPECT["frontier_b6"],
          f"part (b6)'s result reproduced: {len(p6)} dominance pairs, frontier {len(f6)}")
    gained = sorted(set(pn) - set(p6), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(p6) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    n_all = len(merged)
    st_all = sum(1 for r in merged.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for r in merged.values())
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(p6)} after part (b6) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(f6)} (" + ", ".join(c for c in order if c in fn) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(m6['total'][first[0]])} after part (b6), "
                f"{rs.f1(after['total'][first[0]])} now. Across parts (a) and (b1) to (b7), {n_all} units have been "
                f"re-estimated, part (a)'s three re-read here counted once: {st_all} stand and {n_all - st_all} become "
                f"0.5 ({rs.f1(pts_all)} points).")
    print("  " + dom_line)

    # [7] anchors --------------------------------------------------------------------------------------------------
    print("\n[7] ANCHOR EXAMPLES THE PASS SO FAR MOVES (the published anchors, criteria_s44_snapshot.json)")
    code_of = {v: k for k, v in names.items()}
    part_of = {}
    for tag, p in zip(("(a)", "(b1)", "(b2)", "(b3)", "(b4)", "(b5)", "(b6)", "(b7)"), prior + (UNITS,)):
        part_of.update({k: tag for k in p})
    hits, empty = [], []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                cd = code_of.get(ex["system"])
                if cd and (cd, c["id"]) in merged and merged[(cd, c["id"])]["verdict"] != ex["cited"]:
                    hits.append(f"{c['id']}'s {band} example, {cd} (part {part_of[(cd, c['id'])]}, to "
                                f"{rs.f1(merged[(cd, c['id'])]['verdict'])})")
                    if not any(vn[x][c["id"]] == float(band) for x in vn):
                        empty.append((c["id"], band))
    check(len(hits) == EXPECT["anchors_moved"], f"{len(hits)} anchor examples cite a unit the pass moves")
    check(empty == EXPECT["bands_empty"],
          "bands left with no corpus unit at their value: " + ", ".join(f"{c}'s {b}" for c, b in empty))
    keeps = [c for c in order if vn[c]["C2.5"] == 1.0]
    c44 = next(x for x in crit if x["id"] == "C4.4")["anchors"]["bands"]["1.0"]["examples"]
    check([code_of[x["system"]] for x in c44] == ["PE"] and vn["PE"]["C4.4"] == 1.0,
          "C4.4's 1.0 example, Participatory Economics, stands")
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) +
                   ". When the pass is applied, each band needs an example the corpus then scores at that value; " +
                   ", ".join(f"{c}'s {b}" for c, b in empty) + " bands have none left (part (b4), reading 3.5; "
                   "reading 3.8 here); C2.5's 1.0 band keeps one (" + ", ".join(keeps) + ", flagged; part (b5), "
                   "reading 3.7), and C4.4's 1.0 example, Participatory Economics, stands.")
    print("  " + anchor_line)

    # [8] the record -----------------------------------------------------------------------------------------------
    print(f"\n[8] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    unit_order = [k for k in unit_order if k not in REREAD] + [k for k in unit_order if k in REREAD]
    t = tables(rs, v2, unit_order, names, steps, left)
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
    print("\nRESCORING PART (B), SEVENTH GROUP, COMPUTED." if ok else
          "\nRESCORING PART (B), SEVENTH GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
