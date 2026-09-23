#!/usr/bin/env python3
"""
rescoring_s39.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), second group: C5.1's second clause on
its eleven 1.0s outside D28's population, and C3.1's five part (b) units
==============================================================================================================
Session 39. Part (a) (NEEC_Rescoring_s37.md, rescoring_s37.py) fixed the reading of C5.1's second clause and of
C3.1's second clause (its section 3.4); part (b)'s first group (NEEC_Rescoring_s38.md, rescoring_s38.py) did the
five criteria whose readings were fixed. This script holds the second group: the eleven C5.1 1.0s whose second
clause the audit coded A without testing it (audit record, section 7), and C3.1's five part (b) units, 16 in all.
It changes no file and no score: the pass's changes are applied by generator when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). A clause the audit coded A is
carried as cleared on the unit's own text, with two kinds of exception, each listed in EXCEPT with its reason:
C5.1's second clause, which the audit record (section 7) sends to be tested in full on every C5.1 1.0; and a clause
whose entry's or design's own sources contradict the text, or which a reading fixed in part (a) assigns to another
clause. The script asserts that every departure from the audit's A codes is listed, and every listed one occurs.

CHECKS: the group against the audit's register (the eleven C5.1 units and C3.1's part (b) units); every record
complete; the rule; the audit's codes carried or excepted; reach; flags against the summary blocks, cumulatively
with parts (a) and (b1); the consequences of the pass so far (totals, ranks, failures, tiers, dominance, frontier,
what remains); the anchor examples the pass so far moves; and that NEEC_Rescoring_s39.md contains every generated
table verbatim.

Usage: python3 rescoring_s39.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, rescoring_s37.py,
                                   rescoring_s38.py and the files they read, and NEEC_Rescoring_s39.md beside
                                   itself; writes nothing)
Prints file names only. Deterministic.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CORPUS, AUDIT = "criteria.json", "neec_corpus.json", "r4_audit_s35.py"
PART_A, PART_B1, RECORD = "rescoring_s37.py", "rescoring_s38.py", "NEEC_Rescoring_s39.md"
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
NE = "not estimated in this pass; the verdict is fixed by another clause"
HUB = "research-hub at 8e8a6ba (2026-09-21), "
RA, RB1 = "NEEC_Rescoring_s37.md, ", "NEEC_Rescoring_s38.md, "
DOC = {"MC": "NEEC_MutualCredit_LETS_scoring_scratch.md", "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
       "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
       "CN": "NEEC_StateCapitalism_China_scoring_scratch.md", "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
       "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "OS": "NEEC_Ostrom_Commons_scoring_scratch.md"}

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in Appendix B's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- departures from the audit's A codes, each with its reason (asserted both ways) ------------------------------
C51 = "tested in full: the audit coded it A untested (audit record, section 7; part (a), reading 3.4)"
EXCEPT = {
    **{(c, "C5.1", 1): C51 for c in ("NSD", "MS", "UBI", "CCO", "MC", "UBS", "SWF", "CN", "SG", "QA", "OS")},
    ("CCO", "C5.1", 0): "the design's own component list contradicts the text's 70% (reading 3.2)",
    ("UBS", "C5.1", 0): "the document's own sector list and precedents contradict its text (reading 3.2)",
    ("MMT", "C3.1", 1): "part (a)'s reading 3.4 assigns widening enrolment to clause 3, not clause 2 (reading 3.4)",
}

# ---- C5.1 Proven Component Foundation, second clause (reading: part (a) 3.4; this part 3.1, 3.2) ------------------
U("NSD", "C5.1", 0.5, [
    ("C", "decades of operation in Norway, Sweden, Denmark and Finland at national scale (populations of 5-10 "
          "million)", AUD),
    ("U", "the configuration's headline claims (near-universal material security; comprehensive security and "
          "dignity) are recorded short by the corpus's own amended scoring: housing cost overburden in 2024 at 14.6% "
          "in Denmark and 10.6% in Sweden, among the EU's highest (part (b), NSD C1.3), and about 6% of Finland's "
          "citizens' initiatives adopted (part (a), NSD C2.4); the rationale asserts validation without estimating "
          "a match (reading 3.1)",
     REP + "NSD C1.1, C5.1 and Key Strengths; " + RB1 + "NSD C1.3; " + RA + "NSD C2.4")],
  flag=([1.0], "outcomes matched against the configuration's signature claims, low poverty and universal services, "
               "with the housing and initiative shortfalls read as outcomes on NEEC's thresholds rather than on the "
               "benefits the model claims"))
U("MS", "C5.1", 0.5, [
    ("C", "Mondragon: 70+ years at a scale far above 10,000 participants", AUD),
    ("S", "the rationale claims 80,000+ worker-owners; in 2019 Mondragon's cooperatives employed over 81,000, of whom "
          "members were 32-45% depending on sector, with 18% of employment in subsidiaries abroad; the survival "
          "record is documented as 3 closures among the 103 cooperatives founded in 1956-1986, and the founding "
          "cooperative, Fagor Electrodomesticos, failed in 2013",
     "Journal of Labor and Society 26(3) (2023), The Mondragon Worker Cooperatives' Employment Record 1983-2019; "
     "Participedia, Mondragon case; Fortune (27 November 2013)")],
  note="correction for Report v2.0: about 81,000 workers, 32-45% of them members, not 80,000+ worker-owners; the "
       "'97% over 5 years vs 44%' comparison was not located, and the documented figure is 3 closures in 103")
U("UBI", "C5.1", 1.0, [
    ("C", "Alaska Permanent Fund dividend: 40+ years, universal", AUD),
    ("C", "the rationale claims cash transfers effective with positive outcomes, and the Report claims a 20% poverty "
          "reduction from Alaska's dividend (UBI C1.1): dividends cut Alaska's poverty rate by an estimated 2.5-4 "
          "points a year from 1990, lifting about 25,000 residents out of poverty in 2015, about a third, and from "
          "11% to 9% across 2011-2015; the dividend has not reduced employment",
     "Berman and Reamey, Permanent Fund Dividends and Poverty in Alaska, ISER (2016); Berman, World Development "
     "(2018), via Anchorage Daily News; Jones and Marinescu, American Economic Journal: Economic Policy 14(2) "
     "(2022)")],
  flag=([0.5], "the documented outcomes are of a dividend of about $1,000-2,000 a year; no component precedent "
               "operates at the living-wage level at which the entry claims its benefits"))
U("CCO", "C5.1", 0.5, [
    ("U", "the design's own site lists five components (CCO, PTF, PTH, SZH, CIP); the precedents the rationale cites "
          "cover three (CCO: WIR and Alaska's dividend; PTF and PTH: community land trusts); CIP's precedents, "
          "Consul (Madrid, 2015) and Decidim (Barcelona, 2016), have run for under twenty years, and none is cited "
          "for SZH: at most three of five (60%) are shown (reading 3.2)",
     HUB + "index.html; " + REP + "CCO C5.1"),
    ("C", "the one benefit the rationale claims for a cited component is documented: at the end of 2010, 0.46% of "
          "community land trust mortgages were in foreclosure against 4.63% in the conventional market; Alaska's "
          "dividend's documented poverty reduction is recorded under UBI C5.1 above",
     "Thaden, Stable Home Ownership in a Turbulent Economy, Lincoln Institute of Land Policy (2011)")],
  note="the digital-democracy precedents count at clause 1, where they fall short of twenty years, not at clause 2; "
       "the unit reopens if a scoring document cites twenty-year precedents for four of the five components")
U("MC", "C5.1", 0.5, [
    ("C", "WIR Bank has operated continuously since 1934", AUD),
    ("U", "the components the rationale counts have mixed documented outcomes, as the entry's own document records: "
          "WIR's credit moves countercyclically (C3.1), but UK LETS declined from its mid-1990s peak once cheap "
          "credit returned, its schemes drew participants already socially connected (C1.1), and Argentina's "
          "barter networks collapsed as they outgrew their governance (C3.2, C3.5); WIR's 2013 turnover was 1.43 "
          "billion francs, and Bank WIR reports demand for the currency falling again in 2024 (reading 3.1)",
     DOC["MC"] + ", C1.1, C3.1 and C5.4; Monneta, WIR Bank (2013 figures); finews.ch (20 February 2025)")],
  flag=([1.0], "WIR's documented record, nine decades of operation and countercyclical credit, taken as the proof of "
               "the mechanism's core component, with the LETS and barter-network outcomes read as weaker "
               "implementations"),
  note="polish for Report v2.0: 'turnover in the billions of Swiss francs' rests on 2013's 1.43 billion; state the "
       "year")
U("UBS", "C5.1", 0.5, [
    ("U", "the document defines seven sectors (healthcare, education, democracy and legal services, shelter, food, "
          "transport, information); its cited precedents of 20 years or more cover three (healthcare, education, "
          "shelter), its childcare precedent lies outside the seven, and it calls its transit precedents more "
          "recent and more mixed: three of seven (43%) are shown (reading 3.2)",
     DOC["UBS"] + ", overview and C5.1"),
    ("U", "the rationale states that each precedent has documented outcomes without estimating a match to the "
          "benefits claimed, and the document itself records mixed outcomes: Quebec childcare's publicised "
          "child-development findings (the Baker, Gruber and Milligan research) and Kansas City's 2026 reversal of "
          "zero-fare transit (reading 3.1)", DOC["UBS"] + ", C3.5, C4.3 and sources")],
  note="the unit's published flag (alternative 0.5) resolves to its alternative")
U("SWF", "C5.1", 0.5, [
    ("C", "Norway's fund since 1990 and Alaska's since 1976, both far above the scale bar", AUD),
    ("U", "outcomes are mixed across the three implementations the rationale counts: Norway's fund matches its "
          "claims; Alaska's principal is preserved but its 2025 dividend was the smallest in real terms against a "
          "statutory formula above $3,800 (the entry's own C5.4); Timor-Leste has withdrawn above its sustainable "
          "income almost every year since 2008-09, and the IMF warns the fund could be exhausted by the late 2030s "
          "(reading 3.1)",
     DOC["SWF"] + ", C5.1 and C5.4; East Asia Forum (27 January 2025); World Bank, Macro Poverty Outlook: "
     "Timor-Leste (2025); Lowy Institute, The Interpreter (24 March 2026)")],
  flag=([1.0], "Timor-Leste weighed as a single implementation's shortfall (D29(a)), with Norway's and Alaska's "
               "funds preserved as the mechanism claims"))
U("CN", "C5.1", 0.5, [
    ("C", "operated continuously since 1978 for more than 1.4 billion people", AUD),
    ("U", "the rationale certifies track record, not adequacy (Status Quo's reasoning, which part (a) found does not "
          "show this clause), and cites C1.1 for its documented outcomes, which the entry's own document scores "
          "0.5: a reduction of about 70-80% at the middle-income line the protocol prescribes, though over 99% at "
          "the extreme and national lines (reading 3.1)", DOC["CN"] + ", C1.1 and C5.1; " + RA + "SQ C5.1")],
  flag=([1.0], "outcomes matched against the narrower benefit the configuration's own sources claim, eliminating "
               "extreme and national-line poverty, which the World Bank and State Council study documents"))
U("SG", "C5.1", 0.5, [
    ("C", "operated since independence in 1965 at national scale", AUD),
    ("U", "the rationale certifies track record, not adequacy (Status Quo's reasoning), and cites Domains 1 and 3 "
          "for its documented outcomes, which the corpus's own scoring records short: C1.1 0.5, housing "
          "affordability not maintained for the rental segment (part (a), SG C1.3), and evidence-based updates "
          "slow or refused (part (a), SG C3.4) (reading 3.1)",
     DOC["SG"] + ", C1.1 and C5.1; " + RA + "SG C1.3 and C3.4")],
  flag=([1.0], "outcomes matched against the narrow functions its sources claim for residents, home ownership and "
               "compulsory saving"))
U("QA", "C5.1", 0.5, [
    ("C", "components with long records at national scale", AUD),
    ("U", "the rationale claims operation with documented outcomes and follows China and Singapore without "
          "estimating a match; the corpus's own scoring of the configuration, over its whole resident population "
          "(protocol 3.2), records outcomes short of broad welfare: C1.1 0.5 and ten structural failures, among "
          "them C4.5 (reading 3.1)", DOC["QA"] + ", C1.1, C4.5 and C5.1")],
  flag=([1.0], "outcomes matched against the narrow benefit claimed, welfare provision to the configuration's "
               "citizens, which the entry's document records"))
U("OS", "C5.1", 1.0, [
    ("C", "Valencia's tribunal for about a thousand years; Nepal's programme with about 2.9 million households", AUD),
    ("C", "the benefit claimed is that communities governed by these institutions sustain their resources: the "
          "three multi-case datasets the unit cites document it, and Cox, Arnold and Villamayor Tomas's review of 91 "
          "studies found the design principles well supported empirically; the survivorship caveat is scored where "
          "it changes the answer (C3.3, C5.2, C5.4), as the unit says",
     AUD + "; Cox, Arnold and Villamayor Tomas, Ecology and Society 15(4) (2010)")])

# ---- C3.1 Crisis Response Capacity (readings: part (a) 3.4, clause 2; this part 3.3, 3.4) ---------------------------
U("MMT", "C3.1", 0.5, [
    ("C", "no legislative delay: enrolment rises automatically in a recession", AUD),
    ("S", "the guarantee pays a fixed wage (the rationale's $15 an hour), so a downturn widens enrolment, which is "
          "clause 3's subject, and leaves support per covered person unchanged: 0% at the threshold's 30% example; "
          "the one national precedent, Argentina's Jefes de Hogar, paid a fixed 150 pesos per beneficiary (readings "
          "3.3, 3.4)", REP + "MMT C1.1 and C3.1; Decreto 565/2002"),
    ("U", NE, "")])
U("UBI", "C3.1", 0.5, [
    ("C", "no application process, no verification, no delay", AUD),
    ("S", "the benefit continues at its level regardless of employment: support per covered person does not rise "
          "with crisis severity, 0% at the threshold's 30% example; Alaska's dividend is set on an annual cycle, not "
          "by crisis severity (part (b), UBI C3.4) (reading 3.3)", REP + "UBI C3.1; " + RB1 + "UBI C3.4"),
    ("C", "immediate crisis cushion for the entire population", AUD)])
U("DG", "C3.1", 0.5, [
    ("C", "commons and mutual aid networks provide automatic crisis support", AUD),
    ("U", "no rule tying the support that commons and mutual-aid networks give to crisis severity is specified or "
          "modelled in the design's sources (reading 3.3)", REP + "DG C3.1"),
    ("U", NE, "")])
U("PE", "C3.1", 0.5, [
    ("C", "democratic councils can rapidly shift priorities during crises", AUD),
    ("U", "support is reallocated by council deliberation; no automatic rule tying support per person to crisis "
          "severity is specified, and no implementation or model estimates one (reading 3.3)", REP + "PE C3.1"),
    ("U", NE, "")])
U("INT", "C3.1", 0.5, [
    ("C", "response within 72 hours for clearly defined crises is plausible given the architecture", AUD),
    ("U", "the Feedback and Review System detects anomalies and suggests corrections; no rule scaling support with "
          "crisis severity is specified or estimated (reading 3.3)", REP + "INT C3.1"),
    ("C", "with universal coverage", AUD)])

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 16, "c51": 11, "c31": 5, "stand": [("UBI", "C5.1"), ("OS", "C5.1")], "points": 7.0,
          "flags_added": [("NSD", "C5.1"), ("UBI", "C5.1"), ("MC", "C5.1"), ("SWF", "C5.1"), ("CN", "C5.1"),
                          ("SG", "C5.1"), ("QA", "C5.1")],
          "flags_removed": [("UBS", "C5.1")], "remaining": 67, "dominance_b1": 14, "frontier_b1": 13,
          "anchors_moved": 5}


def load(name, path):
    if not os.path.isfile(os.path.join(HERE, path)):
        sys.exit(f"ERROR: missing input {path}")
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tables(rs, r4, cdef, order, names, base, ma, mb, after, left):
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
    rb, rn = rs.ranks(base["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After (a) | After (b1) | After this group (rank) | Change here | Failures | "
            "Tier | D28 units left | Floor if all fall |",
            "|---|---:|---:|---:|---:|---:|---:|---|---:|---:|"]
    for code in rs.order_codes(names, base):
        lf = left.get(code, 0)
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(ma['total'][code])} | "
                    f"{f1(mb['total'][code])} | {f1(after['total'][code])} ({rn[code]}) | "
                    f"{f1(after['total'][code] - mb['total'][code])} | {after['fail'][code]} | "
                    f"{rs.tier(after['fail'][code])} | {lf} | {f1(after['total'][code] - 0.5 * lf)} |")
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
    rs = load("rescoring_s37", PART_A)
    rb = load("rescoring_s38", PART_B1)
    crit = json.loads(rs.read(CRITERIA))["criteria"]
    cids = [c["id"] for c in crit]
    cdef = {c["id"]: c for c in crit}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}

    print(f"NEEC rescoring pass, part (b), second group: C5.1 clause 2 and C3.1 ({RECORD})")
    print(f"inputs: {CRITERIA}, {CORPUS}, {AUDIT}, {PART_A}, {PART_B1}, {RECORD}\n")

    # [1] population -----------------------------------------------------------------------------------------------
    print("[1] THE POPULATION")
    d28 = [(u[0], u[1]) for u in r4.UNITS if not all(ch in "AN" for ch in u[2])]
    done = set(rs.UNITS) | set(rb.UNITS)
    partb = [k for k in d28 if k not in rs.UNITS]
    c51 = [(u[0], u[1]) for u in r4.UNITS if u[1] == "C5.1" and (u[0], u[1]) not in rs.UNITS]
    c31 = [k for k in partb if k[1] == "C3.1" and k not in rb.UNITS]
    check(len(d28) == 134 and len(partb) == 101 and not set(rb.UNITS) - set(partb),
          "D28's population 134; part (b) 101; part (b1)'s 29 inside it")
    check(sorted(UNITS) == sorted(c51 + c31) and len(c51) == EXPECT["c51"] and len(c31) == EXPECT["c31"]
          and all(vec[c][k] == 1.0 for c, k in UNITS) and not set(UNITS) & done,
          f"this group holds exactly the {len(c51)} C5.1 1.0s outside D28's population and C3.1's {len(c31)} part (b) "
          f"units, every one a corpus 1.0 and none re-estimated before")
    print("  C5.1: " + ", ".join(c for c, _ in c51) + "; C3.1: " + ", ".join(c for c, _ in c31))

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
            if "|" in est + src + (rec["flag"][1] if rec["flag"] else "") + rec["note"]:
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
    departs = {(k[0], k[1], i) for k, r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"])
               if (reg[k][i] == "A" and st != "C") or (reg[k][i] == "N" and st != "M")}
    listed_a = {x for x in EXCEPT if reg[(x[0], x[1])][x[2]] == "A"}
    retested_ok = all(UNITS[(c, k)]["clauses"][i][0] in STATUS for c, k, i in EXCEPT)
    check(departs <= set(EXCEPT) and listed_a == set(EXCEPT) and retested_ok,
          f"every departure from the audit's A codes is listed with its reason ({len(departs)} departures among "
          f"{len(EXCEPT)} listed clauses: {len(EXCEPT) - 3} C5.1 second clauses tested in full, 2 own-source "
          f"exceptions, 1 reading supersession); every other A clause is carried as cleared")
    for (c, k, i), why in sorted(EXCEPT.items()):
        if k != "C5.1" or i != 1:
            print(f"  {c} {k} clause {i + 1}: {STATUS[UNITS[(c, k)]['clauses'][i][0]]} ({why})")

    # [4] reach ----------------------------------------------------------------------------------------------------
    print("\n[4] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = {(c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R"}
    was_r = {x for x in r4.REACH if (x[0], x[1]) in UNITS}
    check(now_r == was_r == set(), "no clause of this group is out of reach, and none was coded so")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) and (b1))")
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
          f"flags added {len(added)} (" + ", ".join(" ".join(k) for k in added) + f"); removed {len(removed)} (" +
          ", ".join(" ".join(k) for k in removed) + ", resolved to its alternative)")
    adds, rems = list(added), list(removed)
    for part in (rs.UNITS, rb.UNITS):
        a, r = changes(part)
        adds += a
        rems += r
    moved = sorted({k[0] for k in adds + rems})
    for code in moved:
        n0 = len(blocks[code]["flags"])
        n1 = n0 + sum(1 for k in adds if k[0] == code) - sum(1 for k in rems if k[0] == code)
        print(f"  {code}: {n0} flags -> {n1} after parts (a), (b1) and (b2)")
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Across the pass so far, "
                 f"{len(moved)} entries' flag registers change ({', '.join(moved)}).")
    print("  " + flag_line)

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    va = {c: dict(v) for c, v in vec.items()}
    for (c, k), r in rs.UNITS.items():
        va[c][k] = r["verdict"]
    vb = {c: dict(v) for c, v in va.items()}
    for (c, k), r in rb.UNITS.items():
        vb[c][k] = r["verdict"]
    vn = {c: dict(v) for c, v in vb.items()}
    for (c, k), r in UNITS.items():
        vn[c][k] = r["verdict"]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    base, ma, mb, after = summ(vec), summ(va), summ(vb), summ(vn)
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    left_units = [k for k in partb if k not in rb.UNITS and k not in UNITS]
    left, per = {}, {}
    for c, k in left_units:
        left[c] = left.get(c, 0) + 1
        per[k] = per.get(k, 0) + 1
    check(len(left_units) == EXPECT["remaining"],
          f"{len(left_units)} D28 units remain for part (b); C5.1's second clause is now tested on all thirteen 1.0s")
    rem_line = (f"Left for part (b): {len(left_units)} D28 units (" +
                ", ".join(f"{k} {per[k]}" for k in cids if k in per) + ").")
    print("  " + rem_line)
    pb, fb = rs.dominance(vb, cids)
    pn, fn = rs.dominance(vn, cids)
    check(len(pb) == EXPECT["dominance_b1"] and len(fb) == EXPECT["frontier_b1"],
          f"part (b1)'s result reproduced: {len(pb)} dominance pairs, frontier {len(fb)}")
    order = list(names)
    gained = sorted(set(pn) - set(pb), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(pb) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    n_all = len(rs.UNITS) + len(rb.UNITS) + len(UNITS)
    st_all = sum(1 for p in (rs.UNITS, rb.UNITS, UNITS) for r in p.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for p in (rs.UNITS, rb.UNITS, UNITS) for r in p.values())
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(pb)} after part (b1) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(fb)} (" + ", ".join(c for c in order if c in fn) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(mb['total'][first[0]])} after part (b1), "
                f"{rs.f1(after['total'][first[0]])} now. Across parts (a), (b1) and (b2), {n_all} units have been "
                f"re-estimated: {st_all} stand and {n_all - st_all} become 0.5 ({rs.f1(pts_all)} points).")
    print("  " + dom_line)

    # [7] anchors --------------------------------------------------------------------------------------------------
    print("\n[7] ANCHOR EXAMPLES THE PASS SO FAR MOVES (build_criteria.py checks examples against published scores)")
    code_of = {v: k for k, v in names.items()}
    allu = {}
    for p in (rs.UNITS, rb.UNITS, UNITS):
        allu.update(p)
    hits = []
    for c in crit:
        for band, spec in c["anchors"]["bands"].items():
            for ex in spec.get("examples", []):
                code = code_of.get(ex["system"])
                if code and (code, c["id"]) in allu and allu[(code, c["id"])]["verdict"] != ex["cited"]:
                    part = ("(a)" if (code, c["id"]) in rs.UNITS else "(b1)" if (code, c["id"]) in rb.UNITS
                            else "(b2)")
                    hits.append(f"{c['id']}'s {band} example, {code} (part {part}, to "
                                f"{rs.f1(allu[(code, c['id'])]['verdict'])})")
    check(len(hits) == EXPECT["anchors_moved"], f"{len(hits)} anchor examples cite a unit the pass moves")
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) +
                   ". When the pass is applied, each band needs an example the corpus then scores at that value.")
    print("  " + anchor_line)

    # [8] the record -----------------------------------------------------------------------------------------------
    print(f"\n[8] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    t = tables(rs, r4, cdef, unit_order, names, base, ma, mb, after, left)
    t["dominance"], t["remaining"], t["flags"], t["anchors"] = dom_line, rem_line, flag_line, anchor_line
    GENERATED.clear()
    GENERATED.update(t)
    record = rs.read(RECORD) if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in record]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING PART (B), SECOND GROUP, COMPUTED." if ok else "\nRESCORING PART (B), SECOND GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
