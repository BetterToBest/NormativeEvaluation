#!/usr/bin/env python3
"""
narrow_verifiers_s26.py -- NEEC Session 26: the three Step 1b entry verifiers, narrowed
=====================================================================================
Decision D12 (Session 26) restated the comparative claims of the State Capitalism /
Qatar, Islamic finance and Ostrom-style commons governance scoring documents on the
canonical 23-system corpus, and made verify_comparative_claims.py their single
checker. The entry verifiers written in Sessions 21-23 checked those claims too,
against the 20-system corpus as it stood before insertion, so they no longer pass
on the restated documents, and two of them would overwrite the restated corpus
tables if run with --fill.

This script derives the current entry verifiers from the Session 21-23 versions,
pinned by MD5 as *_s25_snapshot.py (byte copies of the verifiers as they stood at
the end of Session 25). Each narrowed verifier:
  * checks the claims its document makes about the entry itself (arithmetic,
    transcription, sensitivity, scope scenario, the entry's generated tables);
  * asserts that the canonical corpus holds the entry with exactly its vector,
    in place of the old pre-insertion checks (20 systems; entry not yet present);
  * drops every comparison with other systems, which verify_comparative_claims.py
    now asserts on the canonical corpus;
  * writes, with --fill, only the entry's own tables, never the corpus table.
The snapshots stay unedited and still run, against the corpus they were written
for, in run_all_checks.py.

Rules, as in rewrite_session26.py: inputs pinned by MD5; every anchored edit must
match exactly once; all three outputs are built in memory and written only if
every edit applies; output is deterministic.

Usage:  python3 narrow_verifiers_s26.py [INDIR] [OUTDIR]     (defaults: . and out)
"""
import hashlib
import os
import re
import sys

INDIR = sys.argv[1] if len(sys.argv) > 1 else "."
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else "out"

VERIFIERS = ("verify_qatar.py", "verify_islamicfinance.py", "verify_ostrom.py")
PINNED_MD5 = {
    "verify_qatar_s25_snapshot.py": "f30367b473ae865bb9e4206646bbe76a",
    "verify_islamicfinance_s25_snapshot.py": "79c1a02ac120b888dff0437752ca865c",
    "verify_ostrom_s25_snapshot.py": "8ff9a9f5661dd3bf53649f43fe125d3c",
}


def snap(name):
    return name[:-3] + "_s25_snapshot.py"


for name, digest in PINNED_MD5.items():
    path = os.path.join(INDIR, name)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: missing input {name}")
    got = hashlib.md5(open(path, "rb").read()).hexdigest()
    if got != digest:
        sys.exit(f"ERROR: {name} has MD5 {got}, expected {digest} (pinned input)")

LOG = []


def die(msg):
    sys.exit(f"ERROR: {msg}; nothing written")


def rep(text, eid, old, new):
    n = text.count(old)
    if n != 1:
        die(f"edit {eid}: anchor occurs {n} times (must be exactly 1)")
    LOG.append(eid)
    return text.replace(old, new, 1)


def cut(text, eid, start, stop, new=""):
    """Replace the text from the unique `start` up to (not including) the first later `stop`."""
    if text.count(start) != 1:
        die(f"edit {eid}: start anchor occurs {text.count(start)} times")
    i = text.index(start)
    j = text.find(stop, i + len(start))
    if j < 0:
        die(f"edit {eid}: stop anchor not found after the start anchor")
    LOG.append(eid)
    return text[:i] + new + text[j:]


def cut_re(text, eid, pattern, new=""):
    hits = list(re.finditer(pattern, text, flags=re.S))
    if len(hits) != 1:
        die(f"edit {eid}: pattern matches {len(hits)} times")
    LOG.append(eid)
    return text[:hits[0].start()] + new + text[hits[0].end():]


def docstring(text, eid, body):
    i = text.index('"""')
    j = text.index('"""', i + 3)
    LOG.append(eid)
    return text[:i + 3] + "\n" + body + "\n" + text[j:]


def read(name):
    with open(os.path.join(INDIR, name), encoding="utf-8") as f:
        return f.read()


OUT = {}

# ================================================================== verify_qatar.py
t = read(snap("verify_qatar.py"))
t = docstring(t, "Q-doc", """Entry verifier for the State Capitalism / Qatar scoring document (Step 1b:
scored in Session 21; inserted into the canonical corpus in Session 25;
narrowed in Session 26 by narrow_verifiers_s26.py).

This script checks the claims the document makes about this entry itself.
Claims that compare the entry with other systems (criterion bands, ranks, ties,
dominance, domain positions) are checked on the canonical corpus by
verify_comparative_claims.py (decision D12). The Session 21 version, which also
checked them against the 20-system corpus as it stood before insertion, is kept
unedited as verify_qatar_s25_snapshot.py and still runs, against that corpus,
in run_all_checks.py.

Check groups:
  (0) Sources: the canonical corpus is imported from the unmodified
      neec_weighting_robustness_analysis_v2.py, its own transcription
      self-check must pass, it must hold this entry with exactly the vector
      below, and the local helpers must agree with the canonical ones.
  (1) Self-consistency: re-sum the 26-criterion vector against the stated
      domain totals, total, distribution, failures, and tier.
  (2) Transcription: parse the document's criterion headings (scores AND
      flag markers), domain-sum lines, Summary Scores lines, each flagged
      call's inline consequence, and each citizens-only scenario statement;
      and compare its two GENERATED tables verbatim with a fresh render.
  (3) Contestable-call sensitivity: each flagged call alone, jointly, and
      in all 2**12 combinations under the confirmed population scope.
  (4) Population scope: the citizens-only scenario, alone and across the
      flagged calls it leaves open.
  (5) Domain 4: the entry's own failures there. (The rest of the old group
      (5), the corpus comparison, is in verify_comparative_claims.py.)
  (6) Stated numbers: every numeric claim about this entry is rebuilt here
      and must appear verbatim (whitespace normalized) in the text.

Modes:
  python3 verify_qatar.py         run all checks (this is the captured output)
  python3 verify_qatar.py --fill  rewrite the document's two GENERATED
                                  blocks from a fresh render, then exit

PORTABILITY: looks beside itself first, then in the conventional working
locations, and prints only file names, so the captured output reproduces
byte for byte from any directory holding the companion files (the canonical
v2 script and the scoring document). Writes nothing unless --fill is given.""")
t = rep(t, "Q-title",
        'print("verify_qatar.py -- NEEC Step 1b, Session 21 (State Capitalism / Qatar)")',
        'print("verify_qatar.py -- NEEC entry checks: State Capitalism / Qatar (Session 21; narrowed Session 26)")')
t = rep(t, "Q-identity",
        """check("Canonical corpus holds exactly 20 systems", len(SCORES) == 20)
check("Qatar is not already in the canonical corpus", not any('Qatar' in k for k in SCORES))
""",
        """check("Canonical corpus holds State Capitalism / Qatar exactly once",
      [k for k in SCORES if 'Qatar' in k] == [QA_NAME])
check("Its canonical vector equals this script's vector, criterion by criterion",
      SCORES.get(QA_NAME) == QA)
""")
t = rep(t, "Q-pairs-print",
        """print(f"  Dominance helper validated on {len(SCORES) * (len(SCORES) - 1)} ordered pairs; "
      f"{pairs} are dominance pairs")
""",
        """print(f"  Dominance helper validated on {len(SCORES) * (len(SCORES) - 1)} ordered pairs")
""")
t = rep(t, "Q-pairs-check",
        'check("Canonical corpus has 11 ordered dominance pairs (Handoff 20)", pairs == 11)\n', "")
t = cut(t, "Q-group5",
        "# ---------------------------------------------------------------- (5)\n",
        "# ---------------------------------------------------------------- (6)\n",
        """# ---------------------------------------------------------------- (5)
# The corpus comparison moved to verify_comparative_claims.py (Session 26). The
# one check in the old group that concerned this entry alone stays here.
print("\\n(5) DOMAIN 4 (the entry's own failures; comparisons are in verify_comparative_claims.py)")
check("Four of Domain 4's five criteria are failures, none of them flagged",
      sum(QA[c] == 0.0 for c in DOMAINS['D4']) == 4
      and not [c for c in DOMAINS['D4'] if QA[c] == 0.0 and c in FLAGGED])

""")
t = rep(t, "Q-worst2",
        """    dmap = dict(zip(DOMAINS, dd_swf))
    worst2 = [d for d in DOMAINS if d in sorted(DOMAINS, key=lambda x: dmap[x])[:2]]
""", "")
# Drop the 21 comparative phrases from the rebuilt-claims list (they are asserted,
# with 23-system values, by verify_comparative_claims.py).
DROP = {"upward extreme against two canonical systems", "scope tie", "Domain 4 lowest in corpus",
        "Step 1b cohort position", "mechanism against configuration", "SWF differences",
        "SWF shared failures", "SWF domain deltas", "SWF worst domains", "Singapore dominance",
        "Singapore domain deltas", "Singapore failure subset", "China non-dominance",
        "China differences", "China failure subset and total", "prospective corpus size", "rank",
        "dominance summary", "dominance pair count", "non-CCO dominance pairs", "archetype tiers"}
head = "    CLAIMS = [\n"
if t.count(head) != 1:
    die("edit Q-claims: CLAIMS list not found exactly once")
a = t.index(head) + len(head)
b = t.index("\n    ]\n", a)
items = [it for it in re.split(r"(?m)^(?=        \(\")", t[a:b]) if it.strip()]
labels = [re.match(r'        \("([^"]+)"', it).group(1) for it in items]
if len(items) != 42 or not DROP <= set(labels) or len(set(labels)) != 42:
    die(f"edit Q-claims: expected 42 distinct claims including all 21 to drop, found {len(items)}")
kept = [it.rstrip("\n") for it, lb in zip(items, labels) if lb not in DROP]
t = t[:a] + "\n".join(kept) + t[b:]
LOG.append("Q-claims")
t = rep(t, "Q-summary",
        """print("ALL CHECKS PASS. Nothing is inserted anywhere (scratch-before-insert discipline);")
print("this verifies the scratch document's arithmetic, its transcription, its generated")
print("tables, its twelve flagged calls, the confirmed population scope and its scenario,")
print("and every comparative claim against the real canonical 20-system corpus.")""",
        """print("ALL CHECKS PASS. This verifies the scoring document's arithmetic, its transcription,")
print("its generated tables, its twelve flagged calls, the confirmed population scope and its")
print("scenario, and that the canonical corpus holds exactly this vector. Comparative claims")
print("are checked on the canonical corpus by verify_comparative_claims.py.")""")
OUT["verify_qatar.py"] = t

# ================================================================== verify_islamicfinance.py
t = read(snap("verify_islamicfinance.py"))
t = docstring(t, "F-doc", """verify_islamicfinance.py -- entry verifier for NEEC_IslamicFinance_scoring_scratch.md
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
  python3 verify_islamicfinance.py           run every check""")
t = cut(t, "F-corpus-helpers", "def build_corpus(mod):\n",
        "# ---------------------------------------------------------------- generated\n")
t = cut(t, "F-fill", "def render_corpus_table(corpus):\n",
        "# ---------------------------------------------------------------- facts\n",
        '''def fill(doc_text):
    """Rewrite the summary block only. The corpus table is written by
    verify_comparative_claims.py --fill (Session 26)."""
    body = render_summary_table()
    return re.sub(
        r"<!-- GENERATED:summary -->.*?<!-- END GENERATED:summary -->",
        lambda m: f"<!-- GENERATED:summary -->\\n{body}\\n<!-- END GENERATED:summary -->",
        doc_text, flags=re.S)


''')
t = rep(t, "F-section",
        "# ---------------------------------------------------------------- facts\n",
        "# ---------------------------------------------------------------- sensitivity\n")
t = cut(t, "F-facts", "def facts():\n",
        "# ---------------------------------------------------------------- checks\n")
t = rep(t, "F-main",
        """    if "--facts" in sys.argv:
        facts()
        return 0

    mod = load_canon()
    corpus = build_corpus(mod)
""",
        """    mod = load_canon()
""")
t = rep(t, "F-fill-mode",
        """        new = fill(text, corpus)
        with open(DOC, "w", encoding="utf-8") as fh:
            fh.write(new)
        print("filled GENERATED blocks in", os.path.basename(DOC))""",
        """        new = fill(text)
        with open(DOC, "w", encoding="utf-8") as fh:
            fh.write(new)
        print("filled the GENERATED summary block in", os.path.basename(DOC))""")
t = rep(t, "F-title", 'print("verify_islamicfinance.py -- NEEC Session 22")',
        'print("verify_islamicfinance.py -- NEEC entry checks: Islamic finance (Session 22; narrowed Session 26)")')
t = rep(t, "F-identity",
        """    c.check("canonical corpus holds 20 systems", len(mod.SCORES) == 20,
            f"got {len(mod.SCORES)}")
    c.check("system not yet inserted", SYSTEM not in mod.SCORES)
""",
        """    c.check("canonical corpus holds this system", SYSTEM in mod.SCORES)
    c.check("its canonical vector equals this script's vector",
            mod.SCORES.get(SYSTEM) == SCORE)
""")
t = cut(t, "F-group6", '    print("\\n[6] Corpus comparison")\n',
        '    print("\\n[7] Numeric claims rebuilt and matched in the prose")\n')
t = rep(t, "F-numbers", '    print("\\n[7] Numeric claims rebuilt and matched in the prose")',
        '    print("\\n[6] Numeric claims about this entry, rebuilt and matched in the prose")')
t = rep(t, "F-pairs-claim", '        "11 to 12",\n', "")
t = rep(t, "F-generated",
        """    print("\\n[8] Generated blocks are byte-identical to a fresh render")
    c.check("document round-trips through --fill", fill(text, corpus) == text)""",
        """    print("\\n[7] Generated summary block is byte-identical to a fresh render")
    c.check("summary block round-trips through --fill", fill(text) == text)""")
OUT["verify_islamicfinance.py"] = t

# ================================================================== verify_ostrom.py
t = read(snap("verify_ostrom.py"))
t = docstring(t, "O-doc", """verify_ostrom.py — entry verifier for the Step 1b evaluation of Ostrom-style
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

Deterministic: no dict-ordering dependence, no randomness, no clock.""")
t = cut_re(t, "O-corpus-helpers", r"# -{10,}\n# Corpus comparison\n# -{10,}\n.*?(?=# -{10,}\n# Generated blocks\n)")
t = rep(t, "O-corpus-markers",
        'BEGIN_CORPUS = "<!-- BEGIN GENERATED: corpus-table -->"\nEND_CORPUS = "<!-- END GENERATED: corpus-table -->"\n',
        "")
t = cut_re(t, "O-corpus-table-and-facts", r"def render_corpus_table\(\):\n.*?(?=# -{10,}\n# Checks\n)")
t = rep(t, "O-identity-A1",
        """    check("[A1] canonical corpus loads with 20 systems", len(CORPUS) == 20,
          f"got {len(CORPUS)}")
""",
        """    check("[A1] canonical corpus holds this entry", SYSTEM in CORPUS)
""")
t = rep(t, "O-identity-A3",
        """    check("[A3] this entry is not already in the corpus", SYSTEM not in CORPUS)
""",
        """    check("[A3] its canonical vector equals this script's vector",
          CORPUS.get(SYSTEM) == OSTROM)
""")
t = cut(t, "O-groupF", "def group_f():\n", "def group_g():\n")
t = rep(t, "O-groupH",
        '        (BEGIN_CORPUS, END_CORPUS, render_corpus_table, "corpus-table"),\n', "")
t = rep(t, "O-run", "    group_f()\n", "")
t = rep(t, "O-title", '    print(f"verify_ostrom.py — NEEC Session 23 — {SYSTEM}")',
        '    print(f"verify_ostrom.py — NEEC entry checks — {SYSTEM} (Session 23; narrowed Session 26)")')
t = rep(t, "O-main",
        """def main():
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
    return run_checks()""",
        """def main():
    if "--fill" in sys.argv:
        doc = read_doc()
        if doc is None or doc.count(BEGIN_SUMMARY) != 1 or doc.count(END_SUMMARY) != 1:
            sys.exit(f"ERROR: {DOC}: summary-table markers missing or repeated; nothing written")
        body = doc.split(BEGIN_SUMMARY, 1)[1].split(END_SUMMARY, 1)[0]
        new = doc.replace(BEGIN_SUMMARY + body + END_SUMMARY,
                          BEGIN_SUMMARY + "\\n" + render_summary_table() + "\\n" + END_SUMMARY, 1)
        with open(os.path.join(HERE, DOC), "w", encoding="utf-8") as fh:
            fh.write(new)
        print(f"filled the generated summary table in {DOC}")
        return 0
    return run_checks()""")
OUT["verify_ostrom.py"] = t

# ------------------------------------------------------------------ write
for name, text in OUT.items():
    if "BEGIN_CORPUS" in text or "render_corpus_table" in text or "20 systems" in text:
        die(f"{name}: a corpus-comparison remnant survived narrowing")
os.makedirs(OUTDIR, exist_ok=True)
print("narrow_verifiers_s26.py -- the three Step 1b entry verifiers, narrowed (decision D12)")
print(f"inputs pinned: {len(PINNED_MD5)} files")
for name in VERIFIERS:
    prefix = {"verify_qatar.py": "Q-", "verify_islamicfinance.py": "F-", "verify_ostrom.py": "O-"}[name]
    ids = [e for e in LOG if e.startswith(prefix)]
    data = OUT[name].encode("utf-8")
    with open(os.path.join(OUTDIR, name), "wb") as f:
        f.write(data)
    print(f"\n{snap(name)} -> {name}: {len(ids)} edits")
    print("  " + " ".join(ids))
    print(f"  wrote {name}  md5 {hashlib.md5(data).hexdigest()}")
print(f"\nTOTAL: {len(LOG)} edits")
