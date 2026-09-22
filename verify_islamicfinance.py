#!/usr/bin/env python3
"""
verify_islamicfinance.py -- entry verifier for NEEC_IslamicFinance_scoring_scratch.md
====================================================================================
Scored in Session 22; inserted into the canonical corpus in Session 25; narrowed
in Session 26 by narrow_verifiers_s26.py. This script checks the claims the
document makes about this entry itself. Claims that compare the entry with other
systems (criterion bands, ranks, ties, dominance, domain positions, flag counts)
are checked on the canonical corpus by verify_comparative_claims.py, which also
writes the document's corpus table (decision D12). The Session 22 version is kept
unedited as verify_islamicfinance_s25_snapshot.py and still runs, against the
20-system corpus it was written for, in run_all_checks.py.

Seven check groups:

  1. sources          -- the canonical script loads and self-checks, and holds
                         this entry with exactly the vector below
  2. self-consistency -- the score vector's own arithmetic
  3. transcription    -- every score in the document matches the vector
  4. sensitivity      -- exhaustive enumeration over the flagged calls,
                         plus the three coherent joint readings
  5. scope            -- the mechanism-scope vs broad-scope scenario
  6. numbers          -- every numeric claim about this entry is rebuilt and
                         required to appear verbatim in the text
  7. generated block  -- the summary table is byte-identical to a fresh render

Modes:
  python3 verify_islamicfinance.py --fill    rewrite the document's GENERATED
                                             summary block in place
  python3 verify_islamicfinance.py           run every check
"""
import importlib.util
import io
import contextlib
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(HERE, "NEEC_IslamicFinance_scoring_scratch.md")
CANON = os.path.join(HERE, "neec_weighting_robustness_analysis_v2.py")

SYSTEM = "Islamic Finance / Profit-Sharing Banking"

CRITS = ["C1.1", "C1.2a", "C1.2b", "C1.3", "C1.4", "C1.5",
         "C2.1", "C2.2", "C2.3", "C2.4", "C2.5",
         "C3.1", "C3.2", "C3.3", "C3.4", "C3.5",
         "C4.1", "C4.2", "C4.3", "C4.4", "C4.5",
         "C5.1", "C5.2", "C5.3", "C5.4", "C5.5"]

CRIT_NAMES = {
    "C1.1": "Poverty Elimination Capacity",
    "C1.2a": "Wealth Building for Resilience",
    "C1.2b": "Prevention of Exploitative Accumulation",
    "C1.3": "Housing Security",
    "C1.4": "Automation Resilience",
    "C1.5": "Universal Wealth Access (narrowed)",
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
    "Material Security": (["C1.1", "C1.2a", "C1.2b", "C1.3", "C1.4", "C1.5"], 6.0),
    "Human Autonomy": (["C2.1", "C2.2", "C2.3", "C2.4", "C2.5"], 5.0),
    "System Resilience": (["C3.1", "C3.2", "C3.3", "C3.4", "C3.5"], 5.0),
    "Ethical Integrity": (["C4.1", "C4.2", "C4.3", "C4.4", "C4.5"], 5.0),
    "Implementation Viability": (["C5.1", "C5.2", "C5.3", "C5.4", "C5.5"], 5.0),
}

# The scored vector (Reading B -- preponderance of practice).
SCORE = {
    "C1.1": 0.5, "C1.2a": 0.5, "C1.2b": 0.0, "C1.3": 0.5, "C1.4": 0.0, "C1.5": 0.5,
    "C2.1": 0.5, "C2.2": 0.0, "C2.3": 0.5, "C2.4": 0.5, "C2.5": 1.0,
    "C3.1": 0.5, "C3.2": 0.5, "C3.3": 0.5, "C3.4": 1.0, "C3.5": 0.5,
    "C4.1": 0.5, "C4.2": 0.0, "C4.3": 0.5, "C4.4": 0.0, "C4.5": 0.5,
    "C5.1": 1.0, "C5.2": 1.0, "C5.3": 1.0, "C5.4": 0.5, "C5.5": 1.0,
}

# Flagged contestable calls: criterion -> alternative score.
FLAGGED = {
    "C1.1": 0.0, "C1.2a": 1.0, "C1.2b": 0.5, "C1.4": 0.5, "C1.5": 0.0,
    "C2.4": 0.0, "C2.5": 0.5,
    "C3.4": 0.5, "C3.5": 0.0,
    "C4.1": 0.0, "C4.3": 0.0, "C4.4": 0.5, "C4.5": 0.0,
    "C5.2": 0.5, "C5.4": 1.0, "C5.5": 0.5,
}

# Three coherent joint readings. Reading B is the scored vector.
READING_A = {"C1.2a": 1.0, "C1.2b": 0.5, "C1.4": 0.5, "C4.4": 0.5}
READING_C = {"C1.1": 0.0, "C1.5": 0.0, "C2.4": 0.0, "C3.5": 0.0,
             "C4.1": 0.0, "C4.5": 0.0}
# Broad scope: the Islamic social-finance layer (zakat, waqf, takaful) counted
# as part of the mechanism rather than adjacent to it.
BROAD_SCOPE = {"C1.1": 1.0, "C1.2b": 0.5}


def tier(nfail):
    if nfail <= 2:
        return "Potentially Adequate"
    if nfail <= 5:
        return "Partially Adequate"
    return "Structurally Inadequate"


def total(vec):
    return sum(vec[c] for c in CRITS)


def failures(vec):
    return [c for c in CRITS if vec[c] == 0.0]


def domain_totals(vec):
    return {d: sum(vec[c] for c in cs) for d, (cs, _m) in DOMAINS.items()}


def apply(vec, overrides):
    out = dict(vec)
    out.update(overrides)
    return out


def load_canon():
    spec = importlib.util.spec_from_file_location("canon", CANON)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def dominates(a, b):
    """a strictly dominates b: >= on every criterion, > on at least one."""
    ge = all(a[c] >= b[c] for c in CRITS)
    gt = any(a[c] > b[c] for c in CRITS)
    return ge and gt


def pct(x, denom=26.0):
    return round(100.0 * x / denom, 1)


# ---------------------------------------------------------------- generated
def render_summary_table():
    lines = ["| Criterion | Name | Score | Result |", "|---|---|---|---|"]
    for c in CRITS:
        s = SCORE[c]
        res = {1.0: "Pass", 0.5: "Partial", 0.0: "Structural Failure"}[s]
        flag = " *(flagged)*" if c in FLAGGED else ""
        lines.append(f"| {c} | {CRIT_NAMES[c]}{flag} | {s:.1f} | {res} |")
    dt = domain_totals(SCORE)
    lines.append("")
    lines.append("| Domain | Score | Max |")
    lines.append("|---|---|---|")
    for d, (_cs, m) in DOMAINS.items():
        lines.append(f"| {d} | {dt[d]:.1f} | {m:.0f} |")
    t = total(SCORE)
    f = failures(SCORE)
    lines.append(f"| **Total** | **{t:.1f}** | **26** |")
    lines.append("")
    lines.append(f"**Total: {t:.1f}/26 ({pct(t):.1f}%). "
                 f"Structural failures: {len(f)} ({', '.join(f)}). "
                 f"Adequacy tier: {tier(len(f))}.**")
    return "\n".join(lines)


def fill(doc_text):
    """Rewrite the summary block only. The corpus table is written by
    verify_comparative_claims.py --fill (Session 26)."""
    body = render_summary_table()
    return re.sub(
        r"<!-- GENERATED:summary -->.*?<!-- END GENERATED:summary -->",
        lambda m: f"<!-- GENERATED:summary -->\n{body}\n<!-- END GENERATED:summary -->",
        doc_text, flags=re.S)


# ---------------------------------------------------------------- sensitivity
def enumerate_flags():
    keys = sorted(FLAGGED)
    counts = {"Potentially Adequate": 0, "Partially Adequate": 0,
              "Structurally Inadequate": 0}
    totals = []
    for bits in itertools.product([0, 1], repeat=len(keys)):
        vec = dict(SCORE)
        for k, b in zip(keys, bits):
            if b:
                vec[k] = FLAGGED[k]
        t = total(vec)
        totals.append(t)
        counts[tier(len(failures(vec)))] += 1
    return keys, counts, min(totals), max(totals), len(totals)


# ---------------------------------------------------------------- checks
class Checker:
    def __init__(self):
        self.p = 0
        self.f = 0

    def check(self, label, cond, detail=""):
        if cond:
            self.p += 1
            print(f"  PASS  {label}")
        else:
            self.f += 1
            print(f"  FAIL  {label}" + (f"\n        {detail}" if detail else ""))


def norm(s):
    return re.sub(r"\s+", " ", s)


def main():
    mod = load_canon()

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    if "--fill" in sys.argv:
        new = fill(text)
        with open(DOC, "w", encoding="utf-8") as fh:
            fh.write(new)
        print("filled the GENERATED summary block in", os.path.basename(DOC))
        return 0

    flat = norm(text)
    c = Checker()

    print("=" * 78)
    print("verify_islamicfinance.py -- NEEC entry checks: Islamic finance (Session 22; narrowed Session 26)")
    print("=" * 78)

    print("\n[1] Sources")
    c.check("canonical script exposes SCORES", hasattr(mod, "SCORES"))
    c.check("canonical corpus holds this system", SYSTEM in mod.SCORES)
    c.check("its canonical vector equals this script's vector",
            mod.SCORES.get(SYSTEM) == SCORE)
    c.check("criteria order matches canonical",
            list(next(iter(mod.SCORES.values())).keys()) == CRITS)
    c.check("every canonical vector is complete",
            all(set(v) == set(CRITS) for v in mod.SCORES.values()))

    print("\n[2] Self-consistency")
    t = total(SCORE)
    fl = failures(SCORE)
    dt = domain_totals(SCORE)
    c.check("all scores in {0, 0.5, 1}",
            all(s in (0.0, 0.5, 1.0) for s in SCORE.values()))
    c.check("26 criteria scored", len(SCORE) == 26)
    c.check(f"domain totals sum to total ({t})",
            abs(sum(dt.values()) - t) < 1e-9)
    c.check("total is 13.5", abs(t - 13.5) < 1e-9, f"got {t}")
    c.check("percentage is 51.9", abs(pct(t) - 51.9) < 1e-9, f"got {pct(t)}")
    c.check("5 structural failures", len(fl) == 5, f"got {fl}")
    c.check("failure set is C1.2b, C1.4, C2.2, C4.2, C4.4",
            fl == ["C1.2b", "C1.4", "C2.2", "C4.2", "C4.4"], f"got {fl}")
    c.check("tier is Partially Adequate", tier(len(fl)) == "Partially Adequate")
    c.check("domain vector is 2.0/2.5/3.0/1.5/4.5",
            [dt["Material Security"], dt["Human Autonomy"],
             dt["System Resilience"], dt["Ethical Integrity"],
             dt["Implementation Viability"]] == [2.0, 2.5, 3.0, 1.5, 4.5],
            f"got {dt}")

    print("\n[3] Transcription against the document")
    for crit in CRITS:
        s = SCORE[crit]
        label = {1.0: "Pass", 0.5: "Partial", 0.0: "Structural Failure"}[s]
        heading = f"#### {crit} {CRIT_NAMES[crit].replace(' (narrowed)', '')}"
        found = [ln for ln in text.splitlines() if ln.startswith(heading)]
        ok = bool(found) and f"{s:.1f} ({label})" in found[0]
        c.check(f"{crit} heading states {s:.1f} ({label})", ok,
                f"heading: {found[0] if found else 'MISSING'}")
    for crit in FLAGGED:
        found = [ln for ln in text.splitlines()
                 if ln.startswith(f"#### {crit} ")]
        c.check(f"{crit} heading marks the call as contestable",
                bool(found) and "contestable" in found[0].lower())
    for crit in CRITS:
        if crit in FLAGGED:
            continue
        found = [ln for ln in text.splitlines()
                 if ln.startswith(f"#### {crit} ")]
        c.check(f"{crit} heading is not marked contestable",
                bool(found) and "contestable" not in found[0].lower())

    print("\n[4] Sensitivity -- exhaustive enumeration")
    keys, counts, lo, hi, n = enumerate_flags()
    c.check("16 flagged calls", len(keys) == 16, f"got {len(keys)}")
    c.check("65536 combinations", n == 65536, f"got {n}")
    c.check("totals run 8.0 to 16.0", (lo, hi) == (8.0, 16.0), f"got {lo}-{hi}")
    c.check("all three tiers are reachable",
            all(v > 0 for v in counts.values()), str(counts))
    c.check("enumeration counts sum to the combination count",
            sum(counts.values()) == n)
    undisputed = [x for x in fl if x not in FLAGGED]
    c.check("exactly two failures are undisputed (C2.2, C4.2)",
            undisputed == ["C2.2", "C4.2"], f"got {undisputed}")
    for label, ov, exp_t, exp_f in (
            ("A", READING_A, 15.5, 2),
            ("B", {}, 13.5, 5),
            ("C", READING_C, 10.5, 11)):
        v = apply(SCORE, ov)
        c.check(f"reading {label} totals {exp_t} with {exp_f} failures",
                abs(total(v) - exp_t) < 1e-9 and len(failures(v)) == exp_f,
                f"got {total(v)}/{len(failures(v))}")
    for crit, alt in FLAGGED.items():
        seg = extract_criterion(text, crit)
        c.check(f"{crit} states its alternative ({alt:.1f}) inline",
                seg is not None and f"{alt:.1f}" in seg)

    print("\n[5] Scope scenario")
    v = apply(SCORE, BROAD_SCOPE)
    c.check("broad-scope reading totals 14.5 with 4 failures",
            abs(total(v) - 14.5) < 1e-9 and len(failures(v)) == 4,
            f"got {total(v)}/{len(failures(v))}")
    c.check("broad-scope reading stays Partially Adequate",
            tier(len(failures(v))) == "Partially Adequate")

    print("\n[6] Numeric claims about this entry, rebuilt and matched in the prose")
    claims = [
        f"{t:.1f}/26",
        f"{pct(t):.1f}%",
        f"{len(fl)} structural failures",
        "2.0 / 2.5 / 3.0 / 1.5 / 4.5",
        f"{len(keys)} flagged",
        f"{n:,} combinations".replace(",", ","),
        f"{lo:.1f}-{hi:.1f}",
        "15.5/26",
        "10.5/26",
        "14.5/26",
        "8.0-16.0",
    ]
    for cl in claims:
        c.check(f"prose contains {cl!r}", norm(cl) in flat)

    print("\n[7] Generated summary block is byte-identical to a fresh render")
    c.check("summary block round-trips through --fill", fill(text) == text)

    print("\n" + "=" * 78)
    print(f"SUMMARY: {c.p} passed, {c.f} failed (of {c.p + c.f}).")
    print("=" * 78)
    return 1 if c.f else 0


def extract_criterion(text, crit):
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith(f"#### {crit} "):
            start = i
            break
    if start is None:
        return None
    out = []
    for ln in lines[start + 1:]:
        if ln.startswith("#### ") or ln.startswith("### ") or ln.startswith("## "):
            break
        out.append(ln)
    return "\n".join(out)


if __name__ == "__main__":
    sys.exit(main())
