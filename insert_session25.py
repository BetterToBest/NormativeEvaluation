#!/usr/bin/env python3
"""
insert_session25.py -- NEEC Session 25, third consolidated insertion pass
=========================================================================
Inserts the last three Step 1b systems into the two canonical v2 scripts,
closing Step 1b:

  21. State Capitalism / Qatar (Gulf Rentier-Distributive Statism)   (scored Session 21)
  22. Islamic Finance / Profit-Sharing Banking                       (scored Session 22)
  23. Ostrom-Style Commons Governance                                (scored Session 23)

NO VECTOR IS RETYPED. Each 26-criterion vector is extracted by AST parsing
(never executed) from the module-level literal of the verification script
that checked it against its scratch document: verify_qatar.py (QA, plus its
PUBLISHED summary), verify_islamicfinance.py (SCORE), verify_ostrom.py
(OSTROM). Each vector is then re-summed against the summary its OWN scratch
document states -- five domain totals, the total, the percentage, and the
failure count -- read by the three-layout parser below (the three documents
state their summaries in three different layouts; decision D3(a) retires
this parser once every scoring document carries one machine-readable
summary block). Every edit is an anchored replacement that must match its
input exactly once, so the script refuses to run on anything but the pinned
Session 20 inputs, and refuses any vector that disagrees with its document.

INPUTS (SRC_DIR, default: this script's own directory)
  neec_weighting_robustness_analysis_v2_s20_snapshot.py   pinned by MD5
  neec_scores_csv_builder_v2_s20_snapshot.py              pinned by MD5
  verify_qatar.py, verify_islamicfinance.py, verify_ostrom.py   vector sources
  the three scratch documents                                   stated summaries

OUTPUTS (OUT_DIR, default: the current working directory)
  neec_weighting_robustness_analysis_v2.py   (23 systems)
  neec_scores_csv_builder_v2.py              (23 systems)

The three row notes carry 23-system comparative claims only. The three
entries were scored against the 20-system corpus one at a time, so their
documents' comparative claims are 21-system claims; audit_claim_survival_s25.py
re-tests every one of them on the combined corpus, and verify_insertion_s25.py
asserts every claim the notes below make.

Afterwards, run neec_scores_csv_builder_v2.py inside OUT_DIR to regenerate
neec_scores.csv, then verify_insertion_s25.py to check the whole result.
Re-running this script on the same inputs reproduces both outputs byte for
byte (run_all_checks.py confirms this).

Usage: python3 insert_session25.py [SRC_DIR] [OUT_DIR]
"""
import ast
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else HERE
OUT = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.getcwd()

CANON_IN = "neec_weighting_robustness_analysis_v2_s20_snapshot.py"
BUILDER_IN = "neec_scores_csv_builder_v2_s20_snapshot.py"
CANON_OUT = "neec_weighting_robustness_analysis_v2.py"
BUILDER_OUT = "neec_scores_csv_builder_v2.py"
PINNED_MD5 = {
    CANON_IN: "487d5a94138f3f896c3f723498b6c0e9",
    BUILDER_IN: "5f547d0dcc44024b31629ffcf564453d",
}

D1 = ['C1.1', 'C1.2a', 'C1.2b', 'C1.3', 'C1.4', 'C1.5']
DOMAINS = [D1] + [[f'C{d}.{i}' for i in range(1, 6)] for d in range(2, 6)]
ALL_CRITS = [c for g in DOMAINS for c in g]
DOMAIN_NAMES = ["Material Security", "Human Autonomy", "System Resilience",
                "Ethical Integrity", "Implementation Viability"]


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
# The three-layout summary parser (see the docstring; retired by D3(a))
#   Qatar:            '- Material Security: 2.5/6 (42%)' ... '**Overall Score: 9.0/26 (35%)**',
#                     failures in a sentence that may wrap: '... and 10 at 0.0'
#   Islamic finance:  '| Material Security | 2.0 | 6 |' ... '**Total: 13.5/26 (51.9%).
#                     Structural failures: 5 (...). Adequacy tier: ...**'
#   Ostrom:           '| Material Security | 2.0 | 6.0 |' ... '**Total: ... Tier: ...**'
# ---------------------------------------------------------------------------
TOTAL_RE = re.compile(r'^\*\*(?:Total|Overall Score): (\d+\.\d)/26 \((\d+(?:\.\d)?)%\)')


def stated_summary(doc):
    lines = read(doc).split("\n")
    hits = [i for i, line in enumerate(lines) if TOTAL_RE.match(line)]
    if len(hits) != 1:
        sys.exit(f"ERROR: {doc}: expected exactly one total line, found {len(hits)}")
    i = hits[0]
    m = TOTAL_RE.match(lines[i])
    domains = []
    for name in DOMAIN_NAMES:
        rx = re.compile(r'^(?:\| |- )' + re.escape(name) + r'(?: \| |: )(\d+\.\d)\b')
        found = [float(rx.match(x).group(1)) for x in lines[max(0, i - 24):i] if rx.match(x)]
        if len(found) != 1:
            sys.exit(f"ERROR: {doc}: expected one '{name}' line above the total, found {len(found)}")
        domains.append(found[0])
    blob = " ".join(" ".join(lines[i:i + 9]).split())
    fm = re.search(r'Structural failures: (\d+) \(', blob) or re.search(r'and (\d+) at 0\.0', blob)
    if not fm:
        sys.exit(f"ERROR: {doc}: no failure count found at the total line")
    return {'domains': domains, 'total': float(m.group(1)), 'pct': m.group(2), 'failures': int(fm.group(1))}


# ---------------------------------------------------------------------------
# 1. Pinned inputs
# ---------------------------------------------------------------------------
for name, digest in PINNED_MD5.items():
    got = hashlib.md5(read(name).encode("utf-8")).hexdigest()
    if got != digest:
        sys.exit(f"ERROR: {name} has MD5 {got}, expected {digest} (the Session 20 canonical file)")

# ---------------------------------------------------------------------------
# 2. Extract each vector and check it against its own document's stated summary
# ---------------------------------------------------------------------------
REVNOTE = ("N/A (scored Session {s}, natively on the v2, 26-criterion structure -- not part of the "
           "13-system legacy corpus and therefore not touched by Step 1c's retrofit).")

NEW = [
    {'key': 'State Capitalism / Qatar',
     'display': 'State Capitalism / Qatar (Gulf Rentier-Distributive Statism)',
     'source': 'verify_qatar.py', 'vec': 'QA', 'pub': 'PUBLISHED',
     'doc': 'NEEC_StateCapitalism_Qatar_scoring_scratch.md', 'session': 21},
    {'key': 'Islamic Finance / Profit-Sharing Banking',
     'display': 'Islamic Finance / Profit-Sharing Banking',
     'source': 'verify_islamicfinance.py', 'vec': 'SCORE', 'pub': None,
     'doc': 'NEEC_IslamicFinance_scoring_scratch.md', 'session': 22},
    {'key': 'Ostrom-Style Commons Governance',
     'display': 'Ostrom-Style Commons Governance',
     'source': 'verify_ostrom.py', 'vec': 'OSTROM', 'pub': None,
     'doc': 'NEEC_Ostrom_Commons_scoring_scratch.md', 'session': 23},
]

for s in NEW:
    v = module_literal(s['source'], s['vec'])
    if list(v) != ALL_CRITS or any(x not in (0.0, 0.5, 1.0) for x in v.values()):
        sys.exit(f"ERROR: {s['vec']} in {s['source']} is not a 26-criterion vector in canonical order")
    sums = [sum(v[c] for c in g) for g in DOMAINS]
    n_fail = sum(v[c] == 0.0 for c in ALL_CRITS)
    doc = stated_summary(s['doc'])
    pct = f"{sum(sums) / 26 * 100:.1f}" if "." in doc['pct'] else str(round(sum(sums) / 26 * 100))
    if (any(abs(a - b) > 1e-9 for a, b in zip(sums, doc['domains'])) or abs(sum(sums) - doc['total']) > 1e-9
            or pct != doc['pct'] or n_fail != doc['failures']):
        sys.exit(f"ERROR: {s['key']}: the vector in {s['source']} disagrees with the summary stated in {s['doc']}")
    if s['pub']:
        p = module_literal(s['source'], s['pub'])
        stated = [p[f'D{i}'] for i in range(1, 6)]
        if (any(abs(a - b) > 1e-9 for a, b in zip(sums, stated)) or abs(sum(sums) - p['Total']) > 1e-9
                or p['Failures'] != n_fail or p['Tier'] != tier(n_fail)):
            sys.exit(f"ERROR: {s['key']} does not re-sum to the summary stated in {s['source']}")
    s.update(v=v, sums=sums, total=sum(sums), n_fail=n_fail, tier=tier(n_fail),
             revnote=REVNOTE.format(s=s['session']))

# ---------------------------------------------------------------------------
# 3. Row notes (23-system claims only; every claim is asserted in verify_insertion_s25.py)
# ---------------------------------------------------------------------------
NEW[0]['notes'] = (
    "NEW ROW Session 25 (scoring completed Session 21; held under the scratch-before-insert "
    "discipline, then inserted with Islamic Finance / Profit-Sharing Banking and Ostrom-Style "
    "Commons Governance in the third consolidated pass). The third and last state-capitalism "
    "sub-entry (the Gulf case, represented by Qatar), scored as a configured national political "
    "economy -- Qatar as configured in September 2026 -- with 'state capitalism' used as a "
    "taxonomic label only. Population scope: everyone who lives and works in Qatar, non-citizens "
    "included, because the migrant workforce is a designed, load-bearing feature of the "
    "configuration (the Singapore precedent). Ten failures (C1.5, C2.1, C2.2, C2.4, C3.5, C4.2, "
    "C4.3, C4.4, C4.5, C5.5), six undisputed (C2.2, C2.4, C4.2, C4.3, C4.4, C4.5). The twelve "
    "flagged calls are tier-neutral: all 4,096 combinations are Structurally Inadequate (8.0 to "
    "14.0/26). Population scope is the only lever that moves the tier: a citizens-only reading "
    "changes seven criteria and gives 13.0/26 with 6 failures, still Structurally Inadequate at "
    "the boundary, and 128 of the 256 combinations of the eight flagged calls it leaves open "
    "reach Partially Adequate (12.0 to 16.0/26). Domain 4 (0.5/5) ties State Capitalism / China "
    "and Status Quo Market Capitalism for the corpus's lowest. Ranks 22nd of 23, above only "
    "Libertarian Minarchism, and ties no system. Strictly dominated by exactly two systems -- "
    "CCO-PTF-CIP-SZH, and State Capitalism / Singapore (higher on 10 criteria, lower on none; "
    "Singapore's 4 failures are a subset of Qatar's 10) -- and dominates none. Full rationale: "
    "NEEC_StateCapitalism_Qatar_scoring_scratch.md; pre-insertion verification: verify_qatar.py; "
    "claim-survival audit: audit_claim_survival_s25.py. Report System 21 [pending renumbering]; "
    "not yet in Report Part I or Part II."
)
NEW[1]['notes'] = (
    "NEW ROW Session 25 (scoring completed Session 22; inserted in the third consolidated pass). "
    "Scores the mechanism, not a country: profit-and-loss-sharing finance (mudarabah and "
    "musharakah) with the prohibition of riba, layered onto an otherwise-unmodified market "
    "economy; Malaysia's dual system is the principal implementation case. The adjacent "
    "social-finance layer (zakat, waqf, takaful) is scored as a scope scenario (14.5/26, 4 "
    "failures, Partially Adequate). Five failures (C1.2b, C1.4, C2.2, C4.2, C4.4), two undisputed "
    "(C2.2, C4.2). Sixteen flagged calls (65,536 combinations); the three coherent joint readings "
    "span all three tiers: A, as designed, 15.5/26 with 2 failures (Potentially Adequate); B, as "
    "practised, the score here; C, strict form-over-substance, 10.5/26 with 11 failures "
    "(Structurally Inadequate). Domain 5 (4.5/5) equals CCO-PTF-CIP-SZH's, the corpus's highest, "
    "and no other system reaches it; its Domain 5 minus Domain 4 gap (3.0) is the corpus's "
    "second-widest, behind Status Quo Market Capitalism (3.5). Joint-best C5.5 (1.0), with "
    "Participatory Economics, Mutual Credit / LETS, and Ostrom-Style Commons Governance. Exact "
    "three-way tie at 13.5/26 with Georgism / Land Value Tax and Universal Basic Services, "
    "spanning two tiers (2, 3, and 5 failures); rank 13 of 23. Strictly dominates Stakeholder "
    "Capitalism alone (higher on 6 criteria, lower on none), the only Step 1b entry to dominate "
    "one of the 13 legacy systems. Dominated by no system, CCO-PTF-CIP-SZH included: it exceeds "
    "CCO-PTF-CIP-SZH on C5.5 alone, which is enough to block dominance. Full rationale: "
    "NEEC_IslamicFinance_scoring_scratch.md; pre-insertion verification: "
    "verify_islamicfinance.py; claim-survival audit: audit_claim_survival_s25.py. Report System "
    "22 [pending renumbering]; not yet in Report Part I or Part II."
)
NEW[2]['notes'] = (
    "NEW ROW Session 25 (scoring completed Session 23, which closed Step 1b; inserted in the "
    "third consolidated pass). Scores the governance mechanism, not a country: Ostrom's eight "
    "design principles for common-pool-resource institutions, applied to resource systems "
    "embedded in a wider market economy; Nepal's community forestry programme is the principal "
    "national-scale case. Scale convention: generalisation, not best-casing -- scored as though "
    "every common-pool resource in an economy were so governed, with population-scope thresholds "
    "applied to the economy-wide outcome. The knowledge and digital commons extension is adjacent "
    "and scored as a scope scenario (15.0/26, 3 failures, Partially Adequate). Four failures "
    "(C1.2a, C1.5, C2.2, C3.2), none undisputed: each has a stated alternative that removes it. "
    "Twenty flagged calls (1,048,576 combinations) span 9.5 to 19.5/26 and all three tiers; the "
    "coherent joint readings A (the long-enduring case: 19.5/26, 0 failures, Potentially "
    "Adequate) and C (strict population scope: 9.5/26, 11 failures, Structurally Inadequate) are "
    "exactly the enumeration's extremes. Archetype, as decided in the evaluation: a fifth narrow "
    "single-mechanism system, the corpus's first collectively held, non-severable stock, and the "
    "only one that governs a resource directly rather than intermediating value; it is the only "
    "system in the corpus at 0.0 on C3.2. Joint-best C5.5 (1.0). Domain 5 (4.0/5) is beaten only "
    "by CCO-PTF-CIP-SZH and Islamic Finance / Profit-Sharing Banking (4.5 each); Domain 1 (2.0/6) "
    "is below 14 of the other 22 systems. Exact three-way tie at 14.0/26 with Sovereign Wealth "
    "Fund Statism and State Capitalism / Singapore, all Partially Adequate (3, 4, and 4 "
    "failures). Dominated by no system, CCO-PTF-CIP-SZH included (it exceeds CCO-PTF-CIP-SZH on "
    "C5.5 alone), and dominates none. Full rationale: NEEC_Ostrom_Commons_scoring_scratch.md; "
    "pre-insertion verification: verify_ostrom.py; claim-survival audit: "
    "audit_claim_survival_s25.py. Report System 23 [pending renumbering]; not yet in Report Part "
    "I or Part II."
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
    key = f"{key:<37}" if len(key) < 37 else key + " "
    return (f"    {key}{{'D1':{d[0]:.1f},'D2':{d[1]:.1f},'D3':{d[2]:.1f},"
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
CANON_DOC_OLD = """regeneration remains queued as "Step 5 (expanded)".

Run: python3 neec_weighting_robustness_analysis_v2.py
"""
CANON_DOC_NEW = """regeneration remains queued as "Step 5 (expanded)".

SESSION 25 UPDATE: the last three Step 1b systems -- State Capitalism /
Qatar (scored Session 21), Islamic Finance / Profit-Sharing Banking
(Session 22), and Ostrom-Style Commons Governance (Session 23) -- are added
in a third consolidated insertion pass, bringing the corpus from 20 to 23
systems, all on the identical 26-criterion v2 structure, and closing Step
1b. As in Session 20, no vector was retyped: each was extracted by AST
parsing from the verification script that checked it against its own
scratch document (verify_qatar.py, verify_islamicfinance.py,
verify_ostrom.py), re-summed against that document's own stated domain
totals, total, and failure count, formatted programmatically by
`insert_session25.py`, and re-verified after insertion by
`verify_insertion_s25.py`, which also confirms that the 20 previously
canonical systems are unchanged from the Session 20 snapshot
(`neec_weighting_robustness_analysis_v2_s20_snapshot.py`). The three
entries were scored against the 20-system corpus one at a time and never
against each other, so every comparative claim in their documents was
re-tested on the combined corpus first (`audit_claim_survival_s25.py`),
and the CSV row notes carry 23-system claims only. No new scoring judgment
is exercised by this update. The Report's and Paper's prose now lag the
data by the eight systems scored since Session 14; that regeneration
remains queued as "Step 5 (expanded)".

Run: python3 neec_weighting_robustness_analysis_v2.py
"""

CANON_SYSTEMS_OLD = """# retyped) and re-verified after insertion (see verify_insertion_s20.py).
# Short keys here; the CSV carries the confirmed display names.
# ---------------------------------------------------------------------------
SCORES = {
"""
CANON_SYSTEMS_NEW = """# retyped) and re-verified after insertion (see verify_insertion_s20.py).
#
# Systems 21-23 (State Capitalism / Qatar, Islamic Finance / Profit-Sharing
# Banking, Ostrom-Style Commons Governance): added Session 25, natively on
# the v2 structure since first scored (Sessions 21, 22, and 23). Extracted
# by AST from verify_qatar.py, verify_islamicfinance.py, and verify_ostrom.py
# (not retyped), checked against each scratch document's stated summary, and
# re-verified after insertion (see verify_insertion_s25.py).
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
    # --- Session 25 additions below: all three scored natively on the v2
    # structure (Sessions 21-23), so none has retrofit history. Qatar is the
    # third and last state-capitalism sub-entry (the Gulf case); Islamic
    # finance and Ostrom-style commons governance close Step 1b. ---
"""
    + "".join(scores_block(s) for s in NEW)
    + """}

PUBLISHED = {
"""
)

CANON_PUB_OLD = """    'State Capitalism / Singapore':      {'D1':4.0,'D2':2.0,'D3':3.5,'D4':1.0,'D5':3.5,'Total':14.0},
}
"""
CANON_PUB_NEW = (
    """    'State Capitalism / Singapore':      {'D1':4.0,'D2':2.0,'D3':3.5,'D4':1.0,'D5':3.5,'Total':14.0},
"""
    + "".join(published_line(s) for s in NEW)
    + "}\n"
)

CANON_PAIRS_OLD = """        ('CCO-PTF-CIP-SZH', 'State Capitalism / Singapore'),
    ]
"""
CANON_PAIRS_NEW = """        ('CCO-PTF-CIP-SZH', 'State Capitalism / Singapore'),
        # Session 25 additions. Islamic Finance / Profit-Sharing Banking ties
        # Georgism and UBS exactly (13.5/26), and Ostrom-Style Commons
        # Governance ties SWF Statism and Singapore exactly (14.0/26), so none
        # of those four pairs can be a dominance relation; they show how each
        # tie behaves under the alternative schemes. Islamic finance strictly
        # dominates Stakeholder Capitalism, and Singapore strictly dominates
        # Qatar; Islamic finance and Ostrom dominate neither way (they differ
        # on 9 criteria), and China does not dominate Qatar. CCO-PTF-CIP-SZH
        # dominates Qatar but neither of the other two: it scores 1.0 on 23
        # criteria and 0.5 on C1.5, C4.5, and C5.5, and each of the 11 systems
        # it does not dominate -- these two included -- exceeds it on exactly
        # one of those three (both of these on C5.5). Every system dominated
        # by any system is also dominated by CCO-PTF-CIP-SZH, so the Pareto
        # frontier is exactly CCO-PTF-CIP-SZH plus those 11 (12 systems). All
        # of this is asserted in verify_insertion_s25.py.
        ('Islamic Finance / Profit-Sharing Banking', 'Georgism / Land Value Tax'),
        ('Islamic Finance / Profit-Sharing Banking', 'Universal Basic Services'),
        ('Islamic Finance / Profit-Sharing Banking', 'Stakeholder Capitalism'),
        ('Ostrom-Style Commons Governance', 'Sovereign Wealth Fund Statism'),
        ('Ostrom-Style Commons Governance', 'State Capitalism / Singapore'),
        ('Ostrom-Style Commons Governance', 'Islamic Finance / Profit-Sharing Banking'),
        ('State Capitalism / Singapore', 'State Capitalism / Qatar'),
        ('State Capitalism / China', 'State Capitalism / Qatar'),
        ('CCO-PTF-CIP-SZH', 'State Capitalism / Qatar'),
        ('CCO-PTF-CIP-SZH', 'Islamic Finance / Profit-Sharing Banking'),
        ('CCO-PTF-CIP-SZH', 'Ostrom-Style Commons Governance'),
    ]
"""

canon = apply(read(CANON_IN), [
    (CANON_DOC_OLD, CANON_DOC_NEW),
    ("# SOURCE DATA -- 20 systems, all on the 26-criterion v2 structure.",
     "# SOURCE DATA -- 23 systems, all on the 26-criterion v2 structure."),
    (CANON_SYSTEMS_OLD, CANON_SYSTEMS_NEW),
    (CANON_SCORES_OLD, CANON_SCORES_NEW),
    (CANON_PUB_OLD, CANON_PUB_NEW),
    (CANON_PAIRS_OLD, CANON_PAIRS_NEW),
], "canonical script")

# ---------------------------------------------------------------------------
# 6. CSV builder edits
# ---------------------------------------------------------------------------
BUILDER_DOC_OLD = """checks that they are byte-identical to the Session 16 CSV.

CROSS-VALIDATION: every domain/total figure below (all 20 systems) is
"""
BUILDER_DOC_NEW = """checks that they are byte-identical to the Session 16 CSV.

SESSION 25 UPDATE: three further rows added in a third consolidated
insertion pass -- State Capitalism / Qatar (scored Session 21), Islamic
Finance / Profit-Sharing Banking (Session 22), and Ostrom-Style Commons
Governance (Session 23) -- bringing the builder from 20 to 23 systems, all
natively on the v2, 26-criterion structure, and closing Step 1b. Their
D1-D5/failures/tier values were computed from the AST-extracted vectors by
`insert_session25.py` (each vector re-summed against its own scratch
document's stated summary), not retyped, and are cross-validated below
against `neec_weighting_robustness_analysis_v2.py`'s own (also
Session-25-updated) PUBLISHED dict and SCORES vectors. Display names follow
decision D10: Qatar carries the name its scratch document proposed; the
other two keep their scratch titles. Their notes carry 23-system
comparative claims only, each asserted in verify_insertion_s25.py, after
audit_claim_survival_s25.py re-tested the three documents' 21-system claims
on the combined corpus. The 20 existing rows are unchanged, and
verify_insertion_s25.py checks that they are byte-identical to the Session
20 CSV.

CROSS-VALIDATION: every domain/total figure below (all 23 systems) is
"""

BUILDER_ROWS_OLD = """     "Report Part I or Part II."),
]
"""
BUILDER_ROWS_NEW = (
    """     "Report Part I or Part II."),
    # --- Session 25 additions below (the third consolidated review/insert pass: the last
    # three Step 1b systems, scored in Sessions 21-23 and held as scratch until now) ---
"""
    + "".join(builder_row(s) for s in NEW)
    + "]\n"
)

BUILDER_MAP_OLD = """    "State Capitalism / Singapore (GLC Developmental Capitalism)": "State Capitalism / Singapore",
}
"""
BUILDER_MAP_NEW = (
    """    "State Capitalism / Singapore (GLC Developmental Capitalism)": "State Capitalism / Singapore",
"""
    + "".join(f'    "{s["display"]}": "{s["key"]}",\n' for s in NEW)
    + "}\n"
)

BUILDER_END_OLD = """      "remains queued as 'Step 5 (expanded)'.")
"""
BUILDER_END_NEW = """      "remains queued as 'Step 5 (expanded)'.")
print("\\nSession 25: State Capitalism / Qatar, Islamic Finance / Profit-Sharing Banking, and "
      "Ostrom-Style Commons Governance added (rows 21-23), bringing the canonical CSV from 20 "
      "to 23 systems and closing Step 1b. Report and Paper regeneration for all eight systems "
      "scored since Session 14 remains queued as 'Step 5 (expanded)'.")
"""

builder = apply(read(BUILDER_IN), [
    (BUILDER_DOC_OLD, BUILDER_DOC_NEW),
    ("# All 20 systems, now uniformly on the 26-criterion structure.",
     "# All 23 systems, now uniformly on the 26-criterion structure."),
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
    print(f"  {s['key']:<42} D1-D5 {d}  total {s['total']:.1f}/26  "
          f"{s['n_fail']} failures  {s['tier']}   <- {s['source']} + {s['doc']}")
