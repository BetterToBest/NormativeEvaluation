#!/usr/bin/env python3
"""
evidence_cache_s77.py -- NEEC stage 3b (S60): the sources the blind re-read of C2.6, C3.6 and C4.6 for the six
configured economies reads
=================================================================================================================
Session 77. The blind re-read of C2.6 Civil Liberties and Rule of Law, C3.6 Productive and Innovative Capacity and C4.6
Harm Internalization for the six configured national economies (ledger S60; decisions 69.1, 69.2): Status Quo Market
Capitalism (the United States), Nordic Social Democracy (Denmark, Finland, Norway, Sweden), Centrally Planned
Socialism (the Soviet Union), and State Capitalism in China, Singapore and Qatar. Session 70 left the law-in-force
clauses as leads (evidence_cache/C2.6/law_in_force_notes_s70.md, C4.6/notes_s70.md); this script caches the measures
and the law in force the readings rest on, before any prior reading of these units on these criteria was opened:

  C2.6 clause 1: Freedom House's civil-liberties score (0-60) and its 1-7 rating for the Soviet years, V-Dem's Civil
    Liberties Index (the cross-check), both as Our World in Data serves them, and Freedom in the World 2026's country
    pages (the score and question F1, "Is there an independent judiciary?").
  C2.6 clauses 2 and 3, the law in force: the United States (42 CFR 482.13(b)(2); Cruzan v. Director (1990); Virginia
    Code 22.1-271.2, a school-entry vaccination requirement); Denmark (the Health Act's section 15, the Epidemics Act
    of 2021, the Psychiatry Act); Finland (the Patients' Rights Act's section 6, the Communicable Diseases Act's
    sections 48, 60, 63 and its appeal provisions); Sweden (the Patient Act's chapter 4, section 2, the Communicable
    Diseases Act's chapters 3, 5 and 8); Norway (the Patient and User Rights Act's section 4-1, from the Directorate
    of Health's annotated text: lovdata.no refused the container); the Soviet Union (the Fundamentals of Health
    Legislation of 1969, articles 34 to 36, and Wikipedia's article on Soviet punitive psychiatry for the practice);
    China (the Basic Medical and Health Care Promotion Law's article 32, the Civil Code's articles 1219 and 1220, the
    Mental Health Law's articles 28 to 35 and 82, the Law on the Prevention and Treatment of Infectious Diseases as
    revised in 2025); Singapore (the Infectious Diseases Act 1976, sections 15, 21K and 47). Qatar's statutes are
    served by almeezan.qa as a client-rendered application this container could not read (evidence_cache/C2.6/
    sources_s77.md).

The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s77.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s77.py --fetch    re-fetch every source (network) and print md5s
Prints file names and summaries only.
"""
import csv
import io
import os
import re
import sys
import tempfile

import evidence_cache_s71 as e71
import evidence_cache_s73 as e73

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
OWID = "https://ourworldindata.org/grapher/{}.csv?v=1&csvType=full&useColumnShortNames=true"
FH = "https://freedomhouse.org/country/{}/freedom-world/2026"
FH_PAGES = ("united-states", "denmark", "finland", "norway", "sweden", "china", "singapore", "qatar")
ECON_ISO = ("USA", "DNK", "FIN", "NOR", "SWE", "CHN", "SGP", "QAT")
SU_ISO = ("OWID_USS", "RUS")
RETSINFO = "https://www.retsinformation.dk/eli/lta/{}/xml"
FINLEX = "https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/{}"
RIKSDAG = "https://data.riksdagen.se/dokument/{}.text"
SSO = "https://sso.agc.gov.sg/Act/IDA1976?ProvIds={}"
ZHWS = "https://zh.wikisource.org/zh-hans/{}"
PWT110 = "https://dataverse.nl/api/access/datafile/554030"
PIP = ("https://api.worldbank.org/pip/v1/pip?country=USA,DNK,FIN,NOR,SWE,CHN,QAT&year=all&povline=3&fill_gaps=false"
       "&format=json")
EF_PDF = "evidence_cache/C3.6/easterly_fischer_1995_nber_w4735.pdf"
MORSC = ("https://sdmx.oecd.org/public/rest/data/OECD.ENV.EPI,DSD_EXP_MORSC@DF_EXP_MORSC,1.0/"
         "USA+DNK+FIN+NOR+SWE+CHN+SGP+QAT.A.MOR.10P6HB.PM_2_5_OUT+AIRPOL_IN+UWATS+USAN+NHANDW._T._T?startPeriod=1990")
GHO = "https://ghoapi.azureedge.net/api/{}?$filter=SpatialDim%20in%20('USA','DNK','FIN','NOR','SWE','CHN','SGP','QAT')"
PWT_COLS = ["countrycode", "year", "rgdpna", "rgdpe", "pop", "emp", "avh", "rtfpna"]
PIP_COLS = ["country_code", "reporting_year", "reporting_level", "welfare_type", "mean", "median", "spl", "spr"]
# Easterly and Fischer (1995), NBER working paper 4735, a scanned PDF with no text layer (Session 70's cache), read as
# page images in Session 77 and transcribed here: Table 1 (PDF page 40), output per worker, total economy, Western
# estimates, and Table 4 (page 43), TFP growth, Western-estimate GNP, by period; Table 5 (page 44), the CES estimates'
# TFP growth on the Western GNP series (1950-87 sample, elasticity of substitution 0.37). Logarithmic growth rates, %
# a year.
EF_TABLES = [
    ("table1_output_per_worker_total_economy_western", "1950-59", "5.8"),
    ("table1_output_per_worker_total_economy_western", "1960-69", "3.0"),
    ("table1_output_per_worker_total_economy_western", "1970-79", "2.1"),
    ("table1_output_per_worker_total_economy_western", "1980-87", "1.4"),
    ("table1_capital_per_worker_total_economy_western", "1960-69", "5.4"),
    ("table1_capital_per_worker_total_economy_western", "1970-79", "5.0"),
    ("table1_capital_per_worker_total_economy_western", "1980-87", "4.0"),
    ("table4_tfp_western_gnp", "1950-60", "1.3"),
    ("table4_tfp_western_gnp", "1960-70", "-0.1"),
    ("table4_tfp_western_gnp", "1970-80", "-0.8"),
    ("table4_tfp_western_gnp", "1980-87", "-1.2"),
    ("table4_tfp_khanin_material_sectors", "1970-80", "0.4"),
    ("table4_tfp_khanin_material_sectors", "1980-87", "0.4"),
    ("table4_tfp_official_material_sectors", "1970-80", "1.4"),
    ("table4_tfp_official_material_sectors", "1980-87", "0.7"),
    ("table5_ces_tfp_western_gnp_1950_87_sample", "1960-69", "1.10"),
    ("table5_ces_tfp_western_gnp_1950_87_sample", "1970-79", "1.16"),
    ("table5_ces_tfp_western_gnp_1950_87_sample", "1980-87", "1.09"),
]

# (file, kind, source, spec). kind: "owid" (spec: (iso codes, first year, last year)); "html", "xml" (the page's text by
# evidence_cache_s71.html_text()), "akn" (the first Akoma Ntoso act of a Finlex consolidated-statute response),
# "txt" (the text as served), each with spec a list of (anchor regex, lines): the passage is the `lines` lines from
# the first line the anchor matches, headed by its line number in that text. "fh": the Freedom in the World 2026
# country pages, the score header and question F1.
EXTRACTS = [
    ("C2.6/owid_fh_civil_liberties_score_s77.csv", "owid", OWID.format("civil-liberties-score-fh"),
     (ECON_ISO, 2015, 2025)),
    ("C2.6/owid_fh_civil_liberties_rating_su_s77.csv", "owid", OWID.format("civil-liberties-rating-fh"),
     (SU_ISO, 1972, 1991)),
    ("C2.6/owid_vdem_civil_liberties_s77.csv", "owid", OWID.format("civil-liberties-index-vdem"),
     (ECON_ISO + SU_ISO, 1960, 2025)),
    ("C2.6/fh_fiw2026_cl_f1_extract.txt", "fh", FH, None),
    ("C2.6/us_law_c26_extract.txt", "multi",
     [("42 CFR 482.13 (Cornell LII)", "html", "https://www.law.cornell.edu/cfr/text/42/482.13",
       [(r"^\(2\) The patient or his or her representative", 1)]),
      ("Cruzan v. Director, Missouri Dept. of Health, 497 U.S. 261 (1990) (Cornell LII)", "html",
       "https://www.law.cornell.edu/supremecourt/text/497/261",
       [(r"constitutionally protected liberty interest in refusing unwanted medical treatment may be inferred", 1)]),
      ("Code of Virginia 22.1-271.2", "html",
       "https://law.lis.virginia.gov/vacode/title22.1/chapter14/section22.1-271.2/",
       [(r"^A\. No student shall be admitted by a school unless", 6)])]),
    ("C2.6/dk_law_c26_extract.txt", "multi",
     [("Sundhedsloven, LBK nr 275 af 12/03/2025", "xml", RETSINFO.format("2025/275"), [(r"^§ 15\.$", 11)]),
      ("Epidemiloven, LOV nr 285 af 27/02/2021", "xml", RETSINFO.format("2021/285"),
       [(r"^§ 12\.$", 25), (r"^§ 14\.$", 9), (r"^§ 15\.$", 9), (r"^§ 18\.$", 9), (r"^§ 23\.$", 27),
        (r"inden 5 søgnedage efter at der er truffet en afgørelse", 5)]),
      ("Psykiatriloven, LBK nr 1045 af 18/09/2024", "xml", RETSINFO.format("2024/1045"),
       [(r"henholdsvis 3, 10, 20 og 30 dage, efter at frihedsberøvelsen", 1),
        (r"skal efter anmodning fra patienten eller patientrådgiveren indbringe", 1)])]),
    ("C2.6/fi_law_c26_extract.txt", "multi",
     [("Laki potilaan asemasta ja oikeuksista 785/1992", "akn", FINLEX.format("1992/785"), [(r"^6 §$", 7)]),
      ("Tartuntatautilaki 1227/2016", "akn", FINLEX.format("2016/1227"),
       [(r"^48 §$", 7), (r"^60 §$", 4), (r"^63 §$", 4), (r"^Muutoksenhaku$", 12)])]),
    ("C2.6/se_law_c26_extract.txt", "multi",
     [("Patientlag (2014:821)", "txt", RIKSDAG.format("sfs-2014-821"), [(r"^2 § Hälso- och sjukvård får inte ges", 13)]),
      ("Smittskyddslag (2004:168)", "txt", RIKSDAG.format("sfs-2004-168"),
       [(r"^9 § Om det finns risk för spridning", 35), (r"^3 § Om någon bär på eller misstänks bära", 25),
        (r"^8 kap\. Överklagande", 38)])]),
    ("C2.6/no_law_c26_extract.txt", "multi",
     [("Pasient- og brukerrettighetsloven 4-1, from Helsedirektoratet's annotated text", "html",
       "https://www.helsedirektoratet.no/rundskriv/pasient-og-brukerrettighetsloven-med-kommentarer/"
       "samtykke-til-helsehjelp", [(r"^§ 4-1 \. Hovedregel om samtykke", 2), (r"^I enkelte tilfeller er det gitt unntak", 1)])]),
    ("C2.6/su_law_c26_extract.txt", "multi",
     [("Основы законодательства Союза ССР и союзных республик о здравоохранении (1969), ru.wikisource.org", "html",
       "https://ru.wikisource.org/wiki/Основы_законодательства_Союза_ССР_и_союзных_республик_о_здравоохранении",
       [(r"^В интересах излечения больного и с его согласия", 1), (r"^Хирургические операции производятся и", 3),
        (r"^В целях охраны здоровья населения органы здравоохранения обязаны", 5)]),
      ("Punitive psychiatry in the Soviet Union, en.wikipedia.org", "html",
       "https://en.wikipedia.org/wiki/Punitive_psychiatry_in_the_Soviet_Union",
       [(r"^The USSR did not have legislative acts regulating psychiatry until 1988", 1),
        (r"^On 15 May 1969, a Soviet Government decree", 1),
        (r"extrajudicial procedure of admission to psychiatric hospitals", 1)])]),
    ("C2.6/cn_law_c26_extract.txt", "multi",
     [("中华人民共和国基本医疗卫生与健康促进法, zh.wikisource.org", "html", ZHWS.format("中华人民共和国基本医疗卫生与健康促进法"),
       [(r"^第三十二条", 3)]),
      ("中华人民共和国民法典, zh.wikisource.org", "html", ZHWS.format("中华人民共和国民法典"),
       [(r"^第一千二百一十九条", 1), (r"^第一千二百二十条", 1)]),
      ("中华人民共和国精神卫生法, zh.wikisource.org", "html", ZHWS.format("中华人民共和国精神卫生法"),
       [(r"^第三十条", 7), (r"^第三十一条", 1), (r"^第三十二条", 1), (r"^第三十五条", 1), (r"^第八十二条", 1)]),
      ("中华人民共和国传染病防治法 (2025 revision), zh.wikisource.org", "html", ZHWS.format("中华人民共和国传染病防治法"),
       [(r"2025年4月30日", 1), (r"^（一）对甲类传染病患者、病原携带者，予以隔离治疗", 13), (r"^第六十四条", 3)])]),
    ("C2.6/sg_law_c26_extract.txt", "multi",
     [("Infectious Diseases Act 1976, section 15 (sso.agc.gov.sg)", "html", SSO.format("pr15-"),
       [(r"^15\. —\(1\)", 1), (r"^\(2\)\s+The Director-General of Health may order the following persons to remain", 1)]),
      ("Infectious Diseases Act 1976, section 21K", "html", SSO.format("pr21K-"), [(r"^21K\.", 1)]),
      ("Infectious Diseases Act 1976, section 47", "html", SSO.format("pr47-"), [(r"^47\. —\(1\)", 1)])]),    ("C3.6/pwt110_selected_economies.csv", "pwt", PWT110, None),
    ("C3.6/pip_spl_selected_economies.csv", "pip", PIP, None),
    ("C3.6/easterly_fischer_1995_tables_s77.csv", "ef", EF_PDF, None),
    ("C4.6/oecd_exp_morsc_gbd2019_s77.csv", "oecd", MORSC, None),
    ("C4.6/who_gho_sdgpoison_s77.csv", "gho", GHO.format("SDGPOISON"), None),
    ("C4.6/us_law_c46_extract.txt", "multi",
     [("42 U.S.C. 247d-6d (the PREP Act), Cornell LII", "html", "https://www.law.cornell.edu/uscode/text/42/247d-6d",
       [(r"a covered person shall be immune from suit and liability under Federal and State law", 1)]),
      ("42 U.S.C. 247d-6e (the Covered Countermeasure Process Fund), Cornell LII", "html",
       "https://www.law.cornell.edu/uscode/text/42/247d-6e",
       [(r"there is hereby established in the Treasury an emergency fund", 1),
        (r"shall be exclusive of any other civil action or proceeding", 1)]),
      ("42 U.S.C. 9607 (CERCLA liability), Cornell LII", "html", "https://www.law.cornell.edu/uscode/text/42/9607",
       [(r"Notwithstanding any other provision or rule of law, and subject only to the defenses", 3)])]),
    ("C4.6/nordic_law_c46_extract.txt", "multi",
     [("Lov om erstatning for miljøskader, LBK nr 994 af 09/09/2014", "xml", RETSINFO.format("2014/994"),
       [(r"^Loven gælder for skade, der forvoldes ved forurening", 1),
        (r"^Den, der som led i erhvervsmæssig eller offentlig aktivitet", 1),
        (r"^Ansvar efter stk\. 1 indtræder ikke", 1)]),
      ("Miljöbalk (1998:808), 32 kap.", "txt", RIKSDAG.format("sfs-1998-808"),
       [(r"^1 § Skadestånd enligt detta kapitel ska betalas för", 14), (r"^3 § Skadestånd enligt detta kapitel betalas", 11)]),
      ("Laki ympäristövahinkojen korvaamisesta 737/1994", "akn", FINLEX.format("1994/737"),
       [(r"^Tässä laissa tarkoitettuna ympäristövahinkona korvataan", 1),
        (r"^Tämän lain mukainen korvausvelvollisuus on, silloinkin kun", 1)])]),
    ("C4.6/cn_law_c46_extract.txt", "multi",
     [("中华人民共和国民法典, zh.wikisource.org", "html", ZHWS.format("中华人民共和国民法典"),
       [(r"^第一千二百二十九条", 1), (r"^第一千二百三十四条", 1), (r"^第一千二百三十五条", 1)])]),
    ("C4.6/su_environment_c46_extract.txt", "multi",
     [("Environmental issues in the Soviet Union, en.wikipedia.org (text from the Library of Congress Country Study)",
       "html", "https://en.wikipedia.org/wiki/Environmental_issues_in_the_Soviet_Union",
       [(r"^In spite of a series of environmental laws and regulations passed in the 1970s", 1),
        (r"^As part of the process of restructuring", 1)])]),
]

FILES = {
    "C2.6/owid_fh_civil_liberties_score_s77.csv": "d84871dbebf3b278e44ee6792c11351e",
    "C2.6/owid_fh_civil_liberties_rating_su_s77.csv": "a61d3ab35c27601e4956d437929ef459",
    "C2.6/owid_vdem_civil_liberties_s77.csv": "453186c30d89aff354843cf252922f22",
    "C2.6/fh_fiw2026_cl_f1_extract.txt": "226863fccf038771d94597e5dab35c27",
    "C2.6/us_law_c26_extract.txt": "3be8591d98de7a90e8cac26e81961735",
    "C2.6/dk_law_c26_extract.txt": "a00ccb5df32518f6ad8aa2b42b8ada0e",
    "C2.6/fi_law_c26_extract.txt": "61453a44bf32d5d6dc771382ab656cbe",
    "C2.6/se_law_c26_extract.txt": "6fa24b518843b3714d44f6dcd63d3523",
    "C2.6/no_law_c26_extract.txt": "7e64991ce089ddc906ffaffacaad3e25",
    "C2.6/su_law_c26_extract.txt": "cf44d4d6e055ea2471a33962f42c7b3d",
    "C2.6/cn_law_c26_extract.txt": "4013a1eef4ea64f56e8c057f0a9e89f9",
    "C2.6/sg_law_c26_extract.txt": "20a708cabba979224ac7d2a52f9e0a32",
    "C3.6/pwt110_selected_economies.csv": "681cb995284ecc8bb636c45a0fa27fd0",
    "C3.6/pip_spl_selected_economies.csv": "53922527d6c62da7345236ae70f36726",
    "C3.6/easterly_fischer_1995_tables_s77.csv": "38a20fe24475a92fdd367124676a201f",
    "C4.6/oecd_exp_morsc_gbd2019_s77.csv": "29a8bdab034c2353e6031232d3dddc7c",
    "C4.6/who_gho_sdgpoison_s77.csv": "5234238af2b68acd01986b0f96e8ee4d",
    "C4.6/us_law_c46_extract.txt": "2f0af564d0cae66d3c590c7514ca0462",
    "C4.6/nordic_law_c46_extract.txt": "57df9afa0ccd04e6dab71c6ea520c70f",
    "C4.6/cn_law_c46_extract.txt": "2f39195b8d06dc4756740c4b0554d859",
    "C4.6/su_environment_c46_extract.txt": "25194c10c2568a17d8be16b271490e11",
}


def owid_rows(raw, isos, y0, y1):
    rows = list(csv.reader(io.StringIO(raw.decode("utf-8"))))
    return [rows[0]] + [r for r in rows[1:] if r[1] in isos and y0 <= int(r[2]) <= y1]


def text_of(raw, kind):
    if kind in ("html", "xml"):
        return e71.html_text(raw)
    if kind == "akn":
        return e71.html_text(raw.split(b"</akomaNtoso>")[0])
    return raw.decode("utf-8", "replace").replace("\r\n", "\n")


def grab(text, anchors):
    """Each anchor's passage: `n` non-empty lines from the first line the regex matches, headed by its line number."""
    lines = text.splitlines()
    out = []
    for rx, n in anchors:
        hit = next((i for i, ln in enumerate(lines) if re.search(rx, ln)), None)
        if hit is None:
            raise RuntimeError(f"anchor not found: {rx}")
        got, j = [], hit
        while len(got) < n and j < len(lines):
            if lines[j].strip():
                got.append(lines[j].rstrip())
            j += 1
        out += [f"--- from line {hit + 1} (anchor /{rx}/)"] + got + [""]
    return out


def fetch_files():
    out, raw_of = {}, {}

    def raw(url):
        if url not in raw_of:
            raw_of[url] = e73.get(url, ua=True)
        return raw_of[url]

    for name, kind, src, *spec in EXTRACTS:
        spec = spec[0] if spec else None
        if kind == "pwt":
            import pandas as pd
            with tempfile.TemporaryDirectory() as tmp:
                p = os.path.join(tmp, "pwt.dta")
                open(p, "wb").write(raw(src))
                df = pd.read_stata(p)
            df = df[df.countrycode.isin(ECON_ISO) & (df.year >= 1999)][PWT_COLS].sort_values(["countrycode", "year"])
            out[name] = df.to_csv(index=False, lineterminator="\n", float_format="%.6f").encode("utf-8")
        elif kind == "pip":
            import json
            recs = sorted((r for r in json.loads(raw(src)) if r["reporting_year"] >= 2003),
                          key=lambda r: (r["country_code"], r["reporting_year"], r["reporting_level"]))
            buf = io.StringIO()
            w = csv.writer(buf, lineterminator="\n")
            w.writerow(PIP_COLS)
            w.writerows([r[c] for c in PIP_COLS] for r in recs)
            out[name] = buf.getvalue().encode("utf-8")
        elif kind == "ef":
            buf = io.StringIO()
            w = csv.writer(buf, lineterminator="\n")
            w.writerow(["series", "period", "growth_pct_a_year"])
            w.writerows(EF_TABLES)
            out[name] = buf.getvalue().encode("utf-8")
        elif kind == "oecd":
            rs = list(csv.DictReader(io.StringIO(e73.get(src + "&format=csvfilewithlabels", ua=True).decode("utf-8-sig"))))
            keep = sorted(((r["REF_AREA"], r["RISK"], r["TIME_PERIOD"], r["OBS_VALUE"]) for r in rs))
            buf = io.StringIO()
            w = csv.writer(buf, lineterminator="\n")
            w.writerow(["ref_area", "risk", "year", "deaths_per_million"])
            w.writerows(keep)
            out[name] = buf.getvalue().encode("utf-8")
        elif kind == "gho":
            import json
            vs = json.loads(raw(src))["value"]
            keep = sorted((v["SpatialDim"], v["TimeDim"], v["NumericValue"]) for v in vs if v["Dim1"] == "SEX_BTSX")
            buf = io.StringIO()
            w = csv.writer(buf, lineterminator="\n")
            w.writerow(["iso", "year", "rate_per_100000"])
            w.writerows(keep)
            out[name] = buf.getvalue().encode("utf-8")
        elif kind == "owid":
            isos, y0, y1 = spec
            r = raw(src)
            buf = io.StringIO()
            csv.writer(buf, lineterminator="\n").writerows(owid_rows(r, isos, y0, y1))
            out[name] = buf.getvalue().encode("utf-8")
        elif kind == "fh":
            lines = ["Source: Freedom House, Freedom in the World 2026, country pages (as served 2026-10-18); text by "
                     "evidence_cache_s71.html_text(); per page, the score header and question F1.", ""]
            for page in FH_PAGES:
                r = raw(src.format(page))
                lines += [f"=== {src.format(page)} (md5 {e71.md5(r)})"]
                lines += grab(e71.html_text(r), [(r"^Freedom in the World 2026$", 11), (r"^F1$", 5)])
            out[name] = "\n".join(lines).encode()
        else:
            lines = ["Sources as served 2026-10-18; text by evidence_cache_s71.html_text() (an Akoma Ntoso response: "
                     "its first act; a riksdagen.se .text file: as served); passages headed by line number and anchor.",
                     ""]
            for title, k, url, anchors in src:
                r = raw(url)
                lines += [f"=== {title}: {url} (md5 {e71.md5(r)})"] + grab(text_of(r, k), anchors)
            out[name] = "\n".join(lines).encode()
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
    ok &= set(FILES) == {e[0] for e in EXTRACTS}
    print("SUMMARY: " + ("ALL PASS" if ok and FILES else "SOME FAILED"))
    return ok and bool(FILES)


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        sys.exit(0 if check() else 1)
