#!/usr/bin/env python3
"""
verify_ostrom.py — NEEC Session 23 verifier for the Step 1b evaluation of
Ostrom-style commons governance.

Generalises verify_islamicfinance.py (Session 22), which generalised
verify_qatar.py (Session 21). Eight check groups:

  [A] sources and corpus integrity
  [B] self-consistency of the scored vector
  [C] transcription against NEEC_Ostrom_Commons_scoring_scratch.md
      (symmetric: flagged headings must say "contestable", unflagged must not;
       and every flagged criterion must state its alternative inline)
  [D] exhaustive sensitivity over the flagged set, plus three coherent
      joint readings (the D6 proposal, applied)
  [E] the scope scenario (knowledge / digital commons counted in)
  [F] corpus comparison: ties, dominance, ranks, archetype facts
  [G] rebuilt numeric claims used in the prose
  [H] byte-equality of the generated blocks in the document

Modes:
  (no args)  run every check and print PASS/FAIL per check
  --facts    print every computed comparative fact, for writing prose FROM
  --fill     render the two generated blocks for pasting into the document

Deterministic: no dict-ordering dependence, no randomness, no clock.
"""

import sys
import os
import importlib.util
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = "NEEC_Ostrom_Commons_scoring_scratch.md"
SYSTEM = "Ostrom-Style Commons Governance"

# --------------------------------------------------------------------------
# The scored vector. Session 23, Step 1b.
# --------------------------------------------------------------------------

OSTROM = {
    "C1.1": 0.5, "C1.2a": 0.0, "C1.2b": 0.5, "C1.3": 0.5, "C1.4": 0.5, "C1.5": 0.0,
    "C2.1": 0.5, "C2.2": 0.0, "C2.3": 0.5, "C2.4": 0.5, "C2.5": 1.0,
    "C3.1": 0.5, "C3.2": 0.0, "C3.3": 0.5, "C3.4": 1.0, "C3.5": 0.5,
    "C4.1": 1.0, "C4.2": 0.5, "C4.3": 0.5, "C4.4": 0.5, "C4.5": 0.5,
    "C5.1": 1.0, "C5.2": 0.5, "C5.3": 1.0, "C5.4": 0.5, "C5.5": 1.0,
}

# Flagged contestable calls: criterion -> alternative score.
# One alternative per flag, as in Session 22.
FLAGS = {
    "C1.1": 0.0, "C1.2a": 0.5, "C1.2b": 1.0, "C1.3": 0.0, "C1.4": 0.0, "C1.5": 0.5,
    "C2.2": 0.5, "C2.4": 1.0, "C2.5": 0.5,
    "C3.1": 1.0, "C3.2": 0.5, "C3.3": 1.0, "C3.5": 1.0,
    "C4.1": 0.5, "C4.2": 1.0, "C4.3": 0.0, "C4.4": 0.0, "C4.5": 0.0,
    "C5.2": 0.0, "C5.4": 1.0,
}

# Scope scenario: the knowledge / digital commons extension counted IN.
SCENARIO = {"C1.5": 0.5, "C2.3": 1.0}

CRIT_NAMES = {
    "C1.1": "Poverty Elimination Capacity",
    "C1.2a": "Wealth Building for Resilience",
    "C1.2b": "Prevention of Exploitative Accumulation",
    "C1.3": "Housing Security",
    "C1.4": "Automation Resilience",
    "C1.5": "Universal Wealth Access",
    "C2.1": "Freedom from Coercion",
    "C2.2": "Labor Non-Necessity",
    "C2.3": "Creative Development Opportunities",
    "C2.4": "Democratic Participation",
    "C2.5": "Exit Rights and Mobility",
    "C3.1": "Crisis Response Capacity",
    "C3.2": "Inflation Control Mechanisms",
    "C3.3": "Multi-Failure Resistance",
    "C3.4": "Epistemic Adaptability",
    "C3.5": "Failure-Mode Transparency",
    "C4.1": "Intergenerational Justice",
    "C4.2": "Ecological Compliance",
    "C4.3": "Racial and Gender Equity",
    "C4.4": "Power Distribution",
    "C4.5": "Exploitation Elimination",
    "C5.1": "Proven Component Foundation",
    "C5.2": "Staged Transition Pathways",
    "C5.3": "Partial and Parallel Deployability",
    "C5.4": "Political Coalition Potential",
    "C5.5": "Cultural Adaptability",
}

DOMAINS = {
    "Material Security":       ["C1.1", "C1.2a", "C1.2b", "C1.3", "C1.4", "C1.5"],
    "Human Autonomy":          ["C2.1", "C2.2", "C2.3", "C2.4", "C2.5"],
    "System Resilience":       ["C3.1", "C3.2", "C3.3", "C3.4", "C3.5"],
    "Ethical Integrity":       ["C4.1", "C4.2", "C4.3", "C4.4", "C4.5"],
    "Implementation Viability": ["C5.1", "C5.2", "C5.3", "C5.4", "C5.5"],
}

# Sources the document must cite, with the claim each one carries.
REQUIRED_SOURCES = [
    ("Governing the Commons", "Ostrom 1990, the founding statement"),
    ("Cox", "Cox, Arnold & Villamayor-Tomas 2010, 91 studies"),
    ("Hilborn", "Gutierrez, Hilborn & Defeo 2011, 130 co-managed fisheries"),
    ("Chhatre", "Chhatre & Agrawal 2009, 80 forest commons in 10 countries"),
    ("Agarwal", "Bina Agarwal, participatory exclusions"),
    ("Rights and Resources", "RRI, 2.5 billion people / recognition gap"),
    ("Tribunal de las Aguas", "Valencia, millennium-scale longevity"),
    ("polycentric", "Ostrom's own scale statement"),
    ("Gibson", "Agrawal and Gibson, the community-homogeneity critique"),
    ("Hess", "Hess & Ostrom, knowledge commons scope boundary"),
]

# Numeric claims rebuilt independently by group [G]: (label, computed, stated)
# 'stated' values are what the prose says; 'computed' is derived here.

# --------------------------------------------------------------------------
# Corpus loading
# --------------------------------------------------------------------------


def load_corpus():
    path = os.path.join(HERE, "neec_weighting_robustness_analysis_v2.py")
    if not os.path.exists(path):
        path = "/mnt/project/neec_weighting_robustness_analysis_v2.py"
    spec = importlib.util.spec_from_file_location("neec_canon", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CANON = load_corpus()
ALL_CRITS = list(CANON.ALL_CRITS)
CORPUS = dict(CANON.SCORES)


def total(vec):
    return sum(vec[c] for c in ALL_CRITS)


def fails(vec):
    return sum(1 for c in ALL_CRITS if vec[c] == 0.0)


def tier(n):
    return CANON.tier(n)


def pct(vec):
    return 100.0 * total(vec) / 26.0


def domain_scores(vec):
    return {d: sum(vec[c] for c in cs) for d, cs in DOMAINS.items()}


def dominates(a, b):
    """a strictly dominates b: >= everywhere, > somewhere."""
    ge = all(a[c] >= b[c] for c in ALL_CRITS)
    gt = any(a[c] > b[c] for c in ALL_CRITS)
    return ge and gt


# --------------------------------------------------------------------------
# Joint readings (the D6 proposal, applied)
# --------------------------------------------------------------------------

UP_FLAGS = sorted([c for c, alt in FLAGS.items() if alt > OSTROM[c]])
DOWN_FLAGS = sorted([c for c, alt in FLAGS.items() if alt < OSTROM[c]])


def reading_a():
    """The long-enduring-case reading: judged on the resource it governs,
    in the cases where the design principles hold."""
    v = dict(OSTROM)
    for c in UP_FLAGS:
        v[c] = FLAGS[c]
    return v


def reading_c():
    """Strict population scope: every criterion read at full population scale."""
    v = dict(OSTROM)
    for c in DOWN_FLAGS:
        v[c] = FLAGS[c]
    return v


def scenario_vec():
    v = dict(OSTROM)
    v.update(SCENARIO)
    return v


# --------------------------------------------------------------------------
# Exhaustive sensitivity
# --------------------------------------------------------------------------


def enumerate_sensitivity():
    """Every combination of the flagged calls resolved either way.
    Returns (n_combos, min_total, max_total, tiers_reached, tier_counts,
             min_fails, max_fails)."""
    flagged = sorted(FLAGS.keys())
    base = total(OSTROM)
    base_f = fails(OSTROM)
    deltas = []
    for c in flagged:
        d_total = FLAGS[c] - OSTROM[c]
        d_fail = (1 if FLAGS[c] == 0.0 else 0) - (1 if OSTROM[c] == 0.0 else 0)
        deltas.append((d_total, d_fail))

    tier_counts = {"Potentially Adequate": 0,
                   "Partially Adequate": 0,
                   "Structurally Inadequate": 0}
    min_t = max_t = base
    min_f = max_f = base_f
    n = 0
    for combo in product((0, 1), repeat=len(flagged)):
        t = base
        f = base_f
        for pick, (dt, df) in zip(combo, deltas):
            if pick:
                t += dt
                f += df
        tier_counts[tier(f)] += 1
        if t < min_t:
            min_t = t
        if t > max_t:
            max_t = t
        if f < min_f:
            min_f = f
        if f > max_f:
            max_f = f
        n += 1
    reached = sorted(k for k, v in tier_counts.items() if v > 0)
    return n, min_t, max_t, reached, tier_counts, min_f, max_f


def undisputed_failures():
    """Failures no flag can remove."""
    return sorted(c for c in ALL_CRITS
                  if OSTROM[c] == 0.0 and FLAGS.get(c, 0.0) == 0.0)


# --------------------------------------------------------------------------
# Corpus comparison
# --------------------------------------------------------------------------


def ranked_corpus(include_ostrom=True):
    rows = []
    for s, v in CORPUS.items():
        rows.append((s, total(v), fails(v)))
    if include_ostrom:
        rows.append((SYSTEM, total(OSTROM), fails(OSTROM)))
    rows.sort(key=lambda r: (-r[1], r[0]))
    out = []
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][1] == rows[i][1]:
            j += 1
        rank = i + 1
        tied = (j > i)
        for k in range(i, j + 1):
            s, t, f = rows[k]
            out.append((f"{rank}=" if tied else str(rank), s, t,
                        100.0 * t / 26.0, f, tier(f)))
        i = j + 1
    return out


def exact_ties():
    t = total(OSTROM)
    return sorted(s for s, v in CORPUS.items() if total(v) == t)


def dominance_facts():
    dominated_by = sorted(s for s, v in CORPUS.items() if dominates(v, OSTROM))
    dominates_these = sorted(s for s, v in CORPUS.items() if dominates(OSTROM, v))
    return dominated_by, dominates_these


def corpus_dominance_pairs(extra=None):
    """Count ordered strictly-dominating pairs in the corpus (optionally
    with an extra system inserted)."""
    sc = dict(CORPUS)
    if extra:
        sc[SYSTEM] = OSTROM
    names = sorted(sc.keys())
    n = 0
    for a in names:
        for b in names:
            if a != b and dominates(sc[a], sc[b]):
                n += 1
    return n


def differs_from(other):
    """(n_differ, n_higher, n_lower, point_gain) against a corpus system."""
    v = CORPUS[other]
    d = h = l = 0
    for c in ALL_CRITS:
        if OSTROM[c] != v[c]:
            d += 1
            if OSTROM[c] > v[c]:
                h += 1
            else:
                l += 1
    return d, h, l, total(OSTROM) - total(v)


def domain_rank(domain, include_ostrom=True):
    """Rank of Ostrom's score in a domain across the corpus (1 = highest),
    plus the number of systems that beat it."""
    cs = DOMAINS[domain]
    mine = sum(OSTROM[c] for c in cs)
    vals = [(s, sum(v[c] for c in cs)) for s, v in CORPUS.items()]
    better = sorted(s for s, x in vals if x > mine)
    equal = sorted(s for s, x in vals if x == mine)
    return mine, better, equal


# --------------------------------------------------------------------------
# Generated blocks
# --------------------------------------------------------------------------

BEGIN_SUMMARY = "<!-- BEGIN GENERATED: summary-table -->"
END_SUMMARY = "<!-- END GENERATED: summary-table -->"
BEGIN_CORPUS = "<!-- BEGIN GENERATED: corpus-table -->"
END_CORPUS = "<!-- END GENERATED: corpus-table -->"


def render_summary_table():
    lines = []
    lines.append("| Criterion | Name | Score | Result |")
    lines.append("|---|---|---|---|")
    for c in ALL_CRITS:
        v = OSTROM[c]
        result = {0.0: "Structural Failure", 0.5: "Partial", 1.0: "Pass"}[v]
        name = CRIT_NAMES[c]
        if c == "C1.5":
            name += " (narrowed)"
        if c in FLAGS:
            name += " *(flagged)*"
        lines.append(f"| {c} | {name} | {v:.1f} | {result} |")
    ds = domain_scores(OSTROM)
    lines.append("")
    lines.append("| Domain | Score | Max |")
    lines.append("|---|---|---|")
    for d, cs in DOMAINS.items():
        lines.append(f"| {d} | {ds[d]:.1f} | {len(cs)}.0 |")
    lines.append(f"| **Total** | **{total(OSTROM):.1f}** | **26.0** |")
    lines.append("")
    lines.append(f"**Total: {total(OSTROM):.1f}/26 ({pct(OSTROM):.1f}%). "
                 f"Structural failures: {fails(OSTROM)} "
                 f"({', '.join(c for c in ALL_CRITS if OSTROM[c] == 0.0)}). "
                 f"Tier: {tier(fails(OSTROM))}.**")
    return "\n".join(lines)


def render_corpus_table():
    lines = []
    lines.append("| Rank | System | Score /26 | % | Failures | Tier |")
    lines.append("|---|---|---|---|---|---|")
    for rank, s, t, p, f, tr in ranked_corpus():
        label = f"**{s}** [pending insertion]" if s == SYSTEM else s
        lines.append(f"| {rank} | {label} | {t:.1f} | {p:.1f} | {f} | {tr} |")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# --facts
# --------------------------------------------------------------------------


def print_facts():
    print("=" * 78)
    print("COMPUTED FACTS — write the prose FROM these, do not check prose against them")
    print("=" * 78)
    print()
    ds = domain_scores(OSTROM)
    print(f"Total          : {total(OSTROM):.1f}/26  ({pct(OSTROM):.1f}%)")
    print(f"Failures       : {fails(OSTROM)}  -> "
          f"{', '.join(c for c in ALL_CRITS if OSTROM[c] == 0.0)}")
    print(f"Tier           : {tier(fails(OSTROM))}")
    print("Domains        : " + " / ".join(f"{ds[d]:.1f}" for d in DOMAINS))
    print(f"Passes (1.0)   : {', '.join(c for c in ALL_CRITS if OSTROM[c] == 1.0)}"
          f"  (n={sum(1 for c in ALL_CRITS if OSTROM[c] == 1.0)})")
    print(f"Partials (0.5) : n={sum(1 for c in ALL_CRITS if OSTROM[c] == 0.5)}")
    print()
    print(f"Flagged calls  : {len(FLAGS)}  "
          f"(upward {len(UP_FLAGS)}, downward {len(DOWN_FLAGS)})")
    print(f"  upward       : {', '.join(UP_FLAGS)}")
    print(f"  downward     : {', '.join(DOWN_FLAGS)}")
    print(f"Undisputed failures (no flag can remove): "
          f"{undisputed_failures() or 'NONE'}")
    print()
    n, mn, mx, reached, tc, mnf, mxf = enumerate_sensitivity()
    print(f"Exhaustive enumeration: {n:,} combinations ("
          f"2^{len(FLAGS)})")
    print(f"  total range  : {mn:.1f} to {mx:.1f}")
    print(f"  failure range: {mnf} to {mxf}")
    print(f"  tiers reached: {', '.join(reached)}")
    for k in ("Potentially Adequate", "Partially Adequate", "Structurally Inadequate"):
        print(f"    {k:26} {tc[k]:>9,}  ({100.0*tc[k]/n:5.1f}%)")
    print()
    print("Joint readings:")
    for label, v in (("A - long-enduring case", reading_a()),
                     ("B - as scored", OSTROM),
                     ("C - strict population scope", reading_c())):
        print(f"  {label:28} {total(v):>5.1f}/26  {pct(v):5.1f}%  "
              f"{fails(v):>2} failures  {tier(fails(v))}")
    a, c = reading_a(), reading_c()
    print(f"  A-to-C spread: {total(a) - total(c):.1f} points, "
          f"{fails(c) - fails(a)} failures")
    print()
    sv = scenario_vec()
    print(f"Scope scenario (knowledge/digital commons counted in): "
          f"{total(sv):.1f}/26, {fails(sv)} failures, {tier(fails(sv))}  "
          f"[tier {'UNCHANGED' if tier(fails(sv)) == tier(fails(OSTROM)) else 'CHANGED'}]")
    print()
    ties = exact_ties()
    print(f"Exact score ties in corpus at {total(OSTROM):.1f}: {ties or 'NONE'}")
    for s in ties:
        print(f"    {s:34} {fails(CORPUS[s])} failures  {tier(fails(CORPUS[s]))}")
    print()
    db, dt = dominance_facts()
    print(f"Dominated by   : {db or 'NOTHING'}")
    print(f"Dominates      : {dt or 'NOTHING'}")
    print(f"Dominance pairs in corpus: before={corpus_dominance_pairs()}, "
          f"after insertion={corpus_dominance_pairs(extra=True)}")
    print()
    for other in ("Status Quo Market Capitalism", "Georgism / Land Value Tax",
                  "Sovereign Wealth Fund Statism", "Degrowth Economics",
                  "Doughnut Economics"):
        d, h, l, g = differs_from(other)
        print(f"  vs {other:32} differs on {d:>2}, higher on {h:>2}, "
              f"lower on {l:>2}, net {g:+.1f}")
    print()
    for d in DOMAINS:
        mine, better, equal = domain_rank(d)
        print(f"  Domain {d:26} {mine:.1f}  beaten by {len(better)}, "
              f"tied with {len(equal)}")
        if d == "Implementation Viability":
            print(f"      beaten by: {better or 'NOBODY'}")
            print(f"      tied with: {equal or 'NOBODY'}")
    print()
    print("Rank in a 21-system view (corpus of 20 + this entry):")
    for rank, s, t, p, f, tr in ranked_corpus():
        mark = "  <-- new" if s == SYSTEM else ""
        print(f"  {rank:>3}  {s:34} {t:>5.1f}  {p:5.1f}%  {f:>2}  {tr}{mark}")
    print()
    d5 = domain_scores(OSTROM)["Implementation Viability"]
    d4 = domain_scores(OSTROM)["Ethical Integrity"]
    d1 = domain_scores(OSTROM)["Material Security"]
    print(f"Viability-vs-material-security split: D5 {d5:.1f} vs D1 {d1:.1f} "
          f"= {d5 - d1:.1f}")
    splits = []
    for s, v in CORPUS.items():
        dv = domain_scores(v)
        splits.append((dv["Implementation Viability"] - dv["Material Security"], s))
    splits.sort(reverse=True)
    print(f"  widest such split in corpus: {splits[0][0]:.1f} ({splits[0][1]})")
    print(f"  this entry would rank: "
          f"{sum(1 for x, _ in splits if x > d5 - d1) + 1} of {len(splits) + 1}")
    print(f"D4 {d4:.1f}; systems with lower D4: "
          f"{sum(1 for _, v in CORPUS.items() if domain_scores(v)['Ethical Integrity'] < d4)}")
    print()
    print("=" * 78)


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

RESULTS = []


def check(label, cond, detail=""):
    RESULTS.append((label, bool(cond), detail))


def read_doc():
    p = os.path.join(HERE, DOC)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def group_a():
    check("[A1] canonical corpus loads with 20 systems", len(CORPUS) == 20,
          f"got {len(CORPUS)}")
    check("[A2] canonical criteria list has 26 entries", len(ALL_CRITS) == 26,
          f"got {len(ALL_CRITS)}")
    check("[A3] this entry is not already in the corpus", SYSTEM not in CORPUS)
    check("[A4] every criterion scored", set(OSTROM) == set(ALL_CRITS))
    check("[A5] every score in {0.0, 0.5, 1.0}",
          all(v in (0.0, 0.5, 1.0) for v in OSTROM.values()))
    check("[A6] every flag names a real criterion",
          all(c in ALL_CRITS for c in FLAGS))
    check("[A7] every flag's alternative differs from the scored value",
          all(FLAGS[c] != OSTROM[c] for c in FLAGS))
    check("[A8] every flag alternative in {0.0, 0.5, 1.0}",
          all(v in (0.0, 0.5, 1.0) for v in FLAGS.values()))
    check("[A9] scenario names real criteria",
          all(c in ALL_CRITS for c in SCENARIO))
    check("[A10] criterion-name table is complete",
          set(CRIT_NAMES) == set(ALL_CRITS))
    doc = read_doc()
    if doc is None:
        check("[A11] document present", False, f"{DOC} not found")
        for key, why in REQUIRED_SOURCES:
            check(f"[A-src] cites {key} ({why})", False, "no document")
        return
    check("[A11] document present", True)
    for key, why in REQUIRED_SOURCES:
        check(f"[A-src] cites {key}", key.lower() in doc.lower(), why)


def group_b():
    ds = domain_scores(OSTROM)
    for d, cs in DOMAINS.items():
        check(f"[B] domain '{d}' sums to its criteria",
              abs(ds[d] - sum(OSTROM[c] for c in cs)) < 1e-9)
        check(f"[B] domain '{d}' within max", 0.0 <= ds[d] <= len(cs))
    check("[B] domains sum to the total",
          abs(sum(ds.values()) - total(OSTROM)) < 1e-9,
          f"{sum(ds.values())} vs {total(OSTROM)}")
    check("[B] total is 14.0", abs(total(OSTROM) - 14.0) < 1e-9,
          f"{total(OSTROM)}")
    check("[B] percentage is 53.8", abs(pct(OSTROM) - 53.8) < 0.05,
          f"{pct(OSTROM):.4f}")
    check("[B] failure count is 4", fails(OSTROM) == 4, f"{fails(OSTROM)}")
    check("[B] failures are C1.2a, C1.5, C2.2, C3.2",
          [c for c in ALL_CRITS if OSTROM[c] == 0.0] ==
          ["C1.2a", "C1.5", "C2.2", "C3.2"])
    check("[B] tier is Partially Adequate",
          tier(fails(OSTROM)) == "Partially Adequate")
    check("[B] six Passes at 1.0",
          sum(1 for c in ALL_CRITS if OSTROM[c] == 1.0) == 6,
          f"{sum(1 for c in ALL_CRITS if OSTROM[c] == 1.0)}")
    check("[B] sixteen Partials at 0.5",
          sum(1 for c in ALL_CRITS if OSTROM[c] == 0.5) == 16,
          f"{sum(1 for c in ALL_CRITS if OSTROM[c] == 0.5)}")
    check("[B] the Passes are C2.5, C3.4, C4.1, C5.1, C5.3, C5.5",
          [c for c in ALL_CRITS if OSTROM[c] == 1.0] ==
          ["C2.5", "C3.4", "C4.1", "C5.1", "C5.3", "C5.5"])
    check("[B] flagged set has 20 members", len(FLAGS) == 20, f"{len(FLAGS)}")
    check("[B] upward flags = 11", len(UP_FLAGS) == 11, f"{len(UP_FLAGS)}")
    check("[B] downward flags = 9", len(DOWN_FLAGS) == 9, f"{len(DOWN_FLAGS)}")
    check("[B] up and down flags partition the flagged set",
          sorted(UP_FLAGS + DOWN_FLAGS) == sorted(FLAGS))


def group_c():
    doc = read_doc()
    if doc is None:
        check("[C] transcription checks", False, "no document")
        return
    lines = doc.split("\n")
    heads = {}
    for ln in lines:
        if ln.startswith("#### C"):
            cid = ln.split()[1].rstrip(":")
            heads[cid] = ln
    check("[C] document has all 26 criterion headings",
          set(heads) == set(ALL_CRITS),
          f"missing {sorted(set(ALL_CRITS) - set(heads))}")
    for c in ALL_CRITS:
        if c not in heads:
            continue
        h = heads[c]
        # score transcribed correctly
        check(f"[C] {c} heading states {OSTROM[c]:.1f}",
              f": {OSTROM[c]:.1f} " in h or f": {OSTROM[c]:.1f}(" in h
              or h.rstrip().endswith(f": {OSTROM[c]:.1f}"), h)
        # symmetric flag check
        flagged_in_doc = "contestable" in h.lower()
        check(f"[C] {c} flag state matches ({'flagged' if c in FLAGS else 'unflagged'})",
              flagged_in_doc == (c in FLAGS), h)
    # per-criterion alternative stated inline
    sections = {}
    cur = None
    for ln in lines:
        if ln.startswith("#### C"):
            cur = ln.split()[1].rstrip(":")
            sections[cur] = []
        elif cur:
            sections[cur].append(ln)
    for c, alt in sorted(FLAGS.items()):
        body = "\n".join(sections.get(c, []))
        check(f"[C] {c} states its alternative ({alt:.1f}) inline",
              f"{alt:.1f}" in body, "alternative not found in section body")


def group_d():
    n, mn, mx, reached, tc, mnf, mxf = enumerate_sensitivity()
    check("[D] enumeration covers 2^20 combinations", n == 2 ** 20, f"{n}")
    check("[D] enumeration low bound is 9.5", abs(mn - 9.5) < 1e-9, f"{mn}")
    check("[D] enumeration high bound is 19.5", abs(mx - 19.5) < 1e-9, f"{mx}")
    check("[D] scored total lies inside the range", mn <= total(OSTROM) <= mx)
    check("[D] all three tiers are reachable", len(reached) == 3, f"{reached}")
    check("[D] tier counts sum to the enumeration", sum(tc.values()) == n)
    a, c = reading_a(), reading_c()
    check("[D] Reading A totals 19.5", abs(total(a) - 19.5) < 1e-9, f"{total(a)}")
    check("[D] Reading A has 0 failures", fails(a) == 0, f"{fails(a)}")
    check("[D] Reading A is Potentially Adequate",
          tier(fails(a)) == "Potentially Adequate")
    check("[D] Reading C totals 9.5", abs(total(c) - 9.5) < 1e-9, f"{total(c)}")
    check("[D] Reading C has 11 failures", fails(c) == 11, f"{fails(c)}")
    check("[D] Reading C is Structurally Inadequate",
          tier(fails(c)) == "Structurally Inadequate")
    check("[D] Reading B is the scored vector", total(OSTROM) == 14.0)
    check("[D] A and C are the enumeration's extremes",
          abs(total(a) - mx) < 1e-9 and abs(total(c) - mn) < 1e-9,
          "joint readings should bound the enumeration here")
    check("[D] A-to-C spread is 10.0 points",
          abs(total(a) - total(c) - 10.0) < 1e-9)
    check("[D] A-to-C spread is 11 failures", fails(c) - fails(a) == 11)
    check("[D] no failure is undisputed", undisputed_failures() == [],
          f"{undisputed_failures()}")


def group_e():
    sv = scenario_vec()
    check("[E] scenario total is 15.0", abs(total(sv) - 15.0) < 1e-9,
          f"{total(sv)}")
    check("[E] scenario has 3 failures", fails(sv) == 3, f"{fails(sv)}")
    check("[E] scenario tier is unchanged",
          tier(fails(sv)) == tier(fails(OSTROM)),
          f"{tier(fails(sv))} vs {tier(fails(OSTROM))}")
    check("[E] scenario changes exactly 2 criteria",
          sum(1 for c in ALL_CRITS if sv[c] != OSTROM[c]) == 2)


def group_f():
    ties = exact_ties()
    check("[F] exactly two corpus systems tie at 14.0", len(ties) == 2, f"{ties}")
    check("[F] the ties are SWF Statism and Singapore",
          ties == ["Sovereign Wealth Fund Statism", "State Capitalism / Singapore"],
          f"{ties}")
    check("[F] the tie spans failure counts 3, 4, 4",
          sorted([fails(OSTROM)] + [fails(CORPUS[s]) for s in ties]) == [3, 4, 4])
    check("[F] all three tied systems share one tier",
          len({tier(fails(OSTROM))} |
              {tier(fails(CORPUS[s])) for s in ties}) == 1)
    db, dt = dominance_facts()
    check("[F] dominated by NOTHING, CCO-PTF-CIP-SZH included",
          db == [], f"{db}")
    check("[F] dominates nothing in the corpus", dt == [], f"{dt}")
    check("[F] C5.5 is the criterion that blocks CCO-PTF-CIP-SZH dominance",
          OSTROM["C5.5"] > CORPUS["CCO-PTF-CIP-SZH"]["C5.5"] and
          sorted(c for c in ALL_CRITS
                 if OSTROM[c] > CORPUS["CCO-PTF-CIP-SZH"][c]) == ["C5.5"],
          "expected exactly one criterion above CCO-PTF-CIP-SZH")
    before = corpus_dominance_pairs()
    after = corpus_dominance_pairs(extra=True)
    check("[F] corpus has 11 strict-dominance pairs before insertion",
          before == 11, f"{before}")
    check("[F] insertion adds no dominance pair",
          after - before == 0, f"{before} -> {after}")
    mine, better, equal = domain_rank("Implementation Viability")
    check("[F] Domain 5 is 4.0", abs(mine - 4.0) < 1e-9, f"{mine}")
    check("[F] exactly one corpus system beats Domain 5",
          len(better) == 1, f"{better}")
    check("[F] that system is CCO-PTF-CIP-SZH",
          better == ["CCO-PTF-CIP-SZH"], f"{better}")
    check("[F] three corpus systems tie Domain 5 at 4.0",
          equal == ["Mutual Credit / LETS", "Nordic Social Democracy",
                    "Status Quo Market Capitalism"], f"{equal}")
    dsw, hsw, lsw, gsw = differs_from("Sovereign Wealth Fund Statism")
    check("[F] vs SWF Statism: same total, differs on 8, 4 up 4 down",
          (abs(gsw) < 1e-9 and dsw == 8 and hsw == 4 and lsw == 4),
          f"{dsw}/{hsw}/{lsw}/{gsw}")
    m1, b1, e1 = domain_rank("Material Security")
    check("[F] Domain 1 is 2.0", abs(m1 - 2.0) < 1e-9, f"{m1}")
    d, h, l, g = differs_from("Status Quo Market Capitalism")
    check("[F] vs Status Quo: net gain is +3.5", abs(g - 3.5) < 1e-9, f"{g}")
    rows = ranked_corpus()
    mine_row = [r for r in rows if r[1] == SYSTEM]
    check("[F] appears exactly once in the ranked table", len(mine_row) == 1)
    check("[F] ranks 10= in the 21-system view",
          mine_row and mine_row[0][0] == "10=", f"{mine_row}")
    check("[F] ranked table has 21 rows", len(rows) == 21, f"{len(rows)}")


def group_g():
    """Rebuild the numeric claims the prose makes."""
    ds = domain_scores(OSTROM)
    claims = [
        ("domain vector 2.0/2.5/2.5/3.0/4.0",
         [ds[d] for d in DOMAINS], [2.0, 2.5, 2.5, 3.0, 4.0]),
        ("six Passes", sum(1 for c in ALL_CRITS if OSTROM[c] == 1.0), 6),
        ("sixteen Partials", sum(1 for c in ALL_CRITS if OSTROM[c] == 0.5), 16),
        ("four Failures", sum(1 for c in ALL_CRITS if OSTROM[c] == 0.0), 4),
        ("26 criteria accounted for",
         sum(1 for c in ALL_CRITS if OSTROM[c] in (0.0, 0.5, 1.0)), 26),
        ("20 flags of 26 criteria", len(FLAGS), 20),
        ("6 unflagged criteria", 26 - len(FLAGS), 6),
    ]
    for label, got, want in claims:
        check(f"[G] {label}", got == want, f"got {got}, prose says {want}")
    unflagged = sorted(set(ALL_CRITS) - set(FLAGS))
    check("[G] unflagged set is C2.1, C2.3, C3.4, C5.1, C5.3, C5.5",
          unflagged == ["C2.1", "C2.3", "C3.4", "C5.1", "C5.3", "C5.5"],
          f"{unflagged}")


def group_h():
    doc = read_doc()
    if doc is None:
        check("[H] generated blocks match a fresh render", False, "no document")
        return
    for begin, end, render, name in (
        (BEGIN_SUMMARY, END_SUMMARY, render_summary_table, "summary-table"),
        (BEGIN_CORPUS, END_CORPUS, render_corpus_table, "corpus-table"),
    ):
        if begin not in doc or end not in doc:
            check(f"[H] {name} block markers present", False,
                  "marker missing")
            continue
        check(f"[H] {name} block markers present", True)
        body = doc.split(begin, 1)[1].split(end, 1)[0].strip("\n")
        check(f"[H] {name} is byte-identical to a fresh render",
              body == render(),
              "regenerate with --fill")


def run_checks():
    group_a()
    group_b()
    group_c()
    group_d()
    group_e()
    group_f()
    group_g()
    group_h()
    print("=" * 94)
    print(f"verify_ostrom.py — NEEC Session 23 — {SYSTEM}")
    print("=" * 94)
    print()
    npass = 0
    for label, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        if ok:
            npass += 1
        line = f"{status}  {label}"
        if not ok and detail:
            line += f"\n          {detail}"
        print(line)
    print()
    print("=" * 94)
    print(f"SUMMARY: {npass} passed, {len(RESULTS) - npass} failed "
          f"(of {len(RESULTS)}).")
    print("=" * 94)
    return 0 if npass == len(RESULTS) else 1


def main():
    if "--facts" in sys.argv:
        print_facts()
        return 0
    if "--fill" in sys.argv:
        print(BEGIN_SUMMARY)
        print(render_summary_table())
        print(END_SUMMARY)
        print()
        print(BEGIN_CORPUS)
        print(render_corpus_table())
        print(END_CORPUS)
        return 0
    return run_checks()


if __name__ == "__main__":
    sys.exit(main())
