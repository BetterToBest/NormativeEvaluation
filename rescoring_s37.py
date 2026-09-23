#!/usr/bin/env python3
"""
rescoring_s37.py -- NEEC rescoring pass (decisions D28, D29, D31), part (a): the 33 stated-shortfall 1.0s
========================================================================================================
Session 37. The R4 audit (NEEC_R4_MultiClause_Audit_s35.md, r4_audit_s35.py) found 167 corpus 1.0s resting on a
multi-clause Pass Threshold; 134 do not show every clause cleared, and 33 of those contain a clause their own
text says falls short (codes P or X, in either case). The audit record's section 7 orders the rescoring pass:
these 33 first, each re-estimated on the clause its text says falls short and on every clause it leaves
unshown, on cited evidence (for designs, their own specification at protocol 4.1's tier). This script holds
every clause estimate of that part, and changes no file and no score: the pass's changes are applied by
generator when it ends (protocol 10.2, 10.3).

EACH CLAUSE gets one status: C cleared (shown on evidence), S short (the evidence shows it below the bar),
U not shown (no estimate on evidence located), R out of reach (a quantity a mechanism does not govern,
D28(c)), M moot (D28(e)). A clause the audit coded A is carried as cleared on the unit's own text ("as
audited") unless the entry's or design's own sources contradict it. THE RULE (D28): a 1.0 stands only if
every clause is C or M; otherwise it becomes 0.5. This part never scores 0.0 (D28(f)); where a whole-
criterion 0.0 condition may hold, the unit is flagged with 0.0 as its alternative (protocol 6.1).

CHECKS: the population against the audit's register; every record complete; the rule; the reach revisions
(D31); the flag registers against the summary blocks in the scoring documents; the consequences for the
corpus (totals, ranks, failures, tiers, dominance, frontier, the bound left for part (b)); and that
NEEC_Rescoring_s37.md contains every generated table verbatim.

Usage: python3 rescoring_s37.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, the eleven
                                   scoring documents and NEEC_Rescoring_s37.md beside itself; writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, AUDIT, RECORD = "criteria.json", "neec_corpus.json", "r4_audit_s35.py", "NEEC_Rescoring_s37.md"
DOCUMENTS = ("NEEC_Step1c_Retrofit_C1_2ab_C1_5.md", "NEEC_Georgism_LVT_scoring_scratch.md",
             "NEEC_MutualCredit_LETS_scoring_scratch.md", "NEEC_DoughnutEconomics_scoring_scratch.md",
             "NEEC_UniversalBasicServices_scoring_scratch.md", "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
             "NEEC_StateCapitalism_China_scoring_scratch.md", "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
             "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
             "NEEC_Ostrom_Commons_scoring_scratch.md")
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
HUB = "research-hub at 8e8a6ba (2026-09-21)"
REP = "Report v1.6, "

UNITS = {}
GENERATED = {}  # the tables of the last run, for assembling the record


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit of part (a). clauses: (status, estimate, source) in Appendix B's order. flag: (alts, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


AUD = "as audited (the unit's own text)"

# ---- the 33 units, in the audit register's order --------------------------------------------------------------
U("SQ", "C5.1", 0.5, [
    ("C", "operated for centuries; its components in continuous national-scale operation far beyond 20 years",
     AUD),
    ("U", "the rationale claims longevity, not a match of outcomes to claimed benefits, and concedes the record "
          "does not validate adequacy for contemporary challenges; the corpus's own scoring of this entry records "
          "outcomes short of the broad-prosperity benefits its defenders claim (C1.1 0.5; C1.2b, C1.4, C4.4 0.0)",
     REP + "SQ C5.1; neec_corpus.json (SQ)")],
  flag=([1.0], "outcomes matched component by component against narrow claimed functions (price stability, "
               "growth) rather than the system's broad claims"))
U("NSD", "C2.1", 0.5, [
    ("U", "no standardized autonomy figure; the rationale says coercion is reduced significantly, and Nordic "
          "unemployment insurance carries availability and activation conditions, which the criterion's "
          "Requirement counts as bureaucratic control", REP + "NSD C2.1; criteria.json C2.1 (requirement)"),
    ("U", "no revealed-preference study of acceptance under a guaranteed alternative located", "")])
U("NSD", "C2.3", 0.5, [
    ("U", "the Measurement line asks for weekly engagement; the figures located are annual (74% Denmark, 68% "
          "Sweden, 63% Finland took part in at least one artistic activity in a year), an upper bound only; the "
          "rationale's 35-45% is unsourced; EU-SILC table ilc_scp07 (2015, 2022) holds the weekly shares",
     "Special Eurobarometer 399 (2013), via NZ Ministry of Social Development, Social Report"),
    ("C", "about 1,380 hours worked a year against 1,780 in the US leave well over 10 hours a week", AUD),
    ("U", "not located in this pass (EU-SILC well-being module: things one does are worthwhile)", "")],
  note="returns to 1.0 only if ilc_scp07 shows at least 50% engaging weekly and the well-being module at least "
       "7.0 of 10")
U("NSD", "C2.4", 0.5, [
    ("C", "latest national turnouts: Sweden 84.2% (2022), Denmark 84.16% (2022), Iceland 80.1% (2021), Norway "
          "77.2% (2021), Finland 68.5% (2023); four of five at or above 70% (the rationale's 65-75% understated "
          "it)", "IDEA Voter Turnout Database; Valmyndigheten, 2022 results; Nordregio (2024)"),
    ("S", "by September 2020, 36 Finnish citizens' initiatives had reached Parliament and two became law "
          "(same-sex marriage; the Maternity Act): about 6%", "Yle News (September 2020)"),
    ("U", "not estimated in this pass; the verdict is fixed by clause 2", "")])
U("NSD", "C3.1", 0.5, [
    ("C", "benefits automatically increase in downturns without legislative delay", AUD),
    ("S", "support rises by widening coverage at fixed replacement rates; no automatic rise in support per "
          "covered person at the threshold's own example (30% decline, 30% increase); the rationale says the "
          "stabilizers scale moderately", REP + "NSD C3.1; criteria.json C3.1 (pass threshold, measurement)"),
    ("U", "not estimated in this pass", "")])
U("NSD", "C4.4", 0.5, [
    ("S", "wealth Gini 0.65-0.75, the entry's own figure, on which its C1.2b (the same wealth-Gini test) is "
          "already scored 0.5", REP + "NSD C1.2b and C4.4; Paper v1.4, 12.3"),
    ("S", "about 6% of the Finnish citizens' initiatives that reached Parliament were adopted (see C2.4)",
     "Yle News (September 2020)"),
    ("U", "not estimated in this pass", ""),
    ("C", "parliamentary removal functions: Sweden's prime minister lost a confidence vote on 21 June 2021",
     "Riksdag confidence vote, 21 June 2021")])
U("CPS", "C3.2", 0.5, [
    ("S", "official prices held by decree while excess demand appeared as queues, rationing and black markets "
          "(the entry's shortage inflation): repressed and hidden inflation, not price stability",
     REP + "CPS C3.2; Kornai, Economics of Shortage (1980); Nuti, Contributions to Political Economy 5 (1986)"),
    ("U", "no stress record separable from the system's end", ""),
    ("S", "no automatic adjustment: the monetary overhang was released as open inflation when prices were "
          "freed at the system's end", "Nuti (1986); " + REP + "CPS C3.5")])
U("CPS", "C3.5", 0.5, [
    ("C", "failures (shortages, queues, poverty) were highly visible", AUD),
    ("U", "not shown", ""),
    ("S", "correction came through eventual collapse and reform, in every Soviet-type economy: a failure "
          "replicated across independent implementations (D29(a))", REP + "CPS C3.5"),
    ("U", "not estimated in this pass", "")])
U("CPS", "C4.5", 0.5, [
    ("S", "surplus appropriated by the state rather than private owners: extraction continued, to another "
          "appropriator, with nothing placing it below 10% of GDP", REP + "CPS C4.5"),
    ("U", "not estimated in this pass", ""),
    ("U", "not estimated in this pass", "")],
  flag=([0.0], "state appropriation read as structural, load-bearing extraction, the 0.0 band's own test"))
U("MS", "C2.1", 0.5, [
    ("S", "the rationale concedes survival-linked compulsion persists (compete or close replaces work or "
          "starve); no autonomy survey located", REP + "MS C2.1"),
    ("U", "no revealed-preference validation located", "")])
U("MS", "C4.4", 0.5, [
    ("S", "wealth Gini 0.40-0.50 for cooperative systems, the Paper's own figure, above 0.35",
     "Paper v1.4, 12.3 (C1.2b current performance)"),
    ("U", "not estimated in this pass", ""),
    ("C", "economic power distributed through democratic ownership", AUD),
    ("U", "not estimated in this pass", "")])
U("LM", "C2.3", 0.5, [
    ("S", "the rationale says the freedom applies only to economically secure minorities", REP + "LM C2.3"),
    ("U", "claimed only for those with capital; not shown for the population", ""),
    ("U", "not estimated in this pass", "")])
U("LM", "C2.4", 0.5, [
    ("S", "economic democracy is entirely absent (the rationale), and the criterion's Requirement counts it "
          "as much as political democracy", REP + "LM C2.4; criteria.json C2.4 (requirement)"),
    ("U", "not estimated in this pass", ""),
    ("U", "not estimated in this pass", "")])
U("LM", "C4.5", 0.5, [
    ("U", "no mechanism limits private extraction", ""),
    ("U", "formal freedom of contract; exit without a subsistence floor is not shown to be genuine", ""),
    ("S", "the rationale concedes the design ignores economic coercion and power asymmetries", REP + "LM C4.5")],
  flag=([0.0], "the design treats voluntary exchange as non-exploitative by definition: the 0.0 condition of "
               "excluding the criterion's concern as illegitimate (protocol 2.1)"))
U("MMT", "C1.3", 0.5, [
    ("U", "the job guarantee would substantially improve housing security: an improvement, not a stability "
          "rate", REP + "MMT C1.3"),
    ("R", "affordability is set by housing policy and land markets; no source located in the job-guarantee "
          "literature that pairs a housing programme with the guarantee in its design (D31)",
     "Session 35 reach reason, confirmed")],
  note="a scope scenario counting social housing in does not change the score: clause 1 stays not shown")
U("MMT", "C4.2", 0.5, [
    ("U", "within reach under D31 (the guarantee's own literature pairs it with environmental work); "
          "theoretically compatible with absolute reductions is not a 35-45% cut by 2030",
     "Tcherneva, Levy WP 517 (2007); Tcherneva, La garantie d'emploi: l'arme sociale du Green New Deal (2021)"),
    ("U", "within reach under D31; no estimate", ""),
    ("U", "within reach under D31; no estimate", ""),
    ("U", "within reach under D31; no estimate", "")],
  note="supersedes Session 35's out-of-reach coding of all four clauses; a scope scenario counting the "
       "environmental work out leaves no mechanism addressing C4.2 (0.0, one failure more)")
U("MMT", "C5.2", 0.5, [
    ("S", "three stages (pilot, regional, national) against at least four; no four-phase plan located in the "
          "blueprint literature, which sets out structure, funding and administration",
     REP + "MMT C5.2; Tcherneva, Levy WP 902 (2018)"),
    ("U", "no deployment plan of 36 months or less located", ""),
    ("U", "not shown", ""), ("U", "not shown", ""), ("U", "not shown", "")])
U("UBI", "C2.1", 0.5, [
    ("U", "65-75% report increased autonomy: straddles the bar, measures an increase rather than genuine "
          "autonomy, and is unsourced", REP + "UBI C2.1"),
    ("U", "no revealed-preference validation cited", "")])
U("UBI", "C4.5", 0.5, [
    ("R", "the economy-wide extraction share is not governed by an income transfer",
     "Session 35 reach reason, confirmed"),
    ("C", "an exit option from exploitative work", AUD),
    ("S", "eliminates most desperate exploitation: reduced, not below 10% of decisions", REP + "UBI C4.5")])
U("UBI", "C5.3", 0.5, [
    ("C", "implementable at municipal, state or national scale", AUD),
    ("C", "Alaska shows coexistence with the market economy", AUD),
    ("U", "a gradual rollout is asserted; no scaling pathway validated through modelling cited", REP + "UBI C5.3"),
    ("U", "not estimated in this pass", "")])
U("FALC", "C3.2", 0.5, [
    ("C", "post-scarcity abundance claimed to remove inflation (a design's projection)", AUD),
    ("U", "not shown", ""),
    ("S", "assumes the problem away through technology: no mechanism of its own, which D26 places in the 0.5 "
          "band", REP + "FALC C3.2; criteria.json C3.2 (D26)")])
U("CCO", "C3.1", 0.5, [
    ("C", "the design's Recession Protocol acts at 0-72 hours",
     HUB + ", integrated-implementation-roadmap.html, Appendix G"),
    ("S", "the design raises Basic Units by a fixed 20% on a trigger of a GDP decline above 2% for two "
          "quarters, later steps discretionary: below the threshold's own example (30% decline, 30% increase); "
          "the Report's 50% is in no published CCO document located",
     HUB + ", integrated-implementation-roadmap.html, Appendix G"),
    ("U", "re-read on the design's own sources: participation is opt-in and the rollout plan targets 60% "
          "opt-in; coverage of 90% of the affected population is not shown",
     "compassionate-meritocracy-plan, index.html (3-Month Plan for the USA)")],
  note="correction for Report v2.0: the design's figure is 20%, not 50%")
U("CCO", "C5.2", 1.0, [
    ("C", "seven phases over seven years", HUB + ", integrated-implementation-roadmap.html"),
    ("C", "a three-month national launch plan", "compassionate-meritocracy-plan, index.html"),
    ("C", "phase timelines, success metrics and a KPI appendix; a sprint timeline",
     HUB + ", integrated-implementation-roadmap.html (Appendix I); compassionate-meritocracy-plan"),
    ("C", "USD 500 billion over five years for PTFs; a Resource Requirements section",
     HUB + ", integrated-implementation-roadmap.html (Appendix A); compassionate-meritocracy-plan"),
    ("C", "a Risk Assessment and Mitigation section; a Risk Mitigation Framework paper (31 August 2025)",
     "compassionate-meritocracy-plan; " + HUB + ", risk-mitigation-framework.html")],
  note="the plans' specification is what C5.2 judges (its anchor note); their feasibility is scored at C5.1 and "
       "C5.4; the documents are the owner's (self-referential disclosure)")
U("INT", "C5.3", 0.5, [
    ("C", "the federated structure starts with a handful of people", AUD),
    ("C", "nodes coexist with traditional markets", AUD),
    ("U", "starting small is supported by design; no modelling of the scaling pathway cited", REP + "INT C5.3"),
    ("U", "not estimated in this pass", "")])
U("GEO", "C3.4", 0.5, [
    ("C", "rates, valuation methods and phase-ins adjusted across jurisdictions", AUD),
    ("S", "multi-year cycles, not updates within six months: Estonia's national revaluations in 2001 and then "
          "2022; the ACT's transition review about every four years; Denmark's 2024 reform phased in to 2028",
     "NEEC_Georgism_LVT_scoring_scratch.md, C3.4"),
    ("C", "changes through ordinary democratic process", AUD),
    ("C", "no collapse caused by an adjustment located", AUD)])
U("DE", "C3.4", 0.5, [
    ("C", "the global model and city portraits revised on new data", AUD),
    ("S", "scheduled cycles longer than six months: the global monitor annually, Amsterdam biennially",
     "NEEC_DoughnutEconomics_scoring_scratch.md, C3.4"),
    ("S", "the framework's own revisions are made by its authors and DEAL, not governed democratically; only "
          "city applications pass through councils", "NEEC_DoughnutEconomics_scoring_scratch.md, C3.4"),
    ("U", "not shown either way", "")])
U("SWF", "C3.4", 1.0, [
    ("C", "the strategic equity share moved from 40% (1998) to 60% (decided June 2007) to 70% (2017): a core "
          "parameter moved by half its value; the expected return in the fiscal rule from 4% to 3% (2017)",
     "Norges Bank, Matsen speech (1 December 2016); Ministry of Finance press release (16 February 2017)"),
    ("C", "the 2017 decisions came on 16 February, eleven weeks after Norges Bank's recommendation of "
          "1 December 2016", "NBIM letter to the Ministry (1 December 2016); Ministry of Finance (16 February 2017)"),
    ("C", "a democratically enacted change", AUD),
    ("C", "the new equity share held through 2008-2009 without collapse", AUD)],
  flag=([0.5], "evidence dated from the market evidence of lower expected returns rather than from the formal "
               "assessment, which makes the expected-return revision slow"))
U("SG", "C1.3", 0.5, [
    ("C", "a documented stability rate far above the threshold for the resident population", AUD),
    ("S", "not maintained for the rental segment, which houses most non-residents: private rents up 29.7% in "
          "2022 after 9.9% in 2021, HDB rents up about 28.5% in 2022, foreigners about 65% of renters; the "
          "configured-economy population rule counts them (protocol 3.2)",
     "URA via Malay Mail (27 January 2023); Vulcan Post (2023), citing URA and PropertyGuru")])
U("SG", "C3.4", 0.5, [
    ("C", "repeated recalibration: divestment, climate targets, a carbon tax", AUD),
    ("S", "some evidence-based proposals slow or refused: unemployment support long resisted until 2025; an "
          "official poverty line refused", "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.4"),
    ("S", "governed democratically but under a dominant-party supermajority",
     "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.4"),
    ("C", "no collapse from recalibration", AUD)])
U("QA", "C5.3", 0.5, [
    ("C", "the distributive core serves citizens, 9-13% of residents", AUD),
    ("C", "runs in parallel with a market economy", AUD),
    ("S", "no validated scaling pathway exists (the entry's own flag)",
     "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C5.3"),
    ("U", "not estimated in this pass", "")])
U("IF", "C3.4", 0.5, [
    ("C", "product sets re-engineered and frameworks revised", AUD),
    ("S", "after the 2012 tightening of bay' al-inah the industry re-engineered within a few years",
     "NEEC_IslamicFinance_scoring_scratch.md, C3.4"),
    ("S", "changes set by Shariah Advisory Councils of appointed scholars and by central banks: governed, not "
          "democratic (the document's quotation drops democratic)",
     "NEEC_IslamicFinance_scoring_scratch.md, C3.4; audit record, 4"),
    ("C", "no destabilisation", AUD)])
U("IF", "C5.1", 0.5, [
    ("C", "every named contract in commercial use at scale since 1983", AUD),
    ("S", "the design promises profit-and-loss sharing; debt-like sale contracts dominate (tawarruq 46% of "
          "Malaysian Islamic financing by 2019), and the document leaves the match to its other criteria",
     "NEEC_IslamicFinance_scoring_scratch.md, C3.4 and C5.1")])
U("OS", "C3.4", 0.5, [
    ("C", "principle 3 is a procedure for changing the rules", AUD),
    ("C", "in-period adjustment faster than six months (the acequia scarcity rule)", AUD),
    ("C", "rule changes governed by those affected", AUD),
    ("U", "the founding literature records outright failures and fragile appropriator-designed institutions; "
          "no analysis located attributing them to, or clearing them of, a rule adjustment",
     "Ostrom, Governing the Commons (1990), ch. 5 (Turkish inshore fisheries, California groundwater basins, "
     "Sri Lankan and Nova Scotian fisheries)")],
  flag=([1.0], "read as for Georgism: no collapse caused by an adjustment located"))

# ---- expected results (every computed verdict below is asserted) ---------------------------------------------
EXPECT = {"units": 33, "stand": [("CCO", "C5.2"), ("SWF", "C3.4")], "points": 15.5,
          "reach_revised": [("MMT", "C4.2", 0), ("MMT", "C4.2", 1), ("MMT", "C4.2", 2), ("MMT", "C4.2", 3)],
          "flags_added": [("SQ", "C5.1"), ("CPS", "C4.5"), ("LM", "C4.5"), ("SWF", "C3.4"), ("OS", "C3.4")],
          "flags_removed": [("SG", "C3.4"), ("QA", "C5.3"), ("IF", "C3.4")],
          "remaining": 101, "dominance_base": 14, "frontier_base": 12}


def read(name):
    path = os.path.join(HERE, name)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: missing input {name}")
    with open(path, encoding="utf-8") as f:
        return f.read()


def tier(failures):
    return "Potentially Adequate" if failures <= 2 else ("Partially Adequate" if failures <= 5
                                                         else "Structurally Inadequate")


def verdict_of(clauses):
    """D28: 1.0 only if every clause is cleared or moot; otherwise 0.5 (never 0.0 in this part)."""
    return 1.0 if all(st in "CM" for st, _, _ in clauses) else 0.5


def ranks(totals):
    order = sorted(totals.values(), reverse=True)
    return {k: 1 + sum(1 for x in order if x > v) for k, v in totals.items()}


def dominance(vecs, cids):
    pairs = []
    for a in vecs:
        for b in vecs:
            if a != b and all(vecs[a][c] >= vecs[b][c] for c in cids) and any(vecs[a][c] > vecs[b][c] for c in cids):
                pairs.append((a, b))
    frontier = [a for a in vecs if not any(p[1] == a for p in pairs)]
    return pairs, frontier


def blocks_by_code():
    out = {}
    for doc in DOCUMENTS:
        for m in re.finditer(r"```json\n(\{.*?\})\n```", read(doc), re.S):
            try:
                b = json.loads(m.group(1))
            except ValueError:
                continue
            if b.get("schema") == "neec-summary-block/1.0":
                out[b["code"]] = b
    return out


def f1(x):
    return f"{x:.1f}"


def fmt_alts(alts):
    return ", ".join(f1(a) for a in alts)


def tables(r4, cdef, order, names, base, after, remaining):
    """Every table the record must contain, as Markdown, keyed by name."""
    t = {}
    rows = ["| Entry | Criterion | Clauses | Verdict | Flag |", "|---|---|---|---|---|"]
    for key in order:
        rec = UNITS[key]
        fl = f"alternative {fmt_alts(rec['flag'][0])}" if rec["flag"] else ""
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
            lines += ["", f"*Flag:* alternative {fmt_alts(rec['flag'][0])}: {rec['flag'][1]}."]
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {code} {crit}"] = "\n".join(lines)
    rb, ra = ranks(base["total"]), ranks(after["total"])
    rows = ["| Entry | Total now (rank) | After part (a) (rank) | Change | Failures | Tier | Left for part (b) | "
            "Bound after part (b) |", "|---|---:|---:|---:|---:|---|---:|---:|"]
    for code in order_codes(names, base):
        left = remaining.get(code, 0)
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(after['total'][code])} ({ra[code]}) | "
                    f"{f1(after['total'][code] - base['total'][code])} | {after['fail'][code]} | "
                    f"{tier(after['fail'][code])} | {left} | {f1(after['total'][code] - 0.5 * left)} |")
    t["consequences"] = "\n".join(rows)
    return t


def order_codes(names, base):
    return sorted(names, key=lambda c: (-base["total"][c], list(names).index(c)))


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    spec = importlib.util.spec_from_file_location("r4_audit_s35", os.path.join(HERE, AUDIT))
    if not os.path.isfile(os.path.join(HERE, AUDIT)):
        sys.exit(f"ERROR: missing input {AUDIT}")
    r4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r4)
    crit = json.loads(read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}

    print(f"NEEC rescoring pass, part (a): the stated-shortfall 1.0s ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {AUDIT}, {len(DOCUMENTS)} scoring documents, {RECORD}\n")

    # [1] population --------------------------------------------------------------------------------------------
    print("[1] THE POPULATION")
    shortfall = [(u[0], u[1]) for u in r4.UNITS if any(ch in "PXpx" for ch in u[2])]
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    check(len(r4.UNITS) == 167 and len(d28) == 134 and len(shortfall) == EXPECT["units"],
          f"the audit's register: 167 units; 134 not shown clause by clause; {len(shortfall)} with a stated shortfall")
    check(sorted(UNITS) == sorted(shortfall) and all(vec[c][k] == 1.0 for c, k in UNITS),
          "part (a) holds exactly the stated-shortfall units, one record each, every one a corpus 1.0")
    check(set(shortfall) <= set(d28), "every stated-shortfall unit is also in D28's population")

    # [2] records -----------------------------------------------------------------------------------------------
    print("\n[2] THE RECORDS")
    bad = []
    tally = {k: 0 for k in STATUS}
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(r4.CLAUSES[key[1]]):
            bad.append(f"{key}: {len(rec['clauses'])} clauses for {len(r4.CLAUSES[key[1]])}")
        for k, (st, est, src) in enumerate(rec["clauses"]):
            tally[st] = tally.get(st, 0) + 1
            if st not in STATUS or not est.strip():
                bad.append(f"{key} clause {k + 1}: status {st!r} or empty estimate")
            if st in "CSR" and not src.strip():
                bad.append(f"{key} clause {k + 1}: {STATUS.get(st, st)} without a source or reason")
            if "|" in est + src:
                bad.append(f"{key} clause {k + 1}: a pipe character would break the table")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per clause, in Appendix B's order; every cleared, short and "
                   "out-of-reach clause carries its source or reason")
    print("  clause statuses: " + ", ".join(f"{STATUS[k]} {v}" for k, v in tally.items()))

    # [3] the rule ---------------------------------------------------------------------------------------------
    print("\n[3] THE RULE (D28)")
    wrong = [k for k, r in UNITS.items() if verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong, "every verdict follows D28: 1.0 only if every clause is cleared or moot, otherwise 0.5",
          str(wrong))
    check(all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()), "no unit is scored 0.0 in this part (D28(f))")
    probe = [("C", "x", "y"), ("R", "x", "y")]
    check(verdict_of(probe) == 0.5 and verdict_of([("C", "x", "y"), ("M", "x", "")]) == 1.0,
          "self-test: an out-of-reach clause holds a unit at 0.5; cleared and moot clauses let it stand")
    stand = sorted(k for k, r in UNITS.items() if r["verdict"] == 1.0)
    points = sum(1.0 - r["verdict"] for r in UNITS.values())
    check(stand == sorted(EXPECT["stand"]) and points == EXPECT["points"],
          f"{len(stand)} of {len(UNITS)} stand ({', '.join(' '.join(k) for k in stand)}); "
          f"{len(UNITS) - len(stand)} become 0.5 ({f1(points)} points)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))

    # [4] reach -------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = {x for x in r4.REACH if (x[0], x[1]) in UNITS}
    revised = sorted(was_r - now_r)
    check(revised == EXPECT["reach_revised"] and not (now_r - was_r),
          "out of reach now: " + ", ".join(f"{c} {k} clause {i + 1}" for c, k, i in sorted(now_r)) +
          "; revised by D31's source: " + ", ".join(f"{c} {k} clause {i + 1}" for c, k, i in revised))

    # [5] flags -------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks in the scoring documents)")
    blocks = blocks_by_code()
    check(sorted(blocks) == sorted(names), f"summary blocks read from {len(DOCUMENTS)} documents, one per entry")
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}
    added = sorted(k for k, r in UNITS.items() if r["flag"] and k not in had)
    removed = sorted(k for k, r in UNITS.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
    kept = sorted(k for k, r in UNITS.items() if k in had and k not in removed)
    check(added == sorted(EXPECT["flags_added"]) and removed == sorted(EXPECT["flags_removed"]) and not kept,
          f"flags added {len(added)} (" + ", ".join(' '.join(k) for k in added) + f"); removed {len(removed)} (" +
          ", ".join(' '.join(k) for k in removed) + "): their alternative is now the score")
    for code in sorted({k[0] for k in added + removed}):
        n0 = len(blocks[code]["flags"])
        n1 = n0 + sum(1 for k in added if k[0] == code) - sum(1 for k in removed if k[0] == code)
        print(f"  {code}: {n0} flags -> {n1} (enumeration and joint readings recomputed when the pass is applied)")

    # [6] consequences ------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    new = {c: dict(v) for c, v in vec.items()}
    for (c, k), r in UNITS.items():
        new[c][k] = r["verdict"]
    base = {"total": {c: sum(vec[c][k] for k in cids) for c in vec}, "fail": {c: sum(vec[c][k] == 0.0 for k in cids)
                                                                           for c in vec}}
    after = {"total": {c: sum(new[c][k] for k in cids) for c in new}, "fail": {c: sum(new[c][k] == 0.0 for k in cids)
                                                                            for c in new}}
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    remaining_units = [k for k in d28 if k not in UNITS]
    remaining = {}
    for c, _ in remaining_units:
        remaining[c] = remaining.get(c, 0) + 1
    check(len(remaining_units) == EXPECT["remaining"],
          f"{len(remaining_units)} D28 units remain for part (b) (textual bound {f1(0.5 * len(remaining_units))} points), "
          f"plus C5.1's second clause on its standing 1.0s")
    bp, bf = dominance(vec, cids)
    ap, af = dominance(new, cids)
    check(len(bp) == EXPECT["dominance_base"] and len(bf) == EXPECT["frontier_base"],
          f"baseline reproduced: {len(bp)} dominance pairs, frontier {len(bf)}")
    order = list(names)
    gained = sorted(set(ap) - set(bp), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(bp) - set(ap), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    dom_line = (f"After part (a) the corpus has {len(ap)} dominance pairs against {len(bp)} (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(af)} entries "
                f"against {len(bf)} (" + ", ".join(c for c in order if c in af) + f"). First place: "
                f"{', '.join(first)}, {f1(base['total'][first[0]])} to {f1(after['total'][first[0]])}.")
    print("  " + dom_line)

    # [7] the record's tables -----------------------------------------------------------------------------------
    print(f"\n[7] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    t = tables(r4, cdef, unit_order, names, base, after, remaining)
    t["dominance"] = dom_line
    GENERATED.clear()
    GENERATED.update(t)
    record = read(RECORD)
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING PART (A) COMPUTED." if ok else "\nRESCORING PART (A): CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
