#!/usr/bin/env python3
"""
rewrite_session26.py -- NEEC Session 26: decision D12, as the user resolved it
==============================================================================
The three scoring documents written in Sessions 21-23 (State Capitalism /
Qatar, Islamic finance, Ostrom-style commons governance) stated their
comparative claims on the corpus as it stood when each was scored. Handoff 25
proposed appending dated post-insertion notes. The user decided otherwise
(Session 26): reword the claims in place so each document states the current
canonical corpus, with no appended notes.

This script performs that rewrite. It reads the three documents as they stood
at the end of Session 25, pinned by MD5 as *_s25_snapshot.md, applies a fixed
register of anchored edits, regenerates the two corpus tables from the
canonical 23-system corpus, and writes the three live documents under their
canonical names. Nothing else in the documents changes.

Rules, as in insert_session20.py and insert_session25.py:
  * inputs are pinned by MD5; any mismatch stops the run before anything is
    written;
  * every edit's old text must occur exactly once in its snapshot;
  * all three documents are built in memory first, and written only if every
    edit in every document applied;
  * output is deterministic.

Edit kinds (reported per document):
  superseded  one of the nine registered claims (session25_audit_output.txt)
  correction  Handoff 25 Corrections 5-8
  stale       a further statement no longer true of the 23-system corpus or
              of the project's status, found in Session 26
  error       a wording error that was already wrong when written, found in
              Session 26
  table       a corpus table regenerated from the canonical corpus

Every rewritten claim is asserted by verify_comparative_claims.py.

Usage:  python3 rewrite_session26.py [INDIR] [OUTDIR]     (defaults: . and out)
"""
import hashlib
import importlib.util
import io
import contextlib
import os
import sys

INDIR = sys.argv[1] if len(sys.argv) > 1 else "."
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else "out"

QA_DOC = "NEEC_StateCapitalism_Qatar_scoring_scratch.md"
IF_DOC = "NEEC_IslamicFinance_scoring_scratch.md"
OS_DOC = "NEEC_Ostrom_Commons_scoring_scratch.md"
CANON = "neec_weighting_robustness_analysis_v2.py"


def snap(doc):
    return doc[:-3] + "_s25_snapshot.md"


PINNED_MD5 = {
    snap(QA_DOC): "25715519a0f8a6b198d7a38cc101df09",
    snap(IF_DOC): "a39ac0fe668319d82a0fe9335293a5bf",
    snap(OS_DOC): "b39181d7a35443c65e8fbc3f4e924d01",
    CANON: "d5041b130725577eea06bab807e0d2f8",   # the Session 25 canonical script (23 systems)
}

IF_KEY = "Islamic Finance / Profit-Sharing Banking"
OS_KEY = "Ostrom-Style Commons Governance"


def read(name):
    with open(os.path.join(INDIR, name), encoding="utf-8") as f:
        return f.read()


for name, digest in PINNED_MD5.items():
    path = os.path.join(INDIR, name)
    if not os.path.isfile(path):
        sys.exit(f"ERROR: missing input {name}")
    got = hashlib.md5(open(path, "rb").read()).hexdigest()
    if got != digest:
        sys.exit(f"ERROR: {name} has MD5 {got}, expected {digest} (pinned input)")

# ------------------------------------------------------------------ corpus
_spec = importlib.util.spec_from_file_location("_neec_canon", os.path.join(INDIR, CANON))
_canon = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(_canon)
SCORES = _canon.SCORES
CRITS = list(_canon.ALL_CRITS)
if len(SCORES) != 23:
    sys.exit(f"ERROR: canonical corpus holds {len(SCORES)} systems, expected 23")


def total(v):
    return sum(v[c] for c in CRITS)


def nfail(v):
    return sum(1 for c in CRITS if v[c] == 0.0)


def tier(n):
    if n <= 2:
        return "Potentially Adequate"
    if n <= 5:
        return "Partially Adequate"
    return "Structurally Inadequate"


def rows_sorted():
    rows = [(s, total(v), nfail(v)) for s, v in SCORES.items()]
    rows.sort(key=lambda r: (-r[1], r[0]))
    return rows


def render_if_table():
    """Islamic finance's layout: repeated competition-rank numbers; this entry in bold."""
    lines = ["| Rank | System | Score /26 | % | Failures | Tier |", "|---|---|---|---|---|---|"]
    prev, rank = None, 0
    for i, (s, t, f) in enumerate(rows_sorted(), start=1):
        if t != prev:
            rank, prev = i, t
        label = f"**{s}**" if s == IF_KEY else s
        lines.append(f"| {rank} | {label} | {t:.1f} | {100.0 * t / 26.0:.1f} | {f} | {tier(f)} |")
    return "\n".join(lines)


def render_os_table():
    """Ostrom's layout: '=' marks a shared competition rank; this entry in bold."""
    rows = rows_sorted()
    lines = ["| Rank | System | Score /26 | % | Failures | Tier |", "|---|---|---|---|---|---|"]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][1] == rows[i][1]:
            j += 1
        rank = f"{i + 1}=" if j > i else str(i + 1)
        for k in range(i, j + 1):
            s, t, f = rows[k]
            label = f"**{s}**" if s == OS_KEY else s
            lines.append(f"| {rank} | {label} | {t:.1f} | {100.0 * t / 26.0:.1f} | {f} | {tier(f)} |")
        i = j + 1
    return "\n".join(lines)


def between(text, begin, end):
    """The exact text strictly between two markers, each of which must occur once."""
    for m in (begin, end):
        if text.count(m) != 1:
            sys.exit(f"ERROR: marker {m!r} occurs {text.count(m)} times")
    a = text.index(begin) + len(begin)
    return text[a:text.index(end)]


# ------------------------------------------------------------------ the register
# (doc, id, kind, old, new). Each old string must occur exactly once in the snapshot.
E = []


def edit(doc, eid, kind, old, new):
    E.append((doc, eid, kind, old, new))


# ---- State Capitalism / Qatar
edit(QA_DOC, "Q1-status", "stale",
     """Paper Section 8.1 (v1.2 decision). Not yet added to `neec_scores.csv` and
not yet independently cross-checked by a second scorer (H.9 Step 6); both
are open, per this project's disclosure norms (`NEEC_CONTRIBUTING.md` §2,
Appendix H.6). Every arithmetic, transcription, sensitivity, and
comparative claim below is checked by `verify_qatar.py`, whose output is
captured in `verify_qatar_output.txt`. The two tables marked as generated
are written by that script (`python3 verify_qatar.py --fill`), not typed.""",
     """Paper Section 8.1 (v1.2 decision). Added to `neec_scores.csv` and the
canonical scoring scripts in Session 25; not yet independently
cross-checked by a second scorer (H.9 Step 6), which remains open per this
project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6).
Every arithmetic, transcription, and sensitivity claim below is checked by
`verify_qatar.py`, whose output is captured in `verify_qatar_output.txt`;
the two tables marked as generated are written by that script
(`python3 verify_qatar.py --fill`), not typed. Comparative claims are
stated on the canonical 23-system corpus and checked by
`verify_comparative_claims.py`.""")

edit(QA_DOC, "Q2-tie14", "superseded",
     """failures. The upward extreme reaches the same 14.0/26 as Sovereign Wealth
Fund Statism and Singapore, in a different tier: the corpus's standing
reminder that tiers come from failure counts, not totals.""",
     """failures. The upward extreme reaches the same 14.0/26 as Sovereign Wealth
Fund Statism, Singapore, and Ostrom-style commons governance, in a
different tier: the corpus's standing reminder that tiers come from failure
counts, not totals.""")

edit(QA_DOC, "Q3-csv", "stale",
     """**On the canonical CSV.** Consistent with the scratch-before-insert
discipline, this evaluation is **not** added to `neec_scores.csv` in this
pass. For the insertion pass to confirm or change, it proposes the display
name `State Capitalism / Qatar (Gulf Rentier-Distributive Statism)`,
following the siblings' pattern, with the short key `State Capitalism /
Qatar` in the scripts. All three state-capitalism sub-entries are now
scored. Qatar is the first system queued for the second consolidated
insertion pass, with Islamic finance and Ostrom-style commons governance.""",
     """**On the canonical CSV.** This evaluation is in `neec_scores.csv` and the
canonical scoring scripts, added in Session 25 with Islamic finance and
Ostrom-style commons governance. Its display name is `State Capitalism /
Qatar (Gulf Rentier-Distributive Statism)`, following the siblings'
pattern, with the short key `State Capitalism / Qatar` in the scripts. All
three state-capitalism sub-entries are scored and in the canonical corpus.""")

edit(QA_DOC, "Q4-step1b", "stale",
     """  failures (10) of the eight Step 1b systems.""",
     """  failures (10) of the ten Step 1b systems.""")

edit(QA_DOC, "Q5-position", "superseded",
     """3. **Corpus position.** In a prospective 21-system corpus, Qatar would rank
   20th of 21, above only Libertarian Minarchism (8.0/26), with no exact
   tie. It is dominated by CCO-PTF-CIP-SZH and State Capitalism /
   Singapore, and dominates no system. Inserting it would raise the
   corpus's count of strict-dominance relations from 11 to 13 ordered
   pairs; the only two that would not involve CCO-PTF-CIP-SZH, Singapore
   over China and Singapore over Qatar, both run between state-capitalism
   siblings.""",
     """3. **Corpus position.** In the canonical 23-system corpus, Qatar ranks
   22nd of 23, above only Libertarian Minarchism (8.0/26), with no exact
   tie. It is dominated by CCO-PTF-CIP-SZH and State Capitalism /
   Singapore, and dominates no system. The corpus holds 14 ordered
   strict-dominance pairs, 2 of them with Qatar as the dominated system.
   Three do not involve CCO-PTF-CIP-SZH: Singapore over China and
   Singapore over Qatar, both between state-capitalism siblings, and
   Islamic finance over Stakeholder Capitalism.""")

edit(QA_DOC, "Q6-next", "stale",
     """  force survey.
- **The next Step 1b system** is Islamic finance / profit-sharing banking;
  its scope question is set out in Handoff 21.
""",
     """  force survey.
""")

# ---- Islamic Finance / Profit-Sharing Banking
edit(IF_DOC, "F1-status", "stale",
     """H.7v2), as the eight earlier Step 1b systems were. This is the ninth Step 1b
entry and the second-to-last item in the Step 1b queue; Ostrom-style commons
governance remains. Not yet added to `neec_scores.csv` and not yet
independently cross-checked by a second scorer (H.9 Step 6); both are open,
per this project's disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix
H.6).

Every arithmetic, transcription, sensitivity, and comparative claim below is
checked by `verify_islamicfinance.py`, whose output is captured in
`verify_islamicfinance_output.txt`. The two tables marked as generated are
written by that script (`python3 verify_islamicfinance.py --fill`), not typed.
Research notes""",
     """H.7v2), as the eight earlier Step 1b systems were. This is the ninth of the
ten Step 1b entries. Added to `neec_scores.csv` and the canonical scoring
scripts in Session 25; not yet independently cross-checked by a second scorer
(H.9 Step 6), which remains open per this project's disclosure norms
(`NEEC_CONTRIBUTING.md` §2, Appendix H.6).

Every arithmetic, transcription, and sensitivity claim below is checked by
`verify_islamicfinance.py`, whose output is captured in
`verify_islamicfinance_output.txt`, and the summary table is written by that
script (`python3 verify_islamicfinance.py --fill`), not typed. Comparative
claims are stated on the canonical 23-system corpus and checked by
`verify_comparative_claims.py`, which also writes the corpus table (`--fill`).
Research notes""")

edit(IF_DOC, "F2-c14-label", "error",
     """NEEC's most discriminating criterion, and the mechanism has nothing to offer
it. Changing how credit is priced and structured leaves distribution running""",
     """The mechanism has nothing to offer this criterion. Changing how credit is
priced and structured leaves distribution running""")

edit(IF_DOC, "F3-c42-label", "error",
     """NEEC's second most discriminating criterion, held to absolute-reduction
standards. The mechanism's ecological instruments are allocative labels, not""",
     """Held to absolute-reduction standards, as Appendix H.7 requires. The
mechanism's ecological instruments are allocative labels, not""")

edit(IF_DOC, "F4-flags", "stale",
     """This evaluation carries **16 flagged** contestable calls, the largest set of
any entry in the corpus. That is not indecision: it is the direct consequence
of scoring a mechanism whose design and practice diverge, which makes most
criteria two-sided by construction. Treating each flag as an independent
binary gives **65,536 combinations**, with totals running **8.0-16.0**. Every
one of the three adequacy tiers is reachable, so **the tier is not robust**,
and this entry is the least tier-robust in the corpus to date — less robust
than Singapore, whose joint readings also spanned three tiers but from a
smaller flag set. Only **two of the five structural failures are undisputed**
by any flagged call: C2.2 (no unconditional provision) and C4.2 (no
absolute-reduction mechanism).""",
     """This evaluation carries **16 flagged** contestable calls, the second-largest
set of any entry in the corpus, after Ostrom-style commons governance's
twenty. That is not indecision: it is the direct consequence of scoring a
mechanism whose design and practice diverge, which makes most criteria
two-sided by construction. Treating each flag as an independent binary gives
**65,536 combinations**, with totals running **8.0-16.0**. Every one of the
three adequacy tiers is reachable, so **the tier is not robust**. Measured by
the span of the enumeration, 8.0 points and 10 structural failures, this
entry is less tier-robust than State Capitalism / Singapore (6.0 points and 6
failures, from twelve flags) and more tier-robust than Ostrom-style commons
governance (10.0 points and 11 failures, from twenty flags, with no
structural failure undisputed). Here, only **two of the five structural
failures are undisputed** by any flagged call: C2.2 (no unconditional
provision) and C4.2 (no absolute-reduction mechanism).""")

edit(IF_DOC, "F5-after-table", "stale",
     """Ranks are competition ranks; "=" in earlier documents and repeated rank
numbers here both mark a shared total. This row is a scratch score awaiting
an insertion pass.""",
     """Ranks are competition ranks; "=" in other scoring documents and repeated
rank numbers here both mark a shared total. This entry's row is in bold.""")

edit(IF_DOC, "F6-tie-order", "error",
     """  13.5/26 (51.9%), with 2, 3, and 5 structural failures respectively —
  Potentially Adequate, Partially Adequate, Partially Adequate. This""",
     """  13.5/26 (51.9%), with 5, 2, and 3 structural failures respectively —
  Partially Adequate, Potentially Adequate, Partially Adequate. This""")

edit(IF_DOC, "F7-split", "correction",
     """- **The widest viability-versus-ethics split in the corpus.** Domain 5 at
  4.5/5 sits against Domain 4 at 1.5/5, the fifth-lowest ethics score of the
  twenty-one systems (tied with Libertarian Minarchism). The other system at
  the top of Domain 5, CCO-PTF-CIP-SZH, scores 4.5 in Domain 4 as well; the
  nearest analogue for this shape is Status Quo Market Capitalism, at 4.0
  against 0.5, which is the comparison the entry invites.""",
     """- **The second-widest viability-versus-ethics split in the corpus.** Domain
  5 at 4.5/5 sits against Domain 4 at 1.5/5, a 3.0-point gap; the Domain 4
  score is the sixth-lowest of the twenty-three systems (tied with
  Libertarian Minarchism). The other system at the top of Domain 5,
  CCO-PTF-CIP-SZH, scores 4.5 in Domain 4 as well. Only Status Quo Market
  Capitalism, at 4.0 against 0.5, has a wider gap (3.5), and it is the
  comparison the entry invites; the three state-capitalism entries follow
  at 2.5.""")

edit(IF_DOC, "F8-dominance", "superseded",
     """  one of the few entries CCO-PTF-CIP-SZH does not strictly dominate, and
  C5.5 is the sole reason: Islamic finance scores 1.0 on cultural
  adaptability where CCO-PTF-CIP-SZH scores 0.5, and it is the only criterion
  on which it scores higher. It **strictly dominates Stakeholder
  Capitalism** (higher on 6 criteria, lower on none). Insertion takes the
  corpus's strict-dominance relations from **11 to 12** ordered pairs.""",
     """  one of the 11 entries CCO-PTF-CIP-SZH does not strictly dominate, and
  C5.5 is the sole reason: Islamic finance scores 1.0 on cultural
  adaptability where CCO-PTF-CIP-SZH scores 0.5, and it is the only criterion
  on which it scores higher. It **strictly dominates Stakeholder
  Capitalism** (higher on 6 criteria, lower on none), the corpus's only case
  of a Step 1b entry dominating one of the 13 legacy systems. The corpus
  holds **14** ordered strict-dominance pairs in all.""")

edit(IF_DOC, "F9-final-d4", "superseded",
     """own top-ranked entry; its ethical integrity is fifth-lowest of the
twenty-one. The gap between those two numbers is the whole finding.""",
     """own top-ranked entry; its ethical integrity is sixth-lowest of the
twenty-three. The gap between those two numbers is the whole finding.""")

edit(IF_DOC, "F10-final-failures", "error",
     """designed to carry. It has no unconditional provision (C2.2), no
absolute-reduction ecological constraint (C4.2), and no answer to automation
(C1.4). Those are the failures that survive every contestable call, and they
are the same failures every narrow single-mechanism entry in this corpus
records. Scored as a financial-sector reform layered on a market economy, it""",
     """designed to carry. It has no unconditional provision (C2.2) and no
absolute-reduction ecological constraint (C4.2), the two failures that
survive every contestable call, and on every joint reading but Reading A it
has no answer to automation (C1.4). No other narrow single-mechanism entry in
this corpus fails all three. Scored as a financial-sector reform layered on a
market economy, it""")

edit(IF_DOC, "F11-tie-partners", "error",
     """- **Against its archetype siblings.** It differs from Georgism on 10 criteria
  and from Universal Basic Services on 8, and neither dominates in either
  direction despite the identical totals.""",
     """- **Against its tie partners.** It differs from Georgism on 10 criteria
  and from Universal Basic Services on 8, and neither dominates in either
  direction despite the identical totals.""")

# ---- Ostrom-Style Commons Governance
edit(OS_DOC, "O1-status", "stale",
     """H.7v2), as the nine earlier Step 1b systems were. **This is the tenth Step 1b
entry and the last item in the Step 1b queue; with it, Step 1b closes.** Not
yet added to `neec_scores.csv` and not yet independently cross-checked by a
second scorer (H.9 Step 6); both are open, per this project's disclosure norms
(`NEEC_CONTRIBUTING.md` §2, Appendix H.6).

Every arithmetic, transcription, sensitivity, and comparative claim below is
checked by `verify_ostrom.py`, whose output is captured in
`verify_ostrom_output.txt`. The two tables marked as generated are written by
that script (`python3 verify_ostrom.py --fill`), not typed. The comparative
prose was written **from** that script's `--facts` mode rather than checked
against it afterwards; the facts pass caught five would-be errors before they
reached the page, listed in Handoff 23. Research notes are in""",
     """H.7v2), as the nine earlier Step 1b systems were. **This is the tenth and last
Step 1b entry; with it, Step 1b closed.** Added to `neec_scores.csv` and the
canonical scoring scripts in Session 25; not yet independently cross-checked
by a second scorer (H.9 Step 6), which remains open per this project's
disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6).

Every arithmetic, transcription, and sensitivity claim below is checked by
`verify_ostrom.py`, whose output is captured in `verify_ostrom_output.txt`,
and the summary table is written by that script (`python3 verify_ostrom.py
--fill`), not typed. Comparative claims are stated on the canonical 23-system
corpus and checked by `verify_comparative_claims.py`, which also writes the
corpus table (`--fill`). Research notes are in""")

edit(OS_DOC, "O2-c32", "stale",
     """is the one criterion on which it scores below every other system in the
20-system corpus, all of which reach at least 0.5, and the reason is simple
absence rather than malfunction.""",
     """is the one criterion on which it scores below every other system in the
corpus, all 22 of which reach at least 0.5, and the reason is simple absence
rather than malfunction.""")

edit(OS_DOC, "O3-c55", "correction",
     """**The strongest C5.5 case in the corpus, and the criterion on which this entry
beats every other system including CCO-PTF-CIP-SZH.** Validated""",
     """**The strongest C5.5 case in the corpus, and the one criterion on which this
entry scores above CCO-PTF-CIP-SZH.** The 1.0 is joint-best, shared with
Participatory Economics, Mutual Credit / LETS and Islamic finance. Validated""")

edit(OS_DOC, "O4-rule-pointer", "stale",
     """evaluation adopts one and states it; the framework does not yet require one.
See "Recommendation" below.""",
     """evaluation adopts one and states it; decision D8 makes such a rule part of
the scoring protocol (see "Scope-normalisation rule" below).""")

edit(OS_DOC, "O5-after-table", "stale",
     """All comparative claims below are computed by `verify_ostrom.py`, not
transcribed.""",
     """All comparative claims below are stated on the canonical 23-system corpus
and checked by `verify_comparative_claims.py`, not transcribed.""")

edit(OS_DOC, "O6-tie-order", "error",
     """exactly 14.0/26 (53.8%), with 3, 4 and 4 structural failures respectively.
Unlike the three-way tie at 13.5 that Session 22 found, **all three sit in the
same adequacy tier**, so this tie does not illustrate the tier-versus-percentage
distinction; it illustrates something else, which is that three mechanisms with""",
     """exactly 14.0/26 (53.8%), with 4, 3 and 4 structural failures respectively.
Unlike the three-way tie at 13.5 (Georgism / Land Value Tax, Universal Basic
Services and Islamic finance), **all three sit in the same adequacy tier**, so
this tie does not illustrate the tier-versus-percentage distinction; it
illustrates something else, which is that three mechanisms with""")

edit(OS_DOC, "O7-dominance", "correction",
     """**Not dominated by anything, CCO-PTF-CIP-SZH included.** The corpus contains
11 ordered strictly-dominating pairs, and inserting this entry **adds none**.
The single criterion on which it exceeds CCO-PTF-CIP-SZH is **C5.5, cultural
adaptability**, where it scores 1.0 against 0.5 — and that one criterion is
enough to block dominance. This is the same structure Islamic finance showed in
Session 22, and it is now a pattern worth naming in the Paper: mechanism-level
entries that are exceptionally well travelled can resist dominance by a much
higher-scoring system on the strength of a single portability criterion.

**It also dominates nothing**, which distinguishes it from Islamic finance —
the only Step 1b entry so far to strictly dominate an existing system.""",
     """**Not dominated by anything, CCO-PTF-CIP-SZH included.** The corpus contains
14 ordered strict-dominance pairs, and **none involves this entry**. The single
criterion on which it exceeds CCO-PTF-CIP-SZH is **C5.5, cultural
adaptability**, where it scores 1.0 against 0.5 — and that one criterion is
enough to block dominance. The structure is general rather than a property of
well-travelled mechanisms: CCO-PTF-CIP-SZH scores 1.0 on 23 criteria and 0.5
on C1.5, C4.5 and C5.5, so any system that scores 1.0 on one of those three
escapes its dominance. Eleven systems do, four of them through C5.5: this
entry, Islamic finance, Participatory Economics and Mutual Credit / LETS.

**It also dominates nothing**, which distinguishes it from the two Step 1b
entries that do: State Capitalism / Singapore, which dominates China and
Qatar, and Islamic finance, which dominates Stakeholder Capitalism — the only
Step 1b entry that dominates one of the 13 legacy systems.""")

edit(OS_DOC, "O8-domain5", "superseded",
     """**Best-in-corpus cultural adaptability; second-best implementation viability.**
Domain 5 scores **4.0/5**, beaten only by CCO-PTF-CIP-SZH and tied with Mutual
Credit / LETS, Nordic Social Democracy and Status Quo Market Capitalism. Domain
1 scores **2.0/6**, beaten by 13 of the 20 corpus systems. The resulting
**viability-minus-material-security split of 2.0** is the second widest in the
corpus, behind Libertarian Minarchism's 3.0.""",
     """**Joint-best cultural adaptability; joint third-best implementation
viability.** Domain 5 scores **4.0/5**, beaten only by CCO-PTF-CIP-SZH and
Islamic finance (4.5 each) and tied with Mutual Credit / LETS, Nordic Social
Democracy and Status Quo Market Capitalism. Domain 1 scores **2.0/6**, beaten
by 14 of the other 22 systems. The resulting **viability-minus-material-security
split of 2.0** is joint third-widest in the corpus, behind Libertarian
Minarchism's 3.0 and Islamic finance's 2.5, level with Doughnut Economics,
Mutual Credit / LETS, Status Quo Market Capitalism and Universal Basic
Services.""")

edit(OS_DOC, "O9-neighbour", "error",
     """**Against the nearest mechanism-level neighbour.** Compared with Georgism /
Land Value Tax it differs on only **5 criteria**, is higher on 3 and lower on
2, and gains 0.5 — the closest pairing in the corpus between two mechanisms
that both govern access to a natural resource, one by taxing its rent and one
by governing its use directly.""",
     """**Against a nearest neighbour.** Georgism / Land Value Tax is one of the three
systems closest to this entry, each differing from it on only **5 criteria**
(the others are Mutual Credit / LETS and Universal Basic Services). Against
Georgism it is higher on 3 and lower on 2, and gains 0.5 — a close pairing of
two mechanisms that both govern access to a natural resource, one by taxing its
rent and one by governing its use directly.""")

edit(OS_DOC, "O10-d8", "stale",
     """**Recommendation for the reproducibility kit (D3), carried as D8.** Adopt an
explicit **scope-normalisation rule**: every entry declares its scope
(mechanism, configured national economy, or comprehensive system) and the
protocol states how population-scope thresholds are applied in each case. This
entry adopts the generalisation convention and says so, but a convention chosen
by the scorer is exactly what a replication protocol is supposed to remove.
Ostrom-style commons governance is the entry that makes the omission
unmissable, and it should be the worked example in that section.""",
     """**Scope-normalisation rule (decision D8, adopted for the reproducibility kit,
D3).** Every entry declares its scope (mechanism, configured national economy,
or comprehensive system), and the protocol states how population-scope
thresholds are applied in each case. This entry adopts the generalisation
convention and says so, but a convention chosen by the scorer is exactly what a
replication protocol is supposed to remove. Ostrom-style commons governance is
the entry that makes the omission unmissable, and it is the rule's worked
example.""")

edit(OS_DOC, "O11-disclosure", "stale",
     """- **Not yet inserted** into `neec_scores.csv` or the canonical scoring scripts,
  per the scratch-before-insert discipline. It has **not been scored against
  State Capitalism / Qatar or Islamic Finance**, which are also pending; the
  21-system table above is the corpus of 20 plus this entry only. The
  consolidated insertion pass must build the combined 23-system table itself.""",
     """- **Inserted** into `neec_scores.csv` and the canonical scoring scripts in
  Session 25, with State Capitalism / Qatar and Islamic finance; the corpus
  table above is the canonical 23-system corpus.""")

edit(OS_DOC, "O12-robustness", "error",
     """**This entry therefore replaces Islamic finance as the least tier-robust in the
corpus**, and by a wide margin: a 10.0-point and 11-failure span against
Islamic finance's 5.0 and 9.""",
     """**This entry therefore replaces Islamic finance as the least tier-robust in the
corpus**, measured by the span of the enumeration: 10.0 points and 11
structural failures, against Islamic finance's 8.0 and 10, with no failure
undisputed where Islamic finance has two.""")

# The two corpus tables (regenerated, not typed).
TABLES = [
    (IF_DOC, "F12-table", "<!-- GENERATED:corpus -->\n", "\n<!-- END GENERATED:corpus -->", render_if_table),
    (OS_DOC, "O13-table", "<!-- BEGIN GENERATED: corpus-table -->\n", "\n<!-- END GENERATED: corpus-table -->",
     render_os_table),
]

# ------------------------------------------------------------------ apply
out, log = {}, []
for doc in (QA_DOC, IF_DOC, OS_DOC):
    text = read(snap(doc))
    for d, eid, kind, old, new in E:
        if d != doc:
            continue
        n = text.count(old)
        if n != 1:
            sys.exit(f"ERROR: edit {eid}: old text occurs {n} times in {snap(doc)} (must be exactly 1); nothing written")
        text = text.replace(old, new, 1)
        log.append((doc, eid, kind))
    for d, eid, begin, end, render in TABLES:
        if d != doc:
            continue
        body = between(text, begin, end)
        if len(body.splitlines()) != 23:   # 2 header lines + 21 rows in the snapshot
            sys.exit(f"ERROR: {eid}: expected the 21-row snapshot table, found {len(body.splitlines()) - 2} rows")
        text = text.replace(begin + body + end, begin + render() + end, 1)
        log.append((doc, eid, "table"))
    out[doc] = text

os.makedirs(OUTDIR, exist_ok=True)
print("rewrite_session26.py -- decision D12: comparative claims restated on the 23-system corpus")
print(f"inputs pinned: {len(PINNED_MD5)} files; canonical corpus: {len(SCORES)} systems")
for doc in (QA_DOC, IF_DOC, OS_DOC):
    kinds = {}
    for d, eid, kind in log:
        if d == doc:
            kinds[kind] = kinds.get(kind, 0) + 1
    ids = [eid for d, eid, _k in log if d == doc]
    summary = ", ".join(f"{k} {v}" for k, v in sorted(kinds.items()))
    print(f"\n{doc}: {len(ids)} edits ({summary})")
    print("  " + " ".join(ids))
for doc in (QA_DOC, IF_DOC, OS_DOC):
    data = out[doc].encode("utf-8")
    with open(os.path.join(OUTDIR, doc), "wb") as f:
        f.write(data)
    print(f"\nwrote {doc}  md5 {hashlib.md5(data).hexdigest()}")
totals = {}
for _d, _e, kind in log:
    totals[kind] = totals.get(kind, 0) + 1
print("\nTOTAL: " + str(len(log)) + " edits -- " + ", ".join(f"{k} {v}" for k, v in sorted(totals.items())))
