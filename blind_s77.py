#!/usr/bin/env python3
"""
blind_s77.py -- NEEC stage 3b, the blind re-read: C2.6, C3.6 and C4.6 for the six configured economies (ledger S60)
==================================================================================================================
Session 77, on Opus 5.5 (decisions 69.1, 69.2; ledger D52, D53). The three criteria v2.0 added (class N): C2.6 Civil
Liberties and Rule of Law, C3.6 Productive and Innovative Capacity and C4.6 Harm Internalization, read for the six
configured national economies, 18 units: Status Quo Market Capitalism (the United States), Nordic Social Democracy
(Denmark, Finland, Norway, Sweden), Centrally Planned Socialism (the Soviet Union, read on the late-Soviet record as
Sessions 72 and 73 read it), and State Capitalism in China, Singapore and Qatar. Session 65 (part (2.11), on Sonnet
5.5) read them on Freedom House's rating, with the law-in-force clauses and C4.6's mortality clause not shown for any
economy (open item (c); ledger I6). The 17 designs' and mechanisms' units on these criteria were Session 76's.

THE BLIND STEP. The readings below were written from blind_review.blind_view() -- the v2.0 clause text and the
evidence_cache/C2.6/, C3.6/ and C4.6/ file names -- from the criteria's measurement text in criteria.json, and from the
sources this session cached (evidence_cache_s77.py) or names (evidence_cache/<criterion>/sources_s77.md), and committed
to the branch as a checkpoint before part (2.11)'s readings of these units, Session 65's record, or the units' published
scores and rationales on these criteria were opened, except as the record discloses (NEEC_BlindReview_s77.md,
section 2).

READINGS, C2.6 (Freedom House civil liberties >=53 of 60; consent to medical treatment in law; health compulsion
prescribed by law, time-limited and open to an independent court)
  2.6.1 clause 1: Freedom House's civil-liberties score in Freedom in the World 2026 (the year 2025, the stated date),
        cross-checked against V-Dem's Civil Liberties Index for the same year; a configuration of several economies
        clears only if each does. V-Dem's index (0 to 1) has no bar of its own, so a call is flagged only where it
        orders an economy with those Freedom House puts on the other side of 53. The historical configuration: the
        1-7 rating Freedom House gave the Soviet Union over the planned economy's last years before the reforms of
        1987-88 (the 0-60 score begins with the 2006 edition); ratings of 6 and 7, the former rating's two lowest
        bands, are the 0.0 band's "16 or less" (the anchor's own correspondence).
  2.6.2 clause 2: cleared where a statute, code or constitutional provision makes medical intervention in general
        depend on the person's consent and protects refusal and withdrawal, its exceptions being emergency and
        compulsion under statutes that state a time limit and a court; short where consent is required only for some
        interventions, or the law permits treatment or admission on another's consent or an official's decision
        without such a statute; not shown where no such provision was located or the law was not reached.
  2.6.3 clause 3: cleared where each compulsion the law in force provides is prescribed by statute, lapses at a
        stated time unless renewed, and is open to a court, with no standing requirement that penalises refusal; short
        where the law provides a compulsion with no stated lapse or no route to a court, a standing requirement that
        penalises refusal by loss of schooling or work, or where Freedom House scores the judiciary's independence
        (question F1) at 0 or 1 of 4, so that no court the person can go to is independent; not shown where the law was
        not reached. The window's emergency measures (V-Dem's PanDem index, the Oxford tracker) are not read: no
        economy's clause turns on them once the law in force is read.
  2.6.4 0.0 (the band's case): clause 1 at 16 or less, with no clause cleared (D28(f)).

Usage: python3 blind_s77.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, the evidence_cache/C2.6/, C3.6/ and
                               C4.6/ files, neec_corpus_v2.json; writes nothing)
Prints file names and summaries only. Deterministic.
"""
import csv
import io
import json
import os
import re
import sys
from contextlib import redirect_stdout

import blind_review as br
import pass_common as pc

HERE = os.path.dirname(os.path.abspath(__file__))
C26, C36, C46 = "C2.6", "C3.6", "C4.6"
E26, E36, E46 = (f"evidence_cache/{c}/" for c in (C26, C36, C46))
FHS, FHR, VDEM, FHP = (E26 + "owid_fh_civil_liberties_score_s77.csv", E26 + "owid_fh_civil_liberties_rating_su_s77.csv",
                       E26 + "owid_vdem_civil_liberties_s77.csv", E26 + "fh_fiw2026_cl_f1_extract.txt")
US26, DK26, FI26, SE26, NO26, SU26, CN26, SG26, N26 = (
    E26 + "us_law_c26_extract.txt", E26 + "dk_law_c26_extract.txt", E26 + "fi_law_c26_extract.txt",
    E26 + "se_law_c26_extract.txt", E26 + "no_law_c26_extract.txt", E26 + "su_law_c26_extract.txt",
    E26 + "cn_law_c26_extract.txt", E26 + "sg_law_c26_extract.txt", E26 + "sources_s77.md")
ECON = ("SQ", "NSD", "CPS", "CN", "SG", "QA")
ISO = {"SQ": ("USA",), "NSD": ("DNK", "FIN", "NOR", "SWE"), "CN": ("CHN",), "SG": ("SGP",), "QA": ("QAT",)}
FH_PAGE = {"USA": "united-states", "DNK": "denmark", "FIN": "finland", "NOR": "norway", "SWE": "sweden",
           "CHN": "china", "SGP": "singapore", "QAT": "qatar"}
NEW = {}


def U(code, cid, verdict, clauses, flag=None, note="", zero=None):
    """One blind reading. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    NEW[(code, cid)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note, zero=zero)


def path(name):
    return os.path.join(HERE, name)


def rows(name):
    return list(csv.DictReader(open(path(name), encoding="utf-8")))


# ---- the figures the C2.6 readings quote, from the cache ---------------------------------------------------------
FH_SCORE = {(r["code"], int(r["year"])): int(r["civlibs_score"]) for r in rows(FHS)}
FH_SU = {int(r["year"]): int(r["civlibs"]) for r in rows(FHR) if r["code"] == "OWID_USS"}
VD = {(r["code"], int(r["year"])): float(r["civ_libs_vdem__estimate_best"]) for r in rows(VDEM)}


def fh_pages():
    """Each country page's civil-liberties score and its F1 score, from the Freedom in the World 2026 extract."""
    out, cur = {}, None
    lines = open(path(FHP), encoding="utf-8").read().splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"=== https://freedomhouse\.org/country/([a-z-]+)/freedom-world/2026", ln)
        if m:
            cur = m.group(1)
            out[cur] = {}
        elif ln == "CL Civil Liberties":
            out[cur]["cl"] = int(lines[i + 1])
        elif ln == "Is there an independent judiciary?":
            out[cur]["f1"] = int(lines[i + 1].split()[-1])
    return out


FHPAGE = fh_pages()


def cl(iso):
    return FH_SCORE[(iso, 2025)]


def f1(iso):
    return FHPAGE[FH_PAGE[iso]]["f1"]


def cl_str(code):
    return ", ".join(f"{iso} {cl(iso)}" for iso in ISO[code])


def vd_str(code, year=2025):
    return ", ".join(f"{iso} {VD[(iso, year)]:.3f}" for iso in ISO[code])


def runs(series):
    """'1972-1979 6; 1980-1986 7; ...' for a {year: value} series (years missing from the source are skipped)."""
    out, items = [], sorted(series.items())
    start, prev, val = items[0][0], items[0][0], items[0][1]
    for y, v in items[1:]:
        if v != val:
            out.append((start, prev, val))
            start, val = y, v
        prev = y
    out.append((start, prev, val))
    return "; ".join(f"{a}-{b} {v}" if a != b else f"{a} {v}" for a, b, v in out)


SU_RUNS = runs(FH_SU)
SU_VD = (min(VD[("RUS", y)] for y in range(1960, 1985)), max(VD[("RUS", y)] for y in range(1960, 1985)))
SRC1 = f"Freedom House, civil-liberties score ({FHS}); V-Dem Civil Liberties Index ({VDEM}); {FHP}"
FIG_PRINT = {
    "Freedom House civil-liberties score, 2025 (FIW 2026)": "; ".join(f"{iso} {cl(iso)}" for iso in sum(ISO.values(), ())),
    "Freedom House civil-liberties score, 2024 (FIW 2025)": "; ".join(f"{iso} {FH_SCORE[(iso, 2024)]}"
                                                                      for iso in sum(ISO.values(), ())),
    "V-Dem Civil Liberties Index, 2025": "; ".join(f"{iso} {VD[(iso, 2025)]:.3f}" for iso in sum(ISO.values(), ())),
    "Freedom House question F1 (independent judiciary), FIW 2026": "; ".join(f"{iso} {f1(iso)}"
                                                                             for iso in sum(ISO.values(), ())),
    "Freedom House civil-liberties rating (1-7), USSR": SU_RUNS,
    "V-Dem Civil Liberties Index, Soviet Union (V-Dem's Russia), 1960-1984, range": f"{SU_VD[0]:.3f} to {SU_VD[1]:.3f}",
}

# =================================================================================================================
# C2.6 Civil Liberties and Rule of Law
# =================================================================================================================
U("SQ", C26, 0.5,
  [("S", f"short: {cl_str('SQ')} of 60 in 2025 ({FH_SCORE[('USA', 2024)]} in 2024), below the bar; V-Dem's index fell "
         f"from {VD[('USA', 2024)]:.3f} to {VD[('USA', 2025)]:.3f}, between Singapore's and the Nordic economies', so "
         "the two sources agree that the bar is not met (reading 2.6.1)", SRC1),
   ("C", "cleared: a hospital patient 'has the right to make informed decisions regarding his or her care', including "
         "'being able to request or refuse treatment' (42 CFR 482.13(b)(2), the conditions of participation every "
         "Medicare hospital meets), and the Supreme Court infers from the Fourteenth Amendment 'a constitutionally "
         "protected liberty interest in refusing unwanted medical treatment' (Cruzan, 1990) (reading 2.6.2)", US26),
   ("S", "short: school-entry requirements penalise refusal by loss of schooling and lapse at no stated time -- in "
         "Virginia 'no student shall be admitted by a school unless' immunised or exempted on religious or medical "
         "grounds, and a conditionally admitted student who falls behind 'shall be excluded from school' (Code of "
         "Virginia 22.1-271.2) -- though federal quarantine and isolation orders are reassessed within 72 hours and "
         f"open to the courts (42 CFR 70.14, 71.37) and Freedom House scores the judiciary {f1('USA')} of 4 on F1 "
         "(reading 2.6.3)", f"{US26}; {E26}us_cfr_42_70.14.html; {FHP}")],
  note="0.5: clause 1 below the bar in 2025; consent protected, compulsion's limits not")

U("NSD", C26, 0.5,
  [("C", f"cleared: {cl_str('NSD')} of 60 in 2025; V-Dem {vd_str('NSD')}, the cross-check agreeing (reading 2.6.1)",
    SRC1),
   ("C", "cleared in each of the four: Denmark, 'no treatment may be begun or continued without the patient's informed "
         "consent', which may be withdrawn at any time (Health Act, section 15); Finland, the patient is treated 'in "
         "mutual understanding' and a refused treatment is replaced by another acceptable one, care against the "
         "patient's will only under the mental-health, substance-abuse, communicable-diseases and special-care acts "
         "(Patients' Rights Act, section 6); Sweden, 'care may not be given without the patient's consent', which may "
         "be withdrawn at any time (Patient Act, chapter 4, section 2); Norway, 'health care may only be given with the "
         "patient's consent', revocable, exceptions only in the communicable-diseases, mental-health and care acts "
         "(Patient and User Rights Act, section 4-1) (reading 2.6.2)", f"{DK26}; {FI26}; {SE26}; {NO26}"),
   ("S", "short in two of the four, so for the configuration: in Sweden a quarantine (Communicable Diseases Act, "
         "chapter 3, section 9) and an area closure (section 10) state no time limit, being lifted only when the "
         "grounds lapse, and the Public Health Agency's closure cannot be appealed except as a refusal of exemption "
         "(chapter 8, section 1); in Finland a standing requirement bars health and social-care workers without "
         "measles, varicella and influenza vaccination from work with vulnerable patients except for a special reason "
         "(Communicable Diseases Act, section 48), a penalty of refusal by loss of work with no lapse. Denmark's "
         "Epidemics Act meets the clause (admission, isolation and treatment orders of at most four weeks, renewable, "
         "each brought before a court within five weekdays; general rules valid four weeks at a time), as do Finland's "
         "quarantine (at most a month) and isolation (two months) with appeal to the administrative court and Sweden's "
         "isolation by the administrative court (three months, then six at a time); Norway's acts were not reached "
         "(reading 2.6.3)", f"{SE26}; {FI26}; {DK26}; {N26}")],
  note="0.5: civil liberties and consent cleared in all four; compulsion's limits short in Sweden and Finland")

U("CPS", C26, 0.0,
  [("S", f"far short: Freedom House's civil-liberties rating of the USSR was {SU_RUNS} (1 best, 7 worst), the former "
         "rating's two lowest bands until the reforms of 1987-88; V-Dem's index for the Soviet Union (its Russia) was "
         f"{SU_VD[0]:.3f} to {SU_VD[1]:.3f} in 1960-1984, the cross-check agreeing (reading 2.6.1)", SRC1),
   ("S", "short: the Fundamentals of Health Legislation (1969) require consent only for surgery, complex diagnostic "
         "methods (article 35) and methods not yet approved (article 34), and for the mentally ill the consent of "
         "parents or guardians in place of their own; no provision protects refusal of other treatment (reading "
         "2.6.2)", SU26),
   ("S", "far short: article 36 leaves 'the cases and procedure of compulsory treatment and compulsory "
         "hospitalisation' of whole classes (tuberculosis, mental, venereal disease, chronic alcoholism, addiction) to "
         "further legislation, with no time limit and no court; psychiatric confinement needed no court decision, "
         "and the USSR had no statute on psychiatric care until 1988 (reading 2.6.3)", SU26)],
  zero=("the civil-liberties rating stood in the former rating's two lowest bands (16 or less of 60) through the "
        "planned economy's years, with compulsory treatment and confinement outside any court (reading 2.6.4)"),
  flag=("0.5: reading the configuration at 1988-89, when glasnost raised the rating to 5 (17 to 25 of 60), the 0.5 "
        "band", "2.6.1"),
  note="0.0: the rating's two lowest bands, consent and compulsion outside law and court")

U("CN", C26, 0.0,
  [("S", f"far short: {cl_str('CN')} of 60 in 2025, in the 0.0 band's 16 or less; V-Dem {vd_str('CN')}, the "
         "cross-check agreeing (reading 2.6.1)", SRC1),
   ("S", "short: the law gives a right to informed consent on condition, diagnosis and treatment (Basic Medical and "
         "Health Care Promotion Law, article 32) and requires explicit consent for surgery and special examinations "
         "or treatment (Civil Code, article 1219), but a patient who has harmed or may harm himself is admitted on the "
         "guardian's consent (Mental Health Law, articles 30 and 31), with re-diagnosis by other psychiatrists, not a "
         "court, as the only challenge (article 32) (reading 2.6.2)", CN26),
   ("S", "short: isolation and medical observation run for periods 'determined according to national rules and "
         "medical examination results', refusal enforced by the police, and the isolation of a place is reviewed only "
         "by the superior government (Infectious Diseases Law, revised 2025); Freedom House scores the judiciary's "
         f"independence {f1('CHN')} of 4 (F1) (reading 2.6.3)", f"{CN26}; {FHP}")],
  zero="the civil-liberties score is in the 0.0 band's 16 or less, with no clause cleared (reading 2.6.4)",
  note="0.0: the civil-liberties score in the band; compulsion with no court")

U("SG", C26, 0.5,
  [("S", f"short: {cl_str('SG')} of 60 in 2025; V-Dem {vd_str('SG')}, the cross-check agreeing (reading 2.6.1)", SRC1),
   ("U", "not shown: no statute, code or constitutional provision requiring consent to medical treatment was located; "
         "consent rests on the common law of negligence (cited, not cached) (reading 2.6.2)", N26),
   ("S", "short: the Director-General of Health may detain and isolate a person 'for such period of time ... as the "
         "Director-General of Health may determine' (Infectious Diseases Act, section 15), may order classes of people "
         "to be vaccinated in an outbreak (section 47), and during a public-health threat or emergency order there is "
         "'no appeal' from the Director-General's orders (section 21K); Freedom House scores the judiciary's "
         f"independence {f1('SGP')} of 4 (F1) (reading 2.6.3)", f"{SG26}; {FHP}")],
  note="0.5: civil liberties in the middle band; compulsion with no stated limit or appeal")

U("QA", C26, 0.5,
  [("S", f"short: {cl_str('QA')} of 60 in 2025, two points above the 0.0 band; V-Dem {vd_str('QA')}, the cross-check "
         "agreeing (reading 2.6.1)", SRC1),
   ("U", "not shown: Qatar's statutes (almeezan.qa) are served as a client-rendered application the container could "
         "not read, so the law in force on consent was not reached (reading 2.6.2)", N26),
   ("S", f"short: Freedom House scores the judiciary's independence {f1('QAT')} of 4 (F1), so no compulsion is open to an independent court, whatever the communicable-"
         "disease law provides (not reached) (reading 2.6.3)", f"{FHP}; {N26}")],
  note="0.5: civil liberties in the middle band, near its foot; no independent court")
