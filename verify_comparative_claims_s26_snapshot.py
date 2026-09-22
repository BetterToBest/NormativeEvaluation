#!/usr/bin/env python3
"""
verify_comparative_claims.py -- NEEC Session 26: comparative claims, checked on the canonical corpus
====================================================================================================
Decision D12 (Session 26): the comparative claims in the State Capitalism /
Qatar, Islamic finance and Ostrom-style commons governance scoring documents
are stated on the canonical 23-system corpus, in place, with no appended
post-insertion notes. This script is the single checker of those claims.

SCOPE. A comparative claim, here, is any statement of another system's score
on a criterion, of another entry's flagged calls, or of a system's position in
the corpus: criterion bands ("alongside Georgism ..."), pairwise comparisons,
ranks, ties, strict dominance, domain positions and splits, flag counts, and
tier robustness. Characterisations of another system's design, scope or
evidence ("the direct analogue of Georgism's dividend", archetype membership)
are argument rather than data and are not checked here. Each entry's own
arithmetic, transcription and sensitivity claims are checked by its entry
verifier (verify_qatar.py, verify_islamicfinance.py, verify_ostrom.py).

ASSERT, DON'T ONLY PRINT (D3(b)). Every check is an assertion. A claim passes
only if the computed fact holds AND the sentence stating it appears verbatim
in the document (whitespace collapsed, bold markers removed). Criterion-band
references must appear inside the section of the criterion they concern.

SOURCES. The canonical corpus is imported from the unmodified
neec_weighting_robustness_analysis_v2.py and its own transcription self-check
must pass. Entry vectors and flag registers are read, never executed, from the
entry verifiers (Python literals, via ast). Flag counts for entries without a
register are bounded from their documents of record (see group [F]).

Check groups:
  [A] sources and identities
  [B] criterion-level references to other systems' scores and flagged calls
  [C] State Capitalism / Qatar: corpus position and pairwise comparisons
  [D] Islamic finance: corpus position and pairwise comparisons
  [E] Ostrom-style commons governance: corpus position and pairwise comparisons
  [F] flag counts and tier robustness across the corpus
  [G] superseded wording is gone (the Session 25 audit register, resolved)
  [H] the two corpus tables are byte-identical to a fresh render

Modes:
  python3 verify_comparative_claims.py          run every check (the captured output)
  python3 verify_comparative_claims.py --fill   rewrite the two corpus tables in place, then exit

Looks for its inputs beside itself, then in the working directory, and prints
only file names, so the captured output reproduces byte for byte from any
directory holding the inputs. Writes nothing unless --fill is given.
Deterministic: no clock, no randomness, no dict-order dependence.
"""
import ast
import contextlib
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def locate(name):
    for d in (HERE, os.getcwd()):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: cannot find {name} beside this script or in the working directory")


def read(name):
    with open(locate(name), encoding="utf-8") as f:
        return f.read()


CANON_FILE = "neec_weighting_robustness_analysis_v2.py"
DOC_FILE = {
    "QA": "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
    "IF": "NEEC_IslamicFinance_scoring_scratch.md",
    "OS": "NEEC_Ostrom_Commons_scoring_scratch.md",
}
# Documents of record used only to bound flag counts (group [F]).
OLDER_STEP1B_DOC = {
    "GEO": "NEEC_Georgism_LVT_scoring_scratch.md",
    "MC": "NEEC_MutualCredit_LETS_scoring_scratch.md",
    "DE": "NEEC_DoughnutEconomics_scoring_scratch.md",
    "UBS": "NEEC_UniversalBasicServices_scoring_scratch.md",
    "SWF": "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
}
REGISTER_DOC = {
    "CN": "NEEC_StateCapitalism_China_scoring_scratch.md",
    "SG": "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
    "QA": DOC_FILE["QA"], "IF": DOC_FILE["IF"], "OS": DOC_FILE["OS"],
}
LEGACY_DOCS = ("NEEC_Report_v1_6.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md")

N = {  # short keys used throughout this script
    "SQ": "Status Quo Market Capitalism", "NSD": "Nordic Social Democracy",
    "CPS": "Centrally Planned Socialism", "MS": "Market Socialism",
    "LM": "Libertarian Minarchism", "MMT": "MMT + Job Guarantee",
    "UBI": "Universal Basic Income", "DG": "Degrowth Economics",
    "SC": "Stakeholder Capitalism", "FALC": "Fully Automated Luxury Communism",
    "PE": "Participatory Economics", "CCO": "CCO-PTF-CIP-SZH", "INT": "Integral",
    "GEO": "Georgism / Land Value Tax", "MC": "Mutual Credit / LETS",
    "DE": "Doughnut Economics", "UBS": "Universal Basic Services",
    "SWF": "Sovereign Wealth Fund Statism", "CN": "State Capitalism / China",
    "SG": "State Capitalism / Singapore", "QA": "State Capitalism / Qatar",
    "IF": "Islamic Finance / Profit-Sharing Banking",
    "OS": "Ostrom-Style Commons Governance",
}
STEP1B = ("GEO", "MC", "DE", "UBS", "SWF", "CN", "SG", "QA", "IF", "OS")

# ------------------------------------------------------------------ corpus
_spec = importlib.util.spec_from_file_location("_neec_canon", locate(CANON_FILE))
canon = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(canon)
    try:
        SELF_CHECK = canon.verify_transcription()
    except AssertionError:          # the canonical self-check raises on a transcription mismatch
        SELF_CHECK = False
SCORES = canon.SCORES
CRITS = list(canon.ALL_CRITS)
DOM = {f"D{k}": [c for c in CRITS if c.startswith(f"C{k}.")] for k in range(1, 6)}
LEGACY = tuple(k for k, v in N.items() if v in canon.PUBLISHED_LEGACY_25)


def V(k):
    return SCORES[N[k]]


def total(v):
    return sum(v[c] for c in CRITS)


def nfail(v):
    return sum(1 for c in CRITS if v[c] == 0.0)


def fails(v):
    return [c for c in CRITS if v[c] == 0.0]


def dsum(v, d):
    return sum(v[c] for c in DOM[d])


def vdom(a, b):
    """Strict dominance between two vectors (validated against canonical.dominates in [A])."""
    return all(a[c] >= b[c] for c in CRITS) and any(a[c] > b[c] for c in CRITS)


def rank(k):
    """Competition rank by total (1 = highest)."""
    return 1 + sum(1 for s in SCORES.values() if total(s) > total(V(k)))


def keys_at_total(t, exclude=()):
    return sorted(k for k in N if abs(total(V(k)) - t) < 1e-9 and k not in exclude)


def higher_lower(a, b):
    """Criteria on which vector a is higher / lower than vector b, in canonical order."""
    return ([c for c in CRITS if a[c] > b[c]], [c for c in CRITS if a[c] < b[c]])


def hamming(a, b):
    return sum(1 for c in CRITS if a[c] != b[c])


def lst(items):
    items = list(items)
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + ", and " + items[-1]


def deltas(a, b):
    """Domain deltas a minus b, formatted as the documents state them."""
    return ", ".join(f"{dsum(a, d) - dsum(b, d) + 0.0:+.1f}" for d in DOM)


ALL_PAIRS = [(a, b) for a in N for b in N if a != b and canon.dominates(N[a], N[b])]


# ------------------------------------------------------------------ entry verifiers (read, not run)
def literal(filename, name):
    tree = ast.parse(read(filename))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            return ast.literal_eval(node.value)
    sys.exit(f"ERROR: {name} is not a literal assignment in {filename}")


def alts(reg):
    """A flag register as {criterion: alternative score} (Singapore, China and Qatar store (score, note))."""
    return {c: (a[0] if isinstance(a, tuple) else a) for c, a in reg.items()}


ENTRY_VEC = {
    "QA": literal("verify_qatar.py", "QA"),
    "IF": literal("verify_islamicfinance.py", "SCORE"),
    "OS": literal("verify_ostrom.py", "OSTROM"),
    "SG": literal("verify_singapore.py", "SG"),
    "CN": literal("verify_china.py", "CHINA"),
}
FLAGS = {
    "QA": alts(literal("verify_qatar.py", "FLAGGED")),
    "IF": alts(literal("verify_islamicfinance.py", "FLAGGED")),
    "OS": alts(literal("verify_ostrom.py", "FLAGS")),
    "SG": alts(literal("verify_singapore.py", "FLAGGED")),
    "CN": alts(literal("verify_china.py", "FLAGGED")),
}
QA_CITIZENS = literal("verify_qatar.py", "CITIZENS_ONLY")
IF_READING_A = literal("verify_islamicfinance.py", "READING_A")
IF_READING_C = literal("verify_islamicfinance.py", "READING_C")
IF_BROAD = literal("verify_islamicfinance.py", "BROAD_SCOPE")


def moved(v, changes):
    out = dict(v)
    out.update(changes)
    return out


def extreme(k, up):
    """The all-upward (up=True) or all-downward reading of an entry's flag register."""
    v = V(k)
    return moved(v, {c: a for c, a in FLAGS[k].items() if (a > v[c]) == up})


def span(k):
    """(points, failures) between the all-upward and all-downward readings: the enumeration's extremes."""
    hi, lo = extreme(k, True), extreme(k, False)
    return total(hi) - total(lo), nfail(lo) - nfail(hi)


def undisputed(k):
    return [c for c in fails(V(k)) if FLAGS[k].get(c, 0.0) == 0.0]


# ------------------------------------------------------------------ documents
def norm(s):
    return re.sub(r"\s+", " ", s.replace("**", "")).strip()


RAW = {k: read(f) for k, f in DOC_FILE.items()}
TEXT = {k: norm(t) for k, t in RAW.items()}
CRIT_HEAD = re.compile(r"^#{2,4} (C[1-5]\.[1-6][ab]?)\b")


def sections(raw):
    """Criterion sections: from a criterion heading to the next criterion heading or level 1-3 heading."""
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


SECTION = {k: sections(t) for k, t in RAW.items()}

# ------------------------------------------------------------------ checks
RESULTS = []


def check(group, label, cond, detail=""):
    RESULTS.append((group, label, bool(cond), detail))


def claim(group, doc, label, cond, phrase, detail=""):
    present = norm(phrase) in TEXT[doc]
    why = [] if cond else ["computed fact does not hold" + (f" ({detail})" if detail else "")]
    if not present:
        why.append(f"phrase not found: {norm(phrase)!r}")
    check(group, f"{doc}: {label}", cond and present, "; ".join(why))


# ---- [A] sources and identities
check("A", f"{CANON_FILE}: own transcription self-check passes", SELF_CHECK is True)
check("A", "canonical corpus holds 23 systems, 13 legacy and 10 Step 1b",
      len(SCORES) == 23 and len(LEGACY) == 13 and set(N.values()) == set(SCORES)
      and set(LEGACY) | set(STEP1B) == set(N) and not set(LEGACY) & set(STEP1B))
check("A", "every canonical vector scores all 26 criteria in {0, 0.5, 1}",
      all(set(v) == set(CRITS) and all(x in (0.0, 0.5, 1.0) for x in v.values()) for v in SCORES.values()))
check("A", "vector-level dominance agrees with canonical.dominates on all 506 ordered pairs",
      all(vdom(V(a), V(b)) == canon.dominates(N[a], N[b]) for a in N for b in N if a != b))
for k in ("QA", "IF", "OS", "SG", "CN"):
    check("A", f"{N[k]}: the entry verifier's vector equals the canonical vector", ENTRY_VEC[k] == V(k))
for k in ("QA", "IF", "OS", "SG", "CN"):
    reg = FLAGS[k]
    check("A", f"{N[k]}: flag register names real criteria, each alternative differs by 0.5",
          all(c in CRITS and abs(a - V(k)[c]) == 0.5 for c, a in reg.items()))
for k in ("QA", "IF", "OS"):
    check("A", f"{DOC_FILE[k]}: all 26 criterion sections found", set(SECTION[k]) == set(CRITS))
    check("A", f"{DOC_FILE[k]}: names verify_comparative_claims.py as its checker",
          "verify_comparative_claims.py" in TEXT[k])

# ---- [B] criterion-level references (claimed value, taken from the sentence; checked on the corpus)
REFS = [
    # (doc, criterion, anchor in that criterion's section, claimed score, systems)
    ("IF", "C1.1", "alongside Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, and Universal Basic "
                   "Services", 0.5, ("GEO", "MC", "SWF", "UBS")),
    ("IF", "C1.2a", "more than Integral's dissolving credits (0.0) and more than Georgism's dividend (0.0)", 0.0,
     ("INT", "GEO")),
    ("IF", "C1.2b", "as it is for Status Quo Market Capitalism and Universal Basic Services", 0.0, ("SQ", "UBS")),
    ("IF", "C1.4", "applies, as it does to Status Quo Market Capitalism", 0.0, ("SQ",)),
    ("IF", "C1.4", "score 0.5, as Georgism, Mutual Credit / LETS, and Sovereign Wealth Fund Statism are scored", 0.5,
     ("GEO", "MC", "SWF")),
    ("IF", "C1.4", "which Status Quo Market Capitalism already has and is scored 0.0 for", 0.0, ("SQ",)),
    ("IF", "C2.1", "applies, as for Status Quo Market Capitalism", 0.5, ("SQ",)),
    ("IF", "C2.3", "alongside Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, and Status Quo Market "
                   "Capitalism", 0.5, ("GEO", "MC", "SWF", "SQ")),
    ("IF", "C2.4", "the same 0.5 given to Georgism, Mutual Credit / LETS, and Sovereign Wealth Fund Statism", 0.5,
     ("GEO", "MC", "SWF")),
    ("IF", "C2.5", "matches Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, and Universal Basic "
                   "Services", 1.0, ("GEO", "MC", "SWF", "UBS")),
    ("IF", "C3.1", "the same one Market Socialism occupies for cooperative-level resilience", 0.5, ("MS",)),
    ("IF", "C3.4", "the corpus's 1.0 band as given to Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, "
                   "and Universal Basic Services", 1.0, ("GEO", "MC", "SWF", "UBS")),
    ("IF", "C3.5", "the band Stakeholder Capitalism occupies for systemic failures obscured behind positive "
                   "messaging", 0.0, ("SC",)),
    ("IF", "C4.1", "applies, the same band as Nordic Social Democracy", 0.5, ("NSD",)),
    ("IF", "C4.2", "the same finding the corpus records against Stakeholder Capitalism's ESG metrics", 0.0, ("SC",)),
    ("IF", "C4.3", "applies, the band Integral occupies", 0.5, ("INT",)),
    ("IF", "C4.4", "applies, the band Status Quo Market Capitalism occupies", 0.0, ("SQ",)),
    ("IF", "C4.4", "the band Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, and Universal Basic "
                   "Services occupy", 0.5, ("GEO", "MC", "SWF", "UBS")),
    ("IF", "C4.5", "the band Nordic Social Democracy occupies for the same shape of finding", 0.5, ("NSD",)),
    ("IF", "C5.5", "the reasoning behind Market Socialism's 0.0 here", 0.0, ("MS",)),
    ("QA", "C1.1", "the reading behind China's and Singapore's flagged alternatives and the Centrally Planned "
                   "Socialism precedent", 1.0, ("CPS",)),
    ("QA", "C1.2a", "This differs from Singapore's 1.0", 1.0, ("SG",)),
    ("QA", "C1.2b", "This matches Nordic Social Democracy, Sovereign Wealth Fund Statism, China, and Singapore", 0.5,
     ("NSD", "SWF", "CN", "SG")),
    ("QA", "C1.4", "This matches Sovereign Wealth Fund Statism, China, and Singapore", 0.5, ("SWF", "CN", "SG")),
    ("QA", "C1.5", "This differs from Singapore's 0.5, where the excluded group was about a fifth", 0.5, ("SG",)),
    ("QA", "C1.5", "the Market Socialism anchor treats a membership gate as the 0.5 case", 0.5, ("MS",)),
    ("QA", "C2.1", "This differs from Singapore's 0.5, whose permit regime covered about a fifth", 0.5, ("SG",)),
    ("QA", "C2.2", "This matches China and Singapore", 0.0, ("CN", "SG")),
    ("QA", "C2.2", "0.5, a real but conditional baseline (the Nordic anchor case)", 0.5, ("NSD",)),
    ("QA", "C2.3", "This matches China and Singapore, on less direct evidence", 0.5, ("CN", "SG")),
    ("QA", "C2.4", "This matches China and the Centrally Planned Socialism precedent", 0.0, ("CN", "CPS")),
    ("QA", "C2.5", "the Nordic-style structural failure does not apply", 0.0, ("NSD",)),
    ("QA", "C2.5", "This matches China, Singapore, and the Status Quo anchor", 0.5, ("CN", "SG", "SQ")),
    ("QA", "C3.1", "This matches Sovereign Wealth Fund Statism, China, and Singapore", 0.5, ("SWF", "CN", "SG")),
    ("QA", "C3.2", "the band of the H.7 MMT anchor", 0.5, ("MMT",)),
    ("QA", "C3.2", "This differs from China's and Singapore's 1.0", 1.0, ("CN", "SG")),
    ("QA", "C3.4", "would score 1.0, as Singapore and Sovereign Wealth Fund Statism were scored", 1.0, ("SG", "SWF")),
    ("QA", "C3.5", "follows China's 0.0", 0.0, ("CN",)),
    ("QA", "C4.1", "the shape of the Nordic anchor, at a larger scale", 0.5, ("NSD",)),
    ("QA", "C4.1", "Sovereign Wealth Fund Statism scored 1.0 on the strength of the fund's founding purpose", 1.0,
     ("SWF",)),
    ("QA", "C4.2", "This matches Sovereign Wealth Fund Statism, China, and Singapore", 0.0, ("SWF", "CN", "SG")),
    ("QA", "C4.3", "its 0.0 example, Status Quo Market Capitalism, is published at 0.5", 0.5, ("SQ",)),
    ("QA", "C4.3", "This matches China", 0.0, ("CN",)),
    ("QA", "C4.4", "This matches China, and Singapore's flagged 0.0", 0.0, ("CN", "SG")),
    ("QA", "C4.5", "This matches Sovereign Wealth Fund Statism, China, and Singapore", 0.0, ("SWF", "CN", "SG")),
    ("QA", "C5.1", "This matches China and Singapore", 1.0, ("CN", "SG")),
    ("QA", "C5.2", "This matches China and Singapore", 0.5, ("CN", "SG")),
    ("QA", "C5.3", "This matches Sovereign Wealth Fund Statism and Singapore", 1.0, ("SWF", "SG")),
    ("QA", "C5.5", "This differs from Sovereign Wealth Fund Statism's 0.5", 0.5, ("SWF",)),
    ("OS", "C1.2a", "the same call Georgism, Mutual Credit / LETS and Universal Basic Services received on this "
                    "criterion", 0.0, ("GEO", "MC", "UBS")),
    ("OS", "C1.2a", "the basis on which Sovereign Wealth Fund Statism scored 0.5 here", 0.5, ("SWF",)),
    ("OS", "C1.2b", "the basis on which Mutual Credit / LETS scored 1.0 here", 1.0, ("MC",)),
    ("OS", "C1.3", "matching Georgism and Universal Basic Services", 0.5, ("GEO", "UBS")),
    ("OS", "C1.3", "the basis on which Mutual Credit / LETS and Sovereign Wealth Fund Statism scored 0.0 here", 0.0,
     ("MC", "SWF")),
    ("OS", "C1.4", "the same logic on which Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism and "
                   "Universal Basic Services each scored 0.5 here", 0.5, ("GEO", "MC", "SWF", "UBS")),
    ("OS", "C2.2", "the basis on which Georgism, Mutual Credit / LETS and Universal Basic Services scored 0.5 here",
     0.5, ("GEO", "MC", "UBS")),
    ("OS", "C2.4", "the level Participatory Economics, Degrowth Economics and Nordic Social Democracy reach on this "
                   "criterion", 1.0, ("PE", "DG", "NSD")),
    ("OS", "C2.5", "matching Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, Universal Basic Services "
                   "and Doughnut Economics", 1.0, ("GEO", "MC", "SWF", "UBS", "DE")),
    ("OS", "C4.4", "Islamic finance's investment account holders have no governance rights over the assets their "
                   "funds are in, and scored 0.0 here", 0.0, ("IF",)),
    ("OS", "C4.5", "above the 0.0 recorded for Sovereign Wealth Fund Statism, Doughnut Economics, Status Quo Market "
                   "Capitalism and Participatory Economics", 0.0, ("SWF", "DE", "SQ", "PE")),
    ("OS", "C5.5", "shared with Participatory Economics, Mutual Credit / LETS and Islamic finance", 1.0,
     ("PE", "MC", "IF")),
]
for doc, crit, anchor, value, systems in REFS:
    got = {k: V(k)[crit] for k in systems}
    in_section = norm(anchor) in SECTION[doc][crit]
    ok = all(abs(x - value) < 1e-9 for x in got.values()) and in_section
    why = []
    if not in_section:
        why.append(f"anchor not found in the {crit} section: {norm(anchor)!r}")
    bad = {k: x for k, x in got.items() if abs(x - value) > 1e-9}
    if bad:
        why.append("corpus scores differ: " + ", ".join(f"{N[k]} {x}" for k, x in bad.items()))
    names = ", ".join(N[k] for k in systems)
    check("B", f"{doc} {crit}: {names} at {value:.1f}", ok, "; ".join(why))

FLAG_REFS = [
    # (doc, criterion, anchor in that section, entry, relation, value)
    ("QA", "C1.1", "the reading behind China's and Singapore's flagged alternatives", "CN", "alternative", 1.0),
    ("QA", "C1.1", "the reading behind China's and Singapore's flagged alternatives", "SG", "alternative", 1.0),
    ("QA", "C1.1", "would put measured extreme poverty close to zero", "QA", "alternative", 1.0),
    ("QA", "C4.2", "Unlike Singapore's, this call is not flagged", "SG", "flagged", None),
    ("QA", "C4.2", "Unlike Singapore's, this call is not flagged", "QA", "unflagged", None),
    ("QA", "C4.4", "Singapore's flagged 0.0", "SG", "flagged", None),
    ("QA", "C5.4", "as Singapore's flag did for six decades of majorities", "SG", "alternative", 1.0),
    ("QA", "C5.4", "A downward reading (0.0, as in China's flag)", "CN", "alternative", 0.0),
]
for doc, crit, anchor, k, rel, value in FLAG_REFS:
    in_section = norm(anchor) in SECTION[doc][crit]
    reg = FLAGS[k]
    if rel == "alternative":
        fact, what = crit in reg and abs(reg[crit] - value) < 1e-9, f"flagged, alternative {value:.1f}"
    elif rel == "flagged":
        fact, what = crit in reg, "flagged"
    else:
        fact, what = crit not in reg, "not flagged"
    why = [] if in_section else [f"anchor not found in the {crit} section: {norm(anchor)!r}"]
    if not fact:
        why.append(f"{N[k]}'s register does not show {crit} {what}")
    check("B", f"{doc} {crit}: {N[k]}'s {crit} is {what}", fact and in_section, "; ".join(why))

# ---- [C] State Capitalism / Qatar
qa, sg, cn, swf = V("QA"), V("SG"), V("CN"), V("SWF")
qa_up = extreme("QA", True)
qa_cit = moved(qa, QA_CITIZENS)
g = "C"
claim(g, "QA", "ranks 22nd of 23, above only Libertarian Minarchism, no exact tie",
      rank("QA") == 22 and len(SCORES) == 23 and keys_at_total(total(qa), ("QA",)) == []
      and [k for k in N if total(V(k)) < total(qa)] == ["LM"] and abs(total(V("LM")) - 8.0) < 1e-9,
      "In the canonical 23-system corpus, Qatar ranks 22nd of 23, above only Libertarian Minarchism (8.0/26), "
      "with no exact tie.")
dom_by_qa = sorted(a for a, b in ALL_PAIRS if b == "QA")
claim(g, "QA", "dominated by exactly CCO-PTF-CIP-SZH and Singapore; dominates nothing",
      dom_by_qa == ["CCO", "SG"] and not [b for a, b in ALL_PAIRS if a == "QA"],
      "It is dominated by CCO-PTF-CIP-SZH and State Capitalism / Singapore, and dominates no system.")
claim(g, "QA", "14 ordered strict-dominance pairs, 2 with Qatar dominated",
      len(ALL_PAIRS) == 14 and len(dom_by_qa) == 2,
      "The corpus holds 14 ordered strict-dominance pairs, 2 of them with Qatar as the dominated system.")
non_cco = sorted((a, b) for a, b in ALL_PAIRS if "CCO" not in (a, b))
claim(g, "QA", "three pairs do not involve CCO-PTF-CIP-SZH: SG>CN, SG>QA, IF>SC",
      non_cco == sorted([("SG", "CN"), ("SG", "QA"), ("IF", "SC")]),
      "Three do not involve CCO-PTF-CIP-SZH: Singapore over China and Singapore over Qatar, both between "
      "state-capitalism siblings, and Islamic finance over Stakeholder Capitalism.", f"got {non_cco}")
at_up = keys_at_total(total(qa_up), ("QA",))
claim(g, "QA", "the joint upward total (14.0) is SWF Statism's, Singapore's and Ostrom's, in another tier",
      abs(total(qa_up) - 14.0) < 1e-9 and at_up == sorted(["SWF", "SG", "OS"])
      and canon.tier(nfail(qa_up)) == "Structurally Inadequate"
      and all(canon.tier(nfail(V(k))) == "Partially Adequate" for k in at_up),
      "The upward extreme reaches the same 14.0/26 as Sovereign Wealth Fund Statism, Singapore, and Ostrom-style "
      "commons governance, in a different tier", f"at 14.0: {at_up}")
claim(g, "QA", "the citizens-only total (13.0) is Fully Automated Luxury Communism's alone",
      abs(total(qa_cit) - 13.0) < 1e-9 and keys_at_total(total(qa_cit), ("QA",)) == ["FALC"],
      "it ties Fully Automated Luxury Communism at 13.0/26")
d4_low = min(dsum(V(k), "D4") for k in N)
claim(g, "QA", "Domain 4 (0.5) ties China and Status Quo for the corpus's lowest",
      abs(dsum(qa, "D4") - 0.5) < 1e-9 and abs(d4_low - 0.5) < 1e-9
      and sorted(k for k in N if abs(dsum(V(k), "D4") - d4_low) < 1e-9) == sorted(["QA", "CN", "SQ"]),
      "Domain 4 (0.5/5) ties China and Status Quo Market Capitalism for the lowest in the corpus")
cohort = [k for k in STEP1B if k != "QA"]
claim(g, "QA", "lowest total and most failures of the ten Step 1b systems",
      len(STEP1B) == 10 and all(total(V(k)) > total(qa) and nfail(V(k)) < nfail(qa) for k in cohort),
      "Qatar has the lowest total (9.0/26) and the most failures (10) of the ten Step 1b systems")
hi_swf, lo_swf = higher_lower(qa, swf)
claim(g, "QA", "vs SWF Statism: 5.0 points and 7 failures apart",
      abs(total(swf) - 14.0) < 1e-9 and nfail(swf) == 3 and abs(total(swf) - total(qa) - 5.0) < 1e-9
      and nfail(qa) - nfail(swf) == 7,
      "stands at 14.0/26 with 3 failures against 9.0/26 with 10: a difference of 5.0 points and 7 failures")
claim(g, "QA", "vs SWF Statism: 12 criteria differ, Qatar higher only on C1.3",
      hamming(qa, swf) == 12 and hi_swf == ["C1.3"],
      "The two differ on 12 criteria, and Qatar is higher on only one, C1.3")
claim(g, "QA", "vs SWF Statism: shared failures C4.2 and C4.5",
      [c for c in fails(qa) if c in fails(swf)] == ["C4.2", "C4.5"], "They share two failures, C4.2 and C4.5.")
claim(g, "QA", "vs SWF Statism: domain deltas", deltas(qa, swf) == "+0.0, -2.0, -1.0, -1.5, -0.5",
      "The domain deltas (Qatar minus Sovereign Wealth Fund Statism) are +0.0, -2.0, -1.0, -1.5, -0.5.")
worst = sorted(DOM, key=lambda d: (dsum(qa, d) - dsum(swf, d), d))[:2]
claim(g, "QA", "vs SWF Statism: the configuration costs most in Domains 2 and 4",
      sorted(worst) == ["D2", "D4"], "costs most in Human Autonomy and Ethical Integrity", f"got {worst}")
hi_sg, lo_sg = higher_lower(qa, sg)
claim(g, "QA", "Singapore strictly dominates Qatar: higher on 10, lower on none",
      canon.dominates(N["SG"], N["QA"]) and len(lo_sg) == 10 and not hi_sg,
      "Singapore strictly dominates Qatar: it is higher on 10 criteria and lower on none")
claim(g, "QA", "vs Singapore: domain deltas", deltas(qa, sg) == "-1.5, -1.0, -1.5, -0.5, -0.5",
      "the domain deltas (Qatar minus Singapore) are -1.5, -1.0, -1.5, -0.5, -0.5.")
claim(g, "QA", "Singapore's 4 failures are a subset of Qatar's 10",
      nfail(sg) == 4 and set(fails(sg)) < set(fails(qa)), "Singapore's 4 failures are a subset of Qatar's 10.")
hi_cn, lo_cn = higher_lower(qa, cn)
claim(g, "QA", "neither China nor Qatar dominates the other",
      not canon.dominates(N["CN"], N["QA"]) and not canon.dominates(N["QA"], N["CN"]),
      "Neither China nor Qatar dominates the other.")
claim(g, "QA", "vs China: 4 criteria differ",
      hamming(qa, cn) == 4 and hi_cn == ["C5.3"] and lo_cn == ["C1.5", "C3.2", "C5.5"],
      "China and Qatar differ on only 4 criteria: Qatar is higher on C5.3 and lower on C1.5, C3.2, and C5.5.")
claim(g, "QA", "China's 8 failures are a subset of Qatar's 10; China is 1.0 higher",
      nfail(cn) == 8 and set(fails(cn)) < set(fails(qa)) and abs(total(cn) - total(qa) - 1.0) < 1e-9,
      "China's 8 failures are a subset of Qatar's 10, and China's total is higher by 1.0 point.")
claim(g, "QA", "the three state-capitalism entries span two tiers",
      [canon.tier(nfail(V(k))) for k in ("CN", "SG", "QA")]
      == ["Structurally Inadequate", "Partially Adequate", "Structurally Inadequate"]
      and (total(cn), total(sg), total(qa)) == (10.0, 14.0, 9.0),
      "now span two tiers: China (10.0/26, Structurally Inadequate), Singapore (14.0/26, Partially Adequate), "
      "and Qatar (9.0/26, Structurally Inadequate)")

# ---- [D] Islamic finance
f_ = V("IF")
cco = V("CCO")
g = "D"
tie135 = keys_at_total(total(f_), ("IF",))
claim(g, "IF", "exact three-way tie at 13.5 with Georgism and UBS: 5, 2 and 3 failures, two tiers",
      abs(total(f_) - 13.5) < 1e-9 and tie135 == ["GEO", "UBS"]
      and [nfail(V(k)) for k in ("IF", "GEO", "UBS")] == [5, 2, 3]
      and [canon.tier(nfail(V(k))) for k in ("IF", "GEO", "UBS")]
      == ["Partially Adequate", "Potentially Adequate", "Partially Adequate"],
      "Islamic finance, Georgism / Land Value Tax, and Universal Basic Services all score exactly 13.5/26 (51.9%), "
      "with 5, 2, and 3 structural failures respectively — Partially Adequate, Potentially Adequate, Partially "
      "Adequate.", f"at 13.5: {tie135}")
claim(g, "IF", "the tie: one percentage, three failure counts, two tiers",
      len({nfail(V(k)) for k in ("IF", "GEO", "UBS")}) == 3
      and len({canon.tier(nfail(V(k))) for k in ("IF", "GEO", "UBS")}) == 2,
      "three systems, one percentage, three failure counts, two tiers")
d5_best = max(dsum(V(k), "D5") for k in N)
claim(g, "IF", "Domain 5 (4.5) ties CCO-PTF-CIP-SZH for the highest; no other system reaches it",
      abs(dsum(f_, "D5") - 4.5) < 1e-9 and abs(d5_best - 4.5) < 1e-9
      and sorted(k for k in N if abs(dsum(V(k), "D5") - d5_best) < 1e-9) == ["CCO", "IF"],
      "Domain 5 of 4.5/5 ties CCO-PTF-CIP-SZH for the highest in the corpus, and no other system reaches it.")
claim(g, "IF", "the Domain 5 co-leader is the framework's own top-ranked entry", rank("CCO") == 1,
      "Its implementation viability is the highest NEEC has scored anywhere, tied with the framework's own "
      "top-ranked entry")
split54 = {k: dsum(V(k), "D5") - dsum(V(k), "D4") for k in N}
wider = sorted(k for k in N if split54[k] > split54["IF"] + 1e-9)
at25 = sorted(k for k in N if abs(split54[k] - 2.5) < 1e-9)
claim(g, "IF", "second-widest Domain 5 minus Domain 4 split (3.0); only Status Quo wider (3.5)",
      abs(split54["IF"] - 3.0) < 1e-9 and wider == ["SQ"] and abs(split54["SQ"] - 3.5) < 1e-9
      and (dsum(V("SQ"), "D5"), dsum(V("SQ"), "D4")) == (4.0, 0.5)
      and not [k for k in N if k != "IF" and abs(split54[k] - 3.0) < 1e-9],
      "The second-widest viability-versus-ethics split in the corpus. Domain 5 at 4.5/5 sits against Domain 4 at "
      "1.5/5, a 3.0-point gap")
d4 = {k: dsum(V(k), "D4") for k in N}
lower_d4 = sorted(k for k in N if d4[k] < d4["IF"] - 1e-9)
claim(g, "IF", "Domain 4 (1.5) is sixth-lowest of 23, tied only with Libertarian Minarchism",
      abs(d4["IF"] - 1.5) < 1e-9 and len(lower_d4) == 5
      and sorted(k for k in N if k != "IF" and abs(d4[k] - 1.5) < 1e-9) == ["LM"],
      "the Domain 4 score is the sixth-lowest of the twenty-three systems (tied with Libertarian Minarchism)")
claim(g, "IF", "the final assessment restates Domain 4 as sixth-lowest of twenty-three",
      len(lower_d4) == 5 and len(SCORES) == 23,
      "its ethical integrity is sixth-lowest of the twenty-three")
claim(g, "IF", "CCO-PTF-CIP-SZH scores 4.5 in Domain 4 as well", abs(dsum(cco, "D4") - 4.5) < 1e-9,
      "CCO-PTF-CIP-SZH, scores 4.5 in Domain 4 as well")
claim(g, "IF", "Status Quo's gap is wider; the three state-capitalism entries follow at 2.5",
      abs(split54["SQ"] - 3.5) < 1e-9 and at25 == sorted(["CN", "SG", "QA"]),
      "Only Status Quo Market Capitalism, at 4.0 against 0.5, has a wider gap (3.5), and it is the comparison the "
      "entry invites; the three state-capitalism entries follow at 2.5.", f"at 2.5: {at25}")
not_dom_by_cco = sorted(b for b in N if b != "CCO" and not canon.dominates(N["CCO"], N[b]))
claim(g, "IF", "one of the 11 entries CCO-PTF-CIP-SZH does not dominate; C5.5 the sole reason",
      len(not_dom_by_cco) == 11 and "IF" in not_dom_by_cco and higher_lower(f_, cco)[0] == ["C5.5"]
      and (f_["C5.5"], cco["C5.5"]) == (1.0, 0.5),
      "one of the 11 entries CCO-PTF-CIP-SZH does not strictly dominate, and C5.5 is the sole reason: Islamic "
      "finance scores 1.0 on cultural adaptability where CCO-PTF-CIP-SZH scores 0.5, and it is the only criterion "
      "on which it scores higher.")
claim(g, "IF", "not dominated by anything", not [a for a, b in ALL_PAIRS if b == "IF"],
      "Not dominated by anything, including CCO-PTF-CIP-SZH.")
hi_sc, lo_sc = higher_lower(f_, V("SC"))
step1b_over_legacy = sorted((a, b) for a, b in ALL_PAIRS if a in STEP1B and b in LEGACY)
claim(g, "IF", "strictly dominates Stakeholder Capitalism (6 higher, none lower): the only Step 1b > legacy pair",
      [b for a, b in ALL_PAIRS if a == "IF"] == ["SC"] and len(hi_sc) == 6 and not lo_sc
      and step1b_over_legacy == [("IF", "SC")],
      "It strictly dominates Stakeholder Capitalism (higher on 6 criteria, lower on none), the corpus's only case "
      "of a Step 1b entry dominating one of the 13 legacy systems.", f"Step 1b over legacy: {step1b_over_legacy}")
claim(g, "IF", "14 ordered strict-dominance pairs in all", len(ALL_PAIRS) == 14,
      "The corpus holds 14 ordered strict-dominance pairs in all.")
hi_sq, lo_sq = higher_lower(f_, V("SQ"))
claim(g, "IF", "vs Status Quo: 8 differ, 7 higher (listed), +3.0",
      hamming(f_, V("SQ")) == 8 and hi_sq == ["C2.5", "C3.1", "C3.3", "C3.4", "C4.1", "C4.5", "C5.5"]
      and abs(total(f_) - total(V("SQ")) - 3.0) < 1e-9,
      "It differs from Status Quo Market Capitalism on 8 criteria and is higher on 7 of them (C2.5, C3.1, C3.3, "
      "C3.4, C4.1, C4.5, C5.5), for a 3.0-point gain")
claim(g, "IF", "the final assessment restates: above Status Quo on seven criteria", len(hi_sq) == 7,
      "the entry scores above Status Quo Market Capitalism on seven criteria")
claim(g, "IF", "vs Georgism (10 differ) and UBS (8 differ): no dominance either way",
      hamming(f_, V("GEO")) == 10 and hamming(f_, V("UBS")) == 8
      and not any(canon.dominates(N[a], N[b]) for a, b in
                  (("IF", "GEO"), ("GEO", "IF"), ("IF", "UBS"), ("UBS", "IF"))),
      "Against its tie partners. It differs from Georgism on 10 criteria and from Universal Basic Services on 8, "
      "and neither dominates in either direction despite the identical totals.")
hi_swf2, _ = higher_lower(f_, swf)
claim(g, "IF", "vs SWF Statism: 9 differ, IF higher on C1.3, C4.5, C5.2, C5.5",
      hamming(f_, swf) == 9 and hi_swf2 == ["C1.3", "C4.5", "C5.2", "C5.5"],
      "Their scores differ on 9 criteria, with Islamic finance higher on 4 (C1.3, C4.5, C5.2, C5.5).")
broad = moved(f_, IF_BROAD)
claim(g, "IF", "the broad-scope total (14.5, same tier) would tie Mutual Credit / LETS and UBI",
      abs(total(broad) - 14.5) < 1e-9 and keys_at_total(14.5, ("IF",)) == ["MC", "UBI"]
      and canon.tier(nfail(broad)) == canon.tier(nfail(f_)),
      "The tier does not move, but the total would tie Mutual Credit / LETS and Universal Basic Income.")
# Archetype membership is the documents' own classification (argument, not data); this script takes it
# from the Ostrom document's statement, which names all five members, and checks the scores against it.
ARCHETYPE_1 = ("GEO", "MC", "SWF", "IF", "OS")
claim(g, "OS", "archetype 1 (narrow single-mechanism systems) has five members, as the documents classify them",
      len(ARCHETYPE_1) == 5 and set(ARCHETYPE_1) <= set(STEP1B),
      "Commons governance joins archetype 1, narrow single-mechanism systems, as its fifth member after Georgism, "
      "Mutual Credit / LETS, Sovereign Wealth Fund Statism and Islamic finance.")
fails_all_three = sorted(k for k in N if all(V(k)[c] == 0.0 for c in ("C1.4", "C2.2", "C4.2")))
c14_by_reading = [moved(f_, IF_READING_A)["C1.4"], f_["C1.4"], moved(f_, IF_READING_C)["C1.4"]]
claim(g, "IF", "C2.2 and C4.2 undisputed; C1.4 fails on Readings B and C; the only archetype-1 entry failing all three",
      undisputed("IF") == ["C2.2", "C4.2"] and c14_by_reading == [0.5, 0.0, 0.0]
      and [k for k in ARCHETYPE_1 if k in fails_all_three] == ["IF"]
      and fails_all_three == sorted(["IF", "LM", "SC", "SQ"]),
      "It has no unconditional provision (C2.2) and no absolute-reduction ecological constraint (C4.2), the two "
      "failures that survive every contestable call, and on every joint reading but Reading A it has no answer to "
      "automation (C1.4). No other narrow single-mechanism entry in this corpus fails all three.",
      f"fails all three: {fails_all_three}")

# ---- [E] Ostrom-style commons governance
o = V("OS")
g = "E"
below_all = [c for c in CRITS if all(o[c] < V(k)[c] for k in N if k != "OS")]
claim(g, "OS", "C3.2 is the one criterion below every other system; all 22 others reach 0.5",
      below_all == ["C3.2"] and all(V(k)["C3.2"] >= 0.5 for k in N if k != "OS"),
      "is the one criterion on which it scores below every other system in the corpus, all 22 of which reach at "
      "least 0.5")
c55_top = sorted(k for k in N if V(k)["C5.5"] == 1.0)
claim(g, "OS", "C5.5 is the one criterion above CCO-PTF-CIP-SZH; the 1.0 is joint-best with PE, MC and IF",
      higher_lower(o, cco)[0] == ["C5.5"] and c55_top == sorted(["OS", "PE", "MC", "IF"]),
      "the one criterion on which this entry scores above CCO-PTF-CIP-SZH. The 1.0 is joint-best, shared with "
      "Participatory Economics, Mutual Credit / LETS and Islamic finance.", f"C5.5 at 1.0: {c55_top}")
tie14 = keys_at_total(total(o), ("OS",))
claim(g, "OS", "three-way tie at 14.0 with SWF Statism and Singapore: 4, 3 and 4 failures, one tier",
      tie14 == ["SG", "SWF"] and [nfail(V(k)) for k in ("OS", "SWF", "SG")] == [4, 3, 4]
      and len({canon.tier(nfail(V(k))) for k in ("OS", "SWF", "SG")}) == 1,
      "Ostrom-style commons governance, Sovereign Wealth Fund Statism and State Capitalism / Singapore all score "
      "exactly 14.0/26 (53.8%), with 4, 3 and 4 structural failures respectively.", f"at 14.0: {tie14}")
claim(g, "OS", "the three-way tie at 13.5 is Georgism, UBS and Islamic finance",
      keys_at_total(13.5) == sorted(["GEO", "UBS", "IF"]),
      "Unlike the three-way tie at 13.5 (Georgism / Land Value Tax, Universal Basic Services and Islamic finance), "
      "all three sit in the same adequacy tier")
hi_sw, lo_sw = higher_lower(o, swf)
claim(g, "OS", "vs SWF Statism: 8 differ, 4 higher, 4 lower, net zero",
      hamming(o, swf) == 8 and len(hi_sw) == 4 and len(lo_sw) == 4 and abs(total(o) - total(swf)) < 1e-9,
      "differs on 8 of 26 criteria, is higher on 4 and lower on 4, and nets exactly zero")
claim(g, "OS", "14 ordered strict-dominance pairs, none involving this entry",
      len(ALL_PAIRS) == 14 and not [p for p in ALL_PAIRS if "OS" in p],
      "The corpus contains 14 ordered strict-dominance pairs, and none involves this entry.")
claim(g, "OS", "C5.5 (1.0 against 0.5) is the single criterion above CCO-PTF-CIP-SZH",
      higher_lower(o, cco)[0] == ["C5.5"] and (o["C5.5"], cco["C5.5"]) == (1.0, 0.5),
      "The single criterion on which it exceeds CCO-PTF-CIP-SZH is C5.5, cultural adaptability, where it scores 1.0 "
      "against 0.5")
cco_half = [c for c in CRITS if cco[c] == 0.5]
escape = {b: [c for c in CRITS if V(b)[c] > cco[c]] for b in not_dom_by_cco}
claim(g, "OS", "CCO-PTF-CIP-SZH: 1.0 on 23 criteria, 0.5 on C1.5, C4.5, C5.5; eleven escape, four through C5.5",
      sum(1 for c in CRITS if cco[c] == 1.0) == 23 and cco_half == ["C1.5", "C4.5", "C5.5"]
      and len(escape) == 11 and all(len(v) == 1 and v[0] in cco_half for v in escape.values())
      and sorted(b for b, v in escape.items() if v == ["C5.5"]) == sorted(["OS", "IF", "PE", "MC"]),
      "CCO-PTF-CIP-SZH scores 1.0 on 23 criteria and 0.5 on C1.5, C4.5 and C5.5, so any system that scores 1.0 on "
      "one of those three escapes its dominance. Eleven systems do, four of them through C5.5: this entry, Islamic "
      "finance, Participatory Economics and Mutual Credit / LETS.")
step1b_dominators = {a: sorted(b for x, b in ALL_PAIRS if x == a) for a in STEP1B
                     if any(x == a for x, _ in ALL_PAIRS)}
claim(g, "OS", "dominates nothing; the Step 1b dominators are Singapore (China, Qatar) and IF (Stakeholder)",
      not [b for a, b in ALL_PAIRS if a == "OS"]
      and step1b_dominators == {"SG": ["CN", "QA"], "IF": ["SC"]} and step1b_over_legacy == [("IF", "SC")],
      "the two Step 1b entries that do: State Capitalism / Singapore, which dominates China and Qatar, and Islamic "
      "finance, which dominates Stakeholder Capitalism — the only Step 1b entry that dominates one of the 13 legacy "
      "systems.", f"got {step1b_dominators}")
d5 = {k: dsum(V(k), "D5") for k in N}
claim(g, "OS", "Domain 5 (4.0) beaten only by CCO and IF (4.5), tied with MC, NSD, SQ: joint third",
      abs(d5["OS"] - 4.0) < 1e-9 and sorted(k for k in N if d5[k] > 4.0) == ["CCO", "IF"]
      and all(abs(d5[k] - 4.5) < 1e-9 for k in ("CCO", "IF"))
      and sorted(k for k in N if k != "OS" and abs(d5[k] - 4.0) < 1e-9) == sorted(["MC", "NSD", "SQ"]),
      "Joint-best cultural adaptability; joint third-best implementation viability. Domain 5 scores 4.0/5, beaten "
      "only by CCO-PTF-CIP-SZH and Islamic finance (4.5 each) and tied with Mutual Credit / LETS, Nordic Social "
      "Democracy and Status Quo Market Capitalism.")
claim(g, "OS", "Domain 1 (2.0) beaten by 14 of the other 22",
      abs(dsum(o, "D1") - 2.0) < 1e-9 and sum(1 for k in N if dsum(V(k), "D1") > 2.0) == 14,
      "Domain 1 scores 2.0/6, beaten by 14 of the other 22 systems.")
split51 = {k: d5[k] - dsum(V(k), "D1") for k in N}
wider51 = sorted(k for k in N if split51[k] > split51["OS"] + 1e-9)
level51 = sorted(k for k in N if k != "OS" and abs(split51[k] - split51["OS"]) < 1e-9)
claim(g, "OS", "viability-minus-material-security split 2.0: joint third-widest behind LM 3.0 and IF 2.5",
      abs(split51["OS"] - 2.0) < 1e-9 and wider51 == ["IF", "LM"]
      and (split51["LM"], split51["IF"]) == (3.0, 2.5) and level51 == sorted(["DE", "MC", "SQ", "UBS"]),
      "split of 2.0 is joint third-widest in the corpus, behind Libertarian Minarchism's 3.0 and Islamic finance's "
      "2.5, level with Doughnut Economics, Mutual Credit / LETS, Status Quo Market Capitalism and Universal Basic "
      "Services.", f"wider {wider51}, level {level51}")
hi_q, lo_q = higher_lower(o, V("SQ"))
claim(g, "OS", "vs Status Quo: 15 differ, 11 higher, 4 lower, +3.5",
      hamming(o, V("SQ")) == 15 and len(hi_q) == 11 and len(lo_q) == 4 and abs(total(o) - total(V("SQ")) - 3.5) < 1e-9,
      "it differs on 15 criteria, is higher on 11 and lower on 4, and gains 3.5 points")
dist = {k: hamming(o, V(k)) for k in N if k != "OS"}
nearest = sorted(k for k, d in dist.items() if d == min(dist.values()))
hi_g, lo_g = higher_lower(o, V("GEO"))
claim(g, "OS", "nearest neighbours at 5 criteria: Georgism, Mutual Credit / LETS, UBS",
      min(dist.values()) == 5 and nearest == sorted(["GEO", "MC", "UBS"]),
      "Georgism / Land Value Tax is one of the three systems closest to this entry, each differing from it on only 5 "
      "criteria (the others are Mutual Credit / LETS and Universal Basic Services).", f"nearest {nearest}")
claim(g, "OS", "vs Georgism: 3 higher, 2 lower, +0.5",
      len(hi_g) == 3 and len(lo_g) == 2 and abs(total(o) - total(V("GEO")) - 0.5) < 1e-9,
      "Against Georgism it is higher on 3 and lower on 2, and gains 0.5")

# ---- [F] flag counts and tier robustness
g = "F"
HEAD_FLAG = re.compile(r"^#{3,4} C[1-5]\.[1-6][ab]?\b.*flagged as contestable", re.M)
heads = {k: len(HEAD_FLAG.findall(read(f))) for k, f in REGISTER_DOC.items()}
for k in ("CN", "SG", "QA", "IF", "OS"):
    check(g, f"{N[k]}: {heads[k]} headings flagged as contestable = {len(FLAGS[k])} calls in its register",
          heads[k] == len(FLAGS[k]))
VOCAB = re.compile(r"contestable|close call|flagged", re.I)


def flagged_sections(filename):
    return sum(1 for body in sections(read(filename)).values() if VOCAB.search(body))


bound = {k: flagged_sections(f) for k, f in OLDER_STEP1B_DOC.items()}
legacy_bound = sum(len(re.findall(r"contestable", read(f), re.I)) for f in LEGACY_DOCS)
check(g, "older Step 1b entries: criterion sections using flag vocabulary bound their flags at "
         + ", ".join(f"{k} {v}" for k, v in bound.items()), max(bound.values()) <= 5)
check(g, f"legacy entries: 'contestable' occurs {legacy_bound} times in their documents of record, "
         f"so no legacy entry has more than {legacy_bound} flagged calls", legacy_bound == 10)
count = {k: len(FLAGS[k]) for k in ("CN", "SG", "QA", "IF", "OS")}
others_max = max([count[k] for k in ("CN", "SG", "QA")] + list(bound.values()) + [legacy_bound])
claim(g, "OS", "twenty flags: the largest flagged set in the corpus, exceeding Islamic finance's sixteen",
      count["OS"] == 20 and count["IF"] == 16 and others_max < 16,
      "Twenty of twenty-six criteria are flagged — the largest flagged set in the corpus, exceeding Islamic "
      "finance's sixteen.")
claim(g, "IF", "sixteen flags: the second-largest set, after Ostrom's twenty",
      count["OS"] > count["IF"] > others_max,
      "This evaluation carries 16 flagged contestable calls, the second-largest set of any entry in the corpus, "
      "after Ostrom-style commons governance's twenty.")
spans = {k: span(k) for k in ("CN", "SG", "QA", "IF", "OS")}
span_bounds = [(0.5 * n, n) for n in list(bound.values()) + [legacy_bound]]  # each flag moves 0.5 and <= 1 failure
others = [spans[k] for k in ("CN", "SG", "QA", "IF")] + span_bounds
three_tiers = {k: canon.tier(nfail(extreme(k, True))) == "Potentially Adequate"
               and canon.tier(nfail(extreme(k, False))) == "Structurally Inadequate" for k in ("SG", "IF", "OS")}
claim(g, "IF", "enumeration span 8.0 points / 10 failures: between Singapore (6.0 / 6) and Ostrom (10.0 / 11)",
      spans["IF"] == (8.0, 10) and spans["SG"] == (6.0, 6) and spans["OS"] == (10.0, 11)
      and (count["SG"], count["OS"]) == (12, 20) and all(three_tiers.values()) and undisputed("OS") == [],
      "Measured by the span of the enumeration, 8.0 points and 10 structural failures, this entry is less "
      "tier-robust than State Capitalism / Singapore (6.0 points and 6 failures, from twelve flags) and more "
      "tier-robust than Ostrom-style commons governance (10.0 points and 11 failures, from twenty flags, with no "
      "structural failure undisputed).", f"spans {spans}")
claim(g, "OS", "enumeration span 10.0 / 11 exceeds every other entry's; none undisputed against IF's two",
      spans["OS"] == (10.0, 11) and spans["IF"] == (8.0, 10)
      and all(p < 10.0 and f < 11 for p, f in others)
      and undisputed("OS") == [] and len(undisputed("IF")) == 2,
      "This entry therefore replaces Islamic finance as the least tier-robust in the corpus, measured by the span "
      "of the enumeration: 10.0 points and 11 structural failures, against Islamic finance's 8.0 and 10, with no "
      "failure undisputed where Islamic finance has two.")
claim(g, "OS", "the final assessment restates it: all three tiers reachable, no undisputed failure",
      three_tiers["OS"] and undisputed("OS") == [] and all(p < 10.0 for p, _ in others),
      "this is now the least tier-robust entry in the corpus, with all three tiers reachable and no undisputed "
      "failure")

# ---- [G] superseded wording is gone
g = "G"
SUPERSEDED = [
    # (doc, registered claim, old wording that must be absent, new wording that must be present)
    ("QA", "rank 20th of 21", "rank 20th of 21", "Qatar ranks 22nd of 23"),
    ("QA", "dominance pairs 11 -> 13", "from 11 to 13 ordered pairs", "The corpus holds 14 ordered strict-dominance pairs"),
    ("QA", "two pairs not involving CCO-PTF-CIP-SZH", "the only two that would not involve CCO-PTF-CIP-SZH",
     "Three do not involve CCO-PTF-CIP-SZH"),
    ("QA", "joint upward 14.0 is SWF Statism's and Singapore's",
     "as Sovereign Wealth Fund Statism and Singapore, in a different tier",
     "as Sovereign Wealth Fund Statism, Singapore, and Ostrom-style commons governance, in a different tier"),
    ("IF", "rank 12 (competition rank)", "| 12 | Islamic Finance / Profit-Sharing Banking",
     "| 13 | Islamic Finance / Profit-Sharing Banking |"),
    ("IF", "Domain 4 fifth-lowest", "the fifth-lowest ethics score of the twenty-one systems",
     "the Domain 4 score is the sixth-lowest of the twenty-three systems"),
    ("IF", "dominance pairs 11 -> 12", "from 11 to 12", "The corpus holds 14 ordered strict-dominance pairs in all"),
    ("OS", "exactly one system beats Domain 5", "beaten only by CCO-PTF-CIP-SZH and tied with",
     "beaten only by CCO-PTF-CIP-SZH and Islamic finance (4.5 each)"),
    ("OS", "that system is CCO-PTF-CIP-SZH", "beaten only by CCO-PTF-CIP-SZH and tied with",
     "beaten only by CCO-PTF-CIP-SZH and Islamic finance (4.5 each)"),
]
for doc, label, old, new in SUPERSEDED:
    check(g, f"{doc}: Session 25 register, '{label}': old wording absent, restated wording present",
          norm(old) not in TEXT[doc] and norm(new) in TEXT[doc])
STALE = {
    "QA": ["prospective", "21-system", "Not yet added", "is not added to `neec_scores.csv`",
           "of the eight Step 1b systems", "The next Step 1b system", "queued for the second consolidated"],
    "IF": ["21-system", "twenty-one", "Not yet added", "the largest set of any entry", "Against its archetype siblings", "least tier-robust in the corpus to date",
           "most discriminating criterion", "The widest viability-versus-ethics split", "scratch score awaiting",
           "same failures every narrow single-mechanism entry", "Ostrom-style commons governance remains",
           "with 2, 3, and 5 structural failures", "<-- new", "from a smaller flag set"],
    "OS": ["20-system", "21-system", "Not yet inserted", "Not yet added", "beats every other system",
           "Best-in-corpus cultural adaptability", "beaten by 13 of", "second widest in the corpus",
           "the only Step 1b entry so far", "adds none", "nearest mechanism-level neighbour", "Recommendation for the",
           "by a wide margin", "Islamic finance's 5.0 and 9", "with 3, 4 and 4 structural failures",
           "that Session 22 found", "exceptionally well travelled", "[pending insertion]", "Step 1b closes"],
}
for doc, phrases in STALE.items():
    found = [p for p in phrases if norm(p) in TEXT[doc]]
    check(g, f"{doc}: none of {len(phrases)} superseded or stale phrases remains", not found,
          f"still present: {found}")

# ---- [H] the two corpus tables
IF_BEGIN, IF_END = "<!-- GENERATED:corpus -->\n", "\n<!-- END GENERATED:corpus -->"
OS_BEGIN, OS_END = "<!-- BEGIN GENERATED: corpus-table -->\n", "\n<!-- END GENERATED: corpus-table -->"


def tier_of(k):
    return canon.tier(nfail(V(k)))


def ordered():
    return sorted(N, key=lambda k: (-total(V(k)), N[k]))


def render_if():
    """Islamic finance's layout: repeated competition-rank numbers; this entry in bold."""
    out = ["| Rank | System | Score /26 | % | Failures | Tier |", "|---|---|---|---|---|---|"]
    for k in ordered():
        t = total(V(k))
        label = f"**{N[k]}**" if k == "IF" else N[k]
        out.append(f"| {rank(k)} | {label} | {t:.1f} | {100.0 * t / 26.0:.1f} | {nfail(V(k))} | {tier_of(k)} |")
    return "\n".join(out)


def render_os():
    """Ostrom's layout: '=' marks a shared competition rank; this entry in bold."""
    out = ["| Rank | System | Score /26 | % | Failures | Tier |", "|---|---|---|---|---|---|"]
    for k in ordered():
        t = total(V(k))
        shared = len(keys_at_total(t)) > 1
        label = f"**{N[k]}**" if k == "OS" else N[k]
        out.append(f"| {rank(k)}{'=' if shared else ''} | {label} | {t:.1f} | {100.0 * t / 26.0:.1f} | "
                   f"{nfail(V(k))} | {tier_of(k)} |")
    return "\n".join(out)


TABLES = (("IF", IF_BEGIN, IF_END, render_if), ("OS", OS_BEGIN, OS_END, render_os))


def between(text, begin, end):
    if text.count(begin) != 1 or text.count(end) != 1:
        return None
    a = text.index(begin) + len(begin)
    return text[a:text.index(end)]


if "--fill" in sys.argv[1:]:
    for doc, begin, end, render in TABLES:
        body = between(RAW[doc], begin, end)
        if body is None:
            sys.exit(f"ERROR: {DOC_FILE[doc]}: table markers missing or repeated; nothing written")
        new = RAW[doc].replace(begin + body + end, begin + render() + end, 1)
        with open(locate(DOC_FILE[doc]), "w", encoding="utf-8") as f:
            f.write(new)
        print(f"filled the corpus table in {DOC_FILE[doc]}")
    sys.exit(0)

for doc, begin, end, render in TABLES:
    body = between(RAW[doc], begin, end)
    check("H", f"{doc}: corpus table has one pair of markers", body is not None)
    check("H", f"{doc}: corpus table is byte-identical to a fresh render (23 rows)",
          body == render() and len(render().splitlines()) == 25, "regenerate with --fill")

# ------------------------------------------------------------------ report
GROUPS = {
    "A": "SOURCES AND IDENTITIES",
    "B": "CRITERION-LEVEL REFERENCES TO OTHER SYSTEMS",
    "C": "STATE CAPITALISM / QATAR: CORPUS POSITION AND PAIRWISE COMPARISONS",
    "D": "ISLAMIC FINANCE: CORPUS POSITION AND PAIRWISE COMPARISONS",
    "E": "OSTROM-STYLE COMMONS GOVERNANCE: CORPUS POSITION AND PAIRWISE COMPARISONS",
    "F": "FLAG COUNTS AND TIER ROBUSTNESS",
    "G": "SUPERSEDED WORDING IS GONE (THE SESSION 25 AUDIT REGISTER, RESOLVED)",
    "H": "CORPUS TABLES",
}
print("=" * 96)
print("verify_comparative_claims.py -- NEEC Session 26: comparative claims on the canonical 23-system corpus")
print("=" * 96)
print(f"canonical corpus: {CANON_FILE} ({len(SCORES)} systems); documents: "
      + ", ".join(DOC_FILE[k] for k in ("QA", "IF", "OS")))
for key, title in GROUPS.items():
    rows = [r for r in RESULTS if r[0] == key]
    print(f"\n[{key}] {title} ({len(rows)} checks)")
    for _g, label, ok, detail in rows:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok and detail:
            print(f"        {detail}")
npass = sum(1 for r in RESULTS if r[2])
print("\n" + "=" * 96)
print(f"SUMMARY: {npass} passed, {len(RESULTS) - npass} failed (of {len(RESULTS)}).")
print(f"Criterion-level references checked: {len(REFS)} score references and {len(FLAG_REFS)} flag references.")
print("=" * 96)
sys.exit(0 if npass == len(RESULTS) else 1)
