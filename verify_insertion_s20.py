#!/usr/bin/env python3
"""
verify_insertion_s20.py -- NEEC Session 20: verification of the consolidated
insertion of Sovereign Wealth Fund Statism, State Capitalism / China, and
State Capitalism / Singapore into the canonical files (17 -> 20 systems).

Five check groups:
  (1) Sources: the three vectors, and the domain totals their scratch
      documents state, are AST-extracted (never executed) from verify_swf.py,
      verify_china.py, and verify_singapore.py, and re-summed.
  (2) Canonical script: the live neec_weighting_robustness_analysis_v2.py is
      imported and self-verified (transcription and legacy checks); its three
      new vectors must EQUAL the extracted ones, and its 17 earlier systems,
      key order, schemes, and legacy totals must equal the pinned Session 16
      snapshot's.
  (3) CSV: the live builder is re-run in a scratch directory and must
      reproduce the live neec_scores.csv byte for byte; the header and first
      17 rows must be byte-identical to the Session 16 CSV; the three new
      rows must carry the confirmed display names and the computed values.
  (4) Generator: insert_session20.py, re-run on the pinned inputs, must
      reproduce both live scripts byte for byte.
  (5) The 20-system corpus: every comparative claim in the three new CSV
      rows is recomputed, along with tiers, ties, and the Pareto frontier;
      reference tables for the Step 5 regeneration are printed.

PORTABILITY: files are looked up beside this script first, then in the
working directory and the conventional working locations; only file names
are printed, so the captured output reproduces from any directory.
"""

import ast
import csv
import hashlib
import importlib.util
import io
import os
import shutil
import subprocess
import sys
import tempfile
from itertools import combinations, product

HERE = os.path.dirname(os.path.abspath(__file__))
SEARCH_DIRS = (HERE, os.getcwd(), "/home/claude", "/home/claude/neec",
               "/mnt/user-data/outputs", "/mnt/project")

CANON = "neec_weighting_robustness_analysis_v2.py"
CANON_S16 = "neec_weighting_robustness_analysis_v2_s16_snapshot.py"
BUILDER = "neec_scores_csv_builder_v2.py"
BUILDER_S16 = "neec_scores_csv_builder_v2_s16_snapshot.py"
CSV_LIVE = "neec_scores.csv"
CSV_S16 = "neec_scores_s16_snapshot.csv"
GENERATOR = "insert_session20.py"
BASELINE = "baseline_weighting_script.py"
PINNED = {CANON_S16: "1f2c9cd207fa67e0fda1931985311454",
          BUILDER_S16: "ee48e609a1da9c5350b34f3fa67d3a69",
          CSV_S16: "a58d431874f0734afab28f0882734c5e"}


def locate(name):
    for d in SEARCH_DIRS:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    sys.exit(f"ERROR: could not locate {name} in {SEARCH_DIRS}")


def md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def module_literal(path, var):
    tree = ast.parse(open(path, encoding="utf-8").read())
    hits = [ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
            and any(getattr(t, "id", None) == var for t in n.targets)]
    assert len(hits) == 1, f"{var}: {len(hits)} module-level assignments in {os.path.basename(path)}"
    return hits[0]


def load(path, modname):
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


RESULTS = []


def check(label, cond):
    RESULTS.append((label, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


ALL = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5'] + \
      [f'C{d}.{i}' for d in range(2, 6) for i in range(1, 6)]
DOM = {'D1': ALL[:6], 'D2': ALL[6:11], 'D3': ALL[11:16], 'D4': ALL[16:21], 'D5': ALL[21:]}
TIERS = ('Potentially Adequate', 'Partially Adequate', 'Structurally Inadequate')
WEALTH = ('C1.2a', 'C1.2b', 'C1.5')
SWF, CN, SG, CCO = ('Sovereign Wealth Fund Statism', 'State Capitalism / China',
                    'State Capitalism / Singapore', 'CCO-PTF-CIP-SZH')
NEW = (SWF, CN, SG)
DISPLAY = {SWF: 'Sovereign Wealth Fund Statism',
           CN: 'State Capitalism / China (Party-State-Directed Market Economy)',
           SG: 'State Capitalism / Singapore (GLC Developmental Capitalism)'}
SOURCES = {SWF: ('verify_swf.py', 'SWF', 'SWF_PUBLISHED'),
           CN: ('verify_china.py', 'CHINA', 'PUBLISHED'),
           SG: ('verify_singapore.py', 'SG', 'PUBLISHED')}
# Step 1b systems in scoring order (Sessions 6, 7, 14, 15, 17, 18, 19).
STEP1B = ('Georgism / Land Value Tax', 'Mutual Credit / LETS', 'Doughnut Economics',
          'Universal Basic Services', SWF, CN, SG)


def total(v):
    return sum(v[c] for c in ALL)


def dsum(v, d):
    return sum(v[c] for c in DOM[d])


def fails(v):
    return [c for c in ALL if v[c] == 0.0]


def tier(n):
    return TIERS[0] if n <= 2 else TIERS[1] if n <= 5 else TIERS[2]


def dominates(a, b):
    return all(a[c] >= b[c] for c in ALL) and any(a[c] > b[c] for c in ALL)


def moved(v, changes):
    out = dict(v)
    out.update(changes)
    return out


def frontier(corpus):
    return [a for a in corpus if not any(dominates(corpus[b], corpus[a]) for b in corpus if b != a)]


print("=" * 92)
print("verify_insertion_s20.py -- NEEC Session 20 consolidated insertion (17 -> 20 systems)")
print("=" * 92)

# ---------------------------------------------------------------------------- (1)
print("\n(1) SOURCES: vectors AST-extracted from the Step 1b verification scripts")
EXTRACTED, STATED = {}, {}
for name, (fname, vvar, pvar) in SOURCES.items():
    path = locate(fname)
    v, p = module_literal(path, vvar), module_literal(path, pvar)
    EXTRACTED[name], STATED[name] = v, p
    ok = (list(v) == ALL and all(x in (0.0, 0.5, 1.0) for x in v.values())
          and all(abs(dsum(v, d) - p[d]) < 1e-9 for d in DOM) and abs(total(v) - p['Total']) < 1e-9)
    print(f"  {name:<30} <- {fname:<20} {total(v):.1f}/26, {len(fails(v))} failures")
    check(f"{vvar} is a 26-criterion vector that re-sums to {pvar} in {fname}", ok)

# ---------------------------------------------------------------------------- (2)
print("\n(2) CANONICAL SCRIPT: live file vs extracted vectors and the Session 16 snapshot")
for name, digest in PINNED.items():
    check(f"{name} is the pinned Session 16 file (md5 {digest[:8]}...)", md5(locate(name)) == digest)
live = load(locate(CANON), "neec_live")
s16 = load(locate(CANON_S16), "neec_s16")
check("verify_transcription() passes for all 20 systems", live.verify_transcription(verbose=False))
check("verify_unchanged_from_legacy() passes (13 retrofitted systems)",
      live.verify_unchanged_from_legacy(locate(BASELINE), verbose=False))
S = live.SCORES
check("Canonical SCORES holds exactly 20 systems", len(S) == 20)
check("Key order: the 17 snapshot systems, then SWF Statism, China, Singapore",
      list(S) == list(s16.SCORES) + list(NEW))
check("PUBLISHED has the same 20 keys in the same order", list(live.PUBLISHED) == list(S))
check("All 17 earlier vectors are identical to the snapshot's",
      all(S[k] == s16.SCORES[k] for k in s16.SCORES))
check("All 17 earlier PUBLISHED entries are identical to the snapshot's",
      all(live.PUBLISHED[k] == s16.PUBLISHED[k] for k in s16.PUBLISHED))
for name in NEW:
    check(f"{name}: canonical vector == extracted vector (exact)", S[name] == EXTRACTED[name])
    check(f"{name}: canonical PUBLISHED == stated domain totals and total",
          live.PUBLISHED[name] == {k: STATED[name][k] for k in ('D1', 'D2', 'D3', 'D4', 'D5', 'Total')})
check("ALL_CRITS, D1_CRITS, D5_CRITS, and PUBLISHED_LEGACY_25 unchanged",
      live.ALL_CRITS == s16.ALL_CRITS == ALL and live.D1_CRITS == s16.D1_CRITS
      and live.D5_CRITS == s16.D5_CRITS and live.PUBLISHED_LEGACY_25 == s16.PUBLISHED_LEGACY_25)
check("The four weighting schemes are unchanged", live.SCHEMES == s16.SCHEMES)

# ---------------------------------------------------------------------------- (3)
print("\n(3) CSV: regenerated by the live builder; prefix identical to the Session 16 CSV")
with tempfile.TemporaryDirectory() as tmp:
    shutil.copy(locate(CANON), os.path.join(tmp, CANON))
    shutil.copy(locate(BUILDER), os.path.join(tmp, BUILDER))
    run = subprocess.run([sys.executable, BUILDER], cwd=tmp, capture_output=True, text=True)
    check("Live builder runs cleanly (its own cross-validation passes)",
          run.returncode == 0 and "Cross-validation PASSED: all 20 systems" in run.stdout)
    regenerated = open(os.path.join(tmp, "neec_scores.csv"), "rb").read() if run.returncode == 0 else b""
live_csv = open(locate(CSV_LIVE), "rb").read()
old_csv = open(locate(CSV_S16), "rb").read()
check("Regenerated CSV is byte-identical to the live neec_scores.csv", regenerated == live_csv)
new_lines, old_lines = live_csv.split(b"\r\n"), old_csv.split(b"\r\n")
check("Header and first 17 rows byte-identical to the Session 16 CSV",
      len(old_lines) == 19 and old_lines[-1] == b"" and new_lines[:18] == old_lines[:18])
rows = list(csv.reader(io.StringIO(live_csv.decode("utf-8"))))
check("CSV has a header plus exactly 20 rows", len(rows) == 21)
builder = open(locate(BUILDER), encoding="utf-8").read()
names_map = ast.literal_eval(builder.split("csv_names_to_published = ", 1)[1].split("\n}\n", 1)[0] + "\n}")
for name, row in zip(NEW, rows[18:]):
    v = S[name]
    n = len(fails(v))
    expected = [DISPLAY[name], '26', '6.0'] + [f"{dsum(v, d):.1f}" for d in DOM] + \
               [f"{total(v):.1f}", f"{round(total(v) / 26 * 100)}%", str(n), tier(n)]
    check(f"Row '{DISPLAY[name][:44]}': fields match the vector", row[:12] == expected)
    check(f"Builder maps that display name to the key '{name}'", names_map.get(DISPLAY[name]) == name)
check("Builder name map covers all 20 systems, one-to-one",
      len(names_map) == 20 and sorted(names_map.values()) == sorted(S))

# ---------------------------------------------------------------------------- (4)
print("\n(4) GENERATOR: insert_session20.py reproduces both live scripts")
with tempfile.TemporaryDirectory() as tmp:
    src, out = os.path.join(tmp, "src"), os.path.join(tmp, "out")
    os.makedirs(src)
    for fname in (CANON_S16, BUILDER_S16, "verify_swf.py", "verify_china.py", "verify_singapore.py"):
        shutil.copy(locate(fname), os.path.join(src, fname))
    gen = subprocess.run([sys.executable, locate(GENERATOR), src, out], capture_output=True, text=True)
    check("Generator runs cleanly on the pinned inputs", gen.returncode == 0)
    for fname in (CANON, BUILDER):
        p = os.path.join(out, fname)
        same = os.path.isfile(p) and open(p, "rb").read() == open(locate(fname), "rb").read()
        check(f"Generated {fname} is byte-identical to the live file", same)

# ---------------------------------------------------------------------------- (5)
print("\n(5) THE 20-SYSTEM CORPUS: every comparative claim in the new rows")
F = {k: fails(v) for k, v in S.items()}
dom_by = {n: [k for k in S if k != n and dominates(S[k], S[n])] for n in NEW}
dom_over = {n: [k for k in S if k != n and dominates(S[n], S[k])] for n in NEW}
for n in NEW:
    print(f"  {n:<30} {total(S[n]):.1f}/26  failures {F[n]}")
    print(f"  {'':<30} dominated by {dom_by[n] or 'none'}; dominates {dom_over[n] or 'none'}")

print("\n  -- Sovereign Wealth Fund Statism --")
check("Failures are exactly C1.3, C4.2, C4.5", F[SWF] == ['C1.3', 'C4.2', 'C4.5'])
early = STEP1B[:4]
check("No wealth-cluster failure; each of the four earlier Step 1b systems has at least one",
      all(S[SWF][c] > 0 for c in WEALTH) and all(any(S[k][c] == 0 for c in WEALTH) for k in early))
alt = moved(S[SWF], {'C1.2a': 0.0, 'C1.5': 0.0})
check("Flagged C1.2a/C1.5 read at 0.0: 13.0/26, 5 failures, still Partially Adequate",
      total(alt) == 13.0 and len(fails(alt)) == 5 and tier(5) == tier(len(F[SWF])))
check("Dominated only by CCO-PTF-CIP-SZH; dominates no system",
      dom_by[SWF] == [CCO] and dom_over[SWF] == [])

print("\n  -- The SWF Statism / Singapore tie --")
diff = [c for c in ALL if S[SWF][c] != S[SG][c]]
check("Exact tie at 14.0/26, and no other system at 14.0",
      total(S[SWF]) == total(S[SG]) == 14.0 and [k for k in S if total(S[k]) == 14.0] == [SWF, SG])
check("Same tier (Partially Adequate), failure counts 3 and 4",
      len(F[SWF]) == 3 and len(F[SG]) == 4 and tier(3) == tier(4) == TIERS[1])
check("Vectors differ on exactly 7 criteria and share failures C4.2 and C4.5",
      len(diff) == 7 and set(F[SWF]) & set(F[SG]) == {'C4.2', 'C4.5'})

print("\n  -- State Capitalism / China --")
cflag = module_literal(locate("verify_china.py"), 'FLAGGED')
check("Failures are exactly C2.1, C2.2, C2.4, C3.5, C4.2, C4.3, C4.4, C4.5",
      F[CN] == ['C2.1', 'C2.2', 'C2.4', 'C3.5', 'C4.2', 'C4.3', 'C4.4', 'C4.5'])
trio = ['C3.5', 'C4.2', 'C4.3']
failing_flags = sorted(c for c in cflag if S[CN][c] == 0.0)
check("The flagged failures are exactly C3.5, C4.2, C4.3 (5 undisputed)",
      failing_flags == trio and len(F[CN]) - len(trio) == 5)
rule = True
for states in product((0.0, 0.5), repeat=3):
    v = moved(S[CN], dict(zip(trio, states)))
    expect = TIERS[1] if all(x == 0.5 for x in states) else TIERS[2]
    rule = rule and tier(len(fails(v))) == expect
check("Structurally Inadequate unless all three read upward; all three up = 5 failures",
      rule and len(fails(moved(S[CN], {c: 0.5 for c in trio}))) == 5)
cup = moved(S[CN], {c: a for c, (a, _) in cflag.items() if a > S[CN][c]})
check("All nine flagged calls read upward: 13.0/26, 5 failures", total(cup) == 13.0 and len(fails(cup)) == 5)
check("Domain 1 is 3.0/6 with no Domain 1 failure",
      dsum(S[CN], 'D1') == 3.0 and not any(c in DOM['D1'] for c in F[CN]))
d4 = {k: dsum(v, 'D4') for k, v in S.items()}
d2 = {k: dsum(v, 'D2') for k, v in S.items()}
check("Domain 4 (0.5) ties Status Quo for the corpus's lowest",
      min(d4.values()) == 0.5 and sorted(k for k in S if d4[k] == 0.5) == sorted([CN, 'Status Quo Market Capitalism']))
check("Domain 2 (1.0) is second-lowest, above only Centrally Planned Socialism",
      [k for k in S if d2[k] < 1.0] == ['Centrally Planned Socialism'] and [k for k in S if d2[k] == 1.0] == [CN])
tied10 = [k for k in S if total(S[k]) == 10.0]
check("Three-way tie at 10.0 with CPS and Stakeholder; failures 8, 12, 9; one tier",
      sorted(tied10) == sorted(['Centrally Planned Socialism', 'Stakeholder Capitalism', CN])
      and [len(F[k]) for k in (CN, 'Centrally Planned Socialism', 'Stakeholder Capitalism')] == [8, 12, 9]
      and {tier(len(F[k])) for k in tied10} == {TIERS[2]})
check("Dominated by exactly CCO-PTF-CIP-SZH and Singapore; dominates no system",
      dom_by[CN] == [CCO, SG] and dom_over[CN] == [])

print("\n  -- State Capitalism / Singapore --")
sp = locate("verify_singapore.py")
sflag = module_literal(sp, 'FLAGGED')
check("Failures are exactly C2.2, C4.2, C4.4, C4.5", F[SG] == ['C2.2', 'C4.2', 'C4.4', 'C4.5'])
scope = moved(S[SG], module_literal(sp, 'RESIDENT_ONLY'))
check("Citizen-and-PR-only scope: C1.5 -> 1.0, C4.5 -> 0.5; 15.0/26, 3 failures, same tier",
      scope['C1.5'] == 1.0 and scope['C4.5'] == 0.5 and total(scope) == 15.0
      and len(fails(scope)) == 3 and tier(3) == TIERS[1])
up_fl = sorted(c for c in sflag if S[SG][c] == 0.0)
down_fl = sorted(c for c, (a, _) in sflag.items() if a == 0.0)
check("No flagged call on C2.2 or C4.5; C4.2, C4.4 flagged upward; C2.1, C2.4, C3.5, C4.3 downward",
      'C2.2' not in sflag and 'C4.5' not in sflag and up_fl == ['C4.2', 'C4.4']
      and down_fl == ['C2.1', 'C2.4', 'C3.5', 'C4.3'])
six = up_fl + down_fl
ok, seen = True, set()
for states in product((0.0, 0.5), repeat=6):
    j = states.count(0.0)
    t = tier(len(fails(moved(S[SG], dict(zip(six, states))))))
    seen.add(t)
    ok = ok and t == (TIERS[1] if 1 <= j <= 3 else TIERS[0] if j == 0 else TIERS[2])
check("Partially Adequate exactly when 1-3 of the six stand at 0.0 (primary reading: 2)",
      ok and sum(S[SG][c] == 0.0 for c in six) == 2)
sup = moved(S[SG], {c: a for c, (a, _) in sflag.items() if a > S[SG][c]})
sdn = moved(S[SG], {c: a for c, (a, _) in sflag.items() if a < S[SG][c]})
check("Joint readings: 16.5/26 with 2 failures upward, 10.5/26 with 8 downward; all three tiers reached",
      (total(sup), len(fails(sup)), total(sdn), len(fails(sdn))) == (16.5, 2, 10.5, 8)
      and seen == set(TIERS))
check("Domain 1 (4.0) is the highest of the seven Step 1b systems",
      dsum(S[SG], 'D1') == 4.0 and all(dsum(S[k], 'D1') < 4.0 for k in STEP1B if k != SG))
check("First Step 1b system (scoring order) to pass C1.2a or C1.3",
      S[SG]['C1.2a'] == S[SG]['C1.3'] == 1.0
      and not any(S[k][c] == 1.0 for k in STEP1B[:6] for c in ('C1.2a', 'C1.3')))
higher = [c for c in ALL if S[SG][c] > S[CN][c]]
check("Dominates China: higher on 8 criteria, lower on none",
      dominates(S[SG], S[CN]) and len(higher) == 8 and not any(S[SG][c] < S[CN][c] for c in ALL))
check("Its 4 failures are a strict subset of China's 8; China's other 4 are its downward flags",
      set(F[SG]) < set(F[CN]) and sorted(set(F[CN]) - set(F[SG])) == down_fl)
check("Dominated only by CCO-PTF-CIP-SZH; dominates only China",
      dom_by[SG] == [CCO] and dom_over[SG] == [CN])

print("\n  -- Corpus-level structure --")
tcount = {t: sum(tier(len(F[k])) == t for k in S) for t in TIERS}
print(f"  Tier counts: {tcount}")
check("Tier counts: 6 Potentially Adequate, 6 Partially Adequate, 8 Structurally Inadequate",
      [tcount[t] for t in TIERS] == [6, 6, 8])
fr20, fr17 = frontier(S), frontier(s16.SCORES)
print(f"  Pareto frontier ({len(fr20)}): {fr20}")
check("The Pareto frontier is unchanged by the insertion (same 10 systems; none of the three joins it)",
      fr20 == fr17 and len(fr20) == 10 and not set(NEW) & set(fr20))
adequate = {k: v for k, v in S.items() if tier(len(F[k])) != TIERS[2]}
adequate17 = {k: v for k, v in s16.SCORES.items() if tier(len(fails(v))) != TIERS[2]}
print(f"  Adequate-tier subset: {len(adequate)} systems; restricted frontier: {frontier(adequate)}")
check("Adequate subset grows from 10 to 12 (SWF, Singapore); its restricted frontier is unchanged (6)",
      len(adequate17) == 10 and sorted(set(adequate) - set(adequate17)) == sorted([SWF, SG])
      and frontier(adequate) == frontier(adequate17) and len(frontier(adequate)) == 6)
groups = {}
for k in S:
    groups.setdefault(total(S[k]), []).append(k)
ties = {t: g for t, g in groups.items() if len(g) > 1}
for t in sorted(ties, reverse=True):
    print(f"  Exact tie at {t:4.1f}: {ties[t]}  failures {[len(F[k]) for k in ties[t]]}")
check("Exact-tie groups: 19.5, 14.5, 14.0, 13.5, and the three-way 10.0",
      sorted(ties) == [10.0, 13.5, 14.0, 14.5, 19.5] and len(ties[10.0]) == 3
      and all(len(g) == 2 for t, g in ties.items() if t != 10.0))
pairs = [(a, b) for a in S for b in S if a != b and dominates(S[a], S[b])]
pairs17 = [(a, b) for a in s16.SCORES for b in s16.SCORES
           if a != b and dominates(s16.SCORES[a], s16.SCORES[b])]
print(f"  Strict-dominance relations in the corpus: {len(pairs)} ordered pairs "
      f"({sum(a in NEW or b in NEW for a, b in pairs)} involve a new system)")
for a, b in pairs:
    print(f"    {a}  >  {b}")
check("17-system corpus: 7 dominance relations, all from CCO-PTF-CIP-SZH",
      len(pairs17) == 7 and {a for a, _ in pairs17} == {CCO})
check("20-system corpus: 11 relations -- CCO-PTF-CIP-SZH over 10 systems, and Singapore over China, "
      "the only relation not involving CCO-PTF-CIP-SZH",
      len(pairs) == 11 and sum(a == CCO for a, _ in pairs) == 10
      and [p for p in pairs if CCO not in p] == [(SG, CN)] and not any(b == CCO for _, b in pairs))

# ---------------------------------------------------------------------------- tables
print("\n" + "=" * 92)
print("REFERENCE TABLES FOR THE STEP 5 REGENERATION (computed, not asserted)")
print("=" * 92)
print("\nRanking (equal weighting; ties keep canonical order and are marked '='):")
ranked = sorted(S, key=lambda k: -total(S[k]))
for i, k in enumerate(ranked, 1):
    mark = "=" if len(groups[total(S[k])]) > 1 else " "
    print(f"  {i:2d}{mark} {k:<36} {total(S[k]):5.1f}/26 {round(total(S[k]) / 26 * 100):3d}%  "
          f"{len(F[k]):2d} fail  {tier(len(F[k]))}")
print("\nCriterion-level failure counts (systems at 0.0), 20 systems:")
for c in sorted(ALL, key=lambda c: (-sum(S[k][c] == 0.0 for k in S), ALL.index(c))):
    who = [k for k in S if S[k][c] == 0.0]
    print(f"  {c:<6} {len(who):2d}/20  {who}")
print("\nDomain excellence (top five by domain total; ties at the cut-off included):")
for d in DOM:
    vals = sorted(S, key=lambda k: -dsum(S[k], d))
    cut = dsum(S[vals[4]], d)
    top = [k for k in vals if dsum(S[k], d) >= cut]
    print(f"  {d} (max {len(DOM[d])}): " + "; ".join(f"{k} {dsum(S[k], d):.1f}" for k in top))

print("\n" + "=" * 92)
bad = [label for label, ok in RESULTS if not ok]
print(f"SUMMARY: {len(RESULTS) - len(bad)}/{len(RESULTS)} checks pass.")
if bad:
    for label in bad:
        print(f"  FAILED: {label}")
    sys.exit(1)
print("ALL CHECKS PASS. The three Step 1b systems are in the canonical script and CSV exactly")
print("as their verification scripts record them; the 17 earlier systems are untouched; and")
print("every comparative claim in the new CSV rows holds in the 20-system corpus.")
