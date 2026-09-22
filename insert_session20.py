#!/usr/bin/env python3
"""
insert_session20.py -- NEEC Session 20, consolidated insertion pass
=====================================================================
Inserts three Step 1b systems into the two canonical v2 scripts:

  18. Sovereign Wealth Fund Statism                                  (scored Session 17)
  19. State Capitalism / China (Party-State-Directed Market Economy) (scored Session 18)
  20. State Capitalism / Singapore (GLC Developmental Capitalism)    (scored Session 19)

NO VECTOR IS RETYPED. Each 26-criterion vector, and the domain totals its
scratch document states, is extracted by AST parsing (never executed) from
the module-level literals of the verification script that checked it
against that document: verify_swf.py (SWF, SWF_PUBLISHED), verify_china.py
(CHINA, PUBLISHED), and verify_singapore.py (SG, PUBLISHED). The dict text,
the PUBLISHED lines, and the CSV builder's numeric fields are all generated
from those extracted values. Every edit is an anchored replacement that must
match its input exactly once, so the script refuses to run on anything but
the pinned Session 16 inputs.

INPUTS (SRC_DIR, default: this script's own directory)
  neec_weighting_robustness_analysis_v2_s16_snapshot.py   pinned by MD5
  neec_scores_csv_builder_v2_s16_snapshot.py              pinned by MD5
  verify_swf.py, verify_china.py, verify_singapore.py     vector sources

OUTPUTS (OUT_DIR, default: the current working directory)
  neec_weighting_robustness_analysis_v2.py   (20 systems)
  neec_scores_csv_builder_v2.py              (20 systems)

Afterwards, run neec_scores_csv_builder_v2.py inside OUT_DIR to regenerate
neec_scores.csv, then verify_insertion_s20.py to check the whole result.
Re-running this script on the same inputs reproduces both outputs byte for
byte (run_all_checks.py confirms this).

Usage: python3 insert_session20.py [SRC_DIR] [OUT_DIR]
"""
import ast
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
OUT = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.getcwd()

CANON_IN = "neec_weighting_robustness_analysis_v2_s16_snapshot.py"
BUILDER_IN = "neec_scores_csv_builder_v2_s16_snapshot.py"
CANON_OUT = "neec_weighting_robustness_analysis_v2.py"
BUILDER_OUT = "neec_scores_csv_builder_v2.py"
PINNED_MD5 = {
    CANON_IN: "1f2c9cd207fa67e0fda1931985311454",
    BUILDER_IN: "ee48e609a1da9c5350b34f3fa67d3a69",
}

D1 = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5']
DOMAINS = [D1] + [[f'C{d}.{i}' for i in range(1, 6)] for d in range(2, 6)]
ALL_CRITS = [c for g in DOMAINS for c in g]


def read(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()


def module_literal(name, var):
    """Module-level literal assigned to `var` in SRC/name (parsed, not executed)."""
    tree = ast.parse(read(name))
    hits = [ast.literal_eval(node.value) for node in tree.body
            if isinstance(node, ast.Assign)
            and any(getattr(t, "id", None) == var for t in node.targets)]
    if len(hits) != 1:
        sys.exit(f"ERROR: expected one module-level assignment to {var} in {name}, found {len(hits)}")
    return hits[0]


def tier(n):
    return ('Potentially Adequate' if n <= 2 else
            'Partially Adequate' if n <= 5 else 'Structurally Inadequate')


# ---------------------------------------------------------------------------
# 1. Pinned inputs
# ---------------------------------------------------------------------------
for name, digest in PINNED_MD5.items():
    got = hashlib.md5(read(name).encode("utf-8")).hexdigest()
    if got != digest:
        sys.exit(f"ERROR: {name} has MD5 {got}, expected {digest} (the Session 16 canonical file)")

# ---------------------------------------------------------------------------
# 2. Extract and self-check the three vectors
# ---------------------------------------------------------------------------
REVNOTE = ("N/A (scored Session {s}, natively on the v2, 26-criterion structure -- not part of the "
           "13-system legacy corpus and therefore not touched by Step 1c's retrofit).")

NEW = [
    {'key': 'Sovereign Wealth Fund Statism',
     'display': 'Sovereign Wealth Fund Statism',
     'source': 'verify_swf.py', 'vec': 'SWF', 'pub': 'SWF_PUBLISHED',
     'session': 17, 'failures': 3},
    {'key': 'State Capitalism / China',
     'display': 'State Capitalism / China (Party-State-Directed Market Economy)',
     'source': 'verify_china.py', 'vec': 'CHINA', 'pub': 'PUBLISHED',
     'session': 18, 'failures': None},
    {'key': 'State Capitalism / Singapore',
     'display': 'State Capitalism / Singapore (GLC Developmental Capitalism)',
     'source': 'verify_singapore.py', 'vec': 'SG', 'pub': 'PUBLISHED',
     'session': 19, 'failures': None},
]

for s in NEW:
    v = module_literal(s['source'], s['vec'])
    p = module_literal(s['source'], s['pub'])
    if list(v) != ALL_CRITS or any(x not in (0.0, 0.5, 1.0) for x in v.values()):
        sys.exit(f"ERROR: {s['vec']} in {s['source']} is not a 26-criterion vector in canonical order")
    sums = [sum(v[c] for c in g) for g in DOMAINS]
    stated = [p[f'D{i}'] for i in range(1, 6)]
    if any(abs(a - b) > 1e-9 for a, b in zip(sums, stated)) or abs(sum(sums) - p['Total']) > 1e-9:
        sys.exit(f"ERROR: {s['key']} does not re-sum to the totals stated in {s['source']}")
    n_fail = sum(v[c] == 0.0 for c in ALL_CRITS)
    expected_fail = p.get('Failures', s['failures'])
    if n_fail != expected_fail or ('Tier' in p and p['Tier'] != tier(n_fail)):
        sys.exit(f"ERROR: {s['key']} failure count/tier disagrees with {s['source']}")
    s.update(v=v, sums=sums, total=sum(sums), n_fail=n_fail, tier=tier(n_fail),
             revnote=REVNOTE.format(s=s['session']))

# ---------------------------------------------------------------------------
# 3. Row notes (prose; every comparative claim is checked in verify_insertion_s20.py)
# ---------------------------------------------------------------------------
NEW[0]['notes'] = (
    "NEW ROW Session 20 (scoring completed Session 17; held under the scratch-before-insert "
    "discipline, then inserted together with the two state-capitalism rows below in one "
    "consolidated pass). Scores the fund mechanism itself -- Norway's budget-support model and "
    "Alaska's per-capita dividend model -- as a general design layered onto an otherwise-"
    "unmodified market economy, not any whole national economy (the Gulf SWF states are a "
    "separate, still-unscored state-capitalism sub-entry). Three failures (C1.3, C4.2, C4.5), "
    "none in the wealth cluster: the first Step 1b system scored without a failure on C1.2a, "
    "C1.2b, or C1.5, because its mechanism is an accumulating stock rather than a recurring "
    "flow -- the sub-distinction this evaluation introduced within the narrow single-mechanism "
    "archetype. C4.2 fails on the fossil-fuel funding base. The most consequential flagged call "
    "(C1.2a, with C1.5 tracking it) is tier-neutral: resolving both to 0.0 gives 13.0/26 with 5 "
    "failures, still Partially Adequate. Ties State Capitalism / Singapore exactly at 14.0/26, "
    "in the same tier with a different failure count (3 vs. 4); the two vectors differ on 7 "
    "criteria and share failures C4.2 and C4.5. Strictly dominated only by CCO-PTF-CIP-SZH; "
    "dominates no system (checked against all 19 others in verify_insertion_s20.py). Full "
    "rationale: NEEC_SovereignWealthFundStatism_scoring_scratch.md; pre-insertion verification: "
    "verify_swf.py. Report System 18 [pending renumbering]; not yet in Report Part I or Part II."
)
NEW[1]['notes'] = (
    "NEW ROW Session 20 (scoring completed Session 18). The first of three state-capitalism "
    "sub-entries (Singapore below; the Gulf SWF states remain to be scored), each scored as a "
    "configured national political economy rather than a single mechanism; 'state capitalism' "
    "is used as a taxonomic label only, with a normative-commitment disclosure (Paper Section "
    "2.2). Eight failures (C2.1, C2.2, C2.4, C3.5, C4.2, C4.3, C4.4, C4.5): five undisputed and "
    "three flagged (C3.5, C4.2, C4.3). The tier depends jointly on those three -- Structurally "
    "Inadequate whenever at least one stands at 0.0, Partially Adequate (5 failures) only if all "
    "three resolve upward -- the corpus's first jointly dependent tier finding; with all nine "
    "flagged calls read upward the result is 13.0/26 with 5 failures. No Domain 1 failures "
    "(3.0/6). Domain 4 (0.5/5) ties Status Quo Market Capitalism for the corpus's lowest; "
    "Domain 2 (1.0/5) is second-lowest, above only Centrally Planned Socialism. Exact three-way "
    "tie at 10.0/26 with Centrally Planned Socialism and Stakeholder Capitalism, with three "
    "different failure counts (8, 12, 9) in one tier. Strictly dominated by CCO-PTF-CIP-SZH and "
    "by State Capitalism / Singapore; dominates no system. Full rationale: "
    "NEEC_StateCapitalism_China_scoring_scratch.md; pre-insertion verification: "
    "verify_china.py. Report System 19 [pending renumbering]; not yet in Report Part I or "
    "Part II."
)
NEW[2]['notes'] = (
    "NEW ROW Session 20 (scoring completed Session 19). Scores Singapore's political economy as "
    "configured in September 2026, informed by the record since independence in 1965; 'state "
    "capitalism' is used as a taxonomic label only (the scratch document also discloses the "
    "government's preference for 'state-owned enterprise' over 'GLC'). The population scope "
    "includes non-residents, because the low-wage Work Permit workforce is a designed, "
    "load-bearing feature of the model (paralleling China's hukou migrants); a citizen-and-PR-"
    "only reading raises C1.5 to 1.0 and C4.5 to 0.5 (15.0/26, 3 failures, same tier). Four "
    "failures (C2.2, C4.2, C4.4, C4.5): no flagged call disputes C2.2 or C4.5 (C4.5 moves only "
    "under the scope reading), C4.2 and C4.4 are flagged upward, and four passing-side calls "
    "(C2.1, C2.4, C3.5, C4.3) are flagged downward. The tier is Partially Adequate exactly when "
    "one to three of those six tier-relevant calls stand at 0.0 (the primary reading has two), "
    "and the joint readings span all three tiers (16.5/26 with 2 failures upward; 10.5/26 with 8 "
    "downward) -- the corpus's first two-directional tier sensitivity and its weakest tier "
    "robustness. Domain 1 (4.0/6) is the Step 1b cohort's highest, and this is the first Step 1b "
    "system to pass C1.2a or C1.3. Strictly dominates State Capitalism / China (higher on 8 "
    "criteria, lower on none; its 4 failures are a strict subset of China's 8, and the four "
    "China failures it avoids are exactly its four downward-flagged calls); strictly dominated "
    "only by CCO-PTF-CIP-SZH. Ties Sovereign Wealth Fund Statism exactly at 14.0/26 (same tier; "
    "4 vs. 3 failures). Full rationale: NEEC_StateCapitalism_Singapore_scoring_scratch.md; "
    "pre-insertion verification: verify_singapore.py. Report System 20 [pending renumbering]; "
    "not yet in Report Part I or Part II."
)

# ---------------------------------------------------------------------------
# 4. Formatters (reproduce the canonical files' existing layout exactly)
# ---------------------------------------------------------------------------
def scores_block(s):
    lines = [f"    '{s['key']}': {{"]
    for g in DOMAINS:
        lines.append("        " + ",".join(f"'{c}':{s['v'][c]:.1f}" for c in g) + ",")
    lines.append("    },")
    return "\n".join(lines) + "\n"


def published_line(s):
    d = s['sums']
    key = f"'{s['key']}':"
    return (f"    {key:<37}{{'D1':{d[0]:.1f},'D2':{d[1]:.1f},'D3':{d[2]:.1f},"
            f"'D4':{d[3]:.1f},'D5':{d[4]:.1f},'Total':{s['total']:.1f}}},\n")


def string_lines(text, width=88):
    """Split text into implicitly concatenated literals whose join is exactly `text`."""
    if '"' in text or '\\' in text:
        sys.exit("ERROR: row text may not contain double quotes or backslashes")
    words, chunks, cur = text.split(" "), [], ""
    for i, w in enumerate(words):
        piece = w + (" " if i < len(words) - 1 else "")
        if cur and len(cur) + len(piece) > width:
            chunks.append(cur)
            cur = ""
        cur += piece
    chunks.append(cur)
    assert "".join(chunks) == text
    return [f'     "{c}"' for c in chunks]


def builder_row(s):
    d = s['sums']
    head = (f'    ("{s["display"]}", {d[0]:.1f}, {d[1]:.1f}, {d[2]:.1f}, {d[3]:.1f}, '
            f'{d[4]:.1f}, {s["n_fail"]}, "{s["tier"]}",')
    rev = string_lines(s['revnote'])
    rev[-1] += ","
    notes = string_lines(s['notes'])
    notes[-1] += "),"
    return "\n".join([head] + rev + notes) + "\n"


def apply(text, edits, label):
    for old, new in edits:
        n = text.count(old)
        if n != 1:
            sys.exit(f"ERROR ({label}): anchor found {n} times, expected once:\n{old[:200]}")
        text = text.replace(old, new)
    return text


# ---------------------------------------------------------------------------
# 5. Canonical script edits
# ---------------------------------------------------------------------------
CANON_DOC_OLD = """scoring and Session 9-10 regeneration.

Run: python3 neec_weighting_robustness_analysis_v2.py
"""
CANON_DOC_NEW = """scoring and Session 9-10 regeneration.

SESSION 20 UPDATE: three further Step 1b systems -- Sovereign Wealth Fund
Statism (scored Session 17), State Capitalism / China (Session 18), and
State Capitalism / Singapore (Session 19) -- are added here in one
consolidated insertion pass, bringing the corpus from 17 to 20 systems,
all on the identical 26-criterion v2 structure. None of the three vectors
was retyped: each was extracted by AST parsing from the verification
script that checked it against its own scratch document (verify_swf.py,
verify_china.py, verify_singapore.py), formatted programmatically by
`insert_session20.py`, and re-verified after insertion by
`verify_insertion_s20.py`, which also confirms that the 17 previously
canonical systems are unchanged from the Session 16 snapshot
(`neec_weighting_robustness_analysis_v2_s16_snapshot.py`). No new scoring
judgment is exercised by this update. As after Sessions 8 and 16, this
script's canonical DATA is again ahead of the Report's and Paper's prose,
which include none of the five systems scored since Session 14; that
regeneration remains queued as "Step 5 (expanded)".

Run: python3 neec_weighting_robustness_analysis_v2.py
"""

CANON_SYSTEMS_OLD = """# `verify_new_systems.py`, produced in the same session as this update).
# ---------------------------------------------------------------------------
SCORES = {
"""
CANON_SYSTEMS_NEW = """# `verify_new_systems.py`, produced in the same session as this update).
#
# Systems 18-20 (Sovereign Wealth Fund Statism, State Capitalism / China,
# State Capitalism / Singapore): added Session 20, natively on the v2
# structure since first scored (Sessions 17, 18, and 19). Extracted by AST
# from verify_swf.py, verify_china.py, and verify_singapore.py (not
# retyped) and re-verified after insertion (see verify_insertion_s20.py).
# Short keys here; the CSV carries the confirmed display names.
# ---------------------------------------------------------------------------
SCORES = {
"""

CANON_SCORES_OLD = """        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
}

PUBLISHED = {
"""
CANON_SCORES_NEW = (
    """        'C5.1':1.0,'C5.2':0.5,'C5.3':1.0,'C5.4':0.5,'C5.5':0.5,
    },
    # --- Session 20 additions below: all three scored natively on the v2
    # structure (Sessions 17-19), so none has retrofit history. China and
    # Singapore are the first two of three state-capitalism sub-entries; the
    # Gulf SWF states are still to be scored. ---
"""
    + "".join(scores_block(s) for s in NEW)
    + """}

PUBLISHED = {
"""
)

CANON_PUB_OLD = """    'Universal Basic Services':          {'D1':1.5,'D2':3.0,'D3':3.0,'D4':2.5,'D5':3.5,'Total':13.5},
}
"""
CANON_PUB_NEW = (
    """    'Universal Basic Services':          {'D1':1.5,'D2':3.0,'D3':3.0,'D4':2.5,'D5':3.5,'Total':13.5},
"""
    + "".join(published_line(s) for s in NEW)
    + "}\n"
)

CANON_PAIRS_OLD = """        ('CCO-PTF-CIP-SZH', 'Universal Basic Services'),
    ]
"""
CANON_PAIRS_NEW = """        ('CCO-PTF-CIP-SZH', 'Universal Basic Services'),
        # Session 20 additions. State Capitalism / Singapore ties Sovereign
        # Wealth Fund Statism exactly (14.0/26), and State Capitalism / China
        # ties Centrally Planned Socialism and Stakeholder Capitalism exactly
        # (10.0/26), so none of those three pairs can be a dominance relation;
        # they are listed to show how each tie behaves under the alternative
        # schemes. Singapore strictly dominates China (verify_singapore.py).
        ('State Capitalism / Singapore', 'Sovereign Wealth Fund Statism'),
        ('State Capitalism / Singapore', 'State Capitalism / China'),
        ('State Capitalism / China', 'Centrally Planned Socialism'),
        ('State Capitalism / China', 'Stakeholder Capitalism'),
        ('CCO-PTF-CIP-SZH', 'Sovereign Wealth Fund Statism'),
        ('CCO-PTF-CIP-SZH', 'State Capitalism / China'),
        ('CCO-PTF-CIP-SZH', 'State Capitalism / Singapore'),
    ]
"""

canon = apply(read(CANON_IN), [
    (CANON_DOC_OLD, CANON_DOC_NEW),
    ("# SOURCE DATA -- 17 systems, all on the 26-criterion v2 structure.",
     "# SOURCE DATA -- 20 systems, all on the 26-criterion v2 structure."),
    (CANON_SYSTEMS_OLD, CANON_SYSTEMS_NEW),
    (CANON_SCORES_OLD, CANON_SCORES_NEW),
    (CANON_PUB_OLD, CANON_PUB_NEW),
    (CANON_PAIRS_OLD, CANON_PAIRS_NEW),
], "canonical script")

# ---------------------------------------------------------------------------
# 6. CSV builder edits
# ---------------------------------------------------------------------------
BUILDER_DOC_OLD = """rather than one at a time.

CROSS-VALIDATION: every domain/total figure below (all 17 systems) is
"""
BUILDER_DOC_NEW = """rather than one at a time.

SESSION 20 UPDATE: three further rows added in a second consolidated
insertion pass -- Sovereign Wealth Fund Statism (scored Session 17), State
Capitalism / China (Session 18), and State Capitalism / Singapore
(Session 19) -- bringing the builder from 17 to 20 systems, all natively
on the v2, 26-criterion structure. Their D1-D5/failures/tier values were
computed from the AST-extracted vectors by `insert_session20.py`, not
retyped, and are cross-validated below against
`neec_weighting_robustness_analysis_v2.py`'s own (also Session-20-updated)
PUBLISHED dict and SCORES vectors. The display names are the ones the
China and Singapore scratch documents proposed, confirmed by the user at
the start of Session 20; Sovereign Wealth Fund Statism keeps its scratch
title. The 17 existing rows are unchanged, and verify_insertion_s20.py
checks that they are byte-identical to the Session 16 CSV.

CROSS-VALIDATION: every domain/total figure below (all 20 systems) is
"""

BUILDER_ROWS_OLD = """     "world). Report System 17 [pending renumbering]; not yet in Report Part I or Part II."),
]
"""
BUILDER_ROWS_NEW = (
    """     "world). Report System 17 [pending renumbering]; not yet in Report Part I or Part II."),
    # --- Session 20 additions below (the second consolidated review/insert pass: three
    # Step 1b systems scored in Sessions 17-19, held as scratch until now) ---
"""
    + "".join(builder_row(s) for s in NEW)
    + "]\n"
)

BUILDER_MAP_OLD = """    "Universal Basic Services": "Universal Basic Services",
}
"""
BUILDER_MAP_NEW = (
    """    "Universal Basic Services": "Universal Basic Services",
"""
    + "".join(f'    "{s["display"]}": "{s["key"]}",\n' for s in NEW)
    + "}\n"
)

BUILDER_END_OLD = """      "Sessions 9-10 regeneration).")
"""
BUILDER_END_NEW = """      "Sessions 9-10 regeneration).")
print("\\nSession 20: Sovereign Wealth Fund Statism, State Capitalism / China, and State "
      "Capitalism / Singapore added (rows 18-20), bringing the canonical CSV from 17 to 20 "
      "systems. Report and Paper regeneration for all five systems scored since Session 14 "
      "remains queued as 'Step 5 (expanded)'.")
"""

builder = apply(read(BUILDER_IN), [
    (BUILDER_DOC_OLD, BUILDER_DOC_NEW),
    ("# All 17 systems, now uniformly on the 26-criterion structure.",
     "# All 20 systems, now uniformly on the 26-criterion structure."),
    (BUILDER_ROWS_OLD, BUILDER_ROWS_NEW),
    (BUILDER_MAP_OLD, BUILDER_MAP_NEW),
    (BUILDER_END_OLD, BUILDER_END_NEW),
], "CSV builder")

# ---------------------------------------------------------------------------
# 7. Write
# ---------------------------------------------------------------------------
os.makedirs(OUT, exist_ok=True)
for name, text in ((CANON_OUT, canon), (BUILDER_OUT, builder)):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {name}  md5 {hashlib.md5(text.encode('utf-8')).hexdigest()}")
for s in NEW:
    d = s['sums']
    print(f"  {s['key']:<30} D1-D5 {d}  total {s['total']:.1f}/26  "
          f"{s['n_fail']} failures  {s['tier']}   <- {s['source']}")
