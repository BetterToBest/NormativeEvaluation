#!/usr/bin/env python3
"""
verify_protocol_s36.py -- NEEC Session 36: the scoring protocol's own statements, checked
========================================================================================
Protocol draft.4 made statements about the corpus (in 3.5, 6.4 and elsewhere) that no script checked, and
two of them went stale when decisions D18(b) and D26 were applied in Session 33. Draft.5 (Session 36) is the
first version whose corpus-dependent statements are asserted, in the manner of protocol 8.3: each statement
must occur in SCORING_PROTOCOL.md verbatim (whitespace collapsed) AND its fact must hold on the corpus.

Groups:
  A  header and structure: the version, the sections draft.5 adds, horizontal rules that render as rules
  B  3.1: the classes the owner assigned (D17) are exactly the blocks with basis "assigned"
  C  5.1: the archetype table (D30) covers every corpus entry once, each archetype within one scope class;
     the peer rule's consequence stated in section 13; R8 readiness for the second pilot
  D  statements about entries: 3.4(a), 3.5, 6.1, 6.4, 6.5 and the D26, D29 and D31 notes of section 13
  E  4.6 against criteria.json: every anchor threshold is its definition; the corrections as counted
  F  Appendix B against criteria.json and r4_audit_s35.py's clause table
  G  section 13: the register's rows, in order, and a note for each decision since the delegation
  H  revisions R1 to R8, each named in its section
  I  superseded draft.4 statements are gone

Inputs, beside this script or in the working directory: SCORING_PROTOCOL.md, criteria.json,
neec_corpus.json, neec_entry.py (in corpus-file mode: the canonical script must NOT be beside it),
r4_audit_s35.py (imported for its clause table only), the eleven scoring documents that carry the 23 summary
blocks, and NEEC_OstromCommons_replication_scoring.md (the first pilot's declared peers).
Usage: python3 verify_protocol_s36.py     Exit 0 only if every check passes. Deterministic; changes no file.
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = ("NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
        "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
        "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "NEEC_StateCapitalism_China_scoring_scratch.md",
        "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
        "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
        "NEEC_Ostrom_Commons_scoring_scratch.md")
REPL_DOC = "NEEC_OstromCommons_replication_scoring.md"
CLASS_NAME = {"configured national economy": "configured_national_economy", "mechanism": "mechanism",
              "comprehensive system": "comprehensive_system"}


def path(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name}")


def load(name, mod):
    spec = importlib.util.spec_from_file_location(mod, path(name))
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


if os.path.isfile(os.path.join(os.getcwd(), "neec_weighting_robustness_analysis_v2.py")):
    sys.exit("ERROR: run without the canonical script beside this one (neec_entry.py must read neec_corpus.json)")
NE = load("neec_entry.py", "neec_entry")
R4 = load("r4_audit_s35.py", "r4_audit_s35")
PROTO = open(path("SCORING_PROTOCOL.md"), encoding="utf-8").read()
FLAT = re.sub(r"\s+", " ", PROTO.replace("**", ""))
CRIT = json.load(open(path("criteria.json"), encoding="utf-8"))
CORPUS = json.load(open(path("neec_corpus.json"), encoding="utf-8"))
ENTRIES = {e["key"]: e for e in CORPUS["entries"]}
BLOCKS = {}
for d in DOCS:
    for b in NE.blocks_in_markdown(open(path(d), encoding="utf-8").read()):
        BLOCKS[b["code"]] = b
REPL = NE.blocks_in_markdown(open(path(REPL_DOC), encoding="utf-8").read())[0]

RESULTS = []


def check(gid, cond, what, why=""):
    RESULTS.append((gid, bool(cond)))
    print(f"  [{gid}] {'PASS' if cond else 'FAIL'}  {what}" + ("" if cond or not why else f"  -- {why}"))


def says(phrase):
    return re.sub(r"\s+", " ", phrase.replace("**", "")) in FLAT


def section(head, stop=r"^#{2,3} "):
    m = re.search(r"^" + re.escape(head) + r".*?$", PROTO, re.M)
    if not m:
        return ""
    n = re.search(stop, PROTO[m.end():], re.M)
    return PROTO[m.start(): m.end() + (n.start() if n else len(PROTO) - m.end())]


def res(v):
    return NE.total(v), NE.nfail(v), NE.tier(NE.nfail(v))


def reading(b, rid):
    return next((r["result"] for r in b["joint_readings"] if r["id"] == rid), None)


def scenario(b, sid):
    return next((s for s in b["scenarios"] if s["id"] == sid), None)


def claim(gid, phrase, fact, what):
    check(gid, says(phrase) and fact, what, "phrase not found" if not says(phrase) else "fact does not hold")


print("verify_protocol_s36.py -- the scoring protocol's own statements, checked")
print(f"protocol: SCORING_PROTOCOL.md; corpus: neec_corpus.json ({len(ENTRIES)} entries); "
      f"{len(BLOCKS)} summary blocks from {len(DOCS)} documents")

# ---------------------------------------------------------------- A
print("\nA  header and structure")
m = re.search(r"\*\*Version (\S+) ", PROTO[:2000])
check("A1", m and m.group(1) == "2.0-draft.5", "the header states version 2.0-draft.5")
check("A2", says("Decisions D2 to D31 are written in (section 13)")
      and says("delegated methodological decisions to Claude"), "the header records D2 to D31 and the delegation")
heads = ["### 2.3 The operative threshold, clause by clause (decision D28, revision R4)",
         "### 4.6 Anchors (decisions D26, D28(g))",
         "## 5. Peer calibration before scores are fixed (decisions D9, D30)", "### 5.1 Declare peers",
         "### 5.2 Print the peer matrix", "### 5.3 Reconcile every difference", "### 5.4 Then fix the scores",
         "## Appendix B. The clauses of each Pass Threshold (decision D28)"]
pos = [PROTO.find("\n" + h + "\n") for h in heads]
check("A3", all(p > 0 for p in pos) and pos == sorted(pos), "draft.5's new sections are present, in order")
lines = PROTO.split("\n")
bad = [i + 1 for i, l in enumerate(lines) if l == "---" and i and lines[i - 1].strip()]
check("A4", not bad, "every horizontal rule follows a blank line (so none renders as a heading underline)",
      f"lines {bad}")

# ---------------------------------------------------------------- B
print("\nB  3.1: the classes assigned under D17")
s31 = section("### 3.1 ")
assigned = {}
for ln in s31.split("\n"):
    mm = re.match(r"^- (Configured national economy|Mechanism|Comprehensive system): (.+)\.$", ln)
    if mm:
        for k in mm.group(2).split(", "):
            assigned[k] = CLASS_NAME[mm.group(1).lower()]
by_basis = {b["key"]: b["scope"]["class"] for b in BLOCKS.values() if b["scope"]["basis"] == "assigned"}
check("B1", assigned == by_basis and all(ENTRIES[k]["scope_class"] == c for k, c in assigned.items()),
      f"3.1's three class lines name exactly the {len(by_basis)} entries whose blocks say 'assigned', "
      "with the corpus's classes")

# ---------------------------------------------------------------- C
print("\nC  5.1: the archetype table (D30)")
s51 = section("### 5.1 ")
rows = [r for r in s51.split("\n") if r.startswith("| ") and not r.startswith("| Archetype") and "---" not in r]
table = {}
for r in rows:
    cells = [c.strip() for c in r.strip("|").split(" | ")]
    table[cells[0]] = dict(cls=CLASS_NAME.get(cells[1]), members=cells[3].split(", "), basis=cells[4])
members = [k for a in table.values() for k in a["members"]]
check("C1", len(table) == 5 and sorted(members) == sorted(ENTRIES) and len(members) == len(set(members)),
      f"five archetypes; every one of the {len(ENTRIES)} corpus entries is a member of exactly one")
check("C2", all(a["cls"] and all(ENTRIES[k]["scope_class"] == a["cls"] for k in a["members"] if k in ENTRIES)
                for a in table.values()), "each archetype's members all have the scope class its row states")
arch_of = {k: n for n, a in table.items() for k in a["members"]}
os_peers = sorted(k for k in table.get(arch_of.get("Ostrom-Style Commons Governance", ""), {"members": []})["members"]
                  if k != "Ostrom-Style Commons Governance")
declared = sorted(REPL.get("peers") or [])
omitted = sorted(set(os_peers) - set(declared))
claim("C3", "the first pilot would have declared six peers, the other narrow single mechanisms; its replicator "
      "declared four of them, omitting MMT + Job Guarantee and Universal Basic Income",
      len(os_peers) == 6 and set(declared) <= set(os_peers) and len(declared) == 4
      and omitted == ["MMT + Job Guarantee", "Universal Basic Income"],
      "D30's note: by the rule the pilot had six peers; the replicator declared four, omitting MMT + JG and UBI")
cco = "CCO-PTF-CIP-SZH"
check("C4", sum(cco in ln for ln in s31.split("\n")) == 1 and sum(cco in ln for ln in s51.split("\n")) == 1,
      "R8 readiness: the second pilot's target is named on one line of 3.1 and one line of 5.1")

# ---------------------------------------------------------------- D
print("\nD  statements about entries")
SG, OS, IF, QA, GEO, SWF = (BLOCKS[c] for c in ("SG", "OS", "IF", "QA", "GEO", "SWF"))
en = {c: NE.enumerate_register(BLOCKS[c]) for c in ("SG", "OS", "IF", "QA")}
claim("D1", "11 flags, 2,048 combinations, the reach and the enumeration share unchanged, the point span 6.0 -> 5.5",
      len(SG["flags"]) == 11 and en["SG"]["combinations"] == 2048 and NE.d13(SG)["span_points"] == 5.5,
      "3.4(a): Singapore's register as it stands")
claim("D2", "moved four flags — C1.3, C3.1, C3.5 and C4.2 — into scope scenarios and kept two borderline flags, "
      "C4.3 and C5.2", all(scenario(OS, s) for s in ("land-trusts-out", "resource-frame"))
      and {"C4.3", "C5.2"} <= {f["criterion"] for f in OS["flags"]}
      and not {"C1.3", "C3.1", "C3.5", "C4.2"} & {f["criterion"] for f in OS["flags"]},
      "3.4(b): Ostrom's four scope questions are scenarios, its two borderline flags stay")
kc, lt, rf = (scenario(OS, s)["result"] for s in ("knowledge-commons", "land-trusts-out", "resource-frame"))
checks35 = [
    ("The entry now stands at 14.5/26 with 3 failures, Partially Adequate",
     res(OS["vector"]) == (14.5, 3, "Partially Adequate")),
    ("its joint readings are the two extremes of its fifteen flags",
     len(OS["flags"]) == 15 and {r["basis"] for r in OS["joint_readings"]} == {"scored", "extremes"}),
    ("every call upward, 18.0/26 with 0 failures", reading(OS, "up") == dict(total=18.0, failures=0,
                                                                                tier="Potentially Adequate")),
    ("every call downward, 10.5/26 with 9 failures", reading(OS, "down") == dict(total=10.5, failures=9,
                                                                                    tier="Structurally Inadequate")),
    ("which still reach all three tiers", len(NE.d13(OS)["reach"]) == 3),
    ("the knowledge and digital commons counted in (15.5/26, 2 failures, Potentially Adequate)",
     kc == dict(total=15.5, failures=2, tier="Potentially Adequate")),
    ("community land trusts counted out (14.0/26, 4 failures, Partially Adequate)",
     lt == dict(total=14.0, failures=4, tier="Partially Adequate")),
    ("the thresholds read against the governed resource and its members (16.0/26, 3 failures, Partially Adequate)",
     rf == dict(total=16.0, failures=3, tier="Partially Adequate")),
]
for i, (ph, fact) in enumerate(checks35, 1):
    claim(f"D3.{i}", ph, fact, f"3.5: {ph[:70]}")
gv = dict(GEO["vector"], **{"C4.3": 0.0})
claim("D4", "Georgism's tier is not robust (C4.3 resolved to 0.0 gives 3 failures, Partially Adequate)",
      res(gv)[1:] == (3, "Partially Adequate") and not NE.d13(GEO)["robust"], "6.1: Georgism under D16")
claim("D5", "Sovereign Wealth Fund Statism's all-downward reading reaches Structurally Inadequate",
      reading(SWF, "down")["tier"] == "Structurally Inadequate", "6.1: Sovereign Wealth Fund Statism under D16")
order = sorted(BLOCKS.values(), key=lambda b: NE.fragility_key(b, NE.KEYS.index(b["key"])))
d_os, d_if = NE.d13(OS), NE.d13(IF)
claim("D6", "Ostrom-style commons governance is the least tier-robust entry — three tiers, 7.5 points and 9 failures — "
      "and Islamic finance the second — three tiers, 5.0 points and 9 failures, the equal failure spans ordered by "
      "points", [b["code"] for b in order[:2]] == ["OS", "IF"]
      and (len(d_os["reach"]), d_os["span_points"], d_os["span_failures"]) == (3, 7.5, 9)
      and (len(d_if["reach"]), d_if["span_points"], d_if["span_failures"]) == (3, 5.0, 9),
      "6.4: the D13 order of the two least tier-robust entries")
claim("D7", "17.1% of Islamic finance's 65,536 combinations keep its tier against 65.6% of Ostrom's 32,768",
      (en["IF"]["combinations"], f"{100 * en['IF']['keep_share']:.1f}") == (65536, "17.1")
      and (en["OS"]["combinations"], f"{100 * en['OS']['keep_share']:.1f}") == (32768, "65.6"),
      "6.4: the enumeration shares reverse the order")
claim("D8", "Qatar carries twelve flags and is tier-robust; all 4,096 combinations of its calls are Structurally "
      "Inadequate", len(QA["flags"]) == 12 and NE.d13(QA)["robust"] and en["QA"]["combinations"] == 4096
      and en["QA"]["by_tier"] == {"Structurally Inadequate": 4096}, "6.4: Qatar")
qs, ifs = scenario(QA, "citizens-only")["result"], scenario(IF, "social-finance-layer")["result"]
claim("D9", "Qatar with citizens only (13.0/26, 6 failures, Structurally Inadequate)",
      qs == dict(total=13.0, failures=6, tier="Structurally Inadequate"), "6.5: Qatar's scenario")
claim("D10", "Islamic finance with its social-finance layer counted in (14.5/26, 4 failures, Partially Adequate)",
      ifs == dict(total=14.5, failures=4, tier="Partially Adequate"), "6.5: Islamic finance's scenario")
c32 = [k for k, e in ENTRIES.items() if e["vector"]["C3.2"] == 0.0]
claim("D11", "Ostrom-style commons governance's C3.2, then the corpus's only 0.0 there, became 0.5 (14.5/26, 3 "
      "failures, Partially Adequate; tier unchanged)", not c32 and OS["vector"]["C3.2"] == 0.5
      and res(OS["vector"]) == (14.5, 3, "Partially Adequate"), "13, D26: no 0.0 on C3.2 now")
v = OS["vector"]
mech05 = sum(1 for e in ENTRIES.values() if e["scope_class"] == "mechanism" for x in e["vector"].values() if x == 0.5)
claim("D12", "The outcomes are 0.5 as scored, or 0.0 — 14.0/26, 4 failures, Partially Adequate.",
      v["C4.3"] == 0.5 and res(dict(v, **{"C4.3": 0.0})) == (14.0, 4, "Partially Adequate"), "13, D29: Ostrom's C4.3")
claim("D13", "the other 0.5s of the mechanism-class entries against it (131 scores, Ostrom's C4.3 among them)",
      mech05 == 131, "13, D29: the mechanism-class 0.5s the rescoring pass reads")
both = res(dict(v, **{"C4.3": 0.0, "C1.3": 0.0}))
claim("D14", "C1.3 becomes 0.0 — 14.0/26, 4 failures — and a scenario counts them in; with C4.3 at 0.0 as well, "
      "13.5/26, 5 failures", v["C1.3"] == 0.5 and res(dict(v, **{"C1.3": 0.0}))[:2] == (14.0, 4)
      and both == (13.5, 5, "Partially Adequate"), "13, D31: Ostrom's C1.3, and with C4.3")
claim("D15", "governance stays Partially Adequate under either outcome or both",
      both[2] == res(dict(v, **{"C1.3": 0.0}))[2] == res(dict(v, **{"C4.3": 0.0}))[2] == "Partially Adequate",
      "13, D31: Ostrom's tier under D29 and D31")
check("D16", scenario(IF, "social-finance-layer")["kind"] == "scope"
      and scenario(OS, "knowledge-commons")["kind"] == "scope" and scenario(OS, "land-trusts-out")["kind"] == "scope",
      "3.2's extension precedents are carried as scope scenarios in their documents")

# ---------------------------------------------------------------- E
print("\nE  4.6 against criteria.json")


def closing(t):
    return t if t.endswith(".") else t + "."


cr = CRIT["criteria"]
check("E1", all(c["anchors"]["threshold"] == closing(c["definition"]["pass_threshold"]) for c in cr),
      "every anchor's threshold line is its definition's Pass Threshold, verbatim (D28(g))")
corr = CRIT["source"].get("corrections", [])
thr = [r for r in corr if r["field"] == "anchors.threshold"]
sub = sorted(r["criterion"] for r in thr if r["kind"] == "substantive")
claim("E2", "`build_criteria.py` replaced 25 of the 26 Appendix H.7 threshold lines; six had departed from their "
      "definitions in substance — C2.1, C2.2, C2.5, C3.1, C5.1 and C5.3 —",
      len(thr) == 25 and sub == ["C2.1", "C2.2", "C2.5", "C3.1", "C5.1", "C5.3"], "4.6: the corrections as counted")
c32a = next(c for c in cr if c["id"] == "C3.2")["anchors"]["bands"]
check("E3", c32a["0.0"]["examples"] == [] and "active inflationary mechanism" in c32a["0.0"]["text"]
      and "the 13" not in c32a["0.0"]["text"] and "(decision D26)" in c32a["0.5"]["text"]
      and says("the 0.5 band now says so"), "4.6: C3.2's bands carry D26, without the stale count")
wrong = sorted((c["id"], b) for c in cr for b, band in c["anchors"]["bands"].items() if band.get("corrections"))
check("E4", wrong == [("C4.3", "0.0"), ("C4.5", "1.0")] and says("C4.3's 0.0 example")
      and says("C4.5's 1.0 example"), "4.6: the two wrong examples are exactly those the file marks")

# ---------------------------------------------------------------- F
print("\nF  Appendix B")
appb = section("## Appendix B.", stop=r"^## ")
got = {}
for r in appb.split("\n"):
    mm = re.match(r"^\| (C\d\.\d[ab]?) \| (.+) \|$", r)
    if mm:
        got[mm.group(1)] = [x.strip() for x in re.split(r"\(\d+\) ", mm.group(2)) if x.strip()]
order_ids = [c["id"] for c in cr]
want = {c: [t for t, _ in R4.CLAUSES[c]] for c in order_ids if c in R4.CLAUSES}
check("F1", got == want and list(got) == [c for c in order_ids if c in want],
      f"Appendix B lists the {len(want)} multi-clause thresholds' clauses exactly as r4_audit_s35.py splits them")
ok = True
defs = {c["id"]: c["definition"]["pass_threshold"] for c in cr}
for c, cl in want.items():
    p, rest = 0, ""
    for t in cl:
        i = defs[c].find(t, p)
        if i < 0 or defs[c].count(t) != 1:
            ok = False
            break
        rest, p = rest + defs[c][p:i], i + len(t)
    rest += defs[c][p:]
    ok = ok and (rest == R4.LEFTOVER[c] if c in R4.LEFTOVER else re.sub(r"(,|\band\b|\s)", "", rest) == "")
check("F2", ok, "every clause is a verbatim substring of criteria.json's definition, once, in order, leaving "
      "connectives only")
single = [c for c in order_ids if c not in want]
check("F3", single == list(R4.SINGLE) and says("Five criteria have one clause: " + ", ".join(single) + ".")
      and says("Twenty-one criteria have a Pass Threshold of more than one clause"),
      "the one-clause criteria are named as the audit names them")

# ---------------------------------------------------------------- G
print("\nG  section 13: the register")
s13 = section("## 13. ", stop=r"^## ")
ids = re.findall(r"^\| (D\d+(?:\([ab]\))?) ", s13, re.M)
expect = ["D2", "D3(a)", "D3(b)", "D6", "D8", "D9"] + [f"D{n}" for n in range(12, 32)]
check("G1", ids == expect, f"the register lists {len(expect)} decisions, D2 to D31, each once and in order",
      f"got {ids}")
notes = [f"D{n} — " for n in range(19, 32) if n != 25]
check("G2", all(("**" + n) in s13 for n in notes), "a note for D19 to D31 (D25 closed in its row)")
check("G3", says("The two decisions draft.4 left awaiting the owner are settled: D23's publication by D27(a), and "
                 "D24 under the delegation."), "the delegation settles draft.4's two open confirmations")

# ---------------------------------------------------------------- H
print("\nH  revisions R1 to R8")
where = {"R1": "### 3.4 ", "R2": "### 4.1 ", "R3": "### 4.6 ", "R4": "### 2.3 ", "R5": "### 5.1 ",
         "R6": "### 3.2 ", "R7": "## 11. ", "R8": "## 11. "}
for r, h in where.items():
    body = section(h, stop=r"^## " if h.startswith("## ") else r"^#{2,3} ")
    check(f"H{r[1]}", re.search(r"revision\s+" + r + r"\b", body) is not None
          or (r == "R8" and "(R8)" in body), f"{r} is written into {h.strip('# ').strip()}")

# ---------------------------------------------------------------- I
print("\nI  superseded statements of draft.4")
gone = ["review of the whole text is pending", "One question is deferred by decision",
        "10.0 points and 11 failures", "46.7% of Ostrom's 1,048,576", "awaits the owner's confirmation",
        "no system in the 13 scores 0.0 here", "the register is reconsidered then", "is the owner's decision"]
for i, g in enumerate(gone, 1):
    check(f"I{i}", not says(g), f"absent: \"{g}\"")

n_fail = sum(1 for _, ok_ in RESULTS if not ok_)
print(f"\n{len(RESULTS)} checks: {len(RESULTS) - n_fail} passed, {n_fail} failed.")
sys.exit(1 if n_fail else 0)
