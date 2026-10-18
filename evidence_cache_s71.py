#!/usr/bin/env python3
"""
evidence_cache_s71.py -- NEEC stage 3b (S54): the evidence the blind re-read of C4.5 and C3.4 reads
========================================================================================================================
Session 71. The blind re-read of C4.5 (Exploitation Elimination, 17 units) and C3.4 (Epistemic Adaptability, 7
units) (ledger S54; decisions 69.1, 69.2) found no evidence_cache/ directory for either criterion. This script caches
the sources the blind readings in blind_s71.py rest on, before any prior reading was opened:

  C4.5, clause 1 (extraction rates below 10% of GDP), configured economies: the labour share of GDP in Penn World
    Table 10.01 (labsh) for the eight economies the configured entries cover, from which the broad reading (one minus
    the labour share) is computed; the US national-income components through FRED (BEA: compensation, corporate
    profits, rental income of persons, net interest, proprietors' income, GDP), from which the narrow reading
    (corporate profits plus rental income plus net interest) is computed; the World Bank's total natural-resource
    rents (% of GDP), which separate Qatar's and Norway's resource rent from the rest of the non-labour share; and the
    UN SDG database's labour share of GDP (indicator 10.4.1) for the Nordic economies it carries, to 2024.
  C4.5, clause 2 (genuine exit rights): Sweden's unemployment-insurance law, 43 b (45 benefit days' suspension for
    leaving work without valid reason), from riksdagen.se.
  C4.5, Participatory Economics: Hahnel and Wright, Alternatives to Capitalism (2016), the passages on the allowance
    for people who do not want to work and on the consumption budget (effort rating plus any allowance).
  C4.5, CCO-PTF-CIP-SZH: passages of the Research Hub at its pin, 8e8a6ba (Basic Units, opt-in and restricted to
    essentials; Public Trust Housing's pay-in pathway and projected penetration; selective participation; the
    corporate rate schedule's penalty for labour exploitation).
  C3.4, Integral: passages of its Technical White Paper v0.1 (CDS Module 1's intake of objections from participants,
    Module 10's review, amendment and revocation of decisions, ITC's democratically bounded recalibration).
  C3.4, Status Quo: CPI-U and the effective federal funds rate, monthly, 2019 to 2023 (FRED), for the lag between
    the inflation evidence of 2021 and the first rate rise of March 2022.

Sources the readings cite but this script does not cache are named in evidence_cache/C4.5/sources_s71.md and
evidence_cache/C3.4/sources_s71.md (prose, not digest-checked). The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s71.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s71.py --fetch    re-fetch every source (network; pandas and pdftotext needed) and print md5s
Prints file names and summaries only.
"""
import csv
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
ISO = ["USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE"]
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
US_SERIES = ["GDPA", "A033RC1A027NBEA", "A051RC1A027NBEA", "A048RC1A027NBEA", "W255RC1A027NBEA", "A041RC1A027NBEA"]
HUB = "https://raw.githubusercontent.com/BetterToBest/research-hub/8e8a6ba/{}.html"
WP = "https://integralcollective.io/documents/INTEGRAL-Paper-V0.1.pdf"
ATC = "https://www.sscc.wisc.edu/soc/faculty/pages/wright/Published%20writing/Alternatives%20to%20Capitalism.pdf"
SE_ALF = ("https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/"
          "lag-1997238-om-arbetsloshetsforsakring_sfs-1997-238/")

# Passages: (page, [(first line, last line), ...]) in the text each page converts to (html_text() below, or
# pdftotext -layout 24.02 for a PDF); each extract heads every passage with its line range in that text.
HUB_PASSAGES = [("research-summary", [(74, 74), (112, 112), (606, 606)]),
                ("cco-ptf-integrated-framework", [(77, 79), (95, 111), (201, 201), (245, 245)]),
                ("cco-ptf-simulation-replication", [(27, 27), (33, 33)]),
                ("us-real-estate-transformation", [(49, 53), (333, 333)]),
                ("corporate-transformation", [(117, 121)])]
ATC_PASSAGES = [(526, 536), (776, 784), (2019, 2022)]
WP_PASSAGES = [(1200, 1207), (1214, 1219), (1480, 1503), (9545, 9552), (12648, 12655), (22134, 22136)]

# md5 of each file as fetched and written by --fetch (2026-10-18)
FILES = {
    "C4.5/pwt1001_labsh_selected_economies.csv": "981fd5a6afea0c57a696c242b8d51632",
    "C4.5/fred_us_national_income_components.csv": "197df64c670e50e3f9b3b336b82493cc",
    "C4.5/wb_natural_resource_rents_pct_gdp.json": "197f5478caeded7d327f1717561eba0a",
    "C4.5/un_sdg_10_4_1_labour_share.json": "cb91ec12624f5ebfbc29b01b6fa8740f",
    "C4.5/se_lag_1997_238_43b.txt": "bd34bff75e6ad08e54cb1d8b8a91e164",
    "C4.5/hahnel_wright_2016_extract.txt": "8acef4785cfc3268a6fb205d2520f630",
    "C4.5/research_hub_8e8a6ba_cco_extract.txt": "5ceb2816dc1b83ac40a392e0b26c41d3",
    "C3.4/integral_wp_v01_c34_extract.txt": "9ce79d2ac281b823bbbc957acbbe4804",
    "C3.4/fred_cpi_fedfunds_2019_2023.csv": "44124599138a0f6a808cca7e1c021f91",
}


def md5(b):
    return hashlib.md5(b).hexdigest()


def get(url, ua=False):
    args = ["curl", "-sS", "-L", "--http1.1", "-m", "180", "-w", "\n%{http_code}", url]
    if ua:
        args[1:1] = ["-A", "Mozilla/5.0 (neec-evidence-cache/1.0; research repository)"]
    r = subprocess.run(args, capture_output=True)
    body, _, code = r.stdout.rpartition(b"\n")
    if code.decode().strip() != "200" or not body:
        raise RuntimeError(f"HTTP {code.decode().strip()} for {url}")
    return body


def html_text(raw):
    """The plain text a page's passages are numbered in: scripts and styles dropped, block ends as line breaks,
    tags removed, entities decoded, runs of blanks collapsed, at most one empty line in a row."""
    t = raw.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</h[1-6]>|</tr>|</div>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = "\n".join(re.sub(r"[ \t]+", " ", ln).strip() for ln in t.splitlines())
    return re.sub(r"\n{3,}", "\n\n", t)


def pdf_text(raw):
    with tempfile.TemporaryDirectory() as tmp:
        pdf, txt = os.path.join(tmp, "in.pdf"), os.path.join(tmp, "out.txt")
        open(pdf, "wb").write(raw)
        subprocess.run(["pdftotext", "-layout", pdf, txt], check=True, capture_output=True)
        return open(txt, encoding="utf-8").read()


def passages(text, ranges):
    lines = text.splitlines()
    out = []
    for a, b in ranges:
        out.append(f"--- lines {a}-{b}")
        out += [ln.rstrip() for ln in lines[a - 1:b]]
        out.append("")
    return out


def fetch_files():
    out = {}
    # C4.5: Penn World Table 10.01, labour share (labsh), 1990 onward, the eight economies.
    import pandas as pd
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "pwt.dta")
        open(p, "wb").write(get("https://dataverse.nl/api/access/datafile/354098"))
        df = pd.read_stata(p)
    df = df[df.countrycode.isin(ISO) & (df.year >= 1990)][["countrycode", "year", "labsh"]]
    df = df.sort_values(["countrycode", "year"])
    out["C4.5/pwt1001_labsh_selected_economies.csv"] = df.to_csv(
        index=False, lineterminator="\n", float_format="%.6f").encode("utf-8")
    # C4.5: US national income components (BEA, through FRED), annual, 2000 onward, billions of dollars.
    cols = {}
    for sid in US_SERIES:
        rows = list(csv.reader(io.StringIO(get(FRED.format(sid)).decode("utf-8"))))[1:]
        cols[sid] = {r[0][:4]: r[1] for r in rows if r[1] not in ("", ".") and r[0][:4] >= "2000"}
    years = sorted(set.intersection(*(set(c) for c in cols.values())))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["year"] + US_SERIES)
    for y in years:
        w.writerow([y] + [cols[s][y] for s in US_SERIES])
    out["C4.5/fred_us_national_income_components.csv"] = buf.getvalue().encode("utf-8")
    # C4.5: World Bank total natural-resource rents, % of GDP.
    j = json.loads(get("https://api.worldbank.org/v2/country/" + ";".join(ISO)
                       + "/indicator/NY.GDP.TOTL.RT.ZS?format=json&date=2000:2025&per_page=500"))
    rows = {}
    for x in j[1]:
        if x["value"] is not None:
            rows.setdefault(x["countryiso3code"], {})[x["date"]] = x["value"]
    rows = {c: dict(sorted(rows.get(c, {}).items())) for c in ISO}
    out["C4.5/wb_natural_resource_rents_pct_gdp.json"] = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode()
    # C4.5: UN SDG database, indicator 10.4.1, labour share of GDP (series SL_EMP_GTOTL), the areas it carries.
    j = json.loads(get("https://unstats.un.org/sdgapi/v1/sdg/Series/Data?seriesCode=SL_EMP_GTOTL&areaCode=840"
                       "&areaCode=156&areaCode=702&areaCode=634&areaCode=208&areaCode=246&areaCode=578"
                       "&areaCode=752&pageSize=2000"))
    rows = {}
    for x in j.get("data", []):
        rows.setdefault(x["geoAreaName"], {})[str(int(x["timePeriodStart"]))] = x["value"]
    rows = {c: dict(sorted(v.items())) for c, v in sorted(rows.items())}
    out["C4.5/un_sdg_10_4_1_labour_share.json"] = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode()
    # C4.5: Sweden, Lag (1997:238) om arbetsloshetsforsakring, 43 b (the suspension for leaving work).
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", get(SE_ALF).decode("utf-8", "replace"))))
    m = re.search(r"43 b § En sökande ska stängas av.{0,700}?giltig anledning lämnat sitt arbete.{0,600}?"
                  r"stängas av i 20 ersättningsdagar", t)
    out["C4.5/se_lag_1997_238_43b.txt"] = ("Source: " + SE_ALF + "\nSFS 1997:238, 43 b (text as served; whitespace "
                                           "collapsed)\n\n" + m.group(0) + "\n").encode("utf-8")
    # C4.5: Hahnel and Wright (2016), passages (pdftotext -layout).
    raw = get(ATC)
    lines = [f"Source: {ATC} (Hahnel and Wright, Alternatives to Capitalism: Proposals for a Democratic Economy, "
             f"Verso, 2016; PDF md5 {md5(raw)}); text by pdftotext -layout 24.02; passages headed by line range.", ""]
    out["C4.5/hahnel_wright_2016_extract.txt"] = "\n".join(lines + passages(pdf_text(raw), ATC_PASSAGES)).encode()
    # C4.5: Research Hub at 8e8a6ba, passages (html_text).
    lines = ["Source: github.com/BetterToBest/research-hub at 8e8a6ba (2026-09-21), pages as served by "
             "raw.githubusercontent.com; text by evidence_cache_s71.html_text(); passages headed by page and line range.", ""]
    for page, ranges in HUB_PASSAGES:
        raw = get(HUB.format(page))
        lines += [f"=== {page}.html (md5 {md5(raw)})"] + passages(html_text(raw), ranges)
    out["C4.5/research_hub_8e8a6ba_cco_extract.txt"] = "\n".join(lines).encode("utf-8")
    # C3.4: Integral's white paper v0.1, passages (pdftotext -layout).
    raw = get(WP)
    lines = [f"Source: {WP} (Joseph, INTEGRAL: Technical White Paper v0.1, December 2025; PDF md5 {md5(raw)}); "
             "text by pdftotext -layout 24.02; passages headed by line range.", ""]
    out["C3.4/integral_wp_v01_c34_extract.txt"] = "\n".join(lines + passages(pdf_text(raw), WP_PASSAGES)).encode()
    # C3.4: CPI-U (CPIAUCSL) and the effective federal funds rate (FEDFUNDS), monthly, 2019 to 2023.
    cols = {}
    for sid in ("CPIAUCSL", "FEDFUNDS"):
        rows = list(csv.reader(io.StringIO(get(FRED.format(sid)).decode("utf-8"))))[1:]
        cols[sid] = {r[0]: r[1] for r in rows if "2019-01-01" <= r[0] <= "2023-12-01"}
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["date", "CPIAUCSL", "FEDFUNDS"])
    for d in sorted(cols["CPIAUCSL"]):
        w.writerow([d, cols["CPIAUCSL"][d], cols["FEDFUNDS"][d]])
    out["C3.4/fred_cpi_fedfunds_2019_2023.csv"] = buf.getvalue().encode("utf-8")
    return out


def fetch():
    for name, data in fetch_files().items():
        path = os.path.join(CACHE, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        print(f'    "{name}": "{md5(data)}",')


def check():
    ok = True
    for name, want in FILES.items():
        path = os.path.join(CACHE, name)
        good = os.path.isfile(path) and md5(open(path, "rb").read()) == want
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'} {name}: md5 {want[:8]}")
    print("SUMMARY: " + ("ALL PASS" if ok and FILES else "SOME FAILED"))
    return ok and bool(FILES)


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        sys.exit(0 if check() else 1)
