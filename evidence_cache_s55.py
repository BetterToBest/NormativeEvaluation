#!/usr/bin/env python3
"""
evidence_cache_s55.py -- NEEC rescoring pass, stage 2: the evidence cache (W5, decision 52.6), criterion C3.5
=============================================================================================================
Session 55. For each unit of C3.5 Failure-Mode Transparency still in play, record (1) where its published rationale
is and the sources that rationale cites, and (2) the external sources v2.0's measure for C3.5 names, fetched once
and kept as text extracts with their md5s, so that the reading session works from files and not from the network.
The cache records evidence. It makes no reading and changes no score.

Modes
  python3 evidence_cache_s55.py            offline: verify every extract's md5, list which units have which evidence
  python3 evidence_cache_s55.py --fetch    fetch the sources in SOURCES (network), rewrite evidence_cache/C3.5/
Prints file names and summaries only. The offline mode is deterministic and reads no network.
"""
import hashlib, json, os, re, subprocess, sys
import pass_common as pc
import triage_s52 as tri

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "evidence_cache", "C3.5")
INDEX = os.path.join(DIR, "index.json")
REPORT = "NEEC_Report_v1_6.md"
# C3.5 heading line in the Report v1.6, by entry (the Report's first 15 entries)
REPORT_LINE = {"SQ": 326, "NSD": 414, "CPS": 504, "MS": 594, "LM": 684, "MMT": 774, "UBI": 864, "DG": 954, "SC": 1044,
               "FALC": 1134, "PE": 1224, "CCO": 1314, "INT": 1408, "GEO": 1496, "MC": 1586}
SCRATCH = {"GEO": "NEEC_Georgism_LVT_scoring_scratch.md", "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
           "DE": "NEEC_DoughnutEconomics_scoring_scratch.md", "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
           "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "CN": "NEEC_StateCapitalism_China_scoring_scratch.md",
           "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
           "IF": "NEEC_IslamicFinance_scoring_scratch.md", "OS": "NEEC_Ostrom_Commons_scoring_scratch.md"}
# The external sources v2.0's C3.5 measure names (criteria.json, C3.5 definition.measurement), clause by clause.
SOURCES = [
    ("imf_ffs_topic", "clause 4", "IMF, energy subsidies topic page (the Fossil Fuel Subsidies Data)",
     "https://www.imf.org/en/Topics/climate-change/energy-subsidies"),
    ("imf_ffs_wp2023", "clause 4", "IMF working paper, IMF Fossil Fuel Subsidies Data: 2023 Update",
     "https://www.imf.org/en/Publications/WP/Issues/2023/08/22/IMF-Fossil-Fuel-Subsidies-Data-2023-Update-537281"),
    ("gao_priority", "clause 3", "US Government Accountability Office, priority recommendations",
     "https://www.gao.gov/priority-recommendations"),
    ("intosai", "clause 3", "INTOSAI, the supreme audit institutions' body", "https://www.intosai.org/"),
    ("nao_about", "clause 3", "UK National Audit Office, about the NAO and its recommendations work",
     "https://www.nao.org.uk/about-us/"),
]


def md5(b):
    return hashlib.md5(b).hexdigest()


def section(path, line, level):
    """Text of the heading at 1-based `line` up to the next heading of the same or higher level."""
    lines = pc.read(path).split("\n")
    out = [lines[line - 1]]
    for t in lines[line:]:
        m = re.match(r"(#+) ", t)
        if m and len(m.group(1)) <= level:
            break
        out.append(t)
    return "\n".join(out).strip()


def heading_line(path, prefix):
    for i, t in enumerate(pc.read(path).split("\n"), 1):
        if t.startswith(prefix):
            return i
    return None


CITE = re.compile(r"(?:[A-Z][A-Za-zÀ-ſ'\-]+(?: (?:and|&) [A-Z][A-Za-z'\-]+| et al\.)?,? \(?(?:19|20)\d\d[a-z]?\)?|https?://\S+|\*[^*\n]{8,80}\*)")


def unit_record(code):
    if code in SCRATCH:
        f = SCRATCH[code]
        n = heading_line(f, "#### C3.5 Failure-Mode Transparency")
        text, level = section(f, n, 4), 4
    else:
        f, n = REPORT, REPORT_LINE[code]
        text = pc.read(f).split("\n")[n - 1]
    body = re.sub(r"^#+ .*?: [01]\.[05]\b", "", text.split("\n")[0]) + "\n" + "\n".join(text.split("\n")[1:])
    cites = sorted(set(m.group(0).strip(" ,*") for m in CITE.finditer(body))
                   - {"The 2008", "In 2008", "Since 2008"} - {c for c in () })
    cites = [c for c in cites if not re.match(r"(The|In|By|For|Since|After|Until|From|A|An) ", c)]
    return {"file": f, "line": n, "chars": len(text), "md5": md5(text.encode()), "cites": cites}


def units_in_play():
    p = pc.Pass()
    v = p.vsteps[-1]
    cls = {k: p.v2[k]["revision"]["cls"] for k in p.v2ids}
    return [(c, v[c]["C3.5"]) for c in p.order if tri.reach(p, v, cls, c, "C3.5")]


def text_of(html):
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&#39;", "'"), ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">")):
        html = html.replace(a, b)
    return re.sub(r"\s+", " ", html).strip()


def fetch():
    os.makedirs(DIR, exist_ok=True)
    idx = {"criterion": "C3.5", "built_by": "Session 55", "sources": {}, "units": {}}
    for key, clause, title, url in SOURCES:
        r = subprocess.run(["curl", "-sS", "-L", "-m", "40", "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        code = code.decode().strip()
        row = {"clause": clause, "title": title, "url": url, "http": code}
        if code == "200" and body:
            ext = text_of(body.decode("utf-8", "replace"))[:12000]
            with open(os.path.join(DIR, key + ".txt"), "w", encoding="utf-8") as f:
                f.write(ext + "\n")
            row.update(file=key + ".txt", raw_md5=md5(body), extract_md5=md5((ext + "\n").encode()), chars=len(ext))
        else:
            row["file"] = None
        idx["sources"][key] = row
    for code, s in units_in_play():
        idx["units"][code] = dict(score=s, **unit_record(code))
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(idx, f, indent=1, sort_keys=True)
        f.write("\n")
    print(f"wrote {INDEX} and {sum(1 for r in idx['sources'].values() if r['file'])} extracts")


def check():
    ok = True

    def line(c, t):
        nonlocal ok
        print(f"  {'PASS' if c else 'FAIL'} {t}")
        ok = ok and bool(c)
    idx = json.load(open(INDEX, encoding="utf-8"))
    print("NEEC evidence cache, criterion C3.5 (Session 55): digests, and which units have which evidence")
    print("\n[1] EXTERNAL SOURCES NAMED BY v2.0's MEASURE")
    for key, r in idx["sources"].items():
        if r["file"]:
            b = open(os.path.join(DIR, r["file"]), "rb").read()
            line(md5(b) == r["extract_md5"], f"{key} ({r['clause']}): {r['file']}, {r['chars']} characters, md5 {r['extract_md5'][:8]}")
        else:
            line(True, f"{key} ({r['clause']}): NOT CACHED (HTTP {r['http']}); {r['url']}")
    print("\n[2] UNITS STILL IN PLAY (rationale located and unchanged; citations it names)")
    live = dict(units_in_play())
    line(sorted(live) == sorted(idx["units"]), f"{len(live)} units in play now match the index's {len(idx['units'])}")
    for code, u in sorted(idx["units"].items()):
        t = unit_record(code)
        same = t["md5"] == u["md5"]
        line(same, f"{code} {u['score']}: {u['file']} line {u['line']}, {len(u['cites'])} citation strings")
    ncite = sum(1 for u in idx["units"].values() if u["cites"])
    print(f"\n  units whose rationale names a citable source: {ncite} of {len(idx['units'])}; "
          f"sources cached: {sum(1 for r in idx['sources'].values() if r['file'])} of {len(idx['sources'])}")
    print("SUMMARY: " + ("ALL PASS" if ok else "SOME FAILED"))
    return ok


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        sys.exit(0 if check() else 1)
