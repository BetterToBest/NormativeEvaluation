#!/usr/bin/env python3
"""
audit_claim_survival_s25.py -- NEEC Session 25: claim-survival audit
=====================================================================
Three Step 1b entries were scored one at a time against the 20-system
canonical corpus and never against each other:

    State Capitalism / Qatar                    (Session 21, verify_qatar.py)
    Islamic Finance / Profit-Sharing Banking    (Session 22, verify_islamicfinance.py)
    Ostrom-Style Commons Governance             (Session 23, verify_ostrom.py)

Every comparative claim in their scratch documents is therefore a 21-system
claim. This audit asks which of those claims survive in the combined
23-system corpus, WITHOUT editing any verifier: each verifier is re-run,
unmodified, against a view of the corpus that already contains the other two
entries.

METHOD. For each pending entry P:
  1. Build a view: the pinned Session 20 snapshot's text, plus appended
     SCORES[k] = {...} / PUBLISHED[k] = {...} lines for the OTHER two entries
     (vectors AST-extracted, never retyped). Write it under the canonical
     file name in a fresh temporary directory, with P's verifier and P's
     scratch document, and run P's verifier there. P adds itself, so the
     verifier sees 23 systems.
  2. Controls: each verifier reproduces its captured output byte for byte on
     the plain snapshot, and each view loads 22 systems and passes the
     snapshot's own verify_transcription().
  3. Collect every FAIL line, and Qatar's MISSING [claim] lines (its FAILED:
     recap repeats them and is skipped). The set must equal the register
     below exactly -- no unexplained failure, and no registered one missing.
  4. For the two verifiers with a --facts mode (Islamic finance, Ostrom), diff
     the --facts output snapshot-vs-view. This exposes computed facts that a
     verifier prints but never asserts.
  5. Recompute, independently of every verifier, each superseded claim's
     23-system value and each moved --facts value, and assert it.

Categories in the register: 'corpus size' (a check that pins the size or
dominance-pair count of the corpus it was written for); 'superseded' (a
comparative claim that was true of the 21-system view and is not true of the
23-system corpus); 'derivative' (a check that fails only because a table or
claim of the other two kinds changed).

The audit edits nothing. The superseded claims stay in the scratch documents
as dated records; their 23-system replacements are what the insertion notes
(insert_session25.py) and the Step 5 prose must use.

Usage:   python3 audit_claim_survival_s25.py [SRC_DIR]
Exit status is 0 only if every control, every register match, and every
recomputation passes. Output is deterministic (file names only, no paths).
"""
import ast
import difflib
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile

SRC = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
CANON = "neec_weighting_robustness_analysis_v2.py"
SNAP = "neec_weighting_robustness_analysis_v2_s20_snapshot.py"
SNAP_MD5 = "487d5a94138f3f896c3f723498b6c0e9"

D1 = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5']
DOMAINS = [D1] + [[f'C{d}.{i}' for i in range(1, 6)] for d in range(2, 6)]
ALL = [c for g in DOMAINS for c in g]

QA, IF, OS = 'State Capitalism / Qatar', 'Islamic Finance / Profit-Sharing Banking', 'Ostrom-Style Commons Governance'
CCO, SG, CN, SWF = 'CCO-PTF-CIP-SZH', 'State Capitalism / Singapore', 'State Capitalism / China', 'Sovereign Wealth Fund Statism'
ENTRIES = {  # key: (verifier, vector variable, scratch document, captured output)
    QA: ('verify_qatar.py', 'QA', 'NEEC_StateCapitalism_Qatar_scoring_scratch.md', 'verify_qatar_output.txt'),
    IF: ('verify_islamicfinance.py', 'SCORE', 'NEEC_IslamicFinance_scoring_scratch.md', 'verify_islamicfinance_output.txt'),
    OS: ('verify_ostrom.py', 'OSTROM', 'NEEC_Ostrom_Commons_scoring_scratch.md', 'verify_ostrom_output.txt'),
}
FACTS_MODE = (IF, OS)

# ---------------------------------------------------------------------------
# The register: every check expected to fail on the 23-system view.
# (entry, exact failing line, category, 23-system value)
# ---------------------------------------------------------------------------
REGISTER = [
    (QA, "FAIL  Canonical corpus holds exactly 20 systems", "corpus size", "the view holds 22"),
    (QA, "FAIL  Canonical corpus has 11 ordered dominance pairs (Handoff 20)", "corpus size",
     "the view holds 12"),
    (QA, "FAIL  Rank 20 of 21 in the prospective corpus, with no exact tie", "superseded",
     "22nd of 23, no exact tie (still above only Libertarian Minarchism)"),
    (QA, "FAIL  Insertion takes the corpus from 11 to 13 ordered dominance pairs", "superseded",
     "combined insertion: 11 -> 14 (Qatar +2, Islamic finance +1, Ostrom +0)"),
    (QA, "FAIL  The two pairs not involving CCO are Singapore over China and Singapore over Qatar", "superseded",
     "three: also Islamic Finance / Profit-Sharing Banking over Stakeholder Capitalism"),
    (QA, "FAIL  The joint upward total (14.0) is SWF Statism's and Singapore's, both Partially Adequate",
     "superseded", "also Ostrom-Style Commons Governance's; all three Partially Adequate"),
    (QA, "FAIL  Every one of the 42 rebuilt numeric claims appears verbatim in the document", "derivative",
     "its four MISSING claims below are the four superseded rows above"),
    (IF, "FAIL  canonical corpus holds 20 systems", "corpus size", "the view holds 22"),
    (IF, "FAIL  corpus with the new system holds 21", "corpus size", "23"),
    (IF, "FAIL  rank is 12 (competition rank)", "superseded",
     "13 (three-way tie at 13.5 with Georgism / Land Value Tax and Universal Basic Services)"),
    (IF, "FAIL  Domain 4 of 1.5 is fifth-lowest in the corpus", "superseded",
     "sixth-lowest, tied with Libertarian Minarchism"),
    (IF, "FAIL  insertion takes dominance pairs from 11 to 12", "superseded", "combined insertion: 11 -> 14"),
    (IF, "FAIL  document round-trips through --fill", "derivative",
     "the generated corpus table now carries 23 rows"),
    (OS, "FAIL  [A1] canonical corpus loads with 20 systems", "corpus size", "the view holds 22"),
    (OS, "FAIL  [F] corpus has 11 strict-dominance pairs before insertion", "corpus size", "the view holds 14"),
    (OS, "FAIL  [F] exactly one corpus system beats Domain 5", "superseded",
     "two: CCO-PTF-CIP-SZH and Islamic Finance / Profit-Sharing Banking (4.5 each)"),
    (OS, "FAIL  [F] that system is CCO-PTF-CIP-SZH", "superseded",
     "CCO-PTF-CIP-SZH and Islamic Finance / Profit-Sharing Banking"),
    (OS, "FAIL  [F] ranked table has 21 rows", "corpus size", "23"),
    (OS, "FAIL  [H] corpus-table is byte-identical to a fresh render", "derivative",
     "the generated corpus table now carries 23 rows"),
]
QATAR_MISSING = [
    "MISSING [prospective corpus size]: 'In a prospective 23-system corpus'",
    "MISSING [rank]: 'rank 22nd of 23, above only Libertarian Minarchism (8.0/26), with no exact tie'",
    "MISSING [dominance pair count]: 'from 12 to 14 ordered pairs'",
    "MISSING [non-CCO dominance pairs]: 'Singapore over China and Singapore over Qatar and Islamic "
    "Finance / Profit-Sharing Banking over Stakeholder Capitalism'",
]
# Unasserted --facts lines that change for Ostrom-Style Commons Governance (before, after).
OSTROM_MOVED = [
    ("  Domain Material Security          2.0  beaten by 13, tied with 4",
     "  Domain Material Security          2.0  beaten by 14, tied with 5"),
    ("  Domain Human Autonomy             2.5  beaten by 13, tied with 1",
     "  Domain Human Autonomy             2.5  beaten by 13, tied with 2"),
    ("  Domain System Resilience          2.5  beaten by 15, tied with 3",
     "  Domain System Resilience          2.5  beaten by 16, tied with 3"),
    ("  Domain Implementation Viability   4.0  beaten by 1, tied with 3",
     "  Domain Implementation Viability   4.0  beaten by 2, tied with 3"),
    ("  this entry would rank: 2 of 21", "  this entry would rank: 3 of 23"),
    ("D4 3.0; systems with lower D4: 10", "D4 3.0; systems with lower D4: 12"),
]

RESULTS = []


def check(label, cond):
    RESULTS.append(bool(cond))
    print(f"  {'PASS' if cond else 'FAIL'}  {label}")


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()


def module_literal(name, var):
    tree = ast.parse(read(name))
    hits = [ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
            and any(getattr(t, "id", None) == var for t in n.targets)]
    if len(hits) != 1:
        sys.exit(f"ERROR: expected one module-level assignment to {var} in {name}, found {len(hits)}")
    return hits[0]


def sums(v):
    return [sum(v[c] for c in g) for g in DOMAINS]


def appended(key, v):
    s = sums(v)
    return (f"\nSCORES[{key!r}] = {v!r}\n"
            f"PUBLISHED[{key!r}] = {{'D1':{s[0]:.1f},'D2':{s[1]:.1f},'D3':{s[2]:.1f},"
            f"'D4':{s[3]:.1f},'D5':{s[4]:.1f},'Total':{sum(s):.1f}}}\n")


def run_verifier(key, canon_text, args=()):
    verifier, _, doc, _ = ENTRIES[key]
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, CANON), "w", encoding="utf-8") as f:
            f.write(canon_text)
        for name in (verifier, doc):
            shutil.copy(os.path.join(SRC, name), tmp)
        proc = subprocess.run([sys.executable, verifier, *args], cwd=tmp, capture_output=True)
        return proc.returncode, proc.stdout.decode("utf-8")


def load_view(text):
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, CANON)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        spec = importlib.util.spec_from_file_location("view", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod


print("=" * 96)
print("audit_claim_survival_s25.py -- NEEC Session 25: do the three pending entries' claims survive?")
print("=" * 96)

# ---------------------------------------------------------------------------- (1)
print("\n(1) SOURCES")
snap_text = read(SNAP)
check(f"{SNAP} is the pinned Session 20 canonical file (md5 {SNAP_MD5[:8]})",
      hashlib.md5(snap_text.encode("utf-8")).hexdigest() == SNAP_MD5)
VEC = {}
for key, (verifier, var, doc, _) in ENTRIES.items():
    v = module_literal(verifier, var)
    VEC[key] = v
    check(f"{var} in {verifier}: 26 criteria in canonical order, all in {{0, 0.5, 1}}",
          list(v) == ALL and all(x in (0.0, 0.5, 1.0) for x in v.values()))

# ---------------------------------------------------------------------------- (2)
print("\n(2) CONTROLS")
for key, (verifier, _, _, captured) in ENTRIES.items():
    rc, out = run_verifier(key, snap_text)
    check(f"{verifier} on the plain snapshot: exit 0, stdout byte-identical to {captured}",
          rc == 0 and out == read(captured))
VIEWS = {k: snap_text + "".join(appended(o, VEC[o]) for o in ENTRIES if o != k) for k in ENTRIES}
for key in ENTRIES:
    mod = load_view(VIEWS[key])
    others = [o for o in ENTRIES if o != key]
    check(f"View for {ENTRIES[key][0]}: 22 systems (snapshot + {len(others)}), verify_transcription() passes",
          len(mod.SCORES) == 22 and list(mod.SCORES)[20:] == others and mod.verify_transcription(verbose=False))

# ---------------------------------------------------------------------------- (3)
print("\n(3) FAILING CHECKS ON EACH 23-SYSTEM VIEW, AGAINST THE REGISTER")
observed, missing_lines, facts = [], [], {}
for key in ENTRIES:
    rc, out = run_verifier(key, VIEWS[key])
    for line in out.splitlines():
        s = line.strip()
        if re.match(r"FAIL\b", s):
            observed.append((key, s))
        elif s.startswith("MISSING ["):
            missing_lines.append((key, s))
    if key in FACTS_MODE:
        facts[key] = (run_verifier(key, snap_text, ("--facts",))[1], run_verifier(key, VIEWS[key], ("--facts",))[1])
registered = [(k, line) for k, line, _, _ in REGISTER]
for key, line, cat, now in REGISTER:
    print(f"    [{cat:<11}] {ENTRIES[key][0]}: {line[6:]}")
    print(f"                  23-system value: {now}")
unexplained = [o for o in observed if o not in registered]
absent = [r for r in registered if r not in observed]
for o in unexplained:
    print(f"    UNEXPLAINED: {o}")
for r in absent:
    print(f"    REGISTERED BUT NOT OBSERVED: {r}")
check(f"Observed failing checks equal the register exactly ({len(observed)} observed, {len(REGISTER)} registered)",
      sorted(observed) == sorted(registered) and len(observed) == len(set(observed)))
counts = {c: sum(1 for r in REGISTER if r[2] == c) for c in ("corpus size", "superseded", "derivative")}
check(f"Categories: {counts['corpus size']} corpus size, {counts['superseded']} superseded, "
      f"{counts['derivative']} derivative (19 in all)",
      counts == {"corpus size": 7, "superseded": 9, "derivative": 3})
check("Qatar's MISSING claims are exactly its four superseded rows (rebuilt with 23-system values)",
      [m for _, m in missing_lines] == QATAR_MISSING and all(k == QA for k, _ in missing_lines))

# ---------------------------------------------------------------------------- (4)
print("\n(4) --facts DIFFS (computed facts that are printed but not asserted)")
for key in FACTS_MODE:
    before, after = facts[key]
    diff = [d for d in difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm="", n=0)
            if not d.startswith(("---", "+++", "@@"))]
    print(f"\n  {key}: {len(diff)} changed lines")
    for d in diff:
        print(f"    {d}")
    facts[key] = (before.splitlines(), after.splitlines(), diff)
b, a, _ = facts[OS]
check("Ostrom: exactly the six registered unasserted facts move (and each moves as registered)",
      all(x in b and x not in a and y in a and y not in b for x, y in OSTROM_MOVED))
b, a, _ = facts[IF]
check("Islamic finance: its --facts diff is confined to the ranked table, the dominance-pair line, "
      "and the Domain 5 / Domain 4 neighbour lists",
      all(re.match(r"[-+](\(\d+, '|strict-dominance ordered pairs|Domain 5 leaders|Domain 4 lowest)", d)
          for d in facts[IF][2]))

# ---------------------------------------------------------------------------- (5)
print("\n(5) INDEPENDENT RECOMPUTATION ON THE COMBINED 23-SYSTEM CORPUS")
base = load_view(snap_text)
C20 = dict(base.SCORES)
C23 = dict(C20)
C23.update(VEC)


def total(v):
    return sum(v.values())


def dom(v, d):
    return sums(v)[d - 1]


def dominates(a, b, corpus):
    return all(corpus[a][c] >= corpus[b][c] for c in ALL) and any(corpus[a][c] > corpus[b][c] for c in ALL)


def pairs(corpus):
    return {(a, b) for a in corpus for b in corpus if a != b and dominates(a, b, corpus)}


def comp_rank(key, corpus, value, higher_is_better=True):
    x = value(corpus[key])
    return 1 + sum(1 for k in corpus if (value(corpus[k]) > x if higher_is_better else value(corpus[k]) < x))


def nfail(v):
    return sum(1 for c in ALL if v[c] == 0.0)


P20, P23 = pairs(C20), pairs(C23)
check("Qatar: rank 22 of 23 (competition), no exact tie, above only Libertarian Minarchism",
      len(C23) == 23 and comp_rank(QA, C23, total) == 22
      and [k for k in C23 if total(C23[k]) == total(C23[QA])] == [QA]
      and [k for k in C23 if total(C23[k]) < total(C23[QA])] == ['Libertarian Minarchism'])
per_entry = {k: sum(1 for p in P23 if k in p) for k in ENTRIES}
check("Dominance pairs: 11 in the 20-system corpus, 14 in the combined corpus (Qatar +2, IF +1, Ostrom +0)",
      len(P20) == 11 and len(P23) == 14 and P20 < P23 and per_entry == {QA: 2, IF: 1, OS: 0})
check("Non-CCO pairs: Singapore over China, Singapore over Qatar, IF over Stakeholder Capitalism (three)",
      {p for p in P23 if p[0] != CCO} == {(SG, CN), (SG, QA), (IF, 'Stakeholder Capitalism')})
at14 = [k for k in C23 if total(C23[k]) == 14.0]
check("Totals of 14.0: SWF Statism, Singapore, Ostrom -- all Partially Adequate (3, 4, 4 failures)",
      at14 == [SWF, SG, OS] and [nfail(C23[k]) for k in at14] == [3, 4, 4])
at135 = [k for k in C23 if total(C23[k]) == 13.5]
check("IF: rank 13 (competition), in a three-way tie at 13.5 with Georgism and UBS",
      comp_rank(IF, C23, total) == 13 and at135 == ['Georgism / Land Value Tax', 'Universal Basic Services', IF])
check("IF: Domain 4 (1.5) is sixth-lowest, tied only with Libertarian Minarchism",
      comp_rank(IF, C23, lambda v: dom(v, 4), higher_is_better=False) == 6
      and [k for k in C23 if k != IF and dom(C23[k], 4) == 1.5] == ['Libertarian Minarchism'])
check("Ostrom: Domain 5 (4.0) is beaten by exactly CCO-PTF-CIP-SZH and IF (4.5 each)",
      [k for k in C23 if dom(C23[k], 5) > dom(C23[OS], 5)] == [CCO, IF]
      and all(dom(C23[k], 5) == 4.5 for k in (CCO, IF)))
others = [k for k in C23 if k != OS]
beaten = {d: sum(1 for k in others if dom(C23[k], d) > dom(C23[OS], d)) for d in range(1, 6)}
tied = {d: sum(1 for k in others if dom(C23[k], d) == dom(C23[OS], d)) for d in range(1, 6)}
check("Ostrom moved facts: Domain 1 beaten by 14 (tied 5); Domain 2 tied with 2; Domain 3 beaten by 16; "
      "Domain 5 beaten by 2",
      (beaten[1], tied[1], tied[2], beaten[3], beaten[5]) == (14, 5, 2, 16, 2))
split = lambda v: dom(v, 5) - dom(v, 1)
check("Ostrom moved facts: viability-minus-material-security split 2.0 ranks 3 of 23 "
      "(Libertarian Minarchism 3.0, IF 2.5 ahead)",
      split(C23[OS]) == 2.0 and comp_rank(OS, C23, split) == 3
      and sorted(k for k in C23 if split(C23[k]) > 2.0) == sorted(['Libertarian Minarchism', IF]))
check("Ostrom moved facts: 12 of the other 22 systems score below its Domain 4 (3.0)",
      sum(1 for k in others if dom(C23[k], 4) < 3.0) == 12)

# ---------------------------------------------------------------------------- summary
print("\n" + "=" * 96)
n_pass = sum(RESULTS)
print(f"SUMMARY: {n_pass} passed, {len(RESULTS) - n_pass} failed (of {len(RESULTS)}).")
print("Nothing is edited. The registered claims stay in the scratch documents as dated 21-system")
print("records; insert_session25.py's row notes and the Step 5 prose use the 23-system values.")
print("=" * 96)
sys.exit(0 if all(RESULTS) else 1)
