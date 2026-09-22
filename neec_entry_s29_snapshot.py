#!/usr/bin/env python3
"""
neec_entry.py -- NEEC generic entry verifier and summary-block validator
========================================================================
Part of the reproducibility kit (decision D3), Session 27. Written to
SCORING_PROTOCOL.md, which it implements; the protocol section numbers are
cited inline. Session 28: scope.basis also accepts "assigned" (decision D17),
and the schema is cited under its file name on the mount (D20). No output for
a block valid before Session 28 changes.

WHAT IT CHECKS, FOR EVERY SUMMARY BLOCK (protocol section 9)
  * structure: the fields, types and values of summary_block_schema.json,
    re-implemented here so that no third-party package is needed;
  * the entry is in the canonical corpus with exactly this vector (D15), and
    under its CSV display name;
  * the stated summary (five domain totals, total, failures, tier) is the
    arithmetic of the vector (Appendix H.4 / protocol section 2);
  * every flag is well formed: its scored value is the vector's, its
    alternatives are other valid scores, a "both-directions" flag is a 0.5
    with both neighbours, a tracking flag tracks an independent flag;
  * every joint reading resolves only flagged criteria to their stated
    alternatives, consistently with tracking; the default readings are
    exactly the extremes of the flag register (D6, D16); every stated result
    is recomputed;
  * every scenario's stated result is recomputed.

WHAT IT COMPUTES
  * the exhaustive enumeration of the flag register (each independent call at
    its scored value or any alternative; tracking flags move with the call
    they track): combinations, reachable tiers, total and failure ranges, and
    the share of combinations that keep the scored tier (protocol 6.3);
  * tier robustness as decision D13 defines it: the tiers the joint readings
    reach, and their span in points and failures (protocol 6.4);
  * the peer matrix of decision D9: the entry's vector beside its declared
    peers or, if it declares none, its three nearest neighbours (protocol 5).

Comparative claims across entries are NOT checked here (decision D15): that
is the corpus-level checker's job. The --corpus table is an inventory, not a
set of claims.

Usage:
  python3 neec_entry.py --blocks FILE.json [--corpus] [--entry CODE]
  python3 neec_entry.py DOC.md [DOC.md ...]  [--corpus] [--entry CODE]
  python3 neec_entry.py --selftest
Exit status 0 only if every block validates. Looks for the canonical files
beside itself, then in the working directory; prints file names only.
Deterministic: no clock, no randomness, no dict-order dependence.
"""
import contextlib
import csv
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CANON_FILE = "neec_weighting_robustness_analysis_v2.py"
CSV_FILE = "neec_scores.csv"
SCHEMA_ID = "neec-summary-block/1.0"
VALUES = (0.0, 0.5, 1.0)
TIERS = ("Potentially Adequate", "Partially Adequate", "Structurally Inadequate")
TIER_ABBR = {"Potentially Adequate": "PA", "Partially Adequate": "Part", "Structurally Inadequate": "SI"}
SCOPE_CLASSES = ("mechanism", "configured_national_economy", "comprehensive_system")
FLAG_BASES = ("register", "stated", "direction-stated", "both-directions")
BEGIN = "<!-- NEEC-SUMMARY-BLOCK -->"
END = "<!-- /NEEC-SUMMARY-BLOCK -->"
BLOCK_RE = re.compile(re.escape(BEGIN) + r"\s*```json\n(.*?)\n```\s*" + re.escape(END), re.S)
EPS = 1e-9
CODE_OF = {}   # canonical key -> short code, filled from the blocks being checked


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name} beside this script or in the working directory")


# ------------------------------------------------------------------ corpus
def load_canon():
    spec = importlib.util.spec_from_file_location("_neec_canon", locate(CANON_FILE))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    rows = list(csv.DictReader(open(locate(CSV_FILE), encoding="utf-8", newline="")))
    keys = list(mod.SCORES)
    if len(rows) != len(keys):
        sys.exit(f"ERROR: {CSV_FILE} has {len(rows)} rows; the canonical corpus has {len(keys)} systems")
    display = {}
    for k, r in zip(keys, rows):
        if not r["system"].startswith(k):
            sys.exit(f"ERROR: CSV row '{r['system']}' does not correspond to canonical key '{k}'")
        display[k] = r["system"]
    return mod, list(mod.ALL_CRITS), mod.SCORES, display


CANON, CRITS, SCORES, DISPLAY = load_canon()
KEYS = list(SCORES)
DOMAINS = {f"D{d}": [c for c in CRITS if c.startswith(f"C{d}.")] for d in range(1, 6)}


def tier(failures):
    return TIERS[0] if failures <= 2 else TIERS[1] if failures <= 5 else TIERS[2]


def total(v):
    return sum(v[c] for c in CRITS)


def nfail(v):
    return sum(1 for c in CRITS if v[c] == 0.0)


def result(v):
    f = nfail(v)
    return {"total": total(v), "failures": f, "tier": tier(f)}


def applied(v, changes):
    out = dict(v)
    out.update(changes)
    return out


def fmt(x):
    return f"{x:.1f}"


# ------------------------------------------------------------------ JSON layout (deterministic, readable)
def _j(x):
    return json.dumps(x, ensure_ascii=False)


def dump_block(b):
    """Serialise a block in the fixed layout used in documents: one domain per vector line, one item per line."""
    out = ["{"]
    for k in ("schema", "key", "code", "display_name"):
        out.append(f'  {_j(k)}: {_j(b[k])},')
    out.append(f'  "record": {_j(b["record"])},')
    out.append(f'  "scope": {_j(b["scope"])},')
    out.append('  "vector": {')
    for i, (d, crits) in enumerate(DOMAINS.items()):
        sep = "," if i < 4 else ""
        out.append("    " + ", ".join(f"{_j(c)}: {_j(b['vector'][c])}" for c in crits) + sep)
    out.append("  },")
    out.append(f'  "summary": {_j(b["summary"])},')
    for name in ("flags", "joint_readings", "scenarios"):
        items = b[name]
        if not items:
            out.append(f'  "{name}": [],')
            continue
        out.append(f'  "{name}": [')
        for i, it in enumerate(items):
            out.append("    " + _j(it) + ("," if i < len(items) - 1 else ""))
        out.append("  ],")
    if "peers" in b:
        out.append(f'  "peers": {_j(b["peers"])},')
    out[-1] = out[-1].rstrip(",")
    out.append("}")
    text = "\n".join(out)
    if json.loads(text) != b:
        raise AssertionError(f"dump_block does not round-trip for {b.get('key')}")
    return text


def render_markdown(b):
    return f"{BEGIN}\n```json\n{dump_block(b)}\n```\n{END}"


def blocks_in_markdown(text):
    return [json.loads(m.group(1)) for m in BLOCK_RE.finditer(text)]


# ------------------------------------------------------------------ enumeration and D13
def levers(b):
    """Independent calls. Each lever is a list of options (dicts of changes); option 0 is the scored value."""
    flags = {f["criterion"]: f for f in b["flags"]}
    trackers = {}
    for f in b["flags"]:
        if f.get("tracks"):
            trackers.setdefault(f["tracks"], []).append(f)
    out = []
    for f in b["flags"]:
        if f.get("tracks"):
            continue
        opts = [{}]
        for i, alt in enumerate(f["alternatives"]):
            ch = {f["criterion"]: alt}
            for t in trackers.get(f["criterion"], []):
                ch[t["criterion"]] = t["alternatives"][i]
            opts.append(ch)
        out.append((f["criterion"], opts))
    return out, flags


def enumerate_register(b):
    """Exact enumeration by dynamic programming over (delta-failures) -> count, plus total bounds."""
    v = b["vector"]
    lv, _ = levers(b)
    base_t, base_f = total(v), nfail(v)
    dist = {0: 1}
    tmin = tmax = 0.0
    combos = 1
    for _, opts in lv:
        deltas = []
        for ch in opts:
            w = applied(v, ch)
            deltas.append((total(w) - base_t, nfail(w) - base_f))
        new = {}
        for df0, n in dist.items():
            for _, df in deltas:
                new[df0 + df] = new.get(df0 + df, 0) + n
        dist = new
        tmin += min(d[0] for d in deltas)
        tmax += max(d[0] for d in deltas)
        combos *= len(opts)
    by_tier = {}
    for df, n in dist.items():
        t = tier(base_f + df)
        by_tier[t] = by_tier.get(t, 0) + n
    return {
        "combinations": combos,
        "by_tier": {t: by_tier[t] for t in TIERS if t in by_tier},
        "keep_share": by_tier.get(tier(base_f), 0) / combos,
        "total_range": (base_t + tmin, base_t + tmax),
        "failure_range": (base_f + min(dist), base_f + max(dist)),
    }


def extremes(b):
    """The all-upward and all-downward resolutions of the register (tracking flags follow their call)."""
    v = b["vector"]
    lv, _ = levers(b)
    up, down = {}, {}
    for _, opts in lv:
        scored = [(total(applied(v, ch)), i) for i, ch in enumerate(opts)]
        hi = max(scored)[1]
        lo = min(scored)[1]
        up.update(opts[hi])
        down.update(opts[lo])
    return up, down


def d13(b):
    """Decision D13: tiers reached by the joint readings, and their span (points, failures)."""
    res = [r["result"] for r in b["joint_readings"]]
    reach = [t for t in TIERS if any(r["tier"] == t for r in res)]
    pts = max(r["total"] for r in res) - min(r["total"] for r in res)
    fl = max(r["failures"] for r in res) - min(r["failures"] for r in res)
    return {"reach": reach, "span_points": pts, "span_failures": fl, "robust": len(reach) == 1,
            "basis": sorted({r["basis"] for r in b["joint_readings"] if r["basis"] != "scored"}) or ["scored only"]}


def fragility_key(b, idx):
    m = d13(b)
    return (-len(m["reach"]), -m["span_failures"], -m["span_points"], idx)


def undisputed_failures(b):
    flagged_up = {f["criterion"] for f in b["flags"] if max(f["alternatives"]) > f["scored"]}
    return [c for c in CRITS if b["vector"][c] == 0.0 and c not in flagged_up]


# ------------------------------------------------------------------ validation
TOP = ("schema", "key", "code", "display_name", "record", "scope", "vector", "summary", "flags",
       "joint_readings", "scenarios")


def validate(b):
    E = []

    def need(cond, msg):
        if not cond:
            E.append(msg)
        return cond

    if not need(isinstance(b, dict), "block is not a JSON object"):
        return E
    missing = [k for k in TOP if k not in b]
    extra = [k for k in b if k not in TOP + ("peers",)]
    need(not missing, f"missing fields {missing}")
    need(not extra, f"unknown fields {extra}")
    if missing:
        return E
    need(b["schema"] == SCHEMA_ID, f"schema is {b['schema']!r}, expected {SCHEMA_ID!r}")
    key = b["key"]
    if not need(key in SCORES, f"key {key!r} is not in the canonical corpus"):
        return E
    need(bool(re.fullmatch(r"[A-Z]{2,5}", str(b["code"]))), f"code {b['code']!r} is not 2-5 capital letters")
    need(b["display_name"] == DISPLAY[key], f"display_name differs from the CSV ({DISPLAY[key]!r})")
    rec = b["record"]
    need(isinstance(rec, dict) and set(rec) == {"documents", "scored", "structure"}, "record fields")
    need(isinstance(rec.get("documents"), list) and rec.get("documents"), "record.documents is empty")
    need(rec.get("structure") in ("native-v2", "retrofit-step1c"), "record.structure")
    sc = b["scope"]
    need(isinstance(sc, dict) and sc.get("class") in SCOPE_CLASSES, "scope.class")
    need(sc.get("basis") in ("stated", "assigned", "proposed"), "scope.basis")
    need(set(sc) <= {"class", "basis", "population", "source"}, "scope has unknown fields")
    v = b["vector"]
    if not need(isinstance(v, dict) and list(v) == CRITS, "vector must list the 26 criteria in canonical order"):
        return E
    need(all(v[c] in VALUES for c in CRITS), "vector has a value outside {0.0, 0.5, 1.0}")
    need(all(abs(v[c] - SCORES[key][c]) < EPS for c in CRITS),
         "vector differs from the canonical corpus at " + ", ".join(c for c in CRITS if abs(v[c] - SCORES[key][c]) > EPS))
    s = b["summary"]
    need(set(s) == {"D1", "D2", "D3", "D4", "D5", "total", "failures", "tier"}, "summary fields")
    for d, cs in DOMAINS.items():
        need(abs(s.get(d, -1) - sum(v[c] for c in cs)) < EPS, f"summary {d} is not the sum of its criteria")
    r0 = result(v)
    need(abs(s.get("total", -1) - r0["total"]) < EPS, "summary total is not the sum of the vector")
    need(s.get("failures") == r0["failures"], "summary failures is not the number of 0.0 scores")
    need(s.get("tier") == r0["tier"], "summary tier does not follow from the failure count")
    # flags
    seen = set()
    order = []
    for f in b["flags"]:
        c = f.get("criterion")
        if not need(c in CRITS and c not in seen, f"flag criterion {c!r} unknown or repeated"):
            continue
        seen.add(c)
        order.append(CRITS.index(c))
        need(set(f) <= {"criterion", "scored", "alternatives", "basis", "reading", "tracks", "source"},
             f"{c}: unknown flag fields")
        need(abs(f.get("scored", -1) - v[c]) < EPS, f"{c}: flag's scored value differs from the vector")
        alts = f.get("alternatives", [])
        need(isinstance(alts, list) and 1 <= len(alts) <= 2 and all(a in VALUES for a in alts)
             and alts == sorted(set(alts)) and v[c] not in alts, f"{c}: alternatives {alts} invalid")
        need(f.get("basis") in FLAG_BASES, f"{c}: basis {f.get('basis')!r}")
        if f.get("basis") == "both-directions":
            need(v[c] == 0.5 and alts == [0.0, 1.0], f"{c}: a both-directions flag must be a 0.5 with alternatives [0.0, 1.0]")
    need(order == sorted(order), "flags are not in canonical criterion order")
    fl = {f["criterion"]: f for f in b["flags"] if f.get("criterion") in CRITS}
    for f in fl.values():
        t = f.get("tracks")
        if t:
            need(t in fl and not fl[t].get("tracks"), f"{f['criterion']}: tracks {t!r}, which is not an independent flag")
            if t in fl:
                need(len(fl[t]["alternatives"]) == len(f["alternatives"]),
                     f"{f['criterion']}: tracks {t} but has a different number of alternatives")
    if E:
        return E
    # joint readings
    jr = b["joint_readings"]
    ids = [r.get("id") for r in jr]
    need(len(ids) == len(set(ids)), "joint reading ids repeat")
    scored = [r for r in jr if r.get("basis") == "scored"]
    need(len(scored) == 1 and scored[0].get("resolve") == {}, "exactly one joint reading must be the scored one, with no changes")
    up, down = extremes(b)
    bases = [r.get("basis") for r in jr]
    if b["flags"]:
        if "stated" not in bases:
            need(sorted(bases) == ["extremes", "extremes", "scored"],
                 "an entry with flags and no stated joint readings must carry the two extremes (D16)")
    else:
        need(bases == ["scored"], "an entry without flags has only the scored reading")
    for r in jr:
        rid = r.get("id")
        need(set(r) == {"id", "label", "basis", "resolve", "result"}, f"reading {rid}: fields")
        ch = r.get("resolve", {})
        for c, val in ch.items():
            need(c in fl and val in fl[c]["alternatives"], f"reading {rid}: {c}={val} is not a flagged alternative")
        for c, f in fl.items():
            t = f.get("tracks")
            if t and (c in ch or t in ch):
                ok = (c in ch and t in ch and fl[t]["alternatives"].index(ch[t]) == f["alternatives"].index(ch[c]))
                need(ok, f"reading {rid}: {c} must move with {t}, which it tracks")
        if r.get("basis") == "extremes":
            need(ch in (up, down), f"reading {rid}: basis 'extremes' but resolve is not the all-up or all-down resolution")
        rr = result(applied(v, ch))
        need(r.get("result") == rr, f"reading {rid}: stated result {r.get('result')} != computed {rr}")
    if "extremes" in bases:
        got = [r["resolve"] for r in jr if r["basis"] == "extremes"]
        need(up in got and down in got, "the two extremes readings must be the all-up and all-down resolutions")
    # scenarios
    sids = [x.get("id") for x in b["scenarios"]]
    need(len(sids) == len(set(sids)), "scenario ids repeat")
    for x in b["scenarios"]:
        xid = x.get("id")
        need(set(x) == {"id", "label", "kind", "changes", "result"}, f"scenario {xid}: fields")
        need(x.get("kind") in ("scope", "other"), f"scenario {xid}: kind")
        ch = x.get("changes", {})
        need(bool(ch) and all(c in CRITS and val in VALUES and val != v[c] for c, val in ch.items()),
             f"scenario {xid}: changes must be non-empty and differ from the vector")
        rr = result(applied(v, ch))
        need(x.get("result") == rr, f"scenario {xid}: stated result {x.get('result')} != computed {rr}")
    for p in b.get("peers", []):
        need(p in SCORES and p != key, f"peer {p!r} is not another canonical entry")
    return E


# ------------------------------------------------------------------ reports
def nearest(key, k=3):
    v = SCORES[key]
    ds = sorted((sum(1 for c in CRITS if SCORES[o][c] != v[c]), KEYS.index(o), o) for o in KEYS if o != key)
    return [o for _, _, o in ds[:k]]


def entry_report(b, matrix=False):
    v, key = b["vector"], b["key"]
    s = b["summary"]
    out = [f"[{b['code']}] {key}  --  {fmt(s['total'])}/26, {s['failures']} failures, {s['tier']}",
           f"      scope: {b['scope']['class']} ({b['scope']['basis']}); record: {b['record']['structure']}"]
    lv, _ = levers(b)
    bases = {}
    for f in b["flags"]:
        bases[f["basis"]] = bases.get(f["basis"], 0) + 1
    out.append(f"      flags: {len(b['flags'])} criteria, {len(lv)} independent calls"
               + (" (" + ", ".join(f"{k} {bases[k]}" for k in FLAG_BASES if k in bases) + ")" if bases else ""))
    if b["flags"]:
        en = enumerate_register(b)
        out.append(f"      enumeration: {en['combinations']:,} combinations; "
                   + "; ".join(f"{TIER_ABBR[t]} {n:,}" for t, n in en["by_tier"].items())
                   + f"; totals {fmt(en['total_range'][0])}-{fmt(en['total_range'][1])}, "
                   f"failures {en['failure_range'][0]}-{en['failure_range'][1]}; "
                   f"keep scored tier {100 * en['keep_share']:.1f}%")
    for r in b["joint_readings"]:
        rr = r["result"]
        out.append(f"      reading {r['id']:7} {r['basis']:8} {fmt(rr['total']):>5}/26 {rr['failures']:2d} failures  "
                   f"{rr['tier']:24} {r['label']}")
    m = d13(b)
    out.append(f"      D13: joint readings reach {len(m['reach'])} tier(s) ({', '.join(TIER_ABBR[t] for t in m['reach'])}); "
               f"span {fmt(m['span_points'])} points / {m['span_failures']} failures; "
               + ("tier-robust" if m["robust"] else "not tier-robust"))
    for x in b["scenarios"]:
        rr = x["result"]
        out.append(f"      scenario {x['id']}: {fmt(rr['total'])}/26, {rr['failures']} failures, {rr['tier']} "
                   f"({len(x['changes'])} criteria moved; {x['label']})")
    und = undisputed_failures(b)
    out.append(f"      undisputed failures: {len(und)}" + (f" ({', '.join(und)})" if und else ""))
    if matrix:
        peers = b.get("peers") or nearest(key)
        how = "declared peers" if b.get("peers") else "three nearest neighbours (no peers declared)"
        out.append(f"      D9 peer matrix, {how}; '*' marks a criterion where the peer differs:")
        codes = [CODE_OF.get(p, p[:14]) for p in peers]
        out.append("        " + f"{'':6} {'entry':>6} " + " ".join(f"{c:>15}" for c in codes))
        for c in CRITS:
            cells = [f"{fmt(SCORES[p][c]) + ('*' if SCORES[p][c] != v[c] else ' '):>15}" for p in peers]
            out.append("        " + f"{c:6} {fmt(v[c]):>6} " + " ".join(cells))
        for p in peers:
            hi = sum(1 for c in CRITS if v[c] > SCORES[p][c])
            lo = sum(1 for c in CRITS if v[c] < SCORES[p][c])
            dom = ("dominates it" if lo == 0 and hi else "is dominated by it" if hi == 0 and lo else "neither dominates")
            out.append(f"        vs {p}: differs on {hi + lo}, higher on {hi}, lower on {lo}, "
                       f"total {total(v) - total(SCORES[p]):+.1f}; the entry {dom}")
    return out


def corpus_table(blocks):
    idx = {b["key"]: KEYS.index(b["key"]) for b in blocks}
    rows = sorted(blocks, key=lambda b: fragility_key(b, idx[b["key"]]))
    out = ["D13 inventory, least tier-robust first (reach, then failure span, then point span; ties in canonical order).",
           "Share = combinations of the full enumeration that keep the scored tier (secondary; assumes independence).",
           f"  {'code':5} {'tier':5} {'flags':>5} {'calls':>5} {'readings':10} {'reach':12} {'span':>11} "
           f"{'share':>7} {'combos':>10} {'undisputed':>10}"]
    for b in rows:
        m = d13(b)
        lv, _ = levers(b)
        share = f"{100 * enumerate_register(b)['keep_share']:.1f}%" if b["flags"] else "-"
        combos = f"{enumerate_register(b)['combinations']:,}" if b["flags"] else "1"
        out.append(f"  {b['code']:5} {TIER_ABBR[b['summary']['tier']]:5} {len(b['flags']):5d} {len(lv):5d} "
                   f"{'/'.join(m['basis']):10} {'/'.join(TIER_ABBR[t] for t in m['reach']):12} "
                   f"{fmt(m['span_points']):>5} / {m['span_failures']:2d} {share:>7} {combos:>10} "
                   f"{len(undisputed_failures(b)):10d}")
    return out


def selftest():
    key = KEYS[0]
    v = dict(SCORES[key])
    b = {"schema": SCHEMA_ID, "key": key, "code": "SELF", "display_name": DISPLAY[key],
         "record": {"documents": ["synthetic"], "scored": "self-test", "structure": "retrofit-step1c"},
         "scope": {"class": "configured_national_economy", "basis": "proposed"},
         "vector": v, "summary": dict({d: sum(v[c] for c in cs) for d, cs in DOMAINS.items()}, **result(v)),
         "flags": [], "joint_readings": [{"id": "scored", "label": "as scored", "basis": "scored", "resolve": {},
                                          "result": result(v)}], "scenarios": []}
    doc = "# Synthetic document\n\nProse.\n\n" + render_markdown(b) + "\n\nMore prose.\n"
    got = blocks_in_markdown(doc)
    ok = got == [b] and not validate(b)
    bad = json.loads(json.dumps(b))
    bad["vector"]["C1.1"] = 1.0 if v["C1.1"] != 1.0 else 0.0
    caught = bool(validate(bad))
    print(f"selftest: markdown round-trip {'ok' if ok else 'FAILED'}; altered vector rejected: {'yes' if caught else 'NO'}")
    return 0 if ok and caught else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    want_corpus = "--corpus" in argv
    entry = argv[argv.index("--entry") + 1] if "--entry" in argv else None
    blocks, sources = [], []
    if "--blocks" in argv:
        fn = argv[argv.index("--blocks") + 1]
        data = json.load(open(locate(fn), encoding="utf-8"))
        blocks = data if isinstance(data, list) else [data]
        sources = [fn] * len(blocks)
    else:
        docs = [a for a in argv if a.endswith(".md")]
        for fn in docs:
            found = blocks_in_markdown(open(locate(fn), encoding="utf-8").read())
            if not found:
                print(f"FAIL {fn}: no summary block between {BEGIN} and {END}")
            blocks += found
            sources += [fn] * len(found)
    if not blocks:
        print("usage: neec_entry.py --blocks FILE.json | DOC.md ... [--corpus] [--entry CODE] | --selftest")
        return 2
    CODE_OF.update({b["key"]: b["code"] for b in blocks if isinstance(b, dict) and "key" in b and "code" in b})
    print(f"neec_entry.py -- {len(blocks)} summary block(s); canonical corpus: {len(SCORES)} systems")
    print("=" * 92)
    failures = 0
    codes = [b.get("code") for b in blocks]
    if len(codes) != len(set(codes)):
        print("FAIL: codes repeat across blocks")
        failures += 1
    for b, src in zip(blocks, sources):
        errs = validate(b)
        if errs:
            failures += 1
            print(f"FAIL [{b.get('code')}] {b.get('key')} ({src})")
            for e in errs:
                print(f"      - {e}")
            continue
        print(f"PASS [{b['code']}] {b['key']}")
        if entry is None or entry == b["code"]:
            for line in entry_report(b, matrix=(entry == b["code"]))[1:]:
                print(line)
    if want_corpus and not failures:
        print()
        for line in corpus_table(blocks):
            print(line)
        covered = {b["key"] for b in blocks}
        print(f"\nCoverage: {len(covered)} of {len(SCORES)} canonical systems carry a block"
              + ("" if covered == set(SCORES) else "; missing: " + ", ".join(k for k in KEYS if k not in covered)))
    print("\n" + ("ALL BLOCKS VALID." if not failures else f"{failures} block(s) FAILED."))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
