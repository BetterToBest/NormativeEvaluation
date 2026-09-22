#!/usr/bin/env python3
"""
verify_islamicfinance.py -- verifier for NEEC_IslamicFinance_scoring_scratch.md
==============================================================================
Session 22. Generalises verify_qatar.py (Session 21). Seven check groups:

  1. sources          -- the canonical script loads and self-checks
  2. self-consistency -- the score vector's own arithmetic
  3. transcription    -- every score in the document matches the vector
  4. sensitivity      -- exhaustive enumeration over the flagged calls,
                         plus the three coherent joint readings
  5. scope            -- the mechanism-scope vs broad-scope scenario
  6. corpus           -- rank, ties, dominance, domain comparisons
  7. numbers          -- every numeric claim in the prose is rebuilt and
                         required to appear verbatim in the text

Modes:
  python3 verify_islamicfinance.py --facts   print computed facts, no checks
  python3 verify_islamicfinance.py --fill    rewrite the document's GENERATED
                                             blocks in place
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


def build_corpus(mod):
    corpus = {k: dict(v) for k, v in mod.SCORES.items()}
    corpus[SYSTEM] = dict(SCORE)
    return corpus


def ranked(corpus):
    rows = []
    for name, vec in corpus.items():
        t = total(vec)
        f = len(failures(vec))
        rows.append((name, t, pct(t), f, tier(f)))
    rows.sort(key=lambda r: (-r[1], r[0]))
    out, prev, rank = [], None, 0
    for i, r in enumerate(rows, start=1):
        if r[1] != prev:
            rank = i
            prev = r[1]
        out.append((rank,) + r)
    return out


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


def render_corpus_table(corpus):
    lines = ["| Rank | System | Score /26 | % | Failures | Tier |",
             "|---|---|---|---|---|---|"]
    for rank, name, t, p, f, tr in ranked(corpus):
        mark = " **<-- new**" if name == SYSTEM else ""
        lines.append(f"| {rank} | {name}{mark} | {t:.1f} | {p:.1f} | {f} | {tr} |")
    return "\n".join(lines)


def fill(doc_text, corpus):
    def repl(match):
        key = match.group(1)
        body = {"summary": render_summary_table(),
                "corpus": render_corpus_table(corpus)}[key]
        return (f"<!-- GENERATED:{key} -->\n{body}\n<!-- END GENERATED:{key} -->")
    return re.sub(
        r"<!-- GENERATED:(\w+) -->.*?<!-- END GENERATED:\1 -->",
        repl, doc_text, flags=re.S)


# ---------------------------------------------------------------- facts
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


def facts():
    mod = load_canon()
    corpus = build_corpus(mod)
    t = total(SCORE)
    f = failures(SCORE)
    print("=" * 78)
    print("COMPUTED FACTS")
    print("=" * 78)
    print(f"total {t} ({pct(t)}%), failures {len(f)}: {f}, tier {tier(len(f))}")
    print("domains:", {k: v for k, v in domain_totals(SCORE).items()})
    print(f"undisputed failures: "
          f"{[c for c in f if c not in FLAGGED]}")
    keys, counts, lo, hi, n = enumerate_flags()
    print(f"\nflagged calls: {len(keys)} -> {n} combinations")
    print("tier distribution:", counts)
    print(f"totals range {lo}-{hi}")
    for label, ov in (("A (as designed)", READING_A),
                      ("B (as scored)", {}),
                      ("C (strict form-over-substance)", READING_C),
                      ("broad scope (social finance in)", BROAD_SCOPE)):
        v = apply(SCORE, ov)
        tt, ff = total(v), failures(v)
        print(f"reading {label}: {tt}/26 ({pct(tt)}%), "
              f"{len(ff)} failures, {tier(len(ff))}")
    print("\nCORPUS")
    for row in ranked(corpus):
        print(row)
    print("\nexact score ties at %.1f:" % t,
          [n2 for n2, v in corpus.items()
           if abs(total(v) - t) < 1e-9 and n2 != SYSTEM])
    doms = []
    for other in corpus:
        if other == SYSTEM:
            continue
        if dominates(corpus[other], SCORE):
            doms.append(("dominated by", other))
        if dominates(SCORE, corpus[other]):
            doms.append(("dominates", other))
    print("dominance:", doms)
    npairs = sum(1 for a in corpus for b in corpus
                 if a != b and dominates(corpus[a], corpus[b]))
    base = {k: v for k, v in corpus.items() if k != SYSTEM}
    npairs0 = sum(1 for a in base for b in base
                  if a != b and dominates(base[a], base[b]))
    print(f"strict-dominance ordered pairs: {npairs0} -> {npairs}")
    for other in ("Georgism / Land Value Tax", "Universal Basic Services",
                  "Status Quo Market Capitalism", "Sovereign Wealth Fund Statism"):
        diff = [c for c in CRITS if corpus[other][c] != SCORE[c]]
        hi_c = [c for c in diff if SCORE[c] > corpus[other][c]]
        print(f"vs {other}: differ on {len(diff)} ({diff}); "
              f"IF higher on {len(hi_c)} ({hi_c})")
    dt = domain_totals(SCORE)
    d5 = sorted(((sum(v[c] for c in DOMAINS['Implementation Viability'][0]), k)
                 for k, v in corpus.items()), reverse=True)
    print("Domain 5 leaders:", d5[:5])
    print("Domain 5 value for IF:", dt["Implementation Viability"])
    d4 = sorted(((sum(v[c] for c in DOMAINS['Ethical Integrity'][0]), k)
                 for k, v in corpus.items()))
    print("Domain 4 lowest:", d4[:6])
    return corpus


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
    if "--facts" in sys.argv:
        facts()
        return 0

    mod = load_canon()
    corpus = build_corpus(mod)

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    if "--fill" in sys.argv:
        new = fill(text, corpus)
        with open(DOC, "w", encoding="utf-8") as fh:
            fh.write(new)
        print("filled GENERATED blocks in", os.path.basename(DOC))
        return 0

    flat = norm(text)
    c = Checker()

    print("=" * 78)
    print("verify_islamicfinance.py -- NEEC Session 22")
    print("=" * 78)

    print("\n[1] Sources")
    c.check("canonical script exposes SCORES", hasattr(mod, "SCORES"))
    c.check("canonical corpus holds 20 systems", len(mod.SCORES) == 20,
            f"got {len(mod.SCORES)}")
    c.check("system not yet inserted", SYSTEM not in mod.SCORES)
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

    print("\n[6] Corpus comparison")
    rows = ranked(corpus)
    mine = [r for r in rows if r[1] == SYSTEM][0]
    c.check("corpus with the new system holds 21", len(rows) == 21)
    ties = sorted(n2 for n2, v in corpus.items()
                  if abs(total(v) - t) < 1e-9 and n2 != SYSTEM)
    c.check("exact three-way score tie with Georgism and UBS",
            ties == ["Georgism / Land Value Tax", "Universal Basic Services"],
            f"got {ties}")
    c.check("the three tied systems hold 2, 3 and 5 failures",
            sorted(len(failures(corpus[x])) for x in ties + [SYSTEM])
            == [2, 3, 5])
    c.check("the tie spans two adequacy tiers",
            len({tier(len(failures(corpus[x]))) for x in ties + [SYSTEM]}) == 2)
    c.check("rank is 12 (competition rank)", mine[0] == 12, f"got {mine[0]}")
    dom_by = sorted(o for o in corpus
                    if o != SYSTEM and dominates(corpus[o], SCORE))
    dom_of = sorted(o for o in corpus
                    if o != SYSTEM and dominates(SCORE, corpus[o]))
    c.check("dominated by no system, CCO-PTF-CIP-SZH included",
            dom_by == [], f"got {dom_by}")
    c.check("strictly dominates Stakeholder Capitalism only",
            dom_of == ["Stakeholder Capitalism"], f"got {dom_of}")
    sc = corpus["Stakeholder Capitalism"]
    hi_sc = [x for x in CRITS if SCORE[x] > sc[x]]
    lo_sc = [x for x in CRITS if SCORE[x] < sc[x]]
    c.check("higher than Stakeholder Capitalism on 6 criteria, lower on none",
            len(hi_sc) == 6 and not lo_sc, f"got {len(hi_sc)}/{lo_sc}")
    c.check("CCO-PTF-CIP-SZH is held off by C5.5 alone",
            [x for x in CRITS if SCORE[x] > corpus["CCO-PTF-CIP-SZH"][x]]
            == ["C5.5"])
    sq = corpus["Status Quo Market Capitalism"]
    hi_sq = [x for x in CRITS if SCORE[x] > sq[x]]
    df_sq = [x for x in CRITS if SCORE[x] != sq[x]]
    c.check("differs from Status Quo on 8, higher on 7, by 3.0 points",
            (len(df_sq), len(hi_sq)) == (8, 7)
            and abs(total(SCORE) - total(sq) - 3.0) < 1e-9)
    d4vals = sorted((sum(v[cc] for cc in DOMAINS["Ethical Integrity"][0]), k)
                    for k, v in corpus.items())
    pos = [i for i, (val, k) in enumerate(d4vals, 1) if k == SYSTEM][0]
    c.check("Domain 4 of 1.5 is fifth-lowest in the corpus",
            pos == 5 and abs(d4vals[pos - 1][0] - 1.5) < 1e-9, f"got {pos}")
    d5vals = {k: sum(v[cc] for cc in DOMAINS["Implementation Viability"][0])
              for k, v in corpus.items()}
    best = max(d5vals.values())
    c.check("Domain 5 of 4.5 ties the corpus best",
            abs(d5vals[SYSTEM] - 4.5) < 1e-9 and abs(best - 4.5) < 1e-9,
            f"best {best}")
    sharers = sorted(k for k, v in d5vals.items() if abs(v - best) < 1e-9)
    c.check("exactly two systems hold the best Domain 5",
            len(sharers) == 2 and SYSTEM in sharers
            and "CCO-PTF-CIP-SZH" in sharers, f"got {sharers}")
    npairs = sum(1 for a in corpus for b in corpus
                 if a != b and dominates(corpus[a], corpus[b]))
    base = {k: v for k, v in corpus.items() if k != SYSTEM}
    npairs0 = sum(1 for a in base for b in base
                  if a != b and dominates(base[a], base[b]))
    c.check("insertion takes dominance pairs from 11 to 12",
            (npairs0, npairs) == (11, 12), f"got {npairs0} -> {npairs}")

    print("\n[7] Numeric claims rebuilt and matched in the prose")
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
        "11 to 12",
        "8.0-16.0",
    ]
    for cl in claims:
        c.check(f"prose contains {cl!r}", norm(cl) in flat)

    print("\n[8] Generated blocks are byte-identical to a fresh render")
    c.check("document round-trips through --fill", fill(text, corpus) == text)

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
