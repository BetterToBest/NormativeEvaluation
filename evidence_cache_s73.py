#!/usr/bin/env python3
"""
evidence_cache_s73.py -- NEEC stage 3b (S56): the evidence the blind re-read of C4.4 and C4.2 reads
========================================================================================================================
Session 73. The blind re-read of C4.4 Power Distribution (the 17 units of part (2.11)) and C4.2 Ecological Compliance
(the 16 units of part (2.10)), ledger S56, decisions 69.1, 69.2, found evidence_cache/C4.4/ holding Session 65's one
file (V-Dem's Regimes of the World, through Our World in Data, eight economies) and evidence_cache/C4.2/ Session 64's
two (consumption-based CO2, Global Carbon Budget through OWID, to 2023; the IUCN Red List Index through OWID, rounded
to two decimals). This script adds the sources the blind readings in blind_s73.py rest on, cached before any prior
reading of these units on C4.4 or C4.2 was opened:

  C4.4 clause 1 (democratic accountability for >=80% of major decisions), configured economies: self-employment, % of
    total employment (World Bank WDI, SL.EMP.SELF.ZS, modelled ILO estimates), the four configured economies other
    than the Nordic; US government and total nonfarm payroll employment (BLS CES through FRED, USGOVT and PAYEMS,
    monthly, 2000 onward), the public-sector share on the most generous count.
  C4.4, Centrally Planned Socialism: V-Dem's Regimes of the World for Russia (V-Dem codes the Soviet Union's years
    under Russia), 1917 to 1992, through OWID.
  C4.2 clause 2 (biodiversity): the IUCN Red List Index unrounded (UN SDG Global Database, series ER_RSK_LST, SDG
    15.5.1), the eight configured economies, 2000 onward; the OWID file Session 64 cached rounds to two decimals, at
    which the Nordic series cannot be read as rising or falling.
  C4.2 clauses 3 and 4 (ecological footprint against biocapacity; the four downscaled boundaries): the country data of
    Fanning, O'Neill, Hickel and Roux (2022), Nature Sustainability 5, 26-36 (author-accepted supplementary data,
    White Rose eprints 180834), the historical biophysical sheet, 1992 to 2015, each indicator normalised to its
    per-capita boundary (1 = the boundary); and of O'Neill, Fanning, Lamb and Steinberger (2018), Nature
    Sustainability 1, 88-95 (supplementary data 2), which carries blue water, the one of clause 4's four boundaries
    Fanning et al. (2022) do not (most indicators for 2011). Added after the checkpoint, for the reconciliation of
    China's C4.2: Fanning et al.'s business-as-usual projections, 2016 to 2030 (middle and upper bound).
  C4.2, Centrally Planned Socialism: territorial CO2 emissions of the fifteen Soviet republics' territories, 1960 to
    1991 (Global Carbon Budget, OWID co2-data, which allocates the Soviet years to the successor states); consumption-
    based accounts begin in 1990.
  C4.2, Libertarian Minarchism: the Libertarian Party platform (lp.org), sections 2.2 (Environment) and 2.3 (Energy
    and Resources).

Sources the readings cite but this script does not cache are named in evidence_cache/C4.4/sources_s73.md and
evidence_cache/C4.2/sources_s73.md (prose, not digest-checked). The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s73.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s73.py --fetch    re-fetch every source (network; openpyxl needed) and print md5s
Prints file names and summaries only.
"""
import csv
import io
import json
import os
import sys
import time

import evidence_cache_s71 as e71

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
ISO8 = ["USA", "CHN", "SGP", "QAT", "DNK", "FIN", "NOR", "SWE"]
M49 = {"840": "USA", "156": "CHN", "702": "SGP", "634": "QAT", "208": "DNK", "246": "FIN", "578": "NOR", "752": "SWE"}
WB_SELF = ("https://api.worldbank.org/v2/country/USA;CHN;SGP;QAT/indicator/SL.EMP.SELF.ZS"
           "?format=json&date=2000:2025&per_page=500")
FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
US_SERIES = ["USGOVT", "PAYEMS"]   # thousands of persons, monthly, seasonally adjusted
OWID_ROW = "https://ourworldindata.org/grapher/political-regime.csv"
SDG_RLI = ("https://unstats.un.org/sdgapi/v1/sdg/Series/Data?seriesCode=ER_RSK_LST&"
           + "&".join(f"areaCode={c}" for c in M49) + "&pageSize=2000")
FANNING = ("https://eprints.whiterose.ac.uk/id/eprint/180834/13/Fanning%20et%20al_2021-SupplementaryData_Social"
           "%20shortfall%20and%20ecological%20overshoot_authorAccepted.xlsx")
ONEILL = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41893-018-0021-4/MediaObjects/"
          "41893_2018_21_MOESM2_ESM.xlsx")
LP = "https://lp.org/platform/"
LP_PASSAGES = [(173, 179)]   # 2.2 Environment; 2.3 Energy and Resources
OWID_CO2 = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
USSR15 = ("Russia", "Ukraine", "Belarus", "Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan",
          "Azerbaijan", "Armenia", "Georgia", "Moldova", "Lithuania", "Latvia", "Estonia")
ONEILL_NAMES = {"United States": "USA", "China": "CHN", "Singapore": "SGP", "Qatar": "QAT", "Denmark": "DNK",
                "Finland": "FIN", "Norway": "NOR", "Sweden": "SWE"}

# md5 of each file as fetched and written by --fetch (2026-10-18)
FILES = {
    "C4.4/wb_self_employment_pct.json": "3a06ba5c31a28150702f5491ee581d36",
    "C4.4/fred_us_government_payrolls.csv": "8a8b2390193bd082f72beb7a8e79b389",
    "C4.4/owid_vdem_regimes_russia_1917_1992.csv": "4b0f1e02da0cdc1809fdb39524eff9a7",
    "C4.2/un_sdg_red_list_index.json": "eda7fd16235e1354d82763e7e5ca3700",
    "C4.2/fanning_2022_biophysical_historical.csv": "6acabeb5afe7031d877c4227c950e22c",
    "C4.2/fanning_2022_biophysical_bau.csv": "5f29df900a1b5f2e1ddf5fb9ea6c87e5",
    "C4.2/oneill_2018_biophysical.csv": "712e0bffd71b3dcedc8b63d0c2a5561d",
    "C4.2/owid_gcb_ussr_territorial_co2.csv": "e37cbb115c91ac733eef78c5a216985b",
    "C4.2/lp_platform_environment_extract.txt": "bf66e6e6e95ce646597593ef27afece8",
}


def get(url, ua=False, tries=4):
    """e71.get with retries: the World Bank's API timed out intermittently from this container."""
    for i in range(tries):
        try:
            return e71.get(url, ua=ua)
        except RuntimeError:
            if i == tries - 1:
                raise
            time.sleep(2 ** (i + 1))


def csv_bytes(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue().encode("utf-8")


def xlsx_rows(raw, sheet):
    import openpyxl
    wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True, data_only=True)
    return [tuple("" if c is None else str(c) for c in row) for row in wb[sheet].iter_rows(values_only=True)]


def fetch_files():
    out = {}
    # C4.4 clause 1: self-employment, % of total employment (World Bank WDI, modelled ILO estimate).
    j = json.loads(get(WB_SELF))
    rows = {}
    for x in j[1]:
        if x["value"] is not None:
            rows.setdefault(x["countryiso3code"], {})[x["date"]] = round(x["value"], 3)
    rows = {c: dict(sorted(rows.get(c, {}).items())) for c in ("USA", "CHN", "SGP", "QAT")}
    out["C4.4/wb_self_employment_pct.json"] = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode()
    # C4.4 clause 1, United States: government and total nonfarm payroll employment (BLS CES, FRED), monthly.
    cols = {}
    for sid in US_SERIES:
        rs = list(csv.reader(io.StringIO(get(FRED.format(sid)).decode("utf-8"))))[1:]
        cols[sid] = {r[0]: r[1] for r in rs if r[1] not in ("", ".") and r[0][:4] >= "2000"}
    dates = sorted(set.intersection(*(set(c) for c in cols.values())))
    out["C4.4/fred_us_government_payrolls.csv"] = csv_bytes(["date"] + US_SERIES,
                                                            [[d] + [cols[s][d] for s in US_SERIES] for d in dates])
    # C4.4, Centrally Planned Socialism: Regimes of the World for Russia (the Soviet years), 1917 to 1992.
    rs = list(csv.reader(io.StringIO(get(OWID_ROW).decode("utf-8"))))
    out["C4.4/owid_vdem_regimes_russia_1917_1992.csv"] = csv_bytes(
        rs[0], [r for r in rs[1:] if r[1] == "RUS" and 1917 <= int(r[2]) <= 1992])
    # C4.2 clause 2: the Red List Index unrounded (UN SDG Global Database, ER_RSK_LST).
    j = json.loads(get(SDG_RLI))
    rows = {}
    for x in j["data"]:
        rows.setdefault(M49[str(x["geoAreaCode"])], {})[str(int(x["timePeriodStart"]))] = x["value"]
    rows = {c: {y: v for y, v in sorted(rows.get(c, {}).items()) if y >= "2000"} for c in ISO8}
    out["C4.2/un_sdg_red_list_index.json"] = (json.dumps(rows, indent=0, sort_keys=True) + "\n").encode()
    # C4.2 clauses 3 and 4: Fanning et al. (2022), historical biophysical sheet, the eight economies.
    raw = get(FANNING)
    rs = xlsx_rows(raw, "Biophysical_Historical")
    out["C4.2/fanning_2022_biophysical_historical.csv"] = csv_bytes(
        list(rs[0]) + ["source_md5"], [list(r) + [e71.md5(raw)] for r in rs[1:] if r[1] in ISO8])
    # C4.2 clause 4, after the checkpoint (the reconciliation of China's C4.2): the same file's business-as-usual
    # projections, middle and upper 66% bound, 2016 to 2030, the eight economies.
    out["C4.2/fanning_2022_biophysical_bau.csv"] = csv_bytes(
        ["sheet"] + list(rs[0]) + ["source_md5"],
        [[sh] + list(r) + [e71.md5(raw)] for sh in ("Biophysical_BAU_middle", "Biophysical_BAU_upperCI")
         for r in xlsx_rows(raw, sh)[1:] if r[1] in ISO8 and 2016 <= int(r[2]) <= 2030])
    # C4.2 clause 4 (blue water): O'Neill et al. (2018), biophysical sheet, the eight economies.
    raw = get(ONEILL)
    rs = xlsx_rows(raw, "Biophysical")
    out["C4.2/oneill_2018_biophysical.csv"] = csv_bytes(
        ["country", "iso3c"] + list(rs[0][1:]) + ["source_md5"],
        [[r[0], ONEILL_NAMES[r[0]]] + list(r[1:]) + [e71.md5(raw)] for r in rs[1:] if r[0] in ONEILL_NAMES])
    # C4.2, Centrally Planned Socialism: territorial CO2 of the USSR, 1960 to 1991 (GCB, OWID co2-data).
    # The Global Carbon Budget allocates the Soviet years to the fifteen successor states; the file keeps each
    # state's row, and blind_s73.py sums them.
    rs = list(csv.DictReader(io.StringIO(get(OWID_CO2).decode("utf-8"))))
    out["C4.2/owid_gcb_ussr_territorial_co2.csv"] = csv_bytes(
        ["country", "year", "co2_mt", "population"],
        [[r["country"], r["year"], r["co2"], r["population"]] for r in rs
         if r["country"] in USSR15 and 1960 <= int(r["year"]) <= 1991])
    # C4.2, Libertarian Minarchism: the Libertarian Party platform, sections 2.2 and 2.3 (html_text). The page is
    # served dynamically: its own md5 in the header changes between fetches (it did within this session), the
    # passages do not, so a re-fetch is compared on the passages, not on the file's md5.
    raw = get(LP, ua=True)
    lines = [f"Source: {LP} (Libertarian Party platform, as served 2026-10-18; page md5 {e71.md5(raw)}); text by "
             "evidence_cache_s71.html_text(); passages headed by line range.", ""]
    out["C4.2/lp_platform_environment_extract.txt"] = "\n".join(
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
