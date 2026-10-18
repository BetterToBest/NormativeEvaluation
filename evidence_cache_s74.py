#!/usr/bin/env python3
"""
evidence_cache_s74.py -- NEEC stage 3b (S57): the evidence the blind re-read of C1.1 and C3.1 reads
========================================================================================================================
Session 74. The blind re-read of C1.1 Poverty Elimination Capacity (the 14 units of part (2.11)) and C3.1 Crisis
Response Capacity (the 16 units of part (2.9)), ledger S57, decisions 69.1, 69.2, found evidence_cache/C1.1/ holding
Session 65's one file (the World Bank's Societal Poverty Line headcount, WDI SI.POV.SOPO, the eight economies the
configured entries cover) and evidence_cache/C3.1/ Session 62's and 63's sixteen (the IMF's fiscal-measures database
page, US social benefits, initial claims and real GDP through FRED, the CARES Act's lead, the ILO's SDG 1.3.1 coverage
for five economies, and the methodology pages of D.62 and SDG 1.3.1). This script adds the sources the blind
readings in blind_s74.py rest on, cached before any prior reading of these units on C1.1 or C3.1 was opened:

  C1.1, configured economies: the Societal Poverty Line itself and its headcount (World Bank Poverty and Inequality
    Platform API, fields spl and spr, 2021 PPP), the window's baseline (2005) and latest survey year for the United
    States, China and the four Nordic economies -- the line a design's projection has to clear, and a check that the WDI
    series Session 65 cached is the current vintage (WDI last updated 2026-10-08; the eight series unchanged).
  C1.1, Integral: passages of its Technical White Paper v0.1 (December 2025) on access to essentials (post-scarcity
    "access is structurally guaranteed"; the fair-access protocols; the ITC's fairness signal).
  C1.1 and C3.1, Libertarian Minarchism: the Libertarian Party platform (lp.org), sections 2.7 (Money and Financial
    Markets), 2.8 (Marketplace Freedom) and 2.14 (Retirement and Income Security).

Sources the readings cite but this script does not cache are named in evidence_cache/C1.1/sources_s74.md and
evidence_cache/C3.1/sources_s74.md (prose, not digest-checked). The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s74.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s74.py --fetch    re-fetch every source (network) and print md5s
Prints file names and summaries only.
"""
import json
import os
import sys

import evidence_cache_s71 as e71
import evidence_cache_s73 as e73

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
PIP = "https://api.worldbank.org/pip/v1/pip?country={}&year={}&povline=3.0&format=json"
# (economy, survey year): the window's baseline (2005, the start of the 20 years ending at the stated date, 2025) and
# the latest survey year in the WDI series (blind_s74.py, reading 1.1.1).
PIP_POINTS = [("USA", 2005), ("USA", 2024), ("CHN", 2005), ("CHN", 2022), ("DNK", 2005), ("DNK", 2023),
              ("FIN", 2005), ("FIN", 2023), ("NOR", 2005), ("NOR", 2023), ("SWE", 2005), ("SWE", 2023)]
PIP_FIELDS = ["country_code", "reporting_year", "reporting_level", "welfare_type", "survey_acronym", "median", "spl",
              "spr"]
WP_PASSAGES = [(362, 367), (636, 641), (1135, 1148)]
LP = "https://lp.org/platform/"
LP_PASSAGES = [(193, 199), (221, 223)]   # 2.7 Money and Financial Markets; 2.8 Marketplace Freedom; 2.14

# md5 of each file as fetched and written by --fetch (2026-10-18)
FILES = {
    "C1.1/pip_societal_poverty_line.json": "0c55a1b6221bf193cbd677e4c4299333",
    "C1.1/integral_wp_v01_c11_extract.txt": "ed5a3859663be394a5bfccd5807619eb",
    "C3.1/lp_platform_c11_c31_extract.txt": "ef70eaf094a6efa2902e09c17aa33c52",
}


def fetch_files():
    out = {}
    # C1.1: the Societal Poverty Line and its headcount (PIP API), the window's end points.
    rows = []
    for iso, year in PIP_POINTS:
        j = json.loads(e73.get(PIP.format(iso, year)))
        nat = [r for r in j if r.get("reporting_level") == "national"] or j
        rows.append({k: nat[0].get(k) for k in PIP_FIELDS})
    out["C1.1/pip_societal_poverty_line.json"] = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode()
    # C1.1, Integral: white paper v0.1, passages.
    raw = e71.get(e71.WP)
    lines = [f"Source: {e71.WP} (Joseph, INTEGRAL: Technical White Paper v0.1, December 2025; PDF md5 "
             f"{e71.md5(raw)}); text by pdftotext -layout 24.02; passages headed by line range.", ""]
    out["C1.1/integral_wp_v01_c11_extract.txt"] = "\n".join(
        lines + e71.passages(e71.pdf_text(raw), WP_PASSAGES)).encode()
    # C1.1 and C3.1, Libertarian Minarchism: the platform, sections 2.7, 2.8 and 2.14. The page is served
    # dynamically (Session 73): a re-fetch is compared on the passages, not on the page's md5 in the header.
    raw = e73.get(LP, ua=True)
    lines = [f"Source: {LP} (Libertarian Party platform, as served 2026-10-18; page md5 {e71.md5(raw)}); text by "
             "evidence_cache_s71.html_text(); passages headed by line range.", ""]
    out["C3.1/lp_platform_c11_c31_extract.txt"] = "\n".join(
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
