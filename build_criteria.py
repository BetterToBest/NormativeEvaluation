#!/usr/bin/env python3
"""
build_criteria.py -- NEEC Session 45: criteria.json v2.0 (28 criteria), generated
=================================================================================
Version 2 of the criteria generator (version 1, Session 27 with the Session 36
corrections, is pinned as build_criteria_s44_snapshot.py; its output is pinned
as criteria_s44_snapshot.json). Nothing is retyped:

  * the base is criteria_s44_snapshot.json, the 26 criteria as they stood at
    tag s44 (md5 checked);
  * every change is read from Appendix V of NEEC_Criteria_v2_s45.md, the
    record of the v2.0 criteria (Package A of the Session 44 review, adopted
    under the delegation; Package B, adopted by the owner: C2.6 and C3.6);
  * the clause split of a threshold that v2.0 leaves unchanged is read from
    Appendix B of the pinned protocol, SCORING_PROTOCOL_s44_snapshot.md.

It writes criteria.json (schema neec-criteria/2.0) and SCORING_PROTOCOL.md,
which is the pinned Session 44 protocol with generated edits: the version
line, the header's criteria count, a changes paragraph, section 2.3's gap
example and clause count, a note in 2.4 on v2.0's arithmetic, and Appendix B
(the clauses of each Pass Threshold, from criteria.json). Each old text is
asserted before it is replaced, so the protocol is regenerated from
the snapshot on every run, never edited in place.

ASSERTIONS. The run exits 1, writing nothing, unless all of these hold:
  A1 figures     every figure in a Requirement is in its Pass Threshold; every
                 figure in a measurement field is in it or declared descriptive
                 (the block's `allow`);
  A2 quantities  each registered quantity is in exactly one Pass Threshold;
  A3 dates       no Pass Threshold carries a year, except a declared price year;
  A4 place       no field names a US-only measure;
  A5 clauses     every clause is a verbatim substring of its threshold, once, in
                 order, leaving connectives (commas, semicolons, "and", "with")
                 and the declared scope only;
  A6 anchors     every anchor's threshold line is its Pass Threshold (D28(g));
  A7 structure   28 criteria; domain maxima 6, 6, 6, 5, 5; every criterion has a
                 class and the record names no unknown criterion.

Usage:  python3 build_criteria.py             build, assert, write, print the log
        python3 build_criteria.py --selftest  plant one violation of each rule on
                                              the built document; exit 0 only if
                                              the clean document passes and every
                                              planted violation is rejected
Looks for inputs in the working directory. Deterministic.
"""
import copy
import hashlib
import json
import re
import sys
import textwrap

SNAP, SNAP_MD5 = "criteria_s44_snapshot.json", "d4b78634cd233adb8c00b1a5e0a00821"
PROTO_BASE, PROTO_BASE_MD5 = "SCORING_PROTOCOL_s44_snapshot.md", "bbee2c45901c34d58995528e9386d58e"
RECORD = "NEEC_Criteria_v2_s45.md"
OUT, PROTO_OUT = "criteria.json", "SCORING_PROTOCOL.md"

CLASSES = {"W": "wording, commentary or disclosure only", "D": "clauses deleted only",
           "I": "indicator named for an unchanged clause and bar", "M": "bar, measure or clause restated",
           "N": "new criterion", "U": "unchanged"}
DEF_KEYS = ("derivation", "requirement", "rationale", "distinguishes", "measurement", "measurement_protocol",
            "pass_threshold", "disclosure", "threshold_note", "indicators")
MEASURE_FIELDS = ("measurement", "measurement_protocol", "cultural_geographic_adaptation")
QUANTITIES = {  # registered quantity -> pattern; each must be in exactly one Pass Threshold (A2)
    "wealth Gini": r"\bGini\b", "citizen proposals adopted": r"proposals", "carbon": r"carbon|CO2",
    "resource use against regeneration": r"regenerat|biocapacity", "autonomy share": r"autonomy|coercion",
    "association": r"association|[Cc]ivil-liberties", "housing stability": r"housing stability",
    "public debt": r"\b[Dd]ebt\b", "productivity": r"per hour|productivity", "inflation": r"inflation"}
US_ONLY = ("area median income", "Supplemental Poverty Measure", "CPI-U", "Census Bureau")
REFS = re.compile(r"\bC\d\.\d[ab]?\b|\bN\d+\b|\b[DKRGS]\d+\b|\bCO2\b|COVID-19|rtfpna|\bv\d\.\d\b"
                  r"|(?:[Ss]ection|protocol|Appendix|Paper [Ss]ection) [A-Z]?\.?\d+(?:\.\d+)*(?:\([a-g]\))?"
                  r"|SDG(?: indicator)? \d+(?:\.\d+)+|SNA item D\.\d+"
                  r"|[Cc]lauses? \d+(?:\s*(?:–|-|and|,)\s*\d+)*")
NUM = re.compile(r"\$?\d[\d,]*(?:\.\d+)?%?")
YEAR = re.compile(r"\b(?:19|20)\d\d\b")
BAND_NOTE = ("v2.0 (Session 45): this criterion's Pass Threshold was restated ({codes}; NEEC_Criteria_v2_s45.md). "
             "The band texts and examples were written against Paper v1.4's threshold: they describe, and the "
             "threshold above governs (protocol 2.3(g)). Examples are re-estimated in the rescoring pass.")
WORDING_NOTE = ("v2.0 (Session 45): this criterion's Pass Threshold was reworded without a change of bar ({codes}; "
                "NEEC_Criteria_v2_s45.md); the band texts stand.")


def md5(b):
    return hashlib.md5(b).hexdigest()


def figures(text):
    return [n.rstrip(",") for n in NUM.findall(REFS.sub(" ", text))]


def words(n):
    w = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
         "seventeen eighteen nineteen").split()
    tens = {20: "twenty", 30: "thirty", 40: "forty"}
    return w[n] if n < 20 else tens[n - n % 10] + ("-" + w[n % 10] if n % 10 else "")


def and_list(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def natural(cid):
    m = re.match(r"^C(\d)\.(\d)([ab]?)$", cid)
    return (int(m.group(1)), int(m.group(2)), m.group(3))


# ------------------------------------------------------------------ inputs
snap_bytes = open(SNAP, "rb").read()
if md5(snap_bytes) != SNAP_MD5:
    sys.exit(f"ERROR: {SNAP} md5 {md5(snap_bytes)[:8]}, expected {SNAP_MD5[:8]}")
base = json.loads(snap_bytes.decode("utf-8"))
proto_bytes = open(PROTO_BASE, "rb").read()
if md5(proto_bytes) != PROTO_BASE_MD5:
    sys.exit(f"ERROR: {PROTO_BASE} md5 {md5(proto_bytes)[:8]}, expected {PROTO_BASE_MD5[:8]}")
proto = proto_bytes.decode("utf-8")
rec_bytes = open(RECORD, "rb").read()
rec = rec_bytes.decode("utf-8")

# Appendix V: one block per criterion.
appv = rec[rec.index("## Appendix V."):]
blocks, cur = {}, None
for line in appv.split("\n"):
    m = re.match(r"^### (C\d\.\d[ab]?)(?: · (.+))?$", line)
    if m:
        cur = m.group(1)
        blocks[cur] = {"_name": m.group(2)} if m.group(2) else {}
        continue
    f = re.match(r"^- \*\*([a-z_0-9.]+)\*\*: (.*)$", line)
    if f and cur:
        blocks[cur][f.group(1)] = f.group(2).strip()

sm = re.search(r"^- \*\*structure\*\*: (\d+) criteria; domain maxima ([\d, ]+)$", appv, re.M)
if not sm:
    sys.exit(f"ERROR: {RECORD} Appendix V has no structure line")
WANT_N, WANT_DM = int(sm.group(1)), [float(x) for x in sm.group(2).split(", ")]

# The pinned protocol's Appendix B: the clause split of thresholds v2.0 leaves unchanged.
appb_old = proto[proto.index("## Appendix B."):]
v1_clauses = {}
for r in appb_old.split("\n"):
    m = re.match(r"^\| (C\d\.\d[ab]?) \| (.+) \|$", r)
    if m:
        v1_clauses[m.group(1)] = [x.strip() for x in re.split(r"\(\d+\) ", m.group(2)) if x.strip()]

# ------------------------------------------------------------------ assemble
old = {c["id"]: c for c in base["criteria"]}
ORDER = sorted(set(old) | {k for k, b in blocks.items() if "domain" in b}, key=natural)
LOG, criteria = [], []
for cid in ORDER:
    b = blocks.get(cid, {"class": "U", "codes": "none"})
    cls, codes = b.get("class", "U"), b.get("codes", "none")
    if cid in old:
        c = copy.deepcopy(old[cid])
    else:
        c = dict(id=cid, domain=b["domain"], name=b["_name"], definition={},
                 anchors=dict(threshold="", note="", bands={}), sources={})
    d = c["definition"]
    changed = []
    if b.get("_name") and b["_name"] != c["name"]:
        changed.append(f"name ({c['name']} -> {b['_name']})" if cid in old else "name")
        c["name"] = b["_name"]
    for k in DEF_KEYS:
        if k in b and d.get(k) != b[k]:
            changed.append(k)
            d[k] = b[k]
    for k in [x.strip() for x in b.get("remove", "").split(",") if x.strip()]:
        if k not in d:
            sys.exit(f"ERROR: {cid}: the record removes {k}, which the snapshot does not have")
        del d[k]
        changed.append(f"-{k}")
    pt = d["pass_threshold"]
    pt_changed = cid not in old or pt != old[cid]["definition"]["pass_threshold"]
    if "clauses" in b:
        clauses = [x.strip() for x in b["clauses"].split(" | ")]
    elif not pt_changed and cid in v1_clauses:
        clauses = v1_clauses[cid]
    elif not pt_changed:
        clauses = [pt]
    else:
        sys.exit(f"ERROR: {cid}: threshold restated without a clause split")
    d["clauses"] = clauses
    if "scope" in b:
        d["clause_scope"] = b["scope"]
    c["anchors"]["threshold"] = pt + "."
    if cid not in old:
        c["anchors"]["bands"] = {bd: dict(text=b["band_" + bd], examples=[]) for bd in ("1.0", "0.5", "0.0")}
        src = "NEEC_Criteria_v2_s45.md, Appendix V (Package B, decision 45.1)"
        c["sources"] = dict(definition=src, anchors=src, threshold=src)
    else:
        if pt_changed:
            note = (WORDING_NOTE if cls in ("W", "I") else BAND_NOTE).format(codes=codes)
            c["anchors"]["note"] = (c["anchors"]["note"] + " " + note).strip()
        for k, hit in (("definition", bool(changed)), ("threshold", pt_changed)):
            if hit:
                c["sources"][k] += "; restated in v2.0 (NEEC_Criteria_v2_s45.md, Appendix V)"
    c["revision"] = dict(cls=cls, codes=[x.strip() for x in codes.split(",")] if codes != "none" else [])
    criteria.append(c)
    LOG.append((cid, cls, codes, changed, pt_changed, len(clauses)))

DOMAIN_IDS = [dm["id"] for dm in base["domains"]]
domains = [dict(dm, criteria=[c["id"] for c in criteria if c["domain"] == dm["id"]]) for dm in base["domains"]]
doc = dict(
    schema="neec-criteria/2.0",
    framework=f"NEEC Applied, v2.0 criteria: {len(criteria)} criteria in five domains",
    generated_by="build_criteria.py version 2 (Session 45); do not edit by hand",
    source=dict(base=SNAP, base_md5=SNAP_MD5, record=RECORD, record_md5=md5(rec_bytes),
                clause_splits=PROTO_BASE + ", Appendix B (thresholds v2.0 leaves unchanged)",
                v1=base["source"]),
    scale=base["scale"],
    structure=dict(criteria=len(criteria), total_max=float(len(criteria)),
                   domain_max={dm: float(sum(1 for c in criteria if c["domain"] == dm)) for dm in DOMAIN_IDS},
                   tiers_note=f"Tier bands stay integer failure counts (0-2, 3-5, 6+) on {len(criteria)} "
                              "criteria (decision 45.1); Paper v2.0 Appendix A.4 reports the proportional alternative."),
    tiers=[dict(t, failures_max=len(criteria)) if t["failures_min"] == 6 else t for t in base["tiers"]],
    domains=domains,
    classes=CLASSES,
    criteria=criteria,
)


# ------------------------------------------------------------------ assertions
def check_all(doc, blocks):
    fails = []
    crit = doc["criteria"]
    pts = {c["id"]: c["definition"]["pass_threshold"] for c in crit}
    for c in crit:  # A1
        d, cid = c["definition"], c["id"]
        ptf = set(figures(d["pass_threshold"]))
        extra = [n for n in figures(d.get("requirement", "")) if n not in ptf]
        if extra:
            fails.append(("A1", f"{cid} requirement figures not in its Pass Threshold: {extra}"))
        allow = {x.strip() for x in re.split(r",\s+", blocks.get(cid, {}).get("allow", "")) if x.strip()}
        for f in MEASURE_FIELDS:
            extra = [n for n in figures(d.get(f, "")) if n not in ptf and n not in allow]
            if extra:
                fails.append(("A1", f"{cid} {f} figures neither in its Pass Threshold nor declared: {extra}"))
    for q, pat in QUANTITIES.items():  # A2
        where = [cid for cid, pt in pts.items() if re.search(pat, pt)]
        if len(where) != 1:
            fails.append(("A2", f"quantity '{q}' is in {len(where)} Pass Thresholds: {where}"))
    for cid, pt in pts.items():  # A3
        yrs = [y for y in YEAR.findall(pt) if y != blocks.get(cid, {}).get("price_year")]
        if yrs:
            fails.append(("A3", f"{cid} Pass Threshold carries a year: {yrs}"))
    for c in crit:  # A4
        for k, v in c["definition"].items():
            for term in US_ONLY:
                if isinstance(v, str) and term in v:
                    fails.append(("A4", f"{c['id']} {k} names a US-only measure: {term}"))
    for c in crit:  # A5
        d, pt, p, rest = c["definition"], c["definition"]["pass_threshold"], 0, ""
        ok = True
        for t in d["clauses"]:
            i = pt.find(t, p)
            if i < 0 or pt.count(t) != 1:
                ok = False
                break
            rest, p = rest + pt[p:i], i + len(t)
        rest += pt[p:]
        if d.get("clause_scope"):
            rest = rest.replace(d["clause_scope"], "", 1)
        if not ok or re.sub(r"(,|;|\band\b|\bwith\b|\s)", "", rest):
            fails.append(("A5", f"{c['id']} clauses are not verbatim, once, in order, leaving connectives only"))
    for c in crit:  # A6
        if c["anchors"]["threshold"] != c["definition"]["pass_threshold"] + ".":
            fails.append(("A6", f"{c['id']} anchor threshold differs from its Pass Threshold"))
    dm = doc["structure"]["domain_max"]  # A7
    if len(crit) != WANT_N or [dm[k] for k in sorted(dm)] != WANT_DM:
        fails.append(("A7", f"structure: {len(crit)} criteria, domain maxima {dm}"))
    unknown = [k for k in blocks if k not in {c["id"] for c in crit}]
    badcls = [c["id"] for c in crit if c["revision"]["cls"] not in CLASSES]
    if unknown or badcls:
        fails.append(("A7", f"record names unknown criteria {unknown} or classes {badcls}"))
    return fails


def selftest():
    clean = check_all(doc, blocks)
    print("build_criteria.py --selftest: each rule must reject a planted violation")
    print(f"  clean v2.0 document: {len(clean)} failure(s)")
    by = {c["id"]: i for i, c in enumerate(doc["criteria"])}

    def plant(rule, desc, fn):
        bad = copy.deepcopy(doc)
        fn(bad, bad["criteria"])
        hit = [m for r, m in check_all(bad, blocks) if r == rule]
        print(f"  {rule} {'rejects' if hit else 'MISSES '} {desc}")
        return bool(hit)

    def pt(cr, cid, text):
        cr[by[cid]]["definition"]["pass_threshold"] = text
        cr[by[cid]]["anchors"]["threshold"] = text + "."
    res = [
        plant("A1", "a Requirement figure the threshold lacks (C1.2a at $70,000)",
              lambda d, cr: cr[by["C1.2a"]]["definition"].update(requirement="$70,000+ median wealth")),
        plant("A2", "the wealth Gini back in C4.4's threshold",
              lambda d, cr: pt(cr, "C4.4", cr[by["C4.4"]]["definition"]["pass_threshold"] + ", Gini <0.35 for wealth")),
        plant("A3", "a dated clause (C4.2 'by 2030')",
              lambda d, cr: pt(cr, "C4.2", cr[by["C4.2"]]["definition"]["pass_threshold"] + " by 2030")),
        plant("A4", "a US-only measure (C1.3 'area median income')",
              lambda d, cr: cr[by["C1.3"]]["definition"].update(measurement="affordability at 80% area median income")),
        plant("A5", "a clause that is not a substring of its threshold (C4.4)",
              lambda d, cr: cr[by["C4.4"]]["definition"]["clauses"].__setitem__(0, "Democratic accountability")),
        plant("A6", "an anchor threshold that differs from its definition (C2.6)",
              lambda d, cr: cr[by["C2.6"]]["anchors"].update(threshold="Civil-liberties score >=44.")),
        plant("A7", "a missing criterion (C3.6 dropped)",
              lambda d, cr: cr.pop(by["C3.6"])),
    ]
    ok = not clean and all(res)
    print(f"  {sum(res)} of {len(res)} planted violations rejected; clean document passes: {not clean}")
    print("SELFTEST " + ("PASS" if ok else "FAIL"))
    sys.exit(0 if ok else 1)


if "--selftest" in sys.argv[1:]:
    selftest()

fails = check_all(doc, blocks)

# ------------------------------------------------------------------ protocol
def note24():
    """Section 2.4's note on the v2.0 arithmetic, generated from the structure (ties: decision 45.6)."""
    n, om, nm = len(criteria), base["structure"]["domain_max"], doc["structure"]["domain_max"]
    new_ids = [c["id"] for c in criteria if c["id"] not in old]
    dom = {c["id"]: c["domain"] for c in criteria}
    groups = {}
    for dm in DOMAIN_IDS:
        if nm[dm] != om[dm]:
            groups.setdefault(int(nm[dm]), []).append(dm)
    parts = []
    for m, dms in sorted(groups.items(), key=lambda g: g[1]):
        ids = [x for x in new_ids if dom[x] in dms]
        label = ("Domain " if len(dms) == 1 else "Domains ") + and_list([d[1:] for d in dms])
        parts.append(f"{label} {'has' if len(dms) == 1 else 'have'} {words(m)} criteria"
                     f"{' each' if len(dms) > 1 else ''} ({', '.join(ids)}), maximum {m}")
    halves = [k / 2 for k in range(1, 2 * n) if (100 * k) % n == 0 and (100 * k // n) % 2 == 1]
    if halves:
        ties = (f"On {n}, {words(len(halves))} totals fall exactly on a half percent "
                f"({and_list([f'{t:g}' for t in halves])} give {and_list([f'{100 * t / n:g}%' for t in halves])}); "
                "they are rounded half up (decision 45.6), which Python's `round()` does not do.")
    else:
        ties = (f"On {n}, no total falls exactly on a half percent; should a structure produce one, it is rounded "
                "half up (decision 45.6), which Python's `round()` does not do.")
    text = ("**On the v2.0 criteria** (decision 45.1; in force for the corpus once the rescoring pass is applied): "
            f"{'; '.join(parts)}; Total maximum {n}; Percent is Total / {n} × 100; the tier bands are unchanged "
            "(2.5). " + ties)
    return textwrap.fill(text, 78, initial_indent="- ", subsequent_indent="  ", break_on_hyphens=False) + "\n"


single = [c["id"] for c in criteria if len(c["definition"]["clauses"]) == 1]
multi = [c for c in criteria if len(c["definition"]["clauses"]) > 1]
EDITS = [
    ("**Version 2.0-draft.5 — Session 36, 2026-09-22. Status: draft.",
     "**Version 2.0-draft.6 — Session 45, 2026-09-23. Status: draft."),
    ("structure\n(26 criteria in five domains), how uncertainty",
     f"structure\n(v2.0: {len(criteria)} criteria in five domains), how uncertainty"),
    ("**Changes from draft.4**",
     "**Changes from draft.5** (pinned as `SCORING_PROTOCOL_s44_snapshot.md`; this draft\nis generated from it by "
     "`build_criteria.py`, never edited by hand): this header;\n2.3, whose gap example and clause count describe the "
     "v2.0 criteria\n(`NEEC_Criteria_v2_s45.md`); 2.4, a note on v2.0's arithmetic; Appendix B,\nregenerated from "
     "`criteria.json`. Until the rescoring pass is applied, the\npublished scores, and every statement here about them, "
     "stay on the 26 criteria\nof Paper v1.4.\n\n**Changes from draft.4**"),
    ("not against its Requirement line where the two differ (C1.1\nstates an aspirational 95% requirement and an "
     "operative 90% / 85% threshold).\nIf you find another such gap, flag it rather than silently choosing.",
     "not against its Requirement line where the two differ. The v2.0\ncriteria carry no such gap, and "
     "`build_criteria.py` asserts it (Paper v1.4 had\nthem in C1.1, C1.2a, C1.3, C1.4, C3.3, C4.1 and C5.1). If you "
     "find one, flag it\nrather than silently choosing."),
    ("Twenty-one criteria have a Pass Threshold of more than one clause; Appendix B\nsplits each into its clauses, "
     "verbatim and in order. Five have one clause\n(C1.2a, C1.2b, C1.5, C2.2, C3.3).",
     f"{words(len(multi)).capitalize()} criteria have a Pass Threshold of more than one clause; Appendix B\nsplits "
     f"each into its clauses, verbatim and in order. {words(len(single)).capitalize()} have one clause\n"
     f"({', '.join(single)})."),
    ("- **Failures** is the number of criteria scored exactly 0.0.\n",
     "- **Failures** is the number of criteria scored exactly 0.0.\n" + note24()),
]
new_proto = proto
for o, n in EDITS:
    if new_proto.count(o) != 1:
        sys.exit(f"ERROR: protocol text to replace found {new_proto.count(o)} times: {o[:60]!r}")
    new_proto = new_proto.replace(o, n)
rows = []
for c in multi:
    d = c["definition"]
    cell = " ".join(f"({i}) {t}" for i, t in enumerate(d["clauses"], 1))
    if d.get("clause_scope"):
        cell += f"; every clause: {d['clause_scope']}"
    rows.append(f"| {c['id']} | {cell} |")
appb = ("## Appendix B. The clauses of each Pass Threshold (decision D28)\n\n"
        "Generated by `build_criteria.py` from `criteria.json` (the v2.0 criteria, Session 45);\n"
        "do not edit by hand. Each clause is a verbatim substring of the definition's Pass\n"
        "Threshold, in order; what the clauses leave over is connective text, or a scope\n"
        "that applies to every clause and is shown after the clauses. A 1.0 shows each\n"
        f"clause cleared on its own estimate (2.3). {words(len(single)).capitalize()} criteria have one clause: "
        f"{', '.join(single)}.\nThe Session 44 split, on Paper v1.4's thresholds, is pinned in\n"
        "`SCORING_PROTOCOL_s44_snapshot.md`.\n\n"
        "| Criterion | Clauses, in order |\n|---|---|\n" + "\n".join(rows) + "\n")
i = new_proto.index("## Appendix B.")
j = new_proto.find("\n## ", i + 5)
new_proto = new_proto[:i] + appb + ("" if j < 0 else new_proto[j:])

# ------------------------------------------------------------------ report
text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
print("build_criteria.py (version 2) -- NEEC v2.0 criteria")
print("=" * 92)
print(f"Base: {SNAP} (md5 {SNAP_MD5[:8]}, {len(base['criteria'])} criteria); record: {RECORD} (md5 "
      f"{md5(rec_bytes)[:8]}, {len(blocks)} blocks); clause splits: {PROTO_BASE} (md5 {PROTO_BASE_MD5[:8]})")
print(f"\n{'crit':6} {'class':5} {'codes':22} {'threshold':10} {'clauses':>7}  fields changed")
for cid, cls, codes, changed, ptc, n in LOG:
    print(f"{cid:6} {cls:5} {codes[:22]:22} {'restated' if ptc else '-':10} {n:>7}  {', '.join(changed) or '-'}")
cnt = {k: sum(1 for r in LOG if r[1] == k) for k in CLASSES}
print("\nClasses: " + "; ".join(f"{k} {cnt[k]} ({CLASSES[k]})" for k in CLASSES))
print(f"Thresholds restated or new: {sum(1 for r in LOG if r[4])}; one-clause criteria: {len(single)} "
      f"({', '.join(single)}); multi-clause: {len(multi)}")
print(f"Structure: {doc['structure']['criteria']} criteria, maximum {doc['structure']['total_max']:.0f}; domain "
      "maxima " + ", ".join(f"{k} {v:.0f}" for k, v in doc["structure"]["domain_max"].items()))
print("Registered quantities, each in one Pass Threshold:")
for q, pat in QUANTITIES.items():
    where = [c["id"] for c in criteria if re.search(pat, c["definition"]["pass_threshold"])]
    print(f"  {q:36} {', '.join(where)}")
print("\nAssertions A1-A7:")
for rule in ("A1", "A2", "A3", "A4", "A5", "A6", "A7"):
    fs = [m for r, m in fails if r == rule]
    print(f"  {rule}: {'pass' if not fs else 'FAIL'}")
    for m in fs:
        print(f"      {m}")
if fails:
    print(f"\n{len(fails)} assertion failure(s); nothing written.")
    sys.exit(1)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(text)
with open(PROTO_OUT, "w", encoding="utf-8") as fh:
    fh.write(new_proto)
print(f"\nWrote {OUT}: {len(criteria)} criteria, md5 {md5(text.encode('utf-8'))[:8]}.")
print(f"Wrote {PROTO_OUT}: {len(EDITS)} asserted edits and Appendix B regenerated from {PROTO_BASE}, md5 {md5(new_proto.encode('utf-8'))[:8]}.")
