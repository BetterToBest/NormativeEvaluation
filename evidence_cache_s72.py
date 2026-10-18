#!/usr/bin/env python3
"""
evidence_cache_s72.py -- NEEC stage 3b (S55): the evidence the blind re-read of C4.1 reads
========================================================================================================================
Session 72. The blind re-read of C4.1 (Intergenerational Justice: the 15 units of part (2.11) and the 8 designs of
part (b6), all on v2.0's two clauses; ledger S55, decisions 69.1, 69.2) found evidence_cache/C4.1/ holding Session 65's
three files (the IMF's general government gross debt, the World Bank's gross national saving and consumption of fixed
capital, % of GNI, to 2021). This script adds the sources the blind readings in blind_s72.py rest on, cached before any
prior reading of these units on C4.1 was opened:

  Clause 2 (positive wealth transfer: net national saving), configured economies: US net saving and gross national
    income (BEA, NIPA table 5.1, through FRED), annual, 2000 to 2025, which carry the US series past the World Bank's
    last year (2021); the World Bank's adjusted net savings (% of GNI: net national saving plus education
    expenditure, less energy, mineral and forest depletion and pollution damage), the check the readings apply for
    the resource economies (Qatar, Norway).
  Centrally Planned Socialism (the late-Soviet record): Ofer, "Macroeconomic Issues of Soviet Reforms", NBER
    Macroeconomics Annual 1990 (the state budget table, the investment share of GNP, the capital stock's growth); the
    "400 days" programme (Moscow, 1990), Appendix 1, on the rouble state debt the USSR Ministry of Finance reported.
  Libertarian Minarchism: the Libertarian Party's platform (lp.org), its two passages on debt and future generations.
  Participatory Economics: Hahnel and Wright, Alternatives to Capitalism (2016), the passages on household and
    federation borrowing and saving and on the investment plan.
  Integral: passages of its Technical White Paper v0.1 (well-being in place of growth or capital accumulation;
    non-accumulative time credits; sufficiency, not surplus accumulation; credits extinguished on use).
  CCO-PTF-CIP-SZH: passages of the Research Hub at its pin, 8e8a6ba (Basic Units pegged to the primary currency; the
    conversion tax's self-funding threshold; Acre Equity; property held in public trust; funding through taxation).

Sources the readings cite but this script does not cache are named in evidence_cache/C4.1/sources_s72.md (prose, not
digest-checked). The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s72.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s72.py --fetch    re-fetch every source (network; pdftotext needed) and print md5s
Prints file names and summaries only.
"""
import csv
import io
import json
import os
import re
import sys

import evidence_cache_s71 as e71

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
ISO = ["USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE"]
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
US_SERIES = ["W201RC1A027NBEA", "A023RC1A027NBEA"]   # net saving; gross national income (billions of dollars)
WB_ANS = ("https://api.worldbank.org/v2/country/" + ";".join(ISO)
          + "/indicator/NY.ADJ.SVNG.GN.ZS?format=json&date=2000:2025&per_page=500")
OFER = "https://www.nber.org/system/files/chapters/c10977/c10977.pdf"
DAYS400 = "https://www.yabloko.ru/Publ/500/400-days-p1.html"
LP = "https://lp.org/platform/"
HUB = "https://raw.githubusercontent.com/BetterToBest/research-hub/8e8a6ba/{}.html"

# Passages: line ranges in the text each source converts to (e71.html_text() for a page, pdftotext -layout 24.02
# for a PDF); each extract heads every passage with its line range in that text.
OFER_PASSAGES = [(264, 271), (350, 352), (456, 494), (1658, 1668)]
LP_PASSAGES = [(187, 187), (191, 191)]
ATC_PASSAGES = [(336, 340), (812, 823), (1955, 1958)]
WP_PASSAGES = [(319, 323), (344, 348), (431, 433), (845, 847)]
HUB_PASSAGES = [("research-summary", [(112, 112)]),
                ("cco-ptf-simulation-replication", [(39, 39), (1350, 1354)]),
                ("index", [(120, 120)]),
                ("integrated-implementation-roadmap", [(77, 77)])]

# md5 of each file as fetched and written by --fetch (2026-10-18)
FILES = {
    "C4.1/fred_us_net_saving_gni.csv": "3f7fb3a1c710b6e744a3e60b842b864d",
    "C4.1/wb_adjusted_net_savings_pct_gni.json": "c4d87efde1c4518b5303b25a21fbaa1b",
    "C4.1/ofer_1990_extract.txt": "462ef88347140549b6a05cd6ecb2538e",
    "C4.1/programme_400_days_1990_extract.txt": "bae638008cf315596893f97ad3a959c5",
    "C4.1/lp_platform_extract.txt": "98ef50602e676e12edfa8764d5481b02",
    "C4.1/hahnel_wright_2016_c41_extract.txt": "3ee5ead994dcc739d02f25e9daf24d64",
    "C4.1/integral_wp_v01_c41_extract.txt": "a3cd38c41968f737de68aa82a2e448ee",
    "C4.1/research_hub_8e8a6ba_c41_extract.txt": "bfa5ca512580a724961f298a61b62e57",
}


def fetch_files():
    out = {}
    # Clause 2, United States: BEA net saving and gross national income (FRED), annual, 2000 onward.
    cols = {}
    for sid in US_SERIES:
        rows = list(csv.reader(io.StringIO(e71.get(FRED.format(sid)).decode("utf-8"))))[1:]
        cols[sid] = {r[0][:4]: r[1] for r in rows if r[1] not in ("", ".") and r[0][:4] >= "2000"}
    years = sorted(set.intersection(*(set(c) for c in cols.values())))
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["year"] + US_SERIES)
    for y in years:
        w.writerow([y] + [cols[s][y] for s in US_SERIES])
    out["C4.1/fred_us_net_saving_gni.csv"] = buf.getvalue().encode("utf-8")
    # Clause 2: World Bank adjusted net savings, % of GNI.
    j = json.loads(e71.get(WB_ANS))
    rows = {}
    for x in j[1]:
        if x["value"] is not None:
            rows.setdefault(x["countryiso3code"], {})[x["date"]] = x["value"]
    rows = {c: dict(sorted(rows.get(c, {}).items())) for c in ISO}
    out["C4.1/wb_adjusted_net_savings_pct_gni.json"] = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode()
    # Centrally Planned Socialism: Ofer (1990), passages.
    raw = e71.get(OFER)
    lines = [f"Source: {OFER} (Gur Ofer, 'Macroeconomic Issues of Soviet Reforms', NBER Macroeconomics Annual 1990, "
             f"vol. 5, pp. 297-334; PDF md5 {e71.md5(raw)}); text by pdftotext -layout 24.02; passages headed by line "
             "range.", ""]
    out["C4.1/ofer_1990_extract.txt"] = "\n".join(lines + e71.passages(e71.pdf_text(raw), OFER_PASSAGES)).encode()
    # Centrally Planned Socialism: the "400 days" programme (1990), Appendix 1, the state-debt passage (cp1251 page).
    raw = e71.get(DAYS400)
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw.decode("cp1251", "replace")))
    m = re.search(r"Мы можем опираться лишь на данные, представленные Минфином СССР.{0,400}?прошлого года\)\.", t)
    out["C4.1/programme_400_days_1990_extract.txt"] = (
        "Source: " + DAYS400 + " (Programme '400 days', Appendix 1, Moscow, 1990; page as served, cp1251, tags "
        "removed, whitespace collapsed; page md5 " + e71.md5(raw) + ")\n\n" + m.group(0) + "\n").encode("utf-8")
    # Libertarian Minarchism: the Libertarian Party platform, passages (html_text).
    raw = e71.get(LP, ua=True)
    lines = [f"Source: {LP} (Libertarian Party platform, as served 2026-10-18; page md5 {e71.md5(raw)}); text by "
             "evidence_cache_s71.html_text(); passages headed by line range.", ""]
    out["C4.1/lp_platform_extract.txt"] = "\n".join(lines + e71.passages(e71.html_text(raw), LP_PASSAGES)).encode()
    # Participatory Economics: Hahnel and Wright (2016), passages.
    raw = e71.get(e71.ATC)
    lines = [f"Source: {e71.ATC} (Hahnel and Wright, Alternatives to Capitalism: Proposals for a Democratic Economy, "
             f"Verso, 2016; PDF md5 {e71.md5(raw)}); text by pdftotext -layout 24.02; passages headed by line range.", ""]
    out["C4.1/hahnel_wright_2016_c41_extract.txt"] = "\n".join(
        lines + e71.passages(e71.pdf_text(raw), ATC_PASSAGES)).encode()
    # Integral: white paper v0.1, passages.
    raw = e71.get(e71.WP)
    lines = [f"Source: {e71.WP} (Joseph, INTEGRAL: Technical White Paper v0.1, December 2025; PDF md5 "
             f"{e71.md5(raw)}); text by pdftotext -layout 24.02; passages headed by line range.", ""]
    out["C4.1/integral_wp_v01_c41_extract.txt"] = "\n".join(
        lines + e71.passages(e71.pdf_text(raw), WP_PASSAGES)).encode()
    # CCO-PTF-CIP-SZH: Research Hub at 8e8a6ba, passages.
    lines = ["Source: github.com/BetterToBest/research-hub at 8e8a6ba (2026-09-21), pages as served by "
             "raw.githubusercontent.com; text by evidence_cache_s71.html_text(); passages headed by page and line range.", ""]
    for page, ranges in HUB_PASSAGES:
        raw = e71.get(HUB.format(page))
        lines += [f"=== {page}.html (md5 {e71.md5(raw)})"] + e71.passages(e71.html_text(raw), ranges)
    out["C4.1/research_hub_8e8a6ba_c41_extract.txt"] = "\n".join(lines).encode("utf-8")
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
