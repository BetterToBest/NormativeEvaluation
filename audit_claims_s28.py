#!/usr/bin/env python3
"""
audit_claims_s28.py -- NEEC Session 28: the claim register of the eight documents not yet audited
=================================================================================================
Decisions D12 and D14 require every scoring document to state its comparative
claims on the current canonical corpus, restated in place, never by appended
notes. Session 26 did this for the three documents written in Sessions 21-23
(Qatar, Islamic finance, Ostrom). This script audits the other eight, which
were written against corpora of 13 to 20 systems:

    GEO  Georgism / Land Value Tax             Session 6
    MC   Mutual Credit / LETS                  Session 7
    DE   Doughnut Economics                    Session 14
    UBS  Universal Basic Services              Session 15
    SWF  Sovereign Wealth Fund Statism         Session 17
    CN   State Capitalism / China              Session 18
    SG   State Capitalism / Singapore          Session 19
    1C   the Step 1c retrofit (13 systems)     Session 8

It edits nothing. It is the input of the one generator of the D14 pass.

METHOD. Every data claim in the eight documents is registered with (a) a
verbatim phrase, which must occur exactly once in its document after the
normalisation verify_comparative_claims.py uses (whitespace collapsed, bold
markers removed) and, for a reference to another entry's score on a
criterion, inside that criterion's own section (protocol 8.3); (b) a
machine-checkable spec, evaluated on the canonical 23-system corpus and the
Session 28 summary blocks (flags, joint readings, D13); and (c) the verdict
this audit reached on review. The run recomputes every verdict that is a
fact about the corpus (data claims, dated corpus sizes, decision items) and
fails on any disagreement, so a claim that changes status is caught (assert,
don't only print); status, history, record and error verdicts are review
judgments and are printed as such. (d) For an item to restate, the facts its
replacement must state (nowspec), which must hold on the corpus.

The candidates were found by a sentence scan (another entry named together
with a score, tier, rank or dominance signal, or a corpus-position phrase;
about 440 sentences) and read one by one. Registered: data claims. Not
registered, as protocol 8.1 directs: characterisations of another entry's
design, scope, evidence or archetype, qualitative resemblances explicitly
labelled as such, and evidential superlatives ("few systems in this corpus
have a comparably concrete record"), which the handoffs carry as optional
polish. Whole-number percentages written before protocol 2.4 (one decimal) are
not treated as stale on that account alone.

VERDICTS
  holds    true on the canonical corpus; the claims verifier will assert it
  stale    true when written, not now (status, dated corpus size, or a
           comparative fact the later entries changed): restate in place
  error    wrong when written: correct in place
  decision a statement a decision now requires (D16 tier-robustness
           disclosures) that the document does not yet make: add it
  record   a transcript of a script run, pasted into the document: replace
           with a pointer to the captured output the harness reproduces
  history  true as a statement about the project's history, worded as such:
           retained, listed here, not asserted as a corpus fact

Usage:   python3 audit_claims_s28.py
Inputs beside the script or in the working directory: the eight documents
(pinned by MD5), the canonical script and CSV, summary_blocks_s28.json and
neec_entry.py. Exit status 0 only if every phrase is found where required and
every verdict reproduces. Prints file names only; deterministic.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = {
    "GEO": ("NEEC_Georgism_LVT_scoring_scratch.md", "56236eb4"),
    "MC": ("NEEC_MutualCredit_LETS_scoring_scratch.md", "0cec0f4a"),
    "DE": ("NEEC_DoughnutEconomics_scoring_scratch.md", "a0990bb1"),
    "UBS": ("NEEC_UniversalBasicServices_scoring_scratch.md", "2abab03b"),
    "SWF": ("NEEC_SovereignWealthFundStatism_scoring_scratch.md", "48e78c20"),
    "CN": ("NEEC_StateCapitalism_China_scoring_scratch.md", "4c907e60"),
    "SG": ("NEEC_StateCapitalism_Singapore_scoring_scratch.md", "64f7201e"),
    "1C": ("NEEC_Step1c_Retrofit_C1_2ab_C1_5.md", "aa627d9e"),
}
BLOCKS = ("summary_blocks_s28.json", "7973e170")


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name}")


def pinned(name, md5):
    raw = open(locate(name), "rb").read()
    got = hashlib.md5(raw).hexdigest()[:8]
    if got != md5:
        sys.exit(f"ERROR: {name} md5 {got}, expected {md5}")
    return raw.decode("utf-8")


spec = importlib.util.spec_from_file_location("neec_entry", locate("neec_entry.py"))
NE = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(NE)
S, CRITS = NE.SCORES, NE.CRITS
BL = {b["code"]: b for b in json.loads(pinned(*BLOCKS))}
KEY = {c: b["key"] for c, b in BL.items()}
CODE = {k: c for c, k in KEY.items()}
ORDER = list(S)


# ------------------------------------------------------------------ documents
def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()


CRIT_HEAD = re.compile(r"^#{2,4} (C[1-5]\.[1-6][ab]?)\b")


def sections(raw):
    """As verify_comparative_claims.py: a criterion heading to the next criterion or level 1-3 heading."""
    out, cur = {}, None
    for line in raw.split("\n"):
        m = CRIT_HEAD.match(line)
        if m:
            cur = m.group(1)
            out[cur] = [line]
            continue
        if cur and re.match(r"^#{1,3} ", line):
            cur = None
        if cur:
            out[cur].append(line)
    return {c: norm("\n".join(v)) for c, v in out.items()}


RAW = {d: pinned(f, m) for d, (f, m) in DOC.items()}
TEXT = {d: norm(t) for d, t in RAW.items()}
SECT = {d: sections(t) for d, t in RAW.items() if d != "1C"}


# ------------------------------------------------------------------ corpus facts (codes in, codes out)
def v(c):
    return S[KEY[c]]


def tot(c):
    return sum(v(c)[k] for k in CRITS)


def nf(c):
    return sum(1 for k in CRITS if v(c)[k] == 0.0)


def tier(c):
    return NE.tier(nf(c))


def dsum(c, d):
    return sum(v(c)[k] for k in CRITS if k.startswith(f"C{d}."))


def dom(a, b):
    return all(v(a)[k] >= v(b)[k] for k in CRITS) and any(v(a)[k] > v(b)[k] for k in CRITS)


def codes(pred):
    return [CODE[k] for k in ORDER if pred(CODE[k])]


F = {
    "score": lambda c, k: v(c)[k],
    "total": tot,
    "failures": nf,
    "tier": tier,
    "domain": dsum,
    "dominates": dom,
    "dominators": lambda c: codes(lambda x: dom(x, c)),
    "dominated": lambda c: codes(lambda x: dom(c, x)),
    "ties": lambda c: codes(lambda x: x != c and tot(x) == tot(c)),
    "rank": lambda c: (1 + sum(1 for x in CODE.values() if tot(x) > tot(c)),
                       sum(1 for x in CODE.values() if tot(x) >= tot(c))),
    "tier_others": lambda c: codes(lambda x: x != c and tier(x) == tier(c)),
    "in_tier": lambda t: codes(lambda x: tier(x) == t),
    "above_in_tier": lambda c: codes(lambda x: tier(x) == tier(c) and tot(x) > tot(c)),
    "lowest_in_tier": lambda c: all(tot(x) > tot(c) for x in CODE.values() if x != c and tier(x) == tier(c)),
    "domain_below": lambda c, d: codes(lambda x: dsum(x, d) < dsum(c, d)),
    "domain_level": lambda c, d: codes(lambda x: x != c and dsum(x, d) == dsum(c, d)),
    "differ": lambda a, b: [k for k in CRITS if v(a)[k] != v(b)[k]],
    "flags": lambda c: (len(BL[c]["flags"]), len([f for f in BL[c]["flags"] if not f.get("tracks")])),
    "reach": lambda c: [NE.TIER_ABBR[t] for t in NE.d13(BL[c])["reach"]],
    "at_score": lambda k, x: codes(lambda c: v(c)[k] == x),
}


def _pct(c):
    return round(100 * tot(c) / 26, 1)


def _native():
    return codes(lambda c: BL[c]["record"]["structure"] == "native-v2")


def _reading(c, rid):
    r = [x for x in BL[c]["joint_readings"] if x["id"] == rid][0]["result"]
    return (r["total"], r["failures"])


def _d13_order():
    bl = [BL[CODE[k]] for k in ORDER]
    return [bl[i]["code"] for i in sorted(range(len(bl)), key=lambda i: NE.fragility_key(bl[i], i))]


F.update({
    "pct": _pct,
    "same": lambda a, b, k, _x=None: v(a)[k] == v(b)[k],
    "above": lambda a, b: [k for k in CRITS if v(a)[k] > v(b)[k]],
    "above_count": lambda a, b: sum(1 for k in CRITS if v(a)[k] > v(b)[k]),
    "domain_deltas": lambda a, b: [dsum(a, d) - dsum(b, d) for d in range(1, 6)],
    "nondominated": lambda a, b: not dom(a, b) and not dom(b, a),
    "common_failures": lambda a, b: [k for k in CRITS if v(a)[k] == 0.0 and v(b)[k] == 0.0],
    "fail_subset": lambda a, b: all(v(b)[k] == 0.0 for k in CRITS if v(a)[k] == 0.0),
    "fail_minus": lambda a, b: [k for k in CRITS if v(a)[k] == 0.0 and v(b)[k] != 0.0],
    "flags_to_zero": lambda c: [f["criterion"] for f in BL[c]["flags"] if 0.0 in f["alternatives"]],
    "flagged": lambda c: [f["criterion"] for f in BL[c]["flags"]],
    "flag_alt": lambda c, k: next((f["alternatives"] for f in BL[c]["flags"] if f["criterion"] == k), None),
    "reading": _reading,
    "d13_rank": lambda c: 1 + _d13_order().index(c),
    "display": lambda c: BL[c]["display_name"],
    "scope": lambda c: BL[c]["scope"]["class"],
    "native_at": lambda k, x: [c for c in _native() if v(c)[k] == x],
    "native_rank": lambda c: (1 + sum(1 for x in _native() if tot(x) > tot(c)), sum(1 for x in _native() if tot(x) >= tot(c))),
    "class_domain_above": lambda c, cls, d: codes(lambda x: BL[x]["scope"]["class"] == cls and dsum(x, d) > dsum(c, d)),
    "class_domain_level": lambda c, cls, d: codes(lambda x: x != c and BL[x]["scope"]["class"] == cls and dsum(x, d) == dsum(c, d)),
    "at_total": lambda x: codes(lambda c: tot(c) == x),
    "below": lambda c: codes(lambda x: tot(x) < tot(c)),
    "most_failures": lambda: codes(lambda x: nf(x) == max(nf(y) for y in CODE.values())),
    "undominated_by": lambda c: codes(lambda x: x != c and not dom(c, x)),
    "single": lambda c, k, x: (tot(c) - v(c)[k] + x, nf(c) - (v(c)[k] == 0.0) + (x == 0.0)),
    "tier_of_failures": lambda n: NE.tier(n),
    "tier_pct_range": lambda t: (min(_pct(x) for x in CODE.values() if tier(x) == t),
                                 max(_pct(x) for x in CODE.values() if tier(x) == t)),
})


def show(x):
    if isinstance(x, float):
        return NE.fmt(x)
    if isinstance(x, (list, tuple)):
        return "[" + ", ".join(show(y) for y in x) + "]"
    return str(x)


def evaluate(spec):
    """spec: list of (function, args..., expected). Returns (all hold, text of each failing part)."""
    bad = []
    for part in spec:
        fn, args, want = part[0], part[1:-1], part[-1]
        got = F[fn](*args)
        if isinstance(want, list) and isinstance(got, list) and fn not in ("rank", "differ", "domain_deltas"):
            ok = sorted(got) == sorted(want)
        else:
            ok = got == (tuple(want) if isinstance(want, list) and isinstance(got, tuple) else want)
        if not ok:
            bad.append(f"{fn}({', '.join(show(a) for a in args)}) = {show(got)}, claimed {show(want)}")
    return not bad, bad


# ------------------------------------------------------------------ the register
REG = []


def R(doc, rid, kind, phrase, spec=None, verdict="holds", sec=None, now="", nowspec=None):
    REG.append(dict(doc=doc, rid=rid, kind=kind, phrase=phrase, spec=spec or [], verdict=verdict, sec=sec, now=now,
                    nowspec=nowspec or []))


# Kinds: status, size, crit (another entry's score on a criterion), tier, position, pair, dominance,
# flags (another entry's flags or tier robustness), d16 (a disclosure D16 requires), record, history.

def sc(k, x, *cs):
    return [("score", c, k, x) for c in cs]


PART8 = ["MMT", "INT", "MC", "UBS", "SWF", "SG", "IF", "OS"]
NC = "has not yet been independently cross-checked by a second scorer"

# ---- GEO: Georgism / Land Value Tax (Session 6; corpus then 13 systems; inserted Session 8)
R("GEO", "GEO-01", "status", "SCRATCH DRAFT — Step 1b, Session 6.", verdict="stale",
  now="scored natively on v2 (Session 6); in the canonical corpus since Session 8")
R("GEO", "GEO-02", "status", "Not yet added to `neec_scores.csv` (see the schema note in Summary Scores)", verdict="stale",
  now="in neec_scores.csv since Session 8; the second-scorer cross-check is still open (kept)")
R("GEO", "GEO-03", "status", "Adding this row correctly requires the same CSV schema update Step 1c already has queued",
  verdict="stale", now="the schema update and the row were made in Session 8")
R("GEO", "GEO-04", "status", NC, verdict="holds")
R("GEO", "GEO-05", "crit", "the same kind of mechanism NEEC's existing UBI evaluation credits with 1.0 on this criterion",
  sc("C1.1", 1.0, "UBI"), sec="C1.1")
R("GEO", "GEO-06", "crit", "UBI scores 0.0 here even though its C1.1 (poverty elimination) score is a full 1.0",
  sc("C1.2a", 0.0, "UBI") + sc("C1.1", 1.0, "UBI"), sec="C1.2a")
R("GEO", "GEO-07", "crit", "matching UBI's precedent on this exact distinction", sc("C1.2a", 0.0, "UBI", "GEO"), sec="C1.2a")
R("GEO", "GEO-08", "crit", "Status Quo Market Capitalism's own C2.4 score", sc("C2.4", 0.5, "SQ", "GEO"), sec="C2.4")
R("GEO", "GEO-09", "crit", "(Market Socialism and Stakeholder Capitalism both score 0.5 here for materially the same reason)",
  sc("C3.2", 0.5, "MS", "SC"), sec="C3.2")
R("GEO", "GEO-10", "crit", "a real, credited universalist benefit (matching UBI's own precedent)", sc("C4.3", 1.0, "UBI"), sec="C4.3")
R("GEO", "GEO-11", "crit", '''Integral's "components proven, integration merely untested" (0.5)''', sc("C5.1", 0.5, "INT"), sec="C5.1")
R("GEO", "GEO-12", "tier", "with the lowest percentage score of any system this paper has evaluated in that tier — 52%",
  [("lowest_in_tier", "GEO", True)])
R("GEO", "GEO-13", "tier", "well below the next-lowest current members (Market Socialism and MMT+Job Guarantee, each 64% under the legacy 25-criterion count)",
  [("above_in_tier", "GEO", ["CCO", "PE", "NSD", "DG", "MS", "MMT"])], verdict="stale",
  now="the next-lowest member is Market Socialism alone; MMT + Job Guarantee is Partially Adequate since Step 1c",
  nowspec=[("above_in_tier", "GEO", ["NSD", "MS", "DG", "PE", "CCO"]), ("total", "MS", 16.5), ("pct", "MS", 63.5),
           ("tier", "MMT", "Partially Adequate")])
R("GEO", "GEO-14", "history", "alongside Integral's own contribution of the first genuine Partially Adequate case", verdict="history")
R("GEO", "GEO-15", "status", "No formal 26-criterion dominance analysis against the existing corpus was attempted in this pass — that would require re-deriving every other system's C1.2a/C1.2b/C1.5 split first (Step 1c, still pending), which this evaluation does not do.",
  verdict="stale", now="Step 1c is done and dominance is computed on the corpus",
  nowspec=[("dominators", "GEO", ["CCO"]), ("dominated", "GEO", [])])
R("GEO", "GEO-16", "tier", "Georgism clearly underperforms every current Potentially-Adequate-tier system (Nordic, Degrowth, Market Socialism, MMT+JG, Participatory Economics, CCO-PTF) on raw percentage",
  [("tier_others", "GEO", ["NSD", "DG", "MS", "MMT", "PE", "CCO"])], verdict="stale",
  now="drop MMT+JG; every other Potentially Adequate entry is higher",
  nowspec=[("tier_others", "GEO", ["NSD", "MS", "DG", "PE", "CCO"]), ("lowest_in_tier", "GEO", True)])
R("GEO", "GEO-17", "d16", "presented as a close call rather than a confidently-resolved one.", [("reach", "GEO", ["PA", "Part"])],
  verdict="decision", sec="C4.3", now="D16(i): C4.3 encoded [0.0, 1.0]; the tier is not robust to C4.3: say so",
  nowspec=[("reading", "GEO", "down", (13.0, 3)), ("flag_alt", "GEO", "C4.3", [0.0, 1.0])])

# ---- MC: Mutual Credit / LETS (Session 7; inserted Session 8)
R("MC", "MC-01", "status", "SCRATCH DRAFT — Step 1b, Session 7.", verdict="stale",
  now="scored natively on v2 (Session 7); in the canonical corpus since Session 8")
R("MC", "MC-02", "status", "Not yet added to `neec_scores.csv` (schema already updated this session", verdict="stale",
  now="in neec_scores.csv since Session 8; second-scorer cross-check still open")
R("MC", "MC-03", "status", "The CSV's schema was updated this session (`criteria_count`, `domain1_max` columns added", verdict="stale",
  now="the row was added in Session 8")
R("MC", "MC-04", "status", NC, verdict="holds")
R("MC", "MC-05", "crit", "in contrast to several other systems in this corpus (including Georgism) that have at least an indirect, evidenced housing channel.",
  sc("C1.3", 0.5, "GEO"), sec="C1.3")
R("MC", "MC-06", "history", "this is now the third system in the corpus whose material-security failures trace to that same underlying pattern",
  verdict="history")
R("MC", "MC-07", "crit", "where Georgism at least had a partial one.", sc("C1.3", 0.5, "GEO"), sec="C1.5")
R("MC", "MC-08", "crit", "This reasoning differs from Georgism's own C2.2 partial score", sc("C2.2", 0.5, "GEO", "NSD", "MC"), sec="C2.2")
R("MC", "MC-09", "crit", "Uniform partials across all five criteria, the same shape Georgism's own Domain 4 took",
  sc("C4.1", 0.5, "GEO", "MC") + sc("C4.2", 0.5, "GEO", "MC") + sc("C4.3", 0.5, "GEO", "MC") + sc("C4.4", 0.5, "GEO", "MC")
  + sc("C4.5", 0.5, "GEO", "MC"), sec="C4.5")
R("MC", "MC-10", "crit", "this domain's overall shape is notably stronger than Georgism's own Domain 5 (3.0/5, 60%)",
  [("domain", "GEO", 5, 3.0)], sec="C5.5")
R("MC", "MC-11", "error", "the third system in this corpus's history to occupy this tier, after Integral (the first, 3 failures) and Georgism (which instead landed in Potentially Adequate with only 2).",
  verdict="error", now="Georgism never occupied the tier, so Mutual Credit / LETS was the second; the tier now has eight members",
  nowspec=[("in_tier", "Partially Adequate", PART8), ("tier", "GEO", "Potentially Adequate")])
R("MC", "MC-12", "pair", "with a higher raw percentage score (56%) than Georgism's own 52% — which landed in the better tier (Potentially Adequate, 2 failures).",
  [("total", "GEO", 13.5), ("total", "MC", 14.5), ("failures", "GEO", 2), ("tier", "GEO", "Potentially Adequate")])
R("MC", "MC-13", "status", "This project now has three systems in the Partially Adequate tier's near neighborhood worth considering together once Step 1c's retrofit is complete and genuine cross-system comparison becomes possible:",
  verdict="stale", now="Step 1c is complete; state the three on the v2 structure",
  nowspec=[("total", "INT", 19.5), ("failures", "INT", 3), ("tier", "INT", "Partially Adequate")])
R("MC", "MC-14", "pair", "Integral (18.5/25, 74%, 3 failures, under the *original* 25-criterion structure)",
  [("total", "INT", 18.5)], verdict="stale", now="Integral: 19.5/26 (75.0%), 3 failures, Partially Adequate, since Step 1c",
  nowspec=[("total", "INT", 19.5), ("pct", "INT", 75.0), ("failures", "INT", 3)])
R("MC", "MC-15", "size", "no formal 26-criterion dominance analysis against the existing 13-system corpus was attempted — that requires Step 1c's retrofit of the other systems' own C1.2a/C1.2b/C1.5 splits first.",
  verdict="stale", now="on the corpus: dominated by no entry, dominates none",
  nowspec=[("dominators", "MC", []), ("dominated", "MC", []), ("ties", "MC", ["UBI"])])

# ---- DE: Doughnut Economics (Session 14; inserted Session 16)
R("DE", "DE-01", "status", "SCRATCH DRAFT — Step 1b, Session 14.", verdict="stale",
  now="scored natively on v2 (Session 14); in the canonical corpus since Session 16")
R("DE", "DE-02", "status", "Not yet added to `neec_scores.csv` (this evaluation's scores are complete and ready to add", verdict="stale",
  now="in neec_scores.csv since Session 16; not yet a Report Part I entry (Step 5); cross-check open")
R("DE", "DE-03", "status", "This evaluation is deliberately not yet added as a row to `neec_scores.csv` in this pass", verdict="stale",
  now="inserted in Session 16")
R("DE", "DE-04", "status", "This system's scores are complete, internally verified, and ready to add whenever this write-up is reviewed and accepted.",
  verdict="stale", now="inserted in Session 16")
R("DE", "DE-05", "status", "(`verify_doughnut.py`, ad hoc, not yet folded into the project's standing verification scripts since this system is not yet in the canonical CSV)",
  verdict="stale", now="verify_doughnut.py is not in the project files; the arithmetic is checked by neec_entry.py from the summary block")
R("DE", "DE-06", "status", "When this evaluation is reviewed and folded into the canonical CSV, this row should be added to",
  verdict="stale", now="done in Session 16; verify_transcription() passes on the canonical script")
R("DE", "DE-07", "size", "no formal 26-criterion dominance analysis against the full 15-system corpus was attempted in this pass.",
  verdict="stale", now="on the corpus: dominated by CCO-PTF-CIP-SZH only; dominates none",
  nowspec=[("dominators", "DE", ["CCO"]), ("dominated", "DE", [])])
R("DE", "DE-08", "status", NC, verdict="holds")
R("DE", "DE-09", "crit", "the 0.5 band Degrowth's own C1.2a anchor uses", sc("C1.2a", 0.5, "DG"), sec="C1.2a")
R("DE", "DE-10", "crit", "Georgism's (which commits to capturing land rent specifically, scoring 0.5 here) or Mutual Credit/LETS's (whose zero-sum, capped design is this corpus's cleanest C1.2b anchor, scoring 1.0)",
  sc("C1.2b", 0.5, "GEO") + sc("C1.2b", 1.0, "MC"), sec="C1.2b")
R("DE", "DE-11", "crit", "(Nordic's unemployment benefits, Georgism's indirect land-value-capitalization argument, Integral's ITC)",
  sc("C1.4", 0.5, "NSD", "GEO", "INT"), sec="C1.4")
R("DE", "DE-12", "position", "the lowest Domain 1 score of any system in this corpus other than Libertarian Minarchism's flat 0.0/6",
  [("domain_below", "DE", 1, ["LM"]), ("domain", "LM", 1, 0.0)])
R("DE", "DE-13", "crit", "exactly the same reasoning this paper already applies to Market Socialism, Stakeholder Capitalism, and Georgism.",
  sc("C3.2", 0.5, "DE", "MS", "SC", "GEO"), sec="C3.2")
R("DE", "DE-14", "crit", "the corpus's strongest scorers here (Integral, CCO-PTF-CIP-SZH, Participatory Economics, Degrowth)",
  [("at_score", "C3.3", 1.0, ["INT", "CCO", "PE", "DG"])], sec="C3.3")
R("DE", "DE-15", "crit", "Mutual Credit/LETS had C1.2b=1.0", sc("C1.2b", 1.0, "MC"))
R("DE", "DE-16", "flags", "Unlike MMT + Job Guarantee's single tier-crossing call", [("flags", "MMT", (1, 1)), ("reach", "MMT", ["PA", "Part"])])
R("DE", "DE-17", "flags", "even resolving both C1.2a and C1.2b to 0.5 (this evaluation's two most contestable calls) would leave 6 failures",
  [("reach", "DE", ["SI"]), ("reading", "DE", "up", (12.5, 6))])
R("DE", "DE-18", "dominance", "Degrowth Economics does not formally dominate Doughnut Economics, despite scoring far higher in total (19.0/26 versus 11.5/26)",
  [("dominates", "DG", "DE", False), ("total", "DG", 19.0), ("total", "DE", 11.5)])
R("DE", "DE-19", "dominance", "Doughnut Economics escapes Degrowth's dominance via three criteria",
  [("above", "DE", "DG", ["C2.5", "C5.3", "C5.4"])] + sc("C2.5", 0.0, "DG") + sc("C2.5", 1.0, "DE") + sc("C5.3", 1.0, "DE")
  + sc("C5.3", 0.5, "DG") + sc("C5.4", 0.5, "DE") + sc("C5.4", 0.0, "DG"))
R("DE", "DE-20", "pair", "while being the only one of the three to fail the wealth-criteria cluster in its entirety",
  sc("C1.2a", 0.0, "DE") + sc("C1.2b", 0.0, "DE") + sc("C1.5", 0.0, "DE") + sc("C1.2b", 0.5, "GEO") + sc("C1.2b", 1.0, "MC"))

# ---- UBS: Universal Basic Services (Session 15; inserted Session 16)
R("UBS", "UBS-01", "status", "SCRATCH DRAFT — Step 1b, Session 15.", verdict="stale",
  now="scored natively on v2 (Session 15); in the canonical corpus since Session 16")
R("UBS", "UBS-02", "status", "Not yet added to `neec_scores.csv` and not yet independently cross-checked by a second scorer (H.9 Step 6) or inserted into the Report",
  verdict="stale", now="in neec_scores.csv since Session 16; Report Part I entry pending (Step 5); cross-check open")
R("UBS", "UBS-03", "status", "This evaluation is deliberately not yet added as a row to `neec_scores.csv`, consistent with the scratch-before-insert discipline",
  verdict="stale", now="inserted in Session 16")
R("UBS", "UBS-04", "status", "This system's scores are complete, internally verified, and ready to add whenever this write-up is reviewed and accepted.",
  verdict="stale", now="inserted in Session 16")
R("UBS", "UBS-05", "status", NC, verdict="holds")
R("UBS", "UBS-06", "status", "As with every Step 1b system so far, no exhaustive pairwise dominance analysis against the complete corpus was attempted in this pass",
  verdict="stale", now="dominance is computed on the corpus", nowspec=[("dominators", "UBS", ["CCO"]), ("dominated", "UBS", [])])
R("UBS", "UBS-07", "status", "Whether a future Ostrom-commons or sovereign-wealth-fund-statism evaluation shares any of these three now-named shapes is worth checking explicitly",
  verdict="stale", now="both were scored (Sessions 17, 23) and declare the mechanism class",
  nowspec=[("scope", "SWF", "mechanism"), ("scope", "OS", "mechanism")])
R("UBS", "UBS-08", "record", "Where does UBS rank among the (soon-to-be) 17-system corpus, by total score?", verdict="record",
  now="pasted verify_ubs.py output (15-system view): point to verify_ubs.py / verify_ubs_output.txt, reproduced by the harness")
R("UBS", "UBS-09", "status", "(`verify_ubs.py`, ad hoc, not yet folded into the project's standing verification scripts since this system is not yet in the canonical CSV",
  verdict="stale", now="verify_ubs.py is a harness check (run against the 15-system view it was written for)")
R("UBS", "UBS-10", "status", "When this evaluation is reviewed and folded into the canonical CSV, this row should be added to", verdict="stale",
  now="done in Session 16")
R("UBS", "UBS-11", "status", "Whoever next reviews this evaluation may also want to consider inserting Doughnut Economics' own already-complete vector at the same time",
  verdict="stale", now="both were inserted together in Session 16")
R("UBS", "UBS-12", "crit", "(Integral, UBI, Georgism, Mutual Credit/LETS, Doughnut Economics all fail here for closely related reasons)",
  sc("C1.2a", 0.0, "INT", "UBI", "GEO", "MC", "DE"), sec="C1.2a")
R("UBS", "UBS-13", "crit", "unlike Doughnut Economics, which was scored 0.0 here specifically for citing compatible redistributive mechanisms without adopting any of its own",
  sc("C1.2b", 0.0, "DE"), sec="C1.2b")
R("UBS", "UBS-14", "crit", "closely matching the general shape already established for Georgism, Mutual Credit/LETS, and Doughnut Economics in this domain.",
  [("domain", c, 3, 3.0) for c in ("GEO", "MC", "DE")] + sc("C3.4", 1.0, "GEO", "MC", "DE"), sec="C3.5")
R("UBS", "UBS-15", "crit", "the same flat shape already seen for Georgism's own Domain 4",
  sc("C4.1", 0.5, "GEO") + sc("C4.2", 0.5, "GEO") + sc("C4.3", 0.5, "GEO") + sc("C4.4", 0.5, "GEO") + sc("C4.5", 0.5, "GEO"), sec="C4.5")
R("UBS", "UBS-16", "crit", "compare CCO-PTF's and Mutual Credit/LETS's own 1.0 scores here", sc("C5.1", 1.0, "CCO", "MC"), sec="C5.1")
R("UBS", "UBS-17", "crit", '''(in the manner of Integral's own "components proven, integration untested" case)''', sc("C5.1", 0.5, "INT"), sec="C5.1")
R("UBS", "UBS-18", "crit", "matching the pattern already established for Georgism's own C5.5 score.", sc("C5.5", 0.5, "GEO", "UBS"), sec="C5.5")
R("UBS", "UBS-19", "position", "among this corpus's targeted-mechanism systems scored under the v2 structure so far, second only to Mutual Credit/LETS's own 4.0/5 here.",
  [("class_domain_above", "UBS", "mechanism", 5, ["MC"])], verdict="stale",
  now="mechanism class, Domain 5: Islamic finance 4.5, Mutual Credit / LETS and Ostrom 4.0, then UBS tied with SWF Statism at 3.5",
  nowspec=[("class_domain_above", "UBS", "mechanism", 5, ["MC", "IF", "OS"]), ("class_domain_level", "UBS", "mechanism", 5, ["SWF"])])
R("UBS", "UBS-20", "tier", "for why this lands UBS at an exact score tie with a system in the *better* tier.",
  [("total", "GEO", 13.5), ("total", "UBS", 13.5), ("tier", "GEO", "Potentially Adequate")])
R("UBS", "UBS-21", "pair", "to the tenth of a point, with Georgism/Land Value Tax's own published score", [("total", "GEO", 13.5), ("total", "UBS", 13.5)])
R("UBS", "UBS-22", "pair", "Georgism scores higher on C1.2b (0.5, for its land-value-capture mechanism", [("above", "GEO", "UBS", ["C1.2b"])] + sc("C1.2b", 0.5, "GEO"))
R("UBS", "UBS-23", "pair", "while UBS scores higher on C5.1 (1.0, for its broader", [("above", "UBS", "GEO", ["C5.1"])] + sc("C5.1", 1.0, "UBS"))
R("UBS", "UBS-24", "pair", "two criteria where the two systems' scores differ, out of 26", [("differ", "GEO", "UBS", ["C1.2b", "C5.1"])])
R("UBS", "UBS-25", "tier", "Georgism's 2 failures place it in Potentially Adequate, while UBS's 3rd failure (C1.2b, this evaluation's most contested call) places it one tier lower, in Partially Adequate.",
  [("failures", "GEO", 2), ("failures", "UBS", 3), ("tier", "UBS", "Partially Adequate")] + sc("C1.2b", 0.0, "UBS"))
R("UBS", "UBS-26", "error", "resolving that single call would move UBS into Potentially Adequate and produce a second system tied with Georgism at 14 points, not merely 13.5",
  verdict="error", now="at 14.0 UBS would leave Georgism's tie (13.5) and tie SWF Statism, Singapore and Ostrom",
  nowspec=[("at_total", 14.0, ["SWF", "SG", "OS"]), ("total", "GEO", 13.5), ("single", "UBS", "C1.2b", 0.5, (14.0, 2)), ("tier_of_failures", 2, "Potentially Adequate")])
R("UBS", "UBS-27", "dominance", "(1) CCO-PTF-CIP-SZH formally, strictly dominates UBS", [("dominates", "CCO", "UBS", True)])
R("UBS", "UBS-28", "dominance", "(2) Georgism and UBS are confirmed non-dominated", [("nondominated", "GEO", "UBS", True), ("differ", "GEO", "UBS", ["C1.2b", "C5.1"])])
R("UBS", "UBS-29", "dominance", "(3) Mutual Credit/LETS and UBS are also non-dominated, with Mutual Credit ahead via C1.2b",
  [("nondominated", "MC", "UBS", True), ("above", "MC", "UBS", ["C1.2b", "C5.5"]), ("above", "UBS", "MC", ["C1.3"])])
R("UBS", "UBS-30", "dominance", "beating it on six criteria: C1.4, C2.1, C2.2, C4.4, C4.5, and C5.1) while still failing to dominate it outright",
  [("above", "UBS", "DE", ["C1.4", "C2.1", "C2.2", "C4.4", "C4.5", "C5.1"]), ("above", "DE", "UBS", ["C4.1", "C4.2"]), ("dominates", "UBS", "DE", False)])
R("UBS", "UBS-31", "error", "both are Partially Adequate, both have their strongest domain in Implementation Viability, both fail the wealth cluster cleanly",
  sc("C1.2b", 0.0, "MC"), verdict="error", now="Mutual Credit / LETS fails C1.2a and C1.5 but passes C1.2b (1.0); the tier and strongest-domain parts hold",
  nowspec=sc("C1.2b", 1.0, "MC") + sc("C1.2a", 0.0, "MC") + sc("C1.5", 0.0, "MC") + [("tier", "MC", "Partially Adequate"), ("domain", "MC", 5, 4.0), ("domain", "UBS", 5, 3.5)])

# ---- SWF: Sovereign Wealth Fund Statism (Session 17; inserted Session 20)
R("SWF", "SWF-01", "status", "SCRATCH DRAFT — Step 1b, Session 17.", verdict="stale",
  now="scored natively on v2 (Session 17); in the canonical corpus since Session 20")
R("SWF", "SWF-02", "status", "Not yet added to `neec_scores.csv` (see the note in Summary Scores)", verdict="stale", now="inserted in Session 20")
R("SWF", "SWF-03", "status", "this evaluation is not added as a row to `neec_scores.csv` in this pass.", verdict="stale", now="inserted in Session 20")
R("SWF", "SWF-04", "status", "This system's scores are complete and ready to add whenever a dedicated insertion pass", verdict="stale", now="inserted in Session 20")
R("SWF", "SWF-05", "status", "a full 26-criterion re-check against every other system's own current vector is left to a dedicated insertion pass",
  verdict="stale", now="dominance is computed on the corpus", nowspec=[("dominators", "SWF", ["CCO"]), ("dominated", "SWF", [])])
R("SWF", "SWF-06", "status", NC, verdict="holds")
R("SWF", "SWF-07", "crit", "the way Georgism's dividend or a bare UBI payment are (both correctly scored 0.0 here", sc("C1.2a", 0.0, "GEO", "UBI"), sec="C1.2a")
R("SWF", "SWF-08", "flags", "unlike UBS's own flagged C1.2b call, resolving this one does not change this system's tier",
  [("flag_alt", "UBS", "C1.2b", [0.5]), ("reach", "UBS", ["PA", "Part"])], sec="C1.2a")
R("SWF", "SWF-09", "crit", "this criterion tracks it downward for the same reason Participatory Economics' does.", sc("C1.2a", 0.5, "PE") + sc("C1.5", 0.5, "PE"), sec="C1.5")
R("SWF", "SWF-10", "crit", "(matching the pattern already established for Georgism, UBS, and Doughnut Economics, whose own C1.5 scores each follow their own C1.2a finding directly)",
  [("same", c, c, "C1.5", True) for c in ()] + sc("C1.2a", 0.0, "GEO", "UBS", "DE") + sc("C1.5", 0.0, "GEO", "UBS", "DE"), sec="C1.5")
R("SWF", "SWF-11", "crit", "the same generic, modest income-supplementation channel Georgism's own C2.3 write-up describes for its dividend",
  sc("C2.3", 0.5, "GEO", "SWF"), sec="C2.3")
R("SWF", "SWF-12", "crit", "matches the established pattern for every jurisdiction-layered mechanism scored in this corpus to date (Georgism, Mutual Credit/LETS, Doughnut Economics, UBS all score 1.0 here for the same structural reason)",
  [("native_at", "C2.5", 1.0, ["GEO", "MC", "DE", "UBS", "SWF"])], verdict="stale", sec="C2.5",
  now="the list is incomplete: Islamic finance and Ostrom-style commons governance also score 1.0 here",
  nowspec=[("native_at", "C2.5", 1.0, ["GEO", "MC", "DE", "UBS", "SWF", "IF", "OS"])])
R("SWF", "SWF-13", "crit", "(Georgism, Mutual Credit/LETS, Doughnut Economics, UBS all score 1.0 here)", sc("C3.4", 1.0, "GEO", "MC", "DE", "UBS"), sec="C3.4")
R("SWF", "SWF-14", "crit", "matching the precedent this exact finding has for several other systems in this corpus (Doughnut Economics among",
  sc("C4.5", 0.0, "DE"), sec="C4.5")
R("SWF", "SWF-15", "tier", "the same tier Mutual Credit/LETS and Universal Basic Services already occupy",
  [("tier", "MC", "Partially Adequate"), ("tier", "UBS", "Partially Adequate")])
R("SWF", "SWF-16", "history", '''this is the first Step 1b "narrow single-mechanism" system whose three failures are not concentrated in the wealth-accumulation cluster''',
  verdict="history")
R("SWF", "SWF-17", "history", "This system is the first of the four newly-scored systems to clear a Partial (not a failing) score on all three",
  verdict="history")
R("SWF", "SWF-18", "pair", "This system's own failure set (C1.3, C4.2, C4.5) overlaps Mutual Credit/LETS's on only one criterion (C1.3) and does not overlap Universal Basic Services's at all.",
  [("common_failures", "SWF", "MC", ["C1.3"]), ("common_failures", "SWF", "UBS", [])])
R("SWF", "SWF-19", "flags", "unlike UBS's own flagged C1.2b call (which would move UBS into a different tier)", [("reach", "UBS", ["PA", "Part"])])
R("SWF", "SWF-20", "d16", "so this call does not move this system's adequacy tier either way", [("reach", "SWF", ["Part", "SI"])],
  verdict="decision", now="true of that call alone; D16(i) requires disclosing the joint downward reading (C1.2a, C1.5 and C4.3 at 0.0)",
  nowspec=[("reading", "SWF", "down", (12.5, 6)), ("flags", "SWF", (4, 3))])
R("SWF", "SWF-21", "position", "the second-highest total among the four systems scored natively on the v2 structure, without tying",
  [("native_rank", "SWF", (2, 2))], verdict="stale", now="among the ten native-v2 entries: tied 2nd-4th with Singapore and Ostrom, behind Mutual Credit / LETS",
  nowspec=[("native_rank", "SWF", (2, 4)), ("ties", "SWF", ["SG", "OS"])])
R("SWF", "SWF-22", "pair", "this system scores higher than Georgism and UBS's own exact 13.5/26 tie, and just half a point below Mutual Credit/LETS's 14.5/26",
  [("total", "GEO", 13.5), ("total", "UBS", 13.5), ("total", "MC", 14.5), ("total", "SWF", 14.0)])
R("SWF", "SWF-23", "tier", "It shares Mutual Credit/LETS's and UBS's adequacy tier (Partially Adequate, 3 failures)",
  [("failures", "MC", 3), ("failures", "UBS", 3), ("tier", "MC", "Partially Adequate"), ("tier", "UBS", "Partially Adequate")])

# ---- CN: State Capitalism / China (Session 18; inserted Session 20)
R("CN", "CN-01", "status", "SCRATCH DRAFT — Step 1b, Session 18 (2026-09-16).", verdict="stale",
  now="scored natively on v2 (Session 18); in the canonical corpus since Session 20")
R("CN", "CN-02", "status", "Not yet added to `neec_scores.csv` (see Summary Scores)", verdict="stale", now="inserted in Session 20")
R("CN", "CN-03", "status", "Every arithmetic, transcription, sensitivity, and comparative", verdict="stale",
  now="D15 split: verify_china.py checks the entry (against the corpus it was written for); comparative claims go to the corpus-level checker")
R("CN", "CN-04", "status", "Consistent with the scratch-before-insert discipline, this evaluation is not added to `neec_scores.csv` in this pass.",
  verdict="stale", now="inserted in Session 20")
R("CN", "CN-05", "status", "For the insertion pass to confirm or change, this evaluation proposes the display name", verdict="stale",
  now="adopted as proposed at insertion",
  nowspec=[("display", "CN", "State Capitalism / China (Party-State-Directed Market Economy)")])
R("CN", "CN-06", "status", "With Sovereign Wealth Fund Statism also awaiting insertion, two scored systems are now outstanding.",
  verdict="stale", now="both inserted in Session 20")
R("CN", "CN-07", "status", "It has not yet been independently cross-checked by a second scorer (H.9 Step 6).", verdict="holds")
R("CN", "CN-08", "status", "Comparison to the corpus (every formal claim checked by `verify_china.py`).", verdict="stale",
  now="comparative claims are checked on the current corpus by the corpus-level checker (D15)")
R("CN", "CN-10", "crit", "this corpus's own CPS entry scored 1.0 on a similar", sc("C1.1", 1.0, "CPS"), sec="C1.1")
R("CN", "CN-11", "crit", "Nordic Social Democracy's 0.5 (same Gini band) and CPS's 0.5 (formal compression alongside de facto privilege).",
  sc("C1.2b", 0.5, "NSD", "CPS"), sec="C1.2b")
R("CN", "CN-12", "crit", "This sits with Market Socialism's and UBI's 0.5 pattern and below CPS's 1.0", sc("C1.3", 0.5, "MS", "UBI") + sc("C1.3", 1.0, "CPS"), sec="C1.3")
R("CN", "CN-13", "crit", "This matches Nordic's and CPS's 0.5 and sits above Status Quo's 0.0", sc("C1.4", 0.5, "NSD", "CPS") + sc("C1.4", 0.0, "SQ"), sec="C1.4")
R("CN", "CN-14", "crit", "this sits below Status Quo's 0.5, which rests on economic compulsion alone.", sc("C2.1", 0.5, "SQ"), sec="C2.1")
R("CN", "CN-15", "crit", "the Status Quo baseline, which this corpus already scores 0.5 for time scarcity", sc("C2.3", 0.5, "SQ"), sec="C2.3")
R("CN", "CN-16", "crit", "The difference from the CPS precedent (0.0) is one of kind as well as degree.", sc("C2.3", 0.0, "CPS"), sec="C2.3")
R("CN", "CN-17", "crit", "CPS scored 0.5 on harsher facts", sc("C2.5", 0.5, "CPS"), sec="C2.5")
R("CN", "CN-18", "crit", "This matches CPS's 0.5 (rapid resource mobilization in crises) and sits above Status Quo's 0.0",
  sc("C3.1", 0.5, "CPS") + sc("C3.1", 0.0, "SQ"), sec="C3.1")
R("CN", "CN-19", "crit", "Status Quo's 1.0 for conventional monetary policy and CPS's 1.0 for administered prices.", sc("C3.2", 1.0, "SQ", "CPS"), sec="C3.2")
R("CN", "CN-20", "crit", "Not 0.0: unlike CPS, this system has not collapsed under compound stress.", sc("C3.3", 0.0, "CPS"), sec="C3.3")
R("CN", "CN-21", "crit", "scoring the reform era alone would support 1.0, as Market Socialism's documented record does.", sc("C3.4", 1.0, "MS"), sec="C3.4")
R("CN", "CN-22", "crit", "CPS scored 1.0 because its failures", sc("C3.5", 1.0, "CPS"), sec="C3.5")
R("CN", "CN-23", "crit", "the pattern described by this band's Nordic anchor.", sc("C4.1", 0.5, "NSD"), sec="C4.1")
R("CN", "CN-24", "crit", "would apply the Nordic anchor for 0.5", sc("C4.2", 0.5, "NSD"), sec="C4.2")
R("CN", "CN-25", "crit", "Status Quo's own 0.0 rests on a structural growth-imperative argument", sc("C4.2", 0.0, "SQ"), sec="C4.2")
R("CN", "CN-26", "crit", "CPS scored 1.0 on a strong ideological commitment to equality.", sc("C4.3", 1.0, "CPS"), sec="C4.3")
R("CN", "CN-27", "crit", "matching both the CPS anchor's bureaucratic pattern and the Status Quo anchor's wealth pattern.", sc("C4.4", 0.0, "CPS", "SQ"), sec="C4.4")
R("CN", "CN-28", "crit", "The CPS precedent (1.0) credited the abolition of private capital", sc("C4.5", 1.0, "CPS"), sec="C4.5")
R("CN", "CN-29", "crit", "This follows Status Quo's 1.0 reasoning", sc("C5.1", 1.0, "SQ"), sec="C5.1")
R("CN", "CN-30", "crit", "and differs from CPS's 0.5, which rested on that system's collapse.", sc("C5.1", 0.5, "CPS"), sec="C5.1")
R("CN", "CN-31", "crit", "This is materially stronger than CPS's 0.0", sc("C5.4", 0.0, "CPS"), sec="C5.4")
R("CN", "CN-32", "crit", "This matches CPS's 0.5.", sc("C5.5", 0.5, "CPS"), sec="C5.5")
R("CN", "CN-33", "crit", "but Status Quo's published C4.3 is 0.5", sc("C4.3", 0.5, "SQ"))
R("CN", "CN-40", "flags", "Sovereign Wealth Fund Statism's single flagged call was checked to be tier-neutral in both directions",
  [("flags", "SWF", (1, 1)), ("reach", "SWF", ["Part"])], verdict="stale",
  now="under D16: four flagged criteria, three calls; the joint readings reach Part/SI",
  nowspec=[("flags", "SWF", (4, 3)), ("reach", "SWF", ["Part", "SI"])])
R("CN", "CN-41", "history", "This is the first tier finding in the corpus that depends jointly on several contestable calls.", verdict="history")
R("CN", "CN-42", "position", "Domain 2 (1.0/5) is the second-lowest in the prospective corpus, above only CPS, and Domain 4 (0.5/5) ties Status Quo for the lowest.",
  [("domain_below", "CN", 2, ["CPS"]), ("domain_level", "CN", 2, []), ("domain_below", "CN", 4, []), ("domain_level", "CN", 4, ["SQ"])],
  verdict="stale", now="Domain 2 tied with Qatar, above only CPS; Domain 4 lowest in a three-way tie with Status Quo and Qatar",
  nowspec=[("domain_below", "CN", 2, ["CPS"]), ("domain_level", "CN", 2, ["QA"]), ("domain_below", "CN", 4, []), ("domain_level", "CN", 4, ["SQ", "QA"])])
R("CN", "CN-43", "pair", "At 10.0/26, this system ties Centrally Planned Socialism and Stakeholder Capitalism exactly: a three-way tie within one tier, with three different failure counts (8, 12, and 9).",
  [("ties", "CN", ["CPS", "SC"]), ("failures", "CN", 8), ("failures", "CPS", 12), ("failures", "SC", 9),
   ("tier", "CPS", "Structurally Inadequate"), ("tier", "SC", "Structurally Inadequate")])
R("CN", "CN-44", "dominance", "Only CCO-PTF-CIP-SZH dominates this system, and this system dominates no other.",
  [("dominators", "CN", ["CCO"]), ("dominated", "CN", [])], verdict="stale", now="dominated by CCO-PTF-CIP-SZH and Singapore; dominates none",
  nowspec=[("dominators", "CN", ["CCO", "SG"]), ("dominated", "CN", [])])
R("CN", "CN-45", "dominance", "It forms non-dominated pairs with CPS, Status Quo, Stakeholder Capitalism, Nordic Social Democracy, and Sovereign Wealth Fund Statism.",
  [("nondominated", "CN", c, True) for c in ("CPS", "SQ", "SC", "NSD", "SWF")])
R("CN", "CN-46", "position", "In the prospective 19-system corpus it is tied for 16th–18th, ahead of only Libertarian Minarchism (8.0/26).",
  [("rank", "CN", (16, 18))], verdict="stale", now="tied 19th-21st with CPS and Stakeholder Capitalism, ahead of Qatar and Libertarian Minarchism",
  nowspec=[("rank", "CN", (19, 21)), ("ties", "CN", ["CPS", "SC"]), ("below", "CN", ["QA", "LM"])])

# ---- SG: State Capitalism / Singapore (Session 19; inserted Session 20)
R("SG", "SG-01", "status", "SCRATCH DRAFT — Step 1b, Session 19 (2026-09-16).", verdict="stale",
  now="scored natively on v2 (Session 19); in the canonical corpus since Session 20")
R("SG", "SG-02", "status", "Not yet added to `neec_scores.csv` (see Summary Scores)", verdict="stale", now="inserted in Session 20")
R("SG", "SG-03", "status", "Every arithmetic, transcription, sensitivity, and comparative claim below is checked by", verdict="stale",
  now="D15 split, as for China")
R("SG", "SG-04", "status", "Consistent with the scratch-before-insert discipline, this evaluation is not added to `neec_scores.csv` in this pass.",
  verdict="stale", now="inserted in Session 20")
R("SG", "SG-05", "status", "For the insertion pass to confirm or change, this evaluation proposes the display name", verdict="stale",
  now="adopted as proposed at insertion", nowspec=[("display", "SG", "State Capitalism / Singapore (GLC Developmental Capitalism)")])
R("SG", "SG-06", "status", "It has not yet been independently cross-checked by a second scorer (H.9 Step 6).", verdict="holds")
R("SG", "SG-10", "crit", "the reading behind China's own flagged alternative and the CPS precedent's 1.0",
  [("flag_alt", "CN", "C1.1", [1.0])] + sc("C1.1", 1.0, "CPS"), sec="C1.1")
R("SG", "SG-11", "crit", "It differs from China's 0.5, which rested on a falling asset", sc("C1.2a", 0.5, "CN"), sec="C1.2a")
R("SG", "SG-12", "crit", "This matches Nordic Social Democracy's and China's 0.5.", sc("C1.2b", 0.5, "NSD", "CN"), sec="C1.2b")
R("SG", "SG-13", "crit", "This matches Nordic's and China's 0.5.", sc("C1.4", 0.5, "NSD", "CN"), sec="C1.4")
R("SG", "SG-14", "d18", "Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial) — flagged as contestable",
  [("flags", "SG", (11, 11))], verdict="decision", sec="C1.5", now="D18(a): drop the flag suffix; the reading is the citizens-and-PRs scenario")
R("SG", "SG-15", "d18", "a citizen-and-PR-only reading would score 1.0 on the Nordic anchor.",
  [("flags", "SG", (11, 11))] + sc("C1.5", 1.0, "NSD"), verdict="decision", sec="C1.5",
  now="D18(a): restate as the scope scenario (citizens and PRs: C1.5 1.0, C4.5 0.5; 15.0/26, 3 failures)")
R("SG", "SG-16", "d18", "| C1.5 | 0.5 | 1.0 — citizen-and-PR-only scope | 14.5 | 4 | Partially Adequate |", [("flags", "SG", (11, 11))],
  verdict="decision", now="D18(a): remove the row from the flag table")
R("SG", "SG-17", "d18", "All upward readings together give 16.5/26 with 2 failures (Potentially Adequate)", [("reading", "SG", "up", (16.0, 2))],
  verdict="decision", now="D18(a): 16.0/26 with 2 failures")
R("SG", "SG-20", "crit", "economic compulsion with a harsher political overlay than the Status Quo anchor", sc("C2.1", 0.5, "SQ"), sec="C2.1")
R("SG", "SG-21", "crit", "Status Quo Market Capitalism scored 0.0 despite US unemployment insurance", sc("C2.2", 0.0, "SQ"), sec="C2.2")
R("SG", "SG-22", "crit", "Nordic's 0.5 rests on generous, comprehensive conditional provision.", sc("C2.2", 0.5, "NSD"), sec="C2.2")
R("SG", "SG-23", "crit", "This matches the Status Quo and MMT + Job Guarantee anchors, and China's 0.0.", sc("C2.2", 0.0, "SQ", "MMT", "CN"), sec="C2.2")
R("SG", "SG-24", "crit", "engagement exists but is constrained, the Status Quo pattern", sc("C2.3", 0.5, "SQ"), sec="C2.3")
R("SG", "SG-25", "crit", "It is not China's 0.0", sc("C2.4", 0.0, "CN"), sec="C2.4")
R("SG", "SG-26", "crit", "This matches China's and Status Quo's 0.5.", sc("C2.5", 0.5, "CN", "SQ"), sec="C2.5")
R("SG", "SG-27", "crit", "This matches China's and Sovereign Wealth Fund Statism's 0.5.", sc("C3.1", 0.5, "CN", "SWF"), sec="C3.1")
R("SG", "SG-28", "crit", "This follows Status Quo's and China's 1.0.", sc("C3.2", 1.0, "SQ", "CN"), sec="C3.2")
R("SG", "SG-29", "crit", "This matches the Market Socialism band and China's 0.5.", sc("C3.3", 0.5, "MS", "CN"), sec="C3.3")
R("SG", "SG-30", "crit", "matching the Market Socialism anchor and Sovereign Wealth Fund Statism's 1.0", sc("C3.4", 1.0, "MS", "SWF"), sec="C3.4")
R("SG", "SG-31", "crit", "It differs from China's 0.5, which rested on centralization", sc("C3.4", 0.5, "CN"), sec="C3.4")
R("SG", "SG-32", "crit", "would apply the Status Quo band (0.5)", sc("C3.4", 0.5, "SQ"), sec="C3.4")
R("SG", "SG-33", "crit", "China's 0.0 rested on documented concealment", sc("C3.5", 0.0, "CN"), sec="C3.5")
R("SG", "SG-34", "crit", "would apply the Stakeholder Capitalism anchor (0.0)", sc("C3.5", 0.0, "SC"), sec="C3.5")
R("SG", "SG-35", "crit", "Sovereign Wealth Fund Statism's 1.0 does not carry over", sc("C4.1", 1.0, "SWF"), sec="C4.1")
R("SG", "SG-36", "crit", "this is H.7's Nordic anchor almost exactly", sc("C4.1", 0.5, "NSD"), sec="C4.1")
R("SG", "SG-37", "crit", "This matches China's, Sovereign Wealth Fund Statism's, and Status Quo's 0.0.", sc("C4.2", 0.0, "CN", "SWF", "SQ"), sec="C4.2")
R("SG", "SG-38", "crit", "would apply the Nordic anchor (0.5)", sc("C4.2", 0.5, "NSD"), sec="C4.2")
R("SG", "SG-39", "crit", "(That anchor's cited example, Status Quo, is published at 0.5", sc("C4.3", 0.5, "SQ"), sec="C4.3")
R("SG", "SG-40", "crit", "Nordic's 0.5 rests on the independent collective bargaining that is absent here.", sc("C4.5", 0.5, "NSD"), sec="C4.5")
R("SG", "SG-41", "crit", "This matches China's and Sovereign Wealth Fund Statism's 0.5.", sc("C5.2", 0.5, "CN", "SWF"), sec="C5.2")
R("SG", "SG-42", "crit", "matching Sovereign Wealth Fund Statism and Status Quo", sc("C5.3", 1.0, "SWF", "SQ"), sec="C5.3")
R("SG", "SG-43", "crit", "It differs from China's 0.5, which rested on the comprehensive form's need for near-total political control",
  sc("C5.3", 0.5, "CN"), sec="C5.3")
R("SG", "SG-44", "crit", "as meeting the Nordic anchor would score 1.0", sc("C5.4", 1.0, "NSD"), sec="C5.4")
R("SG", "SG-45", "crit", "This matches China's and CPS's 0.5.", sc("C5.5", 0.5, "CN", "CPS"), sec="C5.5")
R("SG", "SG-50", "flags", "Tier robustness — the weakest in the corpus so far, and in both directions.", [("d13_rank", "SG", 1)],
  verdict="stale", now="by the D13 measure the third least tier-robust entry, after Ostrom and Islamic finance (share 64.1% beside it)",
  nowspec=[("d13_rank", "SG", 3), ("d13_rank", "OS", 1), ("d13_rank", "IF", 2)])
R("SG", "SG-51", "flags", "China's joint readings spanned two tiers; this evaluation's span all three.",
  [("reach", "CN", ["Part", "SI"]), ("reach", "SG", ["PA", "Part", "SI"])])
R("SG", "SG-52", "position", "Domain 4 (1.0/5) is the weakest domain, tying Stakeholder Capitalism for third-lowest in the prospective corpus, above only China and Status Quo.",
  [("domain_below", "SG", 4, ["CN", "SQ"]), ("domain_level", "SG", 4, ["SC"])], verdict="stale",
  now="tied with Stakeholder Capitalism, above Status Quo, China and Qatar",
  nowspec=[("domain_below", "SG", 4, ["SQ", "CN", "QA"]), ("domain_level", "SG", 4, ["SC"])])
R("SG", "SG-53", "pair", "Both score 14.0/26, in the same tier, with different failure counts (3 and 4).",
  [("total", "SWF", 14.0), ("tier", "SWF", "Partially Adequate"), ("failures", "SWF", 3), ("failures", "SG", 4)])
R("SG", "SG-54", "pair", "Georgism/UBS (same total, different tiers), China/CPS/Stakeholder Capitalism (same total, radically different profiles), and now Singapore/SWF Statism (same total and tier, different failure counts).",
  [("ties", "GEO", ["UBS"]), ("ties", "SG", ["SWF"])], verdict="stale", now="both ties are three-way: 13.5 adds Islamic finance, 14.0 adds Ostrom",
  nowspec=[("ties", "GEO", ["UBS", "IF"]), ("ties", "SG", ["SWF", "OS"]), ("failures", "OS", 4), ("failures", "IF", 5)])
R("SG", "SG-55", "dominance", "Singapore strictly dominates China, its state-capitalism sibling.", [("dominates", "SG", "CN", True)])
R("SG", "SG-56", "dominance", "It scores at least as high on all 26 criteria and higher on 8, and every domain total is higher (+1.0, +1.0, +1.0, +0.5, +0.5).",
  [("above_count", "SG", "CN", 8), ("above", "CN", "SG", []), ("domain_deltas", "SG", "CN", [1.0, 1.0, 1.0, 0.5, 0.5])])
R("SG", "SG-57", "pair", "Its four failures are a subset of China's eight, and the four China failures it avoids (C2.1, C2.4, C3.5, C4.3) are exactly its four downward-flagged calls.",
  [("fail_subset", "SG", "CN", True), ("fail_minus", "CN", "SG", ["C2.1", "C2.4", "C3.5", "C4.3"]),
   ("flags_to_zero", "SG", ["C2.1", "C2.4", "C3.5", "C4.3"])])
R("SG", "SG-58", "dominance", "Only CCO-PTF-CIP-SZH dominates this system, and it dominates only China.",
  [("dominators", "SG", ["CCO"]), ("dominated", "SG", ["CN"])], verdict="stale", now="dominated by CCO-PTF-CIP-SZH only; dominates China and Qatar",
  nowspec=[("dominators", "SG", ["CCO"]), ("dominated", "SG", ["CN", "QA"])])
R("SG", "SG-59", "position", "In the prospective 20-system corpus it is tied for 10th–11th with Sovereign Wealth Fund Statism.",
  [("rank", "SG", (10, 11))], verdict="stale", now="tied 10th-12th with SWF Statism and Ostrom",
  nowspec=[("rank", "SG", (10, 12)), ("ties", "SG", ["SWF", "OS"])])

# ---- 1C: the Step 1c retrofit (Session 8; thirteen legacy systems)
R("1C", "1C-01", "status", "SCRATCH DELIVERABLE — Session 8.", verdict="stale", now="the retrofit is canonical since Session 8")
R("1C", "1C-02", "status", "followed by Integral (Paper Appendix E, not yet in the Report).", verdict="stale",
  now="Integral is Report System 13 since Report v1.6")
R("1C", "1C-03", "status", "13. Integral (Paper Appendix E — not yet in the Report)", verdict="stale",
  now="heading: Integral is Report System 13 since Report v1.6")
R("1C", "1C-04", "status", "Rewrite the Report's Part I system write-ups (Systems 1–12's own Domain 1 sections still show the legacy C1.2/C1.5 text as of this session)",
  verdict="stale", now="done: Report v1.6 carries all 15 of its systems on the 26-criterion structure")
R("1C", "1C-05", "flags", "Georgism's C4.3, Mutual Credit/LETS's C4.3 and C5.2)", [("flagged", "GEO", ["C4.3"]), ("flagged", "MC", ["C4.3", "C5.2"])])
R("1C", "1C-06", "crit", "This is flagged as more inferential than the Market Socialism/CCO-PTF 1.0 cases below", sc("C1.2a", 1.0, "MS", "CCO", "NSD"))
R("1C", "1C-07", "tier", "Tier: unchanged (Structurally Inadequate — already the corpus's most-failed system).", [("most_failures", ["LM"])])
R("1C", "1C-08", "position", "the corpus's strongest system both before and after", [("rank", "CCO", (1, 1))])
R("1C", "1C-09", "history", "moving it from 2 failures (Potentially Adequate) to 3 (Partially Adequate)", verdict="history")
R("1C", "1C-10", "crit", "pattern this retrofit applies to Status Quo Capitalism, UBI, and Stakeholder Capitalism", sc("C1.2b", 0.0, "SQ", "UBI", "SC", "MMT"))
R("1C", "1C-11", "crit", "MMT+JG's C1.2a is scored identically to Status Quo's", [("same", "MMT", "SQ", "C1.2a", True)])
R("1C", "1C-12", "crit", "initially scored this 0.0 by analogy to Centrally Planned Socialism's flat absence", sc("C1.2a", 0.0, "CPS") + sc("C1.2a", 0.5, "PE"))
R("1C", "1C-13", "flags", "Centrally Planned Socialism is at 12 failures either way", [("failures", "CPS", 12), ("reach", "CPS", ["SI"])])
R("1C", "1C-14", "pair", "Integral's Domain 1 goes from a weak 2.0/5 (40%) under the legacy conflated criterion to a much stronger 3.0/6 (50%)", [("domain", "INT", 1, 3.0)])
R("1C", "1C-15", "pair", "this time at 19.5/26 (75%)", [("total", "NSD", 19.5), ("total", "INT", 19.5)])
R("1C", "1C-16", "tier", "Their tiers still differ (Nordic: 2 failures, Potentially Adequate; Integral: 3 failures, Partially Adequate",
  [("failures", "NSD", 2), ("failures", "INT", 3)])
R("1C", "1C-17", "history", "A genuine three-way tier/percentage crossover, for the first time.", verdict="history")
R("1C", "1C-18", "pair", "MMT + Job Guarantee, 60%, Partially Adequate — a higher percentage than both Georgism and Mutual Credit/LETS, still in the worse tier relative to Georgism.",
  [("total", "MMT", 15.5), ("tier", "MMT", "Partially Adequate"), ("total", "GEO", 13.5), ("total", "MC", 14.5), ("tier", "GEO", "Potentially Adequate")])
R("1C", "1C-19", "pair", "Georgism has the *lowest* percentage of the four but the *best* tier",
  [("total", "GEO", 13.5), ("tier", "GEO", "Potentially Adequate")] + [("tier", c, "Partially Adequate") for c in ("MC", "MMT", "INT")])
R("1C", "1C-20", "tier", "Precisely stated: the Partially Adequate tier itself now has three members (Mutual Credit/LETS, MMT+JG, Integral, spanning 56–75%)",
  [("in_tier", "Partially Adequate", ["MC", "MMT", "INT"])], verdict="stale", now="eight members, spanning 51.9% to 75.0%",
  nowspec=[("in_tier", "Partially Adequate", PART8), ("tier_pct_range", "Partially Adequate", (51.9, 75.0))])
R("1C", "1C-21", "tier", "Three real members with a 19-point spread is still a meaningfully richer basis than the single-member tier that existed before this session (Integral alone)",
  [("in_tier", "Partially Adequate", ["MC", "MMT", "INT"])], verdict="stale", now="restated with 1C-20")
R("1C", "1C-22", "pair", "land at an *exact* percentage tie (both 14.5/26, 56%)",
  [("ties", "MC", ["UBI"]), ("tier", "UBI", "Structurally Inadequate"), ("tier", "MC", "Partially Adequate")])
R("1C", "1C-23", "size", "Running the full 15-system pairwise dominance check under the retrofitted structure", verdict="stale",
  now="on the corpus, CCO-PTF-CIP-SZH fails to dominate the entries listed as fact", nowspec=[("undominated_by", "CCO", ["NSD", "CPS", "LM", "UBI", "DG", "FALC", "PE", "INT", "MC", "IF", "OS"])])
R("1C", "1C-24", "dominance", "(Nordic, Degrowth, Participatory Economics, Integral) — this is not a retrofit artifact",
  [("dominates", "CCO", c, False) for c in ("NSD", "DG", "PE", "INT")])
R("1C", "1C-25", "dominance", "(Centrally Planned Socialism, UBI, Libertarian Minarchism, FALC)",
  [("dominates", "CCO", c, False) for c in ("CPS", "UBI", "LM", "FALC")] + sc("C4.5", 0.5, "CCO") + sc("C4.5", 1.0, "CPS", "UBI", "LM", "FALC"))
R("1C", "1C-26", "record", "Full 15-system ranking under the retrofitted structure", verdict="record",
  now="pasted step1c_retrofit.py output: point to step1c_retrofit.py / step1c_retrofit_output.txt, reproduced by the harness")
R("1C", "1C-27", "history", "giving a complete 15-system, single-structure corpus for the first time.", verdict="history")


# @@REGISTER-END@@


# ------------------------------------------------------------------ run
REVIEW_KINDS = ("status", "history", "record", "error")
SIZE_RE = re.compile(r"\b(\d+)-system")
MARK = {"holds": "  ", "stale": "S ", "error": "E ", "decision": "D ", "record": "R ", "history": "H "}


def fact(part):
    fn, args = part[0], part[1:-1]
    return f"{fn}({', '.join(show(a) for a in args)}) = {show(F[fn](*args))}"


def main():
    print("=" * 92)
    print("audit_claims_s28.py -- the claim register of the eight documents not yet audited (D12, D14)")
    print("=" * 92)
    print(f"canonical corpus: {len(S)} systems; blocks: {BLOCKS[0]} (md5 {BLOCKS[1]}); documents pinned: {len(DOC)}")
    problems, seen, tally = [], set(), {}
    for d, (fname, _) in DOC.items():
        rows = [r for r in REG if r["doc"] == d]
        print(f"\n[{d}] {fname}: {len(rows)} registered claims")
        for r in rows:
            rid = r["rid"]
            if rid in seen:
                problems.append(f"{rid}: duplicate id")
            seen.add(rid)
            p = norm(r["phrase"])
            where = r["sec"] or "document"
            n = (SECT[d].get(r["sec"], "") if r["sec"] else TEXT[d]).count(p)
            if n != 1:
                problems.append(f"{rid}: phrase occurs {n} times in {where}")
            holds, bad = evaluate(r["spec"])
            if r["kind"] in REVIEW_KINDS:
                computed = r["verdict"]
            elif r["kind"] == "size":
                m = SIZE_RE.findall(p)
                computed = ("stale" if any(int(x) != len(S) for x in m) else "holds") if m else r["verdict"]
            elif r["kind"] in ("d16", "d18"):
                computed = "decision" if holds else "holds"
            else:
                computed = "holds" if holds else "stale"
            if computed != r["verdict"]:
                problems.append(f"{rid}: verdict {r['verdict']}, computed {computed} ({'; '.join(bad)})")
            ok_now, bad_now = evaluate(r["nowspec"])
            if not ok_now:
                problems.append(f"{rid}: replacement facts do not hold ({'; '.join(bad_now)})")
            tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
            review = " (review)" if r["kind"] in REVIEW_KINDS else ""
            print(f"  {MARK[r['verdict']]}{rid:7s} {r['kind']:9s} {r['verdict']}{review} [{where}] {p[:72]}{'...' if len(p) > 72 else ''}")
            if r["verdict"] != "holds":
                for b_ in bad:
                    print(f"             as written: {b_}")
                if r["now"]:
                    print(f"             now: {r['now']}")
                for part in r["nowspec"]:
                    print(f"             fact: {fact(part)}")
    print("\n" + "=" * 92)
    print("Verdicts: " + ", ".join(f"{k} {tally[k]}" for k in MARK if k in tally) + f" ({len(REG)} registered)")
    for d in DOC:
        rows = [r for r in REG if r["doc"] == d]
        act = sum(1 for r in rows if r["verdict"] in ("stale", "error", "decision", "record"))
        print(f"  {d:4s} {len(rows):3d} claims: {act:3d} to restate, correct, add or replace; "
              f"{sum(1 for r in rows if r['verdict'] == 'holds'):3d} holding; "
              f"{sum(1 for r in rows if r['verdict'] == 'history'):2d} historical")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(f"  - {p}")
        print(f"\nAUDIT FAILED ({len(problems)} problems).")
        return 1
    print("\nAUDIT PASSED: every phrase found where required; every computable verdict and every replacement fact holds.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
