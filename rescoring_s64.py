#!/usr/bin/env python3
"""
rescoring_s64.py -- NEEC rescoring pass, stage 2, group 2.10: C4.2 Ecological Compliance, class M
=====================================================================================================
Session 64. The 16 units of C4.2 the pass had not re-estimated (part (b7) read the seven published 1.0s, each to 0.5) are
re-read clause by clause against v2.0's text (criteria.json; NEEC_Criteria_v2_s45.md, Appendix V): consumption-based
CO2 emissions falling at least 3.8% a year (the rate of a 35% cut over 2019-2030), biodiversity neutral or positive (the
IUCN Red List Index, SDG indicator 15.5.1), the ecological footprint of consumption per person no greater than world
biocapacity per person, and no more than two of the four nationally downscaled planetary boundaries transgressed.
Part (b7) set the readings applied to designs and mechanisms (its readings 3.3 and 3.4); this group reads the eight 0.5s
and eight 0.0s, the four configured national economies (Status Quo, China, Singapore, Qatar) and the four Nordic countries
Nordic Social Democracy is read on (Denmark, Finland, Norway, Sweden) on the accounts v2.0 names, republished by Our World
in Data. Readings: NEEC_Rescoring_s64.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry not yet re-estimated on C4.2, each against its published score; which rise, fall or
      hold; the 0.0s and their reasons; that none is 1.0
  [2] the evidence cache (evidence_cache/C4.2/): each file by digest, rows quoted found, each unit's published
      rationale located where this script puts it, at its published score
  [3] the rates and Red List Index changes the readings quote, recomputed from the cache
  [4] the flags, and which could change a tier

Usage: python3 rescoring_s64.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, the files of evidence_cache/C4.2/,
                                             the scoring documents holding the units' rationales, NEEC_Rescoring_s64.md;
                                             writes nothing)
       python3 rescoring_s64.py --tables   (prints the generated tables as JSON, for the record)
Prints file names and summaries only. Deterministic.
"""
import csv
import hashlib
import io
import json
import os
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD, CRIT = "(2.10)", "NEEC_Rescoring_s64.md", "C4.2"
CACHE = "evidence_cache/C4.2/"
UNITS = {}
GENERATED = {}


def U(code, verdict, c1, c2, c3, c4, flag=None, note="", zero=None):
    """One unit of C4.2. c1..c4: (status, estimate, source) for the four v2.0 clauses. flag: (alternative, reading).
    zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[c1, c2, c3, c4], flag=flag, note=note, zero=zero)


# ---- the cache (written by Session 64; md5s as written by evidence_cache_s64.py) ---------------------------------------
MD5 = {"owid_gcb_consumption_co2.csv": "2f771097baac251ca01fcae8e81cc630",
       "owid_iucn_red_list_index.csv": "c16141c8b0a74db8a81411f74d09ef34"}
QUOTES = {"owid_gcb_consumption_co2.csv": ["Entity,Code,Year,Annual consumption-based CO", "United States,USA,2023,",
                                           "Singapore,SGP,2023,", "Qatar,QAT,2023,"],
          "owid_iucn_red_list_index.csv": ["Entity,Code,Year,Red List Index", "United States,USA,2025,0.82",
                                           "Finland,FIN,2025,0.98"]}
# the published rationales: (file, line of the C4.2 heading)
RAT = {"SQ": ("NEEC_Report_v1_6.md", 332), "NSD": ("NEEC_Report_v1_6.md", 420), "CPS": ("NEEC_Report_v1_6.md", 510),
       "MS": ("NEEC_Report_v1_6.md", 600), "LM": ("NEEC_Report_v1_6.md", 690), "UBI": ("NEEC_Report_v1_6.md", 870),
       "SC": ("NEEC_Report_v1_6.md", 1050), "GEO": ("NEEC_Report_v1_6.md", 1502), "MC": ("NEEC_Report_v1_6.md", 1592),
       "UBS": ("NEEC_UniversalBasicServices_scoring_scratch.md", 572),
       "SWF": ("NEEC_SovereignWealthFundStatism_scoring_scratch.md", 514),
       "CN": ("NEEC_StateCapitalism_China_scoring_scratch.md", 716),
       "SG": ("NEEC_StateCapitalism_Singapore_scoring_scratch.md", 653),
       "QA": ("NEEC_StateCapitalism_Qatar_scoring_scratch.md", 727),
       "IF": ("NEEC_IslamicFinance_scoring_scratch.md", 523), "OS": ("NEEC_Ostrom_Commons_scoring_scratch.md", 559)}


# ---- the rates, computed from the cache (readings 3.1 to 3.4) ---------------------------------------------------------
def load(name):
    d = {}
    path = os.path.join(HERE, CACHE, name)
    if not os.path.isfile(path):
        return d
    for r in csv.DictReader(open(path, encoding="utf-8")):
        d.setdefault(r["Entity"], {})[int(r["Year"])] = float(list(r.values())[3])
    return d


CO2 = load("owid_gcb_consumption_co2.csv")
RLI = load("owid_iucn_red_list_index.csv")
BAR = 100.0 * (1.0 - 0.65 ** (1.0 / 11.0))     # the annual fall that a 35% cut over 2019-2030 is, in percent


def rate(e, y0, y1):
    """Compound annual rate of change of consumption-based CO2, percent a year."""
    s = CO2[e]
    return 100.0 * ((s[y1] / s[y0]) ** (1.0 / (y1 - y0)) - 1.0)


def last(e):
    return max(CO2[e])


def r3(e):
    """The three windows: 2019 to the latest year of the accounts, ten years back from it, and 2007 to it."""
    y1 = last(e)
    return rate(e, 2019, y1), rate(e, y1 - 10, y1), rate(e, 2007, y1) if 2007 in CO2[e] else None


def f1(x):
    return f"{x:.1f}"


def sg(x):
    return f"{x:+.1f}"


def rli(e):
    return RLI[e][2015], RLI[e][2025]


def fig(e):
    a, b, c = r3(e)
    return (f"{sg(a)}% a year over 2019-{last(e)}, {sg(b)}% over {last(e) - 10}-{last(e)}"
            + (f", {sg(c)}% over 2007-{last(e)}" if c is not None else ""))


def red(e):
    a, b = rli(e)
    return f"{a:.2f} in 2015, {b:.2f} in 2025"


# ---- sources ---------------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
GCB = ("Global Carbon Budget national consumption-based CO2 accounts (Friedlingstein et al.), as republished by Our World "
       "in Data, chart consumption-co2-emissions (" + CACHE + "owid_gcb_consumption_co2.csv, retrieved 2026-10-15)")
IUCN = ("IUCN Red List Index (the indicator SDG 15.5.1 reports), as republished by Our World in Data, chart "
        "red-list-index (" + CACHE + "owid_iucn_red_list_index.csv, retrieved 2026-10-15)")
NOFP = ("the ecological footprint of consumption per person against world biocapacity per person (National Footprint and "
        "Biocapacity Accounts) was not reachable: data.footprintnetwork.org's API answered HTTP 403 and no open "
        "republication was located, so the clause is not shown (reading 3.8)")
NOBND = ("the nationally downscaled boundaries (O'Neill et al. 2018; Fanning et al. 2022) were not located as a table "
         "for this economy, so the count of boundaries transgressed is not shown (reading 3.8)")
NOPROJ1 = ("no projection of consumption-based CO2 under the system, from a model or calibrated components, is stated or "
           "located, so the rate is not shown (part (b7), reading 3.4)")
NOPROJ2 = ("no projection of pressure on species and habitat under the system is stated or located (part (b7), "
           "reading 3.3)")
NOPROJ3 = "no projection of the system's footprint per person against biocapacity is stated or located"
NOPROJ4 = "no projection of the system's pressure on phosphorus, nitrogen, freshwater or land system is stated or located"

# ---- the units (readings in NEEC_Rescoring_s64.md, section 3) -------------------------------------------------------
BARTXT = f"the bar is a fall of {f1(BAR)}% a year (a 35% cut over 2019-2030)"
US1 = f"United States, consumption-based CO2: {fig('United States')}; {BARTXT}; the world's rose {sg(r3('World')[0])}% a year over 2019-{last('World')} (reading 3.3)"
US2 = f"United States, Red List Index {red('United States')}: declining (reading 3.3)"
CN1 = f"China, consumption-based CO2: {fig('China')}: rising; {BARTXT} (reading 3.3)"
CN2 = f"China, Red List Index {red('China')}: declining (reading 3.3)"
SG1 = (f"Singapore, consumption-based CO2: {fig('Singapore')}: the sign depends on the window, and neither reaches the "
       f"bar of {f1(BAR)}% (reading 3.3)")
SG2 = f"Singapore, Red List Index {red('Singapore')}: declining (reading 3.3)"
QA1 = f"Qatar, consumption-based CO2: {fig('Qatar')}: rising; {BARTXT} (reading 3.3)"
QA2 = f"Qatar, Red List Index {red('Qatar')}: declining (reading 3.3)"
NORD = ["Denmark", "Finland", "Norway", "Sweden"]
NSD1 = ("consumption-based CO2, 2019-2023 and 2013-2023 (% a year): " +
        "; ".join(f"{e} {sg(r3(e)[0])} and {sg(r3(e)[1])}" for e in NORD) +
        f"; the bar is {f1(BAR)}%: Finland and Norway reach it on the window that includes 2020's fall, none on the "
        "ten-year window, and Denmark and Sweden reach it on neither, so the economy-wide clause is short (reading 3.4)")
NSD2 = ("Red List Index, 2015 and 2025: " + "; ".join(f"{e} {rli(e)[0]:.2f} and {rli(e)[1]:.2f}" for e in NORD) +
        ": unchanged in all four to the index's two decimals, so non-declining over the window (reading 3.4); the index "
        "covers the species occurring in the country, not the pressure its consumption puts on species elsewhere")


def S(est, src):
    return est, src


U("SQ", 0.0, ("S", US1, f"{GCB}; {REP}SQ C4.2"), ("S", US2, f"{IUCN}; {REP}SQ C4.2"),
  ("U", NOFP, f"{REP}SQ C4.2"), ("U", NOBND, f"{REP}SQ C4.2"),
  zero="the best evidence shows performance far below the threshold with no credible pathway under the system's own logic "
       "(protocol 2.1): consumption-based emissions fell about a fifth of the bar's rate, and the published account "
       "(efficiency gains offset by scale, a growth imperative) is the 0.0 band's own description; a fall of this size "
       "is the system's best case, not a pathway to the bar",
  note="0.0 holds")
U("NSD", 0.5, ("S", NSD1, f"{GCB}; {REP}NSD C4.2"), ("C", NSD2, f"{IUCN}; {REP}NSD C4.2"),
  ("U", NOFP, f"{REP}NSD C4.2"), ("U", NOBND, f"{REP}NSD C4.2"),
  note="0.5 holds: the published account (leading renewable and environmental policy, absolute reductions not "
       "achieved) is the 0.5 band's, and the measure bears it out for two of the four countries on one window; "
       "the only clause cleared in the group, and one clause cleared never makes 1.0 (reading 3.4)")
U("CPS", 0.5, ("U", "no consumption-based account exists for the planned economies of the record (the accounts begin in 1990, "
                    "after the Soviet system's end); " + NOPROJ1, f"{REP}CPS C4.2"),
  ("U", NOPROJ2 + "; the record's Aral Sea and pollution disasters are damage, not a level of the index", f"{REP}CPS C4.2"),
  ("U", NOPROJ3, f"{REP}CPS C4.2"), ("U", NOPROJ4, f"{REP}CPS C4.2"),
  flag=("0.0: weighting the published account (ecological limits disregarded wherever growth was prioritised) as the "
        "0.0 band's growth imperative with no pathway under the system's own logic; the entry's 0.5 rests on lower "
        "per-capita consumption, which the entry itself says was not due to sustainability principles", "3.5"),
  note="0.5 holds on the published account (reading 3.5); flagged")
U("MS", 0.5, ("U", NOPROJ1, f"{REP}MS C4.2"), ("U", NOPROJ2, f"{REP}MS C4.2"), ("U", NOPROJ3, f"{REP}MS C4.2"),
  ("U", NOPROJ4, f"{REP}MS C4.2"),
  flag=("0.0: weighting the entry's own limit, that market competition bounds how much a cooperative can sacrifice "
        "competitiveness for ecology, as a growth imperative the mechanism leaves in place; it could change the "
        "entry's tier", "3.5"),
  note="0.5 holds: democratic control over firms is a mechanism that can subordinate profit to ecology and some "
       "cooperatives use it, and the entry records its limit, the 0.5 band's description (reading 3.5); flagged")
U("LM", 0.0, ("U", "no ecological constraint exists in the system's logic, so no rate is to be read; " + NOPROJ1,
              f"{REP}LM C4.2"), ("U", NOPROJ2, f"{REP}LM C4.2"), ("U", NOPROJ3, f"{REP}LM C4.2"),
  ("U", NOPROJ4, f"{REP}LM C4.2"),
  zero="the system excludes the criterion's concern (protocol 2.1): its own logic confines the state to protecting "
       "rights and rules out the regulatory constraint on extraction and emission that the criterion measures, as the "
       "published account says (externalities unaddressed, private property rights insufficient against a commons)",
  note="0.0 holds (reading 3.6)")
U("UBI", 0.5, ("U", "a transfer raises household consumption; whether the emissions rise depends on what funds it and on "
               "complementary policy, as the entry says; " + NOPROJ1, f"{REP}UBI C4.2"),
  ("U", NOPROJ2, f"{REP}UBI C4.2"), ("U", NOPROJ3, f"{REP}UBI C4.2"), ("U", NOPROJ4, f"{REP}UBI C4.2"),
  flag=("0.0: weighting the transfer's consumption effect as a growth imperative with no ecological mechanism of its "
        "own, a carbon tax being a funding choice the design does not fix", "3.5"),
  note="0.5 holds: the entry's two-sided account (consumption effect against a possible carbon-tax funding) is the 0.5 "
       "band's second description; a mechanism that bears on the criterion without fixing its direction (reading 3.5); "
       "flagged")
U("SC", 0.0, ("U", "ESG metrics report relative improvements (intensity) and net-zero pledges lean on offsets; no "
              "absolute rate attributable to the mechanism is located; " + NOPROJ1, f"{REP}SC C4.2"),
  ("U", NOPROJ2, f"{REP}SC C4.2"), ("U", NOPROJ3, f"{REP}SC C4.2"), ("U", NOPROJ4, f"{REP}SC C4.2"),
  zero="far below the threshold with no credible pathway under the system's own logic (protocol 2.1): relative and "
       "efficiency metrics substitute for absolute ones, the 0.0 band's own text, for which this unit is the band's "
       "example",
  note="0.0 holds (reading 3.6)")
U("GEO", 0.5, ("U", NOPROJ1, f"{REP}GEO C4.2"), ("U", NOPROJ2, f"{REP}GEO C4.2"), ("U", NOPROJ3, f"{REP}GEO C4.2"),
  ("U", "land-use taxation is linked to construction-land carbon-emission efficiency in a 30-province study and "
        "densification is an abatement lever, a channel for the land-system boundary; no downscaled count follows; "
        + NOPROJ4, f"{REP}GEO C4.2"),
  note="0.5 holds: an actively studied causal channel with no hard ecological ceiling, the 0.5 band (reading 3.5)")
U("MC", 0.5, ("U", NOPROJ1, f"{REP}MC C4.2"), ("U", NOPROJ2, f"{REP}MC C4.2"), ("U", NOPROJ3, f"{REP}MC C4.2"),
  ("U", NOPROJ4, f"{REP}MC C4.2"),
  note="0.5 holds: a consistent value for local exchange that structurally cannot fund long-distance supply chains, "
       "with no quantified effect and no ceiling (reading 3.5)")
U("UBS", 0.5, ("U", "the closest precedent, Luxembourg's fare-free public transport (2020), cut road-transport CO2 by about "
               "5.9% in a synthetic difference-in-differences study: a sector's level once, not a consumption-based "
               "annual rate for an economy; " + NOPROJ1, "NEEC_UniversalBasicServices_scoring_scratch.md, C4.2"),
  ("U", NOPROJ2, "NEEC_UniversalBasicServices_scoring_scratch.md, C4.2"),
  ("U", NOPROJ3, "NEEC_UniversalBasicServices_scoring_scratch.md, C4.2"),
  ("U", NOPROJ4, "NEEC_UniversalBasicServices_scoring_scratch.md, C4.2"),
  note="0.5 holds: a quantified, causally designed finding of partial reach (reading 3.5)")
U("SWF", 0.0, ("U", "the exemplars' revenue is fossil-fuel extraction and Norway expanded licensing in 2026; the fund's "
                    "exclusions govern what it holds, not the economy's emissions (part (b6), reading 3.6); "
                    + NOPROJ1, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2"),
  ("U", NOPROJ2, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2"),
  ("U", NOPROJ3, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2"),
  ("U", NOPROJ4, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C4.2"),
  zero="the system excludes the criterion's concern (protocol 2.1): the mechanism's own funding is continued fossil-fuel "
       "extraction, which the criterion constrains, so the mechanism depends on what the criterion requires it to end",
  flag=("0.5: crediting the fund's own conduct (coal, tar-sands and oil-sands exclusions, a spending rule) as partial "
        "mitigation and not crediting the host economy's extraction to the mechanism (protocol 3.2); it could change "
        "the entry's tier", "3.6"),
  note="0.0 holds (reading 3.6); flagged")
U("CN", 0.0, ("S", CN1, f"{GCB}; NEEC_StateCapitalism_China_scoring_scratch.md, C4.2"),
  ("S", CN2, f"{IUCN}; NEEC_StateCapitalism_China_scoring_scratch.md, C4.2"),
  ("U", NOFP, "NEEC_StateCapitalism_China_scoring_scratch.md, C4.2"),
  ("U", NOBND, "NEEC_StateCapitalism_China_scoring_scratch.md, C4.2"),
  zero="far below the threshold with no credible pathway under the system's own logic (protocol 2.1): consumption-based "
       "emissions are rising, the operative targets have been relative (an intensity cut of 18% was targeted and about "
       "12% achieved), and the index is falling",
  flag=("0.5: the published flag kept: weighting the scale of renewable deployment and the announced absolute targets "
        "as a credible pathway", "3.3"),
  note="0.0 holds; the published flag kept (reading 3.3)")
U("SG", 0.0, ("S", SG1, f"{GCB}; NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2"),
  ("S", SG2, f"{IUCN}; NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2"),
  ("U", NOFP, "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2"),
  ("U", NOBND, "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C4.2"),
  zero="far below the threshold with no credible pathway under the system's own logic (protocol 2.1): consumption-based "
       "emissions are up since 2019 and the decade's fall is under the bar, the index is falling, and the 2030 target "
       "path rises on the entry's own account (Climate Action Tracker: highly insufficient)",
  flag=("0.5: the published flag kept: weighting the ten-year fall in consumption-based emissions and the carbon tax "
        "as a credible pathway", "3.3"),
  note="0.0 holds; the published flag kept (reading 3.3)")
U("QA", 0.0, ("S", QA1, f"{GCB}; NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2"),
  ("S", QA2, f"{IUCN}; NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2"),
  ("U", NOFP, "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2"),
  ("U", NOBND, "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C4.2"),
  zero="far below the threshold with no credible pathway under the system's own logic (protocol 2.1): the highest "
       "per-capita emitter in the world on the entry's figures, consumption-based emissions rising, a rent system "
       "funded by hydrocarbon exports, no carbon price, and a pledge against an unpublished baseline",
  note="0.0 holds (reading 3.3)")
U("IF", 0.0, ("U", "proceeds-use labels (green sukuk, a grant scheme, value-based intermediation) direct capital to better "
              "projects without a cap on the total; " + NOPROJ1, "NEEC_IslamicFinance_scoring_scratch.md, C4.2"),
  ("U", NOPROJ2, "NEEC_IslamicFinance_scoring_scratch.md, C4.2"),
  ("U", NOPROJ3, "NEEC_IslamicFinance_scoring_scratch.md, C4.2"),
  ("U", NOPROJ4, "NEEC_IslamicFinance_scoring_scratch.md, C4.2"),
  zero="far below the threshold with no credible pathway under the system's own logic (protocol 2.1): the mechanism's "
       "ecological instruments are allocative labels, none constrains the total, the 0.0 band's relative-for-absolute "
       "substitution that the corpus records against Stakeholder Capitalism",
  note="0.0 holds; the published entry did not flag it (reading 3.6)")
U("OS", 0.5, ("R", "a global test: Ostrom's own statement is that the design principles are for local commons of bounded "
              "scale, and a consumption-based national rate is outside the mechanism's reach; " + NOPROJ1,
              "NEEC_Ostrom_Commons_scoring_scratch.md, C4.2"),
  ("U", NOPROJ2 + "; well-evidenced local yields are not the index", "NEEC_Ostrom_Commons_scoring_scratch.md, C4.2"),
  ("U", "sustained yield of a managed local resource is the mechanism's definition of success and is well evidenced, "
        "but it is not a national footprint per person against biocapacity",
   "NEEC_Ostrom_Commons_scoring_scratch.md, C4.2"),
  ("R", "the nationally downscaled boundaries are a global test and a local commons governs one resource, so the count "
        "is outside the mechanism's reach", "NEEC_Ostrom_Commons_scoring_scratch.md, C4.2"),
  note="0.5 holds: the 0.5 band's meaningful mitigation, with two clauses out of reach by the mechanism's own scale "
       "(reading 3.5)")

EXPECT = {"rise": [], "fall": [], "zero": ["SQ", "LM", "SC", "SWF", "CN", "SG", "QA", "IF"], "ones": [],
          "cleared": ["NSD"], "short": ["CN", "NSD", "QA", "SG", "SQ"],
          "flags": {"CPS": "3.5", "MS": "3.5", "UBI": "3.5", "SWF": "3.6", "CN": "3.3", "SG": "3.3"},
          "tier": ["MS", "SWF"],
          "before": ["MMT", "DG", "FALC", "PE", "CCO", "INT", "DE"]}


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    with redirect_stdout(io.StringIO()):
        idx = [t for t, _, _, _ in pc.PARTS].index(TAG)
        p = pc.Pass(upto=idx)
    print(f"NEEC rescoring pass, stage 2, group 2.10: C4.2 Ecological Compliance, class M ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{len(MD5)} files of {CACHE}, the scoring documents holding the units' rationales, {RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(sorted(set(p.part_of[(c, CRIT)] for c in before)))}) and are "
          "not re-read")
    d = p.v2[CRIT]["definition"]
    check(p.v2[CRIT]["revision"]["cls"] == "M" and len(d["clauses"]) == 4 and "35% cut over 2019" in d["measurement"]
          and "Red List Index" in d["measurement"] and "no more than two of the four" in d["clauses"][3],
          f"{CRIT} is class M with four clauses in v2.0: consumption-based carbon falling at least 3.8% a year, "
          "biodiversity, footprint against biocapacity, no more than two of four boundaries transgressed")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group raises {len(rise)}, lowers {len(fall)} and holds {len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 for c in zeros)
          and [c for c in zeros if pub[c] == 0.0] == zeros,
          f"{len(zeros)} units are 0.0, each on a stated whole-criterion reason (protocol 2.1), each as published")
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    after1 = [c for c in p.order if (UNITS.get((c, CRIT)) or p.merged.get((c, CRIT)) or {}).get("verdict") == 1.0]
    check(ones == EXPECT["ones"] and not after1,
          f"no unit clears all four clauses, so none is 1.0; after this group no entry is at 1.0 on {CRIT}")
    st = [s for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"]]
    cleared = sorted({c for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"] if s == "C"})
    short = sorted({c for c in mine for s, _, _ in UNITS[(c, CRIT)]["clauses"] if s == "S"})
    check(set(st) <= {"U", "S", "C", "R"} and cleared == EXPECT["cleared"] and short == EXPECT["short"],
          f"{st.count('C')} clause cleared ({', '.join(cleared)}), {st.count('S')} short on the accounts "
          f"({', '.join(short)}), {st.count('R')} out of reach, {st.count('U')} not shown")

    print(f"\n[2] THE CACHE ({CACHE}) AND THE PUBLISHED RATIONALES")
    for name, want in MD5.items():
        path = os.path.join(HERE, CACHE, name)
        raw = open(path, "rb").read() if os.path.isfile(path) else b""
        txt = raw.decode("utf-8")
        lost = [q for q in QUOTES.get(name, []) if q not in txt]
        check(hashlib.md5(raw).hexdigest() == want and not lost,
              f"{name}: md5 {want[:8]}, {len(QUOTES.get(name, []))} passage(s) quoted found", ", ".join(lost))
    bad = []
    for c in mine:
        f, n = RAT[c]
        lines = open(os.path.join(HERE, f), encoding="utf-8").read().split("\n")
        head = lines[n - 1].lstrip("# *")
        if not head.startswith(f"C4.2 Ecological Compliance: {pc.f1(pub[c])}"):
            bad.append(c)
    check(sorted(RAT) == sorted(mine) and not bad,
          f"each of the {len(mine)} published rationales is at the line held here, headed with its published score",
          ", ".join(bad))

    print("\n[3] THE RATES AND INDEX CHANGES THE READINGS QUOTE (recomputed from the cache)")
    bar = 100.0 * (1.0 - 0.65 ** (1 / 11))
    check(abs(bar - 3.84) < 0.01 and 3.8 < bar, f"the bar: a 35% cut over 2019-2030 is {bar:.2f}% a year, the 3.8% v2.0 states")
    us, cn, sgp, qa = (r3(e) for e in ("United States", "China", "Singapore", "Qatar"))
    check(-bar < us[0] < 0 and -bar < us[1] < 0 and -bar < us[2] < 0 and all(x > 0 for x in cn[:1] + cn[1:2])
          and all(x is None or x > 0 for x in qa[:1]) and sgp[0] > 0 and -bar < sgp[1] < 0,
          f"United States falls on all three windows but under the bar ({sg(us[0])}, {sg(us[1])}, {sg(us[2])}); China "
          f"rises ({sg(cn[0])}, {sg(cn[1])}); Qatar rises ({sg(qa[0])}, {sg(qa[1])}); Singapore {sg(sgp[0])} and "
          f"{sg(sgp[1])}")
    nord = {e: r3(e) for e in NORD}
    reach_a = sorted(e for e in NORD if nord[e][0] <= -bar)
    reach_b = sorted(e for e in NORD if nord[e][1] <= -bar)
    check(reach_a == ["Finland", "Norway"] and not reach_b,
          f"Nordic countries: {', '.join(reach_a)} reach the bar over 2019-2023, none over 2013-2023")
    drop = [e for e in ("United States", "China", "Singapore", "Qatar", "World") if rli(e)[1] < rli(e)[0]]
    flat = [e for e in NORD if rli(e)[1] >= rli(e)[0] and all(RLI[e][y] >= RLI[e][2015] for y in range(2015, 2026))]
    check(len(drop) == 5 and flat == NORD,
          "Red List Index, 2015 to 2025: United States, China, Singapore, Qatar and the world decline; Denmark, Finland, "
          "Norway and Sweden do not")
    check(f1(BAR) in UNITS[("SQ", CRIT)]["clauses"][0][1] and sg(us[0]) in UNITS[("SQ", CRIT)]["clauses"][0][1]
          and sg(sgp[1]) in UNITS[("SG", CRIT)]["clauses"][0][1] and sg(cn[0]) in UNITS[("CN", CRIT)]["clauses"][0][1],
          "the units' clauses quote the recomputed rates")

    print("\n[4] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))
    vn = p.vectors([UNITS], start=p.vsteps[-1])[-1]
    tiers = []
    for c in fl:
        alt = float(UNITS[(c, CRIT)]["flag"][0][:3])
        v = dict(vn[c])
        v[CRIT] = alt
        f_now = sum(1 for k in p.cids if vn[c][k] == 0.0)
        f_alt = sum(1 for k in p.cids if v[k] == 0.0)
        if pc.tier(f_now) != pc.tier(f_alt):
            tiers.append(c)
    check(sorted(tiers) == EXPECT["tier"], f"flags that could change a tier: {', '.join(sorted(tiers))}")

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.9", "After group 2.10")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    rows_ = ["| Entry | Published | Carbon | Biodiversity | Footprint | Boundaries | Verdict | Flag |",
             "|---|---:|---|---|---|---|---:|---|"]
    for c in mine:
        r = UNITS[(c, CRIT)]
        rows_.append(f"| {c} | {pc.f1(pub[c])} | " + " | ".join(pc.STATUS[x[0]] for x in r["clauses"]) +
                     f" | {pc.f1(r['verdict'])} | {('toward ' + r['flag'][0][:3]) if r['flag'] else ''} |")
    t["summary"] = "\n".join(rows_)
    for c in mine:
        r = UNITS[(c, CRIT)]
        lines = [f"#### {c} {CRIT} {p.v2[CRIT]['name']}: {pc.f1(pub[c])} → {pc.f1(r['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (s, est, src_) in enumerate(r["clauses"]):
            lines.append(f"| {i + 1} | {d['clauses'][i]} | {pc.STATUS[s]} | {est} | {src_} |")
        if r["zero"]:
            lines += ["", f"*0.0 (protocol 2.1):* {r['zero']}."]
        if r["flag"]:
            lines += ["", f"*Flag (reading {r['flag'][1]}):* toward {r['flag'][0]}."]
        if r["note"]:
            lines += ["", f"*Note:* {r['note']}."]
        t[f"unit {c}"] = "\n".join(lines)
    GENERATED.clear()
    GENERATED.update(t)
    if "--tables" in sys.argv[1:]:
        sys.stdout = sys.__stdout__
        print(json.dumps(t, ensure_ascii=False))
        return 0
    rec = open(os.path.join(HERE, RECORD), encoding="utf-8").read() if os.path.isfile(os.path.join(HERE, RECORD)) else ""
    missing = [k for k, v in t.items() if v not in rec]
    check(not missing, f"{RECORD} contains all {len(t)} generated tables", ", ".join(missing[:5]))
    print()
    print(t["summary"])
    print()
    print(t["consequences"])
    print("\nRESCORING STAGE 2, GROUP 2.10, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.10: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
