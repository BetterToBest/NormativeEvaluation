#!/usr/bin/env python3
"""
evidence_cache_s63.py -- NEEC rescoring pass, stage 2: the data files for C3.1 Crisis Response Capacity (group 2.9)
=============================================================================================================
Session 63. Session 62's cache (evidence_cache_s62.py) holds the pages of the sources v2.0's measure names; none of them
carries a figure. This adds the figures the readings need, fetched once and kept with their md5s: the United States'
government social benefits and real GDP (FRED, from the Bureau of Economic Analysis), the weekly initial claims and the
monthly benefits series for the first months of 2020, the date the CARES Act was signed, and the ILO's SDG indicator
1.3.1 (population covered by at least one social protection benefit) for the five economies the group reads, from the
UN Statistics Division's SDG API (series SI_COV_BENFTS, source "ILO - Social Security Inquiry Database"). The ILO's
own pages (HTTP 403 in Session 62) are not needed: the UN API serves the indicator the measure names.
The cache records evidence. It makes no reading and changes no score. The reading script (rescoring_s63.py) checks
each file below by digest and finds every passage it quotes.

Modes
  python3 evidence_cache_s63.py            offline: verify every file's md5 against FILES
  python3 evidence_cache_s63.py --fetch    fetch the sources (network), rewrite evidence_cache/C3.1/ and print the md5s
Prints file names and summaries only.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "evidence_cache", "C3.1")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}&cosd={}&coed={}"
SDG = "https://unstats.un.org/sdgapi/v1/sdg/Series/Data?seriesCode=SI_COV_BENFTS&areaCode={}&pageSize=500"
WIKI = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=CARES_Act&format=json"
SOURCES = {
    "fred_benefits_annual.csv": FRED.format("A063RC1A027NBEA", "2017-01-01", "2023-01-01"),
    "fred_realgdp_annual.csv": FRED.format("GDPCA", "2017-01-01", "2023-01-01"),
    "fred_benefits_monthly.csv": FRED.format("A063RC1", "2019-10-01", "2020-12-01"),
    "fred_claims_weekly.csv": FRED.format("ICSA", "2020-02-15", "2020-05-10"),
    "sdg131_840.json": SDG.format(840), "sdg131_156.json": SDG.format(156), "sdg131_702.json": SDG.format(702),
    "sdg131_634.json": SDG.format(634), "sdg131_578.json": SDG.format(578),
    "cares_act_wikipedia_lead.txt": WIKI,
}
# md5 of each file as fetched and written by --fetch (2026-10-15)
FILES = {
    "fred_benefits_annual.csv": "4fd07cd0e2c379d411929947d7e5f8e0",
    "fred_realgdp_annual.csv": "d23ccfc7fe4b7d96d788af71f8586eea",
    "fred_benefits_monthly.csv": "db9a37ab5d29517f70bbf6deb416c535",
    "fred_claims_weekly.csv": "e6c1c2008b9d47374401cde830f79b2e",
    "sdg131_840.json": "a31a4ebbb59c697ded39214b3acbe601",
    "sdg131_156.json": "f605e05515a3af2b34b79e60f05134c2",
    "sdg131_702.json": "4fa1ce300bbb027338d2dfdc66305887",
    "sdg131_634.json": "445c4aa3ff7aa8ca27e63924f0d09a53",
    "sdg131_578.json": "9a6381d62c39791ceede8b90e524f2de",
    "cares_act_wikipedia_lead.txt": "087f06f311f43d7c10707ab9485c7a36",
}


def md5(b):
    return hashlib.md5(b).hexdigest()


def fetch():
    out = {}
    for name, url in SOURCES.items():
        r = subprocess.run(["curl", "-sS", "-L", "-m", "60", "-A", "neec-evidence-cache/1.0 (research repository)", "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code.decode().strip() != "200" or not body:
            print(f"FAILED {name}: HTTP {code.decode().strip()}")
            continue
        if name.startswith("cares_act"):
            page = list(json.loads(body)["query"]["pages"].values())[0]
            body = (page["extract"][:1400] + "\n").encode()
        with open(os.path.join(DIR, name), "wb") as f:
            f.write(body)
        out[name] = md5(body)
    for k, v in out.items():
        print(f'    "{k}": "{v}",')


def check():
    ok = True
    for name, want in FILES.items():
        path = os.path.join(DIR, name)
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
