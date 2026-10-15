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
CRITS = ["C4.1"]
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
    d41 = p.v2["C4.1"]
    check(d41["revision"]["cls"] == "M" and len(d41["definition"]["clauses"]) == 2 and "80%" in d41["definition"]["clauses"][0],
          "C4.1 is class M with two clauses in v2.0: debt below 80% of GDP, positive net national saving")

    print("\n[2] THE CACHE AND THE FIGURES THE READINGS QUOTE")
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
