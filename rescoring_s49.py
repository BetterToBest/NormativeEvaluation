#!/usr/bin/env python3
"""
rescoring_s49.py -- NEEC rescoring pass (decisions D28, D29, D31), part (b), eighth group: C4.3 Group Equity and
C4.5 Exploitation Elimination, on the v2.0 clauses
==============================================================================================================
Session 49. Parts (a) to (b7) are NEEC_Rescoring_s37.md to NEEC_Rescoring_s47.md (rescoring_s37.py to
rescoring_s47.py), and NEEC_Rescoring_s48.md (rescoring_s48.py) re-read C4.4 on decision 48.3. This script holds the
eighth group, scored on the v2.0 criteria as part (b7) was (decision 7.1 of the Session 44 review): the nine part (b)
units of C4.3 and C4.5, and the three units of C4.5 that part (a) re-estimated on the Session 44 clauses
(Centrally Planned Socialism's, Libertarian Minarchism's and Universal Basic Income's), re-read here on the v2.0
clauses. C4.3 has no part (a) unit. It changes no file and no score: the pass's changes are applied by generator
when it ends (protocol 10.2, 10.3).

Statuses and the rule are part (a)'s: C cleared, S short, U not shown, R out of reach, M moot; a 1.0 stands only if
every clause is C or M, otherwise it becomes 0.5, never 0.0 in this pass (D28(f)). The clauses are v2.0's
(criteria.json). Both criteria keep their clauses verbatim and delete one: C4.3 (class M) its second Session 44
clause, the 150% benefit clause, and C4.5 (class D) its third, residual coercion, which v2.0 measures once, in C2.1.
C4.3 gains a scope, "on each declared axis, non-citizen residents included", and a measure (the gap between groups'
median household incomes), so the audit's A codes on its clauses are re-read against the clause with its scope and
measure (reading 3.2), as rescoring_s48.py re-read C4.4's on decision 48.3; on C4.5 they are carried as cleared on
the unit's own text. A re-read unit of part (a) can keep its verdict or rise (class D), and its record here
supersedes part (a)'s.

CHECKS: the group against the audit's register and against part (a); the v2.0 clauses, scope and deletions; every
record complete; the rule; the audit's codes carried or re-read; every silent clause estimated; reach; Nordic
Social Democracy's C4.3 clause 1 computed from the Eurostat series held below; flags against the summary blocks,
cumulatively with parts (a) to (b7) and decision 48.3; the consequences of the pass so far on the published
26-criterion structure (totals, ranks, failures, tiers, dominance, frontier, what remains, the criteria left with no
1.0), the score ledger, the anchor examples the pass so far moves; and that NEEC_Rescoring_s49.md contains every
generated table verbatim.

Usage: python3 rescoring_s49.py   (reads criteria.json (v2.0), criteria_s44_snapshot.json (the published structure
                                   and anchors), criteria_s47_snapshot.json, neec_corpus.json, neec_scores.csv,
                                   NEEC_Report_v1_6.md, r4_audit_s35.py, rescoring_s37.py to rescoring_s48.py and the
                                   files they read, and NEEC_Rescoring_s49.md beside itself; writes nothing)
       python3 rescoring_s49.py --tables   (prints the generated tables as JSON, for assembling the record)
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
         ("48.3", "rescoring_s48", "rescoring_s48.py", 48))
THIS = ("(b8)", 49)
RECORD = "NEEC_Rescoring_s49.md"
GROUP = ("C4.3", "C4.5")
# v2.0 clause index -> the Session 44 clause it continues (the audit's index). Every v2.0 clause here is verbatim;
# DELETED names the Session 44 clause v2.0 drops. SCOPED: clauses v2.0 places under a new scope and measure, whose A
# codes are re-read (reading 3.2).
MAP = {"C4.3": (0, 2), "C4.5": (0, 1)}
DELETED = {"C4.3": 1, "C4.5": 2}
SCOPED = {"C4.3": (0, 1), "C4.5": ()}
SCOPE = "on each declared axis, non-citizen residents included"
STATUS = {"C": "cleared", "S": "short", "U": "not shown", "R": "out of reach", "M": "moot"}
REP = "Report v1.6, "
AUD = "as audited (the unit's own text)"
S37, S42 = "rescoring_s37.py, ", "NEEC_Rescoring_s42.md, "
EUROSTAT = ("Eurostat, EU-SILC, ilc_di16 (median equivalised net income by group of country of birth) and ilc_di15 "
            "(by group of citizenship), population aged 18 or over, national currency, editions 2016 to 2025, data "
            "updated 2026-09-17, retrieved 2026-09-25 (JSON md5 2b786488 and 9f69c948)")
ALEXEEV = ("Alexeev and Gaddy, Income Distribution in the U.S.S.R. in the 1980s, Review of Income and Wealth 39(1) "
           "(1993), section 1 and Tables 1 and 2 (Goskomstat budget surveys; PDF md5 6e1b8367)")
ITC = ("integralcollective.io, The System: ITC (modules ITC-5, ITC-6 and ITC-7), accessed 2026-09-25 (page md5 "
       "e5e589fa)")
SIM = "Compassionism Simulation at cd0ceec, harness.js (md5 035d1be8) and index.html (md5 1c8273b1), searched 2026-09-25"
HUB = "research hub at 8e8a6ba, searched 2026-09-25"

UNITS = {}
GENERATED = {}


def U(code, crit, verdict, clauses, flag=None, note=""):
    """One unit. clauses: (status, estimate, source) in v2.0's order. flag: (alternatives, reading)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=clauses, flag=flag, note=note)


# ---- Nordic Social Democracy, C4.3 clause 1: the gaps on the immigrant axis (reading 3.4) ------------------------
# Median equivalised net income, national currency (EUR for Finland), of the reporting country's natives (by birth)
# or nationals (by citizenship), and of those born in, or citizens of, a country outside the EU-27 and the reporting
# country; editions 2016 to 2025. "b" marks a break in series in either figure, as Eurostat flags it.
NORDIC_YEARS = tuple(range(2016, 2026))
NORDIC = {
    "birth": {
        "Denmark": [(213529, 183002), (219851, 171600), (226500, 176791), (228836, 191068), (229598, 189506, "b"),
                    (239400, 209478), (248138, 204461), (253630, 205570), (260104, 230993), (269931, 241909)],
        "Finland": [(24051, 18326), (24338, 19282), (24931, 19484), (25231, 20381), (25897, 20240), (25852, 21125),
                    (26930, 22380), (27709, 23037), (29241, 23197), (30403, 24100)],
        "Sweden": [(248147, 177365), (256247, 176124), (263519, 180167), (272096, 180463), (281494, 198176),
                   (287835, 196905), (293348, 216336), (311033, 222370), (333947, 246008), (352700, 256025)],
        "Norway": [(365802, 281814), (369102, 291811), (383209, 290569), (393868, 293357), (411000, 319965),
                   (402426, 307304, "b"), (414680, 329762), (438820, 372356, "b"), (480732, 377561),
                   (509300, 408737)],
    },
    "citizenship": {
        "Denmark": [(212428, 181332), (218185, 174286), (225558, 172662), (228231, 180263), (229785, 161454, "b"),
                    (239410, 187193), (248054, 189525), (253588, 186571), (259269, 222199), (269953, 213899)],
        "Finland": [(23976, 17767), (24293, 18219), (24805, 18038), (25187, 19501), (25877, 19240), (25806, 20562),
                    (26917, 22373), (27676, 21821), (29162, 22284), (30250, 24115)],
        "Sweden": [(243557, 135678), (251330, 145822), (258199, 142591), (266327, 144874), (274526, 168710),
                   (280552, 179397), (283369, 184375), (300516, 206613), (323277, 229966), (341775, 225421)],
        "Norway": [(363214, 240714), (366660, 265514), (379004, 273194), (388809, 278040), (407410, 307814),
                   (397968, 299318, "b"), (409706, 324282), (435588, 350388, "b"), (474402, 342201),
                   (504631, 357327)],
    },
}
LEVEL, RATE = 20.0, 5.0   # the convergence level (<20%) and the reduction (>=5 percentage points per 5 years)


def gap(row):
    return 100 * (row[0] - row[1]) / row[0]


def nordic_measures(rows):
    """The gap's mean over 2023-2025 and over 2018-2020, their difference, and the least-squares trend over the ten
    editions per 5 years."""
    g = dict(zip(NORDIC_YEARS, (gap(r) for r in rows)))
    late = sum(g[y] for y in (2023, 2024, 2025)) / 3
    early = sum(g[y] for y in (2018, 2019, 2020)) / 3
    xs = list(NORDIC_YEARS)
    mx, my = sum(xs) / len(xs), sum(g.values()) / len(xs)
    slope = sum((x - mx) * (g[x] - my) for x in xs) / sum((x - mx) ** 2 for x in xs)
    return dict(late=late, early=early, change=late - early, trend=5 * slope)


# ---- C4.3 Group Equity (readings 3.2 to 3.5) -----------------------------------------------------------------------
NOPROJ = ("no projection of the gap between groups' median household incomes on any declared axis is stated, modelled "
          "or located, so neither the rate nor the convergence is shown (reading 3.3)")
U("NSD", "C4.3", 0.5, [
    ("S", "the entry's own text names immigrant and minority communities, so immigrant background is a declared axis, "
          "read by country of birth and by citizenship (non-EU against natives or nationals); in each of the four "
          "countries a gap above 20% falls by less than 5 points in five years on both measures: {ROWS} (three-year "
          "means, 2023-2025 against 2018-2020; the trend is the least-squares fit over the ten editions, per five "
          "years) (reading 3.4)", EUROSTAT + "; " + REP + "NSD C4.3"),
    ("U", "the audited phrase, the strongest performance on gender equity globally, claims the gender axis, not the "
          "immigrant axis the entry's text declares; on the ten-edition trends the immigrant-axis gaps above 20% reach "
          "20% by {LAST} except Denmark's by citizenship, whose trend rises ({DKTREND} points per five years) although "
          "its three-year mean fell; series this noisy do not establish a convergence trajectory (reading 3.4)",
     EUROSTAT)],
  note="the audit coded both clauses A; both are re-read against the scope and measure v2.0 adds (reading 3.2)")

U("CPS", "C4.3", 0.5, [
    ("U", "the rationale is silent on the rate, as the audit found; the Soviet statistics office did not publish the "
          "size distribution of household income from the 1920s until 1989, and then by republic only for 1988 and "
          "1990, two years apart, so no source can show a gap between nationalities' median household incomes falling "
          "5 points in five years; the 1988 distributions show the southern republics' per capita household incomes "
          "well below the northern ones' (reading 3.5)", ALEXEEV + "; " + REP + "CPS C4.3"),
    ("U", "the audited phrase, women's high labour force participation, education and leadership roles, is an outcome "
          "on another measure, not a trajectory of household income gaps; for the same reason no series by "
          "nationality exists from which a convergence could be projected (readings 3.2 and 3.5)",
     ALEXEEV + "; " + REP + "CPS C4.3")])

U("MMT", "C4.3", 0.5, [
    ("U", "the audited phrase, eliminating discrimination in hiring through the government as employer of last "
          "resort, is a process; the programme's proponents argue that it would effectively eliminate the racial "
          "unemployment gap and set an economy-wide floor on compensation, but a gap in unemployment is not a gap in "
          "median household income, and " + NOPROJ,
     "Paul, Darity and Hamilton, The Federal Job Guarantee: A Policy to Achieve Permanent Full Employment (Center on "
     "Budget and Policy Priorities, 2018); " + REP + "MMT C4.3"),
    ("U", "the rationale's care and community-service jobs address gendered devaluation of labour, a mechanism; " + NOPROJ,
     "Paul, Darity and Hamilton (2018); " + REP + "MMT C4.3")])

U("UBI", "C4.3", 0.5, [
    ("U", "the audited phrase, universal provision that addresses disparities without stigma, describes access to the "
          "benefit, not a fall in a gap; a flat payment narrows percentage gaps once, when it is introduced, which is "
          "not a reduction every five years; " + NOPROJ, REP + "UBI C4.3"),
    ("U", "care work made viable without market employment is a mechanism; " + NOPROJ, REP + "UBI C4.3")])

U("DG", "C4.3", 0.5, [
    ("U", "the audited phrase, explicitly confronting structural inequalities, is a commitment; decolonial and "
          "feminist-economic aims and care valued equally with production are goals and means, and " + NOPROJ,
     REP + "DG C4.3"),
    ("U", "as for clause 1: " + NOPROJ, REP + "DG C4.3")])

U("PE", "C4.3", 0.5, [
    ("U", "the audited phrase, effort-based remuneration that addresses the devaluation of care work, is a "
          "remuneration rule: it ties income to effort, sacrifice and need, but the gaps that would result between "
          "groups depend on hours, need allowances and household composition, and " + NOPROJ, REP + "PE C4.3"),
    ("U", "balanced job complexes and democratic participation are institutions, not an estimate of the gap's path; "
          + NOPROJ, REP + "PE C4.3")])

# ---- C4.3's one 1.0 outside D28's population, re-checked as class M (reading 3.8) ----------------------------------
U("CCO", "C4.3", 0.5, [
    ("U", "the audited phrase, universal provision that addresses disparities without stigma, is the phrase re-read "
          "for Universal Basic Income: access to the benefit, not a fall in a gap; targeting disadvantaged communities "
          "first, with 150%+ proportional benefits during rollout, is a benefit flow, which v2.0's measurement counts "
          "as evidence for the trajectory, not a separate test, and it states no gap or rate; the design's published "
          "model represents no groups, and its research hub projects no gap; " + NOPROJ, REP + "CCO C4.3; " + SIM + "; "
     + HUB),
    ("U", "the audited phrase, trafficking vulnerability eliminated through unconditional security, is an outcome on "
          "another measure, not the path of a household income gap, and aesthetic multipliers that value historically "
          "devalued creative work are a mechanism; " + NOPROJ, REP + "CCO C4.3; " + SIM + "; " + HUB)],
  note="the one C4.3 1.0 outside D28's population (the audit coded every clause A); C4.3 is class M, so it is "
       "re-checked here on readings 3.2 and 3.3 with the rest of C4.3 rather than left for stage 2 (reading 3.8)")
CLASSM = [("CCO", "C4.3")]

# ---- C4.5 Exploitation Elimination (reading 3.6) --------------------------------------------------------------------
U("DG", "C4.5", 0.5, [
    ("C", "removes profit motive for extraction", AUD),
    ("U", "universal basic services secure housing, healthcare, education and transport, but for employment the entry "
          "specifies reduced hours and work-sharing, not an income floor or an assured alternative, and its own C2.2 "
          "rationale says the design does not fully decouple survival from employment, so exit from an employment "
          "relationship without penalty is not shown (reading 3.6)", REP + "DG C1.1, C2.1, C2.2 and C4.5")],
  flag=([1.0], "read as the entry's C2.1 rationale reads its universal basic services, as eliminating survival "
               "coercion, exit from employment would be genuine; the services it names cover housing, healthcare, "
               "education and transport, not food or income, and its C2.2 rationale says survival is not fully "
               "decoupled from employment (reading 3.6)"))

U("FALC", "C4.5", 1.0, [
    ("C", "Eliminates labor exploitation", AUD),
    ("C", "the design provides universal material provision, housing included, through automated production and makes "
          "labour an optional hobby rather than a survival requirement, so no one depends on an employment, tenancy "
          "or credit relationship for subsistence (reading 3.6)", REP + "FALC C1.1, C1.3 and C2.2")])

U("INT", "C4.5", 1.0, [
    ("C", "removes employer-employee extraction", AUD),
    ("C", "the design has no employer, landlord or creditor: housing is community-controlled, production cooperative, "
          "and ITC credits cannot be borrowed, lent or accrue interest; a participant can leave a team or a node, "
          "contribution in one node is recognised for access in another, basic needs are accessible below standard "
          "contribution thresholds with a need-based adjustment for caregiving and health constraints, and a "
          "participant can leave the federation without penalty (reading 3.6)",
     REP + "INT C4.5; " + ITC + "; " + S42 + "INT C2.5")],
  flag=([0.5], "read as requiring that a participant able to contribute who declines all contribution keep access to "
               "basic needs, the design does not show the clause: basic needs are accessible below standard "
               "contribution thresholds, which the design's sources do not say is no contribution at all "
               "(reading 3.6)"))

# ---- part (a)'s units of C4.5, re-read on v2.0 (reading 3.7) ---------------------------------------------------------
U("CPS", "C4.5", 0.5, [
    ("S", "surplus appropriated by the state rather than private owners: extraction continued, to another "
          "appropriator, with nothing placing it below 10% of GDP, as part (a) found", REP + "CPS C4.5; " + S37 +
     "CPS C4.5"),
    ("S", "exit from employment was penalised: the 1977 Constitution made conscientious work the duty of every "
          "able-bodied citizen and declared evasion of socially useful work incompatible with socialist society, and "
          "the RSFSR's decree of 4 May 1961 on persons avoiding socially useful work punished it (reading 3.6)",
     "Constitution of the USSR (1977), article 60; Decree of the Presidium of the Supreme Soviet of the RSFSR of 4 May "
     "1961")],
  flag=([0.0], "state appropriation read as structural, load-bearing extraction, the 0.0 band's own test (part (a))"),
  note="part (a)'s unit re-read on v2.0's clauses: clause 1 is verbatim and stays short, and clause 2, left not "
       "estimated in part (a), is short; it stays 0.5")

U("LM", "C4.5", 0.5, [
    ("U", "no mechanism limits private extraction, as part (a) found: the entry treats voluntary exchange as "
          "non-exploitative by definition", REP + "LM C4.5; " + S37 + "LM C4.5"),
    ("U", "formal freedom of contract with no subsistence floor and no assured alternative: exit is not shown to be "
          "genuine (reading 3.6)", REP + "LM C4.5; " + S37 + "LM C4.5")],
  flag=([0.0], "the design treats voluntary exchange as non-exploitative by definition: the 0.0 condition of excluding "
               "the criterion's concern as illegitimate (protocol 2.1; part (a))"),
  note="part (a)'s unit re-read on v2.0's clauses: its short clause, residual coercion, is deleted, and neither kept "
       "clause is shown; it stays 0.5")

U("UBI", "C4.5", 0.5, [
    ("R", "the economy-wide extraction share is not governed by an income transfer", "Session 35 reach reason, "
                                                                                      "confirmed in part (a)"),
    ("C", "an exit option from exploitative work", AUD)],
  note="part (a)'s unit re-read on v2.0's clauses: its short clause, residual coercion, is deleted, but clause 1 is "
       "out of reach, so it stays 0.5")

REREAD = [("CPS", "C4.5"), ("LM", "C4.5"), ("UBI", "C4.5")]

# ---- A codes on scoped clauses: carried after re-reading (reading 3.2), or estimated --------------------------------
REREAD_CARRIED = []
REREAD_ESTIMATED = [("CCO", "C4.3", 0), ("CCO", "C4.3", 1), ("CPS", "C4.3", 1), ("DG", "C4.3", 0), ("MMT", "C4.3", 0),
                    ("NSD", "C4.3", 0), ("NSD", "C4.3", 1), ("PE", "C4.3", 0), ("UBI", "C4.3", 0)]

# ---- expected results (every computed verdict below is asserted) ------------------------------------------------
EXPECT = {"units": 13, "per_criterion": {"C4.3": 6, "C4.5": 3}, "reread": 3,
          "stand": [("FALC", "C4.5"), ("INT", "C4.5")], "points_b": 3.5, "rise": [],
          "silent": 8, "flags_added": [("DG", "C4.5"), ("INT", "C4.5")], "flags_removed": [],
          "remaining": 8, "published_ones": {"C4.3": 7, "C4.5": 6},
          "ones_left": {"C4.3": [], "C4.5": ["FALC", "INT"]}, "first": ("CCO", 18.5, 18.0)}


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

    print(f"NEEC rescoring pass, part (b), eighth group: C4.3, C4.5 on the v2.0 clauses ({RECORD})")
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
          f"this group holds exactly the part (b) units of C4.3 and C4.5 ({len(grp)}: "
          + ", ".join(f"{g} {per[g]}" for g in GROUP) + "), every one a corpus 1.0 and none re-estimated before")
    pub = {g: sorted(c for c in vec if vec[c][g] == 1.0) for g in GROUP}
    in_a = {g: sorted(c for (c, k) in prior[0] if k == g) for g in GROUP}
    outside = {g: sorted(c for c in pub[g] if (c, g) not in d28) for g in GROUP}
    check({g: len(v) for g, v in pub.items()} == EXPECT["published_ones"]
          and all(sorted([c for c, k in new if k == g] + in_a[g] + outside[g]) == pub[g] for g in GROUP)
          and sorted(REREAD) == sorted((c, g) for g in GROUP for c in in_a[g])
          and all(prior[0][k]["verdict"] == 0.5 for k in REREAD) and len(REREAD) == EXPECT["reread"]
          and outside == {"C4.3": ["CCO"], "C4.5": []} and sorted(CLASSM) == [(c, g) for g in GROUP for c in outside[g]]
          and len(UNITS) == EXPECT["units"],
          "with part (a)'s, they are every published 1.0 of the two criteria in D28's population (" + "; ".join(
              f"{g} {len(pub[g])} published, part (a) took " + (", ".join(in_a[g]) or "none") for g in GROUP) +
          "); outside it, CCO-PTF-CIP-SZH's C4.3, which the audit coded A on every clause, re-checked here as class M "
          "(reading 3.8); part (a)'s "
          f"{len(REREAD)}, each at 0.5 there, are re-read here on the v2.0 clauses")
    for g in GROUP:
        print(f"  {g}: " + ", ".join(c for c, k in grp if k == g) + "; re-read from part (a): "
              + (", ".join(c for c, k in REREAD if k == g) or "none"))

    def words(t):  # a clause moved to the head of its threshold gains a capital; the words are what must match
        return t[:1].lower() + t[1:]
    same = all(words(v2[g]["definition"]["clauses"][i]) == words(r4.CLAUSES[g][MAP[g][i]][0])
               for g in GROUP for i in range(len(MAP[g])))
    gone = all(len(r4.CLAUSES[g]) == len(MAP[g]) + 1 and DELETED[g] not in MAP[g]
               and words(r4.CLAUSES[g][DELETED[g]][0]) not in [words(t) for t in v2[g]["definition"]["clauses"]]
               for g in GROUP)
    d43 = v2["C4.3"]["definition"]
    check(same and gone and all(len(v2[g]["definition"]["clauses"]) == len(MAP[g]) for g in GROUP)
          and v2["C4.3"]["revision"]["cls"] == "M" and v2["C4.5"]["revision"]["cls"] == "D"
          and d43.get("clause_scope") == SCOPE and d43["pass_threshold"].endswith(SCOPE)
          and "each declared axis" in d43["measurement"] and "median household income" in d43["measurement"]
          and "clause_scope" not in v2["C4.5"]["definition"],
          "v2.0's clauses: C4.3 (class M) keeps the Session 44 clauses 1 and 3 verbatim, deletes the 150% clause, and "
          "adds the declared-axis scope and the household income measure; C4.5 (class D) keeps clauses 1 and 2 "
          "verbatim and deletes residual coercion")
    for g in GROUP:
        for i, t in enumerate(v2[g]["definition"]["clauses"]):
            print(f"  {g} ({i + 1}) {t}  [verbatim; Session 44 clause {MAP[g][i] + 1}]")
        print(f"  {g} deleted: Session 44 clause {DELETED[g] + 1}, {r4.CLAUSES[g][DELETED[g]][0]}")
    print(f"  C4.3 scope: {SCOPE}")

    # [2] Nordic Social Democracy's C4.3 clause 1 ------------------------------------------------------------------
    print("\n[2] NORDIC SOCIAL DEMOCRACY, C4.3: THE IMMIGRANT AXIS (Eurostat, EU-SILC; reading 3.4)")
    rows = ["| Country | Axis | Gap 2018-2020 | Gap 2023-2025 | Change | Ten-edition trend per 5 years | Breaks |",
            "|---|---|---:|---:|---:|---:|---|"]
    meas, deciding = {}, {}
    for axis in ("birth", "citizenship"):
        for c, r in NORDIC[axis].items():
            m = nordic_measures(r)
            meas[(c, axis)] = m
            br = [str(y) for y, x in zip(NORDIC_YEARS, r) if len(x) > 2]
            rows.append(f"| {c} | {'country of birth' if axis == 'birth' else 'citizenship'} | {m['early']:.1f}% | "
                        f"{m['late']:.1f}% | {m['change']:+.1f} | {m['trend']:+.1f} | {', '.join(br) or '—'} |")
    nordic_table = "\n".join(rows)
    print(nordic_table)
    for c in NORDIC["birth"]:
        short = [(c, a) for a in ("birth", "citizenship") if meas[(c, a)]["late"] > LEVEL
                 and meas[(c, a)]["change"] > -RATE and meas[(c, a)]["trend"] > -RATE]
        deciding[c] = short
    rev = all(r[0] > r[1] for a in NORDIC for rr in NORDIC[a].values() for r in rr)
    check(rev and all(deciding[c] for c in deciding),
          "natives and nationals have the higher median in every edition, and in each of the four countries a gap "
          "above 20% (2023-2025 mean) falls by less than 5 points in five years on both measures: " + "; ".join(
              f"{c} by {'birth' if a == 'birth' else 'citizenship'}" for c in deciding for _, a in deciding[c]))
    pick = {c: min(deciding[c], key=lambda x: meas[x]["change"] + meas[x]["trend"]) for c in deciding}
    txt = "; ".join(f"{c} by {'country of birth' if a == 'birth' else 'citizenship'}, {meas[(c, a)]['late']:.1f}% "
                    f"against {meas[(c, a)]['early']:.1f}% ({meas[(c, a)]['change']:+.1f}), trend "
                    f"{meas[(c, a)]['trend']:+.1f}" for c, (_, a) in pick.items())
    reach = {}
    for axis in NORDIC:
        for c, r in NORDIC[axis].items():
            m = meas[(c, axis)]
            if m["late"] <= LEVEL:
                continue
            g = dict(zip(NORDIC_YEARS, (gap(x) for x in r)))
            xs = list(NORDIC_YEARS)
            mx, my = sum(xs) / len(xs), sum(g.values()) / len(xs)
            b = sum((x - mx) * (g[x] - my) for x in xs) / sum((x - mx) ** 2 for x in xs)
            reach[(c, axis)] = None if b >= 0 else mx + (LEVEL - my) / b
    rising = sorted(k for k, y in reach.items() if y is None)
    last = max(y for y in reach.values() if y is not None)
    check(rising == [("Denmark", "citizenship")] and meas[("Denmark", "citizenship")]["change"] < 0 and last < 2055,
          f"on the ten-edition trends every immigrant-axis gap above 20% reaches 20% by {last:.0f} except Denmark's by "
          f"citizenship, whose trend rises ({meas[('Denmark', 'citizenship')]['trend']:+.1f}) while its three-year "
          "mean falls: clause 2 not shown")
    for i, fill in ((0, dict(ROWS=txt)), (1, dict(LAST=f"{last:.0f}",
                                                    DKTREND=f"{meas[('Denmark', 'citizenship')]['trend']:+.1f}"))):
        st, est, src = UNITS[("NSD", "C4.3")]["clauses"][i]
        UNITS[("NSD", "C4.3")]["clauses"][i] = (st, est.format(**fill), src)

    # [3] records --------------------------------------------------------------------------------------------------
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
                   "and its source; no clause is left not estimated")
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
    fall_back = [k for k in REREAD if UNITS[k]["verdict"] < prior[0][k]["verdict"]]
    check(stand == sorted(EXPECT["stand"]) and points_b == EXPECT["points_b"] and rise == EXPECT["rise"]
          and not fall_back,
          f"of the part (b) units {sum(1 for k in new if k in stand)} stand ("
          + ", ".join(f"{c} {k}" for c, k in stand) + f") and {sum(1 for k in new if k not in stand)} become 0.5 "
          f"({f1(points_b)} points); every C4.3 unit becomes 0.5; part (a)'s re-read units neither fall nor rise")
    check(all(UNITS[k]["verdict"] == 0.5 and vec[k[0]][k[1]] == 1.0 for k in CLASSM),
          "CCO-PTF-CIP-SZH's C4.3, re-checked as class M on the same readings, becomes 0.5 (reading 3.8)")
    wflag = [k for k, r in UNITS.items() if r["flag"] and r["verdict"] in r["flag"][0]]
    check(not wflag, "every flag names alternatives other than the scored value", str(wflag))
    reg = {(u[0], u[1]): u[2] for u in r4.UNITS}
    code = {(c, k, i): reg[(c, k)][MAP[k][i]] for (c, k) in UNITS for i in range(len(MAP[k]))}
    departs = sorted(x for x, ch in code.items() if x[2] not in SCOPED[x[1]] and x[:2] not in REREAD
                     and ch == "A" and UNITS[x[:2]]["clauses"][x[2]][0] != "C")
    carried_c45 = sorted(x for x, ch in code.items() if x[1] == "C4.5" and x[:2] not in REREAD and ch == "A")
    check(not departs and all(UNITS[x[:2]]["clauses"][x[2]][2] == AUD for x in carried_c45),
          f"no departure from the audit's A codes on C4.5: its {len(carried_c45)} A codes in this group's part (b) "
          "units are carried as cleared on the unit's own text")
    re_a = sorted(x for x, ch in code.items() if x[2] in SCOPED[x[1]] and ch == "A")
    carried = sorted(x for x in re_a if UNITS[x[:2]]["clauses"][x[2]][0] == "C")
    estimated = sorted(x for x in re_a if x not in carried)
    check(carried == sorted(REREAD_CARRIED) and estimated == sorted(REREAD_ESTIMATED),
          f"the audit coded A {len(re_a)} clauses v2.0 places under C4.3's scope and measure: {len(carried)} carried, "
          f"{len(estimated)} estimated after re-reading (reading 3.2)")
    silent = {(c, k, i) for (c, k) in new for i in range(len(MAP[k])) if code[(c, k, i)] == "S"}
    est_status = {}
    for c, k, i in sorted(silent):
        st = UNITS[(c, k)]["clauses"][i][0]
        est_status[st] = est_status.get(st, 0) + 1
    check(len(silent) == EXPECT["silent"],
          f"the audit coded {len(silent)} v2.0 clauses of this group's part (b) units silent, and every one is "
          "estimated here: " + ", ".join(f"{STATUS[s]} {n}" for s, n in sorted(est_status.items())))
    exit_units = [k for k in new if k[1] == "C4.5"]
    check(all(code[(c, k, 1)] == "S" for c, k in exit_units)
          and all(UNITS[k]["verdict"] == (1.0 if UNITS[k]["clauses"][1][0] == "C" else 0.5) for k in exit_units),
          "every C4.5 unit was silent on exit rights, and clause 2 alone decides each C4.5 verdict (reading 3.6)")

    # [5] reach ----------------------------------------------------------------------------------------------------
    print("\n[5] REACH (D28(c)) AND EXTENSIONS (D31)")
    now_r = sorted((c, k, i) for (c, k), r in UNITS.items() for i, (st, _, _) in enumerate(r["clauses"]) if st == "R")
    was_r = sorted(x for x in r4.REACH if (x[0], x[1]) in UNITS)
    check(now_r == was_r == [("UBI", "C4.5", 0)] and prior[0][("UBI", "C4.5")]["clauses"][0][0] == "R",
          "one clause of this group is out of reach, Universal Basic Income's C4.5 clause 1, as the audit coded it and "
          "part (a) confirmed; v2.0 keeps the clause verbatim")

    # [6] flags ----------------------------------------------------------------------------------------------------
    print("\n[6] FLAG REGISTERS (against the summary blocks, cumulatively with parts (a) to (b7) and 48.3)")
    blocks = rs.blocks_by_code()
    had = {(c, f["criterion"]): f for c, b in blocks.items() for f in b["flags"]}

    def changes(units):
        add = sorted(k for k, r in units.items() if r["flag"] and k not in had)
        rem = sorted(k for k, r in units.items() if k in had and r["verdict"] in had[k]["alternatives"]
                     and not r["flag"])
        return add, rem
    added, removed = changes(new)
    kept = sorted(k for k in new if k in had)
    kept_a = all(UNITS[k]["flag"] and UNITS[k]["flag"][0] == prior[0][k]["flag"][0] if prior[0][k]["flag"]
                 else not UNITS[k]["flag"] for k in REREAD)
    check(added == sorted(EXPECT["flags_added"]) and removed == sorted(EXPECT["flags_removed"]) and not kept
          and kept_a,
          f"flags added {len(added)} ({', '.join(f'{c} {k}' for c, k in added)}); removed {len(removed)}; no part (b) "
          "unit of this group carried a flag; part (a)'s re-read units keep their flags")
    merged, part_of = {}, {}
    for (tag, _, _, sess), part in zip(PRIOR, prior):
        merged.update(part)
        part_of.update({k: (tag, sess) for k in part})
    before = dict(merged)
    merged.update(UNITS)
    part_of.update({k: THIS for k in UNITS})
    a0, _ = changes(before)
    adds, rems = changes(merged)
    moved_e = sorted({k[0] for k in adds + rems})
    flag_line = (f"Flags added in this group: {len(added)}; removed: {len(removed)}. Flags added by the pass so far: "
                 f"{len(adds)} (against {len(a0)} before this group); removed: {len(rems)}. Across the pass so far, "
                 f"{len(moved_e)} entries' flag registers change ({', '.join(moved_e)}).")
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
    rem_line = (f"Left for part (b): {len(left_units)} D28 units (" +
                ", ".join(f"{k} {perc[k]}" for k in cids if k in perc) + "), which finish it.")
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
          and [k for k in emptied if emptied[k] == THIS[0]] == ["C4.3"],
          f"no entry scores 1.0 on {len(emptied)} criteria after this group: C4.3 joins the eight emptied before")
    ones_line = ("After this group no entry scores 1.0 on C4.3 (7 published), and C4.5 keeps " + str(len(ones["C4.5"]))
                 + " (" + ", ".join(ones["C4.5"]) + "; 6 published). Every criterion had a 1.0 in the published "
                 "corpus; after the pass so far no entry scores 1.0 on " + str(len(emptied)) + " of them: "
                 + ", ".join(f"{k} (emptied in part {emptied[k]})" for k in cids if k in emptied) + ".")
    print("  " + ones_line)
    rb, rp, rn = rs.ranks(base["total"]), rs.ranks(mp["total"]), rs.ranks(after["total"])
    rows = ["| Entry | Published (rank) | After 48.3 (rank) | After this group (rank) | Change here | Failures | Tier | "
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
          f"first place: {first[0]}, {f1(mp['total'][first[0]])} after 48.3, "
                                                 f"{f1(after['total'][first[0]])} now")
    dom_line = (f"After this group the corpus has {len(pn)} dominance pairs against {len(pp)} after 48.3 (new: " +
                (", ".join(f"{a}>{b}" for a, b in gained) or "none") + "; lost: " +
                (", ".join(f"{a}>{b}" for a, b in lost) or "none") + f"), and its frontier holds {len(fn)} entries "
                f"against {len(fp)} (" + ", ".join(c for c in order if c in fn) + f"). First place: {first[0]}, "
                f"{f1(mp['total'][first[0]])} after 48.3, {f1(after['total'][first[0]])} now. Across the pass so far "
                f"{n_all} units have been re-estimated, each counted once: {st_all} stand and {n_all - st_all} are at "
                f"0.5 ({f1(pts_all)} points).")
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
    c45 = next(x for x in crit if x["id"] == "C4.5")["anchors"]["bands"]["1.0"]["examples"]
    check(here == ["C4.3's 1.0 example, CCO (part (b8))"] and len(hits) == 12 and len(empty) == 9
          and ("C4.3", "1.0") in empty and [code_of[x["system"]] for x in c45] == ["PE"]
          and vec["PE"]["C4.5"] == 0.0,
          f"this group moves one anchor example, C4.3's 1.0, CCO-PTF-CIP-SZH ({len(hits)} across the pass), and C4.3's "
          f"1.0 band joins the {len(empty) - 1} left with no corpus unit; C4.5's 1.0 example names Participatory "
          "Economics, which the corpus scores 0.0 on C4.5 (the misattribution Handoff 30 records)")
    anchor_line = ("Anchor examples citing a unit the pass moves: " + "; ".join(hits) + ". Bands whose example the pass moves "
                   "and which no corpus unit then scores at their value: " + ", ".join(f"{c}'s {b}" for c, b in empty) + ".")
    print("  " + anchor_line)

    # [10] the record ----------------------------------------------------------------------------------------------
    print(f"\n[10] THE RECORD'S TABLES (generated here; {RECORD} must contain them verbatim)")
    unit_order = [(u[0], u[1]) for u in r4.UNITS if (u[0], u[1]) in UNITS]
    unit_order = ([k for k in unit_order if k not in REREAD and k[1] == "C4.3"]
                  + [k for k in unit_order if k not in REREAD and k[1] == "C4.5"]
                  + [k for k in unit_order if k in REREAD])
    t = {}
    rows = ["| Entry | Criterion | Clauses | Verdict | Flag |", "|---|---|---|---|---|"]
    for key in unit_order:
        rec = UNITS[key]
        fl = f"alternative {rs.fmt_alts(rec['flag'][0])}" if rec["flag"] else ""
        was = "0.5 (part (a))" if key in REREAD else "1.0 (class M)" if key in CLASSM else "1.0"
        rows.append(f"| {key[0]} | {key[1]} | {' '.join(s for s, _, _ in rec['clauses'])} | "
                    f"{was} → {f1(rec['verdict'])} | {fl} |")
    t["summary"] = "\n".join(rows)
    for key in unit_order:
        rec, (cd, k) = UNITS[key], key
        was = "0.5 (part (a))" if key in REREAD else "1.0 (class M)" if key in CLASSM else "1.0"
        head = f"#### {cd} {k} {v2[k]['name']}: {was} → {f1(rec['verdict'])}"
        if rec["flag"]:
            head += " — flagged as contestable"
        lines = [head, "", "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (st, est, src) in enumerate(rec["clauses"]):
            lines.append(f"| {i + 1} | {v2[k]['definition']['clauses'][i]} | {STATUS[st]} | {est} | {src} |")
        if rec["flag"]:
            lines += ["", f"*Flag:* alternative {rs.fmt_alts(rec['flag'][0])}: {rec['flag'][1]}."]
        if rec["note"]:
            lines += ["", f"*Note:* {rec['note']}."]
        t[f"unit {cd} {k}"] = "\n".join(lines)
    t["nordic"], t["consequences"], t["dominance"], t["remaining"] = nordic_table, cons_table, dom_line, rem_line
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
    print("\nRESCORING PART (B), EIGHTH GROUP, COMPUTED." if ok else
          "\nRESCORING PART (B), EIGHTH GROUP: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
