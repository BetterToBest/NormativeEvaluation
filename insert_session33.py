#!/usr/bin/env python3
"""
insert_session33.py -- NEEC Session 33: decision D26, applied to the canonical corpus
=====================================================================================
Decision D26 (Session 32, confirmed by the project owner in Session 33) resolves the contradiction in
C3.2's 0.0 band in favour of its note: 0.0 is reserved for an active inflationary mechanism with no
counterbalancing element, not for inflation merely left unaddressed. Ostrom-Style Commons Governance
was the corpus's only entry at 0.0 on C3.2, and its stated reason was absence, so its C3.2 becomes 0.5:
14.0 -> 14.5/26, failures 4 -> 3, tier unchanged (Partially Adequate). No other cell changes.

This generator writes the two canonical scripts from their Session 32 snapshots, pinned by MD5:
  neec_weighting_robustness_analysis_v2.py   the one SCORES cell and the PUBLISHED row (Domain 3 and
                                             the total); a comment stating the revision; and, beside
                                             the Session 25 tie note, a Session 33 note and the two
                                             new tie pairs (Ostrom with Mutual Credit / LETS and with
                                             Universal Basic Income), shown under the four schemes
  neec_scores_csv_builder_v2.py              Ostrom's row (Domain 3, failures, a revision note, and its
                                             notes restated on the Session 33 corpus with decision
                                             D18(b)'s re-expressed register); Universal Basic Income's
                                             notes, which name the three-way tie at 14.5/26
Each textual edit is an exact substring that must occur once. The two builder rows are re-rendered
from their parsed values, so every other byte of both files is unchanged. The facts behind the edits
are asserted by verify_insertion_s33.py and verify_comparative_claims.py (Session 33).

Usage:   python3 insert_session33.py [INDIR] [OUTDIR]        (defaults: . and out)
Prints file names only; deterministic.
"""
import ast
import hashlib
import json
import os
import sys

CANON = "neec_weighting_robustness_analysis_v2.py"
BUILDER = "neec_scores_csv_builder_v2.py"
SNAP = {CANON: ("neec_weighting_robustness_analysis_v2_s32_snapshot.py", "d5041b13"),
        BUILDER: ("neec_scores_csv_builder_v2_s32_snapshot.py", "7cd53027")}
OS = "Ostrom-Style Commons Governance"

CANON_EDITS = [
    ("the D26 comment, above SCORES",
     "\nSCORES = {\n",
     "\n# Session 33 (decision D26, protocol 4.6): Ostrom-Style Commons Governance's C3.2 is revised from\n"
     "# 0.0 to 0.5. C3.2's 0.0 band is reserved for an active inflationary mechanism with no\n"
     "# counterbalancing element, and the entry's stated reason for 0.0 was absence. Its total moves from\n"
     "# 14.0 to 14.5/26 and its failures from 4 to 3; its tier (Partially Adequate) is unchanged. No other\n"
     "# cell changes. Written by insert_session33.py from the Session 32 snapshot\n"
     "# (neec_weighting_robustness_analysis_v2_s32_snapshot.py); verified by verify_insertion_s33.py.\n"
     "SCORES = {\n"),
    ("Ostrom's C3.2 (SCORES)",
     "    'Ostrom-Style Commons Governance': {\n"
     "        'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.5,'C1.3':0.5,'C1.4':0.5,'C1.5':0.0,\n"
     "        'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,\n"
     "        'C3.1':0.5,'C3.2':0.0,",
     "    'Ostrom-Style Commons Governance': {\n"
     "        'C1.1':0.5,'C1.2a':0.0,'C1.2b':0.5,'C1.3':0.5,'C1.4':0.5,'C1.5':0.0,\n"
     "        'C2.1':0.5,'C2.2':0.0,'C2.3':0.5,'C2.4':0.5,'C2.5':1.0,\n"
     "        'C3.1':0.5,'C3.2':0.5,"),
    ("Ostrom's PUBLISHED row (Domain 3 and total)",
     "    'Ostrom-Style Commons Governance':   {'D1':2.0,'D2':2.5,'D3':2.5,'D4':3.0,'D5':4.0,'Total':14.0},",
     "    'Ostrom-Style Commons Governance':   {'D1':2.0,'D2':2.5,'D3':3.0,'D4':3.0,'D5':4.0,'Total':14.5},"),
    ("the Session 33 tie note and pairs",
     "        ('CCO-PTF-CIP-SZH', 'Ostrom-Style Commons Governance'),\n    ]\n",
     "        ('CCO-PTF-CIP-SZH', 'Ostrom-Style Commons Governance'),\n"
     "        # Session 33 (decision D26): Ostrom-Style Commons Governance now scores\n"
     "        # 14.5/26 with 3 failures. It ties Mutual Credit / LETS and Universal Basic\n"
     "        # Income exactly (3, 3 and 7 failures: two tiers) and no longer ties SWF\n"
     "        # Statism or Singapore; the Session 25 note above describes the corpus as\n"
     "        # inserted. No strict-dominance relation is gained or lost, and the Pareto\n"
     "        # frontier is unchanged (12 systems); all of this is asserted in\n"
     "        # verify_insertion_s33.py.\n"
     "        ('Ostrom-Style Commons Governance', 'Mutual Credit / LETS'),\n"
     "        ('Ostrom-Style Commons Governance', 'Universal Basic Income'),\n"
     "    ]\n"),
]

BUILDER_EDITS = [
    ("the D26 comment, above the imports",
     "\nimport csv\n",
     "\n# Session 33 (decision D26): written by insert_session33.py from the Session 32 snapshot\n"
     "# (neec_scores_csv_builder_v2_s32_snapshot.py). Ostrom-Style Commons Governance's row carries C3.2's\n"
     "# revision (Domain 3 2.5 -> 3.0, total 14.0 -> 14.5/26, failures 4 -> 3, tier unchanged), and its\n"
     "# notes are restated on the Session 33 corpus with decision D18(b)'s re-expressed register;\n"
     "# Universal Basic Income's notes name the three-way tie at 14.5/26. No other row changes.\n"
     "import csv\n"),
]

UBI_OLD = ("Now EXACTLY tied with Mutual Credit/LETS at 14.5/26 (56%) -- on opposite sides of the "
           "Structurally-Inadequate/Partially-Adequate boundary (7 failures vs. 3),")
UBI_NEW = ("Now EXACTLY tied with Mutual Credit/LETS and Ostrom-Style Commons Governance at 14.5/26 (56%) -- on "
           "opposite sides of the Structurally-Inadequate/Partially-Adequate boundary (7 failures vs. 3 and 3),")

OS_ROW = (
    OS, 2.0, 2.5, 3.0, 3.0, 4.0, 3, "Partially Adequate",
    "REVISED Session 33 (decision D26, after the first blind replication): C3.2 0.0 -> 0.5 -- C3.2's 0.0 band "
    "is reserved for an active inflationary mechanism with no counterbalancing element, and the Session 23 "
    "score rested on absence alone. D3 2.5/5 -> 3.0/5; total 14.0 -> 14.5/26 (54% -> 56%); failures 4 -> 3; "
    "no tier change. Scored Session 23, natively on the v2, 26-criterion structure -- not part of the 13-system "
    "legacy corpus and therefore not touched by Step 1c's retrofit.",
    "NEW ROW Session 25 (scoring completed Session 23, which closed Step 1b; inserted in the third consolidated "
    "pass); C3.2 revised Session 33 (decision D26). Scores the governance mechanism, not a country: Ostrom's "
    "eight design principles for common-pool-resource institutions, applied to resource systems embedded in a "
    "wider market economy; Nepal's community forestry programme is the principal national-scale case. Scale "
    "convention: generalisation, not best-casing -- scored as though every common-pool resource in an economy "
    "were so governed, with population-scope thresholds applied to the economy-wide outcome. Three scope "
    "scenarios, reported and never scored (decision D18(b)): the knowledge and digital commons counted in "
    "(15.5/26, 2 failures, Potentially Adequate); community land trusts counted out (14.0/26, 4 failures, "
    "Partially Adequate); thresholds read against the governed resource and its members (16.0/26, 3 failures, "
    "Partially Adequate). Three failures (C1.2a, C1.5, C2.2), none undisputed: each has a stated alternative "
    "that removes it. Fifteen flagged calls (32,768 combinations; 65.6% keep the scored tier) span 10.5 to "
    "18.0/26 and all three tiers; the joint readings are the register's extremes (decision D16): every call "
    "resolved upward, 18.0/26 with 0 failures (Potentially Adequate), and every call resolved downward, "
    "10.5/26 with 9 failures (Structurally Inadequate). By the D13 measure the corpus's least tier-robust "
    "entry. Archetype, as decided in the evaluation: a fifth narrow single-mechanism system, the corpus's first "
    "collectively held, non-severable stock, and the only one that governs a resource directly rather than "
    "intermediating value. Joint-best C5.5 (1.0). Domain 5 (4.0/5) is beaten only by CCO-PTF-CIP-SZH and "
    "Islamic Finance / Profit-Sharing Banking (4.5 each); Domain 1 (2.0/6) is below 14 of the other 22 "
    "systems. Exact three-way tie at 14.5/26 with Mutual Credit / LETS and Universal Basic Income, across two "
    "tiers (3, 3, and 7 failures). Dominated by no system, CCO-PTF-CIP-SZH included (it exceeds "
    "CCO-PTF-CIP-SZH on C5.5 alone), and dominates none. Full rationale: NEEC_Ostrom_Commons_scoring_scratch.md; "
    "pre-insertion verification: verify_ostrom.py; claim-survival audit: audit_claim_survival_s25.py; D26 "
    "insertion: verify_insertion_s33.py. Report System 23 [pending renumbering]; not yet in Report Part I or "
    "Part II.")


def pinned(indir, name, md5):
    p = os.path.join(indir, name)
    if not os.path.isfile(p):
        sys.exit(f"ERROR: cannot find {name}")
    raw = open(p, "rb").read()
    got = hashlib.md5(raw).hexdigest()[:8]
    if got != md5:
        sys.exit(f"ERROR: {name} md5 {got}, expected {md5}")
    return raw.decode("utf-8")


def replace_once(text, old, new, what, problems):
    n = text.count(old)
    if n != 1:
        problems.append(f"{what}: anchor occurs {n} times")
        return text
    return text.replace(old, new)


def chunks(s, width=84):
    """Split a string into pieces of at most `width` characters, breaking after spaces (the builder's layout)."""
    out, cur = [], ""
    for word in s.split(" "):
        piece = word if not cur else cur + " " + word
        if cur and len(piece) + 1 > width:
            out.append(cur + " ")
            cur = word
        else:
            cur = piece
    out.append(cur)
    return out


def render_row(v):
    head = (f"    ({json.dumps(v[0], ensure_ascii=False)}, {v[1]!r}, {v[2]!r}, {v[3]!r}, {v[4]!r}, {v[5]!r}, "
            f"{v[6]!r}, {json.dumps(v[7], ensure_ascii=False)},")
    lines = [head]
    for i, s in enumerate(v[8:]):
        for c in chunks(s):
            lines.append("     " + json.dumps(c, ensure_ascii=False))
        lines[-1] += "," if i == 0 else "),"
    return "\n".join(lines)


def row_span(src, name):
    """(first line, last line) of the builder's data tuple for `name`, 1-based, from the parsed source."""
    found = [n for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Tuple) and len(n.elts) == 10
             and isinstance(n.elts[0], ast.Constant) and n.elts[0].value == name]
    if len(found) != 1:
        sys.exit(f"ERROR: {len(found)} rows for {name!r} in the builder")
    return found[0].lineno, found[0].end_lineno, ast.literal_eval(found[0])


def splice(src, name, new_value, problems):
    a, b, _ = row_span(src, name)
    lines = src.split("\n")
    rendered = render_row(new_value)
    if ast.literal_eval(rendered.strip().rstrip(",")) != tuple(new_value):
        problems.append(f"{name}: the re-rendered row does not parse back to its value")
    return "\n".join(lines[:a - 1] + rendered.split("\n") + lines[b:])


def main(argv):
    indir = argv[0] if len(argv) > 0 else "."
    outdir = argv[1] if len(argv) > 1 else "out"
    print("=" * 96)
    print("insert_session33.py -- decision D26: Ostrom-Style Commons Governance's C3.2, 0.0 -> 0.5")
    print("=" * 96)
    problems = []
    out = {}
    canon = pinned(indir, *SNAP[CANON])
    for what, old, new in CANON_EDITS:
        canon = replace_once(canon, old, new, f"{CANON}: {what}", problems)
        print(f"  {CANON}: {what}")
    out[CANON] = canon
    builder = pinned(indir, *SNAP[BUILDER])
    for what, old, new in BUILDER_EDITS:
        builder = replace_once(builder, old, new, f"{BUILDER}: {what}", problems)
        print(f"  {BUILDER}: {what}")
    _, _, ubi = row_span(builder, "Universal Basic Income")
    if ubi[9].count(UBI_OLD) != 1:
        problems.append("Universal Basic Income: the tie sentence is not found once in its notes")
    builder = splice(builder, "Universal Basic Income", ubi[:9] + (ubi[9].replace(UBI_OLD, UBI_NEW),), problems)
    print(f"  {BUILDER}: Universal Basic Income's notes name the three-way tie at 14.5/26")
    _, _, old_os = row_span(builder, OS)
    if old_os[:3] + old_os[4:6] + old_os[7:8] != OS_ROW[:3] + OS_ROW[4:6] + OS_ROW[7:8] \
            or (old_os[3], old_os[6]) != (2.5, 4):
        problems.append(f"{OS}: the snapshot row is not the Session 32 row this pass revises")
    builder = splice(builder, OS, OS_ROW, problems)
    print(f"  {BUILDER}: {OS}'s row (Domain 3 3.0, 3 failures, revision note, notes restated)")
    out[BUILDER] = builder
    for name, text in out.items():
        try:
            ast.parse(text)
        except SyntaxError as err:
            problems.append(f"{name}: does not parse ({err})")
    if problems:
        print("\nPROBLEMS (nothing written):")
        for p in problems:
            print(f"  - {p}")
        return 1
    os.makedirs(outdir, exist_ok=True)
    print()
    for name, text in out.items():
        data = text.encode("utf-8")
        with open(os.path.join(outdir, name), "wb") as f:
            f.write(data)
        print(f"wrote {name} (md5 {hashlib.md5(data).hexdigest()[:8]})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
