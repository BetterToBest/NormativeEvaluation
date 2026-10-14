#!/usr/bin/env python3
"""
rescoring_s56.py -- NEEC rescoring pass, stage 2, group 2.4: C3.5 Failure-Mode Transparency, class I
=====================================================================================================
Session 56. The first class I group, and the third written on the shared module (pass_common.py, decision 52.5). v2.0
keeps C3.5's clauses and bar and names an indicator for each (criteria.json; NEEC_Criteria_v2_s45.md, section 4):
clauses 1 and 2 aspirational, clause 3 the supreme audit institution's published share of recommendations implemented,
clause 4 the IMF's implicit fossil fuel subsidies as a share of GDP, the published lower bound of externalization. The
20 units the pass had not re-estimated are read clause by clause, from the evidence cache of Session 55
(evidence_cache_s55.py, evidence_cache/C3.5/) and the sources this session added to it (SOURCES below). Centrally
Planned Socialism's unit (part (a)) and CCO-PTF-CIP-SZH's and Integral's (part (b6)) are not re-read. Readings:
NEEC_Rescoring_s56.md.

What this script holds and checks, beyond the module's generic checks (records complete, the rule, consequences,
ledger, dominance, anchors, the record's tables):
  [1] the group: one unit per entry not yet re-estimated on C3.5, each against its published score; which rise, fall
      or hold; the 0.0s and their reasons
  [2] the sources added to the cache: every file by digest, and every figure the readings quote found in its file
  [3] the indicator readings: clause 4 recomputed from the IMF rows for every configured national economy (and the
      host economy Stakeholder Capitalism keeps), clause 3 from the audit offices' published figures, each status
      following decision 56.1
  [4] the flags
Sources not in this repository's earlier files are cached under evidence_cache/C3.5/ with their md5s; every figure used
from them is checked against the cached file.

Usage: python3 rescoring_s56.py            (reads criteria.json, criteria_s44_snapshot.json, neec_corpus.json,
                                             pass_common.py and the parts it loads, the files of SOURCES,
                                             NEEC_Rescoring_s56.md; writes nothing)
       python3 rescoring_s56.py --tables   (prints the generated tables as JSON, for the record)
       python3 rescoring_s56.py --fetch    (network: rebuilds the files of SOURCES and prints their digests)
Prints file names and summaries only. Deterministic offline.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD, CRIT = "(2.4)", "NEEC_Rescoring_s56.md", "C3.5"
CACHE = "evidence_cache/C3.5/"
UNITS = {}
GENERATED = {}


def U(code, verdict, c1, c2, c3, c4, flag=None, note="", zero=None):
    """One unit of C3.5. c1..c4: (status, estimate, source) for the four v2.0 clauses. flag: (alternative, reading).
    zero: protocol 2.1's whole-criterion reason (decision 53.2)."""
    UNITS[(code, CRIT)] = dict(verdict=verdict, clauses=[c1, c2, c3, c4], flag=flag, note=note, zero=zero)


# ---- sources added to the cache this session (fetched 2026-10-14; `--fetch` rebuilds them) ---------------------------
IMF_URL = ("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator%2015%20Fossil%20Fuel%20"
           "Subsidies/FeatureServer/0/query")
ISO = ("CHN", "DNK", "FIN", "ISL", "NOR", "QAT", "SGP", "SWE", "USA")
IMF_IND = ("Implicit Fossil Fuel Subsidies - Total", "Implicit Fossil Fuel Subsidies - Global Warming",
           "Implicit Fossil Fuel Subsidies - Local Air Pollution", "Explicit Fossil Fuel Subsidies - Total")
SOURCES = {
    "imf": ("imf_ffs_rows_s56.json", "", None,
            "IMF Fossil Fuel Subsidies Data: 2023 Update (Black, Liu, Parry and Vernon), the country rows served by the "
            "IMF Climate Change Indicators Dashboard (climatedata.imf.org, dataset 'Fossil Fuel Subsidies Table'), "
            "percent of GDP"),
    "gao": ("gao_fy2024_govexec.txt", "", "https://govexec.com/oversight/2024/11/gao-saved-federal-government-675-"
            "billion-fiscal-2024/401343",
            "Government Executive, 'GAO saved the federal government $67.5 billion in fiscal 2024' (November 2024), "
            "reporting GAO's Performance and Accountability Report for fiscal 2024 (GAO-25-900570; gao.gov refuses "
            "this container)"),
    "cn23": ("cnao_rectification_2023.txt", "", "https://subsites.chinadaily.com.cn/npc/2023-12/27/c_952036.htm",
             "China Daily (NPC site), 'Majority of auditing problems from 2022 have been rectified', 27 December 2023"),
    "cn24": ("cnao_rectification_2024.txt", "", "https://subsites.chinadaily.com.cn/npc/2024-12/23/c_1058832.htm",
             "China Daily (NPC site), Xinhua, 'Audit report shows China fixed 94 pct of fiscal irregularities', "
             "23 December 2024"),
    "cn25": ("cnao_rectification_2025.txt", "", "https://subsites.chinadaily.com.cn/npc/2025-12/23/c_1150596.htm",
             "China Daily (NPC site), 'Audit: China fixes bulk of fiscal problems tied to 2024 budget', 23 December "
             "2025"),
    "se20": ("riksrevisionen_ar2020.txt", "", "https://www.riksdagen.se/sv/dokument-och-lagar/dokument/redogorelse/"
             "riksrevisionens-arsredovisning-for-2020_h804rr1/html/",
             "Riksrevisionens årsredovisning för 2020 (Redogörelse 2020/21:RR4, riksdagen.se), the Auditor General's "
             "foreword"),
}
# The md5 of each cached file, as fetched (the second field above is only a label; these govern).
MD5 = {"imf": "dbd31b4bd7ddcea3cfb84f39a5ccc3dc", "gao": "357aeccac1a76030e44590dc426e83bd",
       "cn23": "2740055a20268ae1bcc66484b8600079", "cn24": "f47c55e4f6d977c68ed4c93a41e07594",
       "cn25": "cdbda9e5b4175a38e2c9d899e4051bb6", "se20": "3e9c1d1152af284523eb854c2b3fc058"}
# Figures quoted from the text sources: each must occur verbatim in its cached extract.
QUOTES = {
    "gao": ["four-year rate for implementing its past recommendations was 70%", "fiscal 2023’s rate of 75%",
            "goal of 80%"],
    "cn23": ["Ninety-two percent of auditing problems discovered in 2022 have been rectified as of September"],
    "cn24": ["China has rectified 94 percent of the issues identified in an audit report"],
    "cn25": ["98 percent of the 2,186 issues requiring immediate action have been resolved",
             "1,299 issues requiring phased rectification and 753 issues needing ongoing attention"],
    "se20": ["åtgärdat närmare 85 procent av de rekommendationer som vi lämnat inom ett år"],
}
WINDOW = {"gao": "four-year rate", "cn23": "Ninety-two percent", "cn24": "China has rectified",
          "cn25": "98 percent of the 2,186", "se20": "närmare 85 procent"}

# ---- figures held ------------------------------------------------------------------------------------------------
YEAR = "F2022"   # the 2023 update's latest estimated year; later years are projections
CN = {"immediate": 2186, "phased": 1299, "ongoing": 753, "share_imm": 98}
NORDIC = ("DNK", "FIN", "ISL", "NOR", "SWE")


def imf_rows():
    path = os.path.join(HERE, CACHE, SOURCES["imf"][0])
    if not os.path.isfile(path):
        return {}
    return {(r["ISO3"], r["Indicator"]): r for r in json.load(open(path, encoding="utf-8"))["rows"]}


def implicit(iso, ind="Implicit Fossil Fuel Subsidies - Total"):
    r = imf_rows().get((iso, ind))
    return None if r is None else round(r[YEAR], 2)


def pct(x):
    return f"{x:.2f}%"


FIG = {}


def figs():
    """The clause 4 and clause 3 figures the readings quote, computed from the cached files."""
    if FIG:
        return FIG
    for iso in ISO:
        v = implicit(iso)
        FIG[iso] = pct(v) if v is not None else "?"
    nor = [implicit(i) for i in NORDIC]
    FIG["nordic"] = (f"{pct(min(nor))} (Finland) to {pct(max(nor))} (Denmark)" if None not in nor else "?")
    tot = CN["immediate"] + CN["phased"] + CN["ongoing"]
    FIG["cn_all"] = f"{round(CN['share_imm'] / 100 * CN['immediate'] / tot * 100)}%"
    FIG["cn_tot"] = f"{tot:,}"
    env = [imf_rows().get(("CHN", i)) for i in IMF_IND[1:3]]
    FIG["CHN_env"] = pct(round(env[0][YEAR] + env[1][YEAR], 2)) if None not in env else "?"
    return FIG


figs()

# ---- shared phrases ------------------------------------------------------------------------------------------------
REP = "Report v1.6, "
IMF_SRC = "IMF Fossil Fuel Subsidies Data, 2023 Update, implicit subsidies, 2022 (" + CACHE + SOURCES["imf"][0] + ")"
GAO_SRC = "GAO Performance and Accountability Report, fiscal 2024, as reported by Government Executive (" + CACHE + \
          SOURCES["gao"][0] + ")"
CN_SRC = ("National Audit Office of China, rectification reports to the NPC Standing Committee, 2023 to 2025, as "
          "reported by Xinhua and China Daily (" + CACHE + "cnao_rectification_2023.txt, _2024.txt, _2025.txt)")
SE_SRC = "Riksrevisionen, annual report for 2020 (" + CACHE + SOURCES["se20"][0] + ")"
C1_NONE = "the scoring document names no dated record of the entry's most consequential failure, which the measure requires"
C1_DESIGN = "no monitoring rule stating how soon a failure is identified is specified or cited"
C2_ASP = "aspirational: no diagnostic record or independent evaluation reporting the share of failures whose cause is established is cited"
C3_DESIGN = "no correction record, and no share of identified failures corrected, is stated or cited"
C4_DESIGN = "no externalized cost is projected as a share of total costs"
R3 = "the mechanism does not govern the economy's audit institution; the host's rate is not credited to it (protocol 3.2)"
R4 = "the mechanism prices no fuel use and governs no other externalized cost; the host's figure is not credited to it (protocol 3.2)"

# ---- the units (readings in NEEC_Rescoring_s56.md, section 3) -------------------------------------------------------
U("SQ", 0.5,
  ("U", C1_NONE + "; the rationale names the 2008 crisis without its inquiry", f"{REP}System 1, C3.5"),
  ("U", C2_ASP, f"{REP}System 1, C3.5"),
  ("C", "the four-year rate at which agencies implemented GAO's recommendations was 70% in fiscal 2024 (75% in fiscal "
        "2023), at the bar", GAO_SRC),
  ("C", f"implicit fossil fuel subsidies were {FIG['USA']} of GDP in 2022, under 10%", IMF_SRC),
  note="the published rationale's externalization finding is not borne out on the measure v2.0 names; the verdict is "
       "unchanged because clauses 1 and 2 are not shown (reading 3.4)")
U("NSD", 0.5,
  ("U", C1_NONE, f"{REP}System 2, C3.5"),
  ("U", C2_ASP, f"{REP}System 2, C3.5"),
  ("U", "Sweden's Riksrevisionen reported in 2020 that agencies had acted on nearly 85% of its annual-audit "
        "recommendations within a year; no rate was located for Denmark, Finland, Iceland or Norway",
   SE_SRC),
  ("C", f"implicit fossil fuel subsidies were {FIG['nordic']} of GDP in 2022 in each of the five countries, under 10%",
   IMF_SRC),
  note="published 0.0 on clause 4 alone (environmental costs systematically externalized); on the measure v2.0 names "
       "the configuration clears that clause, so 2.1's 0.0 conditions do not hold for the criterion as a whole and the "
       "unit rises to 0.5 (reading 3.4)")
U("MS", 0.5,
  ("U", "worker ownership makes firm failures visible to members immediately; " + C1_DESIGN, f"{REP}System 4, C3.5"),
  ("U", C2_ASP, f"{REP}System 4, C3.5"),
  ("U", C3_DESIGN, f"{REP}System 4, C3.5"),
  ("U", "market externalities (environmental costs) remain hidden, as the rationale says; " + C4_DESIGN,
   f"{REP}System 4, C3.5"),
  note="the 0.5 band's anchor example; it holds")
U("LM", 0.5,
  ("U", "losses and bankruptcy make a firm's failure visible to its owners and creditors; " + C1_DESIGN,
   f"{REP}System 5, C3.5"),
  ("U", C2_ASP, f"{REP}System 5, C3.5"),
  ("U", "no audit institution or correction record for systemic failures is specified; " + C3_DESIGN,
   f"{REP}System 5, C3.5"),
  ("U", "market externalities are left to claims by identifiable victims; " + C4_DESIGN, f"{REP}System 5, C3.5"),
  flag=("0.0, the anchor's reading: no mechanism makes systemic failures legible, and failures visible only to a firm's "
        "owners do not answer the criterion", "3.3"),
  note="published 0.0 (the 0.0 band's anchor) read under protocol 2.1: firm failures visible to owners and diffuse costs "
       "externalized is the 0.5 band's description, which Market Socialism's unit holds; a correction, as decision 53.3 "
       "raised the design's C1.2a (reading 3.3)")
U("MMT", 0.0,
  ("U", "the Job Guarantee's enrolment shows unemployment, not the failure of any institution; " + C1_DESIGN,
   f"{REP}System 6, C3.5"),
  ("U", C2_ASP, f"{REP}System 6, C3.5"),
  ("R", R3, f"{REP}System 6, C3.5; SCORING_PROTOCOL.md 3.2"),
  ("R", R4, f"{REP}System 6, C3.5; SCORING_PROTOCOL.md 3.2"),
  zero="no structural mechanism addresses the criterion: a job guarantee and functional-finance budgeting have no "
       "channel that detects, diagnoses or corrects failures or prices externalized costs, and the host economy's are "
       "not the mechanism's")
U("UBI", 0.0,
  ("U", C1_DESIGN, f"{REP}System 7, C3.5"),
  ("U", C2_ASP, f"{REP}System 7, C3.5"),
  ("R", R3, f"{REP}System 7, C3.5; SCORING_PROTOCOL.md 3.2"),
  ("R", R4, f"{REP}System 7, C3.5; SCORING_PROTOCOL.md 3.2"),
  zero="no structural mechanism addresses the criterion: a cash transfer has no channel that detects, diagnoses or "
       "corrects failures or prices externalized costs, and the host economy's are not the mechanism's")
U("DG", 0.5,
  ("U", "localized systems make failures visible to communities; " + C1_DESIGN, f"{REP}System 8, C3.5"),
  ("U", C2_ASP, f"{REP}System 8, C3.5"),
  ("U", C3_DESIGN, f"{REP}System 8, C3.5"),
  ("U", "ecological impacts still require technical monitoring, as the rationale says; " + C4_DESIGN,
   f"{REP}System 8, C3.5"))
U("SC", 0.5,
  ("U", "ESG metrics are self-reported with minimal enforcement; " + C1_NONE, f"{REP}System 9, C3.5"),
  ("U", C2_ASP, f"{REP}System 9, C3.5"),
  ("C", "the reform keeps the host economy's institutions, Status Quo's as group 2.3 read them: agencies implemented 70% "
        "of GAO's recommendations within four years in fiscal 2024", f"{REP}System 9, C3.5; {GAO_SRC}"),
  ("C", f"on the same host economy, implicit fossil fuel subsidies were {FIG['USA']} of GDP in 2022, under 10%",
   IMF_SRC),
  flag=("0.0, the anchor's reading: ESG self-reporting obscures systemic failures behind public relations, with clause 4 "
        "read as a lower bound that can show only a shortfall (decision 56.1, alternative)", "3.4"),
  note="published 0.0 (the 0.0 band's second anchor); with clauses 3 and 4 cleared on the host economy the reform "
       "keeps, 2.1's 0.0 conditions do not hold for the criterion as a whole, and the unit rises to 0.5, as Status "
       "Quo's holds (reading 3.4)")
U("FALC", 0.5,
  ("U", "technical failures are highly visible (systems crash, production halts); " + C1_DESIGN, f"{REP}System 10, C3.5"),
  ("U", C2_ASP, f"{REP}System 10, C3.5"),
  ("U", C3_DESIGN, f"{REP}System 10, C3.5"),
  ("U", C4_DESIGN, f"{REP}System 10, C3.5"))
U("PE", 0.5,
  ("U", "production and consumption imbalances are visible through the planning iterations; " + C1_DESIGN,
   f"{REP}System 11, C3.5"),
  ("U", C2_ASP, f"{REP}System 11, C3.5"),
  ("U", C3_DESIGN, f"{REP}System 11, C3.5"),
  ("U", C4_DESIGN, f"{REP}System 11, C3.5"))
U("GEO", 0.5,
  ("U", "where well implemented, mass-valuation results are published with a correction channel for landowners "
        "(Estonia); " + C1_DESIGN, "NEEC_Georgism_LVT_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_Georgism_LVT_scoring_scratch.md, C3.5"),
  ("U", "the valuation's appeal channel corrects parcel errors, but no share corrected is stated; the economy's audit "
        "institution is not the mechanism's", "NEEC_Georgism_LVT_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"),
  ("R", R4, "NEEC_Georgism_LVT_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"))
U("MC", 0.5,
  ("U", "balances are visible to members in a shared ledger; the Redes de Trueque's counterfeiting and voucher inflation "
        "went undetected long enough to cause collapse; " + C1_DESIGN,
   "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5"),
  ("U", C3_DESIGN, "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5"),
  ("R", R4, "NEEC_MutualCredit_LETS_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"))
U("DE", 0.5,
  ("U", "City Portraits surface shortfalls and overshoots publicly, but on a reporting cycle, not within a week of a "
        "failure; no dated record is named", "NEEC_DoughnutEconomics_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_DoughnutEconomics_scoring_scratch.md, C3.5"),
  ("U", "correction is left to each jurisdiction's political process; an assessment found Amsterdam's implementation "
        "'incipient and limited'; no share corrected is stated", "NEEC_DoughnutEconomics_scoring_scratch.md, C3.5"),
  ("U", "the framework reports ecological overshoot but prices none of it; " + C4_DESIGN,
   "NEEC_DoughnutEconomics_scoring_scratch.md, C3.5"))
U("UBS", 0.0,
  ("U", "the transparency the published score credits is ordinary journalistic and academic scrutiny of specific "
        "implementations; " + C1_DESIGN, "NEEC_UniversalBasicServices_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_UniversalBasicServices_scoring_scratch.md, C3.5"),
  ("R", R3, "NEEC_UniversalBasicServices_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"),
  ("R", R4, "NEEC_UniversalBasicServices_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"),
  flag=("0.5: public provision brings each service within public audit and democratic accountability, a channel the "
        "mechanism itself creates", "3.5"),
  zero="no structural mechanism addresses the criterion: the scoring document finds no purpose-built mechanism and "
       "credits only the host economy's ordinary scrutiny, which is not the mechanism's (protocol 3.2), as for "
       "Universal Basic Income and MMT + Job Guarantee",
  note="published 0.5 on the host economy's scrutiny; a correction (reading 3.5)")
U("SWF", 0.5,
  ("U", "Norway's fund scores 100 of 100 on the Truman scoreboard, with a Council on Ethics since 2004; funds such as "
        "Russia's and Iran's score about 5 of 10 on the Linaburg-Maduell index; " + C1_DESIGN,
   "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5"),
  ("U", "over 180 disclosed exclusion decisions by 2025 are corrections of the fund's own holdings; no share of "
        "identified failures corrected is stated", "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5"),
  ("R", R4, "NEEC_SovereignWealthFundStatism_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"))
U("CN", 0.0,
  ("S", "on the dated records the scoring document names, the Henan floods (a State Council investigation found reports "
        "of up to 139 dead or missing deliberately withheld) and the epidemic's onset (a doctor's warning met by a "
        "police reprimand), identification and correction took months, not a week",
   "NEEC_StateCapitalism_China_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_StateCapitalism_China_scoring_scratch.md, C3.5"),
  ("U", f"the National Audit Office reports 92% to 98% of the issues requiring immediate action rectified within the "
        f"year (2023 to 2025); of all {FIG['cn_tot']} issues in the 2024 audit, about {FIG['cn_all']} were resolved by "
        "the December report, the rest on roadmaps; no rate on GAO's basis, recommendations implemented within a "
        "stated period, is published", CN_SRC),
  ("S", f"implicit fossil fuel subsidies were {FIG['CHN']} of GDP in 2022, over 10%", IMF_SRC),
  flag=("0.5, the published flag: the Centrally Planned Socialism precedent, and the central investigations and the "
        "audit office's rectification reports weighted as a correction channel; and on the environmental components "
        f"alone (global warming and local air pollution, {FIG['CHN_env']} of GDP) clause 4 would clear (decision 56.1, "
        "alternative (b))", "3.6"),
  zero="the configuration treats public disclosure of its signature failures as illegitimate (the epidemic warning "
       "punished as false information, a censorship directive during the floods, the labour-protest monitor dissolved), "
       "and on every clause the record shows it falls short",
  note="the published 0.0 and its flag hold; v2.0's clause 4 figure confirms the externalization the rationale names")
U("SG", 0.5,
  ("U", "official data are extensive and the dormitory outbreak's case data were public; " + C1_NONE,
   "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.5"),
  ("U", "the Auditor-General's Office publishes no recommendation-implementation rate that was located (its site "
        "refuses this container)", "NEEC_StateCapitalism_Singapore_scoring_scratch.md, C3.5"),
  ("C", f"implicit fossil fuel subsidies were {FIG['SGP']} of GDP in 2022, under 10%", IMF_SRC),
  flag=("0.0, the published flag: POFMA orders, the absence of any poverty line and non-public state-enterprise data "
        "read as active suppression, with clause 4 read as a lower bound that can show only a shortfall (decision 56.1, "
        "alternative)", "3.6"))
U("QA", 0.5,
  ("S", "the ILO's report on 2020 found no categorical count of fatal occupational injuries possible, and the authorities "
        "do not classify unexplained or heat-related deaths of workers as work-related: failures are left unidentified, "
        "not identified within a week", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.5"),
  ("U", "no recommendation-implementation rate of the State Audit Bureau was located (its site did not answer this "
        "container)", "NEEC_StateCapitalism_Qatar_scoring_scratch.md, C3.5"),
  ("C", f"implicit fossil fuel subsidies were {FIG['QAT']} of GDP in 2022, under 10% (explicit subsidies, undercharging "
        "for supply costs, are a different quantity)", IMF_SRC),
  flag=("0.0, the published reading: deaths left unexplained and a worker detained after raising concerns, with clause 4 "
        "read as a lower bound that can show only a shortfall (decision 56.1, alternative)", "3.6"),
  note="published 0.0 on a continuous estimate of 0.2 to 0.35; with clause 4 cleared on the measure v2.0 names, 2.1's "
       "0.0 conditions do not hold for the criterion as a whole (decision 53.2), and the unit rises to 0.5 (reading "
       "3.6)")
U("IF", 0.5,
  ("U", "the disclosure regime on profit-equalisation and investment-risk reserves is largely observed (IFSB WP-10), "
        "but account holders are in some cases not informed of the bank's practices (IMF WP 15/120); " + C1_DESIGN,
   "NEEC_IslamicFinance_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_IslamicFinance_scoring_scratch.md, C3.5"),
  ("U", C3_DESIGN, "NEEC_IslamicFinance_scoring_scratch.md, C3.5"),
  ("R", R4, "NEEC_IslamicFinance_scoring_scratch.md, C3.5; SCORING_PROTOCOL.md 3.2"),
  flag=("0.0, the published flag: return-smoothing read as active suppression of the mechanism's own central failure "
        "mode", "3.7"))
U("OS", 0.5,
  ("U", "principles 4 to 6 specify monitors accountable to the appropriators, graduated sanctions and cheap conflict "
        "resolution, at a scale where deviations are visible within days; no monitoring rule states a time",
   "NEEC_Ostrom_Commons_scoring_scratch.md, C3.5"),
  ("U", C2_ASP, "NEEC_Ostrom_Commons_scoring_scratch.md, C3.5"),
  ("U", "sanctions and conflict resolution are a correction apparatus, but no share of identified failures corrected "
        "is stated", "NEEC_Ostrom_Commons_scoring_scratch.md, C3.5"),
  ("U", "principle 1's boundaries make costs borne by non-members a designed-in possibility (Stern, International "
        "Journal of the Commons, 2011); no share is stated", "NEEC_Ostrom_Commons_scoring_scratch.md, C3.5"),
  note="the scope scenario reading externalization against the governed resource no longer reaches 1.0: clauses 2 and "
       "3 are not shown in either frame (reading 3.7)")

EXPECT = {"rise": ["NSD", "LM", "SC", "QA"], "fall": ["UBS"], "zero": ["MMT", "UBI", "UBS", "CN"], "ones": [],
          "flags": {"LM": "3.3", "SC": "3.4", "UBS": "3.5", "CN": "3.6", "SG": "3.6", "QA": "3.6", "IF": "3.7"},
          "before": ["CPS", "CCO", "INT"]}
NATIONAL = {"SQ": "USA", "SC": "USA", "CN": "CHN", "SG": "SGP", "QA": "QAT"}


def text_of(html):
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&#39;", "'"), ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">")):
        html = html.replace(a, b)
    return re.sub(r"\s+", " ", html).strip()


def fetch():
    """Network. Rebuild the files of SOURCES and print their digests (to be written into MD5)."""
    os.makedirs(os.path.join(HERE, CACHE), exist_ok=True)
    where = (f"ISO3 IN ({','.join(repr(i) for i in ISO)}) AND Unit='Percent of GDP' AND Indicator IN "
             f"({','.join(repr(i) for i in IMF_IND)})")
    r = subprocess.run(["curl", "-sS", "-G", "-m", "60", "--retry", "4", "--retry-all-errors", IMF_URL, "--data-urlencode", f"where={where}",
                        "--data-urlencode", "outFields=ISO3,Country,Indicator,Unit,Source,F2021,F2022,F2023",
                        "--data-urlencode", "orderByFields=ISO3,Indicator", "--data-urlencode", "returnGeometry=false",
                        "--data-urlencode", "f=json"], capture_output=True, check=True)
    feats = [f["attributes"] for f in json.loads(r.stdout)["features"]]
    out = {"retrieved": "2026-10-14", "source": feats[0]["Source"], "query_url": IMF_URL, "where": where,
           "rows": [{k: a[k] for k in ("ISO3", "Country", "Indicator", "Unit", "F2021", "F2022", "F2023")}
                    for a in feats]}
    with open(os.path.join(HERE, CACHE, SOURCES["imf"][0]), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, sort_keys=True, ensure_ascii=False)
        f.write("\n")
    for key, (name, _, url, _) in SOURCES.items():
        if url is None:
            continue
        r = subprocess.run(["curl", "-sS", "-L", "-m", "60", "--retry", "4", "--retry-all-errors", url], capture_output=True, check=True)
        t = text_of(r.stdout.decode("utf-8", "replace"))
        i = t.find(WINDOW[key])
        ext = (f"Source: {url}\nRetrieved 2026-10-14; raw md5 {hashlib.md5(r.stdout).hexdigest()}; extract: the "
               f"article text from 1,500 characters before the passage quoted to 1,500 after.\n\n"
               + t[max(0, i - 1500):i + 1500] + "\n")
        with open(os.path.join(HERE, CACHE, name), "w", encoding="utf-8") as f:
            f.write(ext)
    for key, (name, _, _, _) in SOURCES.items():
        print(f'    "{key}": "{hashlib.md5(open(os.path.join(HERE, CACHE, name), "rb").read()).hexdigest()}",')
    return 0


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
    print(f"NEEC rescoring pass, stage 2, group 2.4: C3.5 Failure-Mode Transparency, class I ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this group, "
          f"{len(SOURCES)} files of {CACHE}, {RECORD}\n")

    print("[1] THE GROUP")
    pub = {c: p.vec[c][CRIT] for c in p.order}
    before = [c for c in p.order if (c, CRIT) in p.merged]
    mine = [c for c in p.order if (c, CRIT) in UNITS]
    check(before == EXPECT["before"] and sorted(mine + before) == sorted(p.order) and len(UNITS) == len(mine),
          f"one unit per entry on {CRIT} not yet re-estimated, {len(UNITS)} in all; {', '.join(before)} were "
          f"re-estimated before this group ({', '.join(p.part_of[(c, CRIT)] for c in before)}) and are not re-read")
    check(p.v2[CRIT]["revision"]["cls"] == "I" and len(p.v2[CRIT]["definition"]["clauses"]) == 4,
          f"{CRIT} is class I with four clauses in v2.0")
    fall = [c for c in mine if UNITS[(c, CRIT)]["verdict"] < pub[c]]
    rise = [c for c in mine if UNITS[(c, CRIT)]["verdict"] > pub[c]]
    pv = [pub[c] for c in mine]
    check(fall == EXPECT["fall"] and rise == EXPECT["rise"],
          f"published scores of the {len(mine)}: 1.0 x{pv.count(1.0)}, 0.5 x{pv.count(0.5)}, 0.0 x{pv.count(0.0)}; this "
          f"group raises {len(rise)} ({', '.join(rise)}), lowers {len(fall)} ({', '.join(fall)}) and holds "
          f"{len(mine) - len(fall) - len(rise)}")
    zeros = [c for c in mine if UNITS[(c, CRIT)].get("zero")]
    check(zeros == EXPECT["zero"] and all(UNITS[(c, CRIT)]["verdict"] == 0.0 for c in zeros),
          f"{len(zeros)} units are 0.0, each on a stated whole-criterion reason (protocol 2.1): "
          + ", ".join(f"{c} ({'held' if pub[c] == 0.0 else 'from ' + pc.f1(pub[c])})" for c in zeros))
    ones = [c for c in mine if UNITS[(c, CRIT)]["verdict"] == 1.0]
    asp = [c for c in mine if UNITS[(c, CRIT)]["clauses"][1][0] in "CM"]
    check(ones == EXPECT["ones"] and not asp, "no unit clears clause 2, which v2.0 marks aspirational, so none can reach "
          "1.0; after this group no entry is at 1.0 on " + CRIT)

    print("\n[2] THE SOURCES ADDED TO THE CACHE (digests; every figure quoted found in its file)")
    for key, (name, _, url, title) in SOURCES.items():
        path = os.path.join(HERE, CACHE, name)
        raw = open(path, "rb").read() if os.path.isfile(path) else b""
        got = hashlib.md5(raw).hexdigest()
        txt = raw.decode("utf-8")
        lost = [q for q in QUOTES.get(key, []) if q not in txt]
        check(got == MD5.get(key) and not lost, f"{name}: md5 {got[:8]}" + (f", {len(QUOTES[key])} passage(s) "
              "quoted" if key in QUOTES else f", {len(imf_rows())} rows"), ", ".join(lost))

    print("\n[3] THE INDICATOR READINGS (decision 56.1)")
    rows = imf_rows()
    check(len(rows) == len(ISO) * len(IMF_IND) and all(r["Unit"] == "Percent of GDP" for r in rows.values()),
          f"the IMF rows: {len(ISO)} countries x {len(IMF_IND)} series, percent of GDP, {YEAR[1:]} read")
    bad = []
    for c, iso in NATIONAL.items():
        v, st = implicit(iso), UNITS[(c, CRIT)]["clauses"][3]
        if (st[0] == "C") != (v < 10) or (st[0] == "S") != (v >= 10) or FIG[iso] not in st[1]:
            bad.append(c)
    nor = [implicit(i) for i in NORDIC]
    if not (max(nor) < 10 and UNITS[("NSD", CRIT)]["clauses"][3][0] == "C" and FIG["nordic"] in
            UNITS[("NSD", CRIT)]["clauses"][3][1]):
        bad.append("NSD")
    check(not bad, "clause 4: each configured national economy's status follows its implicit subsidies (cleared under "
          "10% of GDP, short at 10% or more): " + ", ".join(f"{c} {FIG[i]}" for c, i in NATIONAL.items() if c != "SC")
          + f", NSD {FIG['nordic']}; Stakeholder Capitalism on its host economy, the United States", ", ".join(bad))
    gw = {i: round(rows[(i, IMF_IND[1])][YEAR] + rows[(i, IMF_IND[2])][YEAR], 2) for i in ISO}
    check(all(gw[i] <= implicit(i) + 1e-9 for i in ISO) and gw["CHN"] < 10 and pct(gw["CHN"]) == FIG["CHN_env"]
          and FIG["CHN_env"] in UNITS[("CN", CRIT)]["flag"][0] and all(gw[i] < 10 for i in ISO),
          "on the environmental components alone (global warming and local air pollution; decision 56.1, alternative "
          f"(b)) every status is the same except China's, {FIG['CHN_env']} against {FIG['CHN']}, which would clear: "
          "carried in China's flag")
    sq3 = UNITS[("SQ", CRIT)]["clauses"][2]
    check(sq3[0] == "C" and "70%" in sq3[1] and UNITS[("SC", CRIT)]["clauses"][2][0] == "C",
          "clause 3: GAO's four-year rate, 70% in fiscal 2024, is at the bar (correction success at least 70%): cleared "
          "for Status Quo and for Stakeholder Capitalism's host economy")
    tot = CN["immediate"] + CN["phased"] + CN["ongoing"]
    check(UNITS[("CN", CRIT)]["clauses"][2][0] == "U" and FIG["cn_all"] in UNITS[("CN", CRIT)]["clauses"][2][1]
          and round(CN["share_imm"] / 100 * CN["immediate"]) < 0.7 * tot,
          f"clause 3, China: 98% of the {CN['immediate']:,} issues requiring immediate action, but about "
          f"{FIG['cn_all']} of all {tot:,} issues, resolved by the report; on GAO's basis not shown")
    check(UNITS[("NSD", CRIT)]["clauses"][2][0] == "U", "clause 3, the Nordic configuration: Sweden's nearly 85% within "
          "a year is one country's; not shown for the configuration")

    print("\n[4] FLAGS")
    fl = {c: UNITS[(c, CRIT)]["flag"][1] for c in mine if UNITS[(c, CRIT)]["flag"]}
    check(fl == EXPECT["flags"], "flags: " + ", ".join(f"{c} toward {UNITS[(c, CRIT)]['flag'][0][:3]} (reading {r})"
                                                       for c, r in fl.items()))

    print("\n[5] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.3", "After group 2.4")
    ok = ok and good

    print(f"\n[6] THE RECORD'S UNIT TABLES (generated here; {RECORD} must contain them verbatim)")
    f1 = pc.f1
    rows_ = ["| Entry | Published | Clause 1 | Clause 2 | Clause 3 | Clause 4 | Verdict | Flag |",
             "|---|---:|---|---|---|---|---:|---|"]
    for c in mine:
        r = UNITS[(c, CRIT)]
        rows_.append(f"| {c} | {f1(pub[c])} | " + " | ".join(pc.STATUS[x[0]] for x in r["clauses"]) +
                     f" | {f1(r['verdict'])} | {('toward ' + r['flag'][0][:3]) if r['flag'] else ''} |")
    t["summary"] = "\n".join(rows_)
    for c in mine:
        r = UNITS[(c, CRIT)]
        lines = [f"#### {c} {CRIT} {p.v2[CRIT]['name']}: {f1(pub[c])} → {f1(r['verdict'])}", "",
                 "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
        for i, (st, est, src) in enumerate(r["clauses"]):
            lines.append(f"| {i + 1} | {p.v2[CRIT]['definition']['clauses'][i]} | {pc.STATUS[st]} | {est} | {src} |")
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
    print("\nRESCORING STAGE 2, GROUP 2.4, COMPUTED." if ok else "\nRESCORING STAGE 2, GROUP 2.4: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--fetch" in sys.argv[1:]:
        sys.exit(fetch())
    if "--tables" in sys.argv[1:]:
        sys.stdout = open(os.devnull, "w")
    sys.exit(main())
