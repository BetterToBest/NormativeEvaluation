#!/usr/bin/env python3
"""
blind_s76.py -- NEEC stage 3b, the blind re-read: C2.6, C3.6 and C4.6 for the 17 designs and mechanisms (ledger S59)
====================================================================================================================
Session 76, on Opus 5.5 (decisions 69.1, 69.2; ledger D52, D53). The three criteria v2.0 added (class N): C2.6 Civil
Liberties and Rule of Law, C3.6 Productive and Innovative Capacity and C4.6 Harm Internalization, read for the 17
entries that are not configured national economies -- nine comprehensive systems and eight mechanisms, 51 units. Session
65 (part (2.11), on Sonnet 5.5) scored them on a stated rule without reading their sources (the "least-read units in
the pass", evidence_cache/designs_index_s70.json); here each is read from the design's own texts. The six configured
economies' units on these criteria are ledger S60's (Session 77).

THE BLIND STEP. The readings below were written from blind_review.blind_view() -- the v2.0 clause text and the
evidence_cache/C2.6/, C3.6/ and C4.6/ file names -- from the criteria's measurement text in criteria.json, and from the
sources this session cached (evidence_cache_s76.py) or names (evidence_cache/<criterion>/sources_s76.md), and committed
to the branch as a checkpoint before part (2.11)'s readings of these units, Session 65's record, or the units' published
scores and rationales on these criteria were opened, except as the record discloses (NEEC_BlindReview_s76.md,
section 2).

READINGS, C2.6 (Freedom House checklist >=53 of 60; consent to medical treatment in law; health compulsion prescribed by
law, time-limited and open to an independent court)
  2.6.1 clause 1, a comprehensive system: the fifteen civil-liberties questions answered 0-4 from the system's own
        sources, crediting only what they state and provide for (protocol 4.1): guarantees, the body that decides
        disputes between participants and the system's administrators and its independence, and, where allocation
        depends on personal data, limits on its use. Cleared at 53 or more with the estimate's range wholly at or above
        the bar; not shown where the sources state guarantees for only some questions, leave disputes with the
        administrators, or the estimate straddles 53.
  2.6.2 clause 1, a mechanism: out of reach (D28(c), protocol 3.2): it adds to or takes from the host's liberties but
        does not govern the 0-60 total; what it adds or takes is recorded.
  2.6.3 clause 2: cleared where the sources make medical intervention depend on the person's consent and protect
        refusal; not shown where they are silent. A mechanism: out of reach, unless it delivers medical care itself
        (then not shown where silent).
  2.6.4 clause 3: cleared where the sources permit no health compulsion outside a judicial process with due process,
        or state that every such measure is prescribed by law, time-limited and open to an independent court; not
        shown where silent. A mechanism: out of reach, unless it governs an employment or essential service whose loss
        could penalise refusal (then not shown where silent).
  2.6.5 0.0 (the band's case): a design that subordinates expression, association, due process or consent to its
        allocation or administration with no independent adjudication; never with a clause cleared (D28(f)).

READINGS, C3.6 (output per hour and TFP non-declining over 20 years; basic-needs output at the system's own hours)
  3.6.1 clauses 1 and 2, a comprehensive system: its mechanisms for allocating investment and rewarding improvement,
        calibrated by the record of their components (the measurement text). Cleared where they are a market
        economy's, unchanged in kind, whose components' record is non-declining: in Penn World Table 10.01, 1999 to
        2019, output per hour and TFP rose in the United States, Denmark, Finland and Sweden (the market economies in
        the cache that are neither resource-dependent nor state-directed). Not shown where the design replaces or
        materially changes them with mechanisms whose record is absent or mixed (the 0.5 band's projection on untested
        assumptions); short where its own sources state a decline.
  3.6.2 clauses 1 and 2, a mechanism: out of reach unless, generalised, it allocates investment economy-wide; then not
        shown where no record isolates the mechanism ("score the mechanism, not a country", protocol 3.2).
  3.6.3 clause 3: cleared where the design states its working time and accounts for basic-needs output at it with
        component evidence; not shown where it states no hours or its account is a projection on untested assumptions.
        A mechanism: out of reach (the host's hours).
  3.6.4 0.0 (the band's case): the design's own assumptions imply that basic needs cannot be provisioned at its
        stated hours, or it suppresses allocation signals with no stated replacement; never with a clause cleared.

READINGS, C4.6 (pollution mortality non-increasing; liability enforceable by those harmed; regulators free of improper
influence)
  4.6.1 clause 1: the design's projected pollution mortality in the economy it is proposed for; not shown where it
        projects none. A mechanism: out of reach, unless it governs a source of the harms counted (community water
        systems: then not shown where unmeasured).
  4.6.2 clause 2: cleared where the sources make those who cause harm liable to compensate those harmed (tort, or a
        scheme funded by a levy on them), enforceably by those harmed and collectively where the harm is dispersed;
        short where they limit liability so that a class of harm goes uncompensated; not shown where silent or
        partial. A mechanism: out of reach unless it governs a harm-causing activity's liability.
  4.6.3 clause 3: cleared where the sources provide for regulators of food, water, air, chemicals and medicines
        independent of those they regulate; short where the design abolishes that regulation; not shown where silent.
        A mechanism: out of reach unless it governs such regulators.
  4.6.4 0.0 (the band's case): no structural mechanism makes harm a cost to whoever causes it -- those who cause harm
        shielded from liability with no compensation they fund, and their regulation controlled by them; never with a
        clause cleared.

THE COMPARISON (written after the checkpoint, 600c994). compare_group() sets each reading against part (2.11)'s
(rescoring_s65.NEW_UNITS: the class N criteria are not in pass_common's merged units). The prior is Session 65's stated
rule throughout; no verdict differs, so nothing is reconciled (protocol 5.3), and the eight clause revisions stand
under Session 71's rule (STAND). FINAL, the blind readings unchanged, is what the generator session (ledger S61)
applies: no verdict changes. No CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4).

Usage: python3 blind_s76.py   (reads criteria.json, neec_corpus.json, neec_scores.csv, the scripts pass_common.PARTS
                               names and the files they read, blind_review.py, blind_s71.py to blind_s75.py, the
                               evidence_cache/C2.6/, C3.6/ and C4.6/ files, neec_corpus_v2_s65_snapshot.json, neec_scores_v2_s65_snapshot.csv
                               and NEEC_BlindReview_s76.md; writes nothing)
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
C26, C36, C46 = "C2.6", "C3.6", "C4.6"
E26, E36, E46 = (f"evidence_cache/{c}/" for c in (C26, C36, C46))
LP26, CCO26, INT26, PE26, OST, JG, BIEN, GEO26, N26 = (
    E26 + "lp_platform_c26_extract.txt", E26 + "cco_research_hub_c26_extract.txt",
    E26 + "integral_wp_v01_c26_extract.txt", E26 + "pe_model_c26_extract.txt", E26 + "ostrom_nobel_c26_extract.txt",
    E26 + "levy_jg_wp902_c26_extract.txt", E26 + "bien_definition_c26_extract.txt",
    E26 + "george_progress_poverty_c26_extract.txt", E26 + "sources_s76.md")
CCO36, INT36, PE36, PWT, N36 = (E36 + "cco_research_hub_c36_extract.txt", E36 + "integral_wp_v01_c36_extract.txt",
                                E36 + "pe_model_c36_extract.txt", E36 + "pwt1001_selected_economies.csv",
                                E36 + "sources_s76.md")
LP46, PE46, INT46, WEF, CCO46, N46 = (E46 + "lp_platform_c46_extract.txt", E46 + "pe_model_c46_extract.txt",
                                      E46 + "integral_wp_v01_c46_extract.txt", E46 + "wef_metrics_c46_extract.txt",
                                      E46 + "cco_research_hub_c46_extract.txt", E46 + "sources_s76.md")
# Files blind_view lists that bear on the configured economies (ledger S60), read for the measures only.
OTHER = [E26 + "owid_freedom_house_civil_liberties_rating.csv", E26 + "law_in_force_notes_s70.md",
         E26 + "us_cfr_42_70.14.html", E26 + "us_cfr_42_71.37.html", E36 + "easterly_fischer_1995_nber_w4735.pdf",
         E46 + "SDGAIRBOD.json", E46 + "SDGPOISON.json", E46 + "SDGWSHBOD.json", E46 + "air42.json",
         E46 + "notes_s70.md"]
# Files a later session added to these directories (Session 77, ledger S60: the configured economies' sources), which
# blind_view lists but which were not there when this group read: outside this group's view, so not required in READ.
LATER = {"evidence_cache/" + f for f in (
         "C2.6/cn_law_c26_extract.txt", "C2.6/dk_law_c26_extract.txt", "C2.6/fh_fiw2026_cl_f1_extract.txt",
         "C2.6/fi_law_c26_extract.txt", "C2.6/no_law_c26_extract.txt",
         "C2.6/owid_fh_civil_liberties_rating_su_s77.csv", "C2.6/owid_fh_civil_liberties_score_s77.csv",
         "C2.6/owid_vdem_civil_liberties_s77.csv", "C2.6/se_law_c26_extract.txt", "C2.6/sg_law_c26_extract.txt",
         "C2.6/su_law_c26_extract.txt", "C2.6/us_law_c26_extract.txt", "C3.6/easterly_fischer_1995_tables_s77.csv",
         "C3.6/pip_spl_selected_economies.csv", "C3.6/pwt110_selected_economies.csv", "C4.6/cn_law_c46_extract.txt",
         "C4.6/nordic_law_c46_extract.txt", "C4.6/oecd_exp_morsc_gbd2019_s77.csv",
         "C4.6/su_environment_c46_extract.txt", "C4.6/us_law_c46_extract.txt", "C4.6/who_gho_sdgpoison_s77.csv",
         "C2.6/sources_s77.md", "C3.6/sources_s77.md", "C4.6/sources_s77.md")}
READ = (LP26, CCO26, INT26, PE26, OST, JG, BIEN, GEO26, N26, CCO36, INT36, PE36, PWT, N36, LP46, PE46, INT46, WEF,
        CCO46, N46, *OTHER)
DESIGNS = ("MS", "LM", "DG", "SC", "FALC", "PE", "CCO", "INT", "DE")
MECHS = ("MMT", "UBI", "GEO", "MC", "UBS", "SWF", "IF", "OS")
NEW = {}


def U(code, cid, verdict, clauses, flag=None, note="", zero=None):
    """One blind reading. clauses: (status, estimate, source) per v2.0 clause. flag: (alternative, reading)."""
    NEW[(code, cid)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note, zero=zero)


def path(name):
    return os.path.join(HERE, name)


def f1(x):
    return f"{x:.1f}"


# ---- the market economies' productivity record, recomputed from the cache (reading 3.6.1) ------------------------
PWT_ROWS = {(r["countrycode"], int(r["year"])): r for r in csv.DictReader(open(path(PWT), encoding="utf-8"))}
MARKET = ("USA", "DNK", "FIN", "SWE")


def cagr(a, b, years=20):
    return 100 * ((b / a) ** (1 / years) - 1)


def lp_tfp(iso, y0=1999, y1=2019):
    """Compound annual change, % a year: output per hour (rgdpo / (emp x avh)) and TFP (rtfpna)."""
    a, b = PWT_ROWS[(iso, y0)], PWT_ROWS[(iso, y1)]
    lp = lambda r: float(r["rgdpo"]) / (float(r["emp"]) * float(r["avh"]))
    return cagr(lp(a), lp(b)), cagr(float(a["rtfpna"]), float(b["rtfpna"]))


REC = {iso: lp_tfp(iso) for iso in MARKET}
REC_STR = "; ".join(f"{iso} {REC[iso][0]:.2f} and {REC[iso][1]:.2f}" for iso in MARKET)
FIG_PRINT = {"PWT 10.01, 1999-2019, output per hour and TFP, compound % a year (USA, DNK, FIN, SWE)": REC_STR}
PWTS = f"Penn World Table 10.01 ({PWT}): {REC_STR} % a year, output per hour and TFP, 1999-2019"


# =================================================================================================================
# C2.6 Civil Liberties and Rule of Law
# =================================================================================================================
NO_CONSENT = "not shown: the sources are silent on consent to medical treatment (reading 2.6.3)"
NO_COMP = "not shown: the sources are silent on compulsory treatment, vaccination, quarantine or isolation (reading 2.6.4)"
R1 = "out of reach: a mechanism does not govern the host's 0-60 civil-liberties total (reading 2.6.2)"
R2 = "out of reach: the mechanism delivers no medical care and governs no consent law (reading 2.6.3)"
R3 = ("out of reach: the mechanism governs no health compulsion and no employment or service whose loss could "
      "penalise refusal (reading 2.6.4)")

U("MS", C26, 0.5,
  [("U", "not shown: Roemer (1994, ch. 1) takes the political setting to be a democracy and Schweickart (2011, pt. II) "
         "presupposes political democracy beside workplace democracy; both specify economic institutions only and state "
         "no guarantees for the checklist's questions, nor the body that decides disputes between citizens and the "
         "public banks or planning boards, nor its independence (reading 2.6.1)", N26),
   ("U", NO_CONSENT, N26), ("U", NO_COMP, N26)],
  note="0.5: liberal-democratic institutions presupposed, not specified")

U("LM", C26, 0.5,
  [("U", "not shown, estimate 50 to 56 of 60, straddling the bar: the platform states full freedom of expression and "
         "religion, no control of media (1.2), privacy against surveillance (1.3), due process, speedy trial, counsel, "
         "jury and the presumption of innocence (1.7), equal rights before government whatever race, sex, creed or "
         "orientation (3.5), and no curtailment of rights in war or epidemic (3.2): D1, D2, D4, E1, E2, F2, F3, G1, G2 "
         "and G3 at 4; academic freedom (D3) and an independent judiciary (F1) implied, not stated, 3 each; labour "
         "agreements 'outside the scope of government' with bargaining at the employer's choice (2.11: E3 about 2.5), "
         "private discrimination left to association (F4 about 3), and no protection from economic exploitation short "
         "of force or fraud (G4 about 2) (reading 2.6.1)", LP26),
   ("C", "cleared: individuals own their bodies (1.1) and the platform recognises each person's freedom to choose 'the "
         "medicines and treatments they will use', opposing any government mandate of treatment, vaccines included "
         "(2.13): intervention without consent is aggression, prohibited (reading 2.6.3)", LP26),
   ("C", "cleared: 'Individual rights shall not be curtailed, whether based on circumstances of war, epidemic, natural "
         "disaster or emergency' (3.2), and no treatment or vaccine may be mandated (2.13); restraint of a person who "
         "deliberately places others at significant risk is a crime tried with due process and a jury (1.7), so any "
         "compulsion runs through a court (reading 2.6.4)", LP26)],
  flag=("1.0: reading academic freedom and an independent judiciary as implied guarantees of a state whose only "
        "functions are courts, police and defence (D3 and F1 at 4), which puts clause 1 at 55 or more", "2.6.1"),
  note="0.5: the strongest stated guarantees of the 17, with clause 1 at the bar; consent and the limits of "
       "compulsion stated")

U("MMT", C26, 0.5,
  [("R", R1 + "; it adds a standing, voluntary job offer that is 'not a workfare program' (WP 902, key features), which "
              "lessens economic coercion, and takes nothing", JG),
   ("R", R2, JG),
   ("U", "not shown: the job is an employment the programme governs, and the sources do not say whether refusing a "
         "health measure could end it (reading 2.6.4)", JG)],
  note="0.5: a mechanism that adds a voluntary job offer; the clauses are the host's")

U("UBI", C26, 0.5,
  [("R", R1 + "; it adds a payment 'without means-test or work requirement' (BIEN), removing benefit conditionality and "
              "its policing, and takes nothing", BIEN),
   ("R", R2, BIEN),
   ("R", R3 + "; its own payment is unconditional by definition, so it cannot be withheld for refusing a health "
              "measure", BIEN)],
  note="0.5: a mechanism that adds an unconditional payment; the clauses are the host's")

U("DG", C26, 0.5,
  [("U", "not shown: Hickel (2020, ch. 5-6) and Kallis et al. (2020, ch. 3) propose democratic deliberation over "
         "production and expanded public services within an existing democracy; they state no guarantees for the "
         "checklist's questions and no adjudication of their own (reading 2.6.1)", N26),
   ("U", NO_CONSENT, N26), ("U", NO_COMP, N26)],
  note="0.5: a democratic setting presupposed, not specified")

U("SC", C26, 0.5,
  [("U", "not shown: the Davos Manifesto 2020 commits companies to 'respect human rights' and the stakeholder metrics "
         "ask them to report on anti-corruption, lobbying and whistleblowing; the design leaves the checklist's questions "
         "to the host state's law and states no guarantees or adjudication of its own (reading 2.6.1)", f"{N26}; {WEF}"),
   ("U", NO_CONSENT, N26), ("U", NO_COMP, N26)],
  note="0.5: a reform of corporate governance inside a host democracy; no guarantees of its own")

U("FALC", C26, 0.5,
  [("U", "not shown: Bastani (2019) sets out automation, common ownership and 'popular municipalism' but states no "
         "court, no due-process institution and no guarantees for the checklist's questions (reading 2.6.1)", N26),
   ("U", NO_CONSENT, N26), ("U", NO_COMP, N26)],
  note="0.5: no rights or adjudication stated")

U("PE", C26, 0.5,
  [("U", "not shown: councils give each member a say in proportion to how far a decision affects them, and each worker "
         "council sets its own effort-rating procedure, 'grievance procedures' included; effort ratings set consumption "
         "rights, and the model names no body independent of the councils for disputes over them; the separate "
         "political proposal (Shalom's parpolity) is not specified for the checklist (reading 2.6.1)", f"{PE26}; {N26}"),
   ("U", NO_CONSENT, PE26), ("U", NO_COMP, PE26)],
  flag=("0.0: reading consumption rights set by co-workers' effort ratings, with grievances heard only inside the "
        "council, as subordinating due process to allocation with no independent adjudication (the 0.0 band)", "2.6.5"),
  note="0.5: self-management with internal grievance procedures; no guarantees stated")

U("CCO", C26, 0.5,
  [("U", "not shown, estimate 46 to 54: the PTH charter states freedom of expression, assembly and political activity, "
         "privacy against surveillance, fair hearings before penalties, equal protection, 'notice, hearing, and appeal "
         "rights' for all enforcement, and that community governance shall not infringe constitutionally protected "
         "rights; independent courts hear discrimination complaints and zone decisions get independent review; personal "
         "data is held under zero-knowledge proofs and user-held keys. Against them: the risk framework's automated "
         "transaction limits and account restrictions reach judicial review only at the 'critical' level, merit "
         "assessments are appealed to 'democratic review', the 'independent judiciary' of PTH communities is an elected "
         "grievance committee, and officials' 'factual honesty' is enforceable by Judicial Guard referral and "
         "prosecution, which bears on expression (D1, D4) and due process (F2) (reading 2.6.1)", CCO26),
   ("U", NO_CONSENT, CCO26), ("U", NO_COMP, CCO26)],
  note="0.5: a bill of rights and due process for its communities, with automated restrictions reviewed by courts "
       "only at the highest level")

U("INT", C26, 0.5,
  [("U", "not shown: the white paper states data safeguards (only effects, not internals, exposed across nodes; local "
         "data sovereignty) and a non-punitive rule ('no credit confiscation, no reputation tribunal'), but no "
         "guarantees for the checklist's questions; a contributor's dispute over a host node's assessment, which sets "
         "the time credits that give access to goods, is 'resolved through the host's CDS or mediation', and "
         "'individuals cannot bypass local CDS by appealing upward' (reading 2.6.1)", INT26),
   ("U", NO_CONSENT, INT26), ("U", NO_COMP, INT26)],
  flag=("0.0: reading disputes over contribution assessments, which set access to goods, as left to the assessing node "
        "with no appeal beyond it -- due process subordinated to allocation with no independent adjudication (the 0.0 "
        "band)", "2.6.5"),
  note="0.5: data limits and a non-punitive rule; disputes stay with the node that assessed")

U("DE", C26, 0.5,
  [("U", "not shown: Raworth (2017) names the partner state, the commons and the household as provisioning domains and "
         "presupposes the host democracy; she states no guarantees or adjudication of her own (reading 2.6.1)", N26),
   ("U", NO_CONSENT, N26), ("U", NO_COMP, N26)],
  note="0.5: a framework for economic goals; rights left to the host")

U("GEO", C26, 0.5,
  [("R", R1 + "; it adds a public register of land values and takes nothing: titles stay where they are ('It is not "
              "necessary to confiscate land; it is only necessary to confiscate rent', book VIII, ch. 2)", GEO26),
   ("R", R2, GEO26), ("R", R3, GEO26)],
  note="0.5: a tax mechanism; the clauses are the host's")

U("MC", C26, 0.5,
  [("R", R1 + "; membership is voluntary and each scheme's committee sets credit limits and resolves disputes, with the "
              "host's courts behind it; nothing is taken", N26),
   ("R", R2, N26), ("R", R3, N26)],
  note="0.5: a voluntary exchange network; the clauses are the host's")

U("UBS", C26, 0.5,
  [("R", R1 + "; it adds a universal 'democracy and legal' service (legal aid and access to courts), which bears on F1 "
              "and F2, and takes nothing", N26),
   ("U", "not shown: health care is one of the seven services, so consent in its delivery is within reach, and the "
         "proposal is silent on it, leaving it to the host's law (reading 2.6.3)", N26),
   ("U", "not shown: the proposal does not say whether access to a service could be conditioned on a health measure "
         "(reading 2.6.4)", N26)],
  note="0.5: a mechanism that adds universal legal aid; consent within its health service unstated")

U("SWF", C26, 0.5,
  [("R", R1 + "; the fund is governed by statute, with a Council on Ethics, and neither adds to nor takes from the "
              "checklist's questions", N26),
   ("R", R2, N26), ("R", R3, N26)],
  note="0.5: a public investment fund; the clauses are the host's")

U("IF", C26, 0.5,
  [("R", R1 + "; generalised to all finance, it would put every financial contract under a Shari'ah supervisory board's "
              "ruling, binding those of other faiths to a religious standard in their finance (D2), while disputes go "
              "to the civil courts or arbitration", N26),
   ("R", R2, N26), ("R", R3, N26)],
  note="0.5: a contract set; the clauses are the host's")

U("OS", C26, 0.5,
  [("R", R1 + "; it adds rapid, low-cost local arenas for resolving conflicts (principle 6) and recognised rights of "
              "users to make their own rules (principle 7); sanctions are graduated and applied by monitors who are "
              "users or accountable to them (principles 4 and 5)", OST),
   ("R", R2, OST), ("R", R3, OST)],
  note="0.5: self-governed commons with local conflict resolution; the clauses are the host's")


# =================================================================================================================
# C3.6 Productive and Innovative Capacity
# =================================================================================================================
NO_HOURS = "not shown: the sources state no working time and no account of basic-needs output at it (reading 3.6.3)"
RM1 = ("out of reach: the mechanism allocates no investment and rewards no improvement economy-wide even when "
       "generalised (reading 3.6.2)")
RM3 = "out of reach: the mechanism sets no working time; the host's hours apply (reading 3.6.3)"

U("MS", C36, 0.5,
  [("U", "not shown: investment through public main banks that monitor firms, with the state steering it by interest "
         "rates (Roemer 1994, ch. 7-8), or a capital-assets tax funding public investment banks (Schweickart 2011, "
         "pt. II), beside markets for goods; the components' record is mixed -- Japan's main-bank system, which Roemer "
         "cites, against Yugoslavia's self-managed firms, whose productivity growth fell through the 1970s and 1980s "
         "(reading 3.6.1)", N36),
   ("U", "not shown: the same mechanisms and record for improvement in methods; neither source provides a reward for "
         "innovation beyond firms' market returns (reading 3.6.1)", N36),
   ("U", NO_HOURS, N36)],
  note="0.5: markets for goods with public control of investment; a mixed record")

U("LM", C36, 0.5,
  [("U", "not shown: private capital markets and profit, the market economies' own components, but with the state's part "
         "in them removed -- education 'best provided by the free market' (2.12), no public research -- so no economy's "
         "record is of the design's mechanism (reading 3.6.1)", f"{LP26}; {PWTS}"),
   ("U", "not shown: improvement rewarded by profit alone, on the same reading (reading 3.6.1)", LP26),
   ("U", NO_HOURS, N36)],
  note="0.5: market allocation without the public research and education market economies have had")

U("MMT", C36, 0.5,
  [("R", RM1 + "; functional finance and the job guarantee manage demand and employment", JG),
   ("R", RM1, JG),
   ("R", RM3 + "; the job guarantee's own output is public-service work, not the basic-needs basket", JG)],
  note="0.5: a demand and employment mechanism; the clauses are the host's")

U("UBI", C36, 0.5,
  [("R", RM1, BIEN), ("R", RM1, BIEN), ("R", RM3, BIEN)],
  note="0.5: a transfer; the clauses are the host's")

U("DG", C36, 0.5,
  [("U", "not shown: the sources treat growth of output as no aim, propose to scale down ecologically destructive "
         "production and move work toward care and agroecology under democratic planning (Hickel 2020, ch. 5-6; Kallis "
         "et al. 2020); they state no mechanism for allocating investment or rewarding improvement and no record "
         "(reading 3.6.1)", N36),
   ("U", "not shown: on the same reading (reading 3.6.1)", N36),
   ("U", "not shown: a shorter working week is stated (Hickel 2020, ch. 5), with no account of basic-needs output at it "
         "(reading 3.6.3)", N36)],
  flag=("0.0: reading the planned shift of work toward labour-intensive care and agroecology, with output growth no "
        "aim, as an intended decline in output per hour with no pathway back under the design's logic (the 0.0 band)",
        "3.6.4"),
  note="0.5: no investment mechanism stated; shorter hours without a provisioning account")

U("SC", C36, 0.5,
  [("C", "cleared: market allocation of investment by private capital, unchanged in kind, with company boards answering "
         "to stakeholders as well as shareholders (Schwab and Vanham 2021); its components' record is non-declining "
         "(reading 3.6.1)", f"{PWTS}; {N36}"),
   ("C", "cleared: improvement rewarded by profit and competition as in the market economies, whose TFP rose over the "
         "20 years (reading 3.6.1)", PWTS),
   ("U", NO_HOURS, N36)],
  note="0.5: the market economies' allocation and record; no stated hours or provisioning account")

U("FALC", C36, 0.5,
  [("U", "not shown: automation and information goods are to drive costs toward zero, with socialised central banking "
         "and public investment (Bastani 2019, ch. 3-4, 8-11); no mechanism for allocating goods that stay scarce is "
         "stated, and none has a record (reading 3.6.1)", N36),
   ("U", "not shown: on the same reading (reading 3.6.1)", N36),
   ("U", "not shown: working time is to fall toward zero by automation, a projection on untested assumptions, with no "
         "provisioning account (reading 3.6.3)", N36)],
  flag=("0.0: reading the end-state of free provision as suppressing price signals with no stated replacement for goods "
        "that remain scarce (the 0.0 band)", "3.6.4"),
  note="0.5: abundance projected from automation; allocation of what stays scarce unstated")

U("PE", C36, 0.5,
  [("U", "not shown: investment is allocated by participatory planning with indicative prices; a council that adopts an "
         "innovation gains until others copy it and indicative prices adjust, and the model holds that diffusion is "
         "faster without private ownership of innovations; no economy has run on it (reading 3.6.1)", PE36),
   ("U", "not shown: improvement rewarded by the temporary gain and by social recognition, on the same reading (reading "
         "3.6.1)", PE36),
   ("U", "not shown: hours are each worker's, compensated as effort; no economy-wide working time and no provisioning "
         "account (reading 3.6.3)", f"{PE26}; {PE36}")],
  note="0.5: a stated replacement for market allocation, untried")

U("CCO", C36, 0.5,
  [("U", "not shown: the dollar economy's market allocation is kept and the PTF adds public-trust investment; the "
         "design's productivity claims ('10-15% export improvements'; total productive work up 42%) come from its own "
         "simulation, a projection on untested assumptions (reading 3.6.1)", CCO36),
   ("U", "not shown: on the same reading (reading 3.6.1)", CCO36),
   ("U", "not shown: a 25-hour standard workweek is stated, 'viable with CCO Basic Unit supplementation' as AI and quantum "
         "computing reduce workloads ('hours move 35 to 25' in 2030-2035): a projection, with no account of basic-needs "
         "output at 25 hours on component evidence (reading 3.6.3)", CCO36)],
  note="0.5: market allocation kept; productivity and the 25-hour week projected")

U("INT", C36, 0.5,
  [("U", "not shown: price is replaced by a stated multi-signal valuation (weighted labour, ecological impact, access "
         "and fairness signals) that sets each good's access value, with open design and cooperative production -- a "
         "stated replacement, so not the 0.0 case, but with no record (reading 3.6.1)", INT36),
   ("U", "not shown: improvement comes through open design refinement, on the same reading (reading 3.6.1)", INT36),
   ("U", "not shown: contributions are recorded in hours but no standard working time is stated, and there is no "
         "provisioning account (reading 3.6.3)", INT36)],
  note="0.5: a stated non-price calculation, untried")

U("DE", C36, 0.5,
  [("U", "not shown: Raworth is 'agnostic about growth' (2017, ch. 7) and states no mechanism of her own for allocating "
         "investment or rewarding improvement (reading 3.6.1)", N36),
   ("U", "not shown: on the same reading (reading 3.6.1)", N36),
   ("U", NO_HOURS, N36)],
  note="0.5: a framework of goals with no productivity mechanism of its own")

U("GEO", C36, 0.5,
  [("R", RM1 + "; the tax falls on land value and lifts taxes from labour and capital, which bears on incentives but "
              "allocates nothing", GEO26),
   ("R", RM1, GEO26), ("R", RM3, GEO26)],
  note="0.5: a tax; the clauses are the host's")

U("MC", C36, 0.5,
  [("R", RM1 + "; mutual credit finances exchange between members, not investment", N36),
   ("R", RM1, N36), ("R", RM3, N36)],
  note="0.5: an exchange network; the clauses are the host's")

U("UBS", C36, 0.5,
  [("R", RM1 + "; it provides services, financed by tax", N36),
   ("R", RM1, N36), ("R", RM3, N36)],
  note="0.5: service provision; the clauses are the host's")

U("SWF", C36, 0.5,
  [("R", RM1 + "; the fund invests outside the economy under a statutory mandate (the Government Pension Fund Global) "
              "and allocates no domestic investment", N36),
   ("R", RM1, N36), ("R", RM3, N36)],
  note="0.5: an external portfolio; the clauses are the host's")

U("IF", C36, 0.5,
  [("U", "not shown: generalised, profit-and-loss-sharing contracts would allocate all external finance by expected "
         "returns shared with the financier (Chapra 1985, ch. 3-4), so the clause is within reach; no record isolates "
         "the mechanism, since the economies that Islamised their banking kept debt-like contracts in practice (reading "
         "3.6.2)", N36),
   ("U", "not shown: on the same reading (reading 3.6.2)", N36),
   ("R", RM3, N36)],
  note="0.5: a financing mechanism within reach of investment, with no isolating record")

U("OS", C36, 0.5,
  [("R", RM1 + "; a commons' rules govern its resource's yield, not the economy's productivity", OST),
   ("R", RM1, OST), ("R", RM3, OST)],
  note="0.5: resource governance; the clauses are the host's")


# =================================================================================================================
# C4.6 Harm Internalization
# =================================================================================================================
NO_PROJ = "not shown: the sources project no pollution mortality for the economy they propose (reading 4.6.1)"
NO_LIAB = "not shown: the sources state no liability of those who cause harm to those harmed (reading 4.6.2)"
NO_REG = ("not shown: the sources state no provision for the bodies that regulate food, water, air, chemicals and "
          "medicines or their independence (reading 4.6.3)")
RH1 = "out of reach: the mechanism governs no source of the pollution harms the clause counts (reading 4.6.1)"
RH2 = "out of reach: the mechanism governs no harm-causing activity's liability (reading 4.6.2)"
RH3 = "out of reach: the mechanism governs no regulator of food, water, air, chemicals or medicines (reading 4.6.3)"

U("MS", C46, 0.5,
  [("U", NO_PROJ, N46),
   ("U", NO_LIAB + "; Roemer argues that public bads such as pollution would be set lower because the rich would not "
                   "dominate the political decision, a political-economy argument, not a liability provision", N46),
   ("U", NO_REG, N46)],
  note="0.5: lower pollution argued from the distribution of profits, not provided for")

U("LM", C46, 0.5,
  [("U", NO_PROJ, LP46),
   ("U", "not shown: 'Where damages can be proven and quantified in a court of law, restitution to the injured parties "
         "must be required' (2.2), and restitution falls on the negligent wrongdoer (1.7): liability enforceable by those "
         "harmed, but limited to damages proven and quantified, with no collective or representative claim for "
         "dispersed harm stated (reading 4.6.2)", f"{LP46}; {LP26}"),
   ("S", "short: occupational and other licensing is opposed in favour of voluntary certification (2.9) and medical "
         "products 'must be freely available in the marketplace without government restrictions or licenses' (2.13): "
         "regulation of medicines, and by the same principle of food and chemicals, is abolished, not freed of influence "
         "(reading 4.6.3)", LP46)],
  note="0.5: liability in court for proven damage, with regulation replaced by voluntary certification")

U("MMT", C46, 0.5,
  [("R", RH1 + "; job-guarantee projects may include environmental remediation, public work rather than a rule on "
              "those who cause harm", N46),
   ("R", RH2, N46), ("R", RH3, N46)],
  note="0.5: an employment mechanism; the clauses are the host's")

U("UBI", C46, 0.5,
  [("R", RH1, BIEN), ("R", RH2, BIEN), ("R", RH3, BIEN)],
  note="0.5: a transfer; the clauses are the host's")

U("DG", C46, 0.5,
  [("U", NO_PROJ, N46),
   ("U", NO_LIAB + "; harmful production is to be capped, scaled down or ended (planned obsolescence) by democratic "
                   "decision (Hickel 2020, ch. 5)", N46),
   ("U", NO_REG, N46)],
  note="0.5: caps and bans on harmful production; no liability or regulatory provision")

U("SC", C46, 0.5,
  [("U", NO_PROJ + "; the stakeholder metrics ask companies to disclose emissions of fine particulates and oxides of "
                   "sulphur and nitrogen, 'a leading cause of ill-health and premature death'", WEF),
   ("U", NO_LIAB + "; the Davos Manifesto asks companies to act as 'a steward of the environmental and material "
                   "universe', with disclosure voluntary and liability left to the host's law", f"{WEF}; {N46}"),
   ("U", "not shown: companies are asked to disclose their lobbying positions and any difference from their purpose; "
         "nothing is stated for the regulators themselves (reading 4.6.3)", WEF)],
  note="0.5: voluntary disclosure of harm and lobbying; liability and regulation left to the host")

U("FALC", C46, 0.5,
  [("U", NO_PROJ, N46), ("U", NO_LIAB, N46), ("U", NO_REG, N46)],
  note="0.5: clean energy and automation projected; no liability or regulatory provision")

U("PE", C46, 0.5,
  [("U", NO_PROJ, PE46),
   ("C", "cleared: a community of affected parties decides how much of each pollutant may be emitted, the emitting "
         "council pays the damage price as a cost of production, and the affected receive credit for the damage they "
         "suffer: a compensation scheme funded by those who cause the harm, collective and controlled by those harmed "
         "(reading 4.6.2)", PE46),
   ("U", "not shown: the community of affected parties is advised by scientists in R&D units it runs, which is "
         "independence of the harmed from the harm-causers for pollution; regulation of food, water, chemicals and "
         "medicines is not addressed (reading 4.6.3)", PE46)],
  note="0.5: those harmed set and are paid for pollution; no projection, and regulation beyond pollution unstated")

U("CCO", C46, 0.5,
  [("U", NO_PROJ, CCO46),
   ("U", NO_LIAB, CCO46),
   ("U", "not shown: the CIP paper names regulatory capture (Stigler) as the problem it answers, with FDA and EPA among "
         "its examples, but provides for elected officials, campaign finance and the Judicial Guard, not for the bodies "
         "that regulate food, water, air, chemicals and medicines (reading 4.6.3)", CCO46)],
  note="0.5: anti-capture design aimed at elected and judicial office, not at regulators")

U("INT", C46, 0.5,
  [("U", NO_PROJ, INT46),
   ("U", "not shown: ecological impact signals raise the access value of harmful goods, and design constraints bar "
         "high-impact production from scaling: harm is made a cost through valuation, not liability, and no compensation "
         "of those harmed is stated (reading 4.6.2)", INT46),
   ("U", "not shown: designs pass peer review and safety analysis with thresholds set by node or federation policy, "
         "under 'collective oversight'; the reviewers' independence from producers is not stated (reading 4.6.3)",
    f"{INT46}; {INT36}")],
  note="0.5: harm priced into access values; no liability, and reviewers' independence unstated")

U("DE", C46, 0.5,
  [("U", NO_PROJ, N46),
   ("U", NO_LIAB + "; Raworth (2017, ch. 6) calls for regenerative design and taxes on pollution, not for liability", N46),
   ("U", NO_REG, N46)],
  note="0.5: regenerative design and pollution taxes urged; no liability or regulatory provision")

U("GEO", C46, 0.5,
  [("R", RH1, GEO26), ("R", RH2 + "; charges on pollution as rent for the commons are not paired with the tax in the "
                                  "design scored (extension test, decision D31)", GEO26), ("R", RH3, GEO26)],
  note="0.5: a land tax; the clauses are the host's")

U("MC", C46, 0.5,
  [("R", RH1, N46), ("R", RH2, N46), ("R", RH3, N46)],
  note="0.5: an exchange network; the clauses are the host's")

U("UBS", C46, 0.5,
  [("R", RH1 + "; it provides services, not a rule on pollution", N46), ("R", RH2, N46), ("R", RH3, N46)],
  note="0.5: service provision; the clauses are the host's")

U("SWF", C46, 0.5,
  [("R", RH1, N46),
   ("R", RH2 + "; the Council on Ethics recommends excluding companies that cause severe environmental damage, a cost "
               "through divestment, not liability to those harmed", N46),
   ("R", RH3, N46)],
  note="0.5: exclusion of harm-causers from the portfolio; the clauses are the host's")

U("IF", C46, 0.5,
  [("R", RH1, N46), ("R", RH2 + "; financing excludes prohibited activities, not harm as such", N46), ("R", RH3, N46)],
  note="0.5: a contract set; the clauses are the host's")

U("OS", C46, 0.5,
  [("U", "not shown: community-managed water systems lie within a commons' reach (unsafe water is one of the clause's "
         "harms), and no source measures their effect on mortality (reading 4.6.1)", OST),
   ("U", "not shown: graduated sanctions and local conflict-resolution arenas make a rule-breaker answer to the other "
         "users (principles 5 and 6), but the sources describe sanctions for overuse, not compensation of those harmed "
         "(reading 4.6.2)", OST),
   ("U", "not shown: monitors are the users or accountable to them (principle 4), so the regulated regulate themselves; "
         "the sources do not show the independence of those they regulate that the clause asks for (reading 4.6.3)",
    OST)],
  note="0.5: self-enforced rules for a shared resource; compensation and independence not shown")


# ---- the blind record ----------------------------------------------------------------------------------------------
def blind_table(p, cid, units):
    rows_ = ["| Unit | Class | Clause statuses | Verdict | Flag |", "|---|---|---|---|---|"]
    for (code, c) in sorted((k for k in units if k[1] == cid), key=lambda k: p.names[k[0]]):
        r = units[(code, c)]
        sts = " ".join(st for st, _, _ in r["clauses"])
        flag = f"toward {r['flag'][0].split(':')[0]}" if r["flag"] else "—"
        cls = "mechanism" if code in MECHS else "design"
        rows_.append(f"| {p.names[code]} | {cls} | {sts} | {pc.f1(r['verdict'])}"
                     f"{' (0.0 reason stated)' if r['zero'] else ''} | {flag} |")
    return "\n".join(rows_)




# ---- after the comparison (written after the checkpoint, 600c994) ------------------------------------------------
# The prior is part (2.11)'s, Session 65's stated rule: every design U U U, every mechanism R R R, each at 0.5, one
# flag (Libertarian Minarchism's C2.6, toward 1.0). No verdict differs, so nothing is reconciled (protocol 5.3). Eight
# units revise on clause statuses alone; under Session 71's rule (NEEC_BlindReview_s71.md, section 6) a blind reading
# stands unless the prior shows evidence it did not weigh, and each of the eight prior clauses states the rule ("the
# sources state no ...", "out of reach") without a source read, so all eight blind readings stand. FINAL is NEW.
STAND = {
    ("LM", C26): "clauses 2 and 3 cleared on the platform's 1.1, 2.13 and 3.2, which the prior did not read; clause 1 "
                 "stays not shown, and both readings flag toward 1.0",
    ("MMT", C26): "clause 3 is within reach because the job guarantee is an employment whose loss could penalise "
                  "refusal (reading 2.6.4); the sources are silent, so not shown",
    ("UBS", C26): "clauses 2 and 3 are within reach because health care is one of the mechanism's seven services "
                  "(readings 2.6.3, 2.6.4); the proposal is silent, so not shown",
    ("SC", C36): "clauses 1 and 2 cleared on the market economies' 1999-2019 record (reading 3.6.1), which the prior "
                 "did not calibrate against",
    ("IF", C36): "clauses 1 and 2 are within reach because generalised profit-and-loss sharing allocates all external "
                 "finance (reading 3.6.2); no record isolates the mechanism, so not shown",
    ("LM", C46): "clause 3 short on the platform's 2.9 and 2.13 (regulation of medicines abolished for voluntary "
                 "certification), which the prior did not read",
    ("OS", C46): "the three clauses are within reach for community-managed water and other commons, whose rules, "
                 "sanctions and monitors are the mechanism's own (Ostrom's principles 4 to 6); not shown on the sources",
    ("PE", C46): "clause 2 cleared on the community of affected parties' procedure, which the prior did not read",
}
FINAL = {k: dict(v) for k, v in NEW.items()}


def prior_units():
    """Part (2.11)'s readings of the 51 units (rescoring_s65.NEW_UNITS: the three class N criteria are not in the
    pass's merged units, which hold the 26 published criteria)."""
    with redirect_stdout(io.StringIO()):
        import rescoring_s65 as r65
    return {k: r65.NEW_UNITS[k] for k in NEW}


def comparison_table(p, prior, units, cid):
    pk = {k: v for k, v in prior.items() if k[1] == cid}
    uk = {k: v for k, v in units.items() if k[1] == cid}
    res, tally = br.compare_group(pk, uk)
    rows_ = ["| Unit | Prior | Blind (Session 76) | Result | Differences |", "|---|---|---|---|---|"]
    for (code, c) in sorted(res, key=lambda k: p.names[k[0]]):
        agree, diffs = res[(code, c)]
        pr, nw = pk[(code, c)], uk[(code, c)]
        ps = " ".join(st for st, _, _ in pr["clauses"]) + " / " + pc.f1(pr["verdict"])
        ns = " ".join(st for st, _, _ in nw["clauses"]) + " / " + pc.f1(nw["verdict"])
        kind = "agree" if agree else ("revise (verdict)" if pr["verdict"] != nw["verdict"] else "revise (clauses)")
        rows_.append(f"| {p.names[code]} | {ps} | {ns} | {kind} | {'; '.join(diffs) if diffs else '—'} |")
    return "\n".join(rows_), res, tally


def earlier_changes(p):
    """Sessions 71's to 75's final verdict changes (blind_s75.earlier_changes() with blind_s75.FINAL and FIRST_FINAL)
    against their priors."""
    import blind_s75 as b75
    with redirect_stdout(io.StringIO()):
        out = b75.earlier_changes(p)
    pr = b75.prior_units(p)
    for fin in (b75.FINAL, b75.FIRST_FINAL):
        out.update({k: (pr[k]["verdict"], u["verdict"]) for k, u in fin.items() if pr[k]["verdict"] != u["verdict"]})
    return out


def standings(changes):
    import blind_s75 as b75
    return b75.standings(changes)


def consequence_table(p, prior, units):
    """This group's verdict changes (none) on top of Sessions 71's to 75's final ones, on the 29."""
    mine = {k: (prior[k]["verdict"], u["verdict"]) for k, u in units.items() if prior[k]["verdict"] != u["verdict"]}
    v2, base = standings({})
    _, both = standings({**earlier_changes(p), **mine})
    held = all(v2[k[0]]["vector"][k[1]] == prior[k]["verdict"] for k in prior)
    lines = ["| Entry | Total on 29 | After Sessions 71 to 76 | Failures | After | Tier after |",
             "|---|---:|---:|---:|---:|---|"]
    for code in v2:
        if both[code] != base[code]:
            lines.append(f"| {v2[code]['display_name']} | {base[code][0]:.1f} | {both[code][0]:.1f} | {base[code][1]} | "
                         f"{both[code][1]} | {pc.tier(both[code][1])} |")
    top = max(t for t, _, _ in both.values())
    first = " and ".join(sorted(v2[c]["display_name"] for c, (t, _, _) in both.items() if t == top))
    tiers = [(v2[c]["display_name"], tr, pc.tier(f)) for c, (t, f, tr) in both.items() if pc.tier(f) != tr]
    return "\n".join(lines), held, (first, top), tiers, mine, both


def flag_effects(p, units, both):
    """Each flag's alternative taken alone, on top of all six groups' final verdicts."""
    lines = ["| Unit | Criterion | Final | Flag toward | Total on 29 then | Failures then | Tier then | Changes |",
             "|---|---|---:|---:|---:|---:|---|---|"]
    movers = []
    for (code, cid) in sorted((k for k in units if units[k]["flag"]), key=lambda k: (k[1], p.names[k[0]])):
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
    rec = os.path.join(HERE, "NEEC_BlindReview_s76.md")
    if not os.path.isfile(rec):
        return ok_print(False, "NEEC_BlindReview_s76.md exists", "missing")
    text = open(rec, encoding="utf-8").read()
    missing = [name for name, t in tables if t not in text]
    return ok_print(not missing, "NEEC_BlindReview_s76.md carries every generated table verbatim (" +
                    ", ".join(name for name, _ in tables) + ")", ", ".join(missing))


def main():
    ok = True

    def ok_print(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    print("blind_s76.py -- the blind re-read of C2.6, C3.6 and C4.6 for the 17 designs and mechanisms (ledger S59)")
    with redirect_stdout(io.StringIO()):
        p = pc.Pass()
    print("inputs: blind_review.py, pass_common.py and its parts, neec_corpus_v2_s65_snapshot.json, " + ", ".join(sorted(READ)) + "\n")

    print("[1] the readings are complete and follow the rules")
    corpus = {e["code"]: e["scope_class"] for e in json.load(open(path("neec_corpus_v2_s65_snapshot.json"), encoding="utf-8"))["entries"]}
    ok_print({c for c, s in corpus.items() if s == "comprehensive_system"} == set(DESIGNS),
             "the nine designs are the corpus's comprehensive systems")
    ok_print({c for c, s in corpus.items() if s == "mechanism"} == set(MECHS), "the eight mechanisms are the corpus's mechanisms")
    want = {(c, cid) for c in DESIGNS + MECHS for cid in (C26, C36, C46)}
    ok_print(set(NEW) == want and len(want) == 51, "one blind reading for each of the 51 units (17 entries, three "
             "criteria), no more", str(sorted(set(NEW) ^ want)))
    pc.check_records(p, NEW, ok_print)
    pc.check_rule(NEW, ok_print)
    ok_print(all(r["flag"] is None or r["flag"][0][:3] in ("0.0", "0.5", "1.0") and r["flag"][0][:3] !=
                 pc.f1(r["verdict"]) for r in NEW.values()), "each flag names an alternative score other than the verdict")
    bad = [k for k in sorted(NEW) if len(br.blind_view(p, k)["clauses_v2"]) != len(NEW[k]["clauses"])]
    ok_print(not bad, "each reading has one status per clause blind_view shows", str(bad))
    for cid, ec in ((C26, E26), (C36, E36), (C46, E46)):
        listed = {ec + f for f in br.blind_view(p, ("MS", cid))["cache_files"]} - LATER
        ok_print(listed <= set(READ), f"every file blind_view lists for {cid} is one this script reads or names",
                 str(sorted(listed - set(READ))))
    ok_print(all(os.path.isfile(path(f)) for f in READ), "every file in READ exists")
    ok_print(not [k for k, u in NEW.items() if k[0] in MECHS and u["verdict"] == 0.0],
             "no mechanism is at 0.0 (Session 73's class observation: a mechanism that governs no clause's quantity "
             "is held at 0.5)")
    ok_print(all(u["verdict"] != 1.0 for u in NEW.values() if any(st == "R" for st, _, _ in u["clauses"])),
             "no reading with a clause out of reach is above 0.5 (D28(c))")
    ok_print(all(st != "R" for k, u in NEW.items() if k[0] in DESIGNS for st, _, _ in u["clauses"]),
             "no design's clause is out of reach (reach is a mechanism's rule, protocol 3.2)")

    print("\n[2] the figures the readings quote, recomputed from the cache")
    for k, v in FIG_PRINT.items():
        print(f"    {k}: {v}")
    ok_print(all(lp >= 0 and tfp >= 0 for lp, tfp in REC.values()),
             "output per hour and TFP non-declining over 1999-2019 in each of the four market economies reading 3.6.1 "
             "calibrates against")

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
          "checkpoint, 600c994)")
    prior = prior_units()
    ok_print(set(prior) == set(NEW), "part (2.11) holds a reading of each of the 51 units")
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
    ok_print(not vd, "no verdict differs: nothing to reconcile (protocol 5.3)", str(vd))
    ok_print(set(STAND) == set(revised), "every clause revision has its stated reason for standing (Session 71's rule)",
             str(sorted(set(STAND) ^ set(revised))))
    ok_print(all(all(st == ("R" if k[0] in MECHS else "U") for st, _, _ in prior[k]["clauses"]) for k in prior),
             "the prior is Session 65's stated rule throughout: every design not shown on each clause, every "
             "mechanism out of reach on each")

    print("\n[5] the final readings (FINAL: the blind readings, unchanged)")
    ok_print(FINAL == NEW, "FINAL is the blind readings as recorded at the checkpoint")
    pc.check_records(p, FINAL, ok_print)
    pc.check_rule(FINAL, ok_print)
    ok_print(not [k for k in FINAL if k[0] == "CCO" and FINAL[k]["verdict"] != prior[k]["verdict"]],
             "no CCO-PTF-CIP-SZH verdict changes (decisions 57.2, 69.4: a rise is applied, a fall held)")

    print("\n[6] consequences once applied (by generator in ledger S61, not here), with Sessions 71 to 75")
    t_cons, held, (fn, ft), tiers, mine, both = consequence_table(p, prior, FINAL)
    ok_print(held, "neec_corpus_v2_s65_snapshot.json carries the prior's verdict for each of the 51 units (the published "
             "provisional scores are the prior's)")
    ok_print(not mine, "this group changes no verdict")
    print(t_cons)
    print(f"\nfirst place on the 29 after Sessions 71 to 76: {fn} at {ft:.1f}")
    print("tier changes after Sessions 71 to 76: " + ("; ".join(f"{n} {a} to {b}" for n, a, b in tiers) or "none"))
    t_flags, movers = flag_effects(p, FINAL, both)
    print(f"\nthe final readings' {sum(1 for u in FINAL.values() if u['flag'])} flags, each taken alone (on all six "
          "groups' final verdicts):")
    print(t_flags)
    print("flags that would change a tier or first place: " + (", ".join(f"{p.names[c]} {cid}" for c, cid in movers)
                                                                or "none"))

    print("\n[7] the record")
    names = (C26, C36, C46)
    record_check([(f"readings, {n}", t) for n, t in zip(names, btables)] +
                 [(f"comparison, {n}", t) for n, t in zip(names, cmp_tables)] +
                 [("consequences", t_cons), ("flag effects", t_flags)], ok_print)
    print("\nBLIND RE-READ OF C2.6, C3.6 AND C4.6 (17 DESIGNS AND MECHANISMS) CHECKED." if ok
          else "\nBLIND RE-READ: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
