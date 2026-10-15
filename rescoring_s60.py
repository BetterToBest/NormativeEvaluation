#!/usr/bin/env python3
"""
rescoring_s60.py -- NEEC rescoring pass, stage 2, group 2.7: C1.4 Automation Resilience, class I
================================================================================================
Session 60. The second class I group, written on the shared module (pass_common.py, decision 52.5). v2.0 keeps C1.4's
clauses and bar ("Poverty <8% and aggregate demand >85% baseline in each of the 30%, 50% and 70% displacement
scenarios") and names the measure: poverty at the Societal Poverty Line, as in C1.1, and aggregate demand as real final
consumption expenditure against the pre-displacement baseline, in each of three scenarios displacing 30%, 50% or 70% of
baseline paid working hours; for a design, its own model of the three scenarios (criteria.json; NEEC_Criteria_v2_s45.md).
The 20 units the pass had not re-estimated are read clause by clause, from the evidence cache Session 59 built
(evidence_cache_s59.py, evidence_cache/C1.4/) and the two extracts this session added to it (SOURCES below).
Fully Automated Luxury Communism's and Participatory Economics' units (part (b4)) and CCO-PTF-CIP-SZH's (group 2.5) are
not re-read. Readings: NEEC_Rescoring_s60.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry not yet re-estimated on C1.4, each against its published score; which rise, fall
      or hold; the 0.0s and their reasons
  [2] the cache: every file the readings use by digest (Session 59's index and extracts, this session's two), every
      passage quoted found in its file, and each unit's published rationale located by the index and unchanged
  [3] the measure (decision 60.1): no unit's sources state an estimate of either clause in any scenario; the clauses
      a mechanism does not govern are out of reach; final consumption expenditure counts general government's
  [4] the flags
Usage: python3 rescoring_s60.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, the files of CACHE named below,
                                             the scoring documents the index names, NEEC_Rescoring_s60.md; writes
                                             nothing)
       python3 rescoring_s60.py --tables   (prints the generated tables as JSON, for the record)
Prints file names and summaries only. Deterministic offline; it reads no network.
"""
import hashlib
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD, CRIT = "(2.7)", "NEEC_Rescoring_s60.md", "C1.4"
CACHE = "evidence_cache/C1.4/"
UNITS = {}
GENERATED = {}


def U(code, verdict, c1, c2, flag=None, note="", zero=None):
    """One unit of C1.4. c1, c2: (status, estimate, source) for the two v2.0 clauses. flag: (alternative, reading).
    zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[c1, c2], flag=flag, note=note, zero=zero)


# ---- the cache (Session 59's files and the two this session added; md5s as built) ----------------------------------
MD5 = {"index.json": None,   # its digest is not fixed: Session 59's script verifies it; here each entry is checked
       "wb_pip_methods.txt": "578656a0c597512ffe3c1054254954aa",
       "wb_final_consumption.txt": None, "wb_final_consumption_kd.txt": None,
       "wb_fce_kd_metadata.txt": "ce048d00c93ea15f3e420d436178d4f4",
       "integral_wp_v01_extract.txt": "41fa8a9a7f8782a136910ffb4a7931b1"}
SOURCES = {
    "wb_fce_kd_metadata.txt": "World Bank, World Development Indicators, NE.CON.TOTL.KD, 'Final consumption expenditure "
                              "(constant 2015 US$)', the indicator's source note (api.worldbank.org, retrieved "
                              "2026-10-15)",
    "integral_wp_v01_extract.txt": "Joseph, INTEGRAL: Technical White Paper v0.1 (integralcollective.io, December 2025; "
                                   "PDF md5 a6defc9a, retrieved 2026-10-15), five passages",
}
QUOTES = {
    "wb_fce_kd_metadata.txt": ["Final consumption expenditure can be measured for households, general government"],
    "integral_wp_v01_extract.txt": [
        "fewer labor hours are needed to maintain stable access to essentials",
        "ensuring that essentials remain accessible regardless of age or ability",
        'raise ValueError("insufficient ITC balance")',
        "Access to food, shelter, tools, care, and shared resources emerges from participation",
        "We seek critical readers willing to stress-test the logic",
    ],
}

# ---- shared phrases ------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
NOMODEL = ("no model or estimate of poverty on the Societal Poverty Line under a 30%, 50% or 70% displacement of paid "
           "hours is stated or cited, and none was located")
NODEM = ("no model or estimate of real final consumption expenditure against a pre-displacement baseline in any of the "
         "three scenarios is stated or cited, and none was located")
R_IF = ("the mechanism prices and structures credit; it governs neither household income nor final consumption, and "
        "the host economy's are not credited to it (protocol 3.2)")
FCE = "World Bank WDI, NE.CON.TOTL.KD, source note (" + CACHE + "wb_fce_kd_metadata.txt)"
WP = ("Joseph, INTEGRAL: Technical White Paper v0.1 (December 2025; PDF md5 a6defc9a), sections 3, 6 and 11.8 and "
      "the closing invitation (" + CACHE + "integral_wp_v01_extract.txt)")
PEER = ("the configuration's unemployment insurance is a time-limited buffer of the kind Singapore's Jobseeker Support "
        "is, and Singapore's unit holds 0.5 on it with training and fiscal capacity, which this configuration also has")

# ---- the units (readings in NEEC_Rescoring_s60.md, section 3) -------------------------------------------------------
U("SQ", 0.0,
  ("U", "the rationale asserts a deflationary spiral at 30% displacement without a model; " + NOMODEL,
   f"{REP}System 1, C1.4"),
  ("U", NODEM, f"{REP}System 1, C1.4"),
  flag=("0.5: " + PEER, "3.4"),
  zero="no structural mechanism addresses the criterion: income and demand run through paid work, and the "
       "configuration's support for the unemployed is insurance against cyclical job loss, not a provision for paid "
       "work becoming optional; the 0.0 band's anchor")
U("NSD", 0.5,
  ("U", "generous unemployment benefits and retraining are a buffer; the rationale says the configuration cannot "
        "sustain 50-70% displacement, without a model; " + NOMODEL, f"{REP}System 2, C1.4"),
  ("U", NODEM, f"{REP}System 2, C1.4"),
  note="the 0.5 band's anchor example; it holds")
U("CPS", 0.5,
  ("U", "employment guaranteed regardless of productivity separates income from market demand for labour; " + NOMODEL,
   f"{REP}System 3, C1.4"),
  ("U", NODEM, f"{REP}System 3, C1.4"))
U("MS", 0.5,
  ("U", "cooperatives can reduce hours rather than shed members and distribute automation's gains to them, under "
        "competitive pressure to automate; " + NOMODEL, f"{REP}System 4, C1.4"),
  ("U", NODEM, f"{REP}System 4, C1.4"))
U("LM", 0.0,
  ("U", NOMODEL, f"{REP}System 5, C1.4"),
  ("U", NODEM, f"{REP}System 5, C1.4"),
  zero="no structural mechanism addresses the criterion: the design removes the safety nets that exist and leaves "
       "income and demand to paid work alone")
U("MMT", 0.5,
  ("U", "the Job Guarantee keeps income tied to (guaranteed) work; the rationale's 'can maintain 30% displacement but "
        "fails at 50-70%' is a judgement, not an estimate; " + NOMODEL, f"{REP}System 6, C1.4"),
  ("U", NODEM, f"{REP}System 6, C1.4"))
U("UBI", 0.5,
  ("U", "an unconditional transfer is an explicit mechanism decoupling income from employment; the rationale's 'scales "
        "naturally with automation' is a design statement, not a level of poverty under a stated scenario; " + NOMODEL,
   f"{REP}System 7, C1.4"),
  ("U", "unconditional transfers sustain household spending, as the rationale says; " + NODEM, f"{REP}System 7, C1.4"),
  note="published 1.0 on the design's logic; under D28 silence is not clearance (protocol 2.3(b)), as parts (b4) and "
       "group 2.5 read Fully Automated Luxury Communism's, Participatory Economics' and CCO-PTF-CIP-SZH's 1.0s; a "
       "correction (reading 3.2)")
U("DG", 0.5,
  ("U", "reduced hours and work-sharing could absorb displacement; no mechanism for income as labour becomes optional is "
        "specified; " + NOMODEL, f"{REP}System 8, C1.4"),
  ("U", NODEM, f"{REP}System 8, C1.4"))
U("SC", 0.0,
  ("U", NOMODEL, f"{REP}System 9, C1.4"),
  ("U", NODEM, f"{REP}System 9, C1.4"),
  flag=("0.5, on the host economy the reform keeps, as Status Quo's flag: " + PEER, "3.4"),
  zero="no structural mechanism addresses the criterion: stakeholder governance leaves firms automating to stay "
       "competitive and adds nothing for income distribution or demand as automation advances; the 0.0 band's "
       "description")
U("INT", 0.5,
  ("U", "the white paper states that essentials remain accessible 'regardless of age or ability' and that automation "
        "lowers the labour needed for them, but access still 'emerges from participation' and redemption needs an ITC "
        "balance; it states no level of poverty under any displacement scenario and invites readers to stress-test "
        "it; " + NOMODEL, f"{REP}System 13, C1.4; {WP}"),
  ("U", "production planned on needs assessed through CDS, not on purchasing power, so demand does not require "
        "employment; " + NODEM, f"{REP}System 13, C1.4; {WP}"),
  note="read on the design's own white paper as group 2.6 read C5.2; it answers the rationale's question only in part "
       "(reading 3.5)")
U("GEO", 0.5,
  ("U", "an LVT-funded dividend would capture automation's surplus to the extent it capitalises into land values, an "
        "assumption less secure for AI-era capital; " + NOMODEL, "NEEC_Georgism_LVT_scoring_scratch.md, C1.4"),
  ("U", NODEM, "NEEC_Georgism_LVT_scoring_scratch.md, C1.4"))
U("MC", 0.5,
  ("U", "mutual credit sustains exchange without wage income, but a displaced member needs something other members "
        "want; " + NOMODEL, "NEEC_MutualCredit_LETS_scoring_scratch.md, C1.4"),
  ("U", NODEM, "NEEC_MutualCredit_LETS_scoring_scratch.md, C1.4"))
U("DE", 0.0,
  ("U", "the social foundation is a measurement target, not a provision; " + NOMODEL,
   "NEEC_DoughnutEconomics_scoring_scratch.md, C1.4"),
  ("U", NODEM, "NEEC_DoughnutEconomics_scoring_scratch.md, C1.4"),
  zero="no structural mechanism addresses the criterion: automation is named as a concern and met with no "
       "income-distribution, contribution-recognition or demand-maintenance mechanism in the framework or its "
       "implementations")
U("UBS", 0.5,
  ("U", "free provision of housing, food, healthcare, education, transport and information lowers the wage income needed "
        "to avoid poverty; " + NOMODEL, "NEEC_UniversalBasicServices_scoring_scratch.md, C1.4"),
  ("U", "the rationale finds no mechanism for demand because the services pay no cash; on the measure v2.0 names, final "
        "consumption expenditure includes general government's, so the services themselves count toward it; " + NODEM,
   f"NEEC_UniversalBasicServices_scoring_scratch.md, C1.4; {FCE}"),
  note="the rationale's demand-side finding is not borne out on the measure; the verdict is unchanged because neither "
       "clause is shown (reading 3.3)")
U("SWF", 0.5,
  ("U", "the fund's revenue does not erode with the wage base, but no payout scales with displacement (Norway's budget "
        "transfer; Alaska's fixed dividend); " + NOMODEL,
   "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.4"),
  ("U", NODEM, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C1.4"))
U("CN", 0.5,
  ("U", "the state directs state-owned employers to absorb workers and has begun retraining for AI displacement; dibao "
        "reaches under 3% of the population; " + NOMODEL, "NEEC_StateCapitalism_China_scoring_scratch.md, C1.4"),
  ("U", "directed investment can sustain demand, as the rationale says (C3.1); " + NODEM,
   "NEEC_StateCapitalism_China_scoring_scratch.md, C1.4"))
U("SG", 0.5,
  ("U", "Jobseeker Support pays up to S$6,000 over six months, conditional on job search, with training and reserve-"
        "funded wage subsidies; " + NOMODEL, "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.4"),
  ("U", NODEM, "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C1.4"),
  flag=("0.0: a six-month conditional payment is insurance against cyclical job loss, as Status Quo's unemployment "
        "insurance is, and the foreign-workforce margin is an exclusion, not a decoupling", "3.4"))
U("QA", 0.5,
  ("U", "citizens' incomes rest on a hydrocarbon rent automation would not touch, through state jobs; non-citizens, "
        "most of the population the protocol counts (3.2), have no mechanism beyond departure; " + NOMODEL,
   "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2"),
  ("U", NODEM, "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C1.4"),
  note="a buffer covering part of the relevant population is the 0.5 band (protocol 2.1)")
U("IF", 0.0,
  ("R", R_IF, "NEEC_IslamicFinance_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2"),
  ("R", R_IF, "NEEC_IslamicFinance_scoring_scratch.md, C1.4; SCORING_PROTOCOL.md 3.2"),
  flag=("0.5, the published flag: profit-and-loss-sharing investment accounts read as a non-wage income channel that "
        "persists under displacement", "3.6"),
  zero="no structural mechanism addresses the criterion: changing how credit is priced leaves distribution running "
       "through wage labour, as for Status Quo")
U("OS", 0.5,
  ("U", "a commons share is not conditioned on employment and its non-wage income is observed, for members of a bounded "
        "resource; " + NOMODEL, "NEEC_Ostrom_Commons_scoring_scratch.md, C1.4"),
  ("U", "no aggregate-demand mechanism, as the rationale says; " + NODEM, "NEEC_Ostrom_Commons_scoring_scratch.md, C1.4"),
  flag=("0.0, the published flag: a bounded subsistence base for a minority cannot hold poverty under 8% economy-wide "
        "at 70% displacement", "3.6"))

EXPECT = {"rise": [], "fall": ["UBI"], "zero": ["SQ", "LM", "SC", "DE", "IF"], "ones": [],
          "flags": {"SQ": "3.4", "SC": "3.4", "SG": "3.4", "IF": "3.6", "OS": "3.6"},
          "before": ["FALC", "PE", "CCO"], "out_of_reach": ["IF"]}


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    with redirect_stdout(io.StringIO()):
        idx = [t for t, _, _, _ in pc.PARTS].index(TAG)
        p = pc.Pass(upto=idx)
    print(f"NEEC rescoring pass, stage 2, group 2.7: C1.4 Automation Resilience, class I ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{len(MD5)} files of {CACHE}, the scoring documents its index names, {RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(p.part_of[(c, CRIT)] for c in before)}) and are not re-read")
    check(p.v2[CRIT]["revision"]["cls"] == "I" and len(p.v2[CRIT]["definition"]["clauses"]) == 2,
          f"{CRIT} is class I with two clauses in v2.0")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group raises {len(rise)}, lowers {len(fall)} ({', '.join(fall)}) and holds {len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 == pub[c] for c in zeros),
          f"{len(zeros)} units are 0.0, each held on a stated whole-criterion reason (protocol 2.1): {', '.join(zeros)}")
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    after = [c for c in p.order if (UNITS.get((c, CRIT)) or p.merged.get((c, CRIT)) or {}).get("verdict") == 1.0]
    check(ones == EXPECT["ones"] and not after,
          f"no unit clears either clause, so none is 1.0; after this group no entry is at 1.0 on {CRIT}")

    print(f"\n[2] THE CACHE ({CACHE}; files by digest, every passage quoted found, every rationale located)")
    for name, want in MD5.items():
        path = os.path.join(HERE, CACHE, name)
        raw = open(path, "rb").read() if os.path.isfile(path) else b""
        if want is None:
            check(bool(raw), f"{name}: present (Session 59's; its digest is held in index.json or by evidence_cache_s59.py)")
            continue
        txt = raw.decode("utf-8")
        lost = [q for q in QUOTES.get(name, []) if q not in txt]
        check(hashlib.md5(raw).hexdigest() == want and not lost,
              f"{name}: md5 {want[:8]}" + (f", {len(QUOTES[name])} passage(s) quoted" if name in QUOTES else ""),
              ", ".join(lost))
    idx_ = json.load(open(os.path.join(HERE, CACHE, "index.json"), encoding="utf-8"))
    src = idx_["sources"]
    check(all(hashlib.md5(open(os.path.join(HERE, CACHE, s["file"]), "rb").read()).hexdigest() == s["extract_md5"]
              for s in src.values() if s.get("extract_md5")),
          f"Session 59's {sum(1 for s in src.values() if s.get('extract_md5'))} extracts match the index's digests "
          f"({', '.join(k for k, s in src.items() if not s.get('extract_md5'))} not cached)")
    bad = []
    for c in mine:
        u = idx_["units"].get(c)
        if u is None or u["score"] != pub[c]:
            bad.append(c)
            continue
        lines = open(os.path.join(HERE, u["file"]), encoding="utf-8").read().split("\n")
        if not lines[u["line"] - 1].lstrip("# *").startswith("C1.4 Automation Resilience"):
            bad.append(c)
    check(sorted(idx_["units"]) == sorted(mine) and not bad,
          f"the index names the same {len(mine)} units, each at its published score, and each rationale's heading is "
          "where the index puts it", ", ".join(bad))

    print("\n[3] THE MEASURE (decision 60.1)")
    st = [s for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"]]
    check(set(st) <= {"U", "R"} and st.count("U") + st.count("R") == 2 * len(mine),
          f"no unit's sources state either clause's quantity in any of the three scenarios: {st.count('U')} clauses "
          f"not shown, {st.count('R')} out of reach")
    reach = [c for c in mine if any(s == "R" for s, _, _ in UNITS[(c, CRIT)]["clauses"])]
    check(reach == EXPECT["out_of_reach"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 for c in reach),
          "out of reach for the one mechanism governing neither quantity (Islamic Finance; protocol 3.2), held at 0.0 "
          "on its whole-criterion reason")
    ubs = UNITS[("UBS", CRIT)]["clauses"][1]
    check("general government" in ubs[1] and "wb_fce_kd_metadata.txt" in ubs[2],
          "final consumption expenditure, v2.0's demand measure, includes general government's (WDI source note): "
          "carried in Universal Basic Services' clause 2")

    print("\n[4] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.6", "After group 2.7")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    f1 = pc.f1
    rows_ = ["| Entry | Published | Clause 1 | Clause 2 | Verdict | Flag |", "|---|---:|---|---|---:|---|"]
    for c in mine:
        r = UNITS[(c, CRIT)]
        rows_.append(f"| {c} | {f1(pub[c])} | " + " | ".join(pc.STATUS[x[0]] for x in r["clauses"]) +
                     f" | {f1(r['verdict'])} | {('toward ' + r['flag'][0][:3]) if r['flag'] else ''} |")
    t["summary"] = "\n".join(rows_)
    for c in mine:
        r = UNITS[(c, CRIT)]
        lines = [f"#### {c} {CRIT} {p.v2[CRIT]['name']}: {f1(pub[c])} → {f1(r['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (s, est, src_) in enumerate(r["clauses"]):
            lines.append(f"| {i + 1} | {p.v2[CRIT]['definition']['clauses'][i]} | {pc.STATUS[s]} | {est} | {src_} |")
        if r["zero"]:
            lines += ["", f"*0.0 (protocol 2.1):* {r['zero']}."]
        if r["flag"]:
            lines += ["", f"*Flag (reading {r['flag'][1]}):* toward {r['flag'][0]}."]
        if r["note"]:
            lines += ["", f"*Note:* {r['note']}."]
        t[f"unit {c}"] = "\n".join(lines)
    GENERATED.clear()
    GENERATED.update(t)
    if "--tables" in sys.argv[1:]:
        sys.stdout = sys.__stdout__
        print(json.dumps(t, ensure_ascii=False))
        return 0
    rec = open(os.path.join(HERE, RECORD), encoding="utf-8").read() if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in rec]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING STAGE 2, GROUP 2.7, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.7: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
