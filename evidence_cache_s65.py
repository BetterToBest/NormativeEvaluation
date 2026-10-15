#!/usr/bin/env python3
"""
evidence_cache_s65.py -- NEEC rescoring pass, stage 2: the data files for C4.1 Intergenerational Justice (group 2.11)
====================================================================================================================
Session 65. C4.1's clause 1 is general government gross debt as a share of GDP (IMF World Economic Outlook, through the
IMF DataMapper API, indicator GGXWDG_NGDP); clause 2 is net national saving as a share of gross national income, positive
over the scoring window (World Bank WDI: gross savings, NY.GNS.ICTR.GN.ZS, less consumption of fixed capital,
NY.ADJ.DKAP.GN.ZS). This keeps the rows of the nine economies the pass reads, fetched once with their md5s: the four
configured economies (United States, China, Singapore, Qatar) and the four Nordic countries Nordic Social Democracy is read
on (Denmark, Finland, Norway, Sweden). Records evidence; makes no reading and changes no score.

Modes
  python3 evidence_cache_s65.py            offline: verify every file's md5 against FILES
  python3 evidence_cache_s65.py --fetch    fetch the sources (network), rewrite evidence_cache/C4.1/ and print the md5s
Prints file names and summaries only.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "evidence_cache", "C4.1")
ISO = ["USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE"]
IMF = "https://www.imf.org/external/datamapper/api/v1/GGXWDG_NGDP/" + "/".join(ISO)
WB = "https://api.worldbank.org/v2/country/" + ";".join(ISO) + "/indicator/{}?format=json&date=2000:2025&per_page=500"
SOURCES = {"imf_weo_gross_debt_pct_gdp.json": IMF,
           "wb_gross_savings_pct_gni.json": WB.format("NY.GNS.ICTR.GN.ZS"),
           "wb_consumption_fixed_capital_pct_gni.json": WB.format("NY.ADJ.DKAP.GN.ZS")}
# md5 of each file as fetched and written by --fetch (2026-10-15)
FILES = {
    "imf_weo_gross_debt_pct_gdp.json": "148ad7d2c97f421dcadc839ea72f99e1",
    "wb_gross_savings_pct_gni.json": "f84dd1655a39ca4107ee4e348c4da369",
    "wb_consumption_fixed_capital_pct_gni.json": "56352b479a298464aacc85eeedd1d136",
}


def md5(b):
    return hashlib.md5(b).hexdigest()


def fetch():
    os.makedirs(DIR, exist_ok=True)
    out = {}
    for name, url in SOURCES.items():
        r = subprocess.run(["curl", "-sS", "-L", "-m", "90", "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code.decode().strip() != "200" or not body:
            print(f"FAILED {name}: HTTP {code.decode().strip()}")
            continue
        j = json.loads(body)
        if name.startswith("imf"):
            vals = j["values"]["GGXWDG_NGDP"]
            rows = {c: vals.get(c, {}) for c in ISO}
        else:
            rows = {}
            for x in j[1]:
                if x["value"] is not None:
                    rows.setdefault(x["countryiso3code"], {})[x["date"]] = x["value"]
            rows = {c: dict(sorted(rows.get(c, {}).items())) for c in ISO}
        data = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode("utf-8")
        with open(os.path.join(DIR, name), "wb") as f:
            f.write(data)
        out[name] = md5(data)
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
