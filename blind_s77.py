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

READINGS, C3.6 (output per hour and TFP non-declining over 20 years; basic-needs output at the system's own hours)
  3.6.1 clauses 1 and 2: Penn World Table 11.0, compound annual change over 2003-2023, the 20 years to its last year
        (the nearest to the stated date): clause 1 real GDP at constant national prices (rgdpna) per hour worked
        (emp x avh), clause 2 TFP at constant national prices (rtfpna); where PWT's hours begin later, the longest
        window they give; a configuration of several economies clears only if each does. The historical
        configuration: Easterly and Fischer (1995), the Western estimates for the total economy over the two decades
        to 1987 -- output per worker (their Table 1) for clause 1, no hours series being at hand (sources_s77.md), and
        growth-accounting TFP for GNP (Table 4) for clause 2, the measure PWT's rtfpna corresponds to; their CES
        estimates (Table 5), which attribute the slowdown to diminishing returns to capital, are the alternative.
  3.6.2 clause 3: the poverty basket's measure is C1.1's Societal Poverty Line; cleared where the economy's mean income
        or consumption per person (the World Bank's Poverty and Inequality Platform, latest survey) exceeds the line,
        so that output, as the households receive it, would provision the basket for the whole population at the
        economy's actual hours (PWT's avh); where the Platform has no survey, output per person (PWT rgdpe / pop)
        against the highest line the economy's median could set (the line is 1.30 plus half the median, 2021 PPP
        dollars a day, and the median is below output per person). The test is met by any economy whose median is
        not far below its mean; it binds designs with short stated hours. Not shown where no survey or output
        record is at hand (the historical configuration).
  3.6.3 0.0 (the band's case): productivity or TFP declining over 20 years with no credible pathway under the
        system's own logic; never with a clause cleared (D28(f)), so a decline with a clause cleared is 0.5, flagged
        toward 0.0.

READINGS, C4.6 (pollution mortality non-increasing; liability enforceable by those harmed; regulators free of improper
influence, WJP sub-factor 6.2 >= 0.77)
  4.6.1 clause 1: the WHO's SDG series do not span the window (the cache's air-pollution series hold 2021 alone, WASH
        2019 alone), so the GBD's risk-attributable rates, as the OECD's GBD 2019 dataset gives them: deaths per
        million attributed to ambient PM2.5 and household solid fuels (SDG 3.9.1) and to unsafe water, unsafe
        sanitation and no handwashing (3.9.2), plus the WHO's unintentional-poisoning rate (3.9.3), at 1999 and 2019,
        the 20 years to the dataset's last year (poisoning from 2000, its first year). The dataset's rates are crude,
        not age-standardized; ageing raises a crude rate, so a fall in it is a fall in the standardized rate, and a
        rise would be not shown. No cross-check with the SDG series is possible over the window. A configuration
        clears only if each economy does; the historical configuration predates the GBD (1990).
  4.6.2 clause 2: cleared where the law makes those who cause harm liable, those harmed can claim before an
        independent court, collectively where the harm is dispersed, no immunity leaves a class of harm uncompensated
        or compensated from public funds alone, and a claim decided against those who caused the harm and paid within
        the window is named; short where an immunity shifts a class of harm to public funds, or Freedom House scores
        the judiciary's independence (F1) at 0 or 1 of 4 (reading 2.6.3's test); not shown where liability law stands
        but no such claim is named in the cache, or the law was not reached.
  4.6.3 clause 3: the World Justice Project's sub-factor 6.2 in its 2025 edition (Session 65's file), at the two
        decimals it publishes, against the bar of 0.77; the Index does not cover the Soviet Union (not shown).
  4.6.4 0.0 (the band's case): no structural mechanism makes harm a cost to whoever causes it -- those who cause it
        shielded from liability with no compensation they fund, and its regulation controlled by those it regulates --
        or pollution mortality rising with no pathway to reverse it; never with a clause cleared (D28(f)).

THE COMPARISON (written after the checkpoint, 3cdf73d). compare_group() sets each reading against part (2.11)'s
(rescoring_s65.NEW_UNITS). All 18 revise; four verdicts differ, all on C3.6 (Status Quo, China and Singapore 0.5 to
1.0, clause 3 now read; Centrally Planned Socialism 0.0 to 0.5, clause 1 cleared on Easterly and Fischer's table 1,
so that D28(f) bars 0.0). Under Session 71's rule every blind reading stands (STAND); a standing verdict difference
without a flag toward the prior's verdict gets one (FLAGS). FINAL, the blind readings with FLAGS, is what the generator
session (ledger S61) applies. The group holds no CCO-PTF-CIP-SZH unit (decisions 57.2, 69.4).

Usage: python3 blind_s77.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, blind_s71.py to blind_s76.py,
                               rescoring_s65.py, the evidence_cache/C2.6/, C3.6/ and C4.6/ files,
                               wjp_rol_sf62_2012_2025.csv, neec_corpus_v2_s65_snapshot.json, neec_scores_v2_s65_snapshot.csv and
                               NEEC_BlindReview_s77.md; writes nothing)
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
PWT, PIPF, EF, EFPDF, N36 = (E36 + "pwt110_selected_economies.csv", E36 + "pip_spl_selected_economies.csv",
                             E36 + "easterly_fischer_1995_tables_s77.csv", E36 + "easterly_fischer_1995_nber_w4735.pdf",
                             E36 + "sources_s77.md")
MORS, POIS, US46, NOR46, CN46, SU46, N46 = (
    E46 + "oecd_exp_morsc_gbd2019_s77.csv", E46 + "who_gho_sdgpoison_s77.csv", E46 + "us_law_c46_extract.txt",
    E46 + "nordic_law_c46_extract.txt", E46 + "cn_law_c46_extract.txt", E46 + "su_environment_c46_extract.txt",
    E46 + "sources_s77.md")
WJP = "wjp_rol_sf62_2012_2025.csv"
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


# =================================================================================================================
# C3.6 Productive and Innovative Capacity
# =================================================================================================================
PWT_ROWS = {(r["countrycode"], int(r["year"])): r for r in rows(PWT)}


def pwt(iso, y, col):
    v = PWT_ROWS[(iso, y)][col]
    return float(v) if v else None


def cagr(a, b, years):
    return 100 * ((b / a) ** (1 / years) - 1)


def lp(iso, y):
    h = pwt(iso, y, "avh")
    return None if h is None else pwt(iso, y, "rgdpna") / (pwt(iso, y, "emp") * h)


def lp_window(iso, y1=2023):
    y0 = next(y for y in range(y1 - 20, y1) if lp(iso, y) is not None)
    return y0, cagr(lp(iso, y0), lp(iso, y1), y1 - y0)


TFP = {iso: cagr(pwt(iso, 2003, "rtfpna"), pwt(iso, 2023, "rtfpna"), 20) for iso in sum(ISO.values(), ())}
LPW = {iso: lp_window(iso) for iso in sum(ISO.values(), ())}
AVH = {iso: pwt(iso, 2023, "avh") for iso in sum(ISO.values(), ())}
PIPR = {}
for r in rows(PIPF):
    if r["reporting_level"] == "national":
        PIPR[r["country_code"]] = r  # the latest national survey (rows are in year order)
SPL_K = {round(float(r["spl"]) - float(r["median"]) / 2, 2) for r in PIPR.values()}
assert SPL_K == {1.3}, SPL_K


def ratio(iso):
    r = PIPR[iso]
    return float(r["mean"]) / float(r["spl"])


SG_OUT = pwt("SGP", 2023, "rgdpe") / pwt("SGP", 2023, "pop") / 365
SG_BOUND = SG_OUT / (1.30 + SG_OUT / 2)
EFT = {(r["series"], r["period"]): float(r["growth_pct_a_year"]) for r in rows(EF)}
EF_LP = [EFT[("table1_output_per_worker_total_economy_western", p)] for p in ("1960-69", "1970-79", "1980-87")]
EF_TFP = [EFT[("table4_tfp_western_gnp", p)] for p in ("1960-70", "1970-80", "1980-87")]
EF_CES = [EFT[("table5_ces_tfp_western_gnp_1950_87_sample", p)] for p in ("1960-69", "1970-79", "1980-87")]


def pct(x):
    return f"{x:+.2f}"


def lp_str(code):
    return ", ".join(f"{iso} {pct(LPW[iso][1])}" + (f" ({LPW[iso][0]}-2023)" if LPW[iso][0] != 2003 else "")
                     for iso in ISO[code])


def tfp_str(code):
    return ", ".join(f"{iso} {pct(TFP[iso])}" for iso in ISO[code])


def r3_str(code):
    return ", ".join(f"{iso} {ratio(iso):.2f} times ({PIPR[iso]['welfare_type']}, {PIPR[iso]['reporting_year']}; "
                     f"{AVH[iso]:.0f} hours a year)" for iso in ISO[code])


SRC36 = f"Penn World Table 11.0 ({PWT})"
SRC363 = f"World Bank PIP ({PIPF}); {PWT}"
FIG_PRINT.update({
    "PWT 11.0, output per hour, compound % a year, 2003-2023": "; ".join(
        f"{iso} {pct(v)}" + (f" ({y0}-2023)" if y0 != 2003 else "") for iso, (y0, v) in LPW.items()),
    "PWT 11.0, TFP (rtfpna), compound % a year, 2003-2023": "; ".join(f"{iso} {pct(v)}" for iso, v in TFP.items()),
    "PIP, mean per person over the Societal Poverty Line, latest national survey": "; ".join(
        f"{iso} {ratio(iso):.2f}" for iso in PIPR),
    "Singapore, PWT output per person a day (2023) and its ratio to the highest line its median could set":
        f"{SG_OUT:.1f}; {SG_BOUND:.2f}",
    "Easterly and Fischer, USSR, output per worker / growth-accounting TFP / CES TFP, 1960s, 1970s, 1980-87":
        f"{EF_LP} / {EF_TFP} / {EF_CES}",
})

U("SQ", C36, 1.0,
  [("C", f"cleared: {lp_str('SQ')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: {tfp_str('SQ')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: mean income {r3_str('SQ')} the Societal Poverty Line (reading 3.6.2)", SRC363)],
  note="1.0: productivity and TFP rising over 2003-2023; output well above the basket at actual hours")

U("NSD", C36, 0.5,
  [("C", f"cleared in each of the four: {lp_str('NSD')} % a year (reading 3.6.1)", SRC36),
   ("S", f"short in two of the four, so for the configuration: {tfp_str('NSD')} % a year; Finland's and Norway's TFP "
         "fell over the 20 years (reading 3.6.1)", SRC36),
   ("C", f"cleared in each of the four: mean income {r3_str('NSD')} the Societal Poverty Line (reading 3.6.2)", SRC363)],
  note="0.5: TFP declining in Finland and Norway; output per hour rising in all four")

U("CPS", C36, 0.5,
  [("C", "cleared: output per worker in the total economy (Western estimates) grew "
         f"{EF_LP[0]}%, {EF_LP[1]}% and {EF_LP[2]}% a year in 1960-69, 1970-79 and 1980-87, slowing but not declining "
         "(reading 3.6.1)", f"Easterly and Fischer (1995), table 1 ({EF}; {EFPDF}, PDF page 40)"),
   ("S", f"short: growth-accounting TFP for Western-estimate GNP was {EF_TFP[0]}, {EF_TFP[1]} and {EF_TFP[2]}% a year "
         "in 1960-70, 1970-80 and 1980-87, declining over the two decades to 1987 while capital per worker grew 4 to 5% "
         "a year: the extensive growth the criterion's second clause is written to catch (reading 3.6.1)",
    f"Easterly and Fischer (1995), tables 1 and 4 ({EF}; {EFPDF}, PDF pages 40 and 43)"),
   ("U", "not shown: no survey of incomes or consumption against a basket exists for the Soviet economy in the cache, "
         "and Easterly and Fischer's record is of growth, not provisioning (reading 3.6.2)", N36)],
  flag=("0.0: the band's case (TFP declining over 20 years, the system's own logic offering no pathway, Easterly and "
        "Fischer's 'worst in the world after we control for investment and human capital'), held at 0.5 only by "
        "D28(f) because output per worker rose; the alternative reading of Easterly and Fischer's CES estimates "
        f"(TFP {EF_CES[0]}, {EF_CES[1]} and {EF_CES[2]}% a year, constant, with an elasticity of substitution of "
        "0.37) would clear clause 2 instead", "3.6.3"),
  note="0.5: output per worker rising, TFP declining on growth accounting; held from 0.0 by D28(f)")

U("CN", C36, 1.0,
  [("C", f"cleared: {lp_str('CN')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: {tfp_str('CN')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: mean consumption {r3_str('CN')} the Societal Poverty Line (reading 3.6.2)", SRC363)],
  flag=("0.5: PWT's TFP rests on China's official national accounts, which alternative series (Wu's, used by the "
        "Conference Board's Total Economy Database, cited, not cached) revise down, putting TFP growth near or below "
        "zero after 2008", "3.6.1"),
  note="1.0: on the named source, productivity and TFP rising fast; the official accounts' reliability flagged")

U("SG", C36, 1.0,
  [("C", f"cleared: {lp_str('SG')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: {tfp_str('SG')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: no survey in the Platform; output per person {SG_OUT:.0f} dollars a day (2021 PPP, 2023) at "
         f"{AVH['SGP']:.0f} hours a year, at least {SG_BOUND:.2f} times the highest Societal Poverty Line its median "
         "could set (reading 3.6.2)", SRC363)],
  note="1.0: productivity and TFP rising over 2003-2023")

U("QA", C36, 0.5,
  [("S", f"short: {lp_str('QA')} % a year, PWT's hours for Qatar beginning in 2005 (reading 3.6.1)", SRC36),
   ("S", f"short: {tfp_str('QA')} % a year (reading 3.6.1)", SRC36),
   ("C", f"cleared: mean income {r3_str('QA')} the Societal Poverty Line (reading 3.6.2)", SRC363)],
  flag=("0.0: the band's case (output per hour and TFP both declining over 20 years, as employment grew "
        "fivefold), held at 0.5 only by D28(f) because the basket is provisioned", "3.6.3"),
  note="0.5: productivity and TFP declining; the basket provisioned by rent")


# =================================================================================================================
# C4.6 Harm Internalization
# =================================================================================================================
MORT = {}
for r in rows(MORS):
    MORT[(r["ref_area"], int(r["year"]))] = MORT.get((r["ref_area"], int(r["year"])), 0.0) + float(r["deaths_per_million"]) / 10
POISON = {(r["iso"], int(r["year"])): float(r["rate_per_100000"]) for r in rows(POIS)}
SUM46 = {iso: (MORT[(iso, 1999)] + POISON[(iso, 2000)], MORT[(iso, 2019)] + POISON[(iso, 2019)])
         for iso in sum(ISO.values(), ())}
WJP25 = {r["code"]: float(r["sf62"]) for r in rows(WJP) if r["edition"] == "2025"}


def m_str(code):
    return ", ".join(f"{iso} {SUM46[iso][0]:.1f} to {SUM46[iso][1]:.1f}" for iso in ISO[code])


def w_str(code):
    return ", ".join(f"{iso} {WJP25[iso]:.2f}" for iso in ISO[code])


SRC461 = f"OECD, GBD 2019 risk-attributable deaths ({MORS}); WHO GHO SDGPOISON ({POIS})"
SRC463 = f"World Justice Project, sub-factor 6.2, 2025 edition ({WJP})"
FIG_PRINT.update({
    "Pollution mortality per 100,000 (crude; air, WASH, poisoning), 1999 to 2019": "; ".join(
        f"{iso} {a:.1f} to {b:.1f}" for iso, (a, b) in SUM46.items()),
    "WJP sub-factor 6.2, 2025": "; ".join(f"{iso} {WJP25[iso]:.2f}" for iso in sum(ISO.values(), ())),
})

U("SQ", C46, 0.5,
  [("C", f"cleared: {m_str('SQ')} per 100,000 (reading 4.6.1)", SRC461),
   ("S", "short: liability for releases is strict under CERCLA ('notwithstanding any other provision or rule of law') "
         "and claims run before courts Freedom House scores 3 of 4 on F1, but the PREP Act makes a covered person "
         "'immune from suit and liability under Federal and State law' for loss from a declared countermeasure, the "
         "only remedy being a fund of 'emergency appropriations' that is 'exclusive of any other civil action': a "
         "class of harm compensated from public funds alone (reading 4.6.2)", f"{US46}; {FHP}"),
   ("C", f"cleared: {w_str('SQ')}, above 0.77 (reading 4.6.3)", SRC463)],
  note="0.5: mortality falling and regulation clean; the PREP Act's immunity puts a class of harm on public funds")

U("NSD", C46, 0.5,
  [("C", f"cleared in each of the four: {m_str('NSD')} per 100,000 (reading 4.6.1)", SRC461),
   ("U", "not shown: the law in force makes polluters liable -- Denmark's Environmental Damage Compensation Act ('shall "
         "compensate the damage the pollution causes', section 3, save damage due to compliance with an authority's "
         "mandatory rules, a defence the clause may read as an immunity), Sweden's Environmental Code (chapter 32), Finland's "
         "Environmental Damage Compensation Act (liability 'even when the damage was not caused intentionally or "
         "negligently', section 7); Norway's act was not reached -- before courts Freedom House scores 4 of 4, but no "
         "claim decided against those who caused the harm and paid within the window is named in the cache for any "
         "of the four (reading 4.6.2)", f"{NOR46}; {FHP}; {N46}"),
   ("C", f"cleared in each of the four: {w_str('NSD')}, above 0.77 (reading 4.6.3)", SRC463)],
  flag=("1.0: if the record of each of the four holds a claim decided against a polluter and paid in 2005-2025, which "
        "the cached sources do not name; strict liability and independent courts are in place", "4.6.2"),
  note="0.5: mortality falling, regulation clean, strict liability in force; no claim record named")

U("CPS", C46, 0.0,
  [("U", "not shown: the GBD's series begin in 1990, after the configuration's years (reading 4.6.1)", SRC461),
   ("U", "not shown: no Soviet liability law or record of claims is in the cache; the state that owned the polluting "
         "enterprises 'was most often the agent of this pollution' (reading 4.6.2)", SU46),
   ("U", "not shown: the Index does not cover the Soviet Union (reading 4.6.3)", SRC463)],
  zero=("no structural mechanism made harm a cost to whoever caused it: the state owned the polluting enterprises and "
        "there was no 'established regulatory agency' until the State Committee for the Protection of Nature in "
        "1988, enforcement of the 1970s laws 'largely ignored' (reading 4.6.4)"),
  flag=("0.5: reading the 1970s environmental laws and the 1980 air-protection norms as a mechanism the system "
        "provided, unenforced rather than absent", "4.6.4"),
  note="0.0: the polluter and the regulator one state, with no agency until 1988")

U("CN", C46, 0.5,
  [("C", f"cleared: {m_str('CN')} per 100,000 (reading 4.6.1)", SRC461),
   ("S", "short: the Civil Code makes those who cause damage by pollution liable (article 1229) and lets organs of the "
         "state and organisations named by law claim restoration and compensation (articles 1234, 1235), but Freedom "
         f"House scores the judiciary's independence {f1('CHN')} of 4 (F1), so the claims run before no independent "
         "court (reading 4.6.2)", f"{CN46}; {FHP}"),
   ("S", f"short: {w_str('CN')}, below 0.77 (reading 4.6.3)", SRC463)],
  note="0.5: mortality falling; liability without an independent court; regulation below the bar")

U("SG", C46, 0.5,
  [("C", f"cleared: {m_str('SG')} per 100,000 (reading 4.6.1)", SRC461),
   ("S", f"short: Freedom House scores the judiciary's independence {f1('SGP')} of 4 (F1); no liability statute or "
         "claim record was read (reading 4.6.2)", f"{FHP}; {N46}"),
   ("C", f"cleared: {w_str('SG')}, above 0.77 (reading 4.6.3)", SRC463)],
  note="0.5: mortality falling and regulation clean; no independent court on Freedom House's reading")

U("QA", C46, 0.5,
  [("C", f"cleared: {m_str('QA')} per 100,000 (reading 4.6.1)", SRC461),
   ("S", f"short: Freedom House scores the judiciary's independence {f1('QAT')} of 4 (F1); the law in force was not "
         "reached (reading 4.6.2)", f"{FHP}; {N46}"),
   ("S", f"short: {w_str('QA')}, below 0.77 (reading 4.6.3)", SRC463)],
  note="0.5: mortality falling; no independent court; regulation below the bar")


# ---- after the comparison (written after the checkpoint, 3cdf73d) ------------------------------------------------
# The prior is part (2.11)'s (rescoring_s65.NEW_UNITS): Freedom House's 1-7 rating for C2.6's clause 1, the law-in-force
# clauses and C4.6's mortality clause not shown, C3.6 on PWT 10.01's 1999-2019 with clause 3 not assessed. Four
# verdicts differ, all on C3.6; under Session 71's rule (NEEC_BlindReview_s71.md, section 6) a blind reading stands
# unless the prior shows evidence it did not weigh. Every difference below states why it stands.
STAND = {
    ("SQ", C26): "clauses 2 and 3 read from the law in force (42 CFR 482.13, Cruzan; the Virginia school-entry "
                 "requirement), which the prior did not name",
    ("NSD", C26): "clauses 2 and 3 read from the four economies' statutes, which the prior did not name; the prior's flag "
                  "toward 1.0 falls with clause 3 short in Sweden and Finland",
    ("CPS", C26): "clauses 2 and 3 short on the Fundamentals of Health Legislation (1969), which the prior did not name; "
                  "clause 1 short on both readings (the prior on the Report's findings, the blind on Freedom House's "
                  "Soviet ratings)",
    ("CN", C26): "clauses 2 and 3 short on the Mental Health Law and the Infectious Diseases Law (2025), which the prior "
                 "did not name",
    ("SG", C26): "clause 3 short on the Infectious Diseases Act's sections 15, 21K and 47, which the prior did not name",
    ("QA", C26): "clause 3 short on Freedom House's F1 (1 of 4), which the prior did not read; the law in force not "
                 "reached on either reading",
    ("SQ", C36): "verdict 0.5 to 1.0: clause 3, which the prior did not assess, cleared on the Poverty and Inequality "
                 "Platform; clauses 1 and 2 cleared on both readings (PWT 10.01 and 11.0)",
    ("NSD", C36): "clause 3, which the prior did not assess, cleared; clause 2 short on both readings (the prior in "
                  "Norway on PWT 10.01, the blind in Finland and Norway on PWT 11.0)",
    ("CPS", C36): "verdict 0.0 to 0.5: the prior's clause 1 ('output per hour growth slowed to a halt', from the paper "
                  "uncached) reads a slowing as a decline; Easterly and Fischer's table 1 gives output per worker "
                  "rising 2.1% and 1.4% a year in 1970-87, so clause 1 is cleared and D28(f) bars 0.0; the prior's "
                  "0.0 reason (TFP declining) is the blind reading's flag toward 0.0",
    ("CN", C36): "verdict 0.5 to 1.0: clause 3, which the prior did not assess, cleared; clauses 1 and 2 cleared on "
                 "both readings",
    ("SG", C36): "verdict 0.5 to 1.0: clause 3, which the prior did not assess, cleared; clause 2's difference is the "
                 "edition, not the reading -- PWT 10.01 gave Singapore's TFP -0.36% a year in 1999-2019, PWT 11.0 "
                 "revises the same years to +0.38% and gives +0.36% for 2003-2023, the window to the edition's last "
                 "year that the criterion's indicator names; the prior's figure is carried as a flag",
    ("QA", C36): "clause 1 short on PWT 11.0's hours (from 2005), which PWT 10.01 lacked; clause 3, which the prior did "
                 "not assess, cleared; the verdict (0.5, flagged toward 0.0) is the same",
    ("SQ", C46): "clause 1 cleared on the GBD's rates (OECD), which the prior could not reach; clause 2 short on the "
                 "PREP Act's immunity, which the prior did not weigh (its Deepwater Horizon record answers the claims "
                 "condition, not the immunity condition)",
    ("NSD", C46): "clause 1 cleared on the GBD's rates, which the prior could not reach",
    ("CPS", C46): "clauses 1 to 3 not shown where the prior had short on the Report's findings (the Aral Sea, "
                  "Chernobyl, the state as polluter and regulator): those findings are the blind reading's 0.0 reason, "
                  "not the clauses' measures (a 20-year mortality rate; the WJP's index, which does not cover the "
                  "Soviet Union); the verdict, 0.0, is the same",
    ("CN", C46): "clause 1 cleared on the GBD's rates; clause 2 short on Freedom House's F1, which the prior did not read",
    ("SG", C46): "clause 1 cleared on the GBD's rates; clause 2 short on Freedom House's F1, which the prior did not read",
    ("QA", C46): "clause 1 cleared on the GBD's rates; clause 2 short on Freedom House's F1, which the prior did not read",
}
# A standing verdict difference whose blind reading carried no flag toward the prior's verdict gets one here.
FLAGS = {
    ("SQ", C36): (f"0.5: reading clause 3 as the basket reaching the whole population rather than output sufficient to "
                  f"provision it: {float(PIPR['USA']['spr']) * 100:.1f}% of the population lived below the Societal "
                  f"Poverty Line in {PIPR['USA']['reporting_year']}, C1.1's measure (the record, section 6)", "3.6.2"),
    ("SG", C36): ("0.5: on PWT 10.01's 1999-2019 Singapore's TFP fell 0.36% a year (the prior's figure), which PWT "
                  "11.0 revises to +0.38%", "3.6.1"),
}


def final_units(units):
    out = {k: dict(v) for k, v in units.items()}
    for k, fl in FLAGS.items():
        out[k]["flag"] = fl
    return out


FINAL = final_units(NEW)


def prior_units():
    """Part (2.11)'s readings of the 18 units (rescoring_s65.NEW_UNITS: the three class N criteria are not in the
    pass's merged units)."""
    with redirect_stdout(io.StringIO()):
        import rescoring_s65 as r65
    return {k: r65.NEW_UNITS[k] for k in NEW}


def comparison_table(p, prior, units, cid):
    pk = {k: v for k, v in prior.items() if k[1] == cid}
    uk = {k: v for k, v in units.items() if k[1] == cid}
    res, tally = br.compare_group(pk, uk)
    rows_ = ["| Unit | Prior | Blind (Session 77) | Result | Differences |", "|---|---|---|---|---|"]
    for (code, c) in sorted(res, key=lambda k: ECON.index(k[0])):
        agree, diffs = res[(code, c)]
        pr, nw = pk[(code, c)], uk[(code, c)]
        ps = " ".join(st for st, _, _ in pr["clauses"]) + " / " + pc.f1(pr["verdict"])
        ns = " ".join(st for st, _, _ in nw["clauses"]) + " / " + pc.f1(nw["verdict"])
        kind = "agree" if agree else ("revise (verdict)" if pr["verdict"] != nw["verdict"] else "revise (clauses)")
        rows_.append(f"| {p.names[code]} | {ps} | {ns} | {kind} | {'; '.join(diffs) if diffs else '—'} |")
    return "\n".join(rows_), res, tally


def earlier_changes(p):
    """Sessions 71's to 76's final verdict changes (blind_s76.earlier_changes() with blind_s76.FINAL, which changes
    none) against their priors."""
    import blind_s76 as b76
    with redirect_stdout(io.StringIO()):
        out = b76.earlier_changes(p)
    pr = b76.prior_units()
    out.update({k: (pr[k]["verdict"], u["verdict"]) for k, u in b76.FINAL.items() if pr[k]["verdict"] != u["verdict"]})
    return out


def standings(changes):
    import blind_s75 as b75
    return b75.standings(changes)


def my_changes(prior, units):
    return {k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items() if prior[k]["verdict"] != u["verdict"]}


def consequence_table(p, prior, units):
    """This group's verdict changes, alone and on top of Sessions 71's to 76's final ones, on the 29."""
    mine = my_changes(prior, units)
    v2, base = standings({})
    _, alone = standings(mine)
    _, both = standings({**earlier_changes(p), **mine})
    held = all(v2[k[0]]["vector"][k[1]] == prior[k]["verdict"] for k in prior)
    lines = ["| Entry | Total on 29 | After this group | After Sessions 71 to 77 | Failures | After all seven | "
             "Tier after all seven |", "|---|---:|---:|---:|---:|---:|---|"]
    for code in v2:
        if alone[code] != base[code] or both[code] != base[code]:
            lines.append(f"| {v2[code]['display_name']} | {base[code][0]:.1f} | {alone[code][0]:.1f} | "
                         f"{both[code][0]:.1f} | {base[code][1]} | {both[code][1]} | {pc.tier(both[code][1])} |")

    def first(st):
        top = max(t for t, _, _ in st.values())
        return " and ".join(sorted(v2[c]["display_name"] for c, (t, _, _) in st.items() if t == top)), top
    tiers = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in both.items() if pc.tier(f) != tr]
    tiers_alone = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in alone.items() if pc.tier(f) != tr]
    return "\n".join(lines), held, first(alone), first(both), tiers, tiers_alone, mine, both


def flag_effects(p, units, both):
    """Each flag's alternative taken alone, on top of all seven groups' final verdicts."""
    lines = ["| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |",
             "|---|---|---:|---:|---:|---:|---|---|"]
    movers = []
    for (code, cid) in sorted((k for k in units if units[k]["flag"]), key=lambda k: (k[1], ECON.index(k[0]))):
        u = units[(code, cid)]
        alt = float(u["flag"][0][:3])
        t, f, _ = both[code]
        t2, f2_ = t + alt - u["verdict"], f + (alt == 0.0) - (u["verdict"] == 0.0)
        others = max(tt for c, (tt, _, _) in both.items() if c != code)
        ch = []
        if pc.tier(f2_) != pc.tier(f):
            ch.append(f"tier: {pc.tier(f)} to {pc.tier(f2_)}")
        if (t >= others) != (t2 >= others) or (t == others) != (t2 == others):
            ch.append("first place: " + ("shared" if t2 == others else "alone" if t2 > others else "lost"))
        if ch:
            movers.append((code, cid))
        lines.append(f"| {p.names[code]} | {cid} | {pc.f1(u['verdict'])} | {alt:.1f} | {t2:.1f} | {f2_} | "
                     f"{pc.tier(f2_)} | {'; '.join(ch) if ch else '—'} |")
    return "\n".join(lines), movers


def record_check(tables, ok_print):
    rec = os.path.join(HERE, "NEEC_BlindReview_s77.md")
    if not os.path.isfile(rec):
        return ok_print(False, "NEEC_BlindReview_s77.md exists", "missing")
    text = open(rec, encoding="utf-8").read()
    missing = [name for name, t in tables if t not in text]
    return ok_print(not missing, "NEEC_BlindReview_s77.md carries every generated table verbatim (" +
                    ", ".join(name for name, _ in tables) + ")", ", ".join(missing))


# ---- the files the readings read, and those blind_view lists that bear on other units -----------------------------
READ = (FHS, FHR, VDEM, FHP, US26, DK26, FI26, SE26, NO26, SU26, CN26, SG26, N26, E26 + "us_cfr_42_70.14.html",
        E26 + "us_cfr_42_71.37.html", E26 + "law_in_force_notes_s70.md", PWT, PIPF, EF, EFPDF, N36, MORS, POIS, US46,
        NOR46, CN46, SU46, N46, E46 + "notes_s70.md", E46 + "SDGAIRBOD.json", E46 + "SDGPOISON.json",
        E46 + "SDGWSHBOD.json", E46 + "air42.json", WJP)
# Listed by blind_view for these criteria but bearing on the 17 designs and mechanisms (Session 76's units), or
# superseded here (Session 65's Freedom House rating file by the score file; PWT 10.01 by PWT 11.0): not read for these
# readings.
OTHER = ([E26 + f for f in ("bien_definition_c26_extract.txt", "cco_research_hub_c26_extract.txt",
                            "george_progress_poverty_c26_extract.txt", "integral_wp_v01_c26_extract.txt",
                            "levy_jg_wp902_c26_extract.txt", "lp_platform_c26_extract.txt",
                            "ostrom_nobel_c26_extract.txt", "pe_model_c26_extract.txt", "sources_s76.md",
                            "owid_freedom_house_civil_liberties_rating.csv")] +
         [E36 + f for f in ("cco_research_hub_c36_extract.txt", "integral_wp_v01_c36_extract.txt",
                            "pe_model_c36_extract.txt", "pwt1001_selected_economies.csv", "sources_s76.md")] +
         [E46 + f for f in ("cco_research_hub_c46_extract.txt", "integral_wp_v01_c46_extract.txt",
                            "lp_platform_c46_extract.txt", "pe_model_c46_extract.txt", "wef_metrics_c46_extract.txt",
                            "sources_s76.md")])


# ---- the blind record ----------------------------------------------------------------------------------------------
def blind_table(p, cid, units):
    rows_ = ["| Unit | Clause statuses | Verdict | Flag |", "|---|---|---|---|"]
    for (code, c) in sorted((k for k in units if k[1] == cid), key=lambda k: ECON.index(k[0])):
        r = units[(code, c)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        rows_.append(f"| {p.names[code]} | {sts} | {pc.f1(r['verdict'])}"
                     f"{' (0.0 reason stated)' if r['zero'] else ''} | {flag} |")
    return "\n".join(rows_)


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s77.py -- the blind re-read of C2.6, C3.6 and C4.6 for the six configured economies (ledger S60)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    print("inputs: blind_review.py, pass_common.py and its parts, neec_corpus_v2_s65_snapshot.json, " + ", ".join(sorted(READ)) + "\n")

    print("[1] the readings are complete and follow the rules")
    corpus = {e["code"]: e["scope_class"] for e in json.load(open(path("neec_corpus_v2_s65_snapshot.json"), encoding="utf-8"))["entries"]}
    ok_print({c for c, s in corpus.items() if s == "configured_national_economy"} == set(ECON),
             "the six are the corpus's configured national economies")
    want = {(c, cid) for c in ECON for cid in (C26, C36, C46)}
    ok_print(set(NEW) == want and len(want) == 18, "one blind reading for each of the 18 units (six economies, three "
             "criteria), no more", str(sorted(set(NEW) ^ want)))
    pc.check_records(p, NEW, ok_print)
    pc.check_rule(NEW, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in NEW.values()), "each flag names an alternative score other than the verdict")
    bad = [k for k in sorted(NEW) if len(br.blind_view(p, k)["clauses_v2"]) != len(NEW[k]["clauses"])]
    ok_print(not bad, "each reading has one status per clause blind_view shows", str(bad))
    for cid, ec in ((C26, E26), (C36, E36), (C46, E46)):
        listed = {ec + f for f in br.blind_view(p, ("SQ", cid))["cache_files"]}
        ok_print(listed <= set(READ) | set(OTHER), f"every file blind_view lists for {cid} is one this script reads "
                 "or names", str(sorted(listed - set(READ) - set(OTHER))))
    ok_print(all(os.path.isfile(path(f)) for f in READ + tuple(OTHER)), "every file in READ and OTHER exists")
    ok_print(all(st != "R" for u in NEW.values() for st, _, _ in u["clauses"]),
             "no configured economy's clause is out of reach (reach is a mechanism's rule, protocol 3.2)")

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG_PRINT.items():
        print(f"    {k}: {v}")
    ok_print(all(cl(i) >= 53 for i in ISO["NSD"]) and all(cl(i) < 53 for c in ("SQ", "CN", "SG", "QA") for i in ISO[c])
             and cl("CHN") <= 16 and all(FH_SU[y] >= 6 for y in range(1972, 1988) if y in FH_SU),
             "C2.6 clause 1 as read: the Nordic four at 53 or more, the others below, China and the Soviet years to "
             "1987 in the 0.0 band")
    ok_print([i for i in TFP if TFP[i] < 0] == ["FIN", "NOR", "QAT"] and LPW["QAT"][1] < 0 and
             all(v >= 0 for i, (_, v) in LPW.items() if i != "QAT") and EF_TFP[1] < 0 and EF_TFP[2] < 0 and
             min(EF_LP) > 0, "C3.6 as read: TFP declining in Finland, Norway and Qatar only, output per hour declining "
             "only in Qatar; Soviet TFP declining and output per worker rising, 1970-87")
    ok_print(all(b <= a for a, b in SUM46.values()) and all(ratio(i) > 1 for i in PIPR) and SG_BOUND > 1,
             "C4.6 clause 1 and C3.6 clause 3 as read: pollution mortality lower in 2019 than in 1999 in each of the "
             "eight, and every economy's mean above its Societal Poverty Line")
    ok_print({i for i, v in WJP25.items() if i in sum(ISO.values(), ()) and round(v, 2) < 0.77} == {"CHN", "QAT"},
             "C4.6 clause 3 as read: China and Qatar below 0.77, the other six above")

    print("\n[3] the readings (verdicts, clause statuses, flags)")
    btables = []
    for cid in (C26, C36, C46):
        print(f"\n{cid} (blind reading):")
        t = blind_table(p, cid, NEW)
        btables.append(t)
        print(t)
        v = [r["verdict"] for k, r in NEW.items() if k[1] == cid]
        print(f"\n{cid}: {v.count(1.0)} at 1.0, {v.count(0.5)} at 0.5, {v.count(0.0)} at 0.0; "
              f"{sum(1 for k, r in NEW.items() if k[1] == cid and r['flag'])} flagged")

    print("\n[4] the comparison with part (2.11)'s readings (compare_group on the readings as recorded at the "
          "checkpoint, 3cdf73d)")
    prior = prior_units()
    ok_print(set(prior) == set(NEW), "part (2.11) holds a reading of each of the 18 units")
    cmp_tables, revised, vd = [], [], []
    for cid in (C26, C36, C46):
        t_cmp, res, tally = comparison_table(p, prior, NEW, cid)
        cmp_tables.append(t_cmp)
        print(f"\n{cid}:")
        print(t_cmp)
        revised += [k for k in res if not res[k][0]]
        d = [k for k in res if prior[k]["verdict"] != NEW[k]["verdict"]]
        vd += d
        print(f"\n{cid}: {tally['agree']} agree, {tally['revise']} revise; {len(d)} verdicts differ")
    ok_print(set(STAND) == set(revised), "every revision has its stated reason for standing (Session 71's rule)",
             str(sorted(set(STAND) ^ set(revised))))
    ok_print(sorted(vd) == sorted([("SQ", C36), ("CPS", C36), ("CN", C36), ("SG", C36)]),
             "four verdicts differ, all on C3.6: Status Quo, China and Singapore 0.5 to 1.0, Centrally Planned "
             "Socialism 0.0 to 0.5", str(vd))
    ok_print(all(NEW[k]["flag"] and NEW[k]["flag"][0][:3] == pc.f1(prior[k]["verdict"]) or k in FLAGS for k in vd),
             "each standing verdict difference carries a flag toward the prior's verdict, from the blind reading or "
             "added (FLAGS)")

    print("\n[5] the final readings (FINAL: the blind readings, with FLAGS added)")
    ok_print(all(FINAL[k]["verdict"] == NEW[k]["verdict"] and FINAL[k]["clauses"] == NEW[k]["clauses"] for k in NEW),
             "FINAL keeps every blind verdict and clause status as recorded at the checkpoint")
    pc.check_records(p, FINAL, ok_print)
    pc.check_rule(FINAL, ok_print)
    ok_print(not any(k[0] == "CCO" for k in FINAL), "the group holds no CCO-PTF-CIP-SZH unit (decisions 57.2, 69.4)")

    print("\n[6] consequences once applied (by generator in ledger S61, not here), with Sessions 71 to 76")
    t_cons, held, (fa, ta), (fb, tb), tiers, tiers_alone, mine, both = consequence_table(p, prior, FINAL)
    ok_print(held, "neec_corpus_v2_s65_snapshot.json carries the prior's verdict for each of the 18 units (the published "
             "provisional scores are the prior's)")
    print(t_cons)
    print(f"\nfirst place on the 29, this group alone: {fa} at {ta:.1f}; after Sessions 71 to 77: {fb} at {tb:.1f}")
    print("tier changes, this group alone: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers_alone) or "none"))
    print("tier changes after Sessions 71 to 77: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers) or "none"))
    t_flags, movers = flag_effects(p, FINAL, both)
    print(f"\nthe final readings' {sum(1 for u in FINAL.values() if u['flag'])} flags, each taken alone (on all seven "
          "groups' final verdicts):")
    print(t_flags)
    print("flags that would change a tier or first place: " + (", ".join(f"{p.names[c]} {cid}" for c, cid in movers)
                                                                or "none"))

    print("\n[7] the record")
    names = (C26, C36, C46)
    record_check([(f"readings, {n}", t) for n, t in zip(names, btables)] +
                 [(f"comparison, {n}", t) for n, t in zip(names, cmp_tables)] +
                 [("consequences", t_cons), ("flag effects", t_flags)], ok_print)
    print("\nBLIND RE-READ OF C2.6, C3.6 AND C4.6 (SIX CONFIGURED ECONOMIES) CHECKED." if ok
          else "\nBLIND RE-READ: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
