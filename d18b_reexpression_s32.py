#!/usr/bin/env python3
"""
d18b_reexpression_s32.py -- NEEC decision D18(b): Ostrom-style commons governance's flag register, re-expressed
===============================================================================================================
Session 32. Protocol 3.4(b) deferred one question to the pilot replication: whether the twenty flags of
Ostrom-style commons governance, most of which its own document says turn on one scope question, should be
re-expressed -- scope questions moved out of the register into scenarios (3.4, 6.5), doubts kept as flags.
The pilot is back (NEEC_OstromCommons_replication_record.md). This script records the decision's proposal and
computes its consequences, and those of decision D26 (the C3.2 anchor) taken with it. It changes no file and
no score.

THE TEST (proposed as a new paragraph of protocol 3.4). A flag's alternative reading is a SCOPE QUESTION when it
  (i)  reads the criterion's threshold against a population, domain or frame other than the one the entry's
       declared population rule fixes (3.2) -- for a mechanism, the resource or membership it governs in place
       of the economy-wide population; or
  (ii) counts an adjacent instrument, programme or extension in or out of the mechanism's boundary.
A scope question is reported as a scenario and leaves the register. An alternative reading that joins such a
clause to a doubt about the evidence or its interpretation stays a flag if the doubt alone, the scope clause set
aside, reaches the alternative value -- and stays a flag when the text does not settle whether it does: a
register is not narrowed on an unsettled reading.

The test is applied to each flag's OWN stated alternative reading, quoted from the document (each phrase is
located exactly once), not to the document's summary claim that most flags turn on the scope question. For
every flag the script also prints what the blind replication did on that criterion, as independent evidence.

It then computes, from the canonical block with the reclassified flags removed: the register, the joint
readings (the two extremes, decision D16's default, since the document's readings A and C were named for the
scope question), the D13 measure and the enumeration; the scenarios the removed flags become; the entry's
position in the corpus by the D13 order (protocol 6.4) and by flag count; the sensitivity of each result to the
two borderline classifications; and the replication's own register under the same test.

Usage: python3 d18b_reexpression_s32.py      (canonical layout: neec_entry.py, the canonical script, the CSV,
                                              the eleven scoring documents and the replication document)
Prints file names only. Deterministic.
"""
import copy
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import neec_entry as NE  # noqa: E402

OS_DOC = "NEEC_Ostrom_Commons_scoring_scratch.md"
IF_DOC = "NEEC_IslamicFinance_scoring_scratch.md"
REPL_DOC = "NEEC_OstromCommons_replication_scoring.md"
ELEVEN = ("NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
          "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
          "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "NEEC_StateCapitalism_China_scoring_scratch.md",
          "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
          "NEEC_StateCapitalism_Qatar_scoring_scratch.md", IF_DOC, OS_DOC)

DOUBT, BOUNDARY, POPULATION, FRAME = "doubt", "scope: boundary (ii)", "scope: population (i)", "scope: frame (i)"
# criterion -> (class, the deciding phrase of the document's stated alternative reading, note)
CLASSIFICATION = {
    "C1.1": (DOUBT, "a resource-tenure regime is not a poverty mechanism at all", ""),
    "C1.2a": (DOUBT, "a collectively held corpus managed on members' behalf is wealth-building in substance", ""),
    "C1.2b": (DOUBT, "on the design reading, which is the basis on which Mutual Credit / LETS scored 1.0 here", ""),
    "C1.3": (BOUNDARY, "community land trusts are an application of the governance form to land rather than part "
                       "of the scored mechanism", ""),
    "C1.4": (DOUBT, "a bounded subsistence base for a minority of the population cannot hold poverty below 8% "
                    "economy-wide", "reads the threshold against the declared, economy-wide population"),
    "C1.5": (DOUBT, "principle 8's nested enterprises could in principle tile a whole population",
             "the same population; a claim about the design's capacity"),
    "C2.2": (DOUBT, "a subsistence commons is unconditional *relative to the labour market*", ""),
    "C2.4": (DOUBT, "the closest call in Domain 2", ""),
    "C2.5": (DOUBT, "a subsistence-dependent member forfeits the livelihood base on exit", ""),
    "C3.1": (POPULATION, "the coverage clause should be read against the population the institution governs rather "
                         "than the national population", ""),
    "C3.2": (DOUBT, "a real household-level hedge even though it is not a price-level instrument", ""),
    "C3.3": (DOUBT, "Alternative if resolved the other way: 1.0** — on the weight of the survival record.", ""),
    "C3.5": (FRAME, "reading externalisation against the governed resource rather than against the wider economy",
             "joined to a doubt (the apparatus's strength) that does not reach 1.0 alone: the section says the "
             "fourth clause is where it breaks"),
    "C4.1": (DOUBT, "the criterion also carries a debt-to-GDP clause and an absolute-carbon clause", ""),
    "C4.2": (FRAME, "is what ecological compliance means for a resource-governance mechanism",
             "the evidence alone does not reach the economy-wide threshold"),
    "C4.3": (DOUBT, "quotas are an external correction rather than part of the mechanism",
             "BORDERLINE: a boundary clause (ii) joined to a doubt; kept, because the blind replication reached the "
             "alternative, 0.0, on the doubt alone"),
    "C4.4": (DOUBT, "cannot be said to distribute power", ""),
    "C4.5": (DOUBT, "relocates extraction rather than eliminating it", ""),
    "C5.2": (DOUBT, "national forestry statutes are implementations of policy rather than of the scored mechanism",
             "BORDERLINE: a boundary clause (ii) joined to a doubt ('the governing fact'); kept, because the text "
             "does not settle whether the doubt alone reaches 0.0"),
    "C5.4": (DOUBT, "on the weight of the survival record and the breadth of the ideological appeal", ""),
}
SCENARIO_OF = {POPULATION: "resource-frame", FRAME: "resource-frame", BOUNDARY: "land-trusts-out"}
SCENARIO_LABEL = {"resource-frame": "thresholds read against the governed resource and its members, not the "
                                    "economy-wide population",
                  "land-trusts-out": "community land trusts counted out of the mechanism's boundary"}
BORDERLINE = ("C4.3", "C5.2")
F1 = NE.fmt


def blocks_of(name):
    return NE.blocks_in_markdown(open(os.path.join(HERE, name), encoding="utf-8").read())


def reexpress(b, scope_crits):
    """The block with the flags in scope_crits moved out of the register into scenarios; readings = D16 default."""
    r = copy.deepcopy(b)
    fl = {f["criterion"]: f for f in b["flags"]}
    r["flags"] = [f for f in b["flags"] if f["criterion"] not in scope_crits]
    up, down = NE.extremes(r) if r["flags"] else ({}, {})
    r["joint_readings"] = [{"id": "scored", "label": "as scored", "basis": "scored", "resolve": {},
                            "result": NE.result(b["vector"])}]
    if r["flags"]:
        r["joint_readings"] += [
            {"id": "up", "label": "every call resolved upward", "basis": "extremes", "resolve": up,
             "result": NE.result(NE.applied(b["vector"], up))},
            {"id": "down", "label": "every call resolved downward", "basis": "extremes", "resolve": down,
             "result": NE.result(NE.applied(b["vector"], down))}]
    groups = {}
    for c in sorted(scope_crits, key=NE.CRITS.index):
        cls = CLASSIFICATION[c][0] if c in CLASSIFICATION else BOUNDARY
        groups.setdefault(SCENARIO_OF.get(cls, "land-trusts-out"), {})[c] = fl[c]["alternatives"][0]
    r["scenarios"] = list(b["scenarios"]) + [
        {"id": sid, "kind": "scope", "label": SCENARIO_LABEL[sid], "changes": ch,
         "result": NE.result(NE.applied(b["vector"], ch))} for sid, ch in sorted(groups.items())]
    return r


def d13_key(b):
    m = NE.d13(b)
    return (len(m["reach"]), m["span_failures"], m["span_points"])


def d13_line(b):
    m = NE.d13(b)
    return (f"reach {len(m['reach'])} tier(s) ({'/'.join(NE.TIER_ABBR[t] for t in m['reach'])}); span "
            f"{F1(m['span_points'])} points / {m['span_failures']} failures; "
            f"{'tier-robust' if m['robust'] else 'not tier-robust'}")


def enum_line(b):
    if not b["flags"]:
        return "no flags"
    e = NE.enumerate_register(b)
    return f"{e['combinations']:,} combinations; {100 * e['keep_share']:.1f}% keep the scored tier (assumes independent calls)"


def rank(blocks, key):
    """Protocol 6.4 order, least tier-robust first; ties share a rank."""
    order = sorted(blocks, key=lambda b: (tuple(-x for x in d13_key(b)), b["key"]))
    pos = [k for k, b in enumerate(order) if b["key"] == key][0]
    ahead = [b["key"] for b in order if d13_key(b) > d13_key(order[pos])]
    tied = [b["key"] for b in order if d13_key(b) == d13_key(order[pos]) and b["key"] != key]
    return len(ahead) + 1, ahead[:2], tied


def main():
    ok = True
    print("d18b_reexpression_s32.py -- decision D18(b): Ostrom-style commons governance's register, re-expressed")
    print("=" * 104)
    osb = [b for b in blocks_of(OS_DOC) if b["code"] == "OS"][0]
    rep = blocks_of(REPL_DOC)
    if len(rep) != 1:
        sys.exit(f"ERROR: {REPL_DOC}: expected one block")
    rep = rep[0]
    errs = NE.validate(osb)
    print(f"{'PASS' if not errs else 'FAIL'} the canonical block validates ({OS_DOC}): "
          f"{F1(osb['summary']['total'])}/26, {osb['summary']['failures']} failures, {osb['summary']['tier']}, "
          f"{len(osb['flags'])} flags")
    ok = ok and not errs
    flagged = [f["criterion"] for f in osb["flags"]]
    same_set = sorted(flagged, key=NE.CRITS.index) == sorted(CLASSIFICATION, key=NE.CRITS.index)
    print(f"{'PASS' if same_set else 'FAIL'} every flag is classified exactly once ({len(CLASSIFICATION)} of "
          f"{len(flagged)})")
    ok = ok and same_set
    text = re.sub(r"\s+", " ", open(os.path.join(HERE, OS_DOC), encoding="utf-8").read())
    found = {c: text.count(re.sub(r"\s+", " ", p)) for c, (_, p, _) in CLASSIFICATION.items()}
    good = all(n == 1 for n in found.values())
    print(f"{'PASS' if good else 'FAIL'} every deciding phrase is located exactly once in the document"
          + ("" if good else f": {[c for c, n in found.items() if n != 1]}"))
    ok = ok and good

    fo = {f["criterion"]: f for f in osb["flags"]}
    fr = {f["criterion"]: f for f in rep["flags"]}
    rscen = {c for s in rep["scenarios"] for c in s["changes"]}

    def pilot(c):
        vo, vr = osb["vector"][c], rep["vector"][c]
        if c in fr:
            if vo == vr and fr[c]["alternatives"] == fo[c]["alternatives"]:
                return "flagged, same alternative"
            if vr in fo[c]["alternatives"] and vo in fr[c]["alternatives"]:
                return "flagged in mirror"
            return "flagged, other alternative"
        if vr in fo[c]["alternatives"]:
            return "took the alternative, unflagged"
        tail = "; a scope scenario moves it to " + F1(rep["scenarios"][0]["changes"][c]) if c in rscen else ""
        return "the original's value, unflagged" + tail

    print("\n[1] THE TWENTY FLAGS, CLASSIFIED BY THEIR OWN STATED ALTERNATIVE READINGS")
    for c in NE.CRITS:
        if c not in fo:
            continue
        cls, phrase, note = CLASSIFICATION[c]
        print(f"  {c:6} {F1(fo[c]['scored'])} -> {fo[c]['alternatives']}  {cls:22} replication: {pilot(c)}")
        print(f"         \"{phrase[:96]}{'...' if len(phrase) > 96 else ''}\"")
        if note:
            print(f"         note: {note}")
    scope = sorted([c for c, (k, _, _) in CLASSIFICATION.items() if k != DOUBT], key=NE.CRITS.index)
    print(f"  scope questions: {len(scope)} ({', '.join(scope)}); doubts: {len(CLASSIFICATION) - len(scope)}; "
          f"borderline, kept as flags: {', '.join(BORDERLINE)}")

    new = reexpress(osb, scope)
    same_vec = new["vector"] == osb["vector"]
    print(f"\n{'PASS' if same_vec else 'FAIL'} no score changes: the re-expressed block carries the canonical vector")
    ok = ok and same_vec
    errs = NE.validate(new)
    print(f"{'PASS' if not errs else 'FAIL'} the re-expressed block validates as a canonical entry")
    for e in errs:
        print(f"     ERROR {e}")
    ok = ok and not errs

    print("\n[2] THE REGISTER, AS SCORED AND RE-EXPRESSED")
    for label, b in (("as scored     ", osb), ("re-expressed  ", new)):
        calls = len(NE.levers(b)[0])
        und = NE.undisputed_failures(b)
        print(f"  {label} {len(b['flags'])} flags ({calls} calls); undisputed failures {len(und)}"
              f"{' (' + ', '.join(und) + ')' if und else ''}")
        for jr in b["joint_readings"]:
            rs = jr["result"]
            print(f"  {'':14} reading {jr['id']:6} {F1(rs['total']):>5}/26 {rs['failures']:2d} failures  {rs['tier']}")
        print(f"  {'':14} D13: {d13_line(b)}")
        print(f"  {'':14} enumeration: {enum_line(b)}")

    print("\n[3] THE SCENARIOS (reported, never scored; protocol 6.5)")
    for s in new["scenarios"]:
        rs = s["result"]
        print(f"  {s['id']:18} " + ", ".join(f"{c} -> {F1(v)}" for c, v in s["changes"].items())
              + f"; {F1(rs['total'])}/26, {rs['failures']} failures, {rs['tier']}")
    rs = [s for s in rep["scenarios"]][0]
    print(f"  (replication)      {rs['id']}: " + ", ".join(f"{c} -> {F1(v)}" for c, v in rs["changes"].items())
          + f"; {F1(rs['result']['total'])}/26, {rs['result']['failures']} failures, {rs['result']['tier']}")

    print("\n[4] THE CORPUS POSITION (23 blocks from the eleven documents)")
    corpus = [b for d in ELEVEN for b in blocks_of(d)]
    keys = sorted(b["key"] for b in corpus)
    print(f"  {len(corpus)} blocks, {len(set(keys))} distinct entries")
    after = [new if b["key"] == osb["key"] else b for b in corpus]
    for label, bl in (("as scored   ", corpus), ("re-expressed", after)):
        r, ahead, tied = rank(bl, osb["key"])
        me = [b for b in bl if b["key"] == osb["key"]][0]
        second = sorted([b for b in bl if b["key"] != osb["key"]], key=lambda b: tuple(-x for x in d13_key(b)))[0]
        print(f"  {label}: D13 rank {r} of {len(bl)} from the least tier-robust"
              + (f" (tied with {', '.join(tied)})" if tied else "")
              + f"; next: {second['key']} ({d13_line(second)})")
        mx = max(len(b["flags"]) for b in bl if b["key"] != osb["key"])
        who = [b["key"] for b in bl if b["key"] != osb["key"] and len(b["flags"]) == mx]
        rel = "more than" if len(me["flags"]) > mx else ("as many as" if len(me["flags"]) == mx else "fewer than")
        print(f"  {'':12}  flags: {len(me['flags'])}, {rel} the largest other register ({mx}: {', '.join(who)})")

    print("\n[5] SENSITIVITY TO THE TWO BORDERLINE CLASSIFICATIONS")
    for label, extra in (("as proposed (both kept)", ()), ("C5.2 moved out", ("C5.2",)), ("C4.3 moved out", ("C4.3",)),
                         ("both moved out", ("C4.3", "C5.2"))):
        b = reexpress(osb, sorted(set(scope) | set(extra), key=NE.CRITS.index))
        bl = [b if x["key"] == osb["key"] else x for x in corpus]
        r, _, tied = rank(bl, osb["key"])
        print(f"  {label:24} {len(b['flags'])} flags; {d13_line(b)}; D13 rank {r}"
              + (f" (tied with {', '.join(tied)})" if tied else ""))

    print("\n[6] THE REPLICATION'S OWN REGISTER UNDER THE SAME TEST")
    print("  C4.2's alternative in the replication (\"if the mechanism's own domain -- rather than the whole economy "
          "-- is taken as the relevant frame\") is a frame question (i); its other four flags are doubts.")
    phrase = "if the mechanism's own domain — rather than the whole economy — is taken as the relevant frame"
    n = re.sub(r"\s+", " ", open(os.path.join(HERE, REPL_DOC), encoding="utf-8").read()).count(phrase)
    print(f"  {'PASS' if n == 1 else 'FAIL'} the replication's C4.2 phrase is located exactly once in {REPL_DOC}")
    ok = ok and n == 1
    rb = copy.deepcopy(rep)
    rb["flags"] = [f for f in rep["flags"] if f["criterion"] != "C4.2"]
    up, down = NE.extremes(rb)
    rb["joint_readings"] = [{"id": "scored", "label": "as scored", "basis": "scored", "resolve": {},
                             "result": NE.result(rep["vector"])},
                            {"id": "up", "label": "every call resolved upward", "basis": "extremes", "resolve": up,
                             "result": NE.result(NE.applied(rep["vector"], up))},
                            {"id": "down", "label": "every call resolved downward", "basis": "extremes",
                             "resolve": down, "result": NE.result(NE.applied(rep["vector"], down))}]
    print(f"  as delivered : {len(rep['flags'])} flags; {d13_line(rep)}")
    print(f"  re-expressed : {len(rb['flags'])} flags; {d13_line(rb)}")

    print("\n[7] WITH DECISION D26 AS RECOMMENDED (C3.2's 0.0 band reserved for an active inflationary mechanism)")
    only = [b["key"] for b in corpus if b["vector"]["C3.2"] == 0.0]
    print(f"  entries scored 0.0 on C3.2: {len(only)} ({', '.join(only)})")
    d26 = copy.deepcopy(new)
    d26["vector"]["C3.2"] = 0.5
    d26["flags"] = [f for f in new["flags"] if f["criterion"] != "C3.2"]
    res = NE.result(d26["vector"])
    d26["summary"] = dict({d: sum(d26["vector"][c] for c in cs) for d, cs in NE.DOMAINS.items()}, **res)
    up, down = NE.extremes(d26)
    d26["joint_readings"] = [
        {"id": "scored", "label": "as scored", "basis": "scored", "resolve": {}, "result": res},
        {"id": "up", "label": "every call resolved upward", "basis": "extremes", "resolve": up,
         "result": NE.result(NE.applied(d26["vector"], up))},
        {"id": "down", "label": "every call resolved downward", "basis": "extremes", "resolve": down,
         "result": NE.result(NE.applied(d26["vector"], down))}]
    d26["scenarios"] = [dict(s, result=NE.result(NE.applied(d26["vector"], s["changes"]))) for s in new["scenarios"]]
    errs = NE.validate(d26)
    expected = ["vector differs from the canonical corpus at C3.2"]
    good = errs == expected
    print(f"  {'PASS' if good else 'FAIL'} the block with D18(b) and D26 applied validates, but for the one intended "
          f"difference from the canonical corpus (C3.2)" + ("" if good else f": {errs}"))
    ok = ok and good
    print(f"  scored: {F1(res['total'])}/26, {res['failures']} failures, {res['tier']}; {len(d26['flags'])} flags")
    for jr in d26["joint_readings"][1:]:
        rs = jr["result"]
        print(f"  reading {jr['id']:6} {F1(rs['total']):>5}/26 {rs['failures']:2d} failures  {rs['tier']}")
    print(f"  D13: {d13_line(d26)}; enumeration: {enum_line(d26)}")
    bl = [d26 if x["key"] == osb["key"] else x for x in corpus]
    r, _, tied = rank(bl, osb["key"])
    print(f"  D13 rank {r} of {len(bl)} from the least tier-robust" + (f" (tied with {', '.join(tied)})" if tied else ""))
    for s in d26["scenarios"]:
        rs = s["result"]
        print(f"  scenario {s['id']:18} {F1(rs['total'])}/26, {rs['failures']} failures, {rs['tier']}")

    print("\nD18(b) PROPOSAL COMPUTED." if ok else "\nD18(b) PROPOSAL NOT COMPUTED: a check failed.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
