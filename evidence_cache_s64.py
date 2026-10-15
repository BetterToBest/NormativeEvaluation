#!/usr/bin/env python3
"""
evidence_cache_s64.py -- NEEC rescoring pass, stage 2: the data files for C4.2 Ecological Compliance (group 2.10)
==================================================================================================================
Session 64. C4.2's clause 1 is the compound annual rate of change of consumption-based CO2 emissions (Global Carbon
Budget national consumption-based accounts) and its clause 2 the IUCN Red List Index (SDG indicator 15.5.1). Our World
in Data republishes both by country as open CSV (its charts "consumption-co2-emissions", from the Global Carbon Budget,
and "red-list-index", from the IUCN); this keeps the rows of the nine economies the group reads, fetched once with their
md5s: the four configured economies (United States, China, Singapore, Qatar), the four Nordic countries Nordic Social
Democracy is read on (Denmark, Finland, Norway, Sweden), and the world.
The Footprint Data Foundation's National Footprint and Biocapacity Accounts (clause 3) and the national-boundary accounts
(clause 4) were not reachable (data.footprintnetwork.org's API answers HTTP 403; no open republication was located), so
those clauses are "not shown" for the economies, as the record says.
The cache records evidence. It makes no reading and changes no score. The reading script (rescoring_s64.py) checks each
file below by digest and recomputes every figure it quotes.

Modes
  python3 evidence_cache_s64.py            offline: verify every file's md5 against FILES
  python3 evidence_cache_s64.py --fetch    fetch the sources (network), rewrite evidence_cache/C4.2/ and print the md5s
Prints file names and summaries only.
"""
import csv
import hashlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(HERE, "evidence_cache", "C4.2")
OWID = "https://ourworldindata.org/grapher/{}.csv?v=1&csvType=full&useColumnShortNames=false"
ENTITIES = ["China", "Denmark", "Finland", "Norway", "Qatar", "Singapore", "Sweden", "United States", "World"]
SOURCES = {"owid_gcb_consumption_co2.csv": OWID.format("consumption-co2-emissions"),
           "owid_iucn_red_list_index.csv": OWID.format("red-list-index")}
# md5 of each file as fetched and written by --fetch (2026-10-15)
FILES = {
    "owid_gcb_consumption_co2.csv": "2f771097baac251ca01fcae8e81cc630",
    "owid_iucn_red_list_index.csv": "c16141c8b0a74db8a81411f74d09ef34",
}


def md5(b):
    return hashlib.md5(b).hexdigest()


def fetch():
    out = {}
    for name, url in SOURCES.items():
        r = subprocess.run(["curl", "-sS", "-L", "-m", "90", "-A", "neec-evidence-cache/1.0 (research repository)", "-w",
                            "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code.decode().strip() != "200" or not body:
            print(f"FAILED {name}: HTTP {code.decode().strip()}")
            continue
        rows = list(csv.reader(io.StringIO(body.decode("utf-8"))))
        keep = [rows[0]] + sorted((x for x in rows[1:] if x[0] in ENTITIES), key=lambda x: (x[0], int(x[2])))
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerows(keep)
        data = buf.getvalue().encode("utf-8")
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
