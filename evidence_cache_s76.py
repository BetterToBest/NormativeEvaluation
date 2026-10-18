#!/usr/bin/env python3
"""
evidence_cache_s76.py -- NEEC stage 3b (S59): the designs' own texts the blind re-read of C2.6, C3.6 and C4.6 reads
========================================================================================================================
Session 76. The blind re-read of C2.6 Civil Liberties and Rule of Law, C3.6 Productive and Innovative Capacity and
C4.6 Harm Internalization for the 17 designs and mechanisms (ledger S59; decisions 69.1, 69.2), whose units Session 65
scored on a stated rule without reading their sources (evidence_cache/designs_index_s70.json, Session 70's citation
index). Ten of the 17 rest on commercially published books, which are cited, not cached (evidence_cache/C2.6/, C3.6/
and C4.6/sources_s76.md). This script caches passages of the designs' own texts that are freely published, before any
prior reading of these units on these criteria was opened:

  Libertarian Minarchism: the Libertarian Party platform (lp.org), the sections on self-ownership, expression,
    privacy, crime and justice, labour markets, education, health care, internal security and rights (C2.6), and on
    the environment, licensing and health care (C4.6).
  CCO-PTF-CIP-SZH: its research hub at the commit Sessions 71 and 75 cached (8e8a6ba): the PTH charter's rights and
    due-process provisions, the risk framework's appeals and judicial review, the referendum's Judicial Guard and
    honesty rule, the digital-governance privacy principle, the Judicial Guard (C2.6); the 25-hour workweek and the
    simulation's productivity claims (C3.6); the CIP paper's statement of the regulatory-capture problem (C4.6).
  Integral: its Technical White Paper v0.1 (December 2025): local dispute resolution and data safeguards (C2.6), true
    economic calculation (C3.6), ecological balance (C4.6).
  Participatory Economics: participatoryeconomics.info's model text (its PDF): councils and effort-rating procedures
    (C2.6), innovation (C3.6), the community of affected parties' pollution procedure (C4.6).
  Ostrom-Style Commons Governance: Ostrom's Nobel lecture (2009), the design principles (C2.6, C4.6).
  MMT + Job Guarantee: the Levy Institute's working paper 902 (Tcherneva, 2018), the programme's key features (C2.6).
  Universal Basic Income: the Basic Income Earth Network's definition (C2.6).
  Georgism / Land Value Tax: Progress and Poverty (George, 1879; Project Gutenberg #55308), book VIII, chapter 2 (C2.6).
  Stakeholder Capitalism: the World Economic Forum's Measuring Stakeholder Capitalism (2020), the lobbying and
    pollution metrics (C4.6).

The script makes no reading and changes no score.

Modes
  python3 evidence_cache_s76.py            offline: verify every cached file's md5 against FILES
  python3 evidence_cache_s76.py --fetch    re-fetch every source (network) and print md5s
Prints file names and summaries only.
"""
import os
import sys

import evidence_cache_s71 as e71
import evidence_cache_s73 as e73

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "evidence_cache")
RH = "https://raw.githubusercontent.com/BetterToBest/research-hub/8e8a6ba/"
LP = "https://lp.org/platform/"
PE = "https://participatoryeconomics.info/wp-content/uploads/2014/11/Participatory-Economics.pdf"
OSTROM = "https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf"
JG = "https://www.levyinstitute.org/pubs/wp_902.pdf"
BIEN = "https://basicincome.org/about-basic-income/"
GEORGE = "https://www.gutenberg.org/ebooks/55308.txt.utf-8"
WEF = "https://www3.weforum.org/docs/WEF_IBC_Measuring_Stakeholder_Capitalism_Report_2020.pdf"

# (file, source, kind, passages): kind "html", "pdf" or "txt" sets the text the passages are numbered in; for the
# research hub, passages is a list of (page, ranges).
EXTRACTS = [
    ("C2.6/lp_platform_c26_extract.txt", LP, "html",
     [(125, 127), (129, 131), (133, 135), (149, 151), (209, 211), (213, 215), (217, 219), (233, 235), (245, 247)]),
    ("C2.6/cco_research_hub_c26_extract.txt", RH, "hub",
     [("democratic-governance-pth.html", [(476, 547), (955, 959)]),
      ("risk-mitigation-framework.html", [(225, 238), (485, 507), (735, 760)]),
      ("referendum.html", [(120, 120), (161, 161)]),
      ("integrated-digital-governance.html", [(130, 136)]),
      ("citizens-internet-portal.html", [(129, 145)])]),
    ("C2.6/integral_wp_v01_c26_extract.txt", e71.WP, "pdf", [(23894, 23920), (25192, 25223)]),
    ("C2.6/pe_model_c26_extract.txt", PE, "pdf", [(605, 615), (785, 812)]),
    ("C2.6/ostrom_nobel_c26_extract.txt", OSTROM, "pdf", [(681, 710)]),
    ("C2.6/levy_jg_wp902_c26_extract.txt", JG, "pdf", [(164, 197)]),
    ("C2.6/bien_definition_c26_extract.txt", BIEN, "html", [(43, 55)]),
    ("C2.6/george_progress_poverty_c26_extract.txt", GEORGE, "txt", [(12600, 12608)]),
    ("C3.6/cco_research_hub_c36_extract.txt", RH, "hub",
     [("corporate-transformation.html", [(85, 95), (129, 133)]),
      ("index.html", [(645, 650)]),
      ("economic-modeling-simulation.html", [(252, 256), (972, 976), (986, 986)])]),
    ("C3.6/integral_wp_v01_c36_extract.txt", e71.WP, "pdf", [(665, 709)]),
    ("C3.6/pe_model_c36_extract.txt", PE, "pdf", [(1141, 1189)]),
    ("C4.6/lp_platform_c46_extract.txt", LP, "html", [(173, 175), (201, 203), (217, 219)]),
    ("C4.6/pe_model_c46_extract.txt", PE, "pdf", [(1197, 1245)]),
    ("C4.6/integral_wp_v01_c46_extract.txt", e71.WP, "pdf", [(612, 627)]),
    ("C4.6/wef_metrics_c46_extract.txt", WEF, "pdf", [(1099, 1106), (1243, 1251)]),
    ("C4.6/cco_research_hub_c46_extract.txt", RH, "hub", [("citizens-internet-portal.html", [(67, 71)])]),
]

# md5 of each file as fetched and written by --fetch (2026-10-18)
FILES = {
    "C2.6/lp_platform_c26_extract.txt": "34ca5fb683a92ccfa3365e5dab0a53f7",
    "C2.6/cco_research_hub_c26_extract.txt": "13c55881b1c82b41ba722a0af3f9274f",
    "C2.6/integral_wp_v01_c26_extract.txt": "36275341374b101cd4cf8f37b22743b1",
    "C2.6/pe_model_c26_extract.txt": "209e204a0f1385c90330565473626425",
    "C2.6/ostrom_nobel_c26_extract.txt": "69bc03248b5b7eb1e694ebcc832a1a56",
    "C2.6/levy_jg_wp902_c26_extract.txt": "345680f88227039a51bdcffae9bf364a",
    "C2.6/bien_definition_c26_extract.txt": "9b991997a2c3cc2a12ae9a7af8d08fc5",
    "C2.6/george_progress_poverty_c26_extract.txt": "bd3f3ed88fe894a1fdce139e4eb914b9",
    "C3.6/cco_research_hub_c36_extract.txt": "a6b8c91b85bac3ba0d8f3e13ebc3ad1c",
    "C3.6/integral_wp_v01_c36_extract.txt": "ca8dbf0b70af20456372d4eecef3e34d",
    "C3.6/pe_model_c36_extract.txt": "4d127e56ed96609c1e36a09ce08ae92b",
    "C4.6/lp_platform_c46_extract.txt": "b54a3a8289434c2db340dbec078533d0",
    "C4.6/pe_model_c46_extract.txt": "0d098fa8d3e1a9947a5735b9d1f503c2",
    "C4.6/integral_wp_v01_c46_extract.txt": "3dcfaa528c765083ddce75b655ee3f3b",
    "C4.6/wef_metrics_c46_extract.txt": "347715925fb4fc3499975db9d048c162",
    "C4.6/cco_research_hub_c46_extract.txt": "d138918a28268f8dec0e3e1d0c62e0f6",
}


def text_of(raw, kind):
    if kind == "html":
        return e71.html_text(raw)
    if kind == "pdf":
        return e71.pdf_text(raw)
    return raw.decode("utf-8", "replace").replace("\r\n", "\n")


def fetch_files():
    out, raw_of = {}, {}

    def raw(url):
        if url not in raw_of:
            raw_of[url] = e73.get(url, ua=True)
        return raw_of[url]

    for name, src, kind, ranges in EXTRACTS:
        if kind == "hub":
            lines = [f"Source: github.com/BetterToBest/research-hub at 8e8a6ba (the commit Sessions 71 and 75 cached), "
                     "pages as served by raw.githubusercontent.com; text by evidence_cache_s71.html_text(); passages "
                     "headed by page and line range.", ""]
            for page, rr in ranges:
                r = raw(src + page)
                lines += [f"=== {page} (md5 {e71.md5(r)})"] + e71.passages(e71.html_text(r), rr)
        else:
            r = raw(src)
            how = {"html": "evidence_cache_s71.html_text()", "pdf": "pdftotext -layout",
                   "txt": "the plain text as served"}[kind]
            lines = [f"Source: {src} (as served 2026-10-18; md5 {e71.md5(r)}); text by {how}; passages headed by "
                     "line range.", ""] + e71.passages(text_of(r, kind), ranges)
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
    ok &= set(FILES) == {name for name, _, _, _ in EXTRACTS}
    print("SUMMARY: " + ("ALL PASS" if ok and FILES else "SOME FAILED"))
    return ok and bool(FILES)


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        sys.exit(0 if check() else 1)
