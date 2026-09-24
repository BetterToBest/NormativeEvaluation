#!/usr/bin/env python3
"""
rescoring_s48.py -- NEEC rescoring pass (decisions D28, D29, D31): C4.4 Power Distribution re-read on decision 48.3's
measure, and the score ledger
====================================================================================================================
Session 48. Parts (a) to (b7) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s47.md (rescoring_s37.py to
rescoring_s47.py). Decision 48.3 (NEEC_Criteria_v2_s45.md) defines C4.4 clause 1, "Democratic accountability for
>=80% of major decisions", as the share of employment in organizations whose investment, production and employment
decisions answer to those they affect, and moves C4.4 from class D to class M. Part (b7) scored all six of C4.4's
units in the pass on the undefined clause; this script re-reads each on the defined measure, and its records supersede
part (b7)'s. It also computes the score ledger: every entry's published total on the 26 criteria, the change each part
of the pass has made to it, and where it stands now, with CCO-PTF-CIP-SZH's criterion by criterion. It changes no file
and no score: the pass's changes are applied by generator when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). The clauses are v2.0's
(criteria.json). A clause the audit coded A is re-read against decision 48.3's measure, as part (b7)'s reading 3.2
re-reads A codes on restated clauses: carried where the audited phrase claims the defined condition, with the
design's own sources, and estimated otherwise.

CHECKS: C4.4 against decision 48.3 (class M now, class D in criteria_s47_snapshot.json, clauses unchanged, the measure
defined); the group is exactly part (b7)'s C4.4 units; every record complete; the rule; Nordic Social Democracy's
clause 1 bound computed from its published inputs; flags cumulatively with parts (a) to (b7); the consequences on the
published 26-criterion structure (totals, ranks, failures, tiers, dominance, frontier, the criteria left with no 1.0,
C4.4's anchor); the ledger (each entry's changes sum to its move; the published totals equal neec_scores.csv's; Report
v1.6 states CCO-PTF-CIP-SZH's); and that NEEC_Rescoring_s48.md contains every generated table verbatim.

Usage: python3 rescoring_s48.py   (reads criteria.json (v2.0 with 48.3), criteria_s47_snapshot.json,
                                   criteria_s44_snapshot.json (the published structure and anchors), neec_corpus.json,
                                   neec_scores.csv, NEEC_Report_v1_6.md, r4_audit_s35.py, rescoring_s37.py to
                                   rescoring_s47.py and the files they read, and NEEC_Rescoring_s48.md beside itself;
                                   writes nothing)
       python3 rescoring_s48.py --tables   (prints the generated tables as JSON, for assembling the record)
Prints file names only. Deterministic.
"""
import csv
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CRITERIA, CRIT47, CRIT44 = "criteria.json", "criteria_s47_snapshot.json", "criteria_s44_snapshot.json"
CORPUS, CSV, REPORT, AUDIT = "neec_corpus.json", "neec_scores.csv", "NEEC_Report_v1_6.md", "r4_audit_s35.py"
PRIOR = (("(a)", "rescoring_s37", "rescoring_s37.py", 37), ("(b1)", "rescoring_s38", "rescoring_s38.py", 38),
         ("(b2)", "rescoring_s39", "rescoring_s39.py", 39), ("(b3)", "rescoring_s40", "rescoring_s40.py", 40),
         ("(b4)", "rescoring_s41", "rescoring_s41.py", 41), ("(b5)", "rescoring_s42", "rescoring_s42.py", 42),
         ("(b6)", "rescoring_s43", "rescoring_s43.py", 43), ("(b7)", "rescoring_s47", "rescoring_s47.py", 47))
THIS = ("48.3", 48)
RECORD = "NEEC_Rescoring_s48.md"
CRIT = "C4.4"
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
S47 = "NEEC_Rescoring_s47.md, "
AUD48 = "as audited, re-read against decision 48.3's measure (the unit's own text)"
HUB = "research hub at 8e8a6ba"
INTWP = "Integral white paper v0.1 (INTEGRAL-Paper-V0.1.pdf, md5 a6defc9a, accessed 2026-09-24)"

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in v2.0's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- Nordic Social Democracy, clause 1: the most generous count of employment in accountable organizations -------
# country: general government employment, % of total employment, 2022 (OECD, Government at a Glance 2025,
# DF_GOV_EMPPS_REP_2025, EMPG, PT_EMP); employees of state-owned enterprises, % of non-agricultural employees, end-2015
# (OECD, The Size and Sectoral Distribution of State-Owned Enterprises, 2017, Figure 10: Norway 9.6, Finland 3.5;
# Denmark and Sweden are not among the nine it names, so at most its tenth value, 2.9); self-employed and employed
# persons, thousands, ages 15-74, 2022 (Eurostat, lfsa_egaps); paid employment in cooperatives, mutuals, associations
# and foundations, % of paid employment, 2014-15 (CIRIEC for the EESC, Recent Evolutions of the Social Economy in the
# European Union, 2017, Table 7.2; Norway is not covered); V-Dem Regimes of the World, 2022 (Our World in Data,
# political-regime: 3, liberal democracy).
NORDIC = {"Denmark": (27.40, 2.9, 238.2, 2971.8, 5.9, 3), "Finland": (24.88, 3.5, 327.6, 2619.2, 7.7, 3),
          "Norway": (30.08, 9.6, 124.9, 2846.2, None, 3), "Sweden": (28.16, 2.9, 495.8, 5198.6, 4.2, 3)}
SE_MAX = ("Luxembourg", 9.9)  # the highest share in the EU-28 (CIRIEC/EESC 2017, Table 7.2)
NORDIC_SRC = ("OECD, Government at a Glance 2025 (general government employment, % of total employment, 2022); OECD, "
              "The Size and Sectoral Distribution of State-Owned Enterprises (2017), Figure 10; Eurostat lfsa_egaps "
              "(2022); CIRIEC for the EESC, Recent Evolutions of the Social Economy in the European Union (2017), "
              "Table 7.2; V-Dem Regimes of the World (Our World in Data, political-regime, 2022); worker-participation.eu, "
              "Denmark, Finland, Norway and Sweden (board-level representation)")


def bound(v):
    gg, soe, self_, emp, se, _ = v
    return gg + soe + 100 * self_ / emp + (se or 0.0)


# ---- the six C4.4 units, re-read on decision 48.3 (part (b7)'s records superseded) --------------------------------
U("DG", "C4.4", 0.5, [
    ("U", "on decision 48.3's measure as on part (b7)'s reading: the rationale names decentralisation, wealth caps, "
          "cooperative ownership and democratic governance, and degrowth research holds the forms of democracy "
          "compatible with degrowth to need additional study; no source states or projects the share of employment "
          "degrowth would place in organizations whose decisions answer to those they affect",
     REP + "DG C4.4; Kallis, Kostakis, Lange, Muraca, Paulson and Schmelzer, Research on Degrowth, Annual Review of "
     "Environment and Resources 43 (2018) 291-316; " + S47 + "DG C4.4, clause 1"),
    ("U", "as part (b7) recorded: no mechanism of the entry's own for removing or replacing those who hold "
          "decision-making authority is specified or located", S47 + "DG C4.4, clause 2")])

U("PE", "C4.4", 1.0, [
    ("C", "the audited phrase, comprehensive economic democracy, claims the defined condition: the model has no "
          "owners of capital and no managerial hierarchy, places all production in workers' councils that decide by "
          "their members' votes and all consumption in consumers' councils, and federations of councils they elect "
          "decide wider matters, so the investment, production and employment decisions of every workplace are taken "
          "by those who work there or by those they elect (all of the design's employment)",
     AUD48 + "; " + REP + "PE C4.4; participatoryeconomy.org, The Model: Overview (The Participatory Economy "
     "Project), accessed 2026-09-24"),
    ("C", "as part (b7) recorded: workers' and consumers' councils elect recallable and rotated representatives to "
          "their federations", S47 + "PE C4.4, clause 2")])

U("CCO", "C4.4", 0.5, [
    ("U", "the audited phrase, CIP provides direct democratic power, does not claim the defined condition, so the "
          "clause is estimated: CIP administers the currency and manages democratic voting for the Public Trust "
          "Housing and Public Trust Foundation decisions, and the Public Trust Foundations (grocers, restaurants, "
          "utilities and transit accepting basic units) are governed democratically by employees, customers and "
          "community representatives; but the design's sources say this network coexists with private markets "
          "rather than replacing them and complements rather than displaces private operations, its corporate paper "
          "describes a shift from shareholder to stakeholder models without saying who would elect the boards of "
          "transformed corporations, and the participation figures it states are for housing (a 50% market share "
          "target) and for merchants within designated zones (55% before synergy effects activate), not for "
          "employment; no source states or projects that the accountable organizations would employ 80% of workers",
     HUB + ": corporate-transformation.html (abstract and section 3); wiki/glossary.html (Public Trust Foundation); "
     "cco-ptf-simulation-replication.html (glossary: SZH, CIP); index.html (PTH penetration target); " + REP +
     "CCO C4.4"),
    ("C", "as part (b7) recorded: Public Trust Housing leadership has term limits, mandatory rotation and recall "
          "elections, and the merit juries are selected at random and rotated", S47 + "CCO C4.4, clause 2")],
  note="part (b7)'s flag on clause 2 (alternative 0.5) no longer bears on the verdict, which clause 1 fixes at 0.5, "
       "and is dropped; under the alternative recorded in decision 48.3(e) the unit would return to 1.0 with that "
       "flag")

U("INT", "C4.4", 1.0, [
    ("C", "the audited phrase, broad democratic accountability, claims the defined condition: the design delegates no "
          "managerial authority, decisions are taken by participants in CDS at every scale with local autonomy "
          "preserved, production is coordinated by rotating teams that coordinate rather than command, and ITC's "
          "non-accumulability keeps wealth from converting into power, so the investment, production and employment "
          "decisions are taken by those they affect (all of the design's employment)",
     AUD48 + "; " + INTWP + ", sections 5.2 and 5.5; " + REP + "INT C4.4"),
    ("C", "as part (b7) recorded: decisions taken in CDS can be reaffirmed, amended, revoked or reopened by its "
          "review module, and no managerial authority is delegated", S47 + "INT C4.4, clause 2")])

U("NSD", "C4.4", 0.5, [
    ("S", "V-Dem's Regimes of the World classes Denmark, Finland, Norway and Sweden as liberal democracies, so their "
          "public sectors count; on the most generous count (all of general government, every central-government "
          "state-owned enterprise, the self-employed, and every cooperative, mutual, association and foundation) "
          "the share of employment in organizations whose decisions answer to those they affect is at most {DK} in "
          "Denmark, {FI} in Finland and {SE} in Sweden, and {NO} in Norway before its social economy, which would "
          "have to employ {NOGAP} of workers, {RATIO} times the highest share in the EU-28 ({SEMAX}); the rest work "
          "in companies whose boards shareholders elect, employees electing a minority (Sweden two or three members, "
          "a quarter to a third of the board; Norway and Denmark a third; Finland as agreed, in companies of 150 or "
          "more); short of 80% in each, by at least {GAP} points (decision 48.3(d))", NORDIC_SRC),
    ("C", "parliamentary removal functions: Sweden's prime minister lost a confidence vote on 21 June 2021, as part (a) "
          "found", S47 + "NSD C4.4, clause 2 (Riksdag confidence vote, 21 June 2021)")],
  note="part (b7)'s flag (alternative 1.0, on its reading 3.6(b)) is removed: decision 48.3 fixes the reading, and "
       "the reading the flag named is recorded there as the alternative for the owner")

U("MS", "C4.4", 1.0, [
    ("C", "the audited phrase, economic power distributed through democratic ownership, claims the defined "
          "condition: the system places enterprises in the ownership of those who work in them and removes the "
          "employer-employee hierarchy, and in its principal component each cooperative's worker-members elect the "
          "governing council, one member one vote, and can dismiss it in general assembly (all of the system's "
          "employment)",
     AUD48 + "; " + REP + "MS C4.4; Ley 11/2019, de 20 de diciembre, de Cooperativas de Euskadi, article 46; "
     "International Co-operative Alliance, Statement on the Cooperative Identity, principle 2"),
    ("C", "as part (b7) recorded: administrators serve two to five years and the general assembly may dismiss them "
          "and elect their replacements in the same session", S47 + "MS C4.4, clause 2")])

EXPECT = {"units": 6, "stand": [("INT", "C4.4"), ("MS", "C4.4"), ("PE", "C4.4")],
          "moved": {("CCO", "C4.4"): (1.0, 0.5)}, "flags_dropped": [("CCO", "C4.4"), ("NSD", "C4.4")],
          "carried": [("INT", "C4.4", 0), ("MS", "C4.4", 0), ("PE", "C4.4", 0)],
          "estimated": [("CCO", "C4.4", 0)], "ones_left": ["MS", "PE", "INT"], "published_ones": 6,
          "dominance_b7": 21, "frontier_b7": 13, "emptied": 8, "reestimated": 128, "first": ("CCO", 19.0, 18.5)}


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
    rs, s47 = mods[0], mods[-1]
    f1 = rs.f1
    crit = json.loads(rs.read(CRIT44))["criteria"]
    cids = [c["id"] for c in crit]
    v2 = {c["id"]: c for c in json.loads(rs.read(CRITERIA))["criteria"]}
    v47 = {c["id"]: c for c in json.loads(rs.read(CRIT47))["criteria"]}
    corpus = json.loads(rs.read(CORPUS))["entries"]
    names = {e["code"]: e["display_name"] for e in corpus}
    vec = {e["code"]: dict(e["vector"]) for e in corpus}
    prior = tuple(m.UNITS for m in mods)

    print(f"NEEC rescoring pass: C4.4 re-read on decision 48.3, and the score ledger ({RECORD})")
    print(f"inputs: {CRITERIA}, {CRIT47}, {CRIT44}, {CORPUS}, {CSV}, {REPORT}, {AUDIT}, "
          + ", ".join(p for _, _, p, _ in PRIOR) + f", {RECORD}\n")

    # [1] the criterion ------------------------------------------------------------------------------------------------
    print("[1] C4.4 ON DECISION 48.3")
    c2, c1 = v2[CRIT], v47[CRIT]
    meas = c2["definition"]["measurement"]
    check(c2["revision"]["cls"] == "M" and c1["revision"]["cls"] == "D"
          and c2["definition"]["clauses"] == c1["definition"]["clauses"]
          and c2["definition"]["pass_threshold"] == c1["definition"]["pass_threshold"]
          and meas.startswith(c1["definition"]["measurement"]) and len(meas) > len(c1["definition"]["measurement"]),
          "C4.4 is class M (class D at tag s47), its Pass Threshold and clauses unchanged, its measurement field "
          "extended by the definition")
    need = ("investment, production and employment decisions", "elect a majority of those who take it",
            "owners of capital elect", "Regimes of the World", "at least 80% of workers")
    check(all(x in meas for x in need), "the definition names the decisions, the accountability test, the minority "
                                        "board rule, the public-sector test and the design rule")
    for i, t in enumerate(c2["definition"]["clauses"]):
        print(f"  C4.4 ({i + 1}) {t}")

    # [2] the group and its records ------------------------------------------------------------------------------------
    print("\n[2] THE GROUP AND ITS RECORDS")
    b7 = {k: r for k, r in s47.UNITS.items() if k[1] == CRIT}
    check(sorted(UNITS) == sorted(b7) and len(UNITS) == EXPECT["units"],
          f"the group is exactly part (b7)'s {len(b7)} C4.4 units, each re-read here: "
          + ", ".join(c for c, _ in UNITS))
    bad = []
    for key, rec in UNITS.items():
        if len(rec["clauses"]) != len(c2["definition"]["clauses"]):
            bad.append(f"{key}: clause count")
        for k, (st, est, src) in enumerate(rec["clauses"]):
            if st not in STATUS or not est.strip() or not src.strip():
                bad.append(f"{key} clause {k + 1}: status, estimate or source missing")
            if "|" in est + src + rec["note"]:
                bad.append(f"{key} clause {k + 1}: a pipe character would break the table")
    for b in bad:
        print(f"  FAIL {b}")
    ok = ok and not bad
    check(not bad, "every unit has one status per v2.0 clause, each with its estimate and its source")
    same2 = [k for k in UNITS if UNITS[k]["clauses"][1][0] != b7[k]["clauses"][1][0]]
    check(not same2, "clause 2's status is part (b7)'s in every unit (decision 48.3 changes clause 1's measure only)")

    # [3] the rule -----------------------------------------------------------------------------------------------------
    print("\n[3] THE RULE (D28) AND THE AUDIT'S CODES, RE-READ ON THE DEFINED MEASURE")
    wrong = [k for k, r in UNITS.items() if rs.verdict_of(r["clauses"]) != r["verdict"]]
    check(not wrong and all(r["verdict"] in (0.5, 1.0) for r in UNITS.values()),
          "every verdict follows D28, and none is 0.0 (D28(f))", str(wrong))
    stand = sorted(k for k, r in UNITS.items() if r["verdict"] == 1.0)
    moved = {k: (b7[k]["verdict"], r["verdict"]) for k, r in UNITS.items() if r["verdict"] != b7[k]["verdict"]}
    check(stand == EXPECT["stand"] and moved == EXPECT["moved"],
          f"{len(stand)} stand ({', '.join(c for c, _ in stand)}); against part (b7) one unit moves: "
          + ", ".join(f"{c} {k} {f1(a)} -> {f1(b)}" for (c, k), (a, b) in moved.items()))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    a1 = sorted((c, k, 0) for (c, k) in UNITS if reg[(c, k)][2] == "A")  # clause 1 continues the audit's clause 3
    carried = sorted(x for x in a1 if UNITS[x[:2]]["clauses"][0][2].startswith(AUD48))
    estimated = sorted(x for x in a1 if x not in carried)
    check(carried == EXPECT["carried"] and estimated == EXPECT["estimated"]
          and all(UNITS[x[:2]]["clauses"][0][0] == "C" for x in carried),
          f"the audit coded clause 1 A in {len(a1)} units: {len(carried)} carried on the defined measure with the "
          f"design's own sources ({', '.join(c for c, _, _ in carried)}), {len(estimated)} estimated "
          f"({', '.join(c for c, _, _ in estimated)})")
    flags_b7 = sorted(k for k in b7 if b7[k]["flag"])
    check(flags_b7 == EXPECT["flags_dropped"] and not any(r["flag"] for r in UNITS.values()),
          f"part (b7)'s two flags ({', '.join(c for c, _ in flags_b7)}) are dropped, and none is added")

    # [4] Nordic Social Democracy's bound ------------------------------------------------------------------------------
    print("\n[4] NORDIC SOCIAL DEMOCRACY, CLAUSE 1: THE MOST GENEROUS COUNT (decision 48.3(d))")
    rows = ["| Country | Regimes of the World | General government | State-owned enterprises | Self-employed | "
            "Social economy | Most generous count | Short of 80% by |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    got = {}
    for c, v in NORDIC.items():
        b = bound(v)
        got[c] = b
        se = "not covered" if v[4] is None else f"{v[4]:.1f}%"
        rows.append(f"| {c} | {v[5]} (liberal democracy) | {v[0]:.1f}% | {v[1]:.1f}% | {100 * v[2] / v[3]:.1f}% | "
                    f"{se} | {b:.1f}% | {80 - b:.1f} |")
    nsd_table = "\n".join(rows)
    print(nsd_table)
    gap_no = 80 - got["Norway"]
    ratio = gap_no / SE_MAX[1]
    fmt = dict(DK=f"{got['Denmark']:.1f}%", FI=f"{got['Finland']:.1f}%", SE=f"{got['Sweden']:.1f}%",
               NO=f"{got['Norway']:.1f}%", NOGAP=f"{gap_no:.1f}%", RATIO=f"{ratio:.1f}",
               SEMAX=f"{SE_MAX[0]}'s {SE_MAX[1]:.1f}%", GAP=f"{min(80 - x for x in got.values()):.0f}")
    st, est, src = UNITS[("NSD", CRIT)]["clauses"][0]
    UNITS[("NSD", CRIT)]["clauses"][0] = (st, est.format(**fmt), src)
    check(all(v[5] >= 2 for v in NORDIC.values()) and all(x < 80 for x in got.values())
          and min(80 - x for x in got.values()) >= 31 and gap_no > 3 * SE_MAX[1],
          f"the public sector counts in all four; the most generous count is below 80% in each (largest {max(got.values()):.1f}%, "
          f"Finland), and Norway's social economy would need {gap_no:.1f}% of employment, {ratio:.1f} times the "
          "highest EU-28 share: clause 1 short")

    # [5] flags --------------------------------------------------------------------------------------------------------
    print("\n[5] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b7))")
    blocks = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}
    merged, part_of = {}, {}
    for (tag, _, _, sess), part in zip(PRIOR, prior):
        merged.update(part)
        part_of.update({k: (tag, sess) for k in part})
    before = dict(merged)
    merged.update(UNITS)
    part_of.update({k: THIS for k in UNITS})

    def changes(units):
        add = sorted(k for k, r in units.items() if r["flag"] and k not in had)
        rem = sorted(k for k, r in units.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
        return add, rem
    a0, r0 = changes(before)
    a1_, r1 = changes(merged)
    moved_e = sorted({k[0] for k in a1_ + r1})
    flag_line = (f"Flags added by the pass so far: {len(a1_)} (against {len(a0)} after part (b7)); removed: {len(r1)}. "
                 f"Across the pass so far, {len(moved_e)} entries' flag registers change ({', '.join(moved_e)}).")
    check(len(a0) - len(a1_) == 2 and r0 == r1, "the pass's added flags fall by two (CCO C4.4, NSD C4.4)")
    print("  " + flag_line)

    # [6] consequences -------------------------------------------------------------------------------------------------
    print("\n[6] CONSEQUENCES (on the published 26-criterion structure; no corpus file changes)")
    vsteps = [{c: dict(v) for c, v in vec.items()}]
    for part in prior + (UNITS,):
        v = {c: dict(x) for c, x in vsteps[-1].items()}
        for (c, k), r in part.items():
            v[c][k] = r["verdict"]
        vsteps.append(v)

    def summ(v):
        return {"total": {c: sum(v[c][k] for k in cids) for c in v},
                "fail": {c: sum(v[c][k] == 0.0 for k in cids) for c in v}}
    steps = [summ(x) for x in vsteps]
    base, m7, after = steps[0], steps[-2], steps[-1]
    check(base["fail"] == after["fail"], "no failure count changes, so no tier changes (D28(f))")
    rb, r7, rn = rs.ranks(base["total"]), rs.ranks(m7["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After (b7) (rank) | After 48.3 (rank) | Change here | Failures | Tier |",
            "|---|---:|---:|---:|---:|---:|---|"]
    for code in rs.order_codes(names, base):
        rows.append(f"| {code} | {f1(base['total'][code])} ({rb[code]}) | {f1(m7['total'][code])} ({r7[code]}) | "
                    f"{f1(after['total'][code])} ({rn[code]}) | {f1(after['total'][code] - m7['total'][code])} | "
                    f"{after['fail'][code]} | {rs.tier(after['fail'][code])} |")
    cons_table = "\n".join(rows)
    p7, f7 = rs.dominance(vsteps[-2], cids)
    pn, fn = rs.dominance(vsteps[-1], cids)
    order = list(names)
    check(len(p7) == EXPECT["dominance_b7"] and len(f7) == EXPECT["frontier_b7"],
          f"part (b7)'s result reproduced: {len(p7)} dominance pairs, frontier {len(f7)}")
    gained = sorted(set(pn) - set(p7), key=lambda p: (order.index(p[0]), order.index(p[1])))
    lost = sorted(set(p7) - set(pn), key=lambda p: (order.index(p[0]), order.index(p[1])))
    first = [c for c in order if after["total"][c] == max(after["total"].values())]
    check((first[0], m7["total"][first[0]], after["total"][first[0]]) == EXPECT["first"] and len(first) == 1,
          f"first place: {first[0]}, {f1(m7['total'][first[0]])} after part (b7), {f1(after['total'][first[0]])} now")
    ones = [c for c in order if vsteps[-1][c][CRIT] == 1.0]
    pub_ones = [c for c in order if vec[c][CRIT] == 1.0]
    emptied = [k for k in cids if not any(vsteps[-1][c][k] == 1.0 for c in vec)]
    c44 = next(x for x in crit if x["id"] == CRIT)["anchors"]["bands"]["1.0"]["examples"]
    check(sorted(ones) == sorted(EXPECT["ones_left"]) and len(pub_ones) == EXPECT["published_ones"]
          and len(emptied) == EXPECT["emptied"] and [x["system"] for x in c44] == ["Participatory Economics"]
          and vsteps[-1]["PE"][CRIT] == 1.0,
          f"C4.4 keeps {len(ones)} 1.0s ({', '.join(ones)}) of {len(pub_ones)} published; its anchor example, "
          f"Participatory Economics, stands; the criteria with no 1.0 stay {len(emptied)}")
    n_all = len(merged)
    st_all = sum(1 for r in merged.values() if r["verdict"] == 1.0)
    pts_all = sum(1.0 - r["verdict"] for r in merged.values())
    check(n_all == EXPECT["reestimated"], f"{n_all} units re-estimated across the pass, each counted once")
    dom_line = (f"After this record the corpus has {len(pn)} dominance pairs against {len(p7)} after part (b7) (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(f7)} (" + ", ".join(c for c in order if c in fn) + f"). First place: {first[0]}, "
                f"{f1(m7['total'][first[0]])} after part (b7), {f1(after['total'][first[0]])} now. Across the pass so "
                f"far {n_all} units have been re-estimated, each counted once: {st_all} stand and {n_all - st_all} "
                f"are at 0.5 ({f1(pts_all)} points). C4.4 keeps {len(ones)} 1.0s ({', '.join(ones)}) against "
                f"{len(pub_ones)} published; its anchor example, Participatory Economics, stands.")
    print("  " + dom_line)

    # [7] the ledger ---------------------------------------------------------------------------------------------------
    print("\n[7] THE SCORE LEDGER (published total, each part's change, the total now; 26 criteria)")
    tags = [t for t, _, _, _ in PRIOR] + [THIS[0]]
    csv_rows = list(csv.DictReader(rs.read(CSV).splitlines()))
    csv_tot = {r["system"]: (float(r["total_score"]), int(r["failures"]), r["criteria_count"]) for r in csv_rows}
    check(len(csv_rows) == len(corpus) and all(
              csv_tot[names[c]] == (base["total"][c], base["fail"][c], "26") for c in names),
          f"the published totals and failure counts in {CORPUS} equal {CSV}'s for all {len(corpus)} entries, on 26 "
          "criteria")
    report = rs.read(REPORT)
    check(f"CCO-PTF-CIP-SZH: {f1(base['total']['CCO'])}/26 (94%)" in report and "was 23.5/25, 94%" in report,
          f"{REPORT} states CCO-PTF-CIP-SZH's published total, {f1(base['total']['CCO'])}/26, and its version 1 total, "
          "23.5/25")
    head = "| Entry | Published | " + " | ".join(tags) + " | Now | Re-estimated | At 0.5 |"
    rows = [head, "|---|---:|" + "---:|" * len(tags) + "---:|---:|---:|"]
    sums_ok = True
    for code in rs.order_codes(names, base):
        deltas = [steps[i + 1]["total"][code] - steps[i]["total"][code] for i in range(len(tags))]
        mine = [k for k in merged if k[0] == code]
        low = [k for k in mine if merged[k]["verdict"] == 0.5]
        sums_ok = sums_ok and abs(sum(deltas) - (after["total"][code] - base["total"][code])) < 1e-9
        cells = " | ".join("" if d == 0 else f1(d) for d in deltas)
        rows.append(f"| {code} | {f1(base['total'][code])} | {cells} | {f1(after['total'][code])} | {len(mine)} | "
                    f"{len(low)} |")
    ledger = "\n".join(rows)
    check(sums_ok, "each entry's changes, part by part, sum to the difference between its published total and its "
                   "total now")
    sess = {t: s for t, _, _, s in PRIOR}
    sess[THIS[0]] = THIS[1]
    rows = ["| Criterion | Published | Now | Part (session) | Clauses not shown or short |", "|---|---:|---:|---|---|"]
    for k in cids:
        key = ("CCO", k)
        if key not in merged:
            continue
        rec = merged[key]
        tag, s = part_of[key]
        texts = (v2[k]["definition"]["clauses"] if tag in ("(b7)", THIS[0]) else [x[0] for x in r4.CLAUSES[k]])
        miss = [f"{i + 1} ({texts[i]}) {STATUS[st]}" for i, (st, _, _) in enumerate(rec["clauses"]) if st in "SUR"]
        rows.append(f"| {k} | {f1(vec['CCO'][k])} | {f1(rec['verdict'])} | {tag} (s{s}) | "
                    f"{'; '.join(miss) or 'none: stands'} |")
    cco_table = "\n".join(rows)
    cco = [k for k in merged if k[0] == "CCO"]
    cco_low = [k for k in cco if merged[k]["verdict"] == 0.5]
    check(abs(base["total"]["CCO"] - 0.5 * len(cco_low) - after["total"]["CCO"]) < 1e-9
          and all(vec["CCO"][k] == 1.0 for _, k in cco),
          f"CCO-PTF-CIP-SZH: {len(cco)} of its published 1.0s re-estimated, {len(cco_low)} at 0.5; "
          f"{f1(base['total']['CCO'])} - {f1(0.5 * len(cco_low))} = {f1(after['total']['CCO'])}")
    ones_by = {c: sum(1 for k in cids if vec[c][k] == 1.0) for c in vec}
    ones_cco = ones_by["CCO"]
    nxt = max((c for c in order if c != "CCO"), key=lambda c: ones_by[c])
    check(all(ones_by[c] < ones_cco for c in vec if c != "CCO"),
          f"CCO-PTF-CIP-SZH was published with more 1.0s than any other entry ({ones_cco}; next {nxt}, "
          f"{ones_by[nxt]})")
    cco_line = (f"CCO-PTF-CIP-SZH was published at {f1(base['total']['CCO'])}/26 with {ones_cco} criteria at 1.0, "
                f"more than any other entry (the next, {names[nxt]}, had {ones_by[nxt]}). The "
                f"pass has re-estimated {len(cco)} of them; {len(cco_low)} are at 0.5, so it stands at "
                f"{f1(after['total']['CCO'])}/26 ({f1(base['total']['CCO'])} - {len(cco_low)} x 0.5). Its three v2.0 "
                f"criteria (C2.6, C3.6, C4.6) are not scored yet, so no total on 29 criteria exists: when they are, "
                f"its 29-criterion total will be its 26-criterion total after the pass plus 0 to 3.")
    print("  " + cco_line)

    # [8] the record ---------------------------------------------------------------------------------------------------
    print(f"\n[8] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    t = {}
    rows = ["| Entry | Criterion | Clauses | Verdict |", "|---|---|---|---|"]
    for key in UNITS:
        rec = UNITS[key]
        was = f1(b7[key]["verdict"]) + (" (flagged)" if b7[key]["flag"] else "")
        rows.append(f"| {key[0]} | {key[1]} | {' '.join(s for s, _, _ in rec['clauses'])} | part (b7) {was} → "
                    f"{f1(rec['verdict'])} |")
    t["summary"] = "\n".join(rows)
    for key, rec in UNITS.items():
        lines = [f"#### {key[0]} C4.4 Power Distribution: part (b7) {f1(b7[key]['verdict'])} → {f1(rec['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for k, (st, est, src) in enumerate(rec["clauses"]):
            lines.append(f"| {k + 1} | {c2['definition']['clauses'][k]} | {STATUS[st]} | {est} | {src} |")
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {key[0]}"] = "\n".join(lines)
    t["nordic"], t["consequences"], t["dominance"], t["flags"] = nsd_table, cons_table, dom_line, flag_line
    t["ledger"], t["cco"], t["cco_line"] = ledger, cco_table, cco_line
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
    print()
    print(cco_table)
    print("\nC4.4 ON DECISION 48.3 AND THE SCORE LEDGER, COMPUTED." if ok else
          "\nC4.4 ON DECISION 48.3 AND THE SCORE LEDGER: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
