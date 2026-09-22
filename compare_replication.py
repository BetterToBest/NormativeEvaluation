#!/usr/bin/env python3
"""
compare_replication.py -- NEEC: the criterion-level comparison of a blind replication (protocol 11.4)
=====================================================================================================
Session 32. A blind replication (decision D2, protocol section 11) re-scores one corpus entry without
sight of its original scoring. This script compares the replicator's summary block with the original's,
at the level of the single criterion, as protocol 11.4 lists:

  * the vectors: exact matches, and each difference by criterion and direction; domain totals, totals,
    failures and passes side by side;
  * the flags: which criteria each side flags, and with which alternatives (the same, mirrored, or other);
    whether each difference in the vectors lies inside the original's register, the replication's, both
    or neither; how much of each side's admissible set the other covers;
  * the scope declaration: class, basis and population rule; the scope scenarios, and the criteria they
    move; the declared peers;
  * the joint readings and the D13 measure (protocol 6.4) on each side, and whether each side's scored
    vector is a combination of the other's register;
  * the tier.

Beside those it reports two agreement statistics, descriptively: Cohen's kappa (the three values treated
as categories) and Krippendorff's alpha (interval metric). Twenty-six criteria of one entry are not a
sample of independent items and one pair of scorers is not a sample of scorers; the statistics describe
this comparison and estimate nothing.

It does NOT attribute a disagreement to evidence, interpretation, scope or the protocol: that is the
replication record's job (protocol 11.5). With --record it checks that the record names every difference
in the vectors exactly once, each with an attribution from {evidence, interpretation, scope, protocol},
and that the record's generated tables are current; with --fill it writes those tables.

BOTH BLOCKS ARE VALIDATED AS CANDIDATES AGAINST THE SAME CORPUS -- the kit's, with the target withheld --
as protocol 11.3 requires of the replicator's block and of the maintainers' baseline. So the script runs
where neec_entry.py sits beside the KIT's corpus file (neec_corpus.json) and no canonical script: exactly
the layout of a replication kit. With --canonical-corpus FILE (the full canonical corpus file, under
another name) it also checks that the original block's key, code, display name and vector are the
canonical entry's, so that the comparison is with the published entry and not an edited copy.

Usage:   python3 compare_replication.py ORIGINAL.md REPLICATION.md [--code CODE]
                                        [--canonical-corpus FILE] [--record RECORD.md [--fill]]
         python3 compare_replication.py --selftest
ORIGINAL.md may hold several blocks; the one compared is the block with code CODE, or else the one block
whose key is the replication's. Exit status 0 only if both blocks validate (and, with --record, the record
passes). Prints file names only. Deterministic: no clock, no randomness, no dict-order dependence.
"""
import copy
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_entry():
    path = os.path.join(HERE, "neec_entry.py")
    if not os.path.isfile(path):
        sys.exit("ERROR: neec_entry.py must sit beside compare_replication.py")
    if os.path.isfile(os.path.join(HERE, "neec_weighting_robustness_analysis_v2.py")) or \
            os.path.isfile(os.path.join(os.getcwd(), "neec_weighting_robustness_analysis_v2.py")):
        sys.exit("ERROR: the canonical script is present; compare_replication.py runs against a kit's corpus "
                 "(neec_corpus.json with the target withheld), as a replication kit is laid out")
    spec = importlib.util.spec_from_file_location("neec_entry", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["neec_entry"] = mod
    spec.loader.exec_module(mod)
    return mod


NE = _load_entry()
CRITS, DOMAINS, TIERS, TIER_ABBR = NE.CRITS, NE.DOMAINS, NE.TIERS, NE.TIER_ABBR
VALUES = (0.0, 0.5, 1.0)
ATTRIBUTIONS = ("evidence", "interpretation", "scope", "protocol")
GEN_RE = re.compile(r"<!-- BEGIN GENERATED: ([a-z0-9-]+) -->\n(.*?)<!-- END GENERATED: \1 -->", re.S)
ATTR_RE = re.compile(r"<!-- BEGIN ATTRIBUTION -->\n(.*?)<!-- END ATTRIBUTION -->", re.S)
EPS = 1e-9


def f1(x):
    return f"{x:.1f}"


def signed(x):
    return f"{x:+.1f}"


# ------------------------------------------------------------------ blocks
def read_blocks(path):
    text = open(path, encoding="utf-8").read()
    blocks = NE.blocks_in_markdown(text)
    if not blocks:
        sys.exit(f"ERROR: {os.path.basename(path)}: no summary block")
    return blocks


def pick_original(blocks, key, code, name):
    if code:
        got = [b for b in blocks if b.get("code") == code]
        if len(got) != 1:
            sys.exit(f"ERROR: {name}: {len(got)} blocks with code {code!r}; exactly one is required")
        return got[0]
    got = [b for b in blocks if b.get("key") == key]
    if len(got) != 1:
        sys.exit(f"ERROR: {name}: {len(got)} blocks with key {key!r}; name the block with --code")
    return got[0]


def flagmap(b):
    return {f["criterion"]: f for f in b["flags"]}


def admissible(b):
    fl = flagmap(b)
    return {c: sorted({b["vector"][c]} | set(fl[c]["alternatives"] if c in fl else [])) for c in CRITS}


def domain_totals(v):
    return {d: sum(v[c] for c in cs) for d, cs in DOMAINS.items()}


# ------------------------------------------------------------------ statistics (descriptive)
def cohen_kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = sum((a.count(k) / n) * (b.count(k) / n) for k in VALUES)
    return None if abs(1 - pe) < EPS else (po - pe) / (1 - pe)


def kripp_alpha_interval(a, b):
    """Krippendorff's alpha, interval metric, two coders, no missing values: the coincidence-matrix form."""
    n = 2 * len(a)
    o = {(x, y): 0.0 for x in VALUES for y in VALUES}
    for x, y in zip(a, b):          # each unit contributes both ordered pairs, weighted 1/(m_u - 1) = 1
        o[(x, y)] += 1
        o[(y, x)] += 1
    nc = {x: sum(o[(x, y)] for y in VALUES) for x in VALUES}
    do = sum(o[(x, y)] * (x - y) ** 2 for x in VALUES for y in VALUES) / n
    de = sum(nc[x] * nc[y] * (x - y) ** 2 for x in VALUES for y in VALUES) / (n * (n - 1))
    return None if de < EPS else 1 - do / de


def kripp_alpha_pairwise(a, b):
    """The same statistic by direct pairwise sums; used by the self-test to check the form above."""
    vals = list(a) + list(b)
    n = len(vals)
    do = sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)
    de = sum((vals[i] - vals[j]) ** 2 for i in range(n) for j in range(n) if i != j) / (n * (n - 1))
    return None if de < EPS else 1 - do / de


def fmt_stat(x):
    return "undefined" if x is None else f"{x:.3f}"


# ------------------------------------------------------------------ the comparison
def compare(o, r):
    """Every fact of protocol 11.4 about original o and replication r (two validated blocks)."""
    vo, vr = o["vector"], r["vector"]
    fo, fr = flagmap(o), flagmap(r)
    ao, ar = admissible(o), admissible(r)
    diffs = [c for c in CRITS if abs(vo[c] - vr[c]) > EPS]
    rows = []
    for c in CRITS:
        rows.append(dict(
            c=c, o=vo[c], r=vr[c], d=vr[c] - vo[c],
            fo=fo[c]["alternatives"] if c in fo else None,
            fr=fr[c]["alternatives"] if c in fr else None,
            in_o=(c in diffs and c in fo and vr[c] in fo[c]["alternatives"]),
            in_r=(c in diffs and c in fr and vo[c] in fr[c]["alternatives"])))
    both = sorted(set(fo) & set(fr), key=CRITS.index)
    rel = {}
    for c in both:
        if vo[c] == vr[c] and fo[c]["alternatives"] == fr[c]["alternatives"]:
            rel[c] = "same"
        elif vo[c] != vr[c] and vr[c] in fo[c]["alternatives"] and vo[c] in fr[c]["alternatives"]:
            rel[c] = "mirrored"
        else:
            rel[c] = "other"
    union = sorted(set(fo) | set(fr), key=CRITS.index)
    res_o, res_r = NE.result(vo), NE.result(vr)
    a = [vo[c] for c in CRITS]
    b = [vr[c] for c in CRITS]
    so, sr = o["scope"], r["scope"]
    scen = lambda blk: [x for x in blk["scenarios"]]
    cov_r_by_o = [c for c in CRITS if set(ar[c]) <= set(ao[c])]
    cov_o_by_r = [c for c in CRITS if set(ao[c]) <= set(ar[c])]
    r_in_o = all(vr[c] in ao[c] for c in CRITS)
    o_in_r = all(vo[c] in ar[c] for c in CRITS)
    return dict(
        diffs=diffs, rows=rows,
        exact=26 - len(diffs),
        higher=[c for c in diffs if vr[c] > vo[c]], lower=[c for c in diffs if vr[c] < vo[c]],
        dom_o=domain_totals(vo), dom_r=domain_totals(vr),
        res_o=res_o, res_r=res_r,
        fail_o=[c for c in CRITS if vo[c] == 0.0], fail_r=[c for c in CRITS if vr[c] == 0.0],
        pass_o=[c for c in CRITS if vo[c] == 1.0], pass_r=[c for c in CRITS if vr[c] == 1.0],
        fail_agree=sum(1 for c in CRITS if (vo[c] == 0.0) == (vr[c] == 0.0)),
        within_step=sum(1 for c in CRITS if abs(vo[c] - vr[c]) <= 0.5 + EPS),
        kappa=cohen_kappa(a, b), alpha=kripp_alpha_interval(a, b),
        flags_o=sorted(fo, key=CRITS.index), flags_r=sorted(fr, key=CRITS.index),
        flags_both=both, flags_union=union, rel=rel,
        only_o=[c for c in CRITS if c in fo and c not in fr], only_r=[c for c in CRITS if c in fr and c not in fo],
        jaccard=(len(both) / len(union)) if union else 1.0,
        diffs_in_o=[x["c"] for x in rows if x["in_o"]], diffs_in_r=[x["c"] for x in rows if x["in_r"]],
        diffs_in_neither=[x["c"] for x in rows if x["c"] in diffs and not x["in_o"] and not x["in_r"]],
        flagged_diffs_o=[c for c in diffs if c in fo], flagged_diffs_r=[c for c in diffs if c in fr],
        cov_r_by_o=cov_r_by_o, cov_o_by_r=cov_o_by_r, r_in_o=r_in_o, o_in_r=o_in_r,
        scope_o=so, scope_r=sr, class_same=so["class"] == sr["class"],
        scen_o=scen(o), scen_r=scen(r),
        scope_moves_o=sorted({c for x in o["scenarios"] if x["kind"] == "scope" for c in x["changes"]}, key=CRITS.index),
        scope_moves_r=sorted({c for x in r["scenarios"] if x["kind"] == "scope" for c in x["changes"]}, key=CRITS.index),
        peers_o=o.get("peers") or [], peers_r=r.get("peers") or [],
        d13_o=NE.d13(o), d13_r=NE.d13(r),
        en_o=NE.enumerate_register(o) if o["flags"] else None,
        en_r=NE.enumerate_register(r) if r["flags"] else None,
        calls_o=len(NE.levers(o)[0]), calls_r=len(NE.levers(r)[0]),
        und_o=NE.undisputed_failures(o), und_r=NE.undisputed_failures(r),
        tier_same=res_o["tier"] == res_r["tier"],
        o_reach_has_r=res_r["tier"] in NE.d13(o)["reach"], r_reach_has_o=res_o["tier"] in NE.d13(r)["reach"],
    )


def lst(cs):
    return ", ".join(cs) if cs else "none"


def counted(cs):
    return f"{len(cs)} ({lst(cs)})" if cs else "0"


def reach(m):
    return "/".join(TIER_ABBR[t] for t in m["reach"])


# ------------------------------------------------------------------ plain report
def report(o, r, k, name_o, name_r):
    out = []
    ro, rr = k["res_o"], k["res_r"]
    out.append(f"original    [{o['code']}] {o['key']}  ({name_o})")
    out.append(f"replication [{r['code']}] {r['key']}  ({name_r})")
    out.append(f"  original:    {f1(ro['total'])}/26, {ro['failures']} failures, {ro['tier']}")
    out.append(f"  replication: {f1(rr['total'])}/26, {rr['failures']} failures, {rr['tier']}")
    out.append("")
    out.append("[1] VECTORS (protocol 11.4: exact matches, and each difference by criterion and direction)")
    out.append(f"  exact matches: {k['exact']} of 26; differences: {len(k['diffs'])} "
               f"(replication higher on {len(k['higher'])}, lower on {len(k['lower'])}); "
               f"total {signed(rr['total'] - ro['total'])}")
    for x in k["rows"]:
        if x["c"] in k["diffs"]:
            out.append(f"    {x['c']:6} original {f1(x['o'])}  replication {f1(x['r'])}  ({signed(x['d'])}); "
                       f"inside the original's register: {'yes' if x['in_o'] else 'no'}; "
                       f"inside the replication's: {'yes' if x['in_r'] else 'no'}")
    out.append("  domains:   " + "  ".join(f"{d} {f1(k['dom_o'][d])}/{f1(k['dom_r'][d])}" for d in DOMAINS)
               + "   (original/replication)")
    out.append(f"  failures:  original {lst(k['fail_o'])}; replication {lst(k['fail_r'])}; "
               f"failure status agrees on {k['fail_agree']} of 26")
    out.append(f"  passes:    original {lst(k['pass_o'])}; replication {lst(k['pass_r'])}")
    out.append(f"  within one step (0.5): {k['within_step']} of 26")
    out.append(f"  descriptive agreement statistics (26 criteria of one entry; not a sample): "
               f"Cohen's kappa {fmt_stat(k['kappa'])}; Krippendorff's alpha (interval) {fmt_stat(k['alpha'])}")
    out.append("")
    out.append("[2] FLAGS (protocol 11.4: the same criteria flagged, with the same alternatives)")
    out.append(f"  original flags {len(k['flags_o'])} criteria ({k['calls_o']} calls); "
               f"replication flags {len(k['flags_r'])} ({k['calls_r']} calls)")
    out.append(f"  flagged by both: {len(k['flags_both'])} ({lst(k['flags_both'])}); Jaccard {k['jaccard']:.3f}")
    for c in k["flags_both"]:
        fo, fr = flagmap(o)[c], flagmap(r)[c]
        out.append(f"    {c:6} original {f1(fo['scored'])} -> {fo['alternatives']}; replication {f1(fr['scored'])} -> "
                   f"{fr['alternatives']}: {k['rel'][c]}")
    out.append(f"  original only: {len(k['only_o'])} ({lst(k['only_o'])})")
    out.append(f"  replication only: {len(k['only_r'])} ({lst(k['only_r'])})")
    out.append(f"  differences inside the original's register: {len(k['diffs_in_o'])} of {len(k['diffs'])} "
               f"({lst(k['diffs_in_o'])})")
    out.append(f"  differences inside the replication's register: {len(k['diffs_in_r'])} of {len(k['diffs'])} "
               f"({lst(k['diffs_in_r'])})")
    out.append(f"  differences inside neither register: {len(k['diffs_in_neither'])} ({lst(k['diffs_in_neither'])})")
    out.append(f"  flags that coincide with a difference: original {len(k['flagged_diffs_o'])} of "
               f"{len(k['flags_o'])}; replication {len(k['flagged_diffs_r'])} of {len(k['flags_r'])}")
    out.append(f"  admissible sets (scored value and alternatives): the original's contains the replication's on "
               f"{len(k['cov_r_by_o'])} of 26 criteria; the replication's contains the original's on "
               f"{len(k['cov_o_by_r'])} of 26")
    out.append("")
    out.append("[3] SCOPE (protocol 11.4: agreement of the scope declaration)")
    for side, sc in (("original", k["scope_o"]), ("replication", k["scope_r"])):
        out.append(f"  {side:11} class {sc['class']} (basis {sc['basis']})")
    out.append(f"  class: {'the same' if k['class_same'] else 'DIFFERENT'}")
    for side, xs in (("original", k["scen_o"]), ("replication", k["scen_r"])):
        if not xs:
            out.append(f"  {side:11} scenarios: none")
        for x in xs:
            rs = x["result"]
            out.append(f"  {side:11} scenario {x['id']} ({x['kind']}): "
                       + ", ".join(f"{c} -> {f1(v)}" for c, v in x["changes"].items())
                       + f"; {f1(rs['total'])}/26, {rs['failures']} failures, {rs['tier']}")
    shared = [c for c in k["scope_moves_o"] if c in k["scope_moves_r"]]
    out.append(f"  criteria moved by scope scenarios: original {lst(k['scope_moves_o'])}; replication "
               f"{lst(k['scope_moves_r'])}; both {lst(shared)}")
    out.append(f"  declared peers: original {lst(k['peers_o']) if k['peers_o'] else 'none declared'}; "
               f"replication {lst(k['peers_r']) if k['peers_r'] else 'none declared'}")
    out.append("")
    out.append("[4] JOINT READINGS AND THE D13 MEASURE (protocol 6.2, 6.4)")
    for side, blk, m, en, und in (("original", o, k["d13_o"], k["en_o"], k["und_o"]),
                                  ("replication", r, k["d13_r"], k["en_r"], k["und_r"])):
        for jr in blk["joint_readings"]:
            rs = jr["result"]
            out.append(f"  {side:11} reading {jr['id']:18} {jr['basis']:8} {f1(rs['total']):>5}/26 "
                       f"{rs['failures']:2d} failures  {rs['tier']}")
        out.append(f"  {side:11} D13: reach {len(m['reach'])} tier(s) ({reach(m)}); span {f1(m['span_points'])} points / "
                   f"{m['span_failures']} failures; {'tier-robust' if m['robust'] else 'not tier-robust'}")
        if en:
            out.append(f"  {side:11} enumeration: {en['combinations']:,} combinations; keep scored tier "
                       f"{100 * en['keep_share']:.1f}% (assumes independent calls)")
        out.append(f"  {side:11} undisputed failures: {len(und)} ({lst(und)})")
    out.append(f"  the replication's vector is a combination of the original's register: "
               f"{'yes' if k['r_in_o'] else 'no'}")
    out.append(f"  the original's vector is a combination of the replication's register: "
               f"{'yes' if k['o_in_r'] else 'no'}")
    out.append("")
    out.append("[5] TIER")
    out.append(f"  original {ro['tier']}; replication {rr['tier']}: {'the same' if k['tier_same'] else 'DIFFERENT'}")
    out.append(f"  the original's joint readings reach the replication's tier: {'yes' if k['o_reach_has_r'] else 'no'}; "
               f"the replication's reach the original's: {'yes' if k['r_reach_has_o'] else 'no'}")
    return out


# ------------------------------------------------------------------ generated Markdown for the record
def alts(a):
    return "—" if a is None else ", ".join(f1(x) for x in a)


def md_sections(o, r, k):
    S = {}
    L = ["| Criterion | Original | Replication | Difference | Original's alternatives | Replication's alternatives |",
         "|---|---|---|---|---|---|"]
    for x in k["rows"]:
        d = "" if x["c"] not in k["diffs"] else signed(x["d"])
        cell = lambda v, c: f"**{f1(v)}**" if c in k["diffs"] else f1(v)
        L.append(f"| {x['c']} | {cell(x['o'], x['c'])} | {cell(x['r'], x['c'])} | {d} | {alts(x['fo'])} | {alts(x['fr'])} |")
    S["vectors"] = L
    ro, rr = k["res_o"], k["res_r"]
    L = ["| | Original | Replication |", "|---|---|---|"]
    names = {"D1": "Material Security", "D2": "Human Autonomy", "D3": "System Resilience", "D4": "Ethical Integrity",
             "D5": "Implementation Viability"}
    for d in DOMAINS:
        L.append(f"| {names[d]} | {f1(k['dom_o'][d])} | {f1(k['dom_r'][d])} |")
    L.append(f"| **Total** | **{f1(ro['total'])}/26 ({round(100 * ro['total'] / 26)}%)** | "
             f"**{f1(rr['total'])}/26 ({round(100 * rr['total'] / 26)}%)** |")
    L.append(f"| Structural failures | {ro['failures']} ({lst(k['fail_o'])}) | {rr['failures']} ({lst(k['fail_r'])}) |")
    L.append(f"| Tier | {ro['tier']} | {rr['tier']} |")
    L.append(f"| Flagged criteria | {len(k['flags_o'])} | {len(k['flags_r'])} |")
    L.append(f"| Undisputed failures | {counted(k['und_o'])} | {counted(k['und_r'])} |")
    S["summary"] = L
    L = ["| Measure | Result |", "|---|---|",
         f"| Exact matches | {k['exact']} of 26 |",
         f"| Differences | {len(k['diffs'])}: {lst(k['diffs'])} (replication higher on {len(k['higher'])}, lower on {len(k['lower'])}) |",
         f"| Within one step (0.5) | {k['within_step']} of 26 |",
         f"| Failure status agrees | {k['fail_agree']} of 26 |",
         f"| Cohen's kappa (values as categories) | {fmt_stat(k['kappa'])} |",
         f"| Krippendorff's alpha (interval) | {fmt_stat(k['alpha'])} |",
         f"| Differences inside the original's register | {len(k['diffs_in_o'])} of {len(k['diffs'])} |",
         f"| Differences inside the replication's register | {len(k['diffs_in_r'])} of {len(k['diffs'])} |",
         f"| Differences inside neither register | {len(k['diffs_in_neither'])} |",
         f"| Replication's vector is a combination of the original's register | {'yes' if k['r_in_o'] else 'no'} |",
         f"| Original's vector is a combination of the replication's register | {'yes' if k['o_in_r'] else 'no'} |"]
    S["agreement"] = L
    L = ["| Criterion | Original (scored → alternatives) | Replication (scored → alternatives) | Relation |",
         "|---|---|---|---|"]
    fo, fr = flagmap(o), flagmap(r)
    for c in k["flags_union"]:
        a = f"{f1(fo[c]['scored'])} → {alts(fo[c]['alternatives'])}" if c in fo else f"{f1(o['vector'][c])}, not flagged"
        b = f"{f1(fr[c]['scored'])} → {alts(fr[c]['alternatives'])}" if c in fr else f"{f1(r['vector'][c])}, not flagged"
        relation = k["rel"].get(c) or ("original only" if c in fo else "replication only")
        L.append(f"| {c} | {a} | {b} | {relation} |")
    L.append("")
    L.append(f"Flagged by both: {len(k['flags_both'])} of {len(k['flags_union'])} flagged criteria (Jaccard "
             f"{k['jaccard']:.3f}); " + ", ".join(f"{sum(1 for v in k['rel'].values() if v == t)} {t}"
                                              for t in ("same", "mirrored", "other")) + ".")
    S["flags"] = L
    L = ["| | Original | Replication |", "|---|---|---|",
         f"| Scope class | {k['scope_o']['class']} ({k['scope_o']['basis']}) | {k['scope_r']['class']} ({k['scope_r']['basis']}) |"]
    so = "; ".join(f"`{x['id']}` ({x['kind']}): " + ", ".join(f"{c} → {f1(v)}" for c, v in x["changes"].items())
                   + f" — {f1(x['result']['total'])}/26, {x['result']['failures']} failures, {x['result']['tier']}"
                   for x in k["scen_o"]) or "none"
    sr = "; ".join(f"`{x['id']}` ({x['kind']}): " + ", ".join(f"{c} → {f1(v)}" for c, v in x["changes"].items())
                   + f" — {f1(x['result']['total'])}/26, {x['result']['failures']} failures, {x['result']['tier']}"
                   for x in k["scen_r"]) or "none"
    L.append(f"| Scenarios | {so} | {sr} |")
    L.append(f"| Declared peers | {', '.join(k['peers_o']) if k['peers_o'] else 'none declared'} | "
             f"{', '.join(k['peers_r']) if k['peers_r'] else 'none declared'} |")
    S["scope"] = L
    L = ["| Side | Reading | Basis | Total | Failures | Tier |", "|---|---|---|---|---|---|"]
    for side, blk in (("Original", o), ("Replication", r)):
        for jr in blk["joint_readings"]:
            rs = jr["result"]
            L.append(f"| {side} | `{jr['id']}` | {jr['basis']} | {f1(rs['total'])}/26 | {rs['failures']} | {rs['tier']} |")
    L.append("")
    for side, m, en in (("Original", k["d13_o"], k["en_o"]), ("Replication", k["d13_r"], k["en_r"])):
        share = f"; enumeration {en['combinations']:,} combinations, {100 * en['keep_share']:.1f}% keep the scored tier " \
                f"(assumes independent calls)" if en else ""
        L.append(f"- **{side}, D13:** reach {len(m['reach'])} tier(s) ({reach(m)}); span {f1(m['span_points'])} "
                 f"points / {m['span_failures']} failures; {'tier-robust' if m['robust'] else 'not tier-robust'}{share}.")
    S["readings"] = L
    return {name: "\n".join(lines) + "\n" for name, lines in S.items()}


def check_record(path, k, sections, fill):
    """The record's generated tables must be current; its attribution table must name every difference once."""
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()
    E = []
    found = {m.group(1): m.group(2) for m in GEN_RE.finditer(text)}
    missing = sorted(set(sections) - set(found))
    unknown = sorted(set(found) - set(sections))
    if missing:
        E.append(f"generated sections missing: {missing}")
    if unknown:
        E.append(f"unknown generated sections: {unknown}")
    if fill and not missing:
        new = GEN_RE.sub(lambda m: f"<!-- BEGIN GENERATED: {m.group(1)} -->\n{sections[m.group(1)]}"
                                   f"<!-- END GENERATED: {m.group(1)} -->", text)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
        text = new
        found = {m.group(1): m.group(2) for m in GEN_RE.finditer(text)}
    stale = sorted(s for s in sections if s in found and found[s] != sections[s])
    if stale:
        E.append(f"generated sections not current (run with --fill): {stale}")
    m = ATTR_RE.search(text)
    rows = []
    if not m:
        E.append("no attribution table (<!-- BEGIN ATTRIBUTION --> ... <!-- END ATTRIBUTION -->)")
    else:
        for line in m.group(1).splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4 or not re.fullmatch(r"C\d\.\d[ab]?", cells[0]):
                continue
            rows.append(cells)
        named = [c[0] for c in rows]
        if sorted(named, key=CRITS.index) != k["diffs"] or len(named) != len(set(named)):
            E.append(f"attribution rows name {named}; the differences are {k['diffs']}")
        for cells in rows:
            c = cells[0]
            if c not in CRITS:
                continue
            want = (f1(k["rows"][CRITS.index(c)]["o"]), f1(k["rows"][CRITS.index(c)]["r"]))
            if (cells[1], cells[2]) != want:
                E.append(f"attribution row {c}: values {cells[1]} / {cells[2]}, expected {want[0]} / {want[1]}")
            cats = [x.strip() for x in re.split(r"[+,]", cells[3]) if x.strip()]
            if not cats or any(x not in ATTRIBUTIONS for x in cats) or len(cats) != len(set(cats)):
                E.append(f"attribution row {c}: '{cells[3]}' is not drawn from {ATTRIBUTIONS}")
    out = [f"record {name}: {len(sections)} generated sections "
           + ("written and " if fill else "") + ("current" if not stale and not missing else "NOT current")
           + f"; attribution table names {len(rows)} difference(s)"]
    for e in E:
        out.append(f"  ERROR {e}")
    return out, not E


# ------------------------------------------------------------------ main
def validate_pair(o, r, canonical_corpus, name_o, name_r):
    out, ok = [], True
    for label, blk, nm in (("original", o, name_o), ("replication", r, name_r)):
        errs = NE.validate(blk, candidate=True)
        out.append(f"{'PASS' if not errs else 'FAIL'} {label:11} [{blk.get('code')}] {blk.get('key')}: validates as a "
                   f"candidate against the kit's corpus ({len(NE.SCORES)} entries)")
        for e in errs:
            out.append(f"     ERROR {e}")
        ok = ok and not errs
    if not ok:
        return out, False
    if o["key"] != r["key"]:
        out.append(f"FAIL the two blocks score different entries: {o['key']!r} and {r['key']!r}")
        return out, False
    if canonical_corpus is not None:
        crits, scores, display, codes, _ = canonical_corpus
        k = o["key"]
        good = (crits == CRITS and k in scores and codes.get(k) == o["code"] and display.get(k) == o["display_name"]
                and all(abs(scores[k][c] - o["vector"][c]) < EPS for c in CRITS))
        out.append(f"{'PASS' if good else 'FAIL'} original is the canonical entry: key, code, display name and vector "
                   f"match the canonical corpus file ({len(scores)} entries)")
        if not good:
            return out, False
        if k in NE.SCORES or len(scores) != len(NE.SCORES) + 1 or \
                any(key not in scores or scores[key] != NE.SCORES[key] for key in NE.SCORES):
            out.append("FAIL the kit's corpus is not the canonical corpus with exactly the target withheld")
            return out, False
        out.append("PASS the kit's corpus is the canonical corpus with exactly the target withheld")
    return out, True


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args, opts = [], {}
    it = iter(argv)
    for a in it:
        if a in ("--code", "--canonical-corpus", "--record"):
            opts[a] = next(it, None)
        elif a == "--fill":
            opts[a] = True
        else:
            args.append(a)
    if len(args) != 2 or any(v is None for v in opts.values()):
        print(__doc__.split("Usage:")[1].split("ORIGINAL.md may")[0].rstrip())
        return 2
    po, pr = args
    no, nr = os.path.basename(po), os.path.basename(pr)
    rb = read_blocks(pr)
    if len(rb) != 1:
        sys.exit(f"ERROR: {nr}: {len(rb)} summary blocks; a replication document carries exactly one")
    r = rb[0]
    o = pick_original(read_blocks(po), r.get("key"), opts.get("--code"), no)
    cc = NE.load_corpus_file(opts["--canonical-corpus"]) if opts.get("--canonical-corpus") else None
    print("compare_replication.py -- protocol 11.4, the criterion-level comparison of a blind replication")
    print("=" * 100)
    lines, ok = validate_pair(o, r, cc, no, nr)
    print("\n".join(lines))
    if not ok:
        print("\nCOMPARISON NOT RUN: a block does not validate.")
        return 1
    print("")
    k = compare(o, r)
    print("\n".join(report(o, r, k, no, nr)))
    if opts.get("--record"):
        print("")
        lines, rok = check_record(opts["--record"], k, md_sections(o, r, k), bool(opts.get("--fill")))
        print("\n".join(lines))
        if not rok:
            return 1
    print("\nCOMPARISON COMPLETE.")
    return 0


# ------------------------------------------------------------------ self-test (synthetic replicator blocks)
def _block(key, code, vector, flags, scope_class="mechanism", scenarios=None, peers=None, doc="SYNTHETIC.md"):
    b = {"schema": NE.SCHEMA_ID, "key": key, "code": code, "display_name": key,
         "record": {"documents": [doc], "scored": "synthetic (compare_replication.py --selftest)",
                    "structure": "native-v2"},
         "scope": {"class": scope_class, "basis": "stated", "population": "synthetic"},
         "vector": {c: vector[c] for c in CRITS}, "summary": None,
         "flags": [dict(criterion=c, scored=vector[c], alternatives=a, basis="stated", reading="synthetic")
                   for c, a in sorted(flags.items(), key=lambda kv: CRITS.index(kv[0]))],
         "joint_readings": [], "scenarios": []}
    res = NE.result(b["vector"])
    b["summary"] = dict({d: s for d, s in domain_totals(b["vector"]).items()}, total=res["total"],
                        failures=res["failures"], tier=res["tier"])
    b["joint_readings"] = [{"id": "scored", "label": "as scored", "basis": "scored", "resolve": {}, "result": res}]
    if b["flags"]:
        up, down = NE.extremes(b)
        b["joint_readings"] += [
            {"id": "up", "label": "every call up", "basis": "extremes", "resolve": up,
             "result": NE.result(NE.applied(b["vector"], up))},
            {"id": "down", "label": "every call down", "basis": "extremes", "resolve": down,
             "result": NE.result(NE.applied(b["vector"], down))}]
    for sid, ch in (scenarios or {}).items():
        b["scenarios"].append({"id": sid, "label": "synthetic", "kind": "scope", "changes": ch,
                               "result": NE.result(NE.applied(b["vector"], ch))})
    if peers is not None:
        b["peers"] = peers
    return b


def selftest():
    key = "Synthetic Replication Target"
    base = dict(zip(CRITS, [0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 0.5, 0.0, 0.5, 0.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5,
                            1.0, 0.5, 0.5, 0.5, 0.5, 1.0, 0.5, 1.0, 0.5, 1.0]))
    oflags = {"C1.4": [0.0], "C2.4": [1.0], "C4.1": [0.5]}
    peers = [NE.KEYS[0]]
    orig = _block(key, "SYN", base, oflags, scenarios={"boundary": {"C1.3": 0.0}}, peers=peers)
    cases, ok_all = [], True

    def variant(changes=None, flags=None, scope_class="mechanism", key_=key):
        v = dict(base)
        v.update(changes or {})
        return _block(key_, "SYNR", v, oflags if flags is None else flags, scope_class=scope_class,
                      scenarios={"boundary": {"C1.3": 0.0}} if v["C1.3"] != 0.0 else None, peers=peers,
                      doc="SYNTHETIC_replication.md")

    def run(name, r, expect):
        nonlocal ok_all
        lines, ok = validate_pair(orig, r, None, "o", "r")
        if isinstance(expect, str):             # a refusal, and the reason it must give
            good = not ok and any(expect in l for l in lines)
            got = "refused" if not ok else "compared"
        else:
            k = compare(orig, r) if ok else None
            good = ok and all(fn(k) for fn in expect)
            got = "compared" if ok else "refused: " + "; ".join(l.strip() for l in lines if "ERROR" in l or "FAIL" in l)[:160]
        ok_all = ok_all and good
        cases.append(f"  {'ok  ' if good else 'FAIL'} {name} ({got})")

    run("an identical replication agrees everywhere", variant(),
        [lambda k: k["exact"] == 26 and not k["diffs"], lambda k: k["jaccard"] == 1.0,
         lambda k: all(v == "same" for v in k["rel"].values()), lambda k: k["class_same"] and k["tier_same"],
         lambda k: k["kappa"] == 1.0 and abs(k["alpha"] - 1.0) < EPS, lambda k: k["r_in_o"] and k["o_in_r"]])
    run("a difference that takes the original's alternative, flagged in mirror, is inside both registers",
        variant({"C1.4": 0.0}, {"C1.4": [0.5], "C2.4": [1.0], "C4.1": [0.5]}),
        [lambda k: k["diffs"] == ["C1.4"] and k["lower"] == ["C1.4"], lambda k: k["rel"]["C1.4"] == "mirrored",
         lambda k: k["diffs_in_o"] == ["C1.4"] and k["diffs_in_r"] == ["C1.4"] and not k["diffs_in_neither"]])
    run("a difference outside every flag is inside neither register",
        variant({"C3.3": 1.0}),
        [lambda k: k["diffs"] == ["C3.3"] and k["higher"] == ["C3.3"], lambda k: k["diffs_in_neither"] == ["C3.3"],
         lambda k: not k["r_in_o"] and not k["o_in_r"]])
    run("three more failures move the replication to another tier",
        variant({"C1.1": 0.0, "C2.1": 0.0, "C3.1": 0.0}),
        [lambda k: not k["tier_same"] and k["res_r"]["failures"] == 6 and k["res_o"]["failures"] == 3,
         lambda k: k["fail_agree"] == 23])
    run("a different scope class is reported as a scope disagreement",
        variant(scope_class="comprehensive_system"), [lambda k: not k["class_same"] and k["exact"] == 26])
    run("a flag only the replication raises is reported as replication-only",
        variant(flags={"C1.4": [0.0], "C2.4": [1.0], "C3.2": [0.0], "C4.1": [0.5]}),
        [lambda k: k["only_r"] == ["C3.2"] and not k["only_o"], lambda k: abs(k["jaccard"] - 0.75) < EPS])
    run("the same criterion flagged with a different alternative is 'other'",
        variant(flags={"C1.4": [0.0], "C2.4": [0.0], "C4.1": [0.5]}),
        [lambda k: k["rel"]["C2.4"] == "other" and k["rel"]["C1.4"] == "same"])
    bad = variant()
    bad["summary"] = dict(bad["summary"], total=bad["summary"]["total"] + 0.5)
    run("a replication whose summary is not its vector's arithmetic is refused", bad, "summary total is not the sum")
    run("a replication of a different entry is refused", variant(key_="Some Other Synthetic Entry"), "score different entries")
    inside = variant()
    inside["key"] = inside["display_name"] = NE.KEYS[0]
    run("a replication whose key is already in the kit's corpus is refused", inside, "is already in the corpus")
    # the two forms of Krippendorff's alpha, and kappa on a hand-checked table
    a = [base[c] for c in CRITS]
    b = list(a)
    b[CRITS.index("C1.4")] = 0.0
    b[CRITS.index("C3.3")] = 1.0
    b[CRITS.index("C4.1")] = 0.5
    same = abs(kripp_alpha_interval(a, b) - kripp_alpha_pairwise(a, b)) < 1e-12
    ok_all = ok_all and same
    cases.append(f"  {'ok  ' if same else 'FAIL'} Krippendorff's alpha: the coincidence-matrix and pairwise forms agree "
                 f"({kripp_alpha_interval(a, b):.6f})")
    k2 = cohen_kappa([0.0, 0.5, 1.0, 0.5], [0.0, 0.5, 0.5, 0.5])   # po 3/4; pe = (1*1 + 2*3 + 1*0)/16 = 7/16
    good = abs(k2 - (0.75 - 7 / 16) / (1 - 7 / 16)) < 1e-12
    ok_all = ok_all and good
    cases.append(f"  {'ok  ' if good else 'FAIL'} Cohen's kappa on a hand-checked table ({k2:.6f} = 5/9)")
    print(f"compare_replication.py --selftest (corpus: {NE.CORPUS_SOURCE or 'canonical script'}, "
          f"{len(NE.SCORES)} entries; synthetic original and replicator blocks)")
    print("\n".join(cases))
    n = len(cases)
    print(f"selftest: {sum(1 for c in cases if c.startswith('  ok'))} of {n} cases behave as expected")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
