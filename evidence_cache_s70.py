#!/usr/bin/env python3
"""
evidence_cache_s70.py -- NEEC stage 3b setup (S53): evidence caches for the shortcuts the accelerated pass left
========================================================================================================================
Session 70. STATE.md's "Next work" item 0 (ledger S53): cache the sources the accelerated pass (Sessions 63-65)
skipped before Session 76-77's blind re-read of C2.1, C2.3, C2.4 (clause 1 and related clauses, configured
economies), C2.6 and C4.6 (law-in-force clauses and C4.6's mortality clause), C3.6 (Easterly and Fischer, 1995, for
Centrally Planned Socialism), and the 17 designs' and mechanisms' own sources for C2.6, C3.6 and C4.6 (index only,
`evidence_cache/designs_index_s70.json`). This session's own network access was initially denied by the
environment's policy (only github.com reachable); the owner broadened it mid-session (see the handoff), after which
every fetch below succeeded except as noted in each criterion's `notes_s70.md`.

The cache records evidence, much of it a lead for a future session rather than a completed reading: several sources
were not reachable even after the network was broadened (data.worldhappiness.report's data API, bls.gov, the OECD's
legacy and current data services, the IDEA turnout database's live query tool, most of the 17 designs' own primary
literature). Each such gap is named in the matching `notes_s70.md`/`law_in_force_notes_s70.md`. This script verifies
only the files it successfully cached; it makes no reading and changes no score.

Modes
  python3 evidence_cache_s70.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s70.py --fetch    re-fetch the sources in SOURCES (network) and print their md5s
Prints file names and summaries only.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (criterion directory, filename): source URL. Re-running --fetch reproduces each file from its live source; a
# source that moves or is retired will show as a digest mismatch here, not silently.
SOURCES = {
    ("C2.1", "whr26_statistical_appendix.pdf"):
        "https://files.worldhappiness.report/WHR26_Statistical_Appendix.pdf",
    ("C2.4", "idea_voter_turnout_codebook.pdf"):
        "https://www.idea.int/sites/default/files/publications/voter-turnout-database-codebook.pdf",
    ("C2.6", "us_cfr_42_70.14.html"):
        "https://www.law.cornell.edu/cfr/text/42/70.14",
    ("C2.6", "us_cfr_42_71.37.html"):
        "https://www.law.cornell.edu/cfr/text/42/71.37",
    ("C3.6", "easterly_fischer_1995_nber_w4735.pdf"):
        "https://www.nber.org/system/files/working_papers/w4735/w4735.pdf",
    ("C4.6", "SDGAIRBOD.json"):
        "https://ghoapi.azureedge.net/api/SDGAIRBOD?$filter=SpatialDim in ('USA','CHN','SGP','QAT')",
    ("C4.6", "SDGWSHBOD.json"):
        "https://ghoapi.azureedge.net/api/SDGWSHBOD?$filter=SpatialDim in ('USA','CHN','SGP','QAT')",
    ("C4.6", "SDGPOISON.json"):
        "https://ghoapi.azureedge.net/api/SDGPOISON?$filter=SpatialDim in ('USA','CHN','SGP','QAT')",
    ("C4.6", "air42.json"):
        "https://ghoapi.azureedge.net/api/AIR_42?$filter=SpatialDim in ('USA','CHN','SGP','QAT')",
}

# md5 of each file as fetched and written on 2026-10-18
FILES = {
    "whr26_statistical_appendix.pdf": "e9347cf9441fa9531d48797f78a07c5c",
    "idea_voter_turnout_codebook.pdf": "e6f1570cd01d65b81fe7b7c1000e5568",
    "us_cfr_42_70.14.html": "2101bbf982ddddd479d9910350fdad08",
    "us_cfr_42_71.37.html": "79c8db362339d0d930bdaf2966d18cd6",
    "easterly_fischer_1995_nber_w4735.pdf": "bee075365a835728ef4b05378d4cca77",
    "SDGAIRBOD.json": "091ced516e9959bb409ab44ae4a8f369",
    "SDGWSHBOD.json": "8b63bfb02b54f4a179e92fc58f0ade8d",
    "SDGPOISON.json": "7b6842c47648ccda913e8f419b50e450",
    "air42.json": "1621b4d1e37ed69226adfd3b93a0f93c",
    "designs_index_s70.json": "b89a2c457569e279d9dda20d506be822",
}
# (criterion, filename) for every file FILES checks, except designs_index_s70.json which sits at evidence_cache/.
LOCATION = {k[1]: k[0] for k in SOURCES}


def md5(b):
    return hashlib.md5(b).hexdigest()


def path_for(name):
    if name in LOCATION:
        return os.path.join(HERE, "evidence_cache", LOCATION[name], name)
    return os.path.join(HERE, "evidence_cache", name)


def fetch():
    out = {}
    for (crit, name), url in SOURCES.items():
        d = os.path.join(HERE, "evidence_cache", crit)
        os.makedirs(d, exist_ok=True)
        r = subprocess.run(["curl", "-sS", "-L", "-m", "60", "-A", "neec-evidence-cache/1.0 (research repository)",
                             "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if code.decode().strip() != "200" or not body:
            print(f"FAILED {name}: HTTP {code.decode().strip()}")
            continue
        path = os.path.join(d, name)
        with open(path, "wb") as f:
            f.write(body)
        out[name] = md5(body)
    for k, v in out.items():
        print(f'    "{k}": "{v}",')


def check():
    ok = True
    for name, want in FILES.items():
        path = path_for(name)
        good = os.path.isfile(path) and md5(open(path, "rb").read()) == want
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'} {name}: md5 {want[:8]}")
    print("SUMMARY: " + ("ALL PASS" if ok and FILES else "SOME FAILED"))
    return ok and bool(FILES)


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        check()
