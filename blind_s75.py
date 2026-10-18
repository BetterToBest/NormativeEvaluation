#!/usr/bin/env python3
"""
blind_s75.py -- NEEC stage 3b, the blind re-read: C2.1, C2.4, C2.3 (configured economies) and C2.5 (ledger S58)
====================================================================================================================
Session 75, on Opus 5.5 (decisions 69.1, 69.2; ledger D52, D53, D54). Two kinds of reading, kept apart:

  FIRST  C2.1 Freedom from Coercion, C2.4 Democratic Participation and C2.3 Creative Development Opportunities, for the
         six configured economies (Status Quo, Nordic Social Democracy, Centrally Planned Socialism, China, Singapore,
         Qatar): 18 units. Decision 65.2 held these criteria at their published scores without measuring clause 1, so
         clause 1 is read here for the first time (blind_review.py's docstring): an ordinary reading, not a
         comparison with a Sonnet reading. Every clause is read, so that the verdict follows from the reading; any
         verdict the readings move is recorded for the generator session (ledger S61).
  NEW    C2.5 Exit Rights and Mobility, all 23 units, on v2.0's three clauses ("Exit feasible within 3 months without
         material penalty", "no differential treatment", "geographic mobility maintained"): the 13 units part (2.11)
         read (Session 65) and the 10 part (b5) read on the pre-v2.0 four-clause list (Session 42; ledger D54).

THE BLIND STEP. The readings below were written from blind_review.blind_view() -- the v2.0 clause text and the
evidence_cache/C2.1/, C2.3/, C2.4/ and C2.5/ file names -- from the criteria's measurement text in criteria.json, and
from the sources this session cached (evidence_cache_s75.py) or names (evidence_cache/<criterion>/sources_s75.md),
and committed to the branch as a checkpoint before part (2.11)'s, part (b5)'s or part (a)'s readings of these units,
Sessions 65's or 42's records, or the units' published scores and rationales on these criteria were opened, except as
the record discloses (NEEC_BlindReview_s75.md, section 2).

READINGS, C2.1 (configured economies; the record states them in full)
  2.1.1 clause 1, >=70% genuine autonomy: the Gallup World Poll's share satisfied with their freedom to choose what
        they do with their life (the measurement text's measure), at the latest year (2025); a configuration of
        several economies clears only if each does; not shown where the poll holds no reading near the stated date.
  2.1.2 clause 2, revealed preference (a method clause, protocol 2.3(d)): cleared only where a named study or record
        shows acceptance of initially refused employment or living situations when an alternative exists; none is
        found for any of the six, so not shown throughout.
  2.1.3 0.0 (protocol 2.1; the 0.0 band's case): a configuration whose own law substitutes state compulsion of
        comparable severity for survival compulsion -- non-work a crime, labour or residence administratively
        directed; never with a clause cleared (D28(f)).

READINGS, C2.4
  2.4.1 clause 1, >=70% participation: turnout as a share of the voting-age population (IDEA) at the latest election of
        the body that takes the binding national decisions (the parliament; in the United States the 2024 federal
        election); the voting-age population counts residents who are not citizens (protocol 3.2). Where no such
        election is held, participation in the processes that take the binding decisions.
  2.4.2 clause 2, >=35% of citizen proposals adopted: the share of citizen-initiated proposals reaching a binding
        decision that are adopted; where no national process exists, not met (the measurement text), so short.
  2.4.3 clause 3, >=65% responsiveness: the OECD Trust Survey's external-efficacy item; not shown where the survey does
        not cover the economy (the European Social Survey fallback reaches none of the four outside Europe).
  2.4.4 0.0 (protocol 2.1; the 0.0 band's case): no meaningful participation mechanism by design or suppression -- a
        constitutionally entrenched single party with no competitive national election, or no elected national body;
        never with a clause cleared.

READINGS, C2.3
  2.3.1 clause 1, >=50% weekly creative engagement: a survey recording weekly frequency of the clause's activities;
        not shown where the only such survey covers part of them (EU-SILC's artistic practice omits study and
        invention, so its share is a lower bound) or none is found.
  2.3.2 clause 2, 10+ hours a week: leisure minutes a day in the OECD Time Use Database, times seven; not shown where
        the economy has no survey in it.
  2.3.3 clause 3, >=70/100 meaning: EU-SILC's "meaning of life" rating (the "worthwhile" item) times ten; not shown
        where neither EU-SILC nor the ONS fields it.
  2.3.4 0.0 (protocol 2.1; the 0.0 band's case): structural suppression of creative activity through state control of
        cultural production, where the system's own doctrine makes independent cultural production illegitimate;
        never with a clause cleared.

READINGS, C2.5
  2.5.1 clause 1, exit within three months without material penalty: what leaving the system's own arrangements costs
        under its own rules. A configured economy: emigration and withdrawal from its compulsory institutions (an exit
        permit, an exit tax on ordinary residents, a forfeited accrued entitlement). A design: its sources' terms of
        leaving (a membership, a stake, a sector). A mechanism, generalised: leaving its own arrangements (a
        membership, a contract, a scheme); and, where it supplies an unconditional means of subsistence, the capacity
        it gives to leave other arrangements (the measurement's third item). Short where the rules impose a permit, a
        prohibition or the forfeit of a material accrued stake; not shown where the sources are silent; out of reach
        (D28(c)) for a mechanism with no arrangement to leave and no means of subsistence (a tax, a fund).
  2.5.2 clause 2, no differential treatment: whether the system's own rules penalise non-participation -- benefits
        conditioned on work, criminal or administrative sanctions, lesser rights or waiting periods for those within
        its population who stay outside its institutions. Not receiving a voluntary scheme's benefits is not a penalty.
  2.5.3 clause 3, geographic mobility maintained: relocating within the economy, or between a network's nodes, without
        losing an essential benefit; short where the rules tie an essential benefit to a locality or registration;
        out of reach for a mechanism that governs no benefit a move could lose.
  2.5.4 0.0 (protocol 2.1): the system excludes exit as illegitimate (emigration prohibited or criminalised, non-
        participation a crime), or its own sources show its coherence requires near-universal participation; a design
        silent on exit whose coherence does not depend on participation is 0.5 (silence is not clearance, and no 0.0
        condition holds); never with a clause cleared.
  2.5.5 the anchors' band texts describe v1.4's readings and do not govern (protocol 2.3(g)).

THE COMPARISON (written after the checkpoint, 6fbcfed). compare_group() sets each reading against the one the pass
holds -- part (2.11)'s or part (b5)'s for C2.5, part (2.11)'s or part (a)'s for the first readings, whose clause 1 was
held unmeasured. The record then reconciles each verdict difference (protocol 5.3, under Session 71's rule: a new verdict
stands unless the prior shows evidence the reading did not weigh, or the reading departs from its own stated reading).
Three move to the prior's (RECONCILE: China's and Qatar's C2.1, MMT + Job Guarantee's C2.5), six stand, each flagged
toward the prior's verdict; one C2.5 clause is corrected on Session 71's record (CLAUSE_FIX). FINAL and FIRST_FINAL are
what the generator session (ledger S61) applies: six C2.5 verdict changes, none on C2.1, C2.4 or C2.3. No
CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4).

Usage: python3 blind_s75.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, blind_s71.py to blind_s74.py, the
                               evidence_cache/C2.1/, C2.3/, C2.4/ and C2.5/ files, neec_corpus_v2.json,
                               neec_scores_v2.csv and NEEC_BlindReview_s75.md; writes nothing)
Prints file names and summaries only. Deterministic.
"""
import csv
import io
import json
import os
import sys
from contextlib import redirect_stdout

import blind_review as br
import pass_common as pc

HERE = os.path.dirname(os.path.abspath(__file__))
C21, C23, C24, C25 = "C2.1", "C2.3", "C2.4", "C2.5"
E1, E3, E4, E5 = (f"evidence_cache/{c}/" for c in (C21, C23, C24, C25))
WHR = E1 + "whr_freedom_s75.json"
N1 = E1 + "sources_s75.md"
ART, TU, MOL, N3 = E3 + "eurostat_artistic_practice_s75.json", E3 + "oecd_time_use_s75.json", \
    E3 + "eurostat_meaning_of_life_s75.json", E3 + "sources_s75.md"
IDEA, TRUST, DTQ, N4 = E4 + "idea_turnout_s75.json", E4 + "oecd_trust_pe_ext_s75.json", \
    E4 + "idea_dt_qatar_2024_11_extract.txt", E4 + "sources_s75.md"
CCOX, INTX, LPX, N5 = E5 + "cco_research_hub_c25_extract.txt", E5 + "integral_wp_v01_c25_extract.txt", \
    E5 + "lp_platform_c25_extract.txt", E5 + "sources_s75.md"
# Session 70's files, listed by blind_view: read for the measures' definitions and its notes on the gaps.
OTHER = [E1 + "notes_s70.md", E1 + "whr26_statistical_appendix.pdf", E3 + "notes_s70.md", E4 + "notes_s70.md",
         E4 + "idea_voter_turnout_codebook.pdf"]
READ = (WHR, N1, ART, TU, MOL, N3, IDEA, TRUST, DTQ, N4, CCOX, INTX, LPX, N5, *OTHER)
ECON = ("SQ", "NSD", "CPS", "CN", "SG", "QA")
NORDIC = ("DNK", "FIN", "NOR", "SWE")
FIRST, NEW = {}, {}


def U(code, cid, verdict, clauses, flag=None, note="", zero=None, into=None):
    """One blind reading. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    (NEW if into is None else into)[(code, cid)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note,
                                                       zero=zero)


def F(code, cid, verdict, clauses, flag=None, note="", zero=None):
    U(code, cid, verdict, clauses, flag, note, zero, into=FIRST)


def path(name):
    return os.path.join(HERE, name)


def load(name):
    return json.load(open(path(name), encoding="utf-8"))


def f1(x):
    return f"{x:.1f}"


# ---- figures, recomputed from the cache -------------------------------------------------------------------------
FR = {iso: {int(y): v["freedom_pct"] for y, v in d.items()} for iso, d in load(WHR)["freedom"].items()}


def fr(iso):
    y = max(FR[iso])
    return y, FR[iso][y]


def fr_str(iso):
    y, v = fr(iso)
    return f"{f1(v)}% ({y})"


def pct(s):
    return float(str(s).rstrip("%").replace(",", "")) if s not in (None, "") else None


IDEA_ROWS = load(IDEA)["rows"]
ISO3 = {"United States": "USA", "China": "CHN", "Singapore": "SGP", "Qatar": "QAT", "Denmark": "DNK",
        "Finland": "FIN", "Norway": "NOR", "Sweden": "SWE"}


def latest_parl(iso):
    """The latest parliamentary election's row (the IDEA export files the United States' federal elections under
    'Parliamentary' as well as 'Presidential')."""
    rs = [r for r in IDEA_ROWS if ISO3[r["Country"]] == iso and r["Election Type"] == "Parliamentary"]
    return max(rs, key=lambda r: str(r["Year"])) if rs else None


def vap(iso):
    r = latest_parl(iso)
    return (str(r["Year"])[:4], pct(r["VAP Turnout"]), pct(r["Voter Turnout"])) if r else None


QA_ROW = latest_parl("QAT")
QA_VAP_N = int(str(QA_ROW["Voting age population"]).replace(",", ""))
QA_CITIZENS, QA_REF_TURNOUT = 380_000, 0.84         # the referendum of 5 November 2024 (DTQ; N4)
QA_SHARE_MAX = 100 * QA_REF_TURNOUT * QA_CITIZENS / QA_VAP_N   # an upper bound: every Qatari counted as an adult
PE = {(r["REF_AREA"], r["TIME_PERIOD"]): float(r["OBS_VALUE"]) for r in load(TRUST)["rows"]}
TRUST_AREAS = set(load(TRUST)["areas_in_dataflow"])
TU_R = {(r["REF_AREA"], r["MEASURE"]): float(r["OBS_VALUE"]) for r in load(TU)["rows"]}
TU_AREAS = set(load(TU)["areas_in_dataflow"])


def lei_h(iso):
    """Leisure, hours a week (minutes a day times seven, over sixty)."""
    return TU_R[(iso, "LEI")] * 7 / 60


GEO2 = {"DK": "DNK", "FI": "FIN", "NO": "NOR", "SE": "SWE"}
MEAN = {GEO2[r["geo"]]: 10 * r["value"] for r in load(MOL)["rows"] if r["life_sat"] == "MEANLIFE"}
MEAN_Y = sorted({r["time"] for r in load(MOL)["rows"] if r["life_sat"] == "MEANLIFE"})
ARTW = {GEO2[r["geo"]]: 0.0 for r in load(ART)["rows"]}
for r in load(ART)["rows"]:
    if r["time"] == "2022" and r["frequenc"] in ("DAY", "WEEK"):
        ARTW[GEO2[r["geo"]]] += r["value"]

FIG_PRINT = {
    "Gallup freedom share, latest (USA, CHN, SGP, QAT, DNK, FIN, NOR, SWE)": "; ".join(
        f"{iso} {fr_str(iso)}" for iso in ("USA", "CHN", "SGP", "QAT") + NORDIC),
    "IDEA, latest parliamentary election: year, VAP turnout %, registered turnout %": "; ".join(
        f"{iso} {vap(iso)}" for iso in ("USA", "SGP", "QAT") + NORDIC) + "; CHN no row",
    "Qatar, referendum participation as a share of the voting-age population, at most %": f1(QA_SHARE_MAX),
    "OECD external efficacy, 2023 (DNK, FIN, NOR, SWE); covered: USA, CHN, SGP, QAT": "; ".join(
        f"{iso} {PE[(iso, '2023')]}" for iso in NORDIC) + "; " + ", ".join(
        f"{iso} {iso in TRUST_AREAS}" for iso in ("USA", "CHN", "SGP", "QAT")),
    "OECD leisure, hours a week (USA, CHN, DNK, FIN, NOR, SWE); covered: SGP, QAT": "; ".join(
        f"{iso} {f1(lei_h(iso))}" for iso in ("USA", "CHN") + NORDIC) + "; " + ", ".join(
        f"{iso} {iso in TU_AREAS}" for iso in ("SGP", "QAT")),
    f"EU-SILC meaning of life x10, {'/'.join(MEAN_Y)} (DNK, FIN, NOR, SWE)": "; ".join(
        f"{iso} {f1(MEAN[iso])}" for iso in NORDIC),
    "EU-SILC 2022, practising artistic activities daily or weekly, % (DNK, FIN, NOR, SWE)": "; ".join(
        f"{iso} {f1(ARTW[iso])}" for iso in NORDIC),
}
WHRS = f"Gallup World Poll via the WHR data application ({WHR})"
NORD_FR = ", ".join(f"{iso} {fr_str(iso)}" for iso in NORDIC)
NORD_VAP = ", ".join(f"{iso} {f1(vap(iso)[1])}% ({vap(iso)[0]})" for iso in NORDIC)
NORD_PE = ", ".join(f"{iso} {PE[(iso, '2023')]}%" for iso in NORDIC)
NORD_LEI = ", ".join(f"{iso} {f1(lei_h(iso))}" for iso in NORDIC)
NORD_MEAN = ", ".join(f"{iso} {f1(MEAN[iso])}" for iso in NORDIC)
NORD_ART = ", ".join(f"{iso} {f1(ARTW[iso])}%" for iso in NORDIC)


# =================================================================================================================
# FIRST: C2.1 Freedom from Coercion, configured economies
# =================================================================================================================
REVP = ("not shown: no study or record is found that shows acceptance of initially refused employment or living "
        "situations when an unconditional alternative exists, for this configuration (reading 2.1.2)")

F("SQ", C21, 0.5,
  [("C", f"cleared: {fr_str('USA')} of Americans are satisfied with their freedom to choose what they do with their "
         f"life, the fourth year at or above 70% ({', '.join(f'{y} {f1(FR['USA'][y])}' for y in (2022, 2023, 2024))}) "
         "(reading 2.1.1)", WHRS),
   ("U", REVP, N1)],
  note="0.5: autonomy above the share threshold, with no revealed-preference evidence; survival compulsion remains "
       "(no unconditional floor; work conditions on SNAP and, from 2027, Medicaid)")

F("NSD", C21, 0.5,
  [("C", f"cleared in each of the four: {NORD_FR} (reading 2.1.1)", WHRS),
   ("U", REVP + "; Finland's 2017-2018 basic income experiment tested an unconditional payment outside the "
         "configuration's own institutions", N1)],
  note="0.5: the highest autonomy shares on record, with no revealed-preference evidence; activation conditions on "
       "assistance are the bureaucratic control the criterion names")

F("CPS", C21, 0.0,
  [("U", "not shown: the Gallup poll begins in 2005; no comparable survey of the Soviet-type economy exists "
         "(reading 2.1.1)", N1),
   ("U", REVP, N1)],
  zero="protocol 2.1 (the 0.0 band's case): the system's own law substitutes state compulsion for market compulsion -- "
       "systematic avoidance of 'socially useful work' was a crime (the 1961 RSFSR decree; Criminal Code article 209), "
       "and residence was administratively controlled through internal passports and the propiska (reading 2.1.3)",
  note="0.0: market coercion replaced by state coercion of comparable severity")

F("CN", C21, 0.5,
  [("S", f"short: {fr_str('CHN')} are satisfied with their freedom to choose, below 70% (reading 2.1.1)", WHRS),
   ("U", REVP, N1)],
  flag=("0.0: reading household registration (hukou), which ties schooling, health insurance and pensions to a place "
        "of registration, with pervasive political surveillance, as a substituted control of comparable severity "
        "(the 0.0 band)", "2.1.3"),
  note="0.5: survival compulsion eased by growth and a means-tested floor (dibao); state controls on residence and "
       "expression remain")

F("SG", C21, 0.5,
  [("C", f"cleared: {fr_str('SGP')} are satisfied with their freedom to choose (reading 2.1.1)", WHRS),
   ("U", REVP, N1)],
  note="0.5: autonomy above the share threshold, with no revealed-preference evidence; work-permit holders' "
       "residence is tied to their employer")

F("QA", C21, 0.5,
  [("U", f"not shown: the poll's latest Qatar reading is {fr_str('QAT')}, before the configuration's stated date and "
         "before the 2018 and 2020 labour reforms; no later reading is published (reading 2.1.1)", f"{WHRS}; {N1}"),
   ("U", REVP, N1)],
  flag=("0.0: reading the sponsorship (kafala) system, which still ties most residents' residence permits to an "
        "employer despite the 2018 and 2020 reforms, as economic coercion maximised by design for the migrant majority "
        "(the 0.0 band)", "2.1.3"),
  note="0.5: citizens' autonomy is high; the migrant majority's position was reformed in law in 2018-2020, with "
       "documented gaps in implementation")


# =================================================================================================================
# FIRST: C2.4 Democratic Participation, configured economies
# =================================================================================================================
NOT_OECD = ("not shown: the OECD Trust Survey does not cover this economy (2021 and 2023 rounds), and the European "
            "Social Survey's equivalent item is fielded only in Europe (reading 2.4.3)")
NOPROC = "short: no national process of citizen-initiated proposals with a right to a decision exists (reading 2.4.2)"
y_us, vap_us, reg_us = vap("USA")
y_sg, vap_sg, reg_sg = vap("SGP")

F("SQ", C24, 0.5,
  [("S", f"short: {f1(vap_us)}% of the voting-age population voted in the {y_us} federal election ({f1(reg_us)}% of "
         "registered voters) (reading 2.4.1)", IDEA),
   ("S", NOPROC + "; state-level initiatives exist in about half the states", N4),
   ("U", NOT_OECD, f"{TRUST}; {N4}")],
  note="0.5: competitive elections and state-level direct democracy, short of each threshold where measured")

F("NSD", C24, 0.5,
  [("S", f"short: voting-age turnout at the latest parliamentary election is {NORD_VAP}: Finland is below 70% "
         "(reading 2.4.1)", IDEA),
   ("S", "short: Finland's citizens' initiative had brought 64 proposals to Parliament by March 2023, of which five "
         "became law and two more in modified form (at most 11%); Sweden has no national process (reading 2.4.2)", N4),
   ("S", f"short: the OECD Trust Survey's external-efficacy share (2023) is {NORD_PE}, each below 65% "
         "(reading 2.4.3)", TRUST)],
  note="0.5: among the highest participation on record, short of all three thresholds in at least one of the four")

F("CPS", C24, 0.0,
  [("S", "short: official turnout near 99.9% in single-candidate elections to the soviets is not participation in a "
         "democratic process (reading 2.4.1)", N4),
   ("S", NOPROC, N4),
   ("U", "not shown: no survey of external efficacy exists for the Soviet-type economy (reading 2.4.3)", N4)],
  zero="protocol 2.1 (the 0.0 band's case): no meaningful participation mechanism by design -- the Party is 'the leading "
       "and guiding force' (1977 Constitution, article 6), elections are uncontested, and dissent is suppressed "
       "(reading 2.4.4)",
  note="0.0: single-party rule without competitive elections")

F("CN", C24, 0.0,
  [("S", "short: no direct national election is held (the National People's Congress is chosen indirectly; direct "
         "elections reach only county and township congresses, with Party-vetted candidates); the binding decisions "
         "are taken within the Party, whose members are under a tenth of adults (reading 2.4.1)", f"{IDEA}; {N4}"),
   ("S", NOPROC, N4),
   ("U", NOT_OECD, f"{TRUST}; {N4}")],
  zero="protocol 2.1 (the 0.0 band's case): no meaningful participation mechanism by design -- the Party's leadership is "
       "constitutionally entrenched (preamble; article 1), no national election is competitive, and organised dissent "
       "is suppressed (reading 2.4.4)",
  flag=("0.5: reading the local people's congress elections, village committee elections and the public consultation "
        "on draft laws as a genuine, if bounded, participation mechanism", "2.4.4"),
  note="0.0: a single-party state with consultative channels and no competitive national election")

F("SG", C24, 0.5,
  [("S", f"short: {f1(vap_sg)}% of the voting-age population voted in the {y_sg} general election, though "
         f"{f1(reg_sg)}% of registered citizens did: the voting-age population counts the residents who are not "
         "citizens (reading 2.4.1; protocol 3.2)", IDEA),
   ("S", NOPROC, N4),
   ("U", NOT_OECD, f"{TRUST}; {N4}")],
  note="0.5: contested elections with compulsory voting for citizens; non-citizens, about four in ten residents, have "
       "no vote")

F("QA", C24, 0.0,
  [("S", f"short: the one Shura Council election (2021) was ended by the referendum of 5 November 2024, after which the "
         f"Council is wholly appointed; the referendum's participants were at most {f1(QA_SHARE_MAX)}% of the "
         f"voting-age population ({QA_VAP_N:,}), since only citizens vote (reading 2.4.1)", f"{DTQ}; {IDEA}"),
   ("S", NOPROC, N4),
   ("U", NOT_OECD, f"{TRUST}; {N4}")],
  zero="protocol 2.1 (the 0.0 band's case): no meaningful participation mechanism by design -- since the 2024 "
       "amendments no national body is elected, political parties are not permitted, and the non-citizen majority "
       "has no political participation at all (reading 2.4.4)",
  flag=("0.5: reading the 2024 constitutional referendum itself, and the elected Central Municipal Council, as a "
        "participation mechanism for citizens", "2.4.4"),
  note="0.0: an appointed legislature since the 2024 referendum; most residents are non-citizens without a vote")


# =================================================================================================================
# FIRST: C2.3 Creative Development Opportunities, configured economies
# =================================================================================================================
NO_WEEKLY = ("not shown: no survey recording the weekly frequency of creative engagement is found for this economy "
             "(reading 2.3.1)")
NO_TU = "not shown: no national time-use survey in the OECD Time Use Database (reading 2.3.2)"
NO_MEAN = "not shown: neither EU-SILC nor the ONS fields the 'worthwhile' item here (reading 2.3.3)"

F("SQ", C23, 0.5,
  [("U", NO_WEEKLY + "; the NEA's arts participation survey records the past year, not the week", N3),
   ("C", f"cleared: {f1(lei_h('USA'))} hours a week of leisure (American Time Use Survey, OECD) (reading 2.3.2)", TU),
   ("U", NO_MEAN, N3)],
  note="0.5: ample leisure on the time-use measure; engagement and meaning unmeasured on the named series")

F("NSD", C23, 0.5,
  [("U", f"not shown: EU-SILC 2022 records {NORD_ART} practising artistic activities daily or weekly, but omits study "
         "and invention, so the clause's share is not established (reading 2.3.1)", ART),
   ("C", f"cleared in each of the four: {NORD_LEI} hours a week of leisure (reading 2.3.2)", TU),
   ("C", f"cleared in each of the four: meaning-of-life rating times ten {NORD_MEAN} (EU-SILC {MEAN_Y[-1]}, the item's "
         "one wave) (reading 2.3.3)", MOL)],
  note="0.5: two of three clauses cleared; weekly engagement not established on a survey covering the clause's "
       "activities")

F("CPS", C23, 0.0,
  [("U", "not shown: no comparable survey of the Soviet-type economy (reading 2.3.1)", N3),
   ("U", "not shown: not in the OECD Time Use Database (reading 2.3.2)", N3),
   ("U", "not shown: no 'worthwhile' item fielded (reading 2.3.3)", N3)],
  zero="protocol 2.1 (the 0.0 band's case): structural suppression through state control of cultural production -- "
       "socialist realism the obligatory method (1934 Writers' Union statute) and prior censorship (Glavlit, 1922-1991) "
       "make independent creative work illegitimate under the system's own doctrine (reading 2.3.4)",
  flag=("0.5: reading the state network of houses of culture and amateur collectives as a genuine, if ideologically "
        "bounded, mechanism of mass creative participation", "2.3.4"),
  note="0.0: creative activity organised and censored by the state")

F("CN", C23, 0.5,
  [("U", NO_WEEKLY, N3),
   ("C", f"cleared: {f1(lei_h('CHN'))} hours a week of leisure (National Bureau of Statistics' 2008 survey, OECD) "
         "(reading 2.3.2)", TU),
   ("U", NO_MEAN, N3)],
  flag=("0.0: reading state censorship of film, publishing and the internet as structural suppression through state "
        "control of cultural production (the 0.0 band)", "2.3.4"),
  note="0.5: a large creative economy under state censorship of content")

F("SG", C23, 0.5,
  [("U", NO_WEEKLY, N3), ("U", NO_TU, f"{TU}; {N3}"), ("U", NO_MEAN, N3)],
  note="0.5: a funded arts sector and long working hours; none of the three measures is published")

F("QA", C23, 0.5,
  [("U", NO_WEEKLY, N3), ("U", NO_TU, f"{TU}; {N3}"), ("U", NO_MEAN, N3)],
  note="0.5: state investment in culture for a citizen minority; the migrant majority's hours are long and unmeasured "
       "on the named series")


# =================================================================================================================
# NEW: C2.5 Exit Rights and Mobility, 23 units
# =================================================================================================================
SILENT1 = "not shown: the sources state no terms for leaving the system (reading 2.5.1)"
SILENT2 = "not shown: the sources do not say how those who stay outside its institutions are treated (reading 2.5.2)"
SILENT3 = "not shown: the sources do not address relocation or the portability of benefits (reading 2.5.3)"

# ---- configured economies ---------------------------------------------------------------------------------------
U("SQ", C25, 0.5,
  [("C", "cleared: no exit permit; the expatriation tax reaches only 'covered expatriates' (net worth of $2 million or "
         "more, or high income tax); accrued Social Security is paid abroad (reading 2.5.1)", N5),
   ("S", "short: SNAP's time limit for able-bodied adults without dependants and the 2025 Medicaid work requirement "
         "condition essential benefits on paid work (reading 2.5.2)", N5),
   ("S", "short: adult Medicaid eligibility differs between expansion and non-expansion states, so a move between them "
         "can end coverage; employer-tied health insurance locks workers to jobs (reading 2.5.3)", N5)],
  note="0.5: free emigration and interstate movement, with work conditions on benefits and state-bound health cover")

U("NSD", C25, 0.5,
  [("C", "cleared in each of the four: emigration is free; exit taxes reach unrealised share gains only and are "
         "deferred within the EEA; accrued pensions are paid abroad (reading 2.5.1)", N5),
   ("S", "short: social assistance and unemployment benefit are conditioned on availability for work in each of the "
         "four (Denmark's 2024 work obligation among them) (reading 2.5.2)", N5),
   ("C", "cleared: national benefits are portable within each economy, and EEA coordination and the Nordic Convention "
         "carry entitlements across borders (reading 2.5.3)", N5)],
  flag=("0.0: reading the tax-funded welfare state's dependence on near-universal participation as the 0.0 band "
        "describes it ('a meaningful opt-out rate would collapse it')", "2.5.4"),
  note="0.5: free exit and portable benefits, with activation conditions on assistance; residents cannot opt out of "
       "the tax base short of emigrating")

U("CPS", C25, 0.0,
  [("S", "short: emigration required an exit visa rarely granted; flight abroad was treason (RSFSR Criminal Code "
         "article 64) (reading 2.5.1)", N5),
   ("S", "short: non-participation in state employment was a crime ('parasitism', article 209) (reading 2.5.2)", N5),
   ("S", "short: residence required a propiska permit; collective farmers held no internal passport until 1974 "
         "(reading 2.5.3)", N5)],
  zero="protocol 2.1: the system excludes exit as illegitimate -- emigration and non-participation were criminal "
       "offences under its own law (reading 2.5.4)",
  note="0.0: exit, non-participation and relocation all criminalised or administratively barred")

U("CN", C25, 0.5,
  [("S", "short: exit is administratively restricted for whole populations (passports collected in Xinjiang from 2016; "
         "exit bans), though most residents may emigrate (reading 2.5.1)", N5),
   ("S", "short: residents without local household registration receive lesser access to schooling, health insurance "
         "and housing (reading 2.5.2)", N5),
   ("S", "short: hukou ties essential benefits to the place of registration, so migrants lose them on moving, though "
         "the 2014 and 2019 reforms eased registration in smaller cities (reading 2.5.3)", N5)],
  flag=("0.0: reading hukou and the regional exit controls as excluding free movement under the system's own logic",
        "2.5.4"),
  note="0.5: emigration open to most; internal mobility constrained by registration, under gradual reform")

U("SG", C25, 0.5,
  [("S", "short: national-service-liable males need exit permits and may not renounce citizenship before completing "
         "national service; otherwise CPF balances are released on renouncing and leaving (reading 2.5.1)", N5),
   ("S", "short: ComCare's assistance is conditioned on work or job search, and the CPF's housing and retirement "
         "provision rests on employment (reading 2.5.2)", N5),
   ("S", "short: the HDB's five-year Minimum Occupation Period bars selling or vacating a subsidised flat, so an early "
         "move forfeits it (reading 2.5.3)", N5)],
  note="0.5: open emigration for most, with national-service exit controls, work conditions and housing lock-in")

U("QA", C25, 0.5,
  [("S", "short: exit permits were abolished for most workers in 2018-2020, but residence remains tied to an employer "
         "sponsor and absconding charges and recruitment debt still penalise leaving (reading 2.5.1)", N5),
   ("S", "short: the non-citizen majority is excluded from the citizens' benefit system and its residence depends on "
         "employment (reading 2.5.2)", N5),
   ("S", "short: a migrant's right to stay ends with the sponsoring job unless a new sponsor is found (reading 2.5.3)",
    N5)],
  flag=("0.0: reading the residual sponsorship system as excluding free exit for the migrant majority on which the "
        "configuration depends", "2.5.4"),
  note="0.5: legal exit reforms since 2018; residence still sponsor-bound for most residents")

# ---- comprehensive systems (their own sources) -------------------------------------------------------------------
U("CCO", C25, 0.5,
  [("S", "short: Acre Equity, built from 70-80% of members' housing payments, is accessible at exit only in part -- "
         "about 10-20% in the first six months, rising to 80-90% after five years -- so an early leaver forfeits most "
         "of it (reading 2.5.1)", CCOX),
   ("C", "cleared: participation is opt-in only, the design preserves private markets and ownership, and its "
         "validation tracks non-participants' outcomes so that they are not harmed (reading 2.5.2)", CCOX),
   ("C", "cleared: members may move between Public Trust Housing properties keeping their equity status ('network "
         "portability'), and the Basic Unit allocation is made to citizens who opt in, not to a place (reading 2.5.3)",
    CCOX)],
  flag=("1.0: reading the tenure-graded haircut as the price of a tenure-building asset rather than a penalty (a renter "
        "who leaves keeps nothing), with up to 25% convertible to cash each year", "2.5.1"),
  note="0.5: opt-in and viable at 30% participation; the housing equity's exit haircut is material in the early years")

U("DE", C25, 0.5,
  [("U", SILENT1, N5), ("U", SILENT2, N5), ("U", SILENT3, N5)],
  note="0.5: a framework adopted by cities within liberal states; its coherence does not depend on universal "
       "participation, and it states no exit terms (reading 2.5.4)")

U("DG", C25, 0.5,
  [("U", SILENT1, N5),
   ("U", "not shown: caps on resource use and income bind every resident alike; the sources say nothing of treatment "
         "of those who stay outside degrowth's institutions (reading 2.5.2)", N5),
   ("U", SILENT3, N5)],
  flag=("0.0: reading society-wide ecological and income caps as a coherence that requires near-universal "
        "participation (the 0.0 band's reading)", "2.5.4"),
  note="0.5: no exit terms stated; its caps are laws binding all, not a participation one could leave")

U("FALC", C25, 0.5,
  [("U", SILENT1, N5), ("U", SILENT2, N5), ("U", SILENT3, N5)],
  note="0.5: universal provision and public ownership; no exit terms stated (reading 2.5.4)")

U("INT", C25, 0.5,
  [("C", "cleared: participation 'remains voluntary' throughout the transition and Integral coexists with market "
         "production; a leaver loses only unused time credits, which are non-transferable access signals that decay "
         "(reading 2.5.1)", INTX),
   ("U", "not shown: essentials stay accessible 'regardless of age or ability', but access is otherwise earned by "
         "contribution, and the paper does not say how non-participants fare once Integral displaces market "
         "production (reading 2.5.2)", INTX),
   ("C", "cleared: a member who relocates has their account migrated to the new node by an equivalence rule "
         "(reading 2.5.3)", INTX)],
  flag=("1.0: reading 'participation remains voluntary' and markets' coexistence as showing no differential treatment",
        "2.5.2"),
  note="0.5: voluntary, federated and portable; the treatment of non-participants after displacement is unstated")

U("LM", C25, 1.0,
  [("C", "cleared: every association is voluntary and the state imposes no exit permit or exit tax; the platform "
         "affirms the right to 'withdraw from' government (3.7) (reading 2.5.1)", LPX),
   ("C", "cleared: the minimal state runs no programme whose non-participants it could penalise (reading 2.5.2)", LPX),
   ("C", "cleared: 'individuals [are] not ... unreasonably constrained by government in the crossing of political "
         "boundaries' (3.4), and no state benefit is lost on moving (reading 2.5.3)", LPX)],
  flag=("0.5: reading the private lock-ins the system leaves in place (employment-tied insurance, housing, the lack of "
        "any floor) as material penalties on exit (the 0.5 band's description)", "2.5.1"),
  note="1.0: no system-imposed exit cost, no compulsory participation, free movement")

U("MS", C25, 0.5,
  [("C", "cleared: workers may leave a self-managed firm at once, holding no capital stake to forfeit (Schweickart); "
         "the citizen's coupon portfolio is a dividend right, not a sold stake (Roemer) (reading 2.5.1)", N5),
   ("S", "short: a private firm may operate only at small scale and passes to its workers when its owner sells or "
         "retires (Schweickart), so those who stay outside worker self-management are treated differently "
         "(reading 2.5.2)", N5),
   ("U", SILENT3, N5)],
  note="0.5: free exit from firms within a socialised economy that bars large private capital")

U("PE", C25, 0.5,
  [("S", "short: with private productive property and markets abolished, there is no arrangement to leave for "
         "within the economy (reading 2.5.1)", N5),
   ("S", "short: consumption rights follow effort and sacrifice in a balanced job complex, so those who decline to "
         "participate receive less than members (reading 2.5.2)", N5),
   ("U", SILENT3, N5)],
  flag=("0.0: reading participatory planning, which iterates on every council's proposals, as a coherence that "
        "requires near-universal participation", "2.5.4"),
  note="0.5: membership of councils is the economy; no alternative arrangement exists within it")

U("SC", C25, 0.5,
  [("U", SILENT1, N5), ("U", SILENT2, N5), ("U", SILENT3, N5)],
  note="0.5: a governance reform within market economies; no exit terms of its own (reading 2.5.4; D29(c))")

# ---- mechanisms (generalised, protocol 3.2) -------------------------------------------------------------------------
U("GEO", C25, 0.5,
  [("R", "out of reach: a land value tax is not an arrangement one enters or leaves, and the dividend is too small to "
         "fund leaving other arrangements (reading 2.5.1; D28(c))", N5),
   ("C", "cleared: the tax falls on land whoever holds it and the citizen's dividend is paid to all alike (reading "
         "2.5.2)", N5),
   ("C", "cleared: the dividend is national, and replacing transaction taxes lowers the cost of moving (reading "
         "2.5.3)", N5)],
  note="0.5: a tax and dividend that impose no participation; exit itself is the host's quantity")

U("IF", C25, 0.5,
  [("C", "cleared: either partner may end a musharaka or mudaraba by notice, and diminishing-musharaka home finance "
         "is settled by buying the remaining units (reading 2.5.1)", N5),
   ("C", "cleared: the contracts are open to all on the same terms (reading 2.5.2)", N5),
   ("R", "out of reach: financing contracts govern no benefit a move could lose (reading 2.5.3; D28(c))", N5)],
  note="0.5: exit terms are those of ordinary partnership contracts; mobility is the host's quantity")

U("MC", C25, 0.5,
  [("S", "short: balances are in a unit not convertible to national currency, so a member leaving with a credit "
         "balance forfeits it, and one in debit must settle (reading 2.5.1)", N5),
   ("C", "cleared: non-members are not penalised (reading 2.5.2)", N5),
   ("S", "short: networks are local, so a member who relocates loses the network and its balance (reading 2.5.3)", N5)],
  note="0.5: voluntary membership, with non-portable, non-convertible balances")

U("MMT", C25, 1.0,
  [("C", "cleared: the Job Guarantee is voluntary employment that may be left at any time, and its standing offer "
         "makes leaving any other job feasible without loss of income (reading 2.5.1)", N5),
   ("C", "cleared: the job offer is open to all and, in Tcherneva's design, does not replace unemployment insurance "
         "or other income support (reading 2.5.2)", N5),
   ("C", "cleared: the offer is national, funded federally and available wherever one lives (reading 2.5.3)", N5)],
  flag=("0.5: reading the buffer-stock proposals that would replace unemployment benefit for those able to work, "
        "penalising those who decline the job, as the mechanism's design (protocol 4.2)", "2.5.2"),
  note="1.0: a voluntary, universal and portable offer that adds an exit option from every other job")

U("OS", C25, 0.5,
  [("C", "cleared: members may leave a commons institution at any time, losing only the use right (reading 2.5.1)",
    N5),
   ("C", "cleared: non-members are excluded from the resource but not otherwise penalised (reading 2.5.2)", N5),
   ("S", "short: use rights are held by members of a bounded local community (design principle 1; the Törbel "
         "commons), so they are lost on relocating (reading 2.5.3)", N5)],
  note="0.5: voluntary exit; bounded, local rights that do not move with the member")

U("SWF", C25, 0.5,
  [("R", "out of reach: a state fund is not an arrangement one enters or leaves, and the dividend does not fund leaving "
         "other arrangements (reading 2.5.1; D28(c))", N5),
   ("S", "short: the dividend requires a full calendar year's residency and excludes those incarcerated on a felony "
         "conviction (Alaska Statutes 43.23.005), so new and some residents are treated differently (reading 2.5.2)",
    N5),
   ("C", "cleared: generalised to a national economy, the dividend is kept on moving within it (reading 2.5.3)", N5)],
  note="0.5: a residency-conditioned dividend; exit itself is the host's quantity")

U("UBI", C25, 1.0,
  [("C", "cleared: an unconditional individual payment makes leaving a job, household or community feasible at once "
         "without losing income -- the measurement's capacity to leave for alternative arrangements (reading 2.5.1)",
    N5),
   ("C", "cleared: paid to every member without means test or work requirement (Van Parijs and Vanderborght) "
         "(reading 2.5.2)", N5),
   ("C", "cleared: national and individual, so it moves with the recipient within the economy (reading 2.5.3)", N5)],
  flag=("0.5: reading the payment as governing no arrangement one exits (D28(c)), or the newcomer waiting periods its "
        "literature discusses as differential treatment", "2.5.1"),
  note="1.0: the paradigm exit-enabling mechanism: no participation, no condition, portable")

U("UBS", C25, 0.5,
  [("C", "cleared: guaranteed housing, food, transport and information alongside health and education keep access "
         "to essentials when leaving a job or arrangement (reading 2.5.1)", N5),
   ("C", "cleared: services are universal, allocated by need, not by participation (reading 2.5.2)", N5),
   ("U", "not shown: housing is allocated by need and administered locally, and the proposals do not say whether an "
         "allocation moves with the household (reading 2.5.3)", N5)],
  flag=("1.0: reading national entitlement to each service as portable by construction", "2.5.3"),
  note="0.5: universal in-kind provision; portability of locally allocated housing is unstated")


# ---- the blind record ----------------------------------------------------------------------------------------------
def blind_table(p, cid, units):
    rows_ = ["| Unit | Clause statuses | Verdict | Flag |", "|---|---|---|---|"]
    for (code, c) in sorted((k for k in units if k[1] == cid), key=lambda k: p.names[k[0]]):
        r = units[(code, c)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        rows_.append(f"| {p.names[code]} | {sts} | {pc.f1(r['verdict'])}{' (0.0 reason stated)' if r['zero'] else ''} "
                     f"| {flag} |")
    return "\n".join(rows_)



# ---- the reconciliation, after the comparison (protocol 5.3; written after the checkpoint, 6fbcfed) -------------
# A blind (or first) verdict stands unless the prior shows evidence the reading did not weigh, or the reading departs
# from its own stated reading (Session 71's rule, NEEC_BlindReview_s71.md, section 6). Three move to the prior's, each
# keeping the new verdict as its flag.
RECONCILE = {
    ("CN", C21): dict(
        verdict=0.0, into="FIRST",
        flag=("0.5: reading the Gallup share near the threshold (67.6%) and the eased survival compulsion as a "
              "partial reduction of coercion, as the first reading did", "2.1.3"),
        zero="protocol 2.1 (the 0.0 band's case): the configuration keeps market compulsion and adds state "
             "compulsion -- a state-mandated labour-transfer programme places Uyghur, Tibetan and other minority "
             "workers into jobs under surveillance with no real choice to refuse (UN human rights experts, January "
             "2026; Xinjiang's 2021-2025 plan projected 13.75 million transfers), and workers cannot organise outside "
             "the party-affiliated federation (reading 2.1.3)",
        note="0.0: market coercion kept and state coercion added, including state-directed labour transfers",
        reason="the prior cites the state-mandated labour-transfer programme (UN experts, January 2026; Xinjiang's "
               "plan of 13.75 million transfers) and the bar on independent unions, which the first reading did not "
               "weigh; labour directed by the state with no real choice to refuse is the substituted compulsion of "
               "reading 2.1.3, a fortiori where market compulsion is kept beside it"),
    ("QA", C21): dict(
        verdict=0.0, into="FIRST",
        flag=("0.5: reading the 2018 and 2020 reforms, which ended exit permits and the no-objection certificate in "
              "law (350,000 job changes approved in two years), as a meaningful reduction of coercion", "2.1.3"),
        zero="protocol 2.1 (the 0.0 band's case): survival compulsion is maximised by design for the non-citizen "
             "majority -- no safety net, and losing a job usually means losing the right to stay -- with absconding "
             "still criminalised and passport confiscation common (Human Rights Watch, World Report 2026; US "
             "Trafficking in Persons Report 2025) (reading 2.1.3)",
        note="0.0: for most residents, no floor and residence tied to the job; reformed in law, not in effect",
        reason="the prior shows what the first reading did not weigh: that non-citizens have no safety net at all, so "
               "that losing a job means losing both income and the right to stay, which is the 0.0 band's 'maximizes "
               "economic coercion by design' for the population the protocol counts (section 3.2); the first reading "
               "weighed the employer tie and flagged toward 0.0, and the prior's evidence settles the flag"),
    ("MMT", C25): dict(
        verdict=0.5, into="NEW",
        clause=(1, ("U", "not shown: the mechanism's own literature divides -- in Tcherneva's design the job offer "
                         "adds to unemployment insurance and other income support; in the buffer-stock proposals it "
                         "replaces unemployment benefit for those able to work, so declining it costs income "
                         "(reading 2.5.2; protocol 4.2)", N5)),
        flag=("1.0: reading Tcherneva's design, in which the job offer adds to and does not replace income support, "
              "as the mechanism", "2.5.2"),
        zero=None,
        note="0.5: a voluntary, universal and portable job offer; whether declining it costs income support is "
             "disputed within the mechanism's own literature",
        reason="the blind reading departs from its own stated reading: its flag names a dispute within the mechanism's "
               "own literature on clause 2 (Tcherneva's job offer beside income support; the buffer-stock proposals "
               "replacing unemployment benefit for those able to work), which protocol 2.1 places at 0.5, flagged "
               "('the sources are genuinely ambiguous'); the prior's point, that the guarantee offers exit from a job "
               "but not from employment, is the same dispute seen from the other side"),
}
# Clause corrections with no verdict effect, after the comparison.
CLAUSE_FIX = {
    ("PE", C25, 1): ("C", "cleared: besides the effort-rated budget, the design allows 'a consumption allowance for "
                          "people who simply don't want to work' at a level meeting basic needs (Wright's statement "
                          "of the procedure in Hahnel and Wright, 2016, kept by Hahnel; Session 71's record, section "
                          "6), so non-participants are not penalised (reading 2.5.2)",
                     "NEEC_BlindReview_s71.md, section 6; Hahnel and Wright, Alternatives to Capitalism (2016)"),
}
# Standing verdict differences whose blind reading carried no flag toward the prior's verdict get one here.
FLAGS = {
    ("CPS", C25): ("0.5: reading the formal job-assignment process as a limited, administered mobility rather than a "
                   "prohibition (the prior's reading)", "2.5.4"),
    ("FALC", C25): ("0.0: reading the automation infrastructure as requiring comprehensive participation (the prior's "
                    "reading of the 0.0 band)", "2.5.4"),
    ("MS", C25): ("0.0: reading the cooperative economy as requiring comprehensive adoption, with workers in "
                  "traditional firms outside its benefits (the prior's reading of the 0.0 band)", "2.5.4"),
    ("UBI", C25): ("0.0: reading the tax-funded payment's dependence on near-universal participation as the 0.0 band "
                   "describes it (the prior's reading)", "2.5.4"),
}
# Why each standing verdict difference stands (the record, section 6, states them in full).
STAND = {
    ("CPS", C25): "the prior's 0.5 states that international exit was 'essentially prohibited' and gives 'slight "
                  "credit for formal job assignment'; the blind reading weighed both, and a system whose own law makes "
                  "flight abroad treason and non-work a crime excludes exit as illegitimate (reading 2.5.4)",
    ("DG", C25): "the prior's 0.0 rests on the band's v1.4 reading (ecological compliance needs comprehensive "
                 "participation; a high-consumption minority would break it), which the blind reading weighed and "
                 "flagged; caps that bind every resident are laws, not a participation one could leave, and the "
                 "sources state no exit terms, so no 0.0 condition is shown (readings 2.5.4, 2.5.5)",
    ("FALC", C25): "the prior's 0.0 asserts that the automation infrastructure cannot function with partial "
                   "participation, citing no source; Bastani states no participation requirement or exit terms, so "
                   "the design is silent, which reading 2.5.4 holds at 0.5",
    ("MS", C25): "the prior's 0.0 rests on 'comprehensive adoption to function optimally' and workers in traditional "
                 "firms lacking cooperative benefits; the second is clause 2's shortfall in the blind reading, and the "
                 "first is optimality, not a structural requirement: Schweickart keeps a bounded capitalist sector",
    ("NSD", C25): "the prior's 0.0 rests on the funding model's need for near-universal participation, which the blind "
                  "reading weighed and flagged; residents leave the tax base only by emigrating, which is free and "
                  "costless under the configuration's rules, so the counterfactual opt-out is not an exit right the "
                  "system denies (readings 2.5.1, 2.5.4)",
    ("UBI", C25): "the prior's 0.0 rests on the funding model's need for universal participation; the payment's level "
                  "is set at the highest sustainable level (Van Parijs and Vanderborght), so the design adapts to "
                  "participation rather than collapsing, and the question is the payment's sustainability (domains 1 "
                  "and 5), not a penalty on exit; every clause is cleared on readings 2.5.1 to 2.5.3",
}


def final_units(units, into):
    out = {k: dict(v) for k, v in units.items()}
    for k, r in RECONCILE.items():
        if r["into"] == into:
            out[k].update(verdict=r["verdict"], flag=r["flag"], zero=r["zero"], note=r["note"])
            if r.get("clause"):
                cl = list(out[k]["clauses"])
                cl[r["clause"][0]] = r["clause"][1]
                out[k]["clauses"] = cl
    for (code, cid, i), clause in CLAUSE_FIX.items():
        if (code, cid) in out:
            cl = list(out[(code, cid)]["clauses"])
            cl[i] = clause
            out[(code, cid)]["clauses"] = cl
    for k, fl in FLAGS.items():
        if k in out:
            out[k]["flag"] = fl
    return out


FINAL = final_units(NEW, "NEW")
FIRST_FINAL = final_units(FIRST, "FIRST")


def prior_units(p):
    """The readings the pass holds for this group's units: part (2.11)'s, part (b5)'s (C2.5's ten pre-v2.0 units) and
    part (a)'s (Nordic Social Democracy's C2.1, C2.3 and C2.4)."""
    return {k: p.merged[k] for k in {**FIRST, **NEW}}


def comparison_table(p, prior, units, cid, label):
    pk = {k: v for k, v in prior.items() if k[1] == cid and k in units}
    uk = {k: v for k, v in units.items() if k[1] == cid}
    res, tally = br.compare_group(pk, uk)
    rows_ = [f"| Unit | Part | Prior | {label} | Result | Differences |", "|---|---|---|---|---|---|"]
    for (code, c) in sorted(res, key=lambda k: p.names[k[0]]):
        agree, diffs = res[(code, c)]
        pr, nw = pk[(code, c)], uk[(code, c)]
        ps = " ".join(st for st, _, _ in pr["clauses"]) + " / " + pc.f1(pr["verdict"])
        ns = " ".join(st for st, _, _ in nw["clauses"]) + " / " + pc.f1(nw["verdict"])
        kind = "agree" if agree else ("revise (verdict)" if pr["verdict"] != nw["verdict"] else "revise (clauses)")
        rows_.append(f"| {p.names[code]} | {p.part_of[(code, c)]} | {ps} | {ns} | {kind} | "
                     f"{'; '.join(diffs) if diffs else '—'} |")
    return "\n".join(rows_), res, tally


def earlier_changes(p):
    """Sessions 71's to 74's final verdict changes (blind_s71.FINAL to blind_s74.FINAL, with blind_s74.EXTRA_FINAL)
    against their priors."""
    import blind_s74 as b74
    with redirect_stdout(io.StringIO()):
        out = b74.earlier_changes(p)
    pr = b74.prior_units(p)
    out.update({k: (pr[k]["verdict"], u["verdict"]) for k, u in b74.FINAL.items() if pr[k]["verdict"] != u["verdict"]})
    xp = b74.extra_prior(p)
    out.update({k: (xp[k]["verdict"], u["verdict"]) for k, u in b74.EXTRA_FINAL.items()
                if xp[k]["verdict"] != u["verdict"]})
    return out


def standings(changes):
    """Totals on the 29 criteria (neec_scores_v2.csv) and failures, with the verdict changes in `changes`
    ({(code, cid): (prior verdict, final verdict)}) applied on top; nothing is written."""
    v2 = {e["code"]: e for e in json.load(open(path("neec_corpus_v2.json"), encoding="utf-8"))["entries"]}
    rows29 = {r["system"]: r for r in csv.DictReader(open(path("neec_scores_v2.csv"), encoding="utf-8"))}
    out = {}
    for code, e in v2.items():
        r = rows29[e["display_name"]]
        t, f = float(r["total_score"]), int(r["failures"])
        for (c, _), (pv, nv) in changes.items():
            if c == code:
                t += nv - pv
                f += (nv == 0.0) - (pv == 0.0)
        out[code] = (t, f, r["adequacy_tier"])
    return v2, out


def my_changes(prior, units):
    return {k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items() if prior[k]["verdict"] != u["verdict"]}


def consequence_table(p, prior, units):
    """This group's verdict changes, alone and on top of Sessions 71's to 74's final ones, on the 29."""
    mine = my_changes(prior, units)
    v2, alone = standings(mine)
    _, both = standings({**earlier_changes(p), **mine})
    held = all(v2[k[0]]["vector"][k[1]] == prior[k]["verdict"] for k in prior)
    base = standings({})[1]
    lines = ["| Entry | Total on 29 | After this group | After Sessions 71 to 75 | Failures | After all five | "
             "Tier after all five |", "|---|---:|---:|---:|---:|---:|---|"]
    for code in v2:
        if alone[code] != base[code] or both[code] != base[code]:
            lines.append(f"| {v2[code]['display_name']} | {base[code][0]:.1f} | {alone[code][0]:.1f} | "
                         f"{both[code][0]:.1f} | {base[code][1]} | {both[code][1]} | {pc.tier(both[code][1])} |")

    def first(st):
        top = max(t for t, _, _ in st.values())
        return " and ".join(sorted(v2[c]["display_name"] for c, (t, _, _) in st.items() if t == top)), top
    tiers = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in both.items() if pc.tier(f) != tr]
    tiers_alone = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in alone.items() if pc.tier(f) != tr]
    return "\n".join(lines), held, first(alone), first(both), tiers, tiers_alone, mine


def flag_effects(p, prior, units):
    """Each flagged final reading's alternative taken alone, on top of all five groups' final verdicts: total,
    failures, tier, and whether first place or the tier would change."""
    changes = earlier_changes(p)
    changes.update(my_changes(prior, units))
    _, base = standings(changes)
    lines = ["| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |",
             "|---|---|---:|---:|---:|---:|---|---|"]
    movers = []
    for (code, cid) in sorted((k for k in units if units[k]["flag"]), key=lambda k: (k[1], p.names[k[0]])):
        u = units[(code, cid)]
        alt = float(u["flag"][0][:3])
        t, f, _ = base[code]
        t2, f2_ = t + alt - u["verdict"], f + (alt == 0.0) - (u["verdict"] == 0.0)
        others = max(tt for c, (tt, _, _) in base.items() if c != code)
        changes_ = []
        if pc.tier(f2_) != pc.tier(f):
            changes_.append(f"tier: {pc.tier(f)} to {pc.tier(f2_)}")
        if (t >= others) != (t2 >= others) or (t == others) != (t2 == others):
            changes_.append("first place: " + ("shared" if t2 == others else "alone" if t2 > others else "lost"))
        if changes_:
            movers.append((code, cid))
        lines.append(f"| {p.names[code]} | {cid} | {pc.f1(u['verdict'])} | {alt:.1f} | {t2:.1f} | {f2_} | "
                     f"{pc.tier(f2_)} | {'; '.join(changes_) if changes_ else '—'} |")
    return "\n".join(lines), movers


def record_check(tables, ok_print):
    rec = os.path.join(HERE, "NEEC_BlindReview_s75.md")
    if not os.path.isfile(rec):
        return ok_print(False, "NEEC_BlindReview_s75.md exists", "missing")
    text = open(rec, encoding="utf-8").read()
    missing = [name for name, t in tables if t not in text]
    return ok_print(not missing, "NEEC_BlindReview_s75.md carries every generated table verbatim (" +
                    ", ".join(name for name, _ in tables) + ")", ", ".join(missing))


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s75.py -- the blind re-read of C2.1, C2.4, C2.3 (configured economies) and C2.5 (ledger S58)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    print("inputs: blind_review.py, pass_common.py and its parts, " + ", ".join(sorted(READ)) + "\n")

    print("[1] the readings are complete and follow the rules")
    econ = {c for c in ECON if p.names.get(c)}
    ok_print(econ == set(ECON), "the six configured economies are corpus entries", str(set(ECON) - econ))
    for cid in (C21, C24, C23):
        keys = {k for k in p.merged if k[1] == cid and k[0] in ECON}
        mine = {k for k in FIRST if k[1] == cid}
        ok_print(mine == keys and len(keys) == 6, f"one first reading of {cid} for each of the six configured "
                 "economies the pass holds, no more", str(sorted(mine ^ keys)))
    keys = {k for k in p.merged if k[1] == C25}
    ok_print(set(NEW) == keys and len(keys) == 23, "one blind reading for each of the 23 C2.5 units the pass holds, "
             "no more", str(sorted(set(NEW) ^ keys)))
    both = {**FIRST, **NEW}
    pc.check_records(p, both, ok_print)
    pc.check_rule(both, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in both.values()), "each flag names an alternative score other than the verdict")
    bad = [k for k in sorted(both) if len(br.blind_view(p, k)["clauses_v2"]) != len(both[k]["clauses"])]
    ok_print(not bad, "each reading has one status per clause blind_view shows", str(bad))
    for cid, ec in ((C21, E1), (C23, E3), (C24, E4), (C25, E5)):
        key = next(k for k in sorted(both) if k[1] == cid)
        listed = {ec + f for f in br.blind_view(p, key)["cache_files"]}
        ok_print(listed <= set(READ), f"every file blind_view lists for {cid} is one this script reads or names",
                 str(sorted(listed - set(READ))))
    ok_print(all(os.path.isfile(path(f)) for f in READ), "every file in READ exists")
    mech = {e["code"] for e in json.load(open(path("neec_corpus_v2.json"), encoding="utf-8"))["entries"]
            if e["scope_class"] == "mechanism"}
    ok_print(not [k for k, u in NEW.items() if k[0] in mech and u["verdict"] == 0.0],
             "no mechanism is at 0.0 (Session 73's class observation: a mechanism that governs no clause's quantity "
             "is held at 0.5)")
    ok_print(all(u["verdict"] != 1.0 for k, u in NEW.items() if any(st == "R" for st, _, _ in u["clauses"])),
             "no reading with a clause out of reach is above 0.5 (D28(c))")

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG_PRINT.items():
        print(f"    {k}: {v}")

    print("\n[3] the readings (verdicts, clause statuses, flags)")
    btables = []
    for cid, units, label in ((C21, FIRST, "first reading"), (C24, FIRST, "first reading"),
                              (C23, FIRST, "first reading"), (C25, NEW, "blind reading")):
        print(f"\n{cid} ({label}):")
        t = blind_table(p, cid, units)
        btables.append(t)
        print(t)
        v = [r["verdict"] for k, r in units.items() if k[1] == cid]
        print(f"\n{cid}: {v.count(1.0)} at 1.0, {v.count(0.5)} at 0.5, {v.count(0.0)} at 0.0; "
              f"{sum(1 for k, r in units.items() if k[1] == cid and r['flag'])} flagged")

    print("\n[4] the comparison with the readings the pass holds (compare_group on the readings as recorded at the "
          "checkpoint, 6fbcfed): C2.5 against parts (2.11) and (b5); the first readings against parts (2.11) and (a), "
          "whose clause 1 was held unmeasured (decision 65.2)")
    prior = prior_units(p)
    cmp_tables, vd = [], []
    for cid, units, label in ((C21, FIRST, "First (Session 75)"), (C24, FIRST, "First (Session 75)"),
                              (C23, FIRST, "First (Session 75)"), (C25, NEW, "Blind (Session 75)")):
        t_cmp, res, tally = comparison_table(p, prior, units, cid, label)
        cmp_tables.append(t_cmp)
        print(f"\n{cid}:")
        print(t_cmp)
        d = sorted((k for k in res if prior[k]["verdict"] != units[k]["verdict"]), key=lambda k: k[0])
        vd += d
        print(f"\n{cid}: {tally['agree']} agree, {tally['revise']} revise; {len(d)} verdicts differ: " + ", ".join(
            f"{p.names[k[0]]} {pc.f1(prior[k]['verdict'])} to {pc.f1(units[k]['verdict'])}" for k in d))
    b5 = [k for k in NEW if p.part_of[k] == "(b5)"]
    ok_print(len(b5) == 10 and all(len(prior[k]["clauses"]) == 4 for k in b5),
             "the ten part (b5) units carry the pre-v2.0 four-clause list, so compare_group reports their clause "
             "count, not a clause status (ledger D54)")

    print("\n[5] the reconciliation (protocol 5.3) and the final readings")
    ok_print(set(RECONCILE) <= set(vd), "every reconciled unit is one whose new verdict differs from the prior's")
    allfinal = {**FIRST_FINAL, **FINAL}
    ok_print(all(allfinal[k]["verdict"] == prior[k]["verdict"] for k in RECONCILE),
             "each reconciliation moves the verdict to the prior's, and only there")
    stand = [k for k in vd if k not in RECONCILE]
    ok_print(set(STAND) == set(stand), "every standing verdict difference has its stated reason")
    ok_print(all(allfinal[k]["flag"] and allfinal[k]["flag"][0][:3] == pc.f1(prior[k]["verdict"]) for k in stand),
             "each standing difference's final reading is flagged toward the prior's verdict")
    ok_print(set(FLAGS) <= set(stand) and all(not NEW[k]["flag"] or NEW[k]["flag"][0][:3] != pc.f1(prior[k]["verdict"])
                                              for k in FLAGS),
             "the flags added after the comparison are for standing differences whose blind reading carried none "
             "toward the prior's verdict")
    ok_print(all(allfinal[k]["flag"] and allfinal[k]["flag"][0][:3] == pc.f1({**FIRST, **NEW}[k]["verdict"])
                 for k in RECONCILE), "each reconciled unit keeps its new verdict as its flag")
    ok_print(all(FINAL[(c, cid)]["verdict"] == NEW[(c, cid)]["verdict"] for c, cid, _ in CLAUSE_FIX),
             "each clause correction leaves its unit's verdict unchanged")
    pc.check_records(p, allfinal, ok_print)
    pc.check_rule(allfinal, ok_print)
    ok_print(not my_changes(prior, FIRST_FINAL), "the first readings of clause 1 move no verdict once reconciled "
             "(decision 65.2's holds stand as verdicts; their clause statuses are recorded)")
    print("standing verdict changes: " + ", ".join(
        f"{p.names[k[0]]} {k[1]} {pc.f1(prior[k]['verdict'])} to {pc.f1(allfinal[k]['verdict'])}" for k in stand))
    cco = [k for k in vd if k[0] == "CCO"]
    ok_print(not cco, "no CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4: a rise is applied, a fall held)",
             str(cco))
    final_tables = [blind_table(p, cid, FIRST_FINAL) for cid in (C21, C24, C23)] + [blind_table(p, C25, FINAL)]
    for cid, t in zip((C21, C24, C23, C25), final_tables):
        print(f"\nfinal readings, {cid}:")
        print(t)

    print("\n[6] consequences once applied (by generator in ledger S61, not here), alone and with Sessions 71 to 74")
    t_cons, held, (f1n, f1t), (f2n, f2t), tiers, tiers_alone, mine = consequence_table(p, prior, allfinal)
    ok_print(held, "neec_corpus_v2.json carries the prior's verdict for each of the 41 units (the published "
             "provisional scores are the prior's)")
    print(t_cons)
    print(f"\nfirst place on the 29 after this group alone: {f1n} at {f1t:.1f}; after Sessions 71 to 75: {f2n} at "
          f"{f2t:.1f}")
    print("tier changes, this group alone: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers_alone) or "none"))
    print("tier changes, after Sessions 71 to 75: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers) or "none"))
    t_flags, movers = flag_effects(p, prior, allfinal)
    print(f"\nthe final readings' {sum(1 for u in allfinal.values() if u['flag'])} flags, each taken alone (on all "
          "five groups' final verdicts):")
    print(t_flags)
    print("flags that would change a tier or first place: " + (", ".join(f"{p.names[c]} {cid}" for c, cid in movers)
                                                                or "none"))

    print("\n[7] the record")
    names = ("C2.1", "C2.4", "C2.3", "C2.5")
    record_check([(f"readings, {n}", t) for n, t in zip(names, btables)] +
                 [(f"comparison, {n}", t) for n, t in zip(names, cmp_tables)] +
                 [(f"final readings, {n}", t) for n, t in zip(names, final_tables)] +
                 [("consequences", t_cons), ("flag effects", t_flags)], ok_print)
    print("\nBLIND RE-READ OF C2.1, C2.4, C2.3 AND C2.5 CHECKED." if ok else "\nBLIND RE-READ: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
