#!/usr/bin/env python3
"""
verify_ostrom.py — entry verifier for the Step 1b evaluation of Ostrom-style
commons governance (scored in Session 23; inserted into the canonical corpus in
Session 25; narrowed in Session 26 by narrow_verifiers_s26.py).

This script checks the claims the document makes about this entry itself.
Claims that compare the entry with other systems (criterion bands, ranks, ties,
dominance, domain positions, flag counts, tier robustness) are checked on the
canonical corpus by verify_comparative_claims.py, which also writes the
document's corpus table (decision D12). The Session 23 version is kept unedited
as verify_ostrom_s25_snapshot.py and still runs, against the 20-system corpus it
was written for, in run_all_checks.py.

Check groups:

  [A] sources and identity: the canonical corpus holds this entry with
      exactly the vector below; the flag register and scenario are well formed
  [B] self-consistency of the scored vector
  [C] transcription against NEEC_Ostrom_Commons_scoring_scratch.md
      (symmetric: flagged headings must say "contestable", unflagged must not;
       and every flagged criterion must state its alternative inline)
  [D] exhaustive sensitivity over the flagged set, plus three coherent
      joint readings (D6)
  [E] the scope scenario (knowledge / digital commons counted in)
  [G] rebuilt numeric claims used in the prose
  [H] byte-equality of the generated summary table in the document
  (Group [F], the corpus comparison, is in verify_comparative_claims.py.)

Modes:
  (no args)  run every check and print PASS/FAIL per check
  --fill     rewrite the document's generated summary table in place

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
# Generated blocks
# --------------------------------------------------------------------------

BEGIN_SUMMARY = "<!-- BEGIN GENERATED: summary-table -->"
END_SUMMARY = "<!-- END GENERATED: summary-table -->"


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
    check("[A1] canonical corpus holds this entry", SYSTEM in CORPUS)
    check("[A2] canonical criteria list has 26 entries", len(ALL_CRITS) == 26,
          f"got {len(ALL_CRITS)}")
    check("[A3] its canonical vector equals this script's vector",
          CORPUS.get(SYSTEM) == OSTROM)
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
    group_g()
    group_h()
    print("=" * 94)
    print(f"verify_ostrom.py — NEEC entry checks — {SYSTEM} (Session 23; narrowed Session 26)")
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
    if "--fill" in sys.argv:
        doc = read_doc()
        if doc is None or doc.count(BEGIN_SUMMARY) != 1 or doc.count(END_SUMMARY) != 1:
            sys.exit(f"ERROR: {DOC}: summary-table markers missing or repeated; nothing written")
        body = doc.split(BEGIN_SUMMARY, 1)[1].split(END_SUMMARY, 1)[0]
        new = doc.replace(BEGIN_SUMMARY + body + END_SUMMARY,
                          BEGIN_SUMMARY + "\n" + render_summary_table() + "\n" + END_SUMMARY, 1)
        with open(os.path.join(HERE, DOC), "w", encoding="utf-8") as fh:
            fh.write(new)
        print(f"filled the generated summary table in {DOC}")
        return 0
    return run_checks()


if __name__ == "__main__":
    sys.exit(main())
