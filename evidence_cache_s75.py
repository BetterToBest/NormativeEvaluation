#!/usr/bin/env python3
"""
evidence_cache_s75.py -- NEEC stage 3b (S58): the evidence the blind re-read of C2.1, C2.4, C2.3 and C2.5 reads
========================================================================================================================
Session 75. The blind re-read of C2.1 Freedom from Coercion, C2.4 Democratic Participation and C2.3 Creative
Development Opportunities for the six configured economies (clause 1 read for the first time, decision 65.2 having
held it), and of C2.5 Exit Rights and Mobility (23 units), ledger S58, decisions 69.1, 69.2, found Session 70's caches
holding the World Happiness Report 2026's statistical appendix (C2.1: the measure's definition, no country table), the
IDEA turnout codebook (C2.4: methodology, no country table) and notes naming the gaps (C2.3: no time-use data; C2.4:
the OECD Trust Survey's coverage unconfirmed), and no C2.5 cache. This script adds the sources the blind readings in
blind_s75.py rest on, cached before any prior reading of these units on these criteria was opened:

  C2.1 clause 1: the Gallup World Poll's "freedom to make life choices" share by country and year, as the World
    Happiness Report's data application serves it (data.worldhappiness.report, its "map" view per year, field FR =
    "Freedom (%)"), 2005 to 2025, for the United States, China, Singapore, Qatar and the four Nordic economies. The
    application's API takes a request token its own page computes, so the page is loaded in a headless browser
    (Playwright, the container's Chromium) and its responses read, as a visitor's browser reads them.
  C2.4 clause 1: International IDEA's Voter Turnout Database, the site's own full export (all countries, all
    elections), rows for the eight economies; China holds no row (no direct national election).
  C2.4 clause 3: the OECD Trust Survey's external-efficacy item (TRUST_PE_EXT, "the political system lets people like
    me have a say"), Government at a Glance 2025's dataflow on the OECD's SDMX API: every country it covers (the
    United States, China, Singapore and Qatar are not among them -- the gap Session 70 named, now confirmed).
  C2.4, Qatar: International IDEA's Democracy Tracker, November 2024 (the referendum ending Shura Council elections).
  C2.3 clause 1: Eurostat, EU-SILC 2022 (ilc_scp07), persons practising artistic activities by frequency, the four
    Nordic economies -- the one comparable survey found that records weekly frequency.
  C2.3 clause 2: the OECD Time Use Database (DF_TIME_USE on the SDMX API), minutes a day by activity, both sexes, the
    economies it covers among the eight (the United States, China and the four Nordic economies).
  C2.3 clause 3: Eurostat, EU-SILC (ilc_pw01b), the "meaning of life" rating (the EU-SILC well-being module's
    "worthwhile" item, 0-10), with the time-use satisfaction rating for scale, the four Nordic economies.
  C2.5, CCO-PTF-CIP-SZH: passages of its research hub at the commit Session 71 cached (8e8a6ba) on opting in, viability
    at partial participation, and Acre Equity's exit haircut and network portability.
  C2.5, Integral: passages of its Technical White Paper v0.1 (December 2025) on voluntary adoption, migrating an ITC
    account between nodes, credit decay and access to essentials.
  C2.5, Libertarian Minarchism: the Libertarian Party platform, sections 3.4 (Free Trade and Migration) and 3.7
    (Self-Determination).

Sources the readings cite but this script does not cache are named in evidence_cache/C2.1/, C2.3/, C2.4/ and C2.5/
sources_s75.md (prose, not digest-checked). The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s75.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s75.py --fetch    re-fetch every source (network; node with Playwright for the WHR
                                           application) and print md5s
Prints file names and summaries only.
"""
import csv
import io
import json
import os
import subprocess
import sys
import tempfile
import time

import evidence_cache_s71 as e71
import evidence_cache_s73 as e73

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
ISO = ["USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE"]
NAMES = {"United States": "USA", "China": "CHN", "Singapore": "SGP", "Qatar": "QAT", "Denmark": "DNK",
         "Finland": "FIN", "Norway": "NOR", "Sweden": "SWE"}
WHR_YEARS = list(range(2005, 2026))
IDEA_EXPORT = "https://www.idea.int/data-tools/export?type=region_only&themeId=293&world=all&loc=home"
IDEA_DT_QA = "https://www.idea.int/democracytracker/report/qatar/november-2024"
SDMX = "https://sdmx.oecd.org/public/rest/data/{}/all?dimensionAtObservation=AllDimensions"
TRUST = "OECD.GOV.GIP,DSD_GOV_INT@DF_GOV_TDG_2025,1.1"
TIME_USE = "OECD.WISE.INE,DSD_TIME_USE@DF_TIME_USE,1.0"
ESTAT = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{}?format=JSON&lang=EN&sex=T&age=Y_GE16"
         "&isced11=TOTAL&geo=DK&geo=FI&geo=NO&geo=SE")
RH = "https://raw.githubusercontent.com/BetterToBest/research-hub/8e8a6ba/"
RH_PASSAGES = [("research-summary.html", [(112, 112), (606, 606)]),
               ("cco-ptf-integrated-framework.html", [(201, 201)]),
               ("cco-ptf-simulation-replication.html", [(27, 27), (39, 39), (111, 111)]),
               ("us-real-estate-transformation.html", [(93, 97), (105, 109), (119, 137)])]
WP_PASSAGES = [(296, 300), (648, 662), (1140, 1146), (9386, 9396), (11959, 11982)]
LP = "https://lp.org/platform/"
LP_PASSAGES = [(241, 243), (253, 255)]
IDEA_DT_PASSAGES = [(805, 809)]

# md5 of each file as fetched and written by --fetch (2026-10-18)
FILES = {
    "C2.1/whr_freedom_s75.json": "667d54cbfcd947970dae66ae18cfa76d",
    "C2.4/idea_turnout_s75.json": "8e57af15d7b2b9849fe9d2ce8f4a0fda",
    "C2.4/oecd_trust_pe_ext_s75.json": "316cf73c8395a98c713469539e029e82",
    "C2.4/idea_dt_qatar_2024_11_extract.txt": "6274f9b7e199e1745ceaf85a29a30d95",
    "C2.3/eurostat_artistic_practice_s75.json": "f62928e607cad84ea0c3255dc0ce4200",
    "C2.3/oecd_time_use_s75.json": "73b32bb664491efd00f023d64d0ed883",
    "C2.3/eurostat_meaning_of_life_s75.json": "1318fe978d9aa5f7fb577c2a65eff0a1",
    "C2.5/cco_research_hub_c25_extract.txt": "88a9aff635764ba38127872efbaa10d1",
    "C2.5/integral_wp_v01_c25_extract.txt": "37521fb9801536a30aff0fba8777ac3a",
    "C2.5/lp_platform_c25_extract.txt": "3e007acdbc4232d8c1e0a3ee33a23baf",
}

WHR_JS = r"""
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const pg = await b.newPage();
  const years = JSON.parse(process.argv[2]);
  await pg.goto('https://data.worldhappiness.report/map', { waitUntil: 'load', timeout: 120000 });
  await pg.waitForTimeout(3000);
  // The page's own request function (chunk 33, module 297) posts {view, year} with an x-request-token header it
  // computes from the time; the same call is made from inside the loaded page, one per year.
  const out = await pg.evaluate(async (years) => {
    const token = () => { const e = Date.now().toString(); let a = 5381; const s = e + "whr-d4sh-2025-x9k7m2";
      for (let o = 0; o < s.length; o++) a = (a << 5) + a + s.charCodeAt(o) >>> 0; return btoa(e + "." + a.toString(16)); };
    const res = {};
    for (const y of years) {
      const r = await fetch("/api/data", { method: "POST", headers: { "Content-Type": "application/json",
        "x-request-token": token() }, body: JSON.stringify({ view: "map", year: y }) });
      res[y] = await r.json();
    }
    return res;
  }, years);
  require('fs').writeFileSync(process.argv[3], JSON.stringify(out));
  await b.close();
})();
"""


def whr_map_views(years):
    """{year: rows} of the WHR application's map view, read in a headless browser from inside the loaded page (the
    API's request token is the page's own, computed client-side)."""
    with tempfile.TemporaryDirectory() as tmp:
        js, out = os.path.join(tmp, "whr.js"), os.path.join(tmp, "whr.json")
        open(js, "w").write(WHR_JS)
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        subprocess.run(["node", js, json.dumps([str(y) for y in years]), out], check=True, timeout=1800,
                       env={**os.environ, "NODE_PATH": root}, capture_output=True)
        return json.load(open(out))


def sdmx_csv(flow, tries=4):
    """The OECD SDMX API's CSV for one dataflow (asked for by the Accept header; the API serves XML without it)."""
    for i in range(tries):
        r = subprocess.run(["curl", "-sS", "-L", "-m", "180", "-H", "Accept: application/vnd.sdmx.data+csv",
                            "-w", "\n%{http_code}", SDMX.format(flow)], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code.decode().strip() == "200" and body.startswith(b"DATAFLOW"):
            return list(csv.DictReader(io.StringIO(body.decode("utf-8"))))
        time.sleep(2 ** (i + 1))
    raise RuntimeError(f"no CSV for {flow}")


def estat_rows(code, keep):
    """Eurostat JSON-stat, flattened to one dict per value, keeping `keep` dimensions."""
    d = json.loads(e73.get(ESTAT.format(code)))
    ids, size = d["id"], d["size"]
    inv = {k: {v: kk for kk, v in d["dimension"][k]["category"]["index"].items()} for k in ids}
    rows = []
    for flat, val in sorted(d["value"].items(), key=lambda kv: int(kv[0])):
        i, c = int(flat), {}
        for k, s in reversed(list(zip(ids, size))):
            c[k] = inv[k][i % s]
            i //= s
        rows.append({**{k: c[k] for k in keep}, "value": val})
    return {"source": ESTAT.format(code), "label": d.get("label"), "updated": d.get("updated"), "rows": rows}


def jbytes(obj):
    return (json.dumps(obj, indent=0, sort_keys=True, ensure_ascii=False) + "\n").encode()


def fetch_files():
    out = {}
    # C2.1 clause 1: Gallup's freedom share (FR) and its rank (RA), per year, the eight economies.
    views = whr_map_views(WHR_YEARS)
    fr = {iso: {} for iso in ISO}
    for y, rows in views.items():
        for r in rows:
            if r.get("GE") in fr and r.get("FR"):
                fr[r["GE"]][y] = {"freedom_pct": float(r["FR"]), "rank": r.get("RA")}
    out["C2.1/whr_freedom_s75.json"] = jbytes({"source": "https://data.worldhappiness.report (view 'map', field FR = "
                                                         "'Freedom (%)', RA = its rank), read 2026-10-18",
                                               "years_served": sorted(views), "freedom": fr})
    # C2.4 clause 1: IDEA's full export, the eight economies' rows.
    raw = e73.get(IDEA_EXPORT, ua=True)
    import openpyxl
    with tempfile.TemporaryDirectory() as tmp:
        x = os.path.join(tmp, "idea.xlsx")
        open(x, "wb").write(raw)
        rows = list(openpyxl.load_workbook(x, read_only=True).worksheets[0].iter_rows(values_only=True))
    head = list(rows[0])
    keep = [dict(zip(head, r)) for r in rows[1:] if r[0] in NAMES]
    out["C2.4/idea_turnout_s75.json"] = jbytes({"source": IDEA_EXPORT, "export_md5": e71.md5(raw),
                                               "rows_in_export": len(rows) - 1, "columns": head, "rows": keep})
    # C2.4 clause 3: the OECD Trust Survey's external-efficacy item, every country covered.
    t = sdmx_csv(TRUST)
    pe = [{k: r[k] for k in ("REF_AREA", "TIME_PERIOD", "OBS_VALUE", "UNIT_MEASURE")} for r in t
          if r["MEASURE"] == "TRUST_PE_EXT"]
    out["C2.4/oecd_trust_pe_ext_s75.json"] = jbytes({"source": SDMX.format(TRUST), "measure": "TRUST_PE_EXT",
                                                     "areas_in_dataflow": sorted({r["REF_AREA"] for r in t}),
                                                     "rows": pe})
    # C2.4, Qatar: the Democracy Tracker's November 2024 entry.
    raw = e73.get(IDEA_DT_QA, ua=True)
    lines = [f"Source: {IDEA_DT_QA} (International IDEA, Democracy Tracker, Qatar, November 2024; page md5 "
             f"{e71.md5(raw)}); text by evidence_cache_s71.html_text(); passages headed by line range.", ""]
    out["C2.4/idea_dt_qatar_2024_11_extract.txt"] = "\n".join(
        lines + e71.passages(e71.html_text(raw), IDEA_DT_PASSAGES)).encode()
    # C2.3 clause 1: EU-SILC 2022, artistic practice by frequency.
    out["C2.3/eurostat_artistic_practice_s75.json"] = jbytes(estat_rows("ilc_scp07", ["frequenc", "geo", "time"]))
    # C2.3 clause 2: the OECD Time Use Database, both sexes, the economies covered among the eight.
    t = sdmx_csv(TIME_USE)
    tu = [{k: r[k] for k in ("REF_AREA", "MEASURE", "OBS_VALUE", "UNIT_MEASURE")} for r in t
          if r["SEX"] == "_T" and r["REF_AREA"] in ISO]
    out["C2.3/oecd_time_use_s75.json"] = jbytes({"source": SDMX.format(TIME_USE), "measures": {
        "LEI": "leisure", "PAW": "paid work or study", "UPW": "unpaid work", "PCA": "personal care", "OTH": "other"},
        "areas_in_dataflow": sorted({r["REF_AREA"] for r in t}), "rows": tu})
    # C2.3 clause 3: EU-SILC, meaning of life (and time use) ratings.
    m = estat_rows("ilc_pw01b", ["life_sat", "geo", "time"])
    m["rows"] = [r for r in m["rows"] if r["life_sat"] in ("MEANLIFE", "TIME")]
    out["C2.3/eurostat_meaning_of_life_s75.json"] = jbytes(m)
    # C2.5, CCO-PTF-CIP-SZH: the research hub at 8e8a6ba.
    lines = [f"Source: github.com/BetterToBest/research-hub at 8e8a6ba (the commit Session 71 cached), pages as served "
             "by raw.githubusercontent.com; text by evidence_cache_s71.html_text(); passages headed by page and line "
             "range.", ""]
    for page, ranges in RH_PASSAGES:
        raw = e73.get(RH + page)
        lines += [f"=== {page} (md5 {e71.md5(raw)})"] + e71.passages(e71.html_text(raw), ranges)
    out["C2.5/cco_research_hub_c25_extract.txt"] = "\n".join(lines).encode()
    # C2.5, Integral: white paper v0.1.
    raw = e71.get(e71.WP)
    lines = [f"Source: {e71.WP} (Joseph, INTEGRAL: Technical White Paper v0.1, December 2025; PDF md5 "
             f"{e71.md5(raw)}); text by pdftotext -layout 24.02; passages headed by line range.", ""]
    out["C2.5/integral_wp_v01_c25_extract.txt"] = "\n".join(
        lines + e71.passages(e71.pdf_text(raw), WP_PASSAGES)).encode()
    # C2.5, Libertarian Minarchism: the platform, 3.4 and 3.7 (served dynamically: compared on the passages).
    raw = e73.get(LP, ua=True)
    lines = [f"Source: {LP} (Libertarian Party platform, as served 2026-10-18; page md5 {e71.md5(raw)}); text by "
             "evidence_cache_s71.html_text(); passages headed by line range.", ""]
    out["C2.5/lp_platform_c25_extract.txt"] = "\n".join(
        lines + e71.passages(e71.html_text(raw), LP_PASSAGES)).encode()
    return out


def fetch():
    for name, data in fetch_files().items():
        path = os.path.join(CACHE, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        print(f'    "{name}": "{e71.md5(data)}",')


def check():
    ok = True
    for name, want in FILES.items():
        path = os.path.join(CACHE, name)
        good = os.path.isfile(path) and e71.md5(open(path, "rb").read()) == want
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'} {name}: md5 {want[:8]}")
    print("SUMMARY: " + ("ALL PASS" if ok and FILES else "SOME FAILED"))
    return ok and bool(FILES)


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        sys.exit(0 if check() else 1)
