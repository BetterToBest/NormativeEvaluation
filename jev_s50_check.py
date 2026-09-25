#!/usr/bin/env python3
"""
jev_s50_check.py -- the automated interpretation check (decisions 50.1 to 50.4) on part (b)'s ninth group
=========================================================================================================
Session 50. Jev (TypeSafe AI's System One model, pinned jev-1.13.0, through the Composio Jev toolkit) was asked, clause
by clause, whether a state meets a clause of C5.2, C5.4 or C5.5 as the pass reads it (NEEC_Rescoring_s50.md,
readings 3.2 to 3.6), and its answers are compared here with the pass's clause statuses (rescoring_s50.py). The check
is flag-only: a disagreement routes a unit to review; it never changes a score and is not a replication (50.2).

STATES hold published or source text and the pass's located evidence, never a verdict or the scorer's reasoning
(50.4): the entry's Report v1.6 rationale (score removed) or its scoring document's passage, and, where the pass
cleared or refused a clause on evidence it located, that evidence as the record states it (each excerpt is checked to
be verbatim in the unit's clause estimate in rescoring_s50.py). The ISSP state quotes the survey's question wording
from the GESIS variable report, which is not in the repository (PDF md5 9f3ca6fd); its results line is checked
against rescoring_s50.py. QUESTIONS: one clause per question; the instruction restates the pass's reading; the one
comparison of figures with a bar (the ISSP shares against 65%) is made in rescoring_s50.py, not by Jev.

CHECKS: every request is rebuilt here from its sources and must equal the recorded request; every record is answered
by jev-1.13.0; then each question's modal answer across the runs is compared with the pass's status (cleared against
not cleared). Prints the table. Writes nothing. Makes no network call.

Usage: python3 jev_s50_check.py              (reads jev_s50_2026-09-25.json, NEEC_Report_v1_6.md,
                                              NEEC_IslamicFinance_scoring_scratch.md,
                                              NEEC_MutualCredit_LETS_scoring_scratch.md, jev_pilot_check.py and
                                              rescoring_s50.py with the files it reads, beside itself)
       python3 jev_s50_check.py --requests   (prints the requests as JSON, for sending; used once, in Session 50)
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA, REPORT, MODEL = "jev_s50_2026-09-25.json", "NEEC_Report_v1_6.md", "jev-1.13.0"
IFDOC, MCDOC = "NEEC_IslamicFinance_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md"
ONLY = ("Judge only what the state itself says (the entry's text and any located evidence it lists). Do not use "
        "outside knowledge about the system or its history.")
FEAS = ("The criterion requires this element to be \"shown feasible by precedent or component evidence\", not only "
        "planned. A precedent is a deployment that actually took place, of this system or of institutions of the same "
        "kind. Component evidence is such a deployment of a component the entry itself names. A plan, a stated "
        "sequence or timeline, a claim that it could be done, a simulation, or a programme of a different kind cited "
        "only for its speed does not count. ")

Q = {
    "C5.2/1": {"type": "choice", "instructions": "The clause under test is \"Staged (≥4 phases)\". " + FEAS + ONLY,
               "criteria": {
                   "shown": "The state cites a deployment that actually took place, of the system or of a component of "
                            "the same kind that the entry names, carried out in at least four successive stages.",
                   "short": "The state cites a staged deployment that took place, or specifies a staged pathway, but "
                            "with fewer than four stages.",
                   "planned_only": "The state specifies or claims a staged pathway, but cites no deployment of the same "
                                   "kind that took place in stages.",
                   "not_stated": "The state gives no staged pathway and no staged deployment."}},
    "C5.2/2": {"type": "choice", "instructions": "The clause under test is \"rapid (≤36 months) deployment\". " + FEAS
               + ONLY,
               "criteria": {
                   "shown": "The state cites a deployment that actually took place, of the system or of a component of "
                            "the same kind that the entry names, completed within 36 months, and, if the entry names "
                            "several defining components, such a deployment for each of them.",
                   "partial": "The state cites deployments within 36 months for some of the components the entry names "
                              "as defining, but for at least one of them only a slower deployment or none.",
                   "planned_only": "The state specifies or claims a rapid pathway of 36 months or less, but cites no "
                                   "deployment of the same kind completed within that time; any precedent it cites is a "
                                   "programme of a different kind, cited for its speed.",
                   "not_stated": "The state gives no rapid pathway and no deployment within 36 months."}},
    "C5.2/4": {"type": "choice", "instructions": "The clause under test is \"resource requirements\". " + FEAS + ONLY,
               "criteria": {
                   "shown": "The state gives the resources the deployment requires (funds, capital, staff or "
                            "institutions) and cites a deployment that took place with resources of that kind and size.",
                   "stated_only": "The state gives resource requirements but cites no deployment showing them "
                                  "sufficient.",
                   "not_stated": "The state gives no resource requirements for the deployment."}},
    "C5.4/1": {"type": "choice",
               "instructions": "The clause under test is \"≥60% support across political spectrum\", for the system "
                               "the state describes. Support for a component of the system, or for a different "
                               "programme, is not support for the system itself. " + ONLY,
               "criteria": {
                   "asserted_met": "The state says that at least 60% of people, across the political spectrum, support "
                                   "or are satisfied with the system itself.",
                   "component_only": "The state gives such support only for a component of the system or for a "
                                     "different programme.",
                   "not_asserted": "The state gives no level of support for the system across the spectrum, or a level "
                                   "below 60%."}},
    "C5.4/2": {"type": "choice",
               "instructions": "The clause under test is \"≥65% opposition to repeal\", for the system the state "
                               "describes. A design with no record shows it by a projection, from a model or from "
                               "calibrated components; evidence for one component or an assumption of support is not a "
                               "projection for the system. " + ONLY,
               "criteria": {
                   "shown": "The state gives a record or a projection that at least 65% of people oppose, or would "
                            "oppose, repealing the system itself.",
                   "component_only": "The state gives such evidence only for a component of the system or a different "
                                     "programme, or states only an assumption of support.",
                   "not_shown": "The state gives no record or projection of opposition to the system's repeal."}},
    "C5.4/2m": {"type": "choice",
                "instructions": "The clause under test is \"≥65% opposition to repeal\" of the Nordic welfare-state "
                                "system. The state reports survey items and their results. The comparison of the "
                                "figures with 65% is made separately: judge only whether the survey items measure "
                                "opposition to repealing the system or its core provision. " + ONLY,
                "criteria": {
                    "measures_opposition": "The items ask whether people want the system's core provision (such as "
                                           "health care and pensions) kept at least at its present level, or held a "
                                           "government responsibility, so the share answering so is a share opposed to "
                                           "repealing it.",
                    "other_measure": "The items measure something other than opposition to repeal or cuts (for example "
                                     "satisfaction, trust or general attitudes), so the shares are not shares opposed "
                                     "to the system's repeal."}},
    "C5.4/3": {"type": "choice",
               "instructions": "The clause under test is \"survival probability ≥80% across administration changes\", "
                               "for the system the state describes. A design with no record shows it by a projection; "
                               "a component's record is not the system's. " + ONLY,
               "criteria": {
                   "shown": "The state gives a record, or a projection, that the system itself has survived, or would "
                            "survive, at least 80% of changes of government or administration.",
                   "component_only": "The state gives such a record or projection only for a component of the system "
                                     "or a different programme.",
                   "not_shown": "The state gives no record or projection of the system's survival across changes of "
                                "administration."}},
    "C5.5/1": {"type": "choice",
               "instructions": "The clause under test is \"Viable across ≥3 economic contexts (high/middle/low "
                               "income)\". " + ONLY,
               "criteria": {
                   "shown": "The state shows or argues that the system is viable in high-, middle- and low-income "
                            "economies, covering each.",
                   "not_shown": "The state does not address viability across income levels, or covers fewer than "
                                "three."}},
    "C5.5/3": {"type": "choice",
               "instructions": "The clause under test is \"parameter flexibility ≥40% adjustment range\". Parameters "
                               "that each local network sets for itself, with no common value fixed by the design, "
                               "count as flexible without limit. " + ONLY,
               "criteria": {
                   "shown": "The state shows that the system's key parameters (such as credit limits, fees or rates) "
                            "are adjusted by a range of at least 40%, or are set by each network with no common value.",
                   "not_shown": "The state names no adjustable parameters, or gives a fixed range narrower than 40%."}},
    "C5.5/4": {"type": "choice",
               "instructions": "The clause under test is \"successful operation validated across diverse "
                               "implementations\". A design with no implementation cannot show it by modelling or by "
                               "its capacities. " + ONLY,
               "criteria": {
                   "shown": "The state cites successful operation of the system itself in several implementations in "
                            "diverse contexts.",
                   "component_only": "The state cites implementations only of parts of the system, or of a narrower or "
                                     "different arrangement.",
                   "not_shown": "The state cites no implementation of the system; it describes design features, "
                                "capacities or possibilities."}},
}
CLEARED = {"shown", "asserted_met", "measures_opposition"}

# The ISSP items as the GESIS variable report words them (ZA6900 v2.0.0, Q6b, Q6f, Q7c, Q7d).
ISSP_WORDING = [
    "Q6: Listed below are various areas of government spending. Please show whether you would like to see more or "
    "less government spending in each area. Remember that if you say 'much more', it might require a tax increase to "
    "pay for it. Q6b: Health. Q6f: Old age pensions. (Spend much more; spend more; spend the same as now; spend less; "
    "spend much less.)",
    "Q7: On the whole, do you think it should or should not be the government's responsibility to... Q7c: ...provide "
    "health care for the sick. Q7d: ...provide a decent standard of living for the old. (Definitely should be; "
    "probably should be; probably should not be; definitely should not be.)"]

# (unit, criterion, entry text, located-evidence excerpts (verbatim in the unit's clause estimates), questions)
# Entry text: ("report", code, criterion) for Report v1.6's rationale; ("doc", file, start, end) for a passage of a
# scoring document, lines start to end inclusive, joined with spaces; ("overview", code) for the Report's overview.
TESTS = [
    ("NSD", "C5.2", [("report", "NSD", "C5.2"), ("overview", "NSD")],
     ["crisis policy and the Saltsjöbaden Agreement (1932-1938), the universal pension and child allowance "
      "(1946-1948), compulsory health insurance and the earnings-related pension (1955-1960), and parental insurance "
      "and the Co-determination Act (1974-1976)",
      "its universal social insurance has a precedent of rapid deployment elsewhere (Britain's, legislated in 1946 and "
      "in force by July 1948)",
      "Sweden's took from the December Compromise of 1906 to the Saltsjöbaden Agreement of 1938"],
     {"clause1": ("C5.2/1", 0), "clause2": ("C5.2/2", 1)}),
    ("LM", "C5.2", [("report", "LM", "C5.2")], [], {"clause1": ("C5.2/1", 0), "clause2": ("C5.2/2", 1)}),
    ("SC", "C5.2", [("report", "SC", "C5.2"), ("overview", "SC")],
     ["the Coal and Steel Codetermination Act (1951), the Works Constitution Act (1952), its revision (1972) and the "
      "Codetermination Act (1976)",
      "Germany's took a quarter-century, from 1951 to 1976"],
     {"clause1": ("C5.2/1", 0), "clause2": ("C5.2/2", 1)}),
    ("MMT", "C5.2", [("report", "MMT", "C5.2")],
     ["India's rural employment guarantee, extended to all districts in three phases between 2006 and 2008",
      "Argentina's Plan Jefes y Jefas de Hogar, a public employment programme begun in April 2002 in the crisis, whose "
      "payrolls ballooned quickly, against a government estimate of 500,000, to nearly 2 million participants, 13% of "
      "the labour force, at a cost peaking at 1% of GDP"],
     {"clause1": ("C5.2/1", 0), "clause2": ("C5.2/2", 1)}),
    ("IF", "C5.2", [("doc", IFDOC, 643, 659)],
     ["the Islamic Banking Act and the first Islamic bank (1983), the interest-free banking scheme for conventional "
      "banks (1993), the Shariah Advisory Council (1997) and the Islamic Financial Services Act (2013)",
      "reports of Pakistan's 2026 roadmap say that banks' Islamic windows already hold the technology and that staff "
      "training is under way, but give no estimate of cost, capital or staff"],
     {"clause1": ("C5.2/1", 0), "clause2": ("C5.2/2", 1), "clause4": ("C5.2/4", 3)}),
    ("CCO", "C5.2", [("report", "CCO", "C5.2")], [], {"clause1": ("C5.2/1", 0), "clause2": ("C5.2/2", 1)}),
    ("NSD", "C5.4", [("report", "NSD", "C5.4")],
     ["the configuration's universal social insurance and public services have been kept through every change of "
      "government since they were built, including centre-right governments in all four countries: Sweden 1976-1982, "
      "1991-1994, 2006-2014 and from 2022; Denmark 1982-1993, 2001-2011 and 2015-2019; Norway 1981-1986, 1989-1990, "
      "1997-2000, 2001-2005 and 2013-2021; Finland 1991-1995, 2015-2019 and from 2023"],
     {"clause1": ("C5.4/1", 0), "clause3": ("C5.4/3", 2)}),
    ("NSD", "C5.4", [("issp",)], ["in the ISSP's 2016 Role of Government module, 95.0 to 99.3% of those answering in "
                                  "each of the four countries wanted government spending on health, and on old age "
                                  "pensions, kept at its level or raised, and 95.5 to 99.7% held that health care for the "
                                  "sick and a decent standard of living for the old should be the government's "
                                  "responsibility"],
     {"clause2": ("C5.4/2m", 1)}),
    ("CCO", "C5.4", [("report", "CCO", "C5.4")], [],
     {"clause1": ("C5.4/1", 0), "clause2": ("C5.4/2", 1), "clause3": ("C5.4/3", 2)}),
    ("PE", "C5.5", [("report", "PE", "C5.5")], [], {"clause1": ("C5.5/1", 0), "clause4": ("C5.5/4", 3)}),
    ("MC", "C5.5", [("doc", MCDOC, 743, 755)],
     ["each network sets its members' credit limits on their demonstrated capacity to contribute and adjusts its own "
      "rules, and its implementations differ in kind, most with no interest or fee on balances and some with "
      "demurrage"],
     {"clause3": ("C5.5/3", 2), "clause4": ("C5.5/4", 3)}),
]
NAMES = {"C5.2": "Staged Transition Pathways", "C5.4": "Political Coalition Potential", "C5.5": "Cultural Adaptability"}
FAILS = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        FAILS.append(msg)


def load(name):
    spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def build():
    """Every request, rebuilt from its sources; and each state excerpt's provenance check."""
    jp, r50 = load("jev_pilot_check.py"), load("rescoring_s50.py")
    with contextlib.redirect_stdout(io.StringIO()):   # fills the ISSP range into Nordic Social Democracy's estimate
        argv, sys.argv = sys.argv, [sys.argv[0]]
        try:
            r50.main()
        finally:
            sys.argv = argv
    lines = open(os.path.join(HERE, REPORT), encoding="utf-8").read().split("\n")
    over = [re.sub(r"^## \*\*Overview:\*\*\s*", "", l).strip() for l in lines if l.startswith("## **Overview:**")]
    overview = dict(zip(jp.ORDER, over))
    texts = {g: jp.report_texts(g, re.escape(NAMES[g]))[1] for g in NAMES}
    reqs, prov = [], []
    for unit, crit, entry, evidence, qs in TESTS:
        parts = []
        for e in entry:
            if e[0] == "report":   # cut at the next heading: C5.5 ends an entry, so the extract runs on into it
                parts.append(texts[e[2]][e[1]].split("\n\n#")[0].strip())
            elif e[0] == "overview":
                parts.append(overview[e[1]])
            elif e[0] == "doc":
                doc = open(os.path.join(HERE, e[1]), encoding="utf-8").read().split("\n")
                parts.append(re.sub(r"\s+", " ", " ".join(doc[e[2] - 1:e[3]])).strip())
        estimates = " ".join(est for _, est, _ in r50.UNITS[(unit, crit)]["clauses"])
        prov.append((unit, crit, [x in estimates for x in evidence]))
        state = {"system": unit + " (an economic system in the NEEC corpus)"}
        if entry[0][0] == "issp":
            state.update(survey_items=ISSP_WORDING, results=evidence)
        else:
            state["entry_text"] = " ".join(parts)
            if evidence:
                state["located_evidence"] = evidence
        questions = {name: dict(Q[qid], instructions=Q[qid]["instructions"]) for name, (qid, _) in qs.items()}
        reqs.append(dict(unit=unit, criterion=crit, request=dict(model=MODEL, state=state, questions=questions)))
    return reqs, prov, r50


def main():
    reqs, prov, r50 = build()
    if "--requests" in sys.argv[1:]:
        print(json.dumps([r["request"] for r in reqs], ensure_ascii=False))
        return 0
    data = json.load(open(os.path.join(HERE, DATA), encoding="utf-8"))
    recs = data["records"]
    runs = sorted({r["run"] for r in recs})
    print(f"Jev interpretation check, part (b)'s ninth group ({DATA}; {data['model']}; runs {runs})\n")
    check(all(all(ok) for _, _, ok in prov),
          "every located-evidence excerpt in a state is verbatim in the unit's clause estimates (rescoring_s50.py)")
    same = all(sum(1 for r in recs if r["run"] == n and r["index"] == i and r["request"] == q["request"]) == 1
               for n in runs for i, q in enumerate(reqs))
    check(same and len(recs) == len(runs) * len(reqs),
          f"every recorded request equals the request rebuilt here from its sources ({len(reqs)} states, "
          f"{len(runs)} runs, {len(recs)} records)")
    check(all(r["error"] is None and r["response"]["model"] == MODEL for r in recs)
          and all(set(r["response"]["answers"]) == set(r["request"]["questions"]) for r in recs),
          f"every record is answered, by {MODEL}, for every question asked")
    print("\n  %-5s %-5s %-8s %-9s %-20s %-11s %-11s %s" % ("unit", "crit", "clause", "pass", "Jev (modal)", "P(choice)",
                                                           "confidence", "agree"))
    agree = n = 0
    dis = []
    for i, q in enumerate(reqs):
        rec = r50.UNITS[(q["unit"], q["criterion"])]
        for name, (qid, k) in {nm: v for t in TESTS[i:i + 1] for nm, v in t[4].items()}.items():
            ans = [r["response"]["answers"][name] for r in recs if r["index"] == i]
            picks = [a["choice"] for a in ans]
            modal = max(set(picks), key=picks.count)
            st = rec["clauses"][k][0]
            ok = (st == "C") == (modal in CLEARED)
            agree, n = agree + ok, n + 1
            pr = [a["probabilities"][a["choice"]] for a in ans]
            cf = [a["confidence"] for a in ans]
            span = lambda xs: (lambda a, b: a if a == b else f"{a}-{b}")(f"{min(xs):.2f}", f"{max(xs):.2f}")
            print("  %-5s %-5s %-8s %-9s %-20s %-11s %-11s %s" % (
                q["unit"], q["criterion"], name, r50.STATUS[st], modal + ("" if len(set(picks)) == 1 else "*"),
                span(pr), span(cf), "yes" if ok else "NO"))
            if not ok:
                dis.append(f"{q['unit']} {q['criterion']} {name}")
    stable = all(len({r["response"]["answers"][nm]["choice"] for r in recs if r["index"] == i}) == 1
                 for i, q in enumerate(reqs) for nm in q["request"]["questions"])
    print(f"\n  (* the runs differ; the modal answer is shown)")
    print(f"  every question returned the same option in every run: {'yes' if stable else 'no'}")
    print("  disagreements (flag-only; decision 50.2): " + (", ".join(dis) or "none"))
    print(f"\nSUMMARY: {agree} of {n} clause verdicts agree; {len(dis)} flagged for review; "
          f"{len(FAILS)} checks failed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
