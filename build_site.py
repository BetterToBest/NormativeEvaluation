#!/usr/bin/env python3
"""build_site.py: generate the NEEC public site (docs/) from the canonical files.

Version 1.0, written for Session 49 (site package prepared 2026-09-24; decisions S1 to S8 in
NEEC_Site_Package_s49.md). The site's design is governed by NEEC_Site_Design_Brief_s45.md.

Reads, and never writes: criteria.json; neec_corpus.json and neec_scores.csv; the summary blocks named
in site/config.json; wjp_rol_sf62_2012_2025.csv (md5 checked); the Appendix A.4 weighting script, whose
SCHEMES it imports unmodified; NEEC_Criteria_v2_s45.md (to confirm each cited decision exists); and the
hand-maintained sources in site/ (config.json, thresholds.json, pages/*.html, assets/).
Writes: docs/, and nothing else.

Scores are shown only when site/config.json sets scores.publish to true, and then only if the corpus
has exactly the criteria of criteria.json and every total, failure count and tier equals neec_scores.csv.

  python3 build_site.py                 write docs/
  python3 build_site.py --check         rebuild in a temporary directory and compare it with docs/;
                                        prints one line and exits 1 on any difference
  python3 build_site.py --preview DIR   write a preview to DIR (never docs/) that shows the corpus's
                                        published scores whatever the gate says, under a preview banner

Standard library only. The output is byte-deterministic: no dates, no random ordering.
"""
import argparse
import contextlib
import csv
import hashlib
import html
import importlib.util
import io
import json
import os
import re
import shutil
import statistics
import sys
import tempfile
from decimal import Decimal, ROUND_HALF_UP
from urllib.parse import quote

VERSION = "1.0"
HERE = os.path.dirname(os.path.abspath(__file__))


def P(*a):
    return os.path.join(HERE, *a)


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def esc(s):
    return html.escape(str(s), quote=True)


def inline(s):
    """Escape, then render the two inline marks the criteria texts use: *italic* and `code`."""
    t = esc(s)
    t = re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", t)
    t = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", t)
    return t


def cslug(cid):
    return cid.lower().replace(".", "-")


def sslug(code):
    return code.lower()


def fmt(x):
    return f"{x:.1f}"


def fmax(x):
    """A maximum: 26, not 26.0."""
    return str(int(x)) if float(x).is_integer() else fmt(x)


def pct(total, mx):
    """Percent rounded half up (decision 45.6), never Python's round-half-even."""
    return int((Decimal(str(total)) * 100 / Decimal(str(mx))).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


SCORE_WORD = {1.0: "pass", 0.5: "partial", 0.0: "structural failure"}
SCORE_CLASS = {1.0: "s10", 0.5: "s05", 0.0: "s00"}
NUMBER_WORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve"}


def score_text(v):
    if v is None:
        return "not yet published"
    return f"{fmt(v)}, {SCORE_WORD[v]}"


def mark(v, extra=""):
    cls = "sp" if v is None else SCORE_CLASS[v]
    return f'<span class="mk {cls}{extra}" aria-hidden="true"></span>'


# --------------------------------------------------------------------------------------------------
# Load and check
# --------------------------------------------------------------------------------------------------

def load(preview):
    cfg = json.load(open(P("site", "config.json"), encoding="utf-8"))
    cat = json.load(open(P("site", "thresholds.json"), encoding="utf-8"))
    src = cfg["sources"]
    crit = json.load(open(P(src["criteria"]), encoding="utf-8"))
    corpus = json.load(open(P(cfg["scores"]["corpus"]), encoding="utf-8"))
    blocks = json.load(open(P(cfg["scores"]["summary_blocks"]), encoding="utf-8"))
    record = open(P(src["record"]), encoding="utf-8").read()
    with open(P(cfg["scores"]["csv"]), newline="", encoding="utf-8") as f:
        csv_rows = list(csv.DictReader(f))
    w = src["wjp"]
    assert md5(P(w["file"])) == w["md5"], f"{w['file']} is not the extract decision 47.1 read"
    with open(P(w["file"]), newline="", encoding="utf-8") as f:
        wjp_rows = list(csv.DictReader(f))
    spec = importlib.util.spec_from_file_location("a4", P(src["weights"]["script"]))
    a4 = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(a4)
    return dict(cfg=cfg, cat=cat, crit=crit, corpus=corpus, blocks=blocks, record=record,
                csv_rows=csv_rows, wjp_rows=wjp_rows, a4=a4, preview=preview)


def model(L):
    cfg, crit, corpus = L["cfg"], L["crit"], L["corpus"]
    domains = crit["domains"]
    cmap = {c["id"]: c for c in crit["criteria"]}
    order = [cid for d in domains for cid in d["criteria"]]
    assert sorted(order) == sorted(cmap) and len(order) == crit["structure"]["criteria"], "criteria.json structure"
    dom_of = {cid: d["id"] for d in domains for cid in d["criteria"]}
    dmap = {d["id"]: d for d in domains}

    gate = cfg["scores"]["publish"]
    publish = gate or L["preview"]
    corpus_crits = corpus["criteria"]
    assert set(corpus_crits) <= set(order), "the corpus scores a criterion criteria.json does not define"
    if gate:
        assert sorted(corpus_crits) == sorted(order), (
            "scores.publish is true but the corpus is not on the criteria of criteria.json; "
            "publish only the v2.0 corpus")
    blocks = {b["code"]: b for b in L["blocks"]}
    csv_by = {r["system"]: r for r in L["csv_rows"]}
    tiers = crit["tiers"]

    def tier_of(fails):
        for t in tiers:
            if t["failures_min"] <= fails <= t["failures_max"]:
                return t["name"]
        raise AssertionError(fails)

    systems = []
    for e in corpus["entries"]:
        code = e["code"]
        conf = cfg["systems"].get(code, {})
        blk = blocks.get(code, {})
        s = dict(code=code, key=e["key"], name=e["display_name"], short=conf.get("short", e["display_name"]),
                 slug=sslug(code), scope=e["scope_class"],
                 docs=blk.get("record", {}).get("documents", []),
                 scored=blk.get("record", {}).get("scored", ""),
                 vector=None)
        assert s["scope"] in cfg["scope_classes"], f"unknown scope class {s['scope']}"
        if publish:
            v = e["vector"]
            assert set(v) == set(corpus_crits), f"{code}: vector does not cover the corpus criteria"
            assert all(x in (0.0, 0.5, 1.0) for x in v.values()), f"{code}: score off the scale"
            s["vector"] = {cid: v.get(cid) for cid in order}
            s["total"] = sum(v.values())
            s["max"] = float(len(corpus_crits))
            s["pct"] = pct(s["total"], s["max"])
            s["failures"] = sum(1 for x in v.values() if x == 0.0)
            s["tier"] = tier_of(s["failures"])
            s["domains"] = {}
            for d in domains:
                cs = [cid for cid in d["criteria"] if cid in v]
                s["domains"][d["id"]] = dict(crits=cs, sum=sum(v[c] for c in cs), max=float(len(cs)))
            row = csv_by.get(e["display_name"]) or csv_by.get(e["key"])
            assert row is not None, f"{e['display_name']} missing from the CSV"
            assert int(row["total_percent"].rstrip("%")) == s["pct"], f"{code}: percent differs from the CSV"
            assert int(row["criteria_count"]) == len(corpus_crits), "CSV and corpus on different structures"
            assert float(row["total_score"]) == s["total"], f"{code}: total differs from the CSV"
            assert int(row["failures"]) == s["failures"], f"{code}: failures differ from the CSV"
            assert row["adequacy_tier"] == s["tier"], f"{code}: tier differs from the CSV"
            s["flags"] = blk.get("flags", [])
            s["readings"] = blk.get("joint_readings", [])
        systems.append(s)
    assert len({s["code"] for s in systems}) == len(systems)
    if publish:
        assert len(L["csv_rows"]) == len(systems), "the CSV and the corpus hold different systems"

    # Competition ranks and field order
    if publish:
        totals = sorted((s["total"] for s in systems), reverse=True)
        for s in systems:
            s["rank"] = totals.index(s["total"]) + 1
            s["tied"] = totals.count(s["total"]) > 1
        tier_idx = {t["name"]: i for i, t in enumerate(tiers)}
        systems.sort(key=lambda s: (tier_idx[s["tier"]], -s["total"], s["short"].lower()))
    else:
        so = cfg["scope_order"]
        systems.sort(key=lambda s: (so.index(s["scope"]), s["short"].lower()))

    M = dict(cfg=cfg, crit=crit, cmap=cmap, order=order, dom_of=dom_of, dmap=dmap, domains=domains,
             publish=publish, gate=gate, preview=L["preview"], systems=systems, corpus_crits=corpus_crits,
             tiers=tiers, record=L["record"])
    M["smap"] = {s["code"]: s for s in systems}
    M["catalog"] = check_catalog(L["cat"], M)
    M["wjp"] = wjp_model(L["wjp_rows"], M)
    M["schemes"] = scheme_model(L["a4"], M)
    M["framework"] = framework_model(M)
    M["findings"] = findings(M) if publish else []
    M["src_md5"] = {k: md5(P(v))[:8] for k, v in (("criteria.json", cfg["sources"]["criteria"]),
                                                    ("neec_corpus.json", cfg["scores"]["corpus"]))}
    return M


def check_catalog(cat, M):
    for e in cat["entries"]:
        for c in e["criteria"]:
            assert c in M["cmap"], f"thresholds.json {e['id']}: unknown criterion {c}"
        if e["clause"]:
            c, i = e["clause"]
            assert 1 <= i <= len(M["cmap"][c]["definition"]["clauses"]), f"{e['id']}: no clause {i} in {c}"
        for d in e["decisions"]:
            assert f"**{d} " in M["record"] or f"**{d}**" in M["record"], f"{e['id']}: decision {d} not in the record"
    ids = [e["id"] for e in cat["entries"]]
    assert len(ids) == len(set(ids))
    return cat["entries"]


def wjp_model(rows, M):
    entry = next(e for e in M["catalog"] if e.get("interactive") == "wjp")
    clause = M["cmap"]["C4.6"]["definition"]["clauses"][entry["clause"][1] - 1]
    bar = float(re.search(r"(\d\.\d\d) or more", clause).group(1))
    by_ed = {}
    for r in rows:
        by_ed.setdefault(r["edition"], []).append([r["code"], r["jurisdiction"], float(r["sf62"])])
    eds = sorted(by_ed)
    cur = {c: (n, x) for c, n, x in by_ed["2025"]}
    vals = sorted(x for _, _, x in by_ed["2025"])
    q = statistics.quantiles(vals, n=4, method="inclusive")
    med = statistics.median(vals)
    assert round(q[2], 2) == bar, "C4.6's bar is no longer the 2025 upper quartile the record states (47.1)"
    ref = entry["reference"]
    cne = {s["code"] for s in M["systems"] if s["scope"] == "configured_national_economy"}
    assert cne == set(ref) | set(entry["not_covered"]), "every configured national economy needs a reference or a note"
    refs = []
    for code, jurs in ref.items():
        for j in jurs:
            refs.append(dict(system=code, code=j, name=cur[j][0], value=round(cur[j][1], 2)))
    meet = sum(1 for x in vals if round(x, 2) >= bar)
    same = [b / 100 for b in range(1, 100) if all((r["value"] >= b / 100) == (r["value"] >= bar) for r in refs)]
    return dict(entry=entry, bar=bar, median=round(med, 2), q3=round(q[2], 4), n=len(vals), meet=meet,
                same=(min(same), max(same)), refs=refs, editions=eds,
                data={ed: sorted(by_ed[ed], key=lambda r: r[2]) for ed in eds})


def scheme_model(a4, M):
    out = []
    for sc in M["cfg"]["weight_schemes"]:
        w = {cid: 1.0 for cid in M["order"]}
        for cid in M["order"]:
            w[cid] *= sc["domains"].get(M["dom_of"][cid], 1.0)
        for cid, k in sc["criteria"].items():
            w[cid] *= k
        ref = a4.SCHEMES[sc["name"]]
        assert all(ref[c] == w[c] for c in a4.ALL_CRITS), f"{sc['name']} no longer matches {a4.__name__}.SCHEMES"
        out.append(dict(name=sc["name"], label=sc["label"], domains=sc["domains"], criteria=sc["criteria"]))
    assert len(out) == len(a4.SCHEMES)
    assert not out[0]["domains"] and not out[0]["criteria"], "the first scheme must be the equal-weight baseline"
    return out


def framework_model(M):
    """The layers above the criteria, as the Paper states them: premises (section 3) and core criteria
    N1 to N14 (section 4). Each applied criterion's links come from its derivation in criteria.json."""
    t = open(P(M["cfg"]["sources"]["paper"]), encoding="utf-8").read().replace("\\", "")
    prem = [dict(n=int(a), title=b.strip(), text=c.strip()) for a, b, c in
            re.findall(r"^### Premise (\d+): (.+?)\s*\n+\*\*Statement:\*\* (.+?)\s*\n", t, flags=re.M)]
    prin = [dict(n=int(a), title=b.strip(), text=c.strip()) for a, b, c in
            re.findall(r"^### N(\d+)\. (.+?)\s*\n+\*\*Principle:\*\* (.+?)\s*\n", t, flags=re.M)]
    assert prem and [p["n"] for p in prem] == list(range(1, len(prem) + 1)), "the Paper's premises"
    assert prin and [p["n"] for p in prin] == list(range(1, len(prin) + 1)), "the Paper's core criteria"
    links = {cid: sorted({int(n) for n in re.findall(r"N(\d+)\s*\(", M["cmap"][cid]["definition"]["derivation"])})
             for cid in M["order"]}
    assert all(links.values()), "a criterion whose derivation names no core criterion"
    assert {n for v in links.values() for n in v} <= {p["n"] for p in prin}, "a derivation cites an unknown core criterion"
    return dict(premises=prem, principles=prin, links=links)


def domain_pcts(s, M):
    return [s["domains"][d["id"]]["sum"] / s["domains"][d["id"]]["max"] * 100 if s["domains"][d["id"]]["max"] else 0.0
            for d in M["domains"]]


def frontier2(points):
    """Points no other point matches or beats on both axes and beats on one."""
    return [p for p in points if not any(q[1] >= p[1] and q[2] >= p[2] and (q[1] > p[1] or q[2] > p[2]) for q in points)]


def dominates(a, b, crits):
    return all(a[c] >= b[c] for c in crits) and any(a[c] > b[c] for c in crits)


def findings(M):
    S, crits = M["systems"], M["corpus_crits"]
    out = []
    counts = [(t["name"], sum(1 for s in S if s["tier"] == t["name"])) for t in M["tiers"]]
    out.append(f"{len(S)} systems on {len(crits)} criteria: " +
               ", ".join(f"{n} {esc(t)}" for t, n in counts) + ". Tiers depend only on the number of "
               "structural failures, so they do not move with the weights.")
    cne = [s for s in S if s["scope"] == "configured_national_economy"]
    if cne:
        top = max(s["total"] for s in cne)
        bs = [s for s in cne if s["total"] == top]
        b = bs[0]
        names = " and ".join(esc(x["short"]) for x in bs)
        out.append(f"Among the configured national economies, existing or historical, the highest total is "
                   f"{names}'s: {fmt(b['total'])} of {fmax(b['max'])} ({b['pct']}%)" +
                   (f", with {b['failures']} structural failure{'s' if b['failures'] != 1 else ''}, {esc(b['tier'])}." if len(bs) == 1 else "."))
    tix = {t["name"]: i for i, t in enumerate(M["tiers"])}
    best = None
    for a in S:
        for b in S:
            if a["total"] > b["total"] and tix[a["tier"]] > tix[b["tier"]]:
                key = (tix[a["tier"]] - tix[b["tier"]], a["total"] - b["total"])
                if best is None or key > best[0]:
                    best = (key, a, b)
    if best:
        _, a, b = best
        gap = best[0][0]
        out.append(f"A higher total can sit in a lower tier: {esc(a['short'])} ({fmt(a['total'])}, "
                   f"{a['failures']} failures) outscores {esc(b['short'])} ({fmt(b['total'])}, "
                   f"{b['failures']} failures) and sits {'one tier' if gap == 1 else f'{gap} tiers'} lower.")
    none10 = [c for c in crits if not any(s["vector"][c] == 1.0 for s in S)]
    if none10:
        out.append(f"No system scores 1.0 on {len(none10)} of the {len(crits)} criteria: " +
                   ", ".join(f'<a href="{{root}}criteria/{cslug(c)}.html">{c}</a>' for c in none10) + ".")
    fails = sorted(((sum(1 for s in S if s["vector"][c] == 0.0), c) for c in crits), key=lambda t: (-t[0], t[1]))
    top = [c for n, c in fails if n == fails[0][0]]
    out.append(f"The most often failed criterion is " + " and ".join(
        f'<a href="{{root}}criteria/{cslug(c)}.html">{c} {esc(M["cmap"][c]["name"])}</a>' for c in top) +
        f": {fails[0][0]} of {len(S)} systems score 0.0 on it.")
    nd = [s for s in S if not any(dominates(o["vector"], s["vector"], crits) for o in S if o is not s)]
    out.append(f"{len(nd)} systems are not dominated: no other system scores at least as high on every "
               f"criterion and higher on one. " + ", ".join(esc(s["short"]) for s in nd) + ".")
    return out


# --------------------------------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------------------------------

WORDMARK = ('<svg class="wm-marks" viewBox="0 0 46 14" aria-hidden="true" focusable="false">'
            '<circle cx="7" cy="7" r="5.5" class="wm1"/>'
            '<circle cx="23" cy="7" r="5" class="wm-ring"/><path d="M23 2 a5 5 0 0 1 0 10z" class="wm1"/>'
            '<circle cx="39" cy="7" r="5" class="wm-ring wm0"/></svg>')


class Site:
    def __init__(self, M, out):
        self.M, self.out, self.files, self.pages = M, out, {}, []
        c = M["cfg"]["site"]
        self.repo, self.raw, self.base = c["repo"], c["raw"], c["base_url"]

    def blob(self, f):
        return f"{self.repo}/blob/main/{quote(f)}"

    def issue(self, form, **prefill):
        name = self.M["cfg"]["issue_forms"][form]
        path = P(".github", "ISSUE_TEMPLATE", name)
        assert os.path.exists(path), f"issue form {name} does not exist"
        ids = set(re.findall(r"^\s+id: (\w+)", open(path, encoding="utf-8").read(), flags=re.M))
        assert set(prefill) - {"title"} <= ids, f"{name} has no field {sorted(set(prefill) - {'title'} - ids)}"
        q = "&".join(f"{k}={quote(str(v))}" for k, v in prefill.items() if v)
        return f"{self.repo}/issues/new?template={self.M['cfg']['issue_forms'][form]}" + (f"&{q}" if q else "")

    def discuss(self, title):
        c = self.M["cfg"]["site"]
        if not c["discussions"]:
            return ""
        return (f'<a class="btn quiet" href="{self.repo}/discussions/new?category={c["discussion_category"]}'
                f'&title={quote(title)}">Discuss it openly</a>')

    def put(self, rel, text):
        assert rel not in self.files, rel
        self.files[rel] = text.encode("utf-8") if isinstance(text, str) else text

    def page(self, rel, pid, title, desc, main, data=None, jsonld=None, absolute=False):
        depth = rel.count("/")
        root = self.base if absolute else "../" * depth
        M, cfg = self.M, self.M["cfg"]
        nav = "".join(
            f'<li><a href="{root}{n["href"]}"{" aria-current=\"page\"" if n["id"] == pid else ""}>{esc(n["label"])}</a></li>'
            for n in cfg["nav"])
        banner = ""
        if M["preview"]:
            banner = ('<p class="banner" role="note">Preview build. It shows the corpus\'s published scores '
                      f'({len(M["corpus_crits"])} criteria, being re-estimated for version {esc(cfg["scores"]["release"])}); '
                      'the public site shows no scores until version 2.0 is released.</p>')
        full_title = esc(title) + ("" if pid == "home" else " | NEEC")
        head_data = ""
        if data is not None:
            head_data = ('<script type="application/json" id="neec-data">' +
                         json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/") +
                         "</script>")
        ld = ""
        if jsonld:
            ld = ('<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False, sort_keys=True) + "</script>")
        url = self.base + ("" if rel == "index.html" else rel)
        main = main.replace("{root}", root)
        doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{esc(desc)}">
<meta name="color-scheme" content="light dark">
<meta name="generator" content="build_site.py {VERSION}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
{"" if M["preview"] else f'<link rel="preload" href="{root}assets/fonts/source-serif-4-roman.woff2" as="font" type="font/woff2" crossorigin>'}
<link rel="stylesheet" href="{root}assets/neec.css">
<link rel="alternate" type="text/plain" href="{root}llms.txt" title="A plain-text guide for AI systems">
<link rel="alternate" type="application/json" href="{root}data/neec.json" title="The site's data">
{ld}
</head>
<body class="p-{pid}">
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
<a class="wordmark" href="{root}index.html" aria-label="NEEC home">{WORDMARK}<span>NEEC</span></a>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</header>
{banner}
<main id="main">
{main}
</main>
{self.footer(root)}
{head_data}
<script src="{root}assets/neec.js" defer></script>
</body>
</html>
"""
        shell = doc.replace(head_data, "") if head_data else doc
        assert not re.search(r"\{\{\w+\}\}|\{root\}|\[\[/?(audit|blind)\]\]", shell), f"{rel}: unreplaced placeholder"
        self.put(rel, doc)
        self.pages.append(rel)

    def footer(self, root):
        M, c = self.M, self.M["cfg"]["site"]
        n = len(M["order"])
        return f"""<footer class="colophon">
<p>NEEC is part of the <a href="{c['hub']}">Better To Best Research Hub</a>. Written by {esc(c['authors'])}.
Text and data under <a href="{c['licence_url']}">{esc(c['licence_name'])}</a>.</p>
<p><a href="{self.repo}">Repository</a> <a href="{root}replicate.html">Replicate</a> <a href="{root}contribute.html">Report an error</a> <a href="{root}llms.txt">For AI systems</a></p>
<p class="build">Built by <code>build_site.py</code> {VERSION} from <code>criteria.json</code> ({n} criteria, md5 {M['src_md5']['criteria.json']}) and <code>neec_corpus.json</code> (md5 {M['src_md5']['neec_corpus.json']}).</p>
</footer>"""

    def fragment(self, name, **values):
        t = open(P("site", "pages", name), encoding="utf-8").read()
        for k, v in values.items():
            t = t.replace("{{" + k + "}}", str(v))
        left = re.findall(r"\{\{(\w+)\}\}", t)
        assert not left, f"site/pages/{name}: no value for {left}"
        return t

    def write(self):
        if os.path.isdir(self.out):
            shutil.rmtree(self.out)
        for rel, b in sorted(self.files.items()):
            path = os.path.join(self.out, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(b)


# --------------------------------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------------------------------

def legend(M):
    items = [("s10", "1.0, pass"), ("s05", "0.5, partial"), ("s00", "0.0, structural failure")]
    if not M["publish"] or len(M["corpus_crits"]) < len(M["order"]):
        items.append(("sp", "not yet published"))
    return ('<ul class="legend" aria-label="Key">' +
            "".join(f'<li><span class="mk {c}" aria-hidden="true"></span>{esc(t)}</li>' for c, t in items) + "</ul>")


def field(M, caption):
    doms = M["domains"]
    pub = M["publish"]
    head1 = '<tr class="fd-dom"><td></td>' + "".join(
        f'<th scope="colgroup" colspan="{len(d["criteria"])}" class="dh {d["id"].lower()}">{esc(d["name"])}</th>'
        for d in doms) + ('<td colspan="2"></td>' if pub else "") + "</tr>"
    cols = []
    for d in doms:
        for i, cid in enumerate(d["criteria"]):
            c = M["cmap"][cid]
            first = " ds" if i == 0 else ""
            cols.append(f'<th scope="col" class="ch {d["id"].lower()}{first}" data-c="{cid}">'
                        f'<a href="{{root}}criteria/{cslug(cid)}.html" tabindex="-1">'
                        f'<span aria-hidden="true">{cid[1:]}</span><span class="vh">{cid} {esc(c["name"])}</span></a></th>')
    tail = ('<th scope="col" class="tot">Total</th><th scope="col" class="fl">Failures</th>' if pub else "")
    head2 = f'<tr class="fd-codes"><th scope="col" class="sys-h"><span class="vh">System</span></th>{"".join(cols)}{tail}</tr>'
    ncols = 1 + len(M["order"]) + (2 if pub else 0)
    groups = []
    if pub:
        for t in M["tiers"]:
            rows = [s for s in M["systems"] if s["tier"] == t["name"]]
            if rows:
                hi = t["failures_max"] if t["failures_max"] < len(M["order"]) else None
                span = f'{t["failures_min"]} to {hi}' if hi is not None else f'{t["failures_min"]} or more'
                groups.append((f'{t["name"]}<span class="gl-note">{span} structural failures</span>', rows))
    else:
        for sc in M["cfg"]["scope_order"]:
            rows = [s for s in M["systems"] if s["scope"] == sc]
            if rows:
                groups.append((esc(M["cfg"]["scope_classes"][sc]["plural"]), rows))
    body = []
    for label, rows in groups:
        tr = [f'<tr class="gl"><th scope="rowgroup" colspan="{ncols}">{label}</th></tr>']
        for s in rows:
            cells = []
            for d in doms:
                for i, cid in enumerate(d["criteria"]):
                    v = s["vector"][cid] if pub else None
                    cls = ("sn" if pub and v is None else "sp") if v is None else SCORE_CLASS[v]
                    txt = "not scored in this data" if cls == "sn" else score_text(v)
                    first = " ds" if i == 0 else ""
                    cells.append(f'<td class="m {cls} {d["id"].lower()}{first}" data-c="{cid}">'
                                 f'<span class="mk" aria-hidden="true"></span><span class="vh">{txt}</span></td>')
            tot = ""
            if pub:
                tot = (f'<td class="tot">{fmt(s["total"])}</td>'
                       f'<td class="fl{" has" if s["failures"] else ""}">{s["failures"]}</td>')
            tr.append(f'<tr data-s="{s["code"]}"><th scope="row" class="sys"><a href="{{root}}systems/{s["slug"]}.html">'
                      f'{esc(s["short"])}</a></th>{"".join(cells)}{tot}</tr>')
        body.append("<tbody>" + "".join(tr) + "</tbody>")
    return (f'<figure class="field-wrap bleed">'
            f'<p class="field-cap" aria-hidden="true">{caption}</p>'
            f'<div class="field-scroll" tabindex="-1">'
            f'<table class="field{" pending" if not pub else ""}" id="field">'
            f'<caption class="vh">{caption}</caption>'
            f'<thead>{head1}{head2}</thead>{"".join(body)}</table></div>'
            f'<figcaption>{legend(M)}<p class="field-help">Select a mark, or move through the field with the '
            f'arrow keys, to see the criterion and a link to the evidence.</p></figcaption>'
            f'<div class="pop" id="pop" role="status" hidden></div></figure>')


def field_data(M):
    return {
        "publish": M["publish"],
        "criteria": {cid: [M["cmap"][cid]["name"], M["dom_of"][cid]] for cid in M["order"]},
        "systems": {s["code"]: [s["short"], s["slug"]] for s in M["systems"]},
    }


def score_data(M):
    """Everything the explorers need, when scores are published."""
    if not M["publish"]:
        return None
    return {
        "order": M["order"],
        "scored": M["corpus_crits"],
        "domains": [[d["id"], d["name"], d["criteria"]] for d in M["domains"]],
        "tiers": [[t["name"], t["failures_min"], t["failures_max"]] for t in M["tiers"]],
        "systems": [dict(code=s["code"], short=s["short"], slug=s["slug"], vector=s["vector"], total=s["total"],
                         failures=s["failures"], tier=s["tier"],
                         readings=[dict(label=r["label"], id=r["id"], resolve=r["resolve"], result=r["result"])
                                   for r in s["readings"]]) for s in M["systems"]],
        "schemes": M["schemes"],
    }


def pending_note(M, what):
    c = M["cfg"]["site"]
    what = (what + " ") if what else ""
    return (f'<p class="pending-note">{what}Version {esc(M["cfg"]["scores"]["release"])} scores are being finalized; '
            f'this appears when they are published. Version 1 scores remain on the '
            f'<a href="{c["v1_site"]}">original NEEC site</a>.</p>')


def buttons(*items):
    items = [i for i in items if i]
    return '<p class="actions">' + "".join(items) + "</p>" if items else ""


def btn(href, label, quiet=False):
    return f'<a class="btn{" quiet" if quiet else ""}" href="{href}">{esc(label)}</a>'


# --------------------------------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------------------------------

def page_home(S):
    M, c = S.M, S.M["cfg"]["site"]
    n_s, n_c = len(M["systems"]), len(M["order"])
    if M["publish"]:
        cap = (f"{NUMBER_WORDS.get(n_s, n_s) if n_s <= 12 else n_s} systems, one mark per criterion, "
               f"grouped by domain and ordered by tier.")
        find = "<ul class=\"findings\">" + "".join(f"<li>{f}</li>" for f in M["findings"]) + "</ul>"
        find += '<p><a href="findings.html">The findings as charts</a>: totals and failures, domain profiles, and trade-offs.</p>'
        find += ('<p class="limits">Totals use equal weights and are one reading of the evidence, not a '
                 'measurement. Each system\'s page registers the close calls a reasonable scorer could set '
                 'differently, and the Thresholds page shows how the ranking moves when you weigh the domains '
                 'differently.</p>')
        a = M["smap"].get(c["author_design"])
        rank_line = ""
        if a:
            rank_line = (f" On the published totals it ranks {a['rank']}{' (tied)' if a['tied'] else ''} of "
                         f"{n_s}, at {fmt(a['total'])} of {fmax(a['max'])}, with {a['failures']} structural "
                         f"failure{'s' if a['failures'] != 1 else ''}.")
        status = ""
    else:
        cap = f"{n_s} systems and {n_c} criteria, grouped by domain and by kind of system."
        find = ('<p>Findings are stated here when the version 2.0 scores are published, each with its reasons '
                'and its limits. The <a href="findings.html">Findings</a> page holds the charts, ready for them.</p>')
        rank_line = ""
        status = S.fragment("status.html", n_criteria=n_c, n_systems=n_s, v1_site=c["v1_site"],
                            releases=f"{S.repo}/releases", release=esc(M["cfg"]["scores"]["release"]))
    main = S.fragment(
        "home.html", n_criteria=n_c, n_systems=n_s, field=field(M, esc(cap)), status=status, findings=find,
        rank_line=rank_line, repo=S.repo, v1_site=c["v1_site"], v1_paper=c["v1_paper"], v1_report=c["v1_report"],
        paper=S.blob(M["cfg"]["sources"]["paper"]), report=S.blob(M["cfg"]["sources"]["report"]),
        csv=S.raw + M["cfg"]["scores"]["csv"], corpus=S.raw + M["cfg"]["scores"]["corpus"],
        criteria_json=S.raw + M["cfg"]["sources"]["criteria"], citation=S.blob(M["cfg"]["sources"]["citation"]),
        licence_url=c["licence_url"], licence=esc(c["licence_name"]), hub=c["hub"])
    jsonld = {
        "@context": "https://schema.org", "@type": "Dataset",
        "name": M["cfg"]["site"]["title"],
        "description": (f"NEEC compares economic systems against one fixed set of {n_c} normative criteria in five "
                        f"domains, and publishes the evidence, protocol and code behind every score."),
        "url": S.base, "license": c["licence_url"], "isAccessibleForFree": True,
        "creator": [{"@type": "Person", "name": "Duke Johnson"}, {"@type": "Organization", "name": "Anthropic (Claude)"}],
        "keywords": ["normative economics", "comparative economic systems", "evaluation criteria", "replication"],
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": S.raw + M["cfg"]["scores"]["csv"]},
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": S.raw + M["cfg"]["sources"]["criteria"]},
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": S.base + "data/neec.json"}],
        "isBasedOn": S.repo,
    }
    S.page("index.html", "home", M["cfg"]["site"]["title"],
           f"How economic systems compare on {n_c} normative criteria, with the evidence behind every score.",
           main, data=dict(field=field_data(M)), jsonld=jsonld)


def page_systems_index(S):
    M = S.M
    rows = []
    for sc in M["cfg"]["scope_order"]:
        ss = sorted([s for s in M["systems"] if s["scope"] == sc], key=lambda s: s["short"].lower())
        if not ss:
            continue
        info = M["cfg"]["scope_classes"][sc]
        head = ('<tr><th scope="col">System</th><th scope="col">Code</th>' +
                ('<th scope="col" class="num">Total</th><th scope="col" class="num">Failures</th><th scope="col">Tier</th>'
                 if M["publish"] else "") + '<th scope="col">Evidence</th></tr>')
        body = []
        for s in ss:
            docs = " ".join(f'<a href="{S.blob(d)}">{esc(d)}</a>' for d in s["docs"])
            sc_cells = ""
            if M["publish"]:
                sc_cells = (f'<td class="num">{fmt(s["total"])}</td><td class="num">{s["failures"]}</td>'
                            f'<td>{esc(s["tier"])}</td>')
            body.append(f'<tr><th scope="row"><a href="{s["slug"]}.html">{esc(s["name"])}</a></th>'
                        f'<td><code>{s["code"]}</code></td>{sc_cells}<td class="docs">{docs}</td></tr>')
        rows.append(f'<section class="scope-group"><h2>{esc(info["plural"])}</h2>'
                    f'<p class="gloss">{esc(info["gloss"][0].upper() + info["gloss"][1:])}.</p>'
                    f'<div class="table-scroll bleed"><table class="list"><thead>{head}</thead>'
                    f'<tbody>{"".join(body)}</tbody></table></div></section>')
    compare = ""
    if M["publish"]:
        opts = "".join(f'<option value="{s["code"]}">{esc(s["short"])}</option>'
                       for s in sorted(M["systems"], key=lambda s: s["short"].lower()))
        sels = "".join(f'<label>System {i}<select name="cmp{i}"><option value="">Choose</option>{opts}</select></label>'
                       for i in (1, 2, 3))
        compare = (f'<section class="compare" id="compare"><h2>Compare side by side</h2>'
                   f'<p>Choose up to three systems to set their rows next to each other. Where one system scores at '
                   f'least as high on every criterion and higher on at least one, the comparison says so.</p>'
                   f'<form class="cmp-form" data-compare>{sels}</form><div class="cmp-out" aria-live="polite"></div></section>')
    else:
        compare = pending_note(M, "A side-by-side comparison of any three systems is built in.")
    n = len(M["systems"])
    kinds = {sc: sum(1 for s in M["systems"] if s["scope"] == sc) for sc in M["cfg"]["scope_order"]}
    lede = (f"NEEC scores {n} economic systems of three kinds: " + ", ".join(
        f'{k} {esc(M["cfg"]["scope_classes"][sc]["plural"].lower() if k != 1 else M["cfg"]["scope_classes"][sc]["label"].lower())}'
        for sc, k in kinds.items()) + ". The kind decides how a threshold written for a whole population is read. "
        "Each system's evidence is in its scoring documents, linked below.")
    main = (f'<h1>Systems</h1><p class="lede">{lede}</p>{compare}{"".join(rows)}'
            f'{buttons(btn(S.issue("system"), "Propose a system to score", quiet=True))}')
    S.page("systems/index.html", "systems", "Systems", f"The {n} economic systems NEEC scores, with their evidence.",
           main, data=dict(scores=score_data(M), field=field_data(M)))


def system_page(S, s):
    M = S.M
    info = M["cfg"]["scope_classes"][s["scope"]]
    parts = [f'<h1>{esc(s["name"])}</h1>',
             f'<p class="lede">{esc(info["label"])}: {esc(info["gloss"])}. Code <code>{s["code"]}</code>.</p>']
    if s["code"] == M["cfg"]["site"]["author_design"]:
        parts.append('<p class="note">Designed by Duke Johnson, one of NEEC\'s two authors. The '
                     '<a href="{root}method.html#disclosure">disclosure</a> says how the project handles this.</p>')
    if M["publish"]:
        parts.append(f'<p class="summary"><span class="big">{fmt(s["total"])}</span> of {fmax(s["max"])} '
                     f'({s["pct"]}%), {s["failures"]} structural failure{"s" if s["failures"] != 1 else ""}, '
                     f'{esc(s["tier"])}. Rank {s["rank"]}{" (tied)" if s["tied"] else ""} of {len(M["systems"])} '
                     f'on equal weights.</p>')
        parts.append('<figure class="radar-fig small"><svg class="radar" data-radar="profile" role="img" '
                     f'aria-label="{esc(s["short"])}: share of each domain\'s points, with the median of all systems"></svg>'
                     '<figcaption>Share of each domain\'s points; the dashed outline is the median of all systems. '
                     '<a href="{root}findings.html#profiles">Compare profiles</a>.</figcaption></figure>')
    else:
        parts.append(pending_note(M, "This system's scores, by criterion and domain, are shown here."))
    doms = []
    for d in M["domains"]:
        items = []
        for cid in d["criteria"]:
            v = s["vector"][cid] if M["publish"] else None
            c = M["cmap"][cid]
            txt = score_text(v) if (not M["publish"] or v is not None) else "not scored in this data"
            items.append(f'<li id="{cslug(cid)}">{mark(v)}<a href="{{root}}criteria/{cslug(cid)}.html"><code>{cid}</code> '
                         f'{esc(c["name"])}</a><span class="sc">{txt}</span></li>')
        sub = ""
        if M["publish"]:
            dd = s["domains"][d["id"]]
            add = " + ".join(fmt(s["vector"][x]) for x in dd["crits"])
            sub = f'<p class="sub"><span class="n">{fmt(dd["sum"])} of {fmax(dd["max"])}</span> = {add}</p>'
        doms.append(f'<section class="dom {d["id"].lower()}"><h3>{esc(d["name"])}</h3>{sub}<ul class="row-list">{"".join(items)}</ul></section>')
    parts.append(f'<h2>By domain</h2><div class="doms bleed">{"".join(doms)}</div>')
    if M["publish"]:
        if s["flags"]:
            fr = "".join(f'<tr><th scope="row"><a href="#{cslug(f["criterion"])}"><code>{f["criterion"]}</code></a></th>'
                         f'<td class="num">{fmt(f["scored"])}</td><td class="num">{", ".join(fmt(x) for x in f["alternatives"])}</td>'
                         f'<td>{esc(f["basis"].replace("-", " "))}</td></tr>' for f in s["flags"])
            rr = "".join(f'<tr><th scope="row">{esc(r["label"][0].upper() + r["label"][1:])}</th>'
                         f'<td class="num">{fmt(r["result"]["total"])}</td><td class="num">{r["result"]["failures"]}</td>'
                         f'<td>{esc(r["result"]["tier"])}</td></tr>' for r in s["readings"])
            parts.append(f'<h2 id="close-calls">Close calls</h2><p>The scoring document registers these scores as calls a '
                         f'reasonable scorer could set differently.</p><div class="table-scroll"><table class="list">'
                         f'<thead><tr><th scope="col">Criterion</th><th scope="col" class="num">Scored</th>'
                         f'<th scope="col" class="num">Alternative</th><th scope="col">Direction</th></tr></thead><tbody>{fr}</tbody></table></div>'
                         f'<p>Resolved together, they give:</p><div class="table-scroll"><table class="list"><thead><tr>'
                         f'<th scope="col">Reading</th><th scope="col" class="num">Total</th><th scope="col" class="num">Failures</th>'
                         f'<th scope="col">Tier</th></tr></thead><tbody>{rr}</tbody></table></div>')
        else:
            parts.append('<h2 id="close-calls">Close calls</h2><p>The scoring document registers no close calls.</p>')
    docs = "".join(f'<li><a href="{S.blob(d)}">{esc(d)}</a> <a class="alt" href="{S.raw}{quote(d)}">plain text</a></li>' for d in s["docs"])
    parts.append(f'<h2>Evidence</h2><p>{esc(s["scored"])}.</p><ul class="docs-list">{docs}</ul>' if s["scored"]
                 else f'<h2>Evidence</h2><ul class="docs-list">{docs}</ul>')
    parts.append(buttons(
        btn(f'{{root}}replicate.html?system={s["code"]}#prompt', "Check this system with an AI"),
        btn(S.issue("score", system=s["name"], title=f"Score challenge: {s['short']}, [criterion]"), "Challenge a score", quiet=True),
        btn(S.issue("evidence", system=s["name"], title=f"New evidence: {s['short']}"), "Add evidence", quiet=True)))
    prof = None
    if M["publish"]:
        allp = [domain_pcts(x, M) for x in M["systems"]]
        prof = dict(axes=[d["name"] for d in M["domains"]], name=s["short"], values=[v / 100 for v in domain_pcts(s, M)],
                    median=[statistics.median(col) / 100 for col in zip(*allp)])
    S.page(f"systems/{s['slug']}.html", "systems", s["name"],
           f"{s['name']}: how NEEC scores it, criterion by criterion, with its evidence.", "\n".join(parts),
           data=dict(profile=prof) if prof else None)


def page_criteria_index(S):
    M = S.M
    secs = []
    for d in M["domains"]:
        rows = []
        for cid in d["criteria"]:
            c = M["cmap"][cid]
            rows.append(f'<tr><th scope="row"><a href="{cslug(cid)}.html"><code>{cid}</code></a></th>'
                        f'<td><a href="{cslug(cid)}.html">{esc(c["name"])}</a></td>'
                        f'<td class="thr">{inline(c["definition"]["pass_threshold"])}</td>'
                        f'<td class="rev">{esc(M["crit"]["classes"][c["revision"]["cls"]].capitalize())}</td></tr>')
        secs.append(f'<section class="dom-sec {d["id"].lower()}" id="{d["id"].lower()}"><h2>{esc(d["name"])}</h2>'
                    f'<p class="gloss">{esc(d["core_question"])} Up to {fmax(M["crit"]["structure"]["domain_max"][d["id"]])} points.</p>'
                    f'<div class="table-scroll bleed"><table class="list crit-list"><thead><tr><th scope="col">Code</th>'
                    f'<th scope="col">Criterion</th><th scope="col">Pass threshold</th><th scope="col">Change in v2.0</th>'
                    f'</tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>')
    n = len(M["order"])
    lede = (f"{n} criteria in five domains. Each says what an economic system ought to achieve and sets a Pass "
            f"Threshold, split into clauses. A score of 1.0 needs every clause shown by named evidence; 0.0 means "
            f"no structural mechanism addresses the criterion.")
    toc = '<ul class="toc">' + "".join(f'<li><a href="#{d["id"].lower()}">{esc(d["name"])}</a></li>' for d in M["domains"]) + "</ul>"
    toc = toc.replace('<ul class="toc">', '<ul class="toc"><li><a href="#structure">From premises to criteria</a></li>')
    main = (f'<h1>Criteria</h1><p class="lede">{lede}</p>{toc}{structure_block(S)}{"".join(secs)}'
            f'<p>The machine-readable text of every criterion, with its anchors for 1.0, 0.5 and 0.0, is '
            f'<a href="{S.raw}criteria.json"><code>criteria.json</code></a>.</p>'
            f'{buttons(btn(S.issue("criterion"), "Propose a new criterion", quiet=True))}')
    S.page("criteria/index.html", "criteria", "Criteria", f"The {n} NEEC criteria, their Pass Thresholds and what changed in version 2.0.", main)


DEF_ORDER = [("requirement", "What it asks"), ("rationale", "Why it matters"),
             ("distinguishes", "How it differs from nearby criteria"),
             ("measurement_protocol", "How it is measured"), ("measurement", "How it is measured"),
             ("indicators", "Indicators"), ("benchmark", "Benchmark"), ("threshold_note", "Note on the threshold"),
             ("disclosure", "Disclosure")]
DEF_SKIP = {"pass_threshold", "clauses", "clause_scope", "derivation"}


def criterion_page(S, cid):
    M = S.M
    c, d = M["cmap"][cid], M["dmap"][M["dom_of"][cid]]
    D = c["definition"]
    rev = M["crit"]["classes"][c["revision"]["cls"]]
    parts = [f'<h1><code class="cid">{cid}</code> {esc(c["name"])}</h1>',
             f'<p class="lede"><a href="index.html#{d["id"].lower()}">{esc(d["name"])}</a>. {esc(d["core_question"])}</p>',
             f'<p class="meta">Change in version 2.0: {esc(rev)} (codes {", ".join(esc(x) for x in c["revision"]["codes"])}).</p>',
             f'<section class="threshold"><h2>Pass threshold</h2><p class="pt">{inline(D["pass_threshold"])}</p>']
    if len(D["clauses"]) > 1:
        parts.append('<p>Clause by clause:</p><ol class="clauses">' + "".join(f"<li>{inline(x)}</li>" for x in D["clauses"]) + "</ol>")
    if D.get("clause_scope"):
        parts.append(f'<p>Every clause: {inline(D["clause_scope"])}.</p>')
    parts.append("</section>")
    seen = set()
    for key, label in DEF_ORDER:
        if key in D and label not in seen:
            seen.add(label)
            parts.append(f'<h2>{esc(label)}</h2><p>{inline(D[key])}</p>')
    extra = [k for k in D if k not in DEF_SKIP and k not in dict(DEF_ORDER)]
    for k in extra:
        parts.append(f'<h3>{esc(k.replace("_", " ").capitalize())}</h3><p>{inline(D[k])}</p>')
    A = c["anchors"]
    bands = "".join(f'<div class="band"><h3>{mark(float(b))}{b}, {SCORE_WORD[float(b)]}</h3><p>{inline(A["bands"][b]["text"])}</p></div>'
                    for b in ("1.0", "0.5", "0.0"))
    parts.append(f'<h2>How scores are anchored</h2>{bands}')
    if A.get("note"):
        parts.append(f'<p class="note">{inline(A["note"])}</p>')
    parts.append(f'<h2>Normative roots</h2><p>{inline(D["derivation"])}.</p>')
    rel = [e for e in M["catalog"] if cid in e["criteria"]]
    if rel:
        parts.append('<h2>Judgment calls on this criterion</h2><ul>' + "".join(
            f'<li><a href="{{root}}thresholds.html#{e["id"]}">{esc(e["title"])}</a></li>' for e in rel) + "</ul>")
    if M["publish"]:
        groups = []
        for v in (1.0, 0.5, 0.0, None):
            ss = [s for s in M["systems"] if s["vector"][cid] == v]
            if ss:
                label = score_text(v) if v is not None else "not scored in this data"
                groups.append(f'<div class="by-score"><h3>{mark(v)}{esc(label[0].upper() + label[1:])}</h3><p>' +
                              ", ".join(f'<a href="{{root}}systems/{s["slug"]}.html#{cslug(cid)}">{esc(s["short"])}</a>' for s in ss) + "</p></div>")
        parts.append(f'<h2>How the systems score</h2>{"".join(groups)}')
    else:
        parts.append(f'<h2>How the systems score</h2>{pending_note(M, "Every system" + chr(39) + "s score on this criterion is listed here.")}')
    parts.append(f'<h2>Sources</h2><p>Definition: {esc(c["sources"]["definition"])}. Anchors: {esc(c["sources"]["anchors"])}.</p>')
    parts.append(buttons(
        btn(f'{{root}}replicate.html?criterion={cid}#prompt', "Check this criterion with an AI"),
        btn(S.issue("pushback", criterion=f"{cid} {c['name']}", title=f"Push back: {cid} {c['name']}"), "Push back on this threshold", quiet=True),
        S.discuss(f"{cid} {c['name']}: where should the bar sit?")))
    S.page(f"criteria/{cslug(cid)}.html", "criteria", f"{cid} {c['name']}",
           f"NEEC criterion {cid}, {c['name']}: its Pass Threshold, clauses, measurement and anchors.", "\n".join(parts))


def page_thresholds(S):
    M = S.M
    W = M["wjp"]
    e = W["entry"]
    clause = M["cmap"]["C4.6"]["definition"]["clauses"][e["clause"][1] - 1]
    refs_rows = "".join(
        f'<tr data-code="{r["code"]}"{" class=\"meets\"" if r["value"] >= W["bar"] else ""}><th scope="row">{esc(r["name"])}</th><td>{esc(M["smap"][r["system"]]["short"])}</td>'
        f'<td class="num">{r["value"]:.2f}</td><td class="verdict">{"meets" if r["value"] >= W["bar"] else "does not meet"}</td></tr>'
        for r in W["refs"])
    notes = " ".join(esc(v) for v in e["not_covered"].values())
    ed_opts = "".join(f'<option value="{ed}"{" selected" if ed == "2025" else ""}>{ed}</option>' for ed in W["editions"])
    wjp_html = f"""
<section class="explorer" id="{e['id']}-explorer" data-wjp>
<h3>C4.6, clause 3: regulation without improper influence</h3>
<p class="clause-q">{inline(clause)}</p>
<div class="wjp-controls">
<label class="bar-label" for="wjp-bar">Bar <output id="wjp-out" for="wjp-bar">{W['bar']:.2f}</output></label>
<input type="range" id="wjp-bar" min="0.30" max="1.00" step="0.01" value="{W['bar']:.2f}" data-adopted="{W['bar']:.2f}" data-median="{W['median']:.2f}">
<p class="snaps"><button type="button" class="btn quiet" data-snap="{W['bar']:.2f}">Upper quartile, {W['bar']:.2f} (adopted)</button>
<button type="button" class="btn quiet" data-snap="{W['median']:.2f}">Median, {W['median']:.2f} (recorded alternative)</button></p>
<label class="ed-label">Edition <select id="wjp-ed">{ed_opts}</select></label>
</div>
<div class="strip-wrap"><svg class="strip" id="wjp-strip" role="img" aria-labelledby="wjp-strip-t"><title id="wjp-strip-t">Sub-factor 6.2 scores of every jurisdiction in the selected edition, with the bar</title></svg></div>
<p class="readout" id="wjp-read" aria-live="polite">At {W['bar']:.2f}, {W['meet']} of {W['n']} jurisdictions in the 2025 edition meet the bar. Every bar from {W['same'][0]:.2f} to {W['same'][1]:.2f} gives the reference economies below the same verdicts.</p>
<div class="table-scroll"><table class="list refs"><caption>Reference economies of the configured national economies, 2025 edition, at two decimals</caption>
<thead><tr><th scope="col">Jurisdiction</th><th scope="col">System</th><th scope="col" class="num">Score</th><th scope="col">At the bar</th></tr></thead>
<tbody>{refs_rows}</tbody></table></div>
<p class="note">{notes} Verdicts here are for one clause of three and are indicative: C4.6 is scored on each entry's stated date and configuration, and no C4.6 score has been set yet. Source: World Justice Project Rule of Law Index, sub-factor 6.2, extracted in <a href="{S.blob(M['cfg']['sources']['wjp']['file'])}"><code>{esc(M['cfg']['sources']['wjp']['file'])}</code></a>; the figures are asserted by <a href="{S.blob('criteria_v2_s45.py')}"><code>criteria_v2_s45.py</code></a>, section 5.</p>
</section>"""
    wjp_data = dict(bar=W["bar"], median=W["median"], editions=W["editions"], data=W["data"],
                    refs=[[r["code"], r["name"], M["smap"][r["system"]]["short"]] for r in W["refs"]])
    if M["publish"]:
        opts = "".join(f'<label class="scheme"><input type="radio" name="scheme" value="{i}"{" checked" if i == 0 else ""}> {esc(sc["label"])}</label>'
                       for i, sc in enumerate(M["schemes"]))
        sliders = "".join(
            f'<label class="dw">{esc(d["name"])} <output data-for="{d["id"]}">1.0</output>'
            f'<input type="range" min="0" max="3" step="0.5" value="1" data-dom="{d["id"]}"></label>' for d in M["domains"])
        weights = (f'<section class="explorer" id="weights" data-weights><h2>Weigh the domains</h2>'
                   f'<p>Totals give every criterion equal weight. The four schemes below are the ones Appendix A.4 of the Paper '
                   f'tests; the sliders let you set your own. Tiers do not move, because they count structural failures, '
                   f'not points.</p><fieldset class="schemes"><legend>Weighting</legend>{opts}'
                   f'<label class="scheme"><input type="radio" name="scheme" value="custom"> My own weights</label></fieldset>'
                   f'<fieldset class="dws" disabled><legend>Domain weights</legend>{sliders}</fieldset>'
                   f'<ol class="rank-list" aria-live="polite"></ol></section>')
        calls = (f'<section class="explorer" id="close-calls" data-calls><h2>Resolve the close calls</h2>'
                 f'<p>Each scoring document registers the scores a reasonable scorer could set differently. Resolve all of '
                 f'them one way and see which systems change tier.</p><fieldset class="schemes"><legend>Reading</legend>'
                 f'<label class="scheme"><input type="radio" name="reading" value="scored" checked> As scored</label>'
                 f'<label class="scheme"><input type="radio" name="reading" value="up"> Every close call upward</label>'
                 f'<label class="scheme"><input type="radio" name="reading" value="down"> Every close call downward</label>'
                 f'</fieldset><div class="calls-out" aria-live="polite"></div></section>')
    else:
        weights = (f'<section class="explorer" id="weights"><h2>Weigh the domains</h2><p>Totals give every criterion '
                   f'equal weight. Here you will be able to apply the four weighting schemes that Appendix A.4 of the Paper '
                   f'tests, or set your own, and watch the ranking move. Tiers never move with weights, because they count '
                   f'structural failures, not points.</p>{pending_note(M, "")}</section>')
        calls = (f'<section class="explorer" id="close-calls"><h2>Resolve the close calls</h2><p>Each scoring document '
                 f'registers the scores a reasonable scorer could set differently. Here you will be able to resolve all of '
                 f'them upward or downward and see which systems change tier.</p>{pending_note(M, "")}</section>')
    cat = []
    for x in M["catalog"]:
        crits = ", ".join(f'<a href="criteria/{cslug(c)}.html">{c}</a>' for c in x["criteria"]) or "Every criterion"
        cl = ""
        if x["clause"]:
            cc, i = x["clause"]
            cl = f'<p class="clause-q"><span class="vh">The clause as written: </span>{inline(M["cmap"][cc]["definition"]["clauses"][i - 1])}</p>'
        alts = "".join(f"<li>{esc(a)}</li>" for a in x["alternatives"]) or "<li>None recorded.</li>"
        live = f'<p><a href="#{x["id"]}-explorer">Move this bar above.</a></p>' if x.get("interactive") else ""
        decs = ", ".join(x["decisions"])
        cat.append(f"""<article class="call" id="{x['id']}">
<h3>{esc(x['title'])}</h3>
<p class="meta">{crits}. Decision{'s' if len(x['decisions']) > 1 else ''} {esc(decs)}. {esc(x['status'])}</p>
{cl}
<dl>
<dt>Adopted</dt><dd>{esc(x['adopted'])}</dd>
<dt>Alternative</dt><dd><ul>{alts}</ul></dd>
<dt>Why</dt><dd>{esc(x['why'])}</dd>
<dt>What it changes</dt><dd>{esc(x['effect'])}</dd>
</dl>{live}
{buttons(btn(S.issue('pushback', topic=x['title'], criterion=', '.join(x['criteria']), title='Push back: ' + x['title']), 'Push back on this choice', quiet=True), S.discuss(x['title']))}
</article>""")
    main = S.fragment("thresholds.html", wjp=wjp_html, weights=weights, calls=calls, catalog="".join(cat),
                      n_calls=len(M["catalog"]), record=S.blob(M["cfg"]["sources"]["record"]),
                      pushback=S.issue("pushback"))
    S.page("thresholds.html", "thresholds", "Set your own bar",
           "Where NEEC's thresholds are judgment calls: move a bar, weigh the domains, and see which systems cross.",
           main, data=dict(wjp=wjp_data, scores=score_data(M)))


# --------------------------------------------------------------------------------------------------
# The visual suite (after the v1 Visual Suite: framework structure, comparison, domain analysis,
# Pareto frontier, key insights), generated from the data and gated like every other score view
# --------------------------------------------------------------------------------------------------

def structure_svg(M):
    F = M["framework"]
    top, rowh, dgap, dhead = 34, 21, 14, 28
    xL, xR, W = 322, 612, 960
    y, cy, heads = top, {}, []
    for d in M["domains"]:
        heads.append((y, d))
        y += dhead
        for cid in d["criteria"]:
            cy[cid] = y
            y += rowh
        y += dgap
    H = y - dgap + 10
    y0, y1 = top + dhead, H - 18
    nums = [p["n"] for p in F["principles"]]
    ny = {n: y0 + i * (y1 - y0) / (len(nums) - 1) for i, n in enumerate(nums)}
    out = [f'<svg class="structure" viewBox="0 0 {W} {H:.0f}" role="img" aria-labelledby="st-t st-d">',
           '<title id="st-t">From core criteria to applied criteria</title>',
           f'<desc id="st-d">Each of the {len(nums)} core criteria, on the left, is linked to the applied criteria '
           f'derived from it, on the right, grouped by domain. The table below gives the same links.</desc>',
           f'<text x="{xL}" y="16" text-anchor="end" class="st-h">Core criteria (NEEC Core)</text>',
           f'<text x="{xR + 12}" y="16" class="st-h">Applied criteria, by domain</text>', '<g class="links">']
    for cid in M["order"]:
        for n in F["links"][cid]:
            a, b = ny[n], cy[cid]
            out.append(f'<path class="lk" data-n="{n}" data-c="{cid}" d="M{xL + 6},{a:.1f} C{xL + 150},{a:.1f} '
                       f'{xR - 150},{b:.1f} {xR - 6},{b:.1f}"/>')
    out.append("</g>")
    for pr in F["principles"]:
        yy = ny[pr["n"]]
        out.append(f'<g class="pn" data-n="{pr["n"]}" tabindex="0"><title>N{pr["n"]} {esc(pr["title"])}: {esc(pr["text"])}</title>'
                   f'<text x="{xL - 10}" y="{yy + 4:.1f}" text-anchor="end"><tspan class="code">N{pr["n"]}</tspan> '
                   f'{esc(pr["title"])}</text><circle cx="{xL}" cy="{yy:.1f}" r="4.5"/></g>')
    for yy, d in heads:
        out.append(f'<text x="{xR + 12}" y="{yy + 14}" class="st-d">{esc(d["name"])}</text>')
    for cid in M["order"]:
        yy = cy[cid]
        out.append(f'<a href="{cslug(cid)}.html" class="cn" data-c="{cid}"><circle cx="{xR}" cy="{yy}" r="4"/>'
                   f'<text x="{xR + 12}" y="{yy + 4}"><tspan class="code">{cid}</tspan> {esc(M["cmap"][cid]["name"])}</text></a>')
    out.append("</svg>")
    return "".join(out)


def structure_block(S):
    M = S.M
    F = M["framework"]
    prem = "".join(f'<li><strong>{esc(x["title"])}.</strong> {esc(x["text"])}</li>' for x in F["premises"])
    rows = "".join(
        f'<tr><th scope="row"><code>N{x["n"]}</code> {esc(x["title"])}</th><td>' +
        ", ".join(f'<a href="{cslug(c)}.html">{c}</a>' for c in M["order"] if x["n"] in F["links"][c]) + "</td></tr>"
        for x in F["principles"])
    n_p, n_n, n_c = len(F["premises"]), len(F["principles"]), len(M["order"])
    return f"""<section id="structure" class="structure-sec">
<h2>From premises to criteria</h2>
<p>NEEC is built in layers. {NUMBER_WORDS.get(n_p, n_p)} empirical premises about the present economy ground {n_n} core criteria, the philosophical layer the Paper calls NEEC Core. Each of the {n_c} applied criteria is derived from one or more core criteria and belongs to one of {len(M['domains'])} domains. The premises and core criteria are stated in the <a href="{S.blob(M['cfg']['sources']['paper'])}">Paper</a>, sections 3 and 4; each applied criterion's derivation is on its page.</p>
<ol class="premises">{prem}</ol>
<p class="note">The Paper derives the core criteria from the premises taken together and gives no premise-by-criterion table, so the diagram draws no links from the premises. Point to, or tab to, a core criterion or an applied criterion to trace its links.</p>
<div class="structure-scroll bleed">{structure_svg(M)}</div>
<details class="st-table"><summary>The same links as a table</summary><div class="table-scroll"><table class="list"><thead><tr><th scope="col">Core criterion</th><th scope="col">Applied criteria derived from it</th></tr></thead><tbody>{rows}</tbody></table></div></details>
</section>"""


def pareto_explainer(M):
    """What dominance and the frontier mean, and, once scores are published, who dominates whom."""
    parts = ['<h3 id="dominance">Understanding the frontier and dominance</h3>',
             '<p>One system <em>dominates</em> another when it scores at least as high on every criterion and higher on '
             'at least one. The dominated system then has a rival that is no worse anywhere and better somewhere, under '
             'the criteria as written.</p>',
             '<p>The <em>Pareto frontier</em> is the set of systems that no other system dominates. On the chart it is '
             'drawn for the two dimensions you choose: frontier systems are ringed in green, labelled, and joined by the '
             'dashed line. It depends on the axes, so a system can sit on the frontier for one pair of dimensions and off '
             'it for another. The statement that matters most is the one across every criterion at once.</p>']
    if M["publish"]:
        S, crits = M["systems"], M["corpus_crits"]
        nd = [s for s in S if not any(dominates(o["vector"], s["vector"], crits) for o in S if o is not s)]
        dom = [s for s in S if s not in nd]
        rows = []
        for s in sorted(dom, key=lambda s: (-s["total"], s["short"].lower())):
            by = [(o, sum(1 for c in crits if o["vector"][c] > s["vector"][c])) for o in nd if dominates(o["vector"], s["vector"], crits)]
            assert by, f"{s['code']} is dominated, so some frontier system must dominate it"
            by.sort(key=lambda t: (t[1], t[0]["short"].lower()))
            rows.append(f'<tr><th scope="row"><a href="systems/{s["slug"]}.html">{esc(s["short"])}</a></th><td>' +
                        ", ".join(f'{esc(o["short"])} <span class="num">({n})</span>' for o, n in by) + "</td></tr>")
        parts.append(f'<p>Across all {len(crits)} criteria, {len(nd)} of the {len(S)} systems are on the frontier: '
                     f'{", ".join(esc(s["short"]) for s in nd)}. Each of the other {len(dom)} is dominated by at least one '
                     f'of them. The number after each name is how many criteria it scores higher on; on every other '
                     f'criterion the two score the same.</p>')
        if rows:
            parts.append('<div class="table-scroll"><table class="list dominance"><thead><tr><th scope="col">Dominated system</th>'
                         '<th scope="col">Dominated by (criteria on which it scores higher)</th></tr></thead>'
                         f'<tbody>{"".join(rows)}</tbody></table></div>')
    parts.append('<p>Dominance is the strongest comparison the scores support, because it needs no weights: under the '
                 'criteria as written, preferring a dominated system to one that dominates it gives up points somewhere '
                 'and gains none anywhere. It says nothing about what the criteria leave out, and nothing about margins: '
                 'one system can dominate another by a single half point on a single criterion. A system off the frontier '
                 'is not thereby a poor one, and a system on it can still carry structural failures; its tier says how many. '
                 'The <a href="systems/index.html#compare">comparison tool</a> sets any two or three systems side by side, '
                 'criterion by criterion.</p>')
    return "".join(parts)


def tier_legend():
    return ('<ul class="legend tiers" aria-label="Tiers"><li><span class="tsw t0" aria-hidden="true"></span>Potentially Adequate</li>'
            '<li><span class="tsw t1" aria-hidden="true"></span>Partially Adequate</li>'
            '<li><span class="tsw t2" aria-hidden="true"></span>Structurally Inadequate</li></ul>')


def page_findings(S):
    M = S.M
    data = None
    if not M["publish"]:
        pn = lambda w: f'<p class="pending-note">{w}</p>'
        insights = pn("The findings are stated here, each computed from the published scores.")
        totals = pn("Every system's total and its structural failures are charted here, ordered by total or by tier.")
        profiles = pn("Each system's profile across the five domains is drawn here, as a share of each domain's points; up to three can be overlaid.")
        frontier = pn("Any two dimensions can be plotted against each other here, with the systems that no other system beats on both.") + pareto_explainer(M)
    else:
        tix = {t["name"]: i for i, t in enumerate(M["tiers"])}
        insights = ('<ul class="findings">' + "".join(f"<li>{f}</li>" for f in M["findings"]) + "</ul>"
                    '<p class="limits">Totals use equal weights. Each statement is computed from the published scores '
                    'when the site is built, and none is typed by hand.</p>')
        rows = []
        for s in sorted(M["systems"], key=lambda s: (-s["total"], s["short"].lower())):
            w = s["total"] / s["max"] * 100
            rings = "".join('<span class="mk s00"></span>' for _ in range(s["failures"]))
            rows.append(f'<tr data-total="{s["total"]}" data-tier="{tix[s["tier"]]}" data-name="{esc(s["short"].lower())}">'
                        f'<th scope="row"><a href="systems/{s["slug"]}.html">{esc(s["short"])}</a></th>'
                        f'<td class="bar-cell"><span class="tbar t{tix[s["tier"]]}" style="width:{w:.2f}%" aria-hidden="true"></span></td>'
                        f'<td class="num">{fmt(s["total"])}</td><td class="num">{s["pct"]}%</td>'
                        f'<td class="fails"><span class="rings" aria-hidden="true">{rings}</span><span class="num">{s["failures"]}</span></td>'
                        f'<td>{esc(s["tier"])}</td></tr>')
        totals = (f'<p>The bar is each system\'s total on equal weights; the rings count its structural failures, which alone '
                  f'decide the tier. Order the rows by total to see where a higher total sits in a lower tier.</p>'
                  f'<p class="seg" role="group" aria-label="Order the rows"><button type="button" class="btn quiet" data-order="total" aria-pressed="true">By total</button>'
                  f'<button type="button" class="btn quiet" data-order="tier" aria-pressed="false">By tier, then total</button></p>'
                  f'{tier_legend()}<div class="table-scroll bleed"><table class="list totals" data-totals>'
                  f'<caption class="vh">Totals, percentages, structural failures and tiers</caption>'
                  f'<thead><tr><th scope="col">System</th><th scope="col"><span class="vh">Total as a bar</span></th><th scope="col" class="num">Total</th>'
                  f'<th scope="col" class="num">Percent</th><th scope="col">Structural failures</th><th scope="col">Tier</th></tr></thead>'
                  f'<tbody>{"".join(rows)}</tbody></table></div>')
        defaults = []
        for sc in M["cfg"]["scope_order"]:
            cs = [s for s in M["systems"] if s["scope"] == sc]
            if cs:
                defaults.append(sorted(cs, key=lambda s: (-s["total"], s["short"].lower()))[0]["code"])
        opts = sorted(M["systems"], key=lambda s: s["short"].lower())
        sels = "".join(
            f'<label>{["First", "Second", "Third"][i]} system<select name="prof{i}"><option value="">None</option>' +
            "".join(f'<option value="{s["code"]}"{" selected" if i < len(defaults) and s["code"] == defaults[i] else ""}>{esc(s["short"])}</option>' for s in opts) +
            "</select></label>" for i in range(3))
        pct_rows = "".join(
            f'<tr><th scope="row"><a href="systems/{s["slug"]}.html">{esc(s["short"])}</a></th>' +
            "".join(f'<td class="num">{v:.0f}%</td>' for v in domain_pcts(s, M)) + "</tr>"
            for s in sorted(M["systems"], key=lambda s: (-s["total"], s["short"].lower())))
        dhead = "".join(f'<th scope="col" class="num">{esc(d["name"])}</th>' for d in M["domains"])
        profiles = (f'<p>Each axis is the share of a domain\'s points a system earns; the dashed outline is the median of all '
                    f'{len(M["systems"])} systems. The first choices below are the highest total in each kind of system. Read '
                    f'the axes one by one: the area of a shape has no meaning of its own.</p>'
                    f'<form class="cmp-form" data-profiles>{sels}</form>'
                    f'<figure class="radar-fig"><svg class="radar" id="radar-findings" role="img" aria-label="Domain profiles of the selected systems"></svg>'
                    f'<figcaption class="radar-legend" aria-live="polite"></figcaption></figure>'
                    f'<details class="st-table"><summary>Every system\'s domain percentages as a table</summary><div class="table-scroll">'
                    f'<table class="list"><thead><tr><th scope="col">System</th>{dhead}</tr></thead><tbody>{pct_rows}</tbody></table></div></details>')
        axes = [("total", "Total")] + [(d["id"], d["name"]) for d in M["domains"]]
        def ax_sel(name, label, default):
            return (f'<label>{label}<select name="{name}">' + "".join(
                f'<option value="{k}"{" selected" if k == default else ""}>{esc(v)}</option>' for k, v in axes) + "</select></label>")
        pts = [(s, s["total"] / s["max"] * 100, domain_pcts(s, M)[0]) for s in M["systems"]]
        fr = sorted(frontier2(pts), key=lambda p: p[1])
        frontier = (f'<p>Plot any two dimensions against each other. A system is on the frontier of the two you choose when no '
                    f'other system scores at least as high on both and higher on one. The frontier depends on the axes: it is '
                    f'a statement about two dimensions, not about every criterion.</p>'
                    f'<form class="cmp-form" data-frontier>{ax_sel("fx", "Across", "total")}{ax_sel("fy", "Up", M["domains"][0]["id"])}</form>'
                    f'{tier_legend()}<p class="field-help">Hover over any dot to see which systems it stands for and their scores. '
                    f'Click or tap a dot to keep its details open, and click it again to close them; with a keyboard, tab to a dot '
                    f'and press Enter.</p><div class="scatter-wrap"><svg class="scatter" id="scatter" role="group" aria-labelledby="sc-t"><title id="sc-t">Systems plotted on the two chosen dimensions</title></svg></div>'
                    f'<p class="readout" id="frontier-read" aria-live="polite">On total and {esc(M["domains"][0]["name"])}, '
                    f'the frontier is {", ".join(esc(p[0]["short"]) for p in fr)}.</p>'
                    f'{pareto_explainer(M)}')
        data = dict(scores=score_data(M), profile_defaults=defaults)
    status = ""
    if not M["publish"]:
        status = (f'<p class="pending-note">Version {esc(M["cfg"]["scores"]["release"])} scores are being finalized. '
                  f'The charts below are built in and fill in when the scores are published; the framework\'s structure, '
                  f'which needs no scores, is drawn on the <a href="criteria/index.html#structure">Criteria</a> page now.</p>')
    main = S.fragment("findings.html", status=status, insights=insights, totals=totals, profiles=profiles, frontier=frontier)
    S.page("findings.html", "findings", "Findings",
           "What NEEC's scores show: totals and structural failures, domain profiles, trade-offs and the frontier, and the computed findings.",
           main, data=data)


# --------------------------------------------------------------------------------------------------
# The AI prompt
# --------------------------------------------------------------------------------------------------

def criterion_prompt_text(c):
    D = c["definition"]
    lines = [f"{c['id']} {c['name']}", f"  Pass Threshold: {D['pass_threshold']}"]
    if len(D["clauses"]) > 1:
        lines += [f"  Clause {i}: {x}" for i, x in enumerate(D["clauses"], 1)]
    if D.get("clause_scope"):
        lines.append(f"  Every clause: {D['clause_scope']}")
    return "\n".join(lines)


def prompt_model(S):
    M = S.M
    t = open(P("site", "ai_prompt.md"), encoding="utf-8").read()
    fill = dict(n_criteria=len(M["order"]), framework=M["crit"]["framework"], raw=S.raw, repo=S.repo, base=S.base,
                criteria_md5=M["src_md5"]["criteria.json"], issue_ai=S.issue("ai"), version=VERSION)
    for k, v in fill.items():
        t = t.replace("{{" + k + "}}", str(v))
    all_text = "\n".join(criterion_prompt_text(M["cmap"][cid]) for cid in M["order"])
    per = {cid: criterion_prompt_text(M["cmap"][cid]) for cid in M["order"]}
    systems = {s["code"]: dict(name=s["name"], docs=[S.raw + quote(d) for d in s["docs"]]) for s in M["systems"]}
    return dict(template=t, all=all_text, per=per, systems=systems,
                no_system="[name the system; for a national economy, also the date to score it at]",
                no_docs=f"   - [the system's scoring documents, linked from its page under {S.base}systems/]")


def render_prompt(PM, mode, system="", criterion=""):
    """The same substitution the page's script performs; used for the static prompt files."""
    t = PM["template"]
    keep, drop = ("audit", "blind") if mode == "audit" else ("blind", "audit")
    t = re.sub(r"\[\[" + drop + r"\]\].*?\[\[/" + drop + r"\]\]\n?", "", t, flags=re.S)
    t = t.replace(f"[[{keep}]]\n", "").replace(f"[[/{keep}]]\n", "")
    sysd = PM["systems"].get(system)
    t = t.replace("{{MODE}}", mode)
    t = t.replace("{{MODE_LABEL}}", "audit the published scores" if mode == "audit" else "score blind, without the published scores")
    t = t.replace("{{SYSTEM}}", sysd["name"] if sysd else PM["no_system"])
    t = t.replace("{{CRITERIA}}", criterion if criterion else f"all {len(PM['per'])} criteria")
    t = t.replace("{{CRITERIA_TEXT}}", PM["per"][criterion] if criterion else PM["all"])
    t = t.replace("{{DOCUMENTS}}", "\n".join(f"   - {d}" for d in sysd["docs"]) if sysd else PM["no_docs"])
    assert "{{" not in t and "[[" not in t, "prompt: unreplaced marker"
    return t


def page_replicate(S):
    M = S.M
    PM = prompt_model(S)
    static = render_prompt(PM, "audit")
    S.put("neec-ai-prompt-audit.md", static)
    S.put("neec-ai-prompt-blind.md", render_prompt(PM, "blind"))
    sys_opts = "".join(f'<option value="{s["code"]}">{esc(s["short"])}</option>'
                       for s in sorted(M["systems"], key=lambda s: s["short"].lower()))
    cr_opts = "".join(f'<option value="{cid}">{cid} {esc(M["cmap"][cid]["name"])}</option>' for cid in M["order"])
    builder = f"""<section class="prompt" id="prompt">
<h2>Check a score with an AI</h2>
<p>This prompt tells any AI system how NEEC scores, where the sources are, and what to send back. Choose what it should check, then copy or download it.</p>
<form class="prompt-form" data-prompt>
<fieldset><legend>What should it do?</legend>
<label class="scheme"><input type="radio" name="mode" value="audit" checked> Audit the published scores against their evidence</label>
<label class="scheme"><input type="radio" name="mode" value="blind"> Score blind, without seeing the published scores</label>
</fieldset>
<div class="pf-row">
<label>System <select name="system"><option value="">Any system (name it yourself)</option>{sys_opts}</select></label>
<label>Criterion <select name="criterion"><option value="">All {len(M['order'])} criteria</option>{cr_opts}</select></label>
</div>
</form>
<p class="actions"><button type="button" class="btn" data-copy="#prompt-text">Copy the prompt</button>
<a class="btn quiet" href="{{root}}neec-ai-prompt-audit.md" data-download download="neec-ai-prompt.md">Download it</a>
<span class="copy-status" aria-live="polite"></span></p>
<pre class="prompt-text" id="prompt-text" tabindex="0">{esc(static)}</pre>
<p class="note">The prompt as files: <a href="{{root}}neec-ai-prompt-audit.md">audit</a> and <a href="{{root}}neec-ai-prompt-blind.md">blind</a>. Links in it point to the plain-text files in the repository, which AI systems read more reliably than web pages.</p>
</section>"""
    main = S.fragment("replicate.html", prompt=builder, repo=S.repo, raw=S.raw, contributing=S.blob(".github/CONTRIBUTING.md"),
                      neec_contributing=S.blob(M["cfg"]["sources"]["contributing"]),
                      replication_record=S.blob(M["cfg"]["sources"]["replication_record"]),
                      protocol=S.blob(M["cfg"]["sources"]["protocol"]), issue_ai=S.issue("ai"))
    S.page("replicate.html", "replicate", "Replicate",
           "Re-run every NEEC computation, check one score, or have any AI system score a system with a ready-made prompt.",
           main, data=dict(prompt=PM))


def page_simple(S, name, pid, title, desc, **values):
    S.page(f"{name}.html", pid, title, desc, S.fragment(f"{name}.html", **values))


def machine_files(S):
    M, c = S.M, S.M["cfg"]["site"]
    data = {
        "schema": "neec-site-data/1",
        "generated_by": f"build_site.py {VERSION}; do not edit by hand",
        "framework": M["crit"]["framework"],
        "scores_published": M["publish"],
        "release": M["cfg"]["scores"]["release"],
        "sources": {k: v for k, v in M["src_md5"].items()},
        "domains": [dict(id=d["id"], name=d["name"], question=d["core_question"], criteria=d["criteria"]) for d in M["domains"]],
        "criteria": [dict(id=cid, name=M["cmap"][cid]["name"], domain=M["dom_of"][cid],
                          pass_threshold=M["cmap"][cid]["definition"]["pass_threshold"],
                          clauses=M["cmap"][cid]["definition"]["clauses"],
                          revision=M["cmap"][cid]["revision"]["cls"], page=f"{S.base}criteria/{cslug(cid)}.html")
                     for cid in M["order"]],
        "tiers": M["tiers"],
        "systems": [dict(code=s["code"], name=s["name"], scope_class=s["scope"], page=f"{S.base}systems/{s['slug']}.html",
                         documents=[S.raw + quote(d) for d in s["docs"]],
                         **({"vector": s["vector"], "total": s["total"], "failures": s["failures"], "tier": s["tier"]}
                            if M["publish"] else {}))
                     for s in M["systems"]],
        "weight_schemes": M["schemes"],
        "judgment_calls": M["catalog"],
    }
    S.put("data/neec.json", json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    W = M["wjp"]
    S.put("data/wjp-sf62.json", json.dumps(dict(source=M["cfg"]["sources"]["wjp"]["file"], bar=W["bar"], median_2025=W["median"],
                                                editions=W["data"]), ensure_ascii=False, sort_keys=True) + "\n")
    n = len(M["order"])
    status = ("Version 2.0 scores are published on the site." if M["gate"] else
              "Version 2.0 scores are being finalized and are not shown on the site yet; the repository's neec_corpus.json "
              "holds the published provisional scores on the earlier 26-criterion structure.")
    llms = f"""# NEEC: Normative Economic Evaluation Criteria

> NEEC compares economic systems against one fixed set of {n} normative criteria in five domains. Each criterion is scored 1.0, 0.5 or 0.0, clause by clause against its Pass Threshold; a 0.0 is a structural failure, and a system's tier depends only on its number of structural failures (0 to 2 Potentially Adequate, 3 to 5 Partially Adequate, 6 or more Structurally Inadequate). {status} Authors: {c['authors']}. Duke Johnson designed CCO-PTF-CIP-SZH, one of the scored systems. Licence: {c['licence_name']}.

## Start here

- [Site data (JSON)]({S.base}data/neec.json): the criteria, systems, tiers, weighting schemes and recorded judgment calls, in one file
- [Criteria (JSON)]({S.raw}criteria.json): every criterion's Pass Threshold, clauses and scoring anchors
- [Scoring protocol]({S.raw}SCORING_PROTOCOL.md): how each criterion is scored; section 13 records every methodological decision
- [Prompt for checking a score]({S.base}neec-ai-prompt-audit.md), and [for scoring blind]({S.base}neec-ai-prompt-blind.md)
- [How to report a divergence or an error]({S.raw}.github/CONTRIBUTING.md)

## Pages

- [Findings]({S.base}findings.html), [systems]({S.base}systems/index.html) and [criteria]({S.base}criteria/index.html)
- [Thresholds]({S.base}thresholds.html): the judgment calls, their recorded alternatives and what each changes
- [Method]({S.base}method.html) and [Replicate]({S.base}replicate.html)

## Optional

- [Repository]({S.repo}) and its [llms.txt]({S.raw}llms.txt)
- [Better To Best Research Hub]({c['hub']})
"""
    S.put("llms.txt", llms)
    urls = "".join(f"<url><loc>{esc(S.base + ('' if p == 'index.html' else p))}</loc></url>\n"
                   for p in sorted(S.pages) if p != "404.html")
    S.put("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    S.put(".nojekyll", "")
    for root, _, files in os.walk(P("site", "assets")):
        for f in sorted(files):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, P("site"))
            S.put(rel.replace(os.sep, "/"), open(full, "rb").read())


def check_links(S):
    """Every local href and src in every page must resolve to a generated file."""
    bad = []
    for rel in S.pages:
        base = os.path.dirname(rel)
        doc = S.files[rel].decode("utf-8")
        for u in re.findall(r'(?:href|src)="([^"]+)"', doc):
            if re.match(r"^(https?:|mailto:|#|data:)", u):
                continue
            target = os.path.normpath(os.path.join(base, u.split("#")[0].split("?")[0])).replace(os.sep, "/")
            if target not in S.files:
                bad.append(f"{rel}: {u}")
    assert not bad, "broken local links:\n  " + "\n  ".join(bad)


def build(out, preview=False):
    L = load(preview)
    M = model(L)
    S = Site(M, out)
    c = M["cfg"]["site"]
    page_home(S)
    page_systems_index(S)
    for s in M["systems"]:
        system_page(S, s)
    page_criteria_index(S)
    for cid in M["order"]:
        criterion_page(S, cid)
    page_findings(S)
    page_thresholds(S)
    page_replicate(S)
    n = len(M["order"])
    page_simple(S, "method", "method", "Method", f"How NEEC scores a system: {n} criteria, three marks, clause-by-clause thresholds and tiers set by structural failures.",
                n_criteria=n, protocol=S.blob(M["cfg"]["sources"]["protocol"]), record=S.blob(M["cfg"]["sources"]["record"]),
                repo=S.repo, releases=f"{S.repo}/releases", paper=S.blob(M["cfg"]["sources"]["paper"]),
                replication_record=S.blob(M["cfg"]["sources"]["replication_record"]), hub=c["hub"])
    page_simple(S, "contribute", "contribute", "Contribute", "Report an error, add evidence, push back on a threshold, or propose a system or a criterion.",
                issue_score=S.issue("score"), issue_evidence=S.issue("evidence"), issue_pushback=S.issue("pushback"),
                issue_ai=S.issue("ai"), issue_system=S.issue("system"), issue_criterion=S.issue("criterion"),
                contributing=S.blob(".github/CONTRIBUTING.md"), neec_contributing=S.blob(M["cfg"]["sources"]["contributing"]),
                discussions=(f'<p>Open questions and wider arguments belong in <a href="{S.repo}/discussions">Discussions</a>, '
                             f'where anyone can reply.</p>' if c["discussions"] else ""), repo=S.repo)
    S.page("404.html", "none", "Page not found", "This page does not exist.", S.fragment("404.html"), absolute=True)
    machine_files(S)
    if preview:
        embed_fonts(S)
    check_links(S)
    return S


def embed_fonts(S):
    """A preview is often opened from disk, where browsers refuse web fonts loaded by URL; inline them."""
    import base64
    css = S.files["assets/neec.css"].decode("utf-8")
    def data(m):
        b = S.files["assets/" + m.group(1)]
        return 'url("data:font/woff2;base64,' + base64.b64encode(b).decode("ascii") + '")'
    S.files["assets/neec.css"] = re.sub(r'url\("(fonts/[^"]+\.woff2)"\)', data, css).encode("utf-8")


def compare_trees(a, b):
    def walk(root):
        out = {}
        for r, _, fs in os.walk(root):
            for f in fs:
                full = os.path.join(r, f)
                out[os.path.relpath(full, root).replace(os.sep, "/")] = open(full, "rb").read()
        return out
    A, B = walk(a), walk(b) if os.path.isdir(b) else {}
    diff = sorted({k for k in A.keys() | B.keys() if A.get(k) != B.get(k)})
    return len(A), diff


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--preview", metavar="DIR")
    a = ap.parse_args()
    docs = P("docs")
    if a.preview:
        out = os.path.abspath(a.preview)
        assert out != docs and not out.startswith(docs + os.sep), "a preview never writes docs/"
        S = build(out, preview=True)
        S.write()
        print(f"preview written to {out}: {len(S.files)} files")
        return 0
    if a.check:
        with tempfile.TemporaryDirectory() as tmp:
            S = build(os.path.join(tmp, "docs"))
            S.write()
            n, diff = compare_trees(os.path.join(tmp, "docs"), docs)
        if diff:
            print(f"site differs from its sources: {len(diff)} of {n} files ({', '.join(diff[:5])}"
                  f"{', ...' if len(diff) > 5 else ''}); run python3 build_site.py")
            return 1
        print(f"site matches its sources: {n} files, scores {'published' if S.M['gate'] else 'not yet published'}")
        return 0
    S = build(docs)
    S.write()
    print(f"docs/ written: {len(S.files)} files, {len(S.pages)} pages, scores "
          f"{'published' if S.M['gate'] else 'not yet published'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
