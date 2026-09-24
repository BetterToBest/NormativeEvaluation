#!/usr/bin/env python3
"""
rescoring_s42.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), fifth group: C2.5 Exit Rights and
Mobility, its ten part (b) units
==============================================================================================================
Session 42. Parts (a) and (b1) to (b4) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s41.md (rescoring_s37.py to
rescoring_s41.py). This script holds the fifth group: C2.5's ten 1.0s, taken whole because their clauses (no
differential treatment, geographic mobility, voluntary association) need readings applied alike across all three
scope classes and four reach codes. It changes no file and no score: the pass's changes are applied by generator
when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). A clause the audit coded A is
carried as cleared on the unit's own text, except where listed in EXCEPT with its reason (one in this group: the
design's own sources contradict it); the script asserts that every departure from the audit's A codes is listed,
and every listed one occurs. A clause marked "not estimated in this pass" is allowed only where another clause of
the same unit already fixes the verdict. The audit's five out-of-reach codes are asserted unchanged (D31 search,
reading 3.4).

CHECKS: the group against the audit's register (the part (b) units of C2.5); every record complete; the rule; the
audit's codes carried or excepted; every silent clause estimated or validly left; reach; flags against the summary
blocks, cumulatively with parts (a) to (b4); the consequences of the pass so far (totals, ranks, failures, tiers,
dominance, frontier, what remains, the 1.0s C2.5 keeps); the anchor examples the pass so far moves and the bands left
with no corpus unit; and that NEEC_Rescoring_s42.md contains every generated table verbatim.

Usage: python3 rescoring_s42.py   (reads criteria.json, neec_corpus.json, r4_audit_s35.py, rescoring_s37.py to
                                   rescoring_s41.py and the files they read, and NEEC_Rescoring_s42.md beside
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
         ("(b4)", "rescoring_s41", "rescoring_s41.py"))
RECORD = "NEEC_Rescoring_s42.md"
GROUP = ("C2.5",)
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
NOTEST = "not estimated in this pass"
HUB = "research hub at 8e8a6ba"
SIM = "harness.js at cd0ceec"
DOC = {"GEO": "NEEC_Georgism_LVT_scoring_scratch.md", "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
       "DE": "NEEC_DoughnutEconomics_scoring_scratch.md", "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
       "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "IF": "NEEC_IslamicFinance_scoring_scratch.md",
       "OS": "NEEC_Ostrom_Commons_scoring_scratch.md"}
REACH_SRC = "r4_audit_s35.py, REACH; reading 3.4"
JUR = ("; who counts as a non-participant under a mechanism that applies to everyone in its jurisdiction is left to "
       "Report v2.0 (reading 3.1)")

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in Appendix B's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- departures from the audit's A codes, each with its reason (asserted both ways) ------------------------------
EXCEPT = {
    ("CCO", "C2.5", 0): "the design's own sources set the share of Acre Equity a resident can realise on leaving Public "
                        "Trust Housing below face value for five years (reading 3.5)",
}

# ---- C2.5 Exit Rights and Mobility (readings 3.1 to 3.6) --------------------------------------------------------
U("LM", "C2.5", 1.0, [
    ("C", "Maximum exit rights and mobility", AUD),
    ("C", "the design's only non-optional institution, the minimal state, protects everyone in its territory, and "
          "Nozick derives it by requiring the dominant protective agency to extend protection to the independents "
          "whose private enforcement it prohibits; every other arrangement is voluntary, and the framework for utopia "
          "lets people join communities by consent while no community may impose its vision on anyone who stays out, "
          "so non-participants bear no burden that participants do not and forgo only what a community offers its "
          "members (reading 3.1)",
     "Nozick, Anarchy, State, and Utopia (1974), chapters 4-5 and 10 (pp. 311-312, 316)"),
    ("C", "no state restrictions on movement", AUD),
    ("C", "Freedom of contract allows voluntary communes", AUD)],
  flag=([0.5], "C2.5's own 0.5 anchor example (Status Quo Market Capitalism) and a peer of the same archetype "
               "(Stakeholder Capitalism, 0.5) count real economic constraints on exit and mobility against the "
               "criterion; read that way, clauses 1 and 3 are not cleared for an entry whose own corpus text records "
               "survival entirely contingent on market participation, with no public income or health support "
               "(its C2.1 and C2.2), and the unit is 0.5 (protocol 5.3; reading 3.6)"))

U("CCO", "C2.5", 0.5, [
    ("S", "the rationale says opt-out is without penalty, but the design's own sources set the share of a Public Trust "
          "Housing resident's Acre Equity that can be realised on leaving well below face value: 10-20% in the first "
          "six months, 30-50% in months 7-24, 60-75% in months 25-60 and 80-90% after five years, attributed to "
          "settlement lags, exit fees and a minimal secondary market; the housing paper's 20-year illustration gives "
          "$168,000-336,000 of Acre Equity with a cash equivalent of $67,000-134,000 upon exit; and the published model "
          "applies an accessible share rising from 0.15 in the first year to 0.85 at five years; so for the residents "
          "of one of the design's five components exit within three months carries a material loss (reading 3.5)",
     HUB + ": basic-living-economic-index.html, Table 1a; us-real-estate-transformation.html, sections 2.3 and "
     "3.1; " + SIM + ", pthLiquidShare"),
    ("C", "the design's draft legislation pays 1,200 basic units a month to every citizen and legal resident aged 18 "
          "or over, automatically, with no means test or work requirement; keeps Public Trust Housing opt-in with the "
          "private real estate market intact; gives each resident an equal initial allocation of non-housing Acre "
          "Equity; and the housing governance paper guarantees non-participants no mandatory participation, full "
          "property rights and alternative providers; so a person who declines any component keeps the income floor "
          "and forgoes only that component's benefits (reading 3.1)",
     HUB + ": integrated-implementation-roadmap.html, Appendix A, sections 102, 201 and 203; "
     "democratic-governance-pth.html, section 5.3"),
    ("C", "Geographic mobility maintained", AUD),
    ("C", "the design's draft constitutional amendment provides that communities may organise voluntary associations "
          "for collective economic and social benefit, subject to individual rights; its draft Act defines Creator "
          "Collectives as voluntary associations; and zone classifications are self-selected by communities, which "
          "may withdraw (reading 3.3)",
     HUB + ": integrated-digital-governance.html, Appendix B.2, section 3; integrated-implementation-roadmap.html, "
     "Appendix A, section 101(b); wiki/faq.html, Social Zone Harmonization")],
  note="clause 3 is carried as audited: the basic unit is paid nationally under the draft Act and Acre Equity moves "
       "between Public Trust Housing properties without loss (us-real-estate-transformation.html, section 2.3); a move "
       "beyond the housing network is an exit from it, recorded under clause 1. Two leads for Report v2.0 do not "
       "decide the unit: the zone-formation algorithm weights each resident's preference by engagement and tenure "
       "(integrated-digital-governance.html, Appendix A.3), which would bear on clause 2 if engagement meant "
       "participation; and the published model pays the basic unit only to its participating share (partRate 0.78), "
       "while the draft Act pays every citizen and legal resident (section 7)")

U("INT", "C2.5", 0.5, [
    ("C", "can leave the federation without penalty", AUD),
    ("U", "the design makes basic needs accessible below standard contribution thresholds and adjusts for caregiving "
          "and health constraints, but releases goods only against verified credit access and aims to replace the "
          "market economy it grows alongside; no source states what a person who declines to join receives once it "
          "has, and the corpus's own review records that it is unclear how non-participants access essentials, "
          "although its C2.5 section estimates no material penalty for non-participation (reading 3.1)",
     "integralcollective.io, The System: ITC (modules ITC-5 and ITC-7) and COS, accessed 2026-09-23; the "
     "project's FAQ as quoted in Socialist Standard 1452 (August 2025); Integral_NEEC_Review.md, C1.1 and C2.5"),
    ("C", "the design recognises contribution made in one node for access in another at federation scale, within "
          "equivalence bands set by federation governance, and makes basic needs accessible below standard "
          "contribution thresholds wherever a person participates (reading 3.2)",
     "integralcollective.io, The System: ITC (modules ITC-5 and ITC-6), accessed 2026-09-23"),
    ("C", "Nodes remain autonomous", AUD)])

U("GEO", "C2.5", 0.5, [
    ("C", "relocate freely without penalty", AUD),
    ("U", NOTEST + "; the verdict is fixed by clause 4" + JUR, ""),
    ("C", "an individual can relocate freely", AUD),
    ("R", "freedom of association is not governed by a land tax; the audit's code is confirmed, since George's "
          "association in equality names social cooperation as the engine of progress, not a protection of voluntary "
          "associations, and no source located in the Georgist literature pairs such a protection with the tax "
          "(reading 3.4)",
     REACH_SRC + "; George, Progress and Poverty (1879), Book X, chapter 3")])

U("MC", "C2.5", 0.5, [
    ("C", "carries no formal penalty beyond settling", AUD),
    ("C", "the mechanism's credit is issued by members for members, its costs are met from within the community, "
          "trading is by consent, and a default is absorbed by the members; it levies nothing on non-members and has "
          "no authority over them, and it is designed as an adjunct to the national currency, so a non-member keeps "
          "the ordinary market and forgoes only the network (reading 3.1)",
     "Linton's LETSystem design criteria (cost of service, consent, disclosure, equivalence, no interest); "
     + DOC["MC"] + ", C2.5"),
    ("U", "a member's balance and credit line are held in one node; linked networks such as the Community Exchange "
          "System let some members trade across communities, but portability is not part of the mechanism as scored, "
          "and the entry's own text says leaving a node means settling or writing off the balance; no source shows a "
          "member keeping credit and trading standing on relocating (reading 3.2)",
     DOC["MC"] + ", C2.5; Community Exchange System and Community Forge, as described in the LETS literature"),
    ("C", "Participation is voluntary at every level examined", AUD)])

U("DE", "C2.5", 0.5, [
    ("C", "both individual mobility and jurisdictional disengagement are low-cost", AUD),
    ("C", "experiences no different currency, tax base, or property regime", AUD),
    ("C", "both individual mobility and jurisdictional disengagement are low-cost", AUD),
    ("U", "the social foundation includes political voice among its twelve dimensions, a floor the economy should "
          "meet rather than an institution that protects association; the entry operates entirely through a "
          "jurisdiction's existing institutions, so whatever protection its residents have is the host's law, which "
          "is not credited to a comprehensive system whose sources do not specify it (reading 3.3)",
     "Raworth, Doughnut Economics (2017), the social foundation; " + DOC["DE"] + ", C2.5; protocol 3.2 and "
     "D29(c)")])

U("UBS", "C2.5", 0.5, [
    ("C", "can decline to use any or all of", AUD),
    ("U", NOTEST + "; the verdict is fixed by clause 4" + JUR, ""),
    ("C", "relocating to a different jurisdiction carries no penalty specific to UBS", AUD),
    ("R", "freedom of association is not governed by public services; the audit's code is confirmed, since the "
          "legal and democracy sector the UBS literature names supplies legal aid, access to courts and local "
          "involvement in the design of services, which is access to justice, not a protection of association "
          "(reading 3.4)",
     REACH_SRC + "; " + DOC["UBS"] + ", sections on the seven sectors, C2.4 and C4.4 (Coote, Kasliwal and Percy "
     "2019; Coote and Percy 2020)")])

U("SWF", "C2.5", 0.5, [
    ("C", "with no additional penalty, lock-in, or exit cost", AUD),
    ("C", "territorial in the same way any public benefit is", AUD),
    ("C", "ordinary geographic mobility", AUD),
    ("R", "freedom of association is not governed by a sovereign fund; the audit's code is confirmed, since neither "
          "the entry's document nor the fund designs it scores place a protection of association in the mechanism "
          "(reading 3.4)",
     REACH_SRC + "; " + DOC["SWF"] + ", C2.5")])

U("IF", "C2.5", 0.5, [
    ("C", "In its scored form the mechanism is strictly elective", AUD),
    ("U", NOTEST + "; the verdict is fixed by clauses 3 and 4", ""),
    ("R", "geographic mobility is not governed by a financing mechanism; the audit's code is confirmed (reading 3.4)",
     REACH_SRC + "; " + DOC["IF"] + ", C2.5"),
    ("R", "freedom of association is not governed by a financing mechanism; the audit's code is confirmed, since the "
          "partnership contract in the scored set creates a commercial partnership rather than protecting the "
          "freedom to associate, and the entry's document places no such protection in the contract set (reading "
          "3.4)",
     REACH_SRC + "; " + DOC["IF"] + ", C2.5")],
  note="the document's flag, which scored the mandatory jurisdictions' reading at 0.5, is removed: the unit is 0.5 "
       "on reach whatever the deployment")

U("OS", "C2.5", 0.5, [
    ("C", "there is no lock-in, no notice period, and no exit charge", AUD),
    ("U", NOTEST + "; the verdict is fixed by clause 3 (whether exclusion under a residence- or citizenship-based "
          "boundary rule is differential treatment of non-participants is left to Report v2.0, reading 3.1)", ""),
    ("S", "withdrawal rights belong to a bounded membership (design principle 1), and in the paradigm case the "
          "Törbel articles of 1483 bar an outsider who buys land in the village from the communal rights, while the "
          "wintering rule ties summer grazing to hay from one's own land there; a member who relocates arrives in "
          "another commons as such an outsider, so an appropriator whose livelihood the commons supports forfeits it "
          "by moving, as the entry's own flag states of exit (reading 3.2)",
     "Ostrom, Governing the Commons (1990), chapter 3 and Table 3.1; Netting, Balancing on an Alp (1981); "
     + DOC["OS"] + ", C2.5"),
    ("U", "design principle 7 makes minimal recognition of appropriators' right to devise their own institutions a "
          "condition of robust commons, but it describes forbearance by external governmental authorities, a "
          "protection the commons institution depends on rather than supplies; no source located shows commons "
          "institutions protecting their members' freedom to form or join other associations (reading 3.3)",
     "Ostrom, Governing the Commons (1990), Table 3.1, design principle 7; protocol 3.2 and D29(c)")],
  note="the document's flag, whose alternative was 0.5, is removed: the unit is 0.5 on clause 3")

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 10, "per_criterion": {"C2.5": 10}, "stand": [("LM", "C2.5")], "points": 4.5,
          "silent": 14, "not_estimated": [("GEO", "C2.5", 1), ("IF", "C2.5", 1), ("OS", "C2.5", 1),
                                          ("UBS", "C2.5", 1)],
          "reach": [("GEO", "C2.5", 3), ("IF", "C2.5", 2), ("IF", "C2.5", 3), ("SWF", "C2.5", 3),
                    ("UBS", "C2.5", 3)],
          "flags_added": [("LM", "C2.5")], "flags_removed": [("IF", "C2.5"), ("OS", "C2.5")],
          "remaining": 37, "dominance_b4": 18, "frontier_b4": 12, "anchors_moved": 8,
          "bands_empty": [("C1.1", "1.0"), ("C2.1", "1.0"), ("C2.3", "1.0"), ("C2.4", "1.0"), ("C3.1", "1.0")],
          "emptied": {"C2.3": "(b1)", "C2.4": "(b1)", "C3.1": "(b2)", "C1.1": "(b3)", "C2.1": "(b4)"},
          "ones_left": {"C2.5": ["LM"]}}


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
    rows = ["| Entry | Published (rank) | After (b4) (rank) | After this group (rank) | Change here | Failures | Tier | "
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

    print(f"NEEC rescoring pass, part (b), fifth group: C2.5 ({RECORD})")
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
          f"this group holds exactly the part (b) units of C2.5 ({len(grp)}), every one a corpus 1.0 and none "
          f"re-estimated before")
    all_c25 = sorted(c for c in vec if vec[c]["C2.5"] == 1.0)
    check(sorted(c for c, _ in UNITS) == all_c25, f"they are all of C2.5's published 1.0s ({len(all_c25)})")
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
          f"{len(stand)} of {len(UNITS)} stand ({', '.join(c for c, _ in stand)}); {len(UNITS) - len(stand)} become "
          f"0.5 ({rs.f1(points)} points)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    departs = {(k[0], k[1], i) for k, r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"])
               if (reg[k][i] == "A" and st != "C") or (reg[k][i] == "N" and st != "M")}
    check(departs == set(EXCEPT) and all(reg[(c, k)][i] == "A" for c, k, i in EXCEPT),
          f"every departure from the audit's A codes is listed with its reason, and every listed one occurs "
          f"({len(EXCEPT)})")
    for (c, k, i), why in sorted(EXCEPT.items()):
        print(f"  {c} {k} clause {i + 1}: {STATUS[UNITS[(c, k)]['clauses'][i][0]]}; {why}")
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
          f"(no D31 source places voluntary association, or for IF geographic mobility, inside the mechanism)")
    for c, k, i in sorted(now_r):
        print(f"  {c} {k} clause {i + 1}: {r4.REACH[(c, k, i)]}")

    # [5] flags ----------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b4))")
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
          f"({', '.join(c for c, _ in removed)}, each now scored at its own alternative); no other unit of this "
          f"group carried a flag")
    adds, rems = list(added), list(removed)
    for part in prior:
        a, r = changes(part)
        adds += a
        rems += r
    moved = sorted({k[0] for k in adds + rems})
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Across the pass so far, "
                 f"{len(moved)} entries' flag registers change ({', '.join(moved)}).")
    print("  " + flag_line)

    # [6] consequences ---------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (computed here; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        vsteps.append(v)
    v4, vn = vsteps[-2], vsteps[-1]

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, m4, after = steps[0], steps[-2], steps[-1]
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
          "1.0s C2.5 keeps: " + "; ".join(
              f"{g} {len(ones[g])} ({', '.join(ones[g])}; published {sum(1 for c in vec if vec[c][g] == 1.0)})"
              for g in GROUP))
    tags = ("published", "(a)", "(b1)", "(b2)", "(b3)", "(b4)", "(b5)")
    emptied = {}
    for tag, v in zip(tags, vsteps):
        for k in cids:
            if k not in emptied and not any(v[c][k] == 1.0 for c in v):
                emptied[k] = tag
    check(all(any(vsteps[0][c][k] == 1.0 for c in vec) for k in cids) and emptied == EXPECT["emptied"],
          "every criterion had a 1.0 in the published corpus; the pass so far leaves " + str(len(emptied)) +
          " with none: " + ", ".join(f"{k} (part {emptied[k]})" for k in emptied))
    ones_line = ("After this group, the entries scoring 1.0 on C2.5 are: " + "; ".join(
        f"{len(ones[g])}" + (f" ({', '.join(ones[g])})" if ones[g] else "") for g in GROUP) +
        f", against {len(all_c25)} published. Every criterion had a 1.0 in the published corpus; after the pass so far "
        "no entry scores 1.0 on " + str(len(emptied)) + " of them: " +
        ", ".join(f"{k} (emptied in part {emptied[k]})" for k in cids if k in emptied) + ".")
    print("  " + ones_line)
    p4, f4 = rs.dominance(v4, cids)
    pn, fn = rs.dominance(vn, cids)
    check(len(p4) == EXPECT["dominance_b4"] and len(f4) == EXPECT["frontier_b4"],
          f"part (b4)'s result reproduced: {len(p4)} dominance pairs, frontier {len(f4)}")
    gained = sorted(set(pn) - set(p4), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(p4) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    allparts = prior + (UNITS,)
    n_all = sum(len(p) for p in allparts)
    st_all = sum(1 for p in allparts for r in p.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for p in allparts for r in p.values())
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(p4)} after part (b4) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(f4)} (" + ", ".join(c for c in order if c in fn) + f"). First place: "
                f"{', '.join(first)}, {rs.f1(m4['total'][first[0]])} after part (b4), "
                f"{rs.f1(after['total'][first[0]])} now. Across parts (a) and (b1) to (b5), {n_all} units have been "
                f"re-estimated: {st_all} stand and {n_all - st_all} become 0.5 ({rs.f1(pts_all)} points).")
    print("  " + dom_line)

    # [7] anchors --------------------------------------------------------------------------------------------------
    print("\n[7] ANCHOR EXAMPLES THE PASS SO FAR MOVES (build_criteria.py checks examples against published scores)")
    code_of = {v: k for k, v in names.items()}
    allu, part_of = {}, {}
    for tag, p in zip(("(a)", "(b1)", "(b2)", "(b3)", "(b4)", "(b5)"), allparts):
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
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) +
                   ". When the pass is applied, each band needs an example the corpus then scores at that value; " +
                   ", ".join(f"{c}'s {b}" for c, b in empty) + " bands have none left (part (b4), reading 3.5); "
                   "C2.5's 1.0 band keeps one (" + ", ".join(ones["C2.5"]) + ", flagged; reading 3.7).")
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
    print("\nRESCORING PART (B), FIFTH GROUP, COMPUTED." if ok else "\nRESCORING PART (B), FIFTH GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
