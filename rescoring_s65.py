#!/usr/bin/env python3
"""
rescoring_s65.py -- NEEC rescoring pass, stage 2, accelerated groups (2.11 onward): one script, one record
=========================================================================================================
Session 65 (decision 65.1). The owner asked to finish the pass in one or two sessions (the weekly usage limit), so the
remaining criteria are read in one script and one record, a criterion at a time, on the same rules as groups 2.2 to 2.10
(D28: 1.0 only if every clause is cleared; 0.0 only on a stated whole-criterion reason under protocol 2.1 and never with
a clause cleared) and the same shared module. What is leaner: no per-criterion record, and the readings are terse. What is
not: every unit has one status per v2.0 clause with an estimate and a source; every figure a reading quotes is recomputed
from the evidence cache; each unit's published rationale is located by heading and checked at its published score; the
record is generated from this script and compared byte for byte; and the shared module's consequence, ledger, dominance
and anchor checks run on the whole set.

Criteria read so far: CRITS below (C4.1 Intergenerational Justice, class M). Each later criterion adds its units, its
checks and its section of NOTES; the record is regenerated.

Usage: python3 rescoring_s65.py                 (checks; reads the cache, the scoring documents, NEEC_Rescoring_s65.md)
       python3 rescoring_s65.py --write-record  (rewrites NEEC_Rescoring_s65.md from this script's tables)
Prints file names and summaries only. Deterministic.
"""
import hashlib
import io
import json
import os
import re
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pass_common as pc  # noqa: E402

TAG, RECORD = "(2.11)", "NEEC_Rescoring_s65.md"
CRITS = ["C4.1", "C4.4", "C3.4", "C4.5", "C2.5"]
UNITS = {}
GENERATED = {}
NOTES = {}
FLAGS_TIER = {}

ORDER15 = ["SQ", "NSD", "CPS", "MS", "LM", "MMT", "UBI", "DG", "SC", "FALC", "PE", "CCO", "INT", "GEO", "MC"]
SCRATCH = {"DE": "NEEC_DoughnutEconomics", "UBS": "NEEC_UniversalBasicServices", "SWF": "NEEC_SovereignWealthFundStatism",
           "CN": "NEEC_StateCapitalism_China", "SG": "NEEC_StateCapitalism_Singapore", "QA": "NEEC_StateCapitalism_Qatar",
           "IF": "NEEC_IslamicFinance", "OS": "NEEC_Ostrom_Commons"}


def U(code, crit, verdict, clauses, flag=None, note="", zero=None):
    """One unit. clauses: one (status, estimate, source) per v2.0 clause. flag: (alternative, reading). zero: protocol 2.1's
    whole-criterion reason (decision 53.2)."""
    UNITS[(code, crit)] = dict(verdict=verdict, clauses=list(clauses), flag=flag, note=note, zero=zero)


def rat_head(code, crit):
    """(file, line, heading) of the published rationale of `code` on `crit`: the Report's k-th heading of the criterion
    for the first fifteen entries, the entry's scoring document's first heading for the other eight."""
    fn = "NEEC_Report_v1_6.md" if code in ORDER15 else SCRATCH[code] + "_scoring_scratch.md"
    hits = []
    for i, line in enumerate(open(os.path.join(HERE, fn), encoding="utf-8"), 1):
        if re.match(r"^#+ \**" + re.escape(crit) + r"\b", line):
            hits.append((i, line.strip()))
    i, h = hits[ORDER15.index(code)] if code in ORDER15 else hits[0]
    return fn, i, h.lstrip("# *")


def REP(code, crit):
    fn, i, _ = rat_head(code, crit)
    return f"{fn}, line {i} ({code} {crit})"


def jload(crit, name):
    return json.load(open(os.path.join(HERE, "evidence_cache", crit, name)))


# =========================================================================================================================
# C4.1 INTERGENERATIONAL JUSTICE (class M): 1 debt-to-GDP < 80%; 2 positive net national saving over the scoring window
# =========================================================================================================================
C41 = "evidence_cache/C4.1/"
C41_MD5 = {"imf_weo_gross_debt_pct_gdp.json": "148ad7d2c97f421dcadc839ea72f99e1",
           "wb_gross_savings_pct_gni.json": "f84dd1655a39ca4107ee4e348c4da369",
           "wb_consumption_fixed_capital_pct_gni.json": "56352b479a298464aacc85eeedd1d136"}
C41_ECON = {"SQ": ["USA"], "CN": ["CHN"], "SG": ["SGP"], "QA": ["QAT"], "NSD": ["DNK", "FIN", "NOR", "SWE"]}
IMF_SRC = "IMF World Economic Outlook, general government gross debt, % of GDP (DataMapper API; " + C41 + "imf_weo_gross_debt_pct_gdp.json, retrieved 2026-10-15)"
WB_SRC = ("World Bank WDI, gross savings less consumption of fixed capital, % of GNI (" + C41 + "wb_gross_savings_pct_gni.json and "
          "wb_consumption_fixed_capital_pct_gni.json, retrieved 2026-10-15)")
NAME = {"USA": "United States", "CHN": "China", "SGP": "Singapore", "QAT": "Qatar", "DNK": "Denmark", "FIN": "Finland",
        "NOR": "Norway", "SWE": "Sweden"}


def c41_fig(iso):
    d, g, c = (jload("C4.1", n) for n in ("imf_weo_gross_debt_pct_gdp.json", "wb_gross_savings_pct_gni.json",
                                          "wb_consumption_fixed_capital_pct_gni.json"))
    years = sorted(y for y in g[iso] if y in c[iso] and y >= "2015")
    nns = {y: g[iso][y] - c[iso][y] for y in years}
    last = max(d[iso])
    debt = d[iso]
    # the latest outturn year: the IMF series runs into forecast years; the pass reads 2024, the last complete year
    return dict(debt24=debt["2024"], debt23=debt["2023"], nmin=min(nns.values()), nmax=max(nns.values()),
                y0=years[0], y1=years[-1], nns=nns)


def c41_text(iso_list):
    parts_d, parts_n = [], []
    for iso in iso_list:
        f = c41_fig(iso)
        parts_d.append(f"{NAME[iso]} {f['debt24']:.1f}%")
        parts_n.append(f"{NAME[iso]} {f['nmin']:.1f}% to {f['nmax']:.1f}%")
    y0, y1 = c41_fig(iso_list[0])["y0"], c41_fig(iso_list[0])["y1"]
    return ("2024: " + ", ".join(parts_d), f"net national saving, {y0}-{y1}: " + ", ".join(parts_n))


def c41_status(iso_list):
    """Clause 1 cleared if every country's 2024 debt < 80; clause 2 if net saving is positive in every year of every one."""
    c1 = "C" if all(c41_fig(i)["debt24"] < 80 for i in iso_list) else "S"
    c2 = "C" if all(min(c41_fig(i)["nns"].values()) > 0 for i in iso_list) else "S"
    return c1, c2


def nodata(why):
    return ("U", why, "the unit's published rationale")


NO_PATH = ("the sources state no debt path, so clause 1 is not shown", "the sources state no net-saving path, so clause 2 is not shown")


def design(code, verdict, why, note, flag=None, zero=None):
    r = REP(code, "C4.1")
    U(code, "C4.1", verdict, [("U", NO_PATH[0] + "; " + why, r), ("U", NO_PATH[1], r)], flag=flag, note=note, zero=zero)


def economies():
    t1, t2 = c41_text(["USA"]); s1, s2 = c41_status(["USA"])
    U("SQ", "C4.1", 0.5, [(s1, t1, IMF_SRC), (s2, t2, WB_SRC)],
      note="published 0.0 rested on climate debt, ecological damage and depletion, which v2.0 moved to C4.2; on C4.1's own "
           "two measures net saving is positive (clause 2 cleared) and debt is above the bar, so 0.0 cannot stand "
           "(protocol 2.1 and D28(f)) and the unit rises to 0.5, a correction as groups 2.8 and 2.9 read the same case")
    t1, t2 = c41_text(["CHN"]); s1, s2 = c41_status(["CHN"])
    U("CN", "C4.1", 0.5, [(s1, t1 + " (59.9% in 2019, 84.1% in 2023)", IMF_SRC), (s2, t2, WB_SRC)],
      note="short on the headline debt figure, which excludes local-government financing vehicles; holds at 0.5")
    t1, t2 = c41_text(["SGP"]); s1, s2 = c41_status(["SGP"])
    U("SG", "C4.1", 0.5, [(s1, t1 + " (the Government issues securities to build its reserves and the Central Provident Fund's "
                                  "assets, not to fund deficits)", IMF_SRC), (s2, t2, WB_SRC)],
      flag=("1.0", "3.2"),
      note="clause 1 is short on the literal gross measure v2.0 names; the debt funds assets, so the reading could be 1.0 "
           "(reading 3.2)")
    t1, t2 = c41_text(["QAT"]); s1, s2 = c41_status(["QAT"])
    U("QA", "C4.1", 1.0, [(s1, t1, IMF_SRC), (s2, t2, WB_SRC)],
      flag=("0.5", "3.3"),
      note="both clauses are cleared on the measures v2.0 names, so the unit rises from 0.5 to 1.0; net national saving as "
           "v2.0 defines it does not net the depletion of the hydrocarbon stock, so the reading is flagged toward 0.5 "
           "(reading 3.3)")
    isos = C41_ECON["NSD"]
    t1, t2 = c41_text(isos); s1, s2 = c41_status(isos)
    U("NSD", "C4.1", 0.5, [(s1, t1 + " (Finland 77.2% in 2023)", IMF_SRC), (s2, t2, WB_SRC)],
      flag=("1.0", "3.4"),
      note="three of the four clear clause 1; Finland's 2024 debt is 2.5 points above the bar; holds at 0.5 (reading 3.4)")


economies()
design("CPS", 0.5, "the planned economy's saving rate was high and its public debt low, but its sources here give no figure",
       "held at the published 0.5; challengeable with the Soviet accounts")
design("MS", 0.5, "worker ownership gives firms a career-span horizon (published rationale)",
       "held at the published 0.5")
design("LM", 0.0, "no debt rule and no saving rule is part of the design",
       "held at 0.0 on protocol 2.1's first condition: no structural mechanism addresses fiscal or wealth sustainability",
       zero="no structural mechanism addresses debt or saving in the design as specified (protocol 2.1, first condition)")
design("MMT", 0.5, "the design treats the inflation constraint, not a debt ratio, as binding, which is a real constraint "
                   "on spending but not a debt or saving path",
       "held at the published 0.5")
design("UBI", 0.5, "funding is left open (a carbon tax or deficit finance), so the design alone fixes neither",
       "held at the published 0.5")
design("SC", 0.0, "no debt rule and no saving rule is part of the design; the firm-level horizon does not reach public debt "
                  "or national saving",
       "held at 0.0 on protocol 2.1's first condition; the published reason (short-termism, ESG funds) is read as firm "
       "governance, not as C4.1's measures",
       zero="no structural mechanism addresses debt or saving in the design as specified (protocol 2.1, first condition)")
design("GEO", 0.5, "land-value revenue is a durable base and the design frames land as shared across generations",
       "held at the published 0.5")
design("MC", 0.5, "no equivalent to a sovereign fund or land trust was located (published rationale)",
       "held at the published 0.5; the published wording sits close to 0.0 and is left as published")
design("UBS", 0.5, "later sufficiency-economy framing ties the proposal to resource limits (published rationale)",
       "held at the published 0.5")
design("IF", 0.5, "the prohibition of interest-based debt constrains borrowing for private contracts; sovereign sukuk are "
                  "debt (published rationale)",
       "held at the published 0.5")

NOTES["C4.1"] = (
    "C4.1 is class M with two clauses: general government gross debt below 80% of GDP, and positive net national saving "
    "(gross savings less consumption of fixed capital, % of GNI) over the scoring window. The four configured economies and "
    "the four Nordic countries are read on the IMF's and the World Bank's series (cached in `evidence_cache/C4.1/`). The "
    "capital-consumption series ends in 2021, so the window is 2015-2021; debt is the 2024 figure, the last complete year. "
    "**Qatar rises from 0.5 to 1.0** (both clauses cleared; flagged toward 0.5 because the measure does not net resource "
    "depletion). **Status Quo rises from 0.0 to 0.5** (a correction: its published 0.0 rested on carbon and ecology, which "
    "C4.2 now holds; net saving is positive). China, Singapore and Nordic Social Democracy hold at 0.5, each short on clause "
    "1 only (Singapore and Nordic Social Democracy flagged toward 1.0). The ten designs and mechanisms are held at their "
    "published scores, none of whose sources states a debt path or a saving path; Libertarian Minarchism and Stakeholder "
    "Capitalism stay at 0.0 on protocol 2.1's first condition. Anyone who can supply a design's own debt or saving path can "
    "challenge its unit through the site's contribution route.")


def checks_C41(check, p):
    d41 = p.v2["C4.1"]
    check(d41["revision"]["cls"] == "M" and len(d41["definition"]["clauses"]) == 2 and "80%" in d41["definition"]["clauses"][0],
          "C4.1 is class M with two clauses in v2.0: debt below 80% of GDP, positive net national saving")

    print("\n[2] C4.1: THE CACHE AND THE FIGURES THE READINGS QUOTE")
    for name, want in C41_MD5.items():
        raw = open(os.path.join(HERE, C41, name), "rb").read()
        check(hashlib.md5(raw).hexdigest() == want, f"{C41}{name}: md5 {want[:8]}")
    f = {iso: c41_fig(iso) for iso in NAME}
    check(f["USA"]["debt24"] > 80 and f["CHN"]["debt24"] > 80 and f["SGP"]["debt24"] > 80 and f["QAT"]["debt24"] < 80
          and f["FIN"]["debt24"] > 80 and max(f[i]["debt24"] for i in ("DNK", "NOR", "SWE")) < 80,
          "debt 2024: United States, China, Singapore and Finland above 80%; Qatar, Denmark, Norway and Sweden below")
    check(all(min(f[i]["nns"].values()) > 0 for i in NAME) and f["FIN"]["y1"] == "2021",
          "net national saving is positive in every year of 2015-2021 for all eight, so clause 2 is cleared for every economy")
    check(abs(f["FIN"]["debt23"] - 77.2) < 0.05 and abs(f["CHN"]["debt23"] - 84.1) < 0.05,
          "the quoted 2023 figures (Finland 77.2%, China 84.1%) are in the cache")
    for code, isos in C41_ECON.items():
        want = c41_status(isos)
        got = (UNITS[(code, "C4.1")]["clauses"][0][0], UNITS[(code, "C4.1")]["clauses"][1][0])
        check(want == got, f"{code}: clause statuses {got} equal those the cache gives")



# =========================================================================================================================
# C4.4 POWER DISTRIBUTION (class M): 1 accountability for >= 80% of major decisions; 2 removal / replacement mechanisms functional
# =========================================================================================================================
C44 = "evidence_cache/C4.4/"
C44_MD5 = {"owid_vdem_regimes_of_the_world.csv": "c388c56ed1f40ffc8b93271236be431d"}
REGIME = {0: "closed autocracy", 1: "electoral autocracy", 2: "electoral democracy", 3: "liberal democracy"}
VDEM = ("V-Dem Regimes of the World, as Our World in Data republishes it (" + C44 + "owid_vdem_regimes_of_the_world.csv, "
        "retrieved 2026-10-15)")
C44_ECON = {"SQ": "United States", "CN": "China", "SG": "Singapore", "QA": "Qatar", "CPS": None}


def regime(entity, year=2024):
    import csv
    for r in csv.DictReader(open(os.path.join(HERE, C44, "owid_vdem_regimes_of_the_world.csv"), encoding="utf-8")):
        if r["Entity"] == entity and int(r["Year"]) == year:
            return int(r["Political regime"])
    raise KeyError(entity)


GGAAG = ("OECD, Government at a Glance (general government employment, no OECD country above about a third of employment; "
         "not cached in this repository)")
Z_FIRST = "no structural mechanism addresses the distribution of decision power (protocol 2.1, first condition)"


def c44_econ(code, verdict, ent, flag=None, note="", zero=None):
    r = regime(ent)
    rep = REP(code, "C4.4")
    if r >= 2:
        c1 = ("S", f"{ent} is a {REGIME[r]} in 2024, so its public sector counts; but even if every public, self-employed and "
                   f"member-governed job counted, the share could not reach 80% of employment ({GGAAG})", VDEM + "; " + rep)
        c2 = ("C", f"free elections choose and can replace the legislature and the executive ({REGIME[r]} in 2024)", VDEM)
    else:
        c1 = ("S", f"{ent} is a {REGIME[r]} in 2024, so V-Dem's classification denies that the authority its public sector answers "
                   "to is chosen in free elections; the public sector does not count and the share cannot reach 80%", VDEM + "; " + rep)
        c2 = ("S", f"no free election can remove or replace the executive ({REGIME[r]} in 2024)", VDEM + "; " + rep)
    U(code, "C4.4", verdict, [c1, c2], flag=flag, note=note, zero=zero)


def c44_design(code, verdict, c1, c2, note, flag=None, zero=None):
    rep = REP(code, "C4.4")
    U(code, "C4.4", verdict, [(c1[0], c1[1], rep), (c2[0], c2[1], rep)], flag=flag, note=note, zero=zero)


NOS = "the sources state no share of workers in accountable organizations"
NOR = "the sources state no mechanism for removing or replacing those who take decisions"
c44_econ("SQ", 0.5, "United States",
         note="published 0.0 rested on wealth concentration (the top 1% owns 32.3%), which v2.0 measures once, in C1.2b; on "
              "C4.4's own two clauses removal by free elections is cleared and the share is short, so 0.0 cannot stand "
              "(D28(f)) and the unit rises to 0.5, a correction")
c44_econ("CN", 0.0, "China", zero="closed autocracy: no free election chooses the authority, both clauses short with no pathway under the "
                                  "system's own logic (protocol 2.1, third condition)", note="holds at 0.0")
c44_econ("SG", 0.0, "Singapore", flag=("0.5", "3.2"),
         zero="electoral autocracy: both clauses short on V-Dem's classification (protocol 2.1, third condition)",
         note="holds at 0.0; published as contestable, and the reading could be 0.5 if elections that have never changed the "
              "governing party since 1959 are read as a functioning removal mechanism (reading 3.2)")
c44_econ("QA", 0.0, "Qatar", zero="closed autocracy: no free election chooses the authority, both clauses short with no pathway "
                                  "(protocol 2.1, third condition)", note="holds at 0.0")
c44_design("CPS", 0.0, ("S", "the planned economy's public sector answered to a party-state, not to an authority chosen in free "
                          "elections, so it does not count and the share is short"),
           ("S", "no free election could remove or replace the party leadership"),
           "holds at 0.0: the published nomenklatura finding is a finding on both clauses",
           zero="a closed party-state with no pathway to either clause under its own logic (protocol 2.1, third condition)")
c44_design("LM", 0.5, ("S", "owner-governed firms are the economy's organizations, so the share of accountable employment is short"),
           ("U", NOR), "held at the published 0.5: limiting the state's scope distributes political power, a real if partial "
                       "mechanism")
c44_design("MMT", 0.5, ("U", NOS + "; a public job guarantee would be a public body answering to an elected authority"),
           ("U", NOR), "held at the published 0.5")
c44_design("UBI", 0.0, ("S", "the economy's organizations stay governed by their owners"), ("U", NOR),
           "held at 0.0: an income transfer does not change who takes decisions", zero=Z_FIRST)
c44_design("SC", 0.0, ("S", "a board a majority of whose members owners of capital elect answers to them, whatever minority the "
                            "workers elect (v2.0's own wording)"), ("U", NOR),
           "held at 0.0: worker directors who remain a minority do not move accountability", zero=Z_FIRST)
c44_design("FALC", 0.0, ("U", NOS + "; the ownership and control of the machines is left open"), ("U", NOR),
           "held at 0.0 on the published finding that control of the machines is unresolved", zero=Z_FIRST)
c44_design("GEO", 0.5, ("U", NOS), ("U", NOR), "held at the published 0.5: a narrow channel (rent capture) is addressed")
c44_design("MC", 0.5, ("U", NOS), ("U", NOR), "held at the published 0.5: a real anti-concentration mechanism, weakened by the "
                                              "centralisation of the largest example")
c44_design("DE", 0.0, ("U", NOS), ("U", NOR), "held at 0.0: the framework names power as a concern in guidance, not as a mechanism",
           zero=Z_FIRST)
c44_design("UBS", 0.5, ("U", NOS), ("U", NOR), "held at the published 0.5")
c44_design("SWF", 0.5, ("U", NOS), ("U", NOR), "held at the published 0.5: Norway's specific case is mixed for a distinctive reason")
c44_design("IF", 0.0, ("U", NOS), ("U", NOR), "held at 0.0 on the published finding", zero=Z_FIRST)
c44_design("OS", 0.5, ("U", NOS + "; a commons is governed by those who use it, which is accountability within its scope"),
           ("U", NOR), "held at the published 0.5")

NOTES["C4.4"] = (
    "C4.4 is class M with two clauses: democratic accountability for at least 80% of major decisions (the share of employment "
    "in organizations whose decisions are taken or elected by those they affect, public bodies counting only where V-Dem's "
    "Regimes of the World makes the country a democracy) and functional removal and replacement mechanisms. The four "
    "configured economies are read on V-Dem's classification (cached in `evidence_cache/C4.4/`): the United States is a "
    "liberal democracy (clause 2 cleared, clause 1 short on any count); China and Qatar are closed autocracies and Singapore "
    "an electoral autocracy (both clauses short). **Status Quo rises from 0.0 to 0.5**: its published 0.0 rested on wealth "
    "concentration, which v2.0 measures once, in C1.2b. China, Singapore and Qatar hold at 0.0; Singapore is flagged toward "
    "0.5. The twelve designs and mechanisms are held at their published scores: none of their sources states a share of "
    "workers in accountable organizations or a removal mechanism, and each 0.0 rests on protocol 2.1's first or third "
    "condition. Anyone who can supply such a share or mechanism for a design can challenge its unit through the site's "
    "contribution route.")


# =========================================================================================================================
# C3.4 EPISTEMIC ADAPTABILITY (class M): 1 parameter adjustability >= 30%; 2 policy updates within 6 months of evidence;
# 3 changes open to challenge and reversal by those affected; 4 zero collapses during parameter adjustments
# =========================================================================================================================
def c34(code, verdict, cl, note, flag=None, zero=None):
    rep = REP(code, "C3.4")
    U(code, "C3.4", verdict, [(a, b, rep) for a, b in cl], flag=flag, note=note, zero=zero)


c34("SQ", 0.5, [("U", "tax, spending and policy-rate settings are adjustable, but no share of parameters adjustable is stated"),
                ("C", "the CARES Act was signed within a week of the March 2020 claims jump (group 2.9, reading 63.2) and post-2008 "
                      "financial regulation was rewritten within two years"),
                ("C", "legislation and rules are open to court challenge, repeal and the next election by those affected"),
                ("S", "the 2022-23 policy-rate rises were followed by bank failures (Silicon Valley Bank, Signature Bank, First "
                      "Republic), so adjustment has been followed by collapse")],
    "holds at 0.5: clauses 2 and 3 are cleared and clause 4 is short on a recent record; slow and captured adaptation is the published reason")
c34("CPS", 0.0, [("S", "the plan's parameters were set by the party-state and fixed over long cycles"),
                 ("S", "evidence that contradicted ideology was suppressed (the Lysenko affair, published rationale)"),
                 ("S", "no process independent of the officials who made a decision could reverse it"),
                 ("S", "the system ended in collapse (1991)")],
    "holds at 0.0: every clause short and no pathway under the system's own logic",
    zero="every clause short on the record, with no pathway under the system's own logic (protocol 2.1, third condition)")
c34("LM", 0.0, [("U", "the design has few adjustable parameters by intent"),
                ("S", "ideological commitment prevents adaptation to evidence of market failure (published rationale)"),
                ("U", "contestability by those affected is not part of the design"),
                ("U", "no record of adjustment")],
    "holds at 0.0 on the published finding that the system continues regardless of outcomes",
    zero="the system excludes adaptation to contrary evidence by its own logic (protocol 2.1, second condition)")
c34("FALC", 0.5, [("U", "the design is technical and parameterised, but no range is stated"), ("U", "no record"),
                  ("U", "algorithmic governance may constrain contestability (published rationale)"), ("U", "no record")],
    "holds at 0.5: technical adaptability high, political adaptability uncertain (published)")
c34("INT", 0.5, [("U", "the white paper names the loops that adjust parameters (FRS, CDS, OAD) but no adjustable range"),
                 ("U", "the white paper's greenhouse example is an illustration inside the design, not an observed update, so "
                       "'within 6 months of evidence' is projected, not shown"),
                 ("C", "its loop routes every correction through democratic deliberation among those affected"),
                 ("U", "'zero collapse during adaptation' is the illustration's outcome, not a record")],
    "falls from 1.0 to 0.5: a correction, on the precedent that a modelled or illustrated adjustment is not an observed one "
    "(CCO-PTF-CIP-SZH's C3.4, part (b1), was held at 0.5 for the same reason); flagged toward 1.0 for the design's own loop",
    flag=("1.0", "3.5"))
c34("CN", 0.5, [("U", "no share stated"),
                ("C", "the reform era is the development literature's leading example of evidence-based experimentation (published)"),
                ("S", "no process independent of the officials who made a decision lets those affected challenge and reverse it"),
                ("U", "no record read for this clause")],
    "holds at 0.5; published as contestable")
c34("QA", 0.5, [("U", "no share stated"),
                ("C", "after the 2014-2016 price fall it cut spending and re-organised within a short time (published)"),
                ("S", "no process independent of the officials who made a decision lets those affected challenge and reverse it"),
                ("U", "no record read for this clause")],
    "holds at 0.5; published as contestable")

NOTES["C3.4"] = (
    "C3.4 is class M with four clauses: parameter adjustability of at least 30%, policy updates within six months of "
    "evidence, changes open to challenge and reversal by those affected, and no collapse during adjustment. Seven units "
    "were not yet re-estimated. **Integral falls from 1.0 to 0.5**, a correction on the precedent of part (b1): its adjustment "
    "cycle is shown in the white paper's own illustration, which projects rather than observes, so clauses 1, 2 and 4 are not "
    "shown; the unit is flagged toward 1.0 for the design's deliberation loop. **Integral's total falls from 14.5 to 14.0, so "
    "first place is no longer shared with CCO-PTF-CIP-SZH unless another unit moves.** Status Quo, China and Qatar hold at "
    "0.5; Centrally Planned Socialism and Libertarian Minarchism hold at 0.0; Fully Automated Luxury Communism holds at 0.5. "
    "No figure is recomputed here: the readings rest on dated public events and on the published rationales.")


def checks_C34(check, p):
    print("\n[C3.4] THE CRITERION")
    d = p.v2["C3.4"]["definition"]
    check(p.v2["C3.4"]["revision"]["cls"] == "M" and len(d["clauses"]) == 4 and "6 months" in d["clauses"][1],
          "C3.4 is class M with four clauses in v2.0: adjustability, updates within six months, challenge and reversal, no collapse")


# =========================================================================================================================
# C4.5 EXPLOITATION ELIMINATION (class D: a unit keeps or raises its score; v2.0 deleted the residual-coercion clause)
# 1 extraction rates < 10% of GDP; 2 genuine exit rights from exploitative relationships
# =========================================================================================================================
def d_hold(code, crit, verdict, c1, c2, why, flag=None, zero=None, note_extra=""):
    rep = REP(code, crit)
    U(code, crit, verdict, [(c1[0], c1[1], rep), (c2[0], c2[1], rep)], flag=flag, zero=zero,
      note=why + ("; " + note_extra if note_extra else ""))


X0 = ("U", "no extraction rate is stated for the unit")
X1 = ("U", "no exit-rights evidence is stated beyond the published rationale")
ZD = "the published 0.0 stands: the extraction is structural, as the published rationale states (protocol 2.1, third condition)"
d_hold("SQ", "C4.5", 0.0, ("S", "42% of GDP is extracted from labor to capital, with landlord-tenant extraction of $380,000 over 20 years "
                               "(published rationale)"), X1, "held at 0.0 (class D: keeps or raises)", zero=ZD)
d_hold("NSD", "C4.5", 0.5, ("S", "reduced by labor protections, bargaining and taxation but capital-labor extraction remains"), X1,
       "held at 0.5; this is the 0.5 band's own example")
d_hold("MS", "C4.5", 0.5, ("S", "capital-labor extraction is removed, but inter-cooperative extraction persists under market competition"),
       X1, "held at 0.5")
d_hold("MMT", "C4.5", 0.5, ("S", "the job guarantee removes the most desperate exploitation, but employment relations continue"),
       X1, "held at 0.5")
d_hold("SC", "C4.5", 0.5, ("S", "capital-labor extraction is structurally unchanged, with better terms in some firms"), X1, "held at 0.5")
d_hold("PE", "C4.5", 0.5, ("C", "the design has no capital owners and no managerial hierarchy, so the extraction channels v2.0 names "
                               "(employer-employee, landlord-tenant, creditor-debtor) are removed by design"),
       ("U", "the design requires comprehensive participation; exit from exploitative relationships is not shown"),
       "rises from 0.0 to 0.5: the published 0.0 rested on coordination burdens and informal hierarchy, the residual-coercion "
       "reading v2.0 deleted from C4.5 (K5), so a class D unit cannot stay below a 0.5 whose mechanism is cleared on clause 1",
       flag=("0.0", "3.6"), note_extra="this rise puts PE level with CCO-PTF-CIP-SZH at 14.5; flagged toward 0.0 for the published "
                                       "'different form of exploitation' reading")
d_hold("CCO", "C4.5", 0.5, ("S", "unconditional security and the land trust remove the most desperate exploitation and landlord-tenant "
                                 "extraction, but the market economy continues alongside"), X1, "held at 0.5")
d_hold("GEO", "C4.5", 0.5, ("S", "land-rent capture addresses landlord-tenant extraction only, and partially"), X1, "held at 0.5")
d_hold("MC", "C4.5", 0.5, ("S", "interest-based extraction is removed within the mechanism's transactions, not outside them"), X1,
       "held at 0.5")
d_hold("DE", "C4.5", 0.0, ("U", "no structural change to the three named relationships was located"), X1, "held at 0.0 (class D)",
       zero="no structural mechanism addresses the three extraction relationships (protocol 2.1, first condition)")
d_hold("UBS", "C4.5", 0.5, ("S", "the shelter sector reduces landlord-tenant extraction; the other two relationships are unaddressed"), X1,
       "held at 0.5")
d_hold("SWF", "C4.5", 0.0, ("U", "no structural connection to any of the three extraction channels was located"), X1,
       "held at 0.0 (class D)",
       zero="no structural mechanism addresses the three extraction relationships (protocol 2.1, first condition)")
d_hold("CN", "C4.5", 0.0, ("S", "private firms stay the main employers, so the precedent that credited abolition of private capital does "
                               "not transfer (published rationale)"), X1, "held at 0.0 (class D)", zero=ZD)
d_hold("SG", "C4.5", 0.0, ("S", "extraction is structural, through a large low-wage workforce with little bargaining power (published)"),
       X1, "held at 0.0 (class D)", zero=ZD)
d_hold("QA", "C4.5", 0.0, ("S", "extraction from migrant labour is load-bearing: Qataris were about 5% of the labour force in 2018 (published)"),
       X1, "held at 0.0 (class D)", zero=ZD)
d_hold("IF", "C4.5", 0.5, X0, X1, "held at 0.5; published as contestable")
d_hold("OS", "C4.5", 0.5, X0, X1, "held at 0.5; published as contestable")

NOTES["C4.5"] = (
    "C4.5 is class D: v2.0 deleted the clause on the share of decisions made under duress (measured once, in C2.1), so a "
    "unit keeps or raises its score. Seventeen units were not yet re-estimated and are read on the two remaining clauses: "
    "extraction rates below 10% of GDP, and genuine exit rights from exploitative relationships. No unit shows clause 2, so "
    "none is 1.0. **Participatory Economics rises from 0.0 to 0.5**: the design removes the three extraction relationships "
    "(clause 1 cleared), and its published 0.0 rested on coordination burdens and informal hierarchy, the residual-coercion "
    "reading v2.0 deleted. **This puts it level with CCO-PTF-CIP-SZH at 14.5 for first place**, and it is flagged toward 0.0. "
    "The other sixteen hold; the seven 0.0s rest on structural extraction (Status Quo, China, Singapore, Qatar) or on no "
    "structural connection to the three relationships (Doughnut Economics, Sovereign Wealth Fund Statism).")


def checks_C45(check, p):
    print("\n[C4.5] THE CRITERION")
    d = p.v2["C4.5"]["definition"]
    check(p.v2["C4.5"]["revision"]["cls"] == "D" and len(d["clauses"]) == 2 and "10% GDP" in d["clauses"][0],
          "C4.5 is class D with two clauses in v2.0: extraction rates below 10% of GDP, exit rights; no unit falls")
    check(all(r["verdict"] >= p.vec[k][c] for (k, c), r in UNITS.items() if c == "C4.5"), "no C4.5 unit falls (class D)")


# =========================================================================================================================
# C2.5 EXIT RIGHTS AND MOBILITY (class D: v2.0 deleted the association clause; a 0.5 whose only unshown clause was it rises)
# 1 exit within 3 months without material penalty; 2 no differential treatment; 3 geographic mobility maintained
# =========================================================================================================================
def c25(code, verdict, why, zero=None, c1=None):
    rep = REP(code, "C2.5")
    nm = "the published rationale does not rest on the deleted association clause"
    U(code, "C2.5", verdict,
      [("U", c1 or "not re-read in this pass (class D)", rep), ("U", "not re-read in this pass (class D)", rep),
       ("U", "not re-read in this pass (class D)", rep)],
      note=why + "; " + nm, zero=zero)


Z25 = "the published 0.0 stands: the published rationale is a whole-criterion finding on participation (protocol 2.1, third condition)"
c25("SQ", 0.5, "held at 0.5: job-mobility costs, healthcare tied to employment and housing barriers are the short clauses")
c25("NSD", 0.0, "held at 0.0: the funding model needs near-universal participation", zero=Z25)
c25("CPS", 0.5, "held at 0.5: the propiska and job assignment limit mobility, with slight credit for formal assignment")
c25("MS", 0.0, "held at 0.0: the system needs comprehensive adoption", zero=Z25)
c25("MMT", 0.5, "held at 0.5: exit from private employment into the job guarantee, but not from employment")
c25("UBI", 0.0, "held at 0.0: the funding model needs universal participation", zero=Z25)
c25("DG", 0.0, "held at 0.0: ecological compliance needs comprehensive participation", zero=Z25)
c25("SC", 0.5, "held at 0.5: formally free and economically constrained")
c25("FALC", 0.0, "held at 0.0: the automation infrastructure needs comprehensive participation", zero=Z25)
c25("PE", 0.5, "held at 0.5: councils can be changed but the system requires comprehensive participation")
c25("CN", 0.5, "held at 0.5: hukou differential treatment and exit bans are the short clauses (published)")
c25("SG", 0.5, "held at 0.5: formal exit available; Freedom House movement score 3 of 4 (published)")
c25("QA", 0.5, "held at 0.5: the exit permit for migrant workers has gone (ILO), other restrictions remain (published)")

NOTES["C2.5"] = (
    "C2.5 is class D: v2.0 deleted the fourth clause (voluntary association, now measured once in C2.6), so a unit keeps "
    "or raises its score, and a 0.5 whose only unshown clause was association rises. Thirteen units were not yet "
    "re-estimated. The published rationale of each of the eight 0.5s was read for that clause and none rests on it (each "
    "names exit, differential treatment or mobility), so **nothing rises: all 13 hold**. The five 0.0s (Nordic Social "
    "Democracy, Market Socialism, Universal Basic Income, Degrowth, Fully Automated Luxury Communism) rest on the "
    "published finding that the system cannot function with large-scale opt-out, a whole-criterion reason that the "
    "deleted clause does not touch. Anyone who can show a unit's exit terms differ from its published rationale can "
    "challenge the unit through the site's contribution route.")


def checks_C25(check, p):
    print("\n[C2.5] THE CRITERION")
    d = p.v2["C2.5"]["definition"]
    check(p.v2["C2.5"]["revision"]["cls"] == "D" and len(d["clauses"]) == 3 and "3 months" in d["clauses"][0],
          "C2.5 is class D with three clauses in v2.0 (the association clause deleted); no unit falls")
    check(all(r["verdict"] >= p.vec[k][c] for (k, c), r in UNITS.items() if c == "C2.5"), "no C2.5 unit falls (class D)")


def checks_C44(check, p):
    print("\n[C4.4] THE CACHE AND THE CLASSIFICATIONS THE READINGS QUOTE")
    d = p.v2["C4.4"]["definition"]
    check(p.v2["C4.4"]["revision"]["cls"] == "M" and len(d["clauses"]) == 2 and "80%" in d["clauses"][0],
          "C4.4 is class M with two clauses in v2.0: accountability for at least 80% of major decisions, functional removal")
    for name, want in C44_MD5.items():
        raw = open(os.path.join(HERE, C44, name), "rb").read()
        check(hashlib.md5(raw).hexdigest() == want, f"{C44}{name}: md5 {want[:8]}")
    got = {e: regime(e) for e in ("United States", "China", "Singapore", "Qatar", "Denmark", "Finland", "Norway", "Sweden")}
    check(got == {"United States": 3, "China": 0, "Singapore": 1, "Qatar": 0, "Denmark": 3, "Finland": 3, "Norway": 3, "Sweden": 3},
          "2024 regimes: United States liberal democracy; China and Qatar closed autocracies; Singapore an electoral autocracy")


CHECKS = {"C4.1": checks_C41, "C4.4": checks_C44, "C3.4": checks_C34, "C4.5": checks_C45, "C2.5": checks_C25}


# =========================================================================================================================
# the checks, the tables, the record
# =========================================================================================================================
def build_record(t, p):
    L = ["# NEEC Rescoring Pass — Record, Stage 2, accelerated groups (2.11 onward)", "",
         "**Session 65 · 2026-10-15 · Scorer and engineer: Claude · Owner: Duke Johnson**",
         "**Status: scratch (protocol 10.1).** Generated by `rescoring_s65.py` (harness check 111); the script is the source "
         "of every table below and the check compares this file with its output byte for byte. Decision 65.1 (delegated, "
         "optional): at the owner's request to finish the pass in one or two sessions the remaining criteria are read in one "
         "script and one record, on the rules of groups 2.2 to 2.10. No score changes until stage 3 applies the pass by "
         "generator.", "",
         "Criteria in this record: " + ", ".join(f"{c} {p.v2[c]['name']}" for c in CRITS) + ".", ""]
    for c in CRITS:
        L += [f"## {c} {p.v2[c]['name']}", "", NOTES[c], "", t[f"summary {c}"], ""]
        for code in [k for (k, cc) in UNITS if cc == c]:
            L += [t[f"unit {code} {c}"], ""]
    L += ["## Consequences", "", t["consequences"], "", t["dominance"], "", t["ledger"], "", t["anchors"], ""]
    return "\n".join(L)


def main():
    ok = True

    def check(cond, text, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'} {text}" + ("" if cond or not detail else f": {detail}"))
        ok = ok and bool(cond)
        return cond

    with redirect_stdout(io.StringIO()):
        idx = [x[0] for x in pc.PARTS].index(TAG)
        p = pc.Pass(upto=idx)
    print(f"NEEC rescoring pass, stage 2, accelerated groups: {', '.join(CRITS)} ({RECORD})")
    print(f"inputs: {pc.CRITERIA}, {pc.CRIT44}, {pc.CORPUS}, pass_common.py and the {idx} parts before this one, the cache, "
          f"the scoring documents, {RECORD}\n")

    print("[1] THE GROUPS")
    for c in CRITS:
        mine = [k for k in p.order if (k, c) in UNITS]
        before = [k for k in p.order if (k, c) in p.merged]
        check(sorted(mine + before) == sorted(p.order) and len(mine) == sum(1 for (_, cc) in UNITS if cc == c),
              f"{c}: one unit per entry not yet re-estimated ({len(mine)}); {len(before)} were re-estimated before and are not re-read")
        pub = {k: p.vec[k][c] for k in p.order}
        rise = [k for k in mine if UNITS[(k, c)]["verdict"] > pub[k]]
        fall = [k for k in mine if UNITS[(k, c)]["verdict"] < pub[k]]
        check(True, f"{c}: raises {len(rise)} ({', '.join(rise)}), lowers {len(fall)} ({', '.join(fall)}), holds "
                    f"{len(mine) - len(rise) - len(fall)}")
        bad = [k for k in mine if not rat_head(k, c)[2].startswith(f"{c} {p.v2[c]['name']}: {pc.f1(pub[k])}")]
        check(not bad, f"{c}: each published rationale is found by heading at its published score", ", ".join(bad))
    for c in CRITS:
        CHECKS[c](check, p)

    print("\n[3] FLAGS")
    fl = {k: v for k, v in UNITS.items() if v["flag"]}
    vn = p.vectors([UNITS], start=p.vsteps[-1])[-1]
    tiers = []
    for (code, c), r in fl.items():
        v = dict(vn[code])
        v[c] = float(r["flag"][0][:3])
        if pc.tier(sum(1 for k in p.cids if vn[code][k] == 0.0)) != pc.tier(sum(1 for k in p.cids if v[k] == 0.0)):
            tiers.append(f"{code} {c}")
    FLAGS_TIER["tier"] = sorted(tiers)
    check(True, f"{len(fl)} flags ({', '.join(f'{k[0]} {k[1]} toward {v['flag'][0]}' for k, v in fl.items())}); those that could change a tier: {', '.join(sorted(tiers)) or 'none'}")

    print("\n[4] THE SHARED MODULE'S CHECKS (records, the rule, consequences, ledger, dominance, anchors)")
    good, t = pc.run_group(p, TAG, UNITS, RECORD, "After group 2.10", "After the accelerated groups")
    ok = ok and good

    for c in CRITS:
        cl = p.v2[c]["definition"]["clauses"]
        pub = {k: p.vec[k][c] for k in p.order}
        rows_ = ["| Entry | Published | " + " | ".join(f"Clause {i + 1}" for i in range(len(cl))) + " | Verdict | Flag |",
                 "|---|---:|" + "---|" * len(cl) + "---:|---|"]
        for (code, cc), r in UNITS.items():
            if cc != c:
                continue
            rows_.append(f"| {code} | {pc.f1(pub[code])} | " + " | ".join(pc.STATUS[x[0]] for x in r["clauses"]) +
                         f" | {pc.f1(r['verdict'])} | {('toward ' + r['flag'][0][:3]) if r['flag'] else ''} |")
        t[f"summary {c}"] = "\n".join(rows_)
        for (code, cc), r in UNITS.items():
            if cc != c:
                continue
            lines = [f"#### {code} {c} {p.v2[c]['name']}: {pc.f1(pub[code])} → {pc.f1(r['verdict'])}", "",
                     "| # | Clause (v2.0) | Status | Estimate | Source |", "|---:|---|---|---|---|"]
            for i, (s_, est, src_) in enumerate(r["clauses"]):
                lines.append(f"| {i + 1} | {cl[i]} | {pc.STATUS[s_]} | {est} | {src_} |")
            if r["zero"]:
                lines += ["", f"*0.0 (protocol 2.1):* {r['zero']}."]
            if r["flag"]:
                lines += ["", f"*Flag (reading {r['flag'][1]}):* toward {r['flag'][0]}."]
            if r["note"]:
                lines += ["", f"*Note:* {r['note']}."]
            t[f"unit {code} {c}"] = "\n".join(lines)
    rec = build_record(t, p)
    if "--write-record" in sys.argv[1:]:
        open(os.path.join(HERE, RECORD), "w", encoding="utf-8").write(rec)
        print(f"  wrote {RECORD}")
    else:
        have = open(os.path.join(HERE, RECORD), encoding="utf-8").read() if os.path.isfile(os.path.join(HERE, RECORD)) else ""
        check(have == rec, f"{RECORD} equals the record this script generates")
    print()
    print("\n\n".join(t[f"summary {c}"] for c in CRITS))
    print()
    print(t["consequences"])
    print("\nRESCORING STAGE 2, ACCELERATED GROUPS, COMPUTED." if ok else "\nRESCORING STAGE 2, ACCELERATED GROUPS: CHECKS FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
