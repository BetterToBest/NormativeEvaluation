#!/usr/bin/env python3
"""
Independent verification of the State Capitalism / Qatar score vector
(Step 1b, Session 21) BEFORE it is spliced into any canonical file.
Generalized from verify_singapore.py (Session 19), per this project's
methodology: "programmatic verification over visual checking," "dominance
checks are programmatic," and Session 20's standing rule, "generate, don't
transcribe."

Seven check groups:
  (0) Sources: the REAL canonical SCORES dict (20 systems) is imported from
      the unmodified neec_weighting_robustness_analysis_v2.py, its own
      transcription self-check is required to pass, and the vector-level
      dominance test below is validated against the canonical helper on
      every ordered pair of canonical systems.
  (1) Self-consistency: re-sum the 26-criterion vector against the stated
      domain totals, total, distribution, failures, and tier.
  (2) Transcription: parse the scratch document's criterion headings
      (scores AND flag markers), domain-sum lines, Summary Scores lines,
      each flagged call's inline consequence, and each citizens-only
      scenario statement; and compare its two GENERATED tables verbatim
      with a fresh render.
  (3) Contestable-call sensitivity: each flagged call alone, jointly, and
      in all 2**12 combinations under the confirmed population scope.
  (4) Population scope: the citizens-only scenario, alone and across the
      flagged calls it leaves open.
  (5) Corpus comparison: every comparative claim recomputed against the
      canonical corpus.
  (6) Stated numbers: every numeric claim and computed figure in the
      document is rebuilt here and must appear verbatim (whitespace
      normalized) in the text.

Modes:
  python3 verify_qatar.py         run all checks (this is the captured output)
  python3 verify_qatar.py --fill  rewrite the document's two GENERATED
                                  blocks from a fresh render, then exit

PORTABILITY: looks beside itself first, then in the conventional working
locations, and prints only file names, so the captured output reproduces
byte for byte from any directory holding the companion files (the canonical
v2 script and the scratch document). Writes nothing unless --fill is given.
"""

import contextlib
import importlib.util
import io
import os
import re
import sys
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = (HERE, os.getcwd(), "/home/claude", "/home/claude/neec",
               "/home/claude/qatar", "/mnt/user-data/outputs", "/mnt/project")
SCRATCH_DOC = "NEEC_StateCapitalism_Qatar_scoring_scratch.md"
CANON = "neec_weighting_robustness_analysis_v2.py"


def find(filename):
    for d in SEARCH_DIRS:
        p = os.path.join(d, filename)
        if os.path.isfile(p):
            return p
    return None


def locate(filename):
    p = find(filename)
    if p is None:
        sys.exit(f"ERROR: could not locate {filename} in {SEARCH_DIRS}")
    return p


ALL_CRITS = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5'] + \
            [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
DOMAINS = {
    'D1': ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5'],
    'D2': [f'C2.{i}' for i in range(1, 6)],
    'D3': [f'C3.{i}' for i in range(1, 6)],
    'D4': [f'C4.{i}' for i in range(1, 6)],
    'D5': [f'C5.{i}' for i in range(1, 6)],
}
DOMAIN_MAX = {'D1': 6, 'D2': 5, 'D3': 5, 'D4': 5, 'D5': 5}
DOMAIN_NAMES = {'D1': 'Material Security', 'D2': 'Human Autonomy',
                'D3': 'System Resilience', 'D4': 'Ethical Integrity',
                'D5': 'Implementation Viability'}
TIERS = ('Potentially Adequate', 'Partially Adequate', 'Structurally Inadequate')
CRIT_RE = r'C[1-5]\.[1-6][ab]?'
NUM = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
       8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}

QA_NAME = 'State Capitalism / Qatar'
SG_NAME = 'State Capitalism / Singapore'
CN_NAME = 'State Capitalism / China'
SWF_NAME = 'Sovereign Wealth Fund Statism'
CCO_NAME = 'CCO-PTF-CIP-SZH'
STEP1B = ('Georgism', 'Mutual Credit', 'Doughnut', 'Universal Basic Services',
          SWF_NAME, CN_NAME, SG_NAME)

# The vector scored in the scratch document. Population scope: everyone who
# lives and works in Qatar, non-citizens included (user-confirmed, Session 21).
QA = {
    'C1.1': 0.5, 'C1.2a': 0.5, 'C1.2b': 0.5, 'C1.3': 0.5, 'C1.4': 0.5, 'C1.5': 0.0,
    'C2.1': 0.0, 'C2.2': 0.0, 'C2.3': 0.5, 'C2.4': 0.0, 'C2.5': 0.5,
    'C3.1': 0.5, 'C3.2': 0.5, 'C3.3': 0.5, 'C3.4': 0.5, 'C3.5': 0.0,
    'C4.1': 0.5, 'C4.2': 0.0, 'C4.3': 0.0, 'C4.4': 0.0, 'C4.5': 0.0,
    'C5.1': 1.0, 'C5.2': 0.5, 'C5.3': 1.0, 'C5.4': 0.5, 'C5.5': 0.0,
}
PUBLISHED = {'D1': 2.5, 'D2': 1.0, 'D3': 2.0, 'D4': 0.5, 'D5': 3.0,
             'Total': 9.0, 'Percent': 35, 'Failures': 10,
             'Tier': 'Structurally Inadequate'}
PASSES = {'C5.1', 'C5.3'}

# Every contestable call flagged inline in the scratch document.
FLAGGED = {
    'C1.1':  (1.0, 'extreme line / CPS precedent'),
    'C1.2a': (1.0, 'UBS median wealth above the bar'),
    'C1.2b': (0.0, 'citizenship divide, no limit at the top'),
    'C1.5':  (0.5, 'citizenship read as a membership gate'),
    'C2.1':  (0.5, '2020 reforms as reduced coercion'),
    'C3.3':  (1.0, 'three compound shocks absorbed'),
    'C3.4':  (1.0, 'post-2014 and post-blockade adjustment'),
    'C3.5':  (0.5, 'ILO cooperation, registry, fiscal data'),
    'C4.1':  (1.0, 'SWF Statism precedent'),
    'C5.3':  (0.5, 'partial by necessity, no scaling path'),
    'C5.4':  (1.0, '90.6% referendum approval'),
    'C5.5':  (0.5, 'SWF Statism precedent, GCC variation'),
}
UNDISPUTED_FAILURES = {'C2.2', 'C2.4', 'C4.2', 'C4.3', 'C4.4', 'C4.5'}
CITIZENS_ONLY = {'C1.1': 1.0, 'C1.2a': 1.0, 'C1.3': 1.0, 'C1.5': 1.0,
                 'C2.1': 0.5, 'C2.2': 0.5, 'C4.5': 0.5}

# Figures the rationale computes from sourced inputs (group 6).
BUDGET_OIL, BUDGET_TOTAL = 155, 199          # QAR bn, 2026 budget (GCO)
WEALTH_BAR, YEARS = 60000, 20                # C1.2a threshold
MIN_WAGE_USD = 274                           # QAR 1,000 (HRW)
LNG_LOST, LNG_CAPACITY = 12.8, 77            # mtpa (Al Jazeera; MECouncil)
LNG_PLANNED = 142                            # mtpa by 2030 (MECouncil)
Q1_OIL_2025, Q1_OIL_2026 = 42.5, 32.7        # QAR bn (Reuters via Zawya)
CPI_PEAK_2008, CPI_STRESS_BOUND = 15.1, 5    # % (IMF via TheGlobalEconomy)
CPI_LONG_RUN = 3.2                           # % average 1980-2024
MIGRANT_SHARE_HRW = 91                       # % of population (HRW 2026)
CITIZEN_SHARE_HIGH = 13                      # % (International IDEA)


def dsums(v):
    return {d: sum(v[c] for c in cs) for d, cs in DOMAINS.items()}


def total(v):
    return sum(v[c] for c in ALL_CRITS)


def fails(v):
    return [c for c in ALL_CRITS if v[c] == 0.0]


def tier(n):
    return ('Potentially Adequate' if n <= 2 else
            'Partially Adequate' if n <= 5 else 'Structurally Inadequate')


def dominates(a, b):
    return all(a[c] >= b[c] for c in ALL_CRITS) and any(a[c] > b[c] for c in ALL_CRITS)


def moved(v, changes):
    out = dict(v)
    out.update(changes)
    return out


def describe(v):
    n = len(fails(v))
    return f"{total(v):.1f}/26, {n} failure{'' if n == 1 else 's'}, {tier(n)}"


def key_like(corpus, fragment):
    hits = [k for k in corpus if fragment in k]
    assert len(hits) == 1, f"expected one key containing {fragment!r}, got {hits}"
    return hits[0]


def lst(items):
    items = list(items)
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + ", and " + items[-1]


def deltas_str(ds):
    return ", ".join(f"{x + 0.0:+.1f}" for x in ds)


def ordinal(n):
    suf = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suf}"


def in_order(items):
    return sorted(items, key=ALL_CRITS.index)


CIT = moved(QA, CITIZENS_ONLY)
LIVE_ALL = [c for c in ALL_CRITS if c in FLAGGED]
LIVE_CIT = [c for c in LIVE_ALL if c not in CITIZENS_ONLY]
SCOPE_SET_FLAGS = [c for c in LIVE_ALL if c in CITIZENS_ONLY]


def enumerate_flags(base, live):
    counts, totals = {}, []
    for bits in product((0, 1), repeat=len(live)):
        v = moved(base, {c: FLAGGED[c][0] for c, b in zip(live, bits) if b})
        n = len(fails(v))
        counts[tier(n)] = counts.get(tier(n), 0) + 1
        totals.append((total(v), n))
    return counts, min(totals), max(totals)


def render_sensitivity():
    out = ["| Criterion | Primary | Alternative reading | Total | Failures | Tier |",
           "|---|---|---|---|---|---|"]
    for c in LIVE_ALL:
        alt, label = FLAGGED[c]
        v = moved(QA, {c: alt})
        n = len(fails(v))
        out.append(f"| {c} | {QA[c]:.1f} | {alt:.1f} — {label} | {total(v):.1f} | {n} | {tier(n)} |")
    return "\n".join(out) + "\n"


def render_scope():
    out = ["| Reading | Criteria moved | Total | Failures | Tier | Flagged calls varied | Combinations by tier | Total range |",
           "|---|---|---|---|---|---|---|---|"]
    for label, v, live, nmoved in (("All residents (confirmed)", QA, LIVE_ALL, 0),
                                   ("Citizens only (scenario)", CIT, LIVE_CIT, len(CITIZENS_ONLY))):
        counts, lo, hi = enumerate_flags(v, live)
        by = "; ".join(f"{t} {counts[t]:,}" for t in TIERS if t in counts)
        n = len(fails(v))
        out.append(f"| {label} | {nmoved} | {total(v):.1f}/26 | {n} | {tier(n)} | "
                   f"{len(live)} | {by} | {lo[0]:.1f}–{hi[0]:.1f} |")
    return "\n".join(out) + "\n"


BLOCKS = {'sensitivity-table': render_sensitivity, 'scope-table': render_scope}


def block_re(name):
    return re.compile(r'(<!-- GENERATED:' + re.escape(name) + r'[^>]*-->\n)(.*?)'
                      r'(<!-- /GENERATED:' + re.escape(name) + r' -->)', re.S)


if '--fill' in sys.argv[1:]:
    path = locate(SCRATCH_DOC)
    text = open(path, encoding='utf-8').read()
    for name, fn in BLOCKS.items():
        rx = block_re(name)
        if len(rx.findall(text)) != 1:
            sys.exit(f"ERROR: expected exactly one {name} block in {SCRATCH_DOC}")
        text = rx.sub(lambda m, fn=fn: m.group(1) + fn() + m.group(3), text)
    open(path, 'w', encoding='utf-8').write(text)
    print(f"Filled {len(BLOCKS)} generated blocks in {os.path.basename(path)}.")
    sys.exit(0)

RESULTS = []


def check(label, cond):
    RESULTS.append((label, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


print("=" * 92)
print("verify_qatar.py -- NEEC Step 1b, Session 21 (State Capitalism / Qatar)")
print("=" * 92)

# ---------------------------------------------------------------- (0)
print("\n(0) SOURCES")
canon_path = locate(CANON)
spec = importlib.util.spec_from_file_location("neec_v2", canon_path)
neec_v2 = importlib.util.module_from_spec(spec)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    spec.loader.exec_module(neec_v2)
    self_check = neec_v2.verify_transcription(verbose=False)
SCORES = neec_v2.SCORES
print(f"  Imported {len(SCORES)} canonical systems from {os.path.basename(canon_path)}")
check("Canonical script's own transcription self-check passes", self_check is True)
check("Canonical corpus holds exactly 20 systems", len(SCORES) == 20)
check("Qatar is not already in the canonical corpus", not any('Qatar' in k for k in SCORES))
check("Local tier() agrees with the canonical tier() for 0-26 failures",
      all(tier(n) == neec_v2.tier(n) for n in range(27)))
check("Local failure_count agrees with the canonical one on every corpus vector",
      all(len(fails(s)) == neec_v2.failure_count(s) for s in SCORES.values()))
pairs, mismatch = 0, 0
for a in SCORES:
    for b in SCORES:
        if a != b:
            mine, theirs = dominates(SCORES[a], SCORES[b]), bool(neec_v2.dominates(a, b))
            mismatch += int(mine != theirs)
            pairs += int(mine)
print(f"  Dominance helper validated on {len(SCORES) * (len(SCORES) - 1)} ordered pairs; "
      f"{pairs} are dominance pairs")
check("Vector-level dominance test agrees with the canonical helper on every ordered pair",
      mismatch == 0)
check("Canonical corpus has 11 ordered dominance pairs (Handoff 20)", pairs == 11)
doc_path = find(SCRATCH_DOC)
print(f"  Scratch document: {SCRATCH_DOC if doc_path else 'NOT FOUND'}")

# ---------------------------------------------------------------- (1)
print("\n(1) SELF-CONSISTENCY")
assert set(QA) == set(ALL_CRITS) and all(x in (0.0, 0.5, 1.0) for x in QA.values())
ds = dsums(QA)
for d, cs in DOMAINS.items():
    print(f"  {d} = {' + '.join(f'{QA[c]:.1f}' for c in cs)} = {ds[d]:.1f}/{DOMAIN_MAX[d]}")
    check(f"{d} equals stated {PUBLISHED[d]}", abs(ds[d] - PUBLISHED[d]) < 1e-9)
t, f = total(QA), fails(QA)
pct = round(t / 26 * 100)
print(f"  Total = {' + '.join(f'{ds[d]:.1f}' for d in DOMAINS)} = {t:.1f}/26 ({pct}%)")
check("Total equals stated 9.0/26 (35%)",
      abs(t - PUBLISHED['Total']) < 1e-9 and pct == PUBLISHED['Percent'])
check("Failure count equals stated 10", len(f) == PUBLISHED['Failures'])
check("Tier equals stated 'Structurally Inadequate'", tier(len(f)) == PUBLISHED['Tier'])
n1 = sum(QA[c] == 1.0 for c in ALL_CRITS)
nh = sum(QA[c] == 0.5 for c in ALL_CRITS)
print(f"  Distribution: {n1} at 1.0, {nh} at 0.5, {len(f)} at 0.0 -> "
      f"{n1}(1.0) + {nh}(0.5) = {n1 + 0.5 * nh:.1f}")
check("Distribution (2 / 14 / 10) re-derives the total",
      (n1, nh, len(f)) == (2, 14, 10) and abs(n1 + 0.5 * nh - t) < 1e-9)
check("The two Passes are exactly C5.1 and C5.3",
      {c for c in ALL_CRITS if QA[c] == 1.0} == PASSES)
print(f"  Failures: {f}")
check("Failures = 6 undisputed + 4 flagged upward",
      set(f) == UNDISPUTED_FAILURES | {c for c in FLAGGED if QA[c] == 0.0}
      and len(UNDISPUTED_FAILURES) == 6)
check("Every flagged alternative differs from its primary score by exactly 0.5",
      all(abs(alt - QA[c]) == 0.5 for c, (alt, _) in FLAGGED.items()))
check("Exactly one flagged call would create a failure (C1.2b)",
      {c for c, (alt, _) in FLAGGED.items() if alt == 0.0} == {'C1.2b'})
check("No flagged call disputes any of the six undisputed failures",
      not (UNDISPUTED_FAILURES & set(FLAGGED)))
check("Twelve flagged calls in total", len(FLAGGED) == 12)

# ---------------------------------------------------------------- (2)
print("\n(2) TRANSCRIPTION CHECK AGAINST THE SCRATCH DOCUMENT")
text = norm = None
if doc_path is None:
    print(f"  SKIPPED: {SCRATCH_DOC} not found beside this script or in working dirs.")
else:
    text = open(doc_path, encoding="utf-8").read()
    norm = re.sub(r'\s+', ' ', text)
    heads = list(re.finditer(r'^####\s+(' + CRIT_RE + r')\s([^\n]*)$', text, re.M))
    parsed = {}
    for i, m in enumerate(heads):
        sm = re.search(r':\s*(0\.0|0\.5|1\.0)\s*\(', m.group(2))
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[m.end():end]
        cut = re.search(r'^\*\*Domain [1-5] =', body, re.M)
        if cut:
            body = body[:cut.start()]
        parsed[m.group(1)] = (float(sm.group(1)) if sm else None,
                              'flagged as contestable' in m.group(2),
                              re.sub(r'\s+', ' ', body))
    check("Document has exactly one scored heading per criterion (26, no duplicates)",
          len(heads) == 26 and set(parsed) == set(ALL_CRITS)
          and all(v[0] is not None for v in parsed.values()))
    mism = [(c, parsed[c][0], QA[c]) for c in ALL_CRITS if c in parsed and parsed[c][0] != QA[c]]
    if mism:
        print(f"  Heading/vector mismatches: {mism}")
    check("Every heading score matches this script's vector", not mism)
    flagged_doc = {c for c, v in parsed.items() if v[1]}
    if flagged_doc != set(FLAGGED):
        print(f"  Flag mismatch: doc-only {in_order(flagged_doc - set(FLAGGED))}, "
              f"script-only {in_order(set(FLAGGED) - flagged_doc)}")
    check("Headings marked 'flagged as contestable' are exactly the twelve flagged calls",
          flagged_doc == set(FLAGGED))

    cons_re = re.compile(r'Consequence, checked: (\d+\.\d)/26 with (\d+) failures?; tier unchanged\.')
    bad = []
    for c in ALL_CRITS:
        found = cons_re.findall(parsed[c][2])
        if c in FLAGGED:
            v = moved(QA, {c: FLAGGED[c][0]})
            want = [(f"{total(v):.1f}", str(len(fails(v))))]
            if found != want or tier(len(fails(v))) != PUBLISHED['Tier']:
                bad.append((c, found, want))
        elif found:
            bad.append((c, found, []))
    if bad:
        print(f"  Inline-consequence mismatches: {bad}")
    check("Each flagged call states its consequence once and correctly; no other call states one",
          not bad)

    scope_re = re.compile(r'Citizens-only scenario: (\d\.\d)')
    bad = []
    for c in ALL_CRITS:
        found = scope_re.findall(parsed[c][2])
        want = [f"{CITIZENS_ONLY[c]:.1f}"] if c in CITIZENS_ONLY else []
        if found != want:
            bad.append((c, found, want))
    if bad:
        print(f"  Scope-statement mismatches: {bad}")
    check("Exactly the seven scope-moved criteria state their citizens-only score, each correct",
          not bad)

    dom_found = {}
    for m in re.finditer(r'^\*\*Domain ([1-5]) = ([0-9. +]+?) = (\d\.\d)/(\d) \((\d+)%\)\*\*$',
                         text, re.M):
        dom_found[f"D{m.group(1)}"] = ([float(x) for x in m.group(2).split('+')],
                                       float(m.group(3)), int(m.group(4)), int(m.group(5)))
    check("Document states all five domain-sum lines", set(dom_found) == set(DOMAINS))
    for d in DOMAINS:
        if d in dom_found:
            addends, stated, mx, p = dom_found[d]
            check(f"{d} line: addends in criterion order re-sum to {stated}/{mx} ({p}%)",
                  addends == [QA[c] for c in DOMAINS[d]] and abs(sum(addends) - stated) < 1e-9
                  and abs(stated - ds[d]) < 1e-9 and mx == DOMAIN_MAX[d]
                  and p == round(ds[d] / DOMAIN_MAX[d] * 100))

    listed = {}
    for m in re.finditer(r'^- ([A-Za-z ]+): (\d\.\d)/(\d) \((\d+)%\)$', text, re.M):
        listed[m.group(1)] = (float(m.group(2)), int(m.group(3)), int(m.group(4)))
    check("Summary Scores' five domain-total lines match, names and percentages included",
          set(listed) == set(DOMAIN_NAMES.values())
          and all(listed[DOMAIN_NAMES[d]]
                  == (ds[d], DOMAIN_MAX[d], round(ds[d] / DOMAIN_MAX[d] * 100)) for d in DOMAINS))
    om = re.search(r'\*\*Overall Score: (\d+\.\d)/26 \((\d+)%\)\*\*', text)
    check("Overall Score line states 9.0/26 (35%)",
          om is not None and float(om.group(1)) == t and int(om.group(2)) == pct)
    em = re.search(r'\*Explicit sum, per Appendix H\.4: ([0-9. +]+?) = (\d+\.\d)\.\*', text)
    check("Explicit-sum line lists the five domain totals in order and re-sums to the total",
          em is not None
          and [float(x) for x in em.group(1).split('+')] == [ds[d] for d in DOMAINS]
          and abs(float(em.group(2)) - t) < 1e-9)
    dm = re.search(r'Score distribution:\s*(\d+)\s+criteria\s+at\s+1\.0\s+\(([^)]*)\),\s+'
                   r'(\d+)\s+at\s+0\.5,\s+and\s+(\d+)\s+at\s+0\.0', text)
    check("Distribution line (2 / 14 / 10, Passes named) matches",
          dm is not None
          and (int(dm.group(1)), int(dm.group(3)), int(dm.group(4))) == (n1, nh, len(f))
          and set(re.findall(CRIT_RE, dm.group(2))) == PASSES)
    fm = re.search(r'\*\*Structural Failures:\*\*\s*(\d+)\s+criteria\s+at\s+0\.0\s+—\s+([^\n]+?)\.\s*$',
                   text, re.M)
    check("Failure line lists exactly the vector's ten failures, in criterion order",
          fm is not None and int(fm.group(1)) == len(f) and re.findall(CRIT_RE, fm.group(2)) == f)
    am = re.search(r'\*\*Adequacy:\*\* ([A-Za-z ]+?) \(', text)
    check("Adequacy line states the computed tier", am is not None and am.group(1) == tier(len(f)))

    for name, fn in BLOCKS.items():
        m = block_re(name).search(text)
        check(f"GENERATED block '{name}' matches a fresh render exactly",
              m is not None and m.group(2) == fn())

    row_re = re.compile(r'^\|\s*(' + CRIT_RE + r')\s*\|\s*(\d\.\d)\s*\|\s*(\d\.\d)\s*—[^|]*\|'
                        r'\s*(\d+\.\d)\s*\|\s*(\d+)\s*\|\s*([A-Za-z ]+?)\s*\|\s*$', re.M)
    rows = {m.group(1): m for m in row_re.finditer(text)}
    bad_rows = []
    for c, m in rows.items():
        v = moved(QA, {c: FLAGGED[c][0]})
        want = (QA[c], FLAGGED[c][0], total(v), len(fails(v)), tier(len(fails(v))))
        got = (float(m.group(2)), float(m.group(3)), float(m.group(4)),
               int(m.group(5)), m.group(6))
        if want != got:
            bad_rows.append((c, want, got))
    if bad_rows:
        print(f"  Sensitivity-table row mismatches: {bad_rows}")
    check("Sensitivity table: one row per flagged call, every cell re-computed",
          set(rows) == set(FLAGGED) and len(rows) == 12 and not bad_rows)

# ---------------------------------------------------------------- (3)
print("\n(3) CONTESTABLE-CALL SENSITIVITY (confirmed scope: all residents counted)")
print(f"  {'crit':7}{'primary':>8}{'alt':>6}{'total':>7}{'fails':>7}  {'tier':25}reading")
crossers = []
for c in LIVE_ALL:
    alt, label = FLAGGED[c]
    v = moved(QA, {c: alt})
    nf = len(fails(v))
    if tier(nf) != PUBLISHED['Tier']:
        crossers.append(c)
    print(f"  {c:7}{QA[c]:>8.1f}{alt:>6.1f}{total(v):>7.1f}{nf:>7}  {tier(nf):25}{label}")
check("No single flagged call, resolved alone, changes the tier", not crossers)
up = moved(QA, {c: a for c, (a, _) in FLAGGED.items() if a > QA[c]})
dn = moved(QA, {c: a for c, (a, _) in FLAGGED.items() if a < QA[c]})
print(f"\n  All upward readings together:   {describe(up)}")
print(f"  All downward readings together: {describe(dn)}")
check("Joint upward reading = 14.0/26 with 6 failures (still Structurally Inadequate)",
      abs(total(up) - 14.0) < 1e-9 and len(fails(up)) == 6
      and tier(len(fails(up))) == PUBLISHED['Tier'])
check("Joint downward reading = 8.0/26 with 11 failures",
      abs(total(dn) - 8.0) < 1e-9 and len(fails(dn)) == 11)
counts, lo, hi = enumerate_flags(QA, LIVE_ALL)
min_fails = min(len(fails(moved(QA, {c: FLAGGED[c][0] for c, b in zip(LIVE_ALL, bits) if b})))
                for bits in product((0, 1), repeat=len(LIVE_ALL)))
print(f"  Exhaustive enumeration over all {len(LIVE_ALL)} flagged calls: "
      f"{2 ** len(LIVE_ALL):,} combinations -> {counts}")
print(f"  Lowest {lo[0]:.1f}/26 ({lo[1]} failures); highest {hi[0]:.1f}/26 ({hi[1]} failures); "
      f"fewest failures in any combination: {min_fails}")
check("All 4,096 combinations are Structurally Inadequate",
      counts == {PUBLISHED['Tier']: 2 ** len(LIVE_ALL)})
check("Enumeration extremes equal the joint readings, a 6.0-point range",
      (lo[0], hi[0]) == (total(dn), total(up)) and abs(hi[0] - lo[0] - 6.0) < 1e-9)
check("The tier cannot move: six failures are undisputed, and six is the threshold",
      min_fails == len(UNDISPUTED_FAILURES) == 6
      and tier(6) == 'Structurally Inadequate' and tier(5) == 'Partially Adequate')
c54 = moved(QA, {'C5.4': 0.0})
print(f"  C5.4 read downward instead (0.0): {describe(c54)}")
check("A downward C5.4 reading adds a failure without changing the tier",
      len(fails(c54)) == len(f) + 1 and tier(len(fails(c54))) == PUBLISHED['Tier'])

# ---------------------------------------------------------------- (4)
print("\n(4) POPULATION SCOPE (citizens-only scenario)")
changed = [c for c in ALL_CRITS if CIT[c] != QA[c]]
print(f"  Criteria moved: {[(c, QA[c], CIT[c]) for c in changed]}")
check("Scenario moves exactly the seven criteria the document lists",
      changed == in_order(CITIZENS_ONLY))
print(f"  Citizens-only alone: {describe(CIT)}")
check("Citizens-only reading = 13.0/26 with 6 failures (Structurally Inadequate, at the boundary)",
      abs(total(CIT) - 13.0) < 1e-9 and len(fails(CIT)) == 6)
check("It raises the total by exactly 4.0 points", abs(total(CIT) - t - 4.0) < 1e-9)
check("The scope itself sets four flagged criteria (C1.1, C1.2a, C1.5, C2.1), leaving eight",
      SCOPE_SET_FLAGS == ['C1.1', 'C1.2a', 'C1.5', 'C2.1'] and len(LIVE_CIT) == 8)
ccounts, clo, chi = enumerate_flags(CIT, LIVE_CIT)
print(f"  Enumeration over the eight remaining flagged calls: "
      f"{2 ** len(LIVE_CIT)} combinations -> {ccounts}")
print(f"  Lowest {clo[0]:.1f}/26 ({clo[1]} failures); highest {chi[0]:.1f}/26 ({chi[1]} failures)")
check("128 of 256 combinations reach Partially Adequate; none reaches Potentially Adequate",
      ccounts.get('Partially Adequate') == 128
      and ccounts.get('Structurally Inadequate') == 128
      and 'Potentially Adequate' not in ccounts)
check("Citizens-only totals run from 12.0 to 16.0", (clo[0], chi[0]) == (12.0, 16.0))
check("The population scope is the only tier-relevant choice in this evaluation",
      counts == {PUBLISHED['Tier']: 4096} and 'Partially Adequate' in ccounts)

# ---------------------------------------------------------------- (5)
print("\n(5) CORPUS COMPARISON")
pros = dict(SCORES)
pros[QA_NAME] = QA
SWF, CN, SG = SCORES[SWF_NAME], SCORES[CN_NAME], SCORES[SG_NAME]
LM = key_like(SCORES, 'Libertarian')
SQ = key_like(SCORES, 'Status Quo')
FALC = key_like(SCORES, 'Fully Automated')
ties = [n for n, s in SCORES.items() if abs(total(s) - t) < 1e-9]
above = [n for n, s in SCORES.items() if total(s) > t]
below = [n for n, s in SCORES.items() if total(s) < t]
rank = len(above) + 1
print(f"  At 9.0/26: {len(above)} systems above, {len(below)} below; ties: {ties or 'none'}")
check("Rank 20 of 21 in the prospective corpus, with no exact tie",
      rank == 20 and len(pros) == 21 and not ties)
check("Only Libertarian Minarchism scores lower (8.0/26)",
      below == [LM] and abs(total(SCORES[LM]) - 8.0) < 1e-9)
dom_by = [n for n, s in SCORES.items() if dominates(s, QA)]
dom_over = [n for n, s in SCORES.items() if dominates(QA, s)]
print(f"  Dominated by: {dom_by or 'none'}; dominates: {dom_over or 'none'}")
check("Dominated by exactly CCO-PTF-CIP-SZH and Singapore; dominates nothing",
      dom_by == [CCO_NAME, SG_NAME] and dom_over == [])
pros_pairs = [(a, b) for a in pros for b in pros if a != b and dominates(pros[a], pros[b])]
non_cco = [(a, b) for a, b in pros_pairs if CCO_NAME not in (a, b)]
print(f"  Prospective corpus: {len(pros_pairs)} ordered dominance pairs; "
      f"without CCO-PTF-CIP-SZH: {non_cco}")
check("Insertion takes the corpus from 11 to 13 ordered dominance pairs",
      pairs == 11 and len(pros_pairs) == 13)
check("The two pairs not involving CCO are Singapore over China and Singapore over Qatar",
      non_cco == [(SG_NAME, CN_NAME), (SG_NAME, QA_NAME)])


def compare(name, other):
    diff = [c for c in ALL_CRITS if other[c] != QA[c]]
    higher = [c for c in diff if QA[c] > other[c]]
    lower = [c for c in diff if QA[c] < other[c]]
    dd = [ds[d] - dsums(other)[d] for d in DOMAINS]
    print(f"  vs {name}: {total(other):.1f}/26, {len(fails(other))} failures; "
          f"differ on {len(diff)}; Qatar higher on {higher or 'none'}, "
          f"lower on {len(lower)}; deltas {deltas_str(dd)}")
    return diff, higher, lower, dd


d_swf, h_swf, l_swf, dd_swf = compare(SWF_NAME, SWF)
check("vs SWF Statism: 12 criteria differ, Qatar higher only on C1.3, shared failures C4.2 and C4.5",
      len(d_swf) == 12 and h_swf == ['C1.3']
      and in_order(set(f) & set(fails(SWF))) == ['C4.2', 'C4.5'])
check("vs SWF Statism: 5.0 points and 7 failures apart, deltas +0.0 / -2.0 / -1.0 / -1.5 / -0.5",
      abs(total(SWF) - t - 5.0) < 1e-9 and len(f) - len(fails(SWF)) == 7
      and [round(x, 1) for x in dd_swf] == [0.0, -2.0, -1.0, -1.5, -0.5])
d_sg, h_sg, l_sg, dd_sg = compare(SG_NAME, SG)
check("Singapore strictly dominates Qatar: higher on 10 criteria, lower on none",
      dominates(SG, QA) and len(l_sg) == 10 and h_sg == [])
check("vs Singapore: deltas -1.5 / -1.0 / -1.5 / -0.5 / -0.5, and Singapore's 4 failures are a subset",
      [round(x, 1) for x in dd_sg] == [-1.5, -1.0, -1.5, -0.5, -0.5]
      and set(fails(SG)) < set(f) and len(fails(SG)) == 4)
d_cn, h_cn, l_cn, dd_cn = compare(CN_NAME, CN)
check("Neither China nor Qatar dominates the other",
      not dominates(CN, QA) and not dominates(QA, CN))
check("vs China: only 4 criteria differ (Qatar higher on C5.3; lower on C1.5, C3.2, C5.5)",
      len(d_cn) == 4 and h_cn == ['C5.3'] and l_cn == ['C1.5', 'C3.2', 'C5.5'])
check("China's 8 failures are a subset of Qatar's 10, and China's total is higher by 1.0",
      set(fails(CN)) < set(f) and len(fails(CN)) == 8 and abs(total(CN) - t - 1.0) < 1e-9)
d4 = sorted(((dsums(s)['D4'], n) for n, s in pros.items()), key=lambda x: (x[0], x[1]))
print(f"  Lowest Domain 4 totals: {d4[:4]}")
check("Qatar's Domain 4 (0.5) ties China and Status Quo for the corpus's lowest",
      d4[0][0] == 0.5 and {n for v, n in d4 if v == 0.5} == {QA_NAME, CN_NAME, SQ})
check("Four of Domain 4's five criteria are failures, none of them flagged",
      sum(QA[c] == 0.0 for c in DOMAINS['D4']) == 4
      and not [c for c in DOMAINS['D4'] if QA[c] == 0.0 and c in FLAGGED])
cohort = {n: SCORES[n] for n in (SWF_NAME, CN_NAME, SG_NAME)}
for frag in ('Georgism', 'Mutual Credit', 'Doughnut', 'Universal Basic Services'):
    k = key_like(SCORES, frag)
    cohort[k] = SCORES[k]
cohort[QA_NAME] = QA
print("  Step 1b cohort totals: "
      + "; ".join(f"{n.split(' (')[0]} {total(s):.1f}/{len(fails(s))}f" for n, s in cohort.items()))
check("Qatar has the lowest total and the most failures of the eight Step 1b systems",
      len(cohort) == 8 and all(total(s) > t for n, s in cohort.items() if n != QA_NAME)
      and all(len(fails(s)) < len(f) for n, s in cohort.items() if n != QA_NAME))
at14 = [n for n, s in SCORES.items() if abs(total(s) - total(up)) < 1e-9]
check("The joint upward total (14.0) is SWF Statism's and Singapore's, both Partially Adequate",
      set(at14) == {SWF_NAME, SG_NAME}
      and all(tier(len(fails(SCORES[n]))) == 'Partially Adequate' for n in at14))
at13 = [n for n, s in SCORES.items() if abs(total(s) - total(CIT)) < 1e-9]
check("Only Fully Automated Luxury Communism scores 13.0, the citizens-only total", at13 == [FALC])
arch = ((CN_NAME, CN), (SG_NAME, SG), (QA_NAME, QA))
print("  Configured national political economies: "
      + "; ".join(f"{n}: {describe(s)}" for n, s in arch))
check("The three configured national political economies span two tiers",
      len({tier(len(fails(s))) for _, s in arch}) == 2)

# ---------------------------------------------------------------- (6)
print("\n(6) STATED NUMBERS (rebuilt here, then matched verbatim in the document)")
if norm is None:
    print("  SKIPPED: document not found.")
else:
    oil_share = BUDGET_OIL / BUDGET_TOTAL * 100
    monthly = WEALTH_BAR / (YEARS * 12)
    lng_share = LNG_LOST / LNG_CAPACITY * 100
    q1_fall = (Q1_OIL_2025 - Q1_OIL_2026) / Q1_OIL_2025 * 100
    stress_mult = round(CPI_PEAK_2008 / CPI_STRESS_BOUND)
    und = in_order(UNDISPUTED_FAILURES)
    ff = in_order([c for c in FLAGGED if QA[c] == 0.0])
    dmap = dict(zip(DOMAINS, dd_swf))
    worst2 = [d for d in DOMAINS if d in sorted(DOMAINS, key=lambda x: dmap[x])[:2]]
    check("Citizen-share range brackets the secondary estimates (10.5% and 11.6%)",
          100 - MIGRANT_SHARE_HRW <= 10.5 <= CITIZEN_SHARE_HIGH
          and 100 - MIGRANT_SHARE_HRW <= 11.6 <= CITIZEN_SHARE_HIGH)
    check("Long-run inflation average exceeds the 3% threshold", CPI_LONG_RUN > 3.0)
    check("Planned LNG capacity is a near-doubling, not a doubling",
          1.5 < LNG_PLANNED / LNG_CAPACITY < 2.0)
    CLAIMS = [
        ("oil and gas share of 2026 budget revenue",
         f"QAR {BUDGET_OIL} billion of the QAR {BUDGET_TOTAL} billion in budgeted 2026 revenue, "
         f"{oil_share:.1f}%"),
        ("LNG capacity and expansion",
         f"{LNG_CAPACITY} million tonnes a year of capacity and plans to reach "
         f"{LNG_PLANNED} million by 2030"),
        ("C1.2a savings arithmetic",
         f"Accumulating ${WEALTH_BAR:,} over twenty years takes ${monthly:.0f} a month, about "
         f"{round(monthly / MIN_WAGE_USD * 100)}% of the US${MIN_WAGE_USD} basic minimum wage"),
        ("share of LNG capacity lost",
         f"That is {LNG_LOST} of {LNG_CAPACITY} million tonnes a year, {lng_share:.1f}% (computed), "
         f"consistent with the roughly {round(lng_share)}% reported"),
        ("first-quarter 2026 revenue fall", f"a {q1_fall:.1f}% fall"),
        ("2008 inflation against the stress bound",
         f"the 2008 peak was about {NUM[stress_mult]} times the {CPI_STRESS_BOUND}% stress bound"),
        ("citizen share range", f"roughly {100 - MIGRANT_SHARE_HRW}–{CITIZEN_SHARE_HIGH}%"),
        ("undisputed failures",
         f"{NUM[len(und)].capitalize()} failures ({', '.join(und)}) are disputed by no flagged call"),
        ("threshold restated",
         f"and {NUM[6]} failures is itself the Structurally Inadequate threshold"),
        ("flagged failures",
         f"{NUM[len(ff)].capitalize()} failures are flagged upward ({', '.join(ff)}), and "
         f"{NUM[1]} flagged call would add a failure (C1.2b)"),
        ("full enumeration",
         f"all {2 ** len(LIVE_ALL):,} combinations of the {NUM[len(LIVE_ALL)]} flagged calls "
         f"are Structurally Inadequate"),
        ("joint upward reading",
         f"All upward readings together give {total(up):.1f}/26 with {len(fails(up))} failures"),
        ("joint downward reading",
         f"all downward readings together give {total(dn):.1f}/26 with {len(fails(dn))} failures"),
        ("upward extreme against two canonical systems",
         f"The upward extreme reaches the same {total(up):.1f}/26 as Sovereign Wealth Fund "
         f"Statism and Singapore, in a different tier"),
        ("range of flagged totals",
         f"move the total over a {NUM[int(hi[0] - lo[0])]}-point range but never the tier"),
        ("scope criteria moved",
         f"Counting citizens only changes {NUM[len(changed)]} criteria ({lst(changed)})"),
        ("scope total", f"gives {total(CIT):.1f}/26 with {len(fails(CIT))} failures"),
        ("scope tie", f"it ties Fully Automated Luxury Communism at {total(CIT):.1f}/26"),
        ("flags set by the scope",
         f"The scope itself sets {NUM[len(SCOPE_SET_FLAGS)]} flagged criteria ({lst(SCOPE_SET_FLAGS)})"),
        ("scope enumeration",
         f"Of the {2 ** len(LIVE_CIT)} combinations of the {NUM[len(LIVE_CIT)]} flagged calls it "
         f"leaves open, {ccounts['Partially Adequate']} reach Partially Adequate and none reaches "
         f"Potentially Adequate; totals run from {clo[0]:.1f} to {chi[0]:.1f}"),
        ("scope point gain", f"only raises the total by {total(CIT) - t:.1f} points"),
        ("Domain 4 lowest in corpus",
         f"Domain 4 ({ds['D4']:.1f}/5) ties China and Status Quo Market Capitalism for the "
         f"lowest in the corpus"),
        ("Domain 4 failures",
         f"{NUM[4].capitalize()} of its five criteria are structural failures, none of them flagged"),
        ("Step 1b cohort position",
         f"Qatar has the lowest total ({t:.1f}/26) and the most failures ({len(f)}) of the "
         f"{NUM[len(cohort)]} Step 1b systems"),
        ("mechanism against configuration",
         f"stands at {total(SWF):.1f}/26 with {len(fails(SWF))} failures against {t:.1f}/26 with "
         f"{len(f)}: a difference of {total(SWF) - t:.1f} points and {len(f) - len(fails(SWF))} failures"),
        ("SWF differences",
         f"The two differ on {len(d_swf)} criteria, and Qatar is higher on only "
         f"{NUM[len(h_swf)]}, {', '.join(h_swf)}"),
        ("SWF shared failures",
         f"They share {NUM[2]} failures, {lst(in_order(set(f) & set(fails(SWF))))}"),
        ("SWF domain deltas",
         f"The domain deltas (Qatar minus Sovereign Wealth Fund Statism) are {deltas_str(dd_swf)}"),
        ("SWF worst domains", f"costs most in {lst([DOMAIN_NAMES[d] for d in worst2])}"),
        ("Singapore dominance",
         f"Singapore strictly dominates Qatar: it is higher on {len(l_sg)} criteria and lower on none"),
        ("Singapore domain deltas",
         f"the domain deltas (Qatar minus Singapore) are {deltas_str(dd_sg)}"),
        ("Singapore failure subset",
         f"Singapore's {len(fails(SG))} failures are a subset of Qatar's {len(f)}"),
        ("China non-dominance", "Neither China nor Qatar dominates the other"),
        ("China differences",
         f"China and Qatar differ on only {len(d_cn)} criteria: Qatar is higher on {lst(h_cn)} "
         f"and lower on {lst(l_cn)}"),
        ("China failure subset and total",
         f"China's {len(fails(CN))} failures are a subset of Qatar's {len(f)}, and China's total "
         f"is higher by {total(CN) - t:.1f} point"),
        ("prospective corpus size", f"In a prospective {len(pros)}-system corpus"),
        ("rank",
         f"rank {ordinal(rank)} of {len(pros)}, above only Libertarian Minarchism "
         f"({total(SCORES[LM]):.1f}/26), with no exact tie"),
        ("dominance summary",
         f"It is dominated by {lst([CCO_NAME, SG_NAME])}, and dominates no system"),
        ("dominance pair count", f"from {pairs} to {len(pros_pairs)} ordered pairs"),
        ("non-CCO dominance pairs",
         " and ".join(f"{a.replace('State Capitalism / ', '')} over "
                      f"{b.replace('State Capitalism / ', '')}" for a, b in non_cco)),
        ("archetype tiers",
         f"now span two tiers: China ({total(CN):.1f}/26, {tier(len(fails(CN)))}), Singapore "
         f"({total(SG):.1f}/26, {tier(len(fails(SG)))}), and Qatar ({t:.1f}/26, {tier(len(f))})"),
        ("C5.4 downward reading",
         f"it would add a failure but, with {NUM[len(f)]} already, could not change the tier"),
    ]
    missing = [(lbl, phrase) for lbl, phrase in CLAIMS if phrase not in norm]
    for lbl, phrase in missing:
        print(f"  MISSING [{lbl}]: {phrase!r}")
    print(f"  {len(CLAIMS)} rebuilt phrases checked against the document text")
    check(f"Every one of the {len(CLAIMS)} rebuilt numeric claims appears verbatim in the document",
          not missing)

# ----------------------------------------------------------------------------
print("\n" + "=" * 92)
bad = [lbl for lbl, ok in RESULTS if not ok]
print(f"SUMMARY: {len(RESULTS) - len(bad)}/{len(RESULTS)} checks pass.")
if bad:
    for lbl in bad:
        print(f"  FAILED: {lbl}")
    sys.exit(1)
print("ALL CHECKS PASS. Nothing is inserted anywhere (scratch-before-insert discipline);")
print("this verifies the scratch document's arithmetic, its transcription, its generated")
print("tables, its twelve flagged calls, the confirmed population scope and its scenario,")
print("and every comparative claim against the real canonical 20-system corpus.")
