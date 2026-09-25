#!/usr/bin/env python3
"""
run_all_checks.py -- NEEC single entry point for reproducibility checks
=======================================================================
Version 24 (Session 49). Runs every verification and analysis script on file
and confirms that each still reproduces its captured output BYTE FOR BYTE.
Three scripts written before Session 20 had no captured output; theirs was
first captured in Session 20 (verify_ubs, verify_new_systems, step1c_retrofit).
Version 0 (Session 20) ran 18 checks; version 1 (Session 25) ran 27. Version 2
adds decision D12 (Session 26): the generator that restates the comparative
claims of the three Session 21-23 scoring documents on the canonical corpus,
the generator that narrows their entry verifiers, the three narrowed entry
verifiers, the comparative-claims verifier, and a negative control in which
that verifier must reject the documents as they stood before D12. The Session
21-25 scripts now run against the Session 25 snapshots of those documents and
verifiers (see below): 34 checks. Version 3 (Session 27) adds the first
scripts of the reproducibility kit (decision D3): build_criteria.py, which
generates criteria.json from Paper v1.4 and checks every anchor example against
the published scores; build_summary_blocks.py, which stages the 23 summary
blocks (D3(a)); neec_entry.py, the generic entry verifier, run three ways (the
corpus inventory of the D13 measure, one entry with its D9 peer matrix, and its
self-test); and a negative control in which neec_entry.py must reject the
staged blocks against the Session 20 corpus, which lacks three of their
systems: 40 checks. Version 4 (Session 28) adds decisions D16 to D19:
stage_blocks_s28.py, which applies D17 and D18(a) to the staged blocks and
asserts that nothing else changes; neec_entry.py on the Session 28 blocks (the
D13 inventory after D16 to D18); and audit_claims_s28.py, the claim register
of the eight scoring documents not audited before (222 claims, each phrase
located and each computable verdict and replacement fact asserted on the
canonical corpus): 43 checks. Version 5 (Session 29) adds the D14 landing:
d14_landing_s29.py, the one generator that restates the eleven scoring
documents from their Session 26 snapshots and embeds their summary blocks;
verify_comparative_claims.py, generalised to all eleven documents (the Session
28 claim register, the restated phrases and their facts, the D13 measure from
the blocks in the documents, the blocks themselves); a negative control in
which it must reject the Session 26 texts; and neec_entry.py run on the
documents themselves: 47 checks. Every earlier check that reads one of those
documents now reads its Session 26 snapshot, and the Session 26 claims
verifier runs from its own snapshot. Version 6 (Session 30) adds decision D22:
verify_doughnut.py, reconstructed from the Doughnut Economics Verification
section; restate_s30.py, which restates that section; the Session 30 claims
verifier and a negative control in which it must reject the section as the
D14 pass left it. It adds candidate mode and the corpus file (D23): the corpus
file's builder, neec_entry.py's candidate self-test, and a negative control in
which a canonical entry is rejected as a candidate. And it adds the first blind
replication kit (D24): its builder, which regenerates the kit's blind protocol,
corpus and brief byte for byte, and the maintainers' baseline, the original
Ostrom-style commons governance entry validated as a candidate against the
kit's corpus: 56 checks. The D14 generator and the Session 29 claims verifier
now run against the Doughnut Economics document as the D14 pass left it, and
the D14 generator against the Session 29 neec_entry.py, which it pins.
Version 7 (Session 32) adds the first pilot replication's return (decision D2,
protocol 11.4-11.5): the replication's block validated as a candidate against
the kit's corpus, as the replicator was asked to validate it;
compare_replication.py, the criterion-level comparison of a blind replication,
run three ways (its self-test in a kit's layout; the comparison of the pilot's
replication with the original entry, which also checks the replication
record's generated tables and attribution table; and a negative control in
which it must refuse to run beside the canonical script); and
d18b_reexpression_s32.py, which computes decision D18(b)'s re-expression of
the Ostrom-style commons governance register, and decision D26 taken with it,
without changing any file: 61 checks.
Version 8 (Session 33) applies decisions D18(b) and D26 (the first pilot's consequences; confirmed by the
project owner): insert_session33.py writes the canonical scripts with Ostrom-style commons governance's C3.2
at 0.5 from their Session 32 snapshots; the Session 33 canonical script, CSV builder and corpus file are run
on the new corpus; verify_insertion_s33.py asserts that one cell changed and what follows from it;
restate_s33.py restates seven scoring documents from their Session 32 snapshots; the Session 33 claims
verifier runs on them, with a negative control in which it must reject the Session 32 documents; and
neec_entry.py reads the Session 33 blocks and verify_doughnut.py runs on the Session 33 corpus. Every
version 7 check now runs against the Session 32 files (see below), marked [Session 32 state] where that
changes its inputs. Version 8 also makes the harness runnable on a claude.ai Project, which cannot hold an
empty file: an expected-empty stream is written as EMPTY rather than read from a file, the refusal check
compares the refusal message on stderr (an uncaught exception also exits 1 with empty stdout, so exit
status and stdout alone could not tell a refusal from a crash), and a missing reference file fails its
check instead of stopping the run: 71 checks.
Version 9 (Session 34) adds Appendix A.4 on the Session 33 corpus: run_a4_full_rerun_33.py, which is
run_a4_full_rerun_23.py with its corpus-specific assertions re-derived (Ostrom-Style Commons Governance now
ties Mutual Credit / LETS and Universal Basic Income at 14.5), and a negative control in which it must
reject the Session 32 corpus, failing exactly its seven re-derived checks with an empty standard error (a
failure, not a crash). The two checks follow the 71 of version 8, whose numbering is unchanged:
run_a4_full_rerun_23.py keeps running against the Session 32 corpus it was written for. Version 9 also
regenerates README.md, the repository's landing page, with build_readme.py, whose score table, tier counts
and check count are computed from neec_scores.csv and from this harness (and the protocol's version from
SCORING_PROTOCOL.md's header), and compares it byte for byte with the committed copy, so the landing page
cannot drift from the data: 74 checks.
Version 10 (Session 35) adds revision R4's audit: r4_audit_s35.py, which audits every corpus 1.0 resting on
a multi-clause Pass Threshold clause by clause (167 units, 542 clause codes, each coded phrase located in its
rationale), computes decision D28 and the two rules it was weighed against, compares the quoted thresholds in
criteria.json and in two scoring documents with the definitions, and checks that the decision record
(NEEC_R4_MultiClause_Audit_s35.md) contains its generated tables verbatim. It changes no file: 75 checks.
Version 11 (Session 36) adds scoring protocol v2.0-draft.5 and what came with it: build_criteria.py, which now
corrects criteria.json after transcribing it (every anchor threshold becomes its definition's Pass Threshold,
decision D28(g); C3.2's bands carry decision D26, revision R3); build_replication_kit.py's self-test of
revision R8 on the protocol in force, which builds no kit; and verify_protocol_s36.py, which asserts the
protocol's own statements about the corpus, its archetype table, its decision register and its Appendix B,
with a negative control in which it must reject draft.4. Protocol draft.4, criteria.json and build_criteria.py
as they stood in Session 35 are pinned as *_s35_snapshot.* files: every check written before Session 36 that
reads one of them (the Session 27 criteria build, the Session 28 staging, the first replication kit, and the
Session 35 audit, which compares the uncorrected anchors with the definitions) reads the snapshot, so the
first kit still rebuilds byte for byte with the revised builder: 79 checks. Version 12 (Session 37) adds
rescoring_s37.py, part (a) of the rescoring pass (decisions D28, D29, D31): the 33 stated-shortfall 1.0s
re-estimated clause by clause, their consequences computed without changing any corpus file, and the
record NEEC_Rescoring_s37.md checked against its generated tables: 80 checks. Version 13 (Session 38) adds
rescoring_s38.py, the first group of part (b): the 29 part (b) units on the five criteria whose readings part (a)
fixed (C3.4, C5.3, C2.4, C1.3, C2.3), their consequences computed cumulatively with part (a), the pinned
Compassionism Simulation runs of cco_simulation_checks_s38.js checked by engine digest (the simulation's source is
not in this directory, so the JavaScript itself is not rerun here), and the record NEEC_Rescoring_s38.md checked
against its generated tables: 81 checks. Version 14 (Session 39) adds
rescoring_s39.py, the second group of part (b): C5.1's second clause tested in full on its eleven 1.0s outside
D28's population and C3.1's five part (b) units, with every departure from the audit's codes listed and asserted,
their consequences computed cumulatively with parts (a) and (b1), the anchor examples the pass moves counted, and
the record NEEC_Rescoring_s39.md checked against its generated tables: 82 checks.
Version 15 (Session 40) adds
rescoring_s40.py, the third group of part (b): C1.1's nine part (b) units, whose stress clause the audit coded silent,
with CCO-PTF-CIP-SZH's base clause tested against the design's own published model, the pinned Compassionism
Simulation runs of cco_simulation_checks_s40.js checked by both engine digests (harness.js and index.html; the
JavaScript itself is not rerun here), their consequences computed cumulatively with parts (a), (b1) and (b2), and the
record NEEC_Rescoring_s40.md checked against its generated tables: 83 checks.
Version 16 (Session 41) adds
rescoring_s41.py, the fourth group of part (b): the eleven part (b) units of C1.4, C2.1 and C3.2, with no departure
from the audit's A codes and the two clauses left not estimated each asserted to sit in a unit another clause decides,
their consequences computed cumulatively with parts (a) to (b3), the criteria the pass so far leaves with no 1.0
found and asserted, and the record NEEC_Rescoring_s41.md checked against its generated tables: 84 checks.
Version 17 (Session 42) adds
rescoring_s42.py, the fifth group of part (b): C2.5's ten part (b) units, with the one departure from the audit's A
codes listed and asserted, the audit's five out-of-reach codes confirmed, the four clauses left not estimated each
asserted to sit in a unit another clause decides, their consequences computed cumulatively with parts (a) to (b4),
and the record NEEC_Rescoring_s42.md checked against its generated tables: 85 checks.
Version 18 (Session 43) adds
rescoring_s43.py, the sixth group of part (b): the ten part (b) units of C3.5 and C4.1, with no departure from
the audit's A codes, the audit's four out-of-reach codes confirmed, the four clauses left not estimated each
asserted to sit in a unit another clause decides, a flag outside the group that rests on a unit it moves
asserted, their consequences computed cumulatively with parts (a) to (b5), and the record
NEEC_Rescoring_s43.md checked against its generated tables: 86 checks.
Version 19 (Session 44) adds
criteria_review_s44.py, the evidence tables of the criteria review (NEEC_Criteria_Review_s44.md): the implicit
norm weights under equal criterion weighting, the quantities scored in more than one Pass Threshold located verbatim,
their corpus agreement, and the Requirement figures that differ from a Pass Threshold; no file changed: 87 checks.
Version 20 (Session 45) adds the v2.0 criteria (NEEC_Criteria_v2_s45.md: Package A of the review, and Package B,
adopted by the owner, 28 criteria): build_criteria.py version 2, which builds criteria.json (neec-criteria/2.0)
from the pinned Session 44 criteria and the record's Appendix V, asserts seven rules (one figure per quantity,
no Requirement figure outside its threshold, no dated threshold, no US-only measure, verbatim clauses, anchors
equal to thresholds, the 28-criterion structure) and regenerates the protocol as draft.6; its self-test, in which
each rule must reject a planted violation; and criteria_v2_s45.py, the record's evidence tables. criteria.json,
build_criteria.py, SCORING_PROTOCOL.md and criteria_schema.json as they stood at tag s44 are pinned as
*_s44_snapshot.* files: every check written in Sessions 36 to 44 that reads one of them reads the snapshot and is
marked [Session 44 state]; the first replication kit's check reads the schema snapshot, which is byte-identical to
the schema it was built with. build_readme.py now also reads criteria.json. 90 checks.
Version 21 (Session 46) carries decision 46.1, Package C, adopted by the owner in part: C2.6 gains two clauses
(consent to medical treatment; compulsion prescribed by law, time-limited and open to judicial review) and C4.6
Harm Internalization is added, 29 criteria. The record is amended in place and tag s45 keeps its prior state, so
the three Session 45 checks now run build_criteria.py version 2.1, which regenerates the protocol as draft.7, and
criteria_v2_s45.py on the amended record; the two build captures are recaptured as build_criteria_s46_output.txt
and build_criteria_s46_selftest_output.txt (the Session 45 captures are at tag s45), and
criteria_v2_s45_output.txt is recaptured under its own name. No check is added or removed: 90 checks.
Version 22 (Session 47) carries decision 47.1, C4.6's clause 3 bar (World Justice Project sub-factor 6.2, 0.77,
the upper quartile of its 2025 edition), amended in place in the record, tag s46 keeping its prior state: the
build check runs build_criteria.py version 2.2, which regenerates the protocol as draft.8, and its capture is
renamed build_criteria_s47_output.txt (the self-test's capture is unchanged); criteria_v2_s45.py gains section 5,
which reads wjp_rol_sf62_2012_2025.csv (sub-factor 6.2 for every edition, extracted from the Project's 2025 data
file) and asserts the bar and every figure the record states. It adds rescoring_s47.py, part (b)'s seventh group
and the first on the v2.0 clauses: the ten part (b) units of C4.2 and C4.4, with part (a)'s three units of those
criteria re-read, each v2.0 clause mapped to the Session 44 clause the audit coded, the audit's A codes carried on
verbatim clauses and listed on restated ones, their consequences computed cumulatively with parts (a) to (b6), and
the record NEEC_Rescoring_s47.md checked against its generated tables. It reads the v2.0 criteria.json and the
pinned criteria_s44_snapshot.json side by side, so it is not pinned: 91 checks.
Version 23 (Session 48) carries decisions 48.1 to 48.3, amended in place in the record, tag s47 keeping its prior
state: 48.3 defines C4.4 clause 1's measure and moves C4.4 from class D to class M. The build check runs
build_criteria.py version 2.3, which regenerates the protocol as draft.9, and its capture is renamed
build_criteria_s48_output.txt; criteria_v2_s45.py counts the classes anew and asserts China's and Qatar's WJP series
(48.1). rescoring_s47.py asserts C4.4's Session 47 class, so check 91 now reads criteria.json as it stood at tag
s47, pinned byte-identical as criteria_s47_snapshot.json and copied in under the canonical name. It adds
rescoring_s48.py: C4.4's six units in the pass re-read on 48.3's measure (part (b7)'s records superseded),
Nordic Social Democracy's clause 1 bound computed from its published inputs, the consequences with parts (a) to
(b7), and the score ledger (every entry's published total, each part's change, its total now; the published totals
checked against neec_scores.csv), with NEEC_Rescoring_s48.md checked against its generated tables: 92 checks.
Version 24 (Session 49) adds the public site (decisions 49.1 to 49.10, from the site package prepared in a chat
session, NEEC_Site_Package_s49.md): build_site.py --check, which rebuilds docs/ in its own temporary directory from
criteria.json, the corpus, the record, Paper v1.4, the A.4 weighting script, the WJP extract, the issue forms and
site/, compares the result with docs/ file by file, and prints one line, which the harness also shows. Its inputs
keep their subdirectories, so a check's files may now name paths in subdirectories. A negative control, in which
the copied docs/index.html is replaced by docs/404.html, must fail with exit 1: 94 checks. Decisions 49.1 to 49.12
are recorded in NEEC_Criteria_v2_s45.md, whose md5 criteria.json carries, so the build check's capture is renamed
build_criteria_s49_output.txt and recaptured; nothing else in criteria.json or the protocol changes.

HOW EACH CHECK RUNS. A check copies exactly the files its script needs into
a fresh temporary directory (under the names the script expects), runs the
script there, and compares its standard output (and, where a check names
one, its standard error), and any file it writes, with the captured copy on
file. EMPTY stands for an expected-empty stream, so no empty file is needed. Nothing in this directory is modified.

HISTORICAL SCRIPTS STAY UNEDITED. A verification script written before an
insertion pass makes claims about the corpus as it stood then (for example,
"the canonical corpus holds exactly 17 systems"). Rather than rewrite those
records, each one runs against the corpus it was written for:
  * the Session 16 corpus (17 systems): the pinned, byte-identical snapshot
    neec_weighting_robustness_analysis_v2_s16_snapshot.py, copied in under
    the canonical file name;
  * the Session 15 corpus (15 systems): a read-only view generated here from
    that snapshot, minus the two systems Session 16 inserted. The view narrows
    only SCORES and PUBLISHED and re-exports everything else unchanged. Helpers
    that read corpus data on their own (verify_transcription, dominates,
    run_full_report) therefore still see the snapshot's 17 systems; the 15
    shared vectors are identical there, so every lookup by name agrees.
  * the Session 20 corpus (20 systems): the pinned, byte-identical snapshots
    neec_weighting_robustness_analysis_v2_s20_snapshot.py,
    neec_scores_csv_builder_v2_s20_snapshot.py and neec_scores_s20_snapshot.csv
    (pinned in Session 25), copied in under the canonical file names. The
    Session 20 scripts and the Session 21-23 verifiers run against these.
  * the Session 25 documents and verifiers (pinned in Session 26, before
    decision D12 restated the three Session 21-23 scoring documents and
    narrowed their entry verifiers): *_s25_snapshot.md, verify_*_s25_snapshot.py
    and verify_*_output_s25_snapshot.txt, byte-identical copies, copied in
    under the canonical file names. The Session 21-25 scripts run against these.
  * the Session 26 documents and claims verifier (pinned in Session 29, before
    the D14 pass restated the eleven scoring documents): *_s26_snapshot.md and
    verify_comparative_claims_s26_snapshot.py, byte-identical copies, copied in
    under the canonical file names. The Session 16-28 scripts that read those
    documents run against these.
  * the Session 29 Doughnut Economics document, claims verifier and entry
    verifier (pinned in Session 30, before decision D22 and candidate mode):
    NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md,
    verify_comparative_claims_s29_snapshot.py and neec_entry_s29_snapshot.py,
    byte-identical copies, copied in under the canonical file names. The
    Session 29 scripts run against these where they depend on them.
  * the Session 32 corpus, documents and claims verifier (pinned in Session 33,
    before decisions D18(b) and D26): neec_weighting_robustness_analysis_v2,
    neec_scores_csv_builder_v2 and verify_comparative_claims (*_s32_snapshot.py),
    neec_scores_s32_snapshot.csv, neec_corpus_s32_snapshot.json, and the seven
    scoring documents restate_s33.py restates (*_s32_snapshot.md), byte-identical
    copies, copied in under the canonical file names. Every version 7 check runs
    against these.
  * the Session 35 protocol and criteria (pinned in Session 36, before protocol draft.5 and the
    correction of criteria.json): SCORING_PROTOCOL_s35_snapshot.md, criteria_s35_snapshot.json and
    build_criteria_s35_snapshot.py, byte-identical copies, copied in under the canonical file names. Every
    check written before Session 36 that reads one of them runs against these.
New insertion passes should pin their own snapshot the same way. Once the
project lives in a Git repository, a tag can replace the snapshot files.

Usage:   python3 run_all_checks.py
Exit status is 0 only if every check that runs passes. A check is skipped
(not failed) only when an external tool it needs, such as Node.js, is
absent.
"""
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CANON = "neec_weighting_robustness_analysis_v2.py"
S16 = "neec_weighting_robustness_analysis_v2_s16_snapshot.py"
BASELINE = "baseline_weighting_script.py"
BUILDER = "neec_scores_csv_builder_v2.py"
S20 = "neec_weighting_robustness_analysis_v2_s20_snapshot.py"
S20_BUILDER = "neec_scores_csv_builder_v2_s20_snapshot.py"
S20_CSV = "neec_scores_s20_snapshot.csv"
PENDING = {  # Session 21-23 verifiers and the scratch documents they check
    "verify_qatar.py": "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
    "verify_islamicfinance.py": "NEEC_IslamicFinance_scoring_scratch.md",
    "verify_ostrom.py": "NEEC_Ostrom_Commons_scoring_scratch.md",
}
PENDING_FILES = {k: k for pair in PENDING.items() for k in pair}
QA_DOC, IF_DOC, OS_DOC = (PENDING[v] for v in ("verify_qatar.py", "verify_islamicfinance.py", "verify_ostrom.py"))
# Session 25 snapshots (pinned in Session 26): canonical name -> snapshot file.
S25 = {n: n[:-3] + "_s25_snapshot" + n[-3:] for n in PENDING_FILES}
S25_OUT = {o: o[:-4] + "_s25_snapshot.txt"
           for o in ("verify_qatar_output.txt", "verify_islamicfinance_output.txt", "verify_ostrom_output.txt")}
# Inputs of the Session 27 kit: the summary-block generator reads these documents and verifiers.
KIT_BLOCK_INPUTS = ("build_summary_blocks.py", "neec_entry.py", CANON, "neec_scores.csv",
                    "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                    "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
                    "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                    "NEEC_StateCapitalism_China_scoring_scratch.md", "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                    QA_DOC, IF_DOC, OS_DOC, "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md", "NEEC_Paper_v1_4.md",
                    "verify_china.py", "verify_singapore.py", "verify_qatar.py", "verify_islamicfinance.py",
                    "verify_ostrom.py")
KIT_ENTRY_INPUTS = ("neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s27.json")
# Session 28: decisions D16-D19 (staging) and the claim register of the eight unaudited documents.
S28_STAGE_INPUTS = ("stage_blocks_s28.py", "neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s27.json",
                    "SCORING_PROTOCOL.md")
S28_DOCS = ("NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
            "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
            "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "NEEC_StateCapitalism_China_scoring_scratch.md",
            "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md")
S28_AUDIT_INPUTS = ("audit_claims_s28.py", "neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s28.json") + S28_DOCS
# Inputs of verify_comparative_claims.py (Session 26).
CLAIMS_INPUTS = (CANON, "verify_comparative_claims.py", QA_DOC, IF_DOC, OS_DOC,
                 "verify_qatar.py", "verify_islamicfinance.py", "verify_ostrom.py",
                 "verify_singapore.py", "verify_china.py",
                 "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                 "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
                 "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                 "NEEC_StateCapitalism_China_scoring_scratch.md", "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                 "NEEC_Report_v1_6.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md")
# Session 29: the D14 landing. The eleven scoring documents and their Session 26 snapshots.
ELEVEN = S28_DOCS + (QA_DOC, IF_DOC, OS_DOC)
S26 = {d: d[:-3] + "_s26_snapshot.md" for d in ELEVEN}
S26_CLAIMS = "verify_comparative_claims_s26_snapshot.py"
D14_INPUTS = ("d14_landing_s29.py", "summary_blocks_s28.json", "neec_entry.py", CANON, "neec_scores.csv")
CLAIMS29_INPUTS = (CANON, "neec_scores.csv", "neec_entry.py", "audit_claims_s28.py", "summary_blocks_s28.json",
                   "d14_landing_s29.py", "verify_comparative_claims.py", "verify_qatar.py", "verify_islamicfinance.py",
                   "verify_ostrom.py", "verify_singapore.py", "verify_china.py") + ELEVEN
# Session 30: D22, candidate mode and the corpus file (D23), the first blind replication kit (D24).
DE_DOC = "NEEC_DoughnutEconomics_scoring_scratch.md"
DE_S29 = "NEEC_DoughnutEconomics_scoring_scratch_s29_snapshot.md"
ENTRY_S29 = "neec_entry_s29_snapshot.py"
S29_CLAIMS = "verify_comparative_claims_s29_snapshot.py"
CLAIMS30_INPUTS = CLAIMS29_INPUTS + ("restate_s30.py", "verify_doughnut.py")
ENTRY30 = ("neec_entry.py", CANON, "neec_scores.csv", "neec_corpus.json")
KIT_INPUTS = ("build_replication_kit.py", "SCORING_PROTOCOL.md", "criteria.json", "criteria_schema.json",
              "summary_block_schema.json", "neec_entry.py", "neec_corpus.json", "build_corpus_file.py")
KIT = "out/neec_replication_kit_OS/"
# Session 32: the first pilot replication's return.
REPL_DOC = "NEEC_OstromCommons_replication_scoring.md"
REPL_RECORD = "NEEC_OstromCommons_replication_record.md"
KIT_LAYOUT = {"compare_replication.py": "compare_replication.py", "neec_entry.py": "neec_entry.py",
              "neec_corpus.json": "replication_kit_OS_neec_corpus.json"}
VIEW15 = "@view15"   # generated file (see VIEW15_SOURCE)
EMPTY = "@empty"     # an expected-empty stream: a claude.ai Project cannot hold an empty file
# Session 33: decisions D18(b) and D26. The files they change, and their Session 32 snapshots.
S33_DOCS = (OS_DOC, QA_DOC, IF_DOC, "NEEC_MutualCredit_LETS_scoring_scratch.md",
            "NEEC_UniversalBasicServices_scoring_scratch.md", "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
            "NEEC_StateCapitalism_Singapore_scoring_scratch.md")
S32 = {n: n[:-3] + "_s32_snapshot.py" for n in (CANON, BUILDER, "verify_comparative_claims.py")}
S32.update({d: d[:-3] + "_s32_snapshot.md" for d in S33_DOCS})
S32.update({"neec_scores.csv": "neec_scores_s32_snapshot.csv", "neec_corpus.json": "neec_corpus_s32_snapshot.json"})
# Session 36: protocol draft.5 and the corrected criteria.json. The files they replace, pinned as they stood in
# Session 35. The protocol (draft.4, Session 30) and criteria.json (Session 27) did not change between Session 32
# and Session 35, so these snapshots are also the Session 32 state that pin32() gives the version 7 checks.
S35 = {"SCORING_PROTOCOL.md": "SCORING_PROTOCOL_s35_snapshot.md", "criteria.json": "criteria_s35_snapshot.json",
       "build_criteria.py": "build_criteria_s35_snapshot.py"}
# Session 45: the v2.0 criteria. The files they replace, pinned as they stood at tag s44. criteria_schema.json did
# not change between Session 27 and Session 44, so its snapshot is also the state every earlier check read.
S44 = {n: n.rsplit(".", 1)[0] + "_s44_snapshot." + n.rsplit(".", 1)[1]
       for n in ("criteria.json", "build_criteria.py", "SCORING_PROTOCOL.md", "criteria_schema.json")}

VIEW15_SOURCE = '''"""Derived view generated by run_all_checks.py: the pinned Session 16 snapshot
minus the two systems Session 16 inserted, i.e. the 15-system corpus data that
the Session 10-15 scripts were written against. Read-only; not a canonical file."""
import importlib.util as _u
_spec = _u.spec_from_file_location("_neec_s16", "neec_weighting_robustness_analysis_v2_s16_snapshot.py")
_m = _u.module_from_spec(_spec)
_spec.loader.exec_module(_m)
_DROP = ("Doughnut Economics", "Universal Basic Services")
# Re-export the snapshot's public names unchanged, then narrow the two corpus tables.
globals().update({_k: _v for _k, _v in vars(_m).items()
                  if not _k.startswith("_") and _k not in ("SCORES", "PUBLISHED")})
SCORES = {k: v for k, v in _m.SCORES.items() if k not in _DROP}
PUBLISHED = {k: v for k, v in _m.PUBLISHED.items() if k not in _DROP}
'''

# The Session 20 insertion verifier's inputs, with the Session 20 corpus under the canonical names.
S20_INPUTS = {CANON: S20, S16: S16, BASELINE: BASELINE,
               "neec_scores_csv_builder_v2.py": S20_BUILDER,
               "neec_scores_csv_builder_v2_s16_snapshot.py": "neec_scores_csv_builder_v2_s16_snapshot.py",
               "neec_scores.csv": S20_CSV,
               "neec_scores_s16_snapshot.csv": "neec_scores_s16_snapshot.csv",
               "insert_session20.py": "insert_session20.py",
               "verify_swf.py": "verify_swf.py", "verify_china.py": "verify_china.py",
               "verify_singapore.py": "verify_singapore.py"}

# Each check: name, command, files {name in temp dir: source file here or VIEW15},
# stdout (captured file to match, or None), outputs {file written: reference file here},
# and optionally expect_exit (default 0; a negative control expects 1).
V7_CHECKS = [
    # --- the Session 32 state (23 systems; version 7's current corpus) ---
    dict(name="Canonical script, current corpus (23 systems, full report)",
         cmd=["python", CANON], files={CANON: CANON, BASELINE: BASELINE},
         stdout="session25_v2script_output.txt"),
    dict(name="CSV builder regenerates neec_scores.csv (23 systems)",
         cmd=["python", BUILDER], files={CANON: CANON, BUILDER: BUILDER},
         stdout="session25_csv_builder_output.txt",
         outputs={"neec_scores.csv": "neec_scores.csv"}),
    dict(name="Session 25 generator reproduces both canonical scripts from the Session 20 files",
         cmd=["python", "insert_session25.py", ".", "out"],
         files=dict(S25, **{k: k for k in (S20, S20_BUILDER, "insert_session25.py")}),
         stdout="session25_generator_output.txt",
         outputs={"out/" + CANON: CANON, "out/" + BUILDER: BUILDER}),
    dict(name="verify_insertion_s25.py (Session 25 insertion, current corpus; includes negative tests)",
         cmd=["python", "verify_insertion_s25.py"],
         files=dict(S25, **{k: k for k in (CANON, BUILDER, "neec_scores.csv", BASELINE, S20, S20_BUILDER,
                                                     S20_CSV, "insert_session25.py", "verify_insertion_s25.py")}),
         stdout="session25_verify_insertion_output.txt"),
    dict(name="run_a4_full_rerun_23.py (Appendix A.4, current corpus)",
         cmd=["python", "run_a4_full_rerun_23.py"],
         files={CANON: CANON, BASELINE: BASELINE, "run_a4_full_rerun_23.py": "run_a4_full_rerun_23.py"},
         stdout="a4_rerun_23_raw_output.txt"),
    dict(name="audit_claim_survival_s25.py (the Session 21-23 claims on the combined corpus)",
         cmd=["python", "audit_claim_survival_s25.py"],
         files=dict(S25, **S25_OUT, **{k: k for k in (S20, "audit_claim_survival_s25.py")}),
         stdout="session25_audit_output.txt"),
    # --- decision D12 (Session 26): restated documents, narrowed entry verifiers, current corpus ---
    dict(name="Session 26 generator restates the three scoring documents from their Session 25 snapshots",
         cmd=["python", "rewrite_session26.py", ".", "out"],
         files=dict({S25[d]: S25[d] for d in (QA_DOC, IF_DOC, OS_DOC)},
                    **{CANON: CANON, "rewrite_session26.py": "rewrite_session26.py"}),
         stdout="session26_rewrite_output.txt",
         outputs={"out/" + d: S26[d] for d in (QA_DOC, IF_DOC, OS_DOC)}),
    dict(name="Session 26 generator narrows the three entry verifiers from their Session 25 snapshots",
         cmd=["python", "narrow_verifiers_s26.py", ".", "out"],
         files=dict({S25[v]: S25[v] for v in PENDING}, **{"narrow_verifiers_s26.py": "narrow_verifiers_s26.py"}),
         stdout="session26_narrow_output.txt",
         outputs={"out/" + v: v for v in PENDING}),
    dict(name="verify_qatar.py (entry checks; current corpus, Session 26 document)",
         cmd=["python", "verify_qatar.py"],
         files={CANON: CANON, "verify_qatar.py": "verify_qatar.py", QA_DOC: S26[QA_DOC]},
         stdout="verify_qatar_output.txt"),
    dict(name="verify_islamicfinance.py (entry checks; current corpus, Session 26 document)",
         cmd=["python", "verify_islamicfinance.py"],
         files={CANON: CANON, "verify_islamicfinance.py": "verify_islamicfinance.py", IF_DOC: S26[IF_DOC]},
         stdout="verify_islamicfinance_output.txt"),
    dict(name="verify_ostrom.py (entry checks; current corpus, Session 26 document)",
         cmd=["python", "verify_ostrom.py"],
         files={CANON: CANON, "verify_ostrom.py": "verify_ostrom.py", OS_DOC: S26[OS_DOC]},
         stdout="verify_ostrom_output.txt"),
    dict(name="verify_comparative_claims.py as of Session 26 (snapshot; current corpus, Session 26 documents)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: S26.get(k, k) for k in CLAIMS_INPUTS}, **{"verify_comparative_claims.py": S26_CLAIMS}),
         stdout="session26_verify_claims_output.txt"),
    dict(name="verify_comparative_claims.py as of Session 26 rejects the Session 25 documents (negative control; exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: S26.get(k, k) for k in CLAIMS_INPUTS}, **{"verify_comparative_claims.py": S26_CLAIMS},
                    **{d: S25[d] for d in (QA_DOC, IF_DOC, OS_DOC)}),
         stdout="session26_verify_claims_negative_output.txt", expect_exit=1),
    # --- Session 27: the reproducibility kit (current corpus) ---
    dict(name="build_criteria.py generates criteria.json from Paper v1.4 and checks every anchor example",
         cmd=["python", "build_criteria.py"],
         files={k: k for k in ("build_criteria.py", "NEEC_Paper_v1_4.md", CANON)},
         stdout="build_criteria_output.txt", outputs={"criteria.json": "criteria.json"}),
    dict(name="build_summary_blocks.py stages the 23 summary blocks (D3(a))",
         cmd=["python", "build_summary_blocks.py"],
         files={k: S26.get(k, k) for k in KIT_BLOCK_INPUTS},
         stdout="build_summary_blocks_output.txt", outputs={"summary_blocks_s27.json": "summary_blocks_s27.json"}),
    dict(name="neec_entry.py validates the 23 staged blocks and prints the D13 inventory",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s27.json", "--corpus"],
         files={k: k for k in KIT_ENTRY_INPUTS}, stdout="neec_entry_corpus_output.txt"),
    dict(name="neec_entry.py, one entry with its D9 peer matrix (Ostrom-style commons governance)",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s27.json", "--entry", "OS"],
         files={k: k for k in KIT_ENTRY_INPUTS}, stdout="neec_entry_OS_output.txt"),
    dict(name="neec_entry.py self-test (Markdown round-trip; an altered vector is rejected)",
         cmd=["python", "neec_entry.py", "--selftest"],
         files={k: k for k in ("neec_entry.py", CANON, "neec_scores.csv")}, stdout="neec_entry_selftest_output.txt"),
    dict(name="neec_entry.py rejects the staged blocks against the Session 20 corpus (negative control; exit 1 expected)",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s27.json", "--corpus"],
         files={"neec_entry.py": "neec_entry.py", CANON: S20, "neec_scores.csv": S20_CSV,
                "summary_blocks_s27.json": "summary_blocks_s27.json"},
         stdout="neec_entry_negative_s20_output.txt", expect_exit=1),
    # --- Session 28: decisions D16-D19, and the claim register (current corpus) ---
    dict(name="stage_blocks_s28.py applies D17 and D18(a) to the staged blocks (nothing else changes)",
         cmd=["python", "stage_blocks_s28.py"], files={k: k for k in S28_STAGE_INPUTS},
         stdout="stage_blocks_s28_output.txt", outputs={"summary_blocks_s28.json": "summary_blocks_s28.json"}),
    dict(name="neec_entry.py validates the Session 28 blocks and prints the D13 inventory after D16-D18",
         cmd=["python", "neec_entry.py", "--blocks", "summary_blocks_s28.json", "--corpus"],
         files={k: k for k in ("neec_entry.py", CANON, "neec_scores.csv", "summary_blocks_s28.json")},
         stdout="neec_entry_corpus_s28_output.txt"),
    dict(name="audit_claims_s28.py (the claim register of the eight documents not audited before; 222 claims)",
         cmd=["python", "audit_claims_s28.py"], files={k: S26.get(k, k) for k in S28_AUDIT_INPUTS},
         stdout="audit_claims_s28_output.txt"),
    # --- Session 29: the D14 landing (current corpus) ---
    dict(name="d14_landing_s29.py restates the eleven scoring documents from their Session 26 snapshots (D14; "
              "Doughnut Economics as the D14 pass left it)",
         cmd=["python", "d14_landing_s29.py", ".", "out"],
         files=dict({S26[d]: S26[d] for d in ELEVEN}, **{k: (ENTRY_S29 if k == "neec_entry.py" else k)
                                                          for k in D14_INPUTS}),
         stdout="d14_landing_s29_output.txt",
         outputs={"out/" + d: (DE_S29 if d == DE_DOC else d) for d in ELEVEN}),
    dict(name="verify_comparative_claims.py as of Session 29 (snapshot; the documents as the D14 pass left them)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: k for k in CLAIMS29_INPUTS}, **{"verify_comparative_claims.py": S29_CLAIMS, DE_DOC: DE_S29}),
         stdout="verify_claims_s29_output.txt"),
    dict(name="verify_comparative_claims.py as of Session 29 rejects the Session 26 documents (negative control; "
              "exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: k for k in CLAIMS29_INPUTS}, **{"verify_comparative_claims.py": S29_CLAIMS},
                    **{d: S26[d] for d in ELEVEN}),
         stdout="verify_claims_s29_negative_output.txt", expect_exit=1),
    dict(name="neec_entry.py reads the 23 summary blocks from the eleven documents and prints the D13 inventory",
         cmd=["python", "neec_entry.py"] + list(ELEVEN) + ["--corpus"],
         files=dict({k: k for k in ("neec_entry.py", CANON, "neec_scores.csv")}, **{d: d for d in ELEVEN}),
         stdout="neec_entry_documents_s29_output.txt"),
    # --- Session 30: D22, candidate mode and the corpus file (D23), the first blind replication kit (D24) ---
    dict(name="verify_doughnut.py (reconstructed in Session 30; the Doughnut Economics arithmetic and transcript)",
         cmd=["python", "verify_doughnut.py"],
         files={k: k for k in (CANON, "neec_scores.csv", "verify_doughnut.py", DE_DOC)},
         stdout="verify_doughnut_output.txt"),
    dict(name="restate_s30.py restates the Doughnut Economics Verification section from its Session 29 snapshot (D22)",
         cmd=["python", "restate_s30.py", ".", "out"],
         files={k: k for k in (DE_S29, "d14_landing_s29.py", "restate_s30.py")},
         stdout="restate_s30_output.txt", outputs={"out/" + DE_DOC: DE_DOC}),
    dict(name="verify_comparative_claims.py (Session 30: comparative claims in the eleven documents; current corpus)",
         cmd=["python", "verify_comparative_claims.py"], files={k: k for k in CLAIMS30_INPUTS},
         stdout="verify_claims_s30_output.txt"),
    dict(name="verify_comparative_claims.py rejects the Doughnut Economics document as the D14 pass left it "
              "(negative control; exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files=dict({k: k for k in CLAIMS30_INPUTS}, **{DE_DOC: DE_S29}),
         stdout="verify_claims_s30_negative_output.txt", expect_exit=1),
    dict(name="build_corpus_file.py writes neec_corpus.json from the canonical corpus and the eleven documents (D23)",
         cmd=["python", "build_corpus_file.py"],
         files=dict({k: k for k in ("build_corpus_file.py", "neec_entry.py", CANON, "neec_scores.csv")},
                    **{d: d for d in ELEVEN}),
         stdout="build_corpus_file_output.txt", outputs={"neec_corpus.json": "neec_corpus.json"}),
    dict(name="neec_entry.py candidate-mode self-test (a synthetic candidate; seven altered ones rejected)",
         cmd=["python", "neec_entry.py", "--selftest", "--candidate"], files={k: k for k in ENTRY30},
         stdout="neec_entry_selftest_candidate_output.txt"),
    dict(name="neec_entry.py --candidate rejects a canonical entry (negative control; exit 1 expected)",
         cmd=["python", "neec_entry.py", "--candidate", OS_DOC], files=dict({k: k for k in ENTRY30}, **{OS_DOC: OS_DOC}),
         stdout="neec_entry_candidate_negative_output.txt", expect_exit=1),
    dict(name="build_replication_kit.py OS builds the first blind replication kit (blind protocol, corpus, brief; "
              "leak scan; archive)",
         cmd=["python", "build_replication_kit.py", "OS", ".", "out"], files={k: k for k in KIT_INPUTS},
         stdout="build_replication_kit_OS_output.txt",
         outputs={KIT + "SCORING_PROTOCOL.md": "replication_kit_OS_SCORING_PROTOCOL.md",
                  KIT + "neec_corpus.json": "replication_kit_OS_neec_corpus.json",
                  KIT + "REPLICATION_BRIEF.md": "replication_kit_OS_REPLICATION_BRIEF.md"}),
    dict(name="pilot baseline: the original Ostrom entry validates as a candidate against the kit's corpus",
         cmd=["python", "neec_entry.py", "--candidate", OS_DOC],
         files={"neec_entry.py": "neec_entry.py", "neec_corpus.json": "replication_kit_OS_neec_corpus.json",
                OS_DOC: OS_DOC},
         stdout="neec_entry_candidate_OS_blind_output.txt"),
    # --- Session 32: the first pilot replication's return ---
    dict(name="compare_replication.py self-test in a kit's layout (synthetic replications; refusals; the statistics)",
         cmd=["python", "compare_replication.py", "--selftest"], files=dict(KIT_LAYOUT),
         stdout="compare_replication_selftest_output.txt"),
    dict(name="compare_replication.py: pilot 1, the replication against the original entry (protocol 11.4), "
              "and the replication record's tables and attributions (11.5)",
         cmd=["python", "compare_replication.py", OS_DOC, REPL_DOC, "--canonical-corpus", "neec_corpus_canonical.json",
              "--record", REPL_RECORD],
         files=dict(KIT_LAYOUT, **{"neec_corpus_canonical.json": "neec_corpus.json", OS_DOC: OS_DOC,
                                   REPL_DOC: REPL_DOC, REPL_RECORD: REPL_RECORD}),
         stdout="compare_replication_OS_pilot1_output.txt"),
    dict(name="the replication's block validates as a candidate against the kit's corpus, with its D9 peer matrix "
              "(the replicator's own check, re-run)",
         cmd=["python", "neec_entry.py", "--candidate", REPL_DOC],
         files={"neec_entry.py": "neec_entry.py", "neec_corpus.json": "replication_kit_OS_neec_corpus.json",
                REPL_DOC: REPL_DOC},
         stdout="neec_entry_candidate_OSR_output.txt"),
    dict(name="compare_replication.py refuses to run beside the canonical script (negative control; exit 1 expected)",
         cmd=["python", "compare_replication.py", "--selftest"], files=dict(KIT_LAYOUT, **{CANON: CANON}),
         stdout=EMPTY, stderr="compare_replication_canonical_refusal_stderr.txt", expect_exit=1),
    dict(name="d18b_reexpression_s32.py: decision D18(b), the Ostrom register re-expressed, and D26 with it "
              "(no file changes)",
         cmd=["python", "d18b_reexpression_s32.py"],
         files=dict({k: k for k in ENTRY30 + ("d18b_reexpression_s32.py", REPL_DOC)}, **{d: d for d in ELEVEN}),
         stdout="d18b_reexpression_s32_output.txt"),
    # --- Session 20 corpus (20 systems), via the pinned Session 20 snapshot ---
    dict(name="verify_ostrom.py as of Session 25 (Session 23; Session 20 corpus, Session 25 document)",
         cmd=["python", "verify_ostrom.py"],
         files={CANON: S20, "verify_ostrom.py": S25["verify_ostrom.py"],
                PENDING["verify_ostrom.py"]: S25[PENDING["verify_ostrom.py"]]},
         stdout=S25_OUT["verify_ostrom_output.txt"]),
    dict(name="verify_islamicfinance.py as of Session 25 (Session 22; Session 20 corpus, Session 25 document)",
         cmd=["python", "verify_islamicfinance.py"],
         files={CANON: S20, "verify_islamicfinance.py": S25["verify_islamicfinance.py"],
                PENDING["verify_islamicfinance.py"]: S25[PENDING["verify_islamicfinance.py"]]},
         stdout=S25_OUT["verify_islamicfinance_output.txt"]),
    dict(name="verify_qatar.py as of Session 25 (Session 21; Session 20 corpus, Session 25 document)",
         cmd=["python", "verify_qatar.py"],
         files={CANON: S20, "verify_qatar.py": S25["verify_qatar.py"],
                PENDING["verify_qatar.py"]: S25[PENDING["verify_qatar.py"]]},
         stdout=S25_OUT["verify_qatar_output.txt"]),
    dict(name="Session 20 canonical script (20 systems, full report)",
         cmd=["python", CANON], files={CANON: S20, BASELINE: BASELINE},
         stdout="session20_v2script_output.txt"),
    dict(name="Session 20 CSV builder regenerates the Session 20 CSV",
         cmd=["python", BUILDER], files={CANON: S20, BUILDER: S20_BUILDER},
         stdout="session20_csv_builder_output.txt",
         outputs={"neec_scores.csv": S20_CSV}),
    dict(name="Session 20 generator reproduces the Session 20 canonical files from the Session 16 files",
         cmd=["python", "insert_session20.py", ".", "out"],
         files={k: k for k in (S16, "neec_scores_csv_builder_v2_s16_snapshot.py", "insert_session20.py",
                               "verify_swf.py", "verify_china.py", "verify_singapore.py")},
         stdout=None,
         outputs={"out/" + CANON: S20, "out/" + BUILDER: S20_BUILDER}),
    dict(name="verify_insertion_s20.py (Session 20 insertion; Session 20 corpus)",
         cmd=["python", "verify_insertion_s20.py"],
         files=dict(S20_INPUTS, **{"verify_insertion_s20.py": "verify_insertion_s20.py"}),
         stdout="verify_insertion_s20_output.txt"),
    dict(name="run_a4_full_rerun_20.py (Appendix A.4; Session 20 corpus)",
         cmd=["python", "run_a4_full_rerun_20.py"],
         files={CANON: S20, BASELINE: BASELINE, "run_a4_full_rerun_20.py": "run_a4_full_rerun_20.py"},
         stdout="a4_rerun_20_raw_output.txt"),
    # --- Session 16 and earlier corpora ---
    dict(name="verify_singapore.py (Session 19; Session 16 corpus)",
         cmd=["python", "verify_singapore.py"],
         files={CANON: S16, "verify_singapore.py": "verify_singapore.py",
                "verify_swf.py": "verify_swf.py", "verify_china.py": "verify_china.py",
                "NEEC_StateCapitalism_Singapore_scoring_scratch.md":
                    S26["NEEC_StateCapitalism_Singapore_scoring_scratch.md"]},
         stdout="verify_singapore_output.txt"),
    dict(name="verify_china.py (Session 18; Session 16 corpus)",
         cmd=["python", "verify_china.py"],
         files={CANON: S16, "verify_china.py": "verify_china.py", "verify_swf.py": "verify_swf.py",
                "NEEC_StateCapitalism_China_scoring_scratch.md":
                    S26["NEEC_StateCapitalism_China_scoring_scratch.md"]},
         stdout="verify_china_output.txt"),
    dict(name="verify_swf.py (Session 17; Session 16 corpus)",
         cmd=["python", "verify_swf.py"],
         files={CANON: S16, "verify_swf.py": "verify_swf.py"},
         stdout="verify_swf_output.txt"),
    dict(name="Session 16 canonical script (17 systems, full report)",
         cmd=["python", CANON], files={CANON: S16, BASELINE: BASELINE},
         stdout="session16_v2script_output.txt"),
    dict(name="session16_full_analysis.py (Session 16 corpus)",
         cmd=["python", "session16_full_analysis.py"],
         files={CANON: S16, BASELINE: BASELINE,
                "session16_full_analysis.py": "session16_full_analysis.py"},
         stdout="session16_full_analysis_output.txt"),
    dict(name="regen_analysis_paper.py (Session 10; 15-system view, baseline absent as in the original run)",
         cmd=["python", "regen_analysis_paper.py"],
         files={CANON: VIEW15, S16: S16, "regen_analysis_paper.py": "regen_analysis_paper.py"},
         stdout="regen_verification_output_v16.txt"),
    dict(name="run_a4_full_rerun.py (Session 12 Appendix A.4 run; 15-system view)",
         cmd=["python", "run_a4_full_rerun.py"],
         files={CANON: VIEW15, S16: S16, "run_a4_full_rerun.py": "run_a4_full_rerun.py"},
         stdout="full_a4_rerun_raw_output.txt"),
    dict(name="verify_ubs.py (Session 15; 15-system view; output first captured in Session 20)",
         cmd=["python", "verify_ubs.py"],
         files={CANON: VIEW15, S16: S16, "verify_ubs.py": "verify_ubs.py"},
         stdout="verify_ubs_output.txt"),
    dict(name="verify_new_systems.py (Session 16; output first captured in Session 20)",
         cmd=["python", "verify_new_systems.py"],
         files={"verify_new_systems.py": "verify_new_systems.py"},
         stdout="verify_new_systems_output.txt"),
    dict(name="step1c_retrofit.py (Session 8; output first captured in Session 20)",
         cmd=["python", "step1c_retrofit.py"],
         files={"step1c_retrofit.py": "step1c_retrofit.py", BASELINE: BASELINE},
         stdout="step1c_retrofit_output.txt"),
    dict(name="neec_c14_crossvalidation.py (Appendix G Python reference) reproduces its CSV",
         cmd=["python", "neec_c14_crossvalidation.py"],
         files={"neec_c14_crossvalidation.py": "neec_c14_crossvalidation.py"}, stdout=None,
         outputs={"neec_c14_crossvalidation_run2_v4.1_results.csv":
                  "neec_c14_crossvalidation_run2_v4_1_results.csv"}),
    dict(name="neec_c14_v41_realjs_check.js (Appendix G, v4.1 source) reproduces its CSV",
         cmd=["node", "neec_c14_v41_realjs_check.js"],
         files={"neec_c14_v41_realjs_check.js": "neec_c14_v41_realjs_check.js"}, stdout=None,
         outputs={"neec_c14_v41_realjs_yearbyyear.csv": "neec_c14_v41_realjs_yearbyyear.csv"}),
    dict(name="neec_c14_v42_realjs_check.js (Appendix G, v4.2 source) reproduces its CSV",
         cmd=["node", "neec_c14_v42_realjs_check.js"],
         files={"neec_c14_v42_realjs_check.js": "neec_c14_v42_realjs_check.js"}, stdout=None,
         outputs={"neec_c14_v42_realjs_yearbyyear.csv": "neec_c14_v42_realjs_yearbyyear.csv"}),
]

CLAIMS33_INPUTS = CLAIMS30_INPUTS + ("restate_s33.py", "d18b_reexpression_s32.py")
S33_CHECKS = [
    # --- the current state: Session 33, decisions D18(b) and D26 ---
    dict(name="insert_session33.py writes both canonical scripts from their Session 32 snapshots (decision D26)",
         cmd=["python", "insert_session33.py", ".", "out"],
         files={k: k for k in (S32[CANON], S32[BUILDER], "insert_session33.py")},
         stdout="insert_session33_output.txt", outputs={"out/" + CANON: CANON, "out/" + BUILDER: BUILDER}),
    dict(name="Canonical script, current corpus (Session 33: 23 systems, full report)",
         cmd=["python", CANON], files={CANON: CANON, BASELINE: BASELINE}, stdout="session33_v2script_output.txt"),
    dict(name="CSV builder regenerates neec_scores.csv (Session 33)",
         cmd=["python", BUILDER], files={CANON: CANON, BUILDER: BUILDER},
         stdout="session33_csv_builder_output.txt", outputs={"neec_scores.csv": "neec_scores.csv"}),
    dict(name="verify_insertion_s33.py (one cell changed; CSV, corpus file and corpus consistent; negative tests)",
         cmd=["python", "verify_insertion_s33.py"],
         files={k: k for k in ("verify_insertion_s33.py", CANON, S32[CANON], "neec_scores.csv", S32["neec_scores.csv"],
                               "neec_corpus.json", S32["neec_corpus.json"])},
         stdout="verify_insertion_s33_output.txt"),
    dict(name="restate_s33.py restates seven scoring documents from their Session 32 snapshots (D18(b), D26)",
         cmd=["python", "restate_s33.py", ".", "out"],
         files=dict({S32[d]: S32[d] for d in S33_DOCS},
                    **{k: k for k in ("restate_s33.py", "d14_landing_s29.py", "d18b_reexpression_s32.py",
                                      "neec_entry.py", CANON, "neec_scores.csv")}),
         stdout="restate_s33_output.txt", outputs={"out/" + d: d for d in S33_DOCS}),
    dict(name="verify_comparative_claims.py (Session 33: comparative claims in the eleven documents; current corpus)",
         cmd=["python", "verify_comparative_claims.py"], files={k: k for k in CLAIMS33_INPUTS},
         stdout="verify_claims_s33_output.txt"),
    dict(name="verify_comparative_claims.py (Session 33) rejects the seven Session 32 documents (negative control; "
              "exit 1 expected)",
         cmd=["python", "verify_comparative_claims.py"],
         files={k: (S32[k] if k in S33_DOCS else k) for k in CLAIMS33_INPUTS},
         stdout="verify_claims_s33_negative_output.txt", expect_exit=1),
    dict(name="build_corpus_file.py writes neec_corpus.json from the Session 33 corpus and documents",
         cmd=["python", "build_corpus_file.py"],
         files=dict({k: k for k in ("build_corpus_file.py", "neec_entry.py", CANON, "neec_scores.csv")},
                    **{d: d for d in ELEVEN}),
         stdout="build_corpus_file_s33_output.txt", outputs={"neec_corpus.json": "neec_corpus.json"}),
    dict(name="neec_entry.py reads the 23 summary blocks from the eleven documents (Session 33) and prints the D13 "
              "inventory",
         cmd=["python", "neec_entry.py"] + list(ELEVEN) + ["--corpus"],
         files=dict({k: k for k in ("neec_entry.py", CANON, "neec_scores.csv")}, **{d: d for d in ELEVEN}),
         stdout="neec_entry_documents_s33_output.txt"),
    dict(name="verify_doughnut.py on the Session 33 corpus (the same captured output: D26 does not touch it)",
         cmd=["python", "verify_doughnut.py"],
         files={k: k for k in (CANON, "neec_scores.csv", "verify_doughnut.py", DE_DOC)},
         stdout="verify_doughnut_output.txt"),
]


# Session 34: Appendix A.4 on the Session 33 corpus (appended after the version 8 checks).
S34_CHECKS = [
    dict(name="run_a4_full_rerun_33.py (Appendix A.4, Session 33 corpus)",
         cmd=["python", "run_a4_full_rerun_33.py"],
         files={CANON: CANON, BASELINE: BASELINE, "run_a4_full_rerun_33.py": "run_a4_full_rerun_33.py"},
         stdout="a4_rerun_33_raw_output.txt"),
    dict(name="run_a4_full_rerun_33.py rejects the Session 32 corpus (negative control; exit 1 expected; its seven "
              "re-derived checks fail and nothing is written to stderr)",
         cmd=["python", "run_a4_full_rerun_33.py"],
         files={CANON: S32[CANON], BASELINE: BASELINE, "run_a4_full_rerun_33.py": "run_a4_full_rerun_33.py"},
         stdout="a4_rerun_33_negative_output.txt", stderr=EMPTY, expect_exit=1),
    dict(name="build_readme.py regenerates README.md from neec_scores.csv and this harness (the landing page "
              "cannot drift from the data)",
         cmd=["python", "build_readme.py"],
         files={k: k for k in ("build_readme.py", "neec_scores.csv", "run_all_checks.py", "SCORING_PROTOCOL.md",
                               "criteria.json")},
         stdout=None, outputs={"README.md": "README.md"}),
]


def pin32(chk):
    """A version 7 check, run against the Session 32 files: sources and reference outputs map to snapshots."""
    c = dict(chk)
    pin = {**S44, **S35, **S32}
    c["files"] = {dest: pin.get(src, src) for dest, src in chk["files"].items()}
    c["outputs"] = {prod: pin.get(ref, ref) for prod, ref in chk.get("outputs", {}).items()}
    if c["files"] != chk["files"] or c["outputs"] != chk.get("outputs", {}):
        c["name"] = chk["name"] + " [Session 32 state]"
    return c


def pin44(chk):
    """A Session 36-44 check, run against the files as they stood at tag s44 (sources and reference outputs)."""
    c = dict(chk)
    c["files"] = {dest: S44.get(src, src) for dest, src in chk["files"].items()}
    c["outputs"] = {prod: S44.get(ref, ref) for prod, ref in chk.get("outputs", {}).items()}
    if c["files"] != chk["files"] or c["outputs"] != chk.get("outputs", {}):
        c["name"] = chk["name"] + " [Session 44 state]"
    return c


# Session 35: revision R4's audit and decision D28 (appended after the version 9 checks).
S35_CHECKS = [
    dict(name="r4_audit_s35.py (revision R4: every corpus 1.0 on a multi-clause Pass Threshold, audited clause by "
              "clause; decision D28 and its bound; the record's tables; changes no file) [Session 35 state]",
         cmd=["python", "r4_audit_s35.py"],
         files={k: S35.get(k, k) for k in ("r4_audit_s35.py", "criteria.json", "neec_corpus.json", "neec_scores.csv",
                               "NEEC_Report_v1_6.md", "NEEC_R4_MultiClause_Audit_s35.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md",
                               "NEEC_IslamicFinance_scoring_scratch.md", "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="r4_audit_s35_output.txt", stderr=EMPTY),
]

# Session 36: protocol v2.0-draft.5, the corrected criteria.json, revision R8 (appended after the version 10 checks).
PROTO_DOCS = ("NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
              "NEEC_DoughnutEconomics_scoring_scratch.md", "NEEC_UniversalBasicServices_scoring_scratch.md",
              "NEEC_SovereignWealthFundStatism_scoring_scratch.md", "NEEC_StateCapitalism_China_scoring_scratch.md",
              "NEEC_StateCapitalism_Singapore_scoring_scratch.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
              QA_DOC, IF_DOC, OS_DOC, REPL_DOC)
PROTO_INPUTS = ("verify_protocol_s36.py", "SCORING_PROTOCOL.md", "criteria.json", "neec_corpus.json", "neec_entry.py",
                "r4_audit_s35.py") + PROTO_DOCS
S36_CHECKS = [
    dict(name="build_criteria.py (Session 36) generates criteria.json and corrects it: every anchor threshold is its "
              "definition's Pass Threshold (D28(g)); C3.2's bands carry D26 (R3)",
         cmd=["python", "build_criteria.py"],
         files={k: k for k in ("build_criteria.py", "NEEC_Paper_v1_4.md", CANON)},
         stdout="build_criteria_s36_output.txt", outputs={"criteria.json": "criteria.json"}),
    dict(name="build_replication_kit.py --selftest-r8: revision R8 on protocol draft.5 (no kit built; the first kit's "
              "3.1 marker is one R8 refuses)",
         cmd=["python", "build_replication_kit.py", "--selftest-r8", "."],
         files={k: k for k in ("build_replication_kit.py", "SCORING_PROTOCOL.md", "SCORING_PROTOCOL_s35_snapshot.md")},
         stdout="build_replication_kit_r8_selftest_output.txt", stderr=EMPTY),
    dict(name="verify_protocol_s36.py: the protocol's statements about the corpus, its archetype table, register and "
              "Appendix B (draft.5)",
         cmd=["python", "verify_protocol_s36.py"], files={k: k for k in PROTO_INPUTS},
         stdout="verify_protocol_s36_output.txt", stderr=EMPTY),
    dict(name="verify_protocol_s36.py rejects protocol draft.4 (negative control; exit 1 expected; its stale "
              "statements fail and nothing is written to stderr)",
         cmd=["python", "verify_protocol_s36.py"],
         files=dict({k: k for k in PROTO_INPUTS}, **{"SCORING_PROTOCOL.md": S35["SCORING_PROTOCOL.md"]}),
         stdout="verify_protocol_s36_negative_output.txt", stderr=EMPTY, expect_exit=1),
]

# Session 37: the rescoring pass, part (a) (appended after the version 11 checks).
S37_CHECKS = [
    dict(name="rescoring_s37.py: rescoring pass part (a), the 33 stated-shortfall 1.0s re-estimated clause by clause "
              "(D28, D31); consequences computed, no corpus file changed",
         cmd=["python", "rescoring_s37.py"],
         files={k: k for k in ("rescoring_s37.py", "r4_audit_s35.py", "criteria.json", "neec_corpus.json",
                               "NEEC_Rescoring_s37.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s37_output.txt", stderr=EMPTY),
]

# Session 38: the rescoring pass, part (b), first group (appended after the version 12 checks).
S38_CHECKS = [
    dict(name="rescoring_s38.py: rescoring pass part (b), first group, the 29 units of C3.4, C5.3, C2.4, C1.3 and "
              "C2.3 re-estimated clause by clause (D28, D31); consequences with part (a), no corpus file changed",
         cmd=["python", "rescoring_s38.py"],
         files={k: k for k in ("rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py", "criteria.json",
                               "neec_corpus.json", "NEEC_Rescoring_s38.md", "cco_simulation_checks_s38_output.txt",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s38_output.txt", stderr=EMPTY),
]

# Session 39: the rescoring pass, part (b), second group (appended after the version 13 checks).
S39_CHECKS = [
    dict(name="rescoring_s39.py: rescoring pass part (b), second group, C5.1 clause 2 on 11 units and C3.1's 5 "
              "units re-estimated clause by clause (D28); consequences with parts (a) and (b1), no corpus file changed",
         cmd=["python", "rescoring_s39.py"],
         files={k: k for k in ("rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py",
                               "criteria.json", "neec_corpus.json", "NEEC_Rescoring_s39.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s39_output.txt", stderr=EMPTY),
]

# Session 40: the rescoring pass, part (b), third group (appended after the version 14 checks).
S40_CHECKS = [
    dict(name="rescoring_s40.py: rescoring pass part (b), third group, C1.1's 9 units re-estimated clause by clause "
              "(D28), CCO's against the design's pinned simulation; consequences with parts (a), (b1) and (b2), no "
              "corpus file changed",
         cmd=["python", "rescoring_s40.py"],
         files={k: k for k in ("rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py",
                               "r4_audit_s35.py", "criteria.json", "neec_corpus.json", "NEEC_Rescoring_s40.md",
                               "cco_simulation_checks_s40_output.txt",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s40_output.txt", stderr=EMPTY),
]

# Session 41: the rescoring pass, part (b), fourth group (appended after the version 15 checks).
S41_CHECKS = [
    dict(name="rescoring_s41.py: rescoring pass part (b), fourth group, the 11 units of C1.4, C2.1 and C3.2 "
              "re-estimated clause by clause (D28); consequences with parts (a) to (b3), no corpus file changed",
         cmd=["python", "rescoring_s41.py"],
         files={k: k for k in ("rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py",
                               "rescoring_s37.py", "r4_audit_s35.py", "criteria.json", "neec_corpus.json",
                               "NEEC_Rescoring_s41.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s41_output.txt", stderr=EMPTY),
]

# Session 42: the rescoring pass, part (b), fifth group (appended after the version 16 checks).
S42_CHECKS = [
    dict(name="rescoring_s42.py: rescoring pass part (b), fifth group, C2.5's 10 units re-estimated clause by "
              "clause (D28); consequences with parts (a) to (b4), no corpus file changed",
         cmd=["python", "rescoring_s42.py"],
         files={k: k for k in ("rescoring_s42.py", "rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py",
                               "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py", "criteria.json",
                               "neec_corpus.json", "NEEC_Rescoring_s42.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s42_output.txt", stderr=EMPTY),
]

# Session 43: the rescoring pass, part (b), sixth group (appended after the version 17 checks).
S43_CHECKS = [
    dict(name="rescoring_s43.py: rescoring pass part (b), sixth group, the 10 units of C3.5 and C4.1 re-estimated "
              "clause by clause (D28); consequences with parts (a) to (b5), no corpus file changed",
         cmd=["python", "rescoring_s43.py"],
         files={k: k for k in ("rescoring_s43.py", "rescoring_s42.py", "rescoring_s41.py", "rescoring_s40.py",
                               "rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py", "r4_audit_s35.py",
                               "criteria.json", "neec_corpus.json", "NEEC_Rescoring_s43.md",
                               "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s43_output.txt", stderr=EMPTY),
]

# Session 44: the criteria review's evidence tables (appended after the version 18 checks).
S44_CHECKS = [
    dict(name="criteria_review_s44.py: the criteria review's evidence tables (norm weights, quantities scored in more "
              "than one Pass Threshold, their corpus agreement, Requirement figures differing from a Pass Threshold)",
         cmd=["python", "criteria_review_s44.py"],
         files={k: k for k in ("criteria_review_s44.py", "criteria.json", "neec_corpus.json")},
         stdout="criteria_review_s44_output.txt", stderr=EMPTY),
]

# Session 45: the v2.0 criteria (appended after the version 19 checks).
V2_INPUTS = ("build_criteria.py", "criteria_s44_snapshot.json", "SCORING_PROTOCOL_s44_snapshot.md",
             "NEEC_Criteria_v2_s45.md")
S45_CHECKS = [
    dict(name="build_criteria.py (version 2.3) builds criteria.json v2.0, 29 criteria, from the pinned Session 44 "
              "criteria and the record's Appendix V, asserts rules A1-A7, and regenerates the protocol as draft.9",
         cmd=["python", "build_criteria.py"], files={k: k for k in V2_INPUTS},
         stdout="build_criteria_s49_output.txt", stderr=EMPTY,
         outputs={"criteria.json": "criteria.json", "SCORING_PROTOCOL.md": "SCORING_PROTOCOL.md"}),
    dict(name="build_criteria.py --selftest: each of rules A1-A7 rejects a planted violation, and the clean v2.0 "
              "document passes (negative control)",
         cmd=["python", "build_criteria.py", "--selftest"], files={k: k for k in V2_INPUTS},
         stdout="build_criteria_s46_selftest_output.txt", stderr=EMPTY),
    dict(name="criteria_v2_s45.py: the v2.0 record's evidence tables (figure scan, norm weights, units by revision "
              "class, registered quantities, C4.6's clause 3 bar from the World Justice Project's data)",
         cmd=["python", "criteria_v2_s45.py"],
         files={k: k for k in ("criteria_v2_s45.py", "criteria_s44_snapshot.json", "criteria.json",
                               "NEEC_Criteria_v2_s45.md", "neec_corpus.json", "wjp_rol_sf62_2012_2025.csv")},
         stdout="criteria_v2_s45_output.txt", stderr=EMPTY),
]

# Session 47: part (b)'s seventh group, on the v2.0 clauses (appended after the version 21 checks). It reads the
# v2.0 criteria.json for the clauses and criteria_s44_snapshot.json for the published structure. Since Session 48
# (decision 48.3 moved C4.4 to class M) it reads criteria.json as it stood at tag s47, criteria_s47_snapshot.json.
S47_CHECKS = [
    dict(name="rescoring_s47.py: rescoring pass part (b), seventh group, the 10 units of C4.2 and C4.4 on the v2.0 "
              "clauses, with part (a)'s 3 units of those criteria re-read (D28); consequences with parts (a) to (b6), "
              "no corpus file changed [Session 47 criteria]",
         cmd=["python", "rescoring_s47.py"],
         files={k: k for k in ("rescoring_s47.py", "rescoring_s43.py", "rescoring_s42.py", "rescoring_s41.py",
                               "rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py", "rescoring_s37.py",
                               "r4_audit_s35.py", "criteria_s44_snapshot.json", "neec_corpus.json",
                               "NEEC_Rescoring_s47.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s47_output.txt", stderr=EMPTY),
]
S47_CHECKS[0]["files"]["criteria.json"] = "criteria_s47_snapshot.json"

# Session 48: C4.4 re-read on decision 48.3, and the score ledger (appended after the version 22 checks). It reads the
# v2.0 criteria.json (with 48.3) and criteria_s47_snapshot.json side by side, so it is not pinned.
S48_CHECKS = [
    dict(name="rescoring_s48.py: C4.4's six units in the pass re-read on decision 48.3's measure (D28), Nordic Social "
              "Democracy's clause 1 bound, consequences with parts (a) to (b7), and the score ledger; no corpus file "
              "changed",
         cmd=["python", "rescoring_s48.py"],
         files={k: k for k in ("rescoring_s48.py", "rescoring_s47.py", "rescoring_s43.py", "rescoring_s42.py",
                               "rescoring_s41.py", "rescoring_s40.py", "rescoring_s39.py", "rescoring_s38.py",
                               "rescoring_s37.py", "r4_audit_s35.py", "criteria.json", "criteria_s47_snapshot.json",
                               "criteria_s44_snapshot.json", "neec_corpus.json", "neec_scores.csv",
                               "NEEC_Report_v1_6.md", "NEEC_Rescoring_s48.md", "NEEC_Step1c_Retrofit_C1_2ab_C1_5.md",
                               "NEEC_Georgism_LVT_scoring_scratch.md", "NEEC_MutualCredit_LETS_scoring_scratch.md",
                               "NEEC_DoughnutEconomics_scoring_scratch.md",
                               "NEEC_UniversalBasicServices_scoring_scratch.md",
                               "NEEC_SovereignWealthFundStatism_scoring_scratch.md",
                               "NEEC_StateCapitalism_China_scoring_scratch.md",
                               "NEEC_StateCapitalism_Singapore_scoring_scratch.md",
                               "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "NEEC_IslamicFinance_scoring_scratch.md",
                               "NEEC_Ostrom_Commons_scoring_scratch.md")},
         stdout="rescoring_s48_output.txt", stderr=EMPTY),
]


def tree(*roots):
    """Every file under the given directories here, each mapped to itself (the copy keeps the subdirectories)."""
    out = {}
    for root in roots:
        for r, _, fs in os.walk(os.path.join(HERE, root)):
            for f in fs:
                rel = os.path.relpath(os.path.join(r, f), HERE).replace(os.sep, "/")
                out[rel] = rel
    return dict(sorted(out.items()))


# Session 49: the public site (appended after the version 23 checks). build_site.py --check rebuilds docs/ in its own
# temporary directory from its inputs and site/, and compares the result with docs/, which is copied in whole.
S49_CHECKS = [
    dict(name="build_site.py --check: the public site docs/ equals what build_site.py generates from criteria.json, "
              "the corpus, the record, Paper v1.4, the A.4 weighting script, the WJP extract, the issue forms and "
              "site/ (decision 49.7)",
         cmd=["python", "build_site.py", "--check"],
         files={**{k: k for k in ("build_site.py", "criteria.json", "neec_corpus.json", "neec_scores.csv",
                                  "summary_blocks_s28.json", "NEEC_Criteria_v2_s45.md", "NEEC_Paper_v1_4.md",
                                  "wjp_rol_sf62_2012_2025.csv", "neec_weighting_robustness_analysis_v2.py")},
                **tree("site", "docs", os.path.join(".github", "ISSUE_TEMPLATE"))},
         stdout="build_site_check_output.txt", stderr=EMPTY, show_stdout=True),
]
S49_CHECKS.append(dict(S49_CHECKS[0], files={**S49_CHECKS[0]["files"], "docs/index.html": "docs/404.html"},
                       name="build_site.py --check rejects a docs/ whose home page is replaced by another page "
                            "(negative control; exit 1 expected)",
                       stdout="build_site_check_negative_output.txt", expect_exit=1))

CHECKS = (S33_CHECKS + [pin32(c) for c in V7_CHECKS] + S34_CHECKS + S35_CHECKS
          + [pin44(c) for c in S36_CHECKS + S37_CHECKS + S38_CHECKS + S39_CHECKS + S40_CHECKS + S41_CHECKS
             + S42_CHECKS + S43_CHECKS + S44_CHECKS]
          + S45_CHECKS + S47_CHECKS + S48_CHECKS + S49_CHECKS)


def md5(data):
    return hashlib.md5(data).hexdigest()[:8]


def run_check(chk):
    exe = sys.executable if chk["cmd"][0] == "python" else shutil.which(chk["cmd"][0])
    if exe is None:
        return "SKIP", [f"{chk['cmd'][0]} not found on PATH"]
    notes = []
    with tempfile.TemporaryDirectory() as tmp:
        for dest, src in chk["files"].items():
            target = os.path.join(tmp, dest)
            if src == VIEW15:
                with open(target, "w", encoding="utf-8") as f:
                    f.write(VIEW15_SOURCE)
                continue
            if not os.path.isfile(os.path.join(HERE, src)):
                return "FAIL", [f"missing input file: {src}"]
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copy(os.path.join(HERE, src), target)
        proc = subprocess.run([exe] + chk["cmd"][1:], cwd=tmp, capture_output=True)
        expect = chk.get("expect_exit", 0)
        ok = proc.returncode == expect
        if not ok:
            tail = proc.stderr.decode("utf-8", "replace").strip().splitlines()[-1:] or [""]
            notes.append(f"exit status {proc.returncode}, expected {expect}: {tail[0][:120]}")
        elif expect:
            notes.append(f"exit status {proc.returncode}, as expected")
        if chk.get("show_stdout"):
            notes.append(proc.stdout.decode("utf-8", "replace").strip())
        for stream, got in (("stdout", proc.stdout), ("stderr", proc.stderr)):
            name = chk.get(stream)
            if not name:
                continue
            if name == EMPTY:
                ref, label = b"", "(empty)"
            elif not os.path.isfile(os.path.join(HERE, name)):
                ok = False
                notes.append(f"{stream}: missing reference file {name}")
                continue
            else:
                ref, label = open(os.path.join(HERE, name), "rb").read(), name
            same = got == ref
            ok = ok and same
            notes.append(f"{stream} {'==' if same else '!='} {label} (md5 {md5(ref)})")
        for produced, reference in chk.get("outputs", {}).items():
            p = os.path.join(tmp, produced)
            if not os.path.isfile(os.path.join(HERE, reference)):
                ok = False
                notes.append(f"missing reference file {reference}")
                continue
            ref = open(os.path.join(HERE, reference), "rb").read()
            same = os.path.isfile(p) and open(p, "rb").read() == ref
            ok = ok and same
            notes.append(f"{os.path.basename(produced)} {'==' if same else '!='} {reference} (md5 {md5(ref)})")
    return ("PASS" if ok else "FAIL"), notes


def main():
    print("=" * 92)
    print(f"run_all_checks.py -- {len(CHECKS)} reproducibility checks")
    print("=" * 92)
    tally = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    for i, chk in enumerate(CHECKS, 1):
        status, notes = run_check(chk)
        tally[status] += 1
        print(f"\n[{i:2d}] {status}  {chk['name']}")
        for n in notes:
            print(f"          {n}")
    print("\n" + "=" * 92)
    print(f"SUMMARY: {tally['PASS']} passed, {tally['FAIL']} failed, {tally['SKIP']} skipped "
          f"(of {len(CHECKS)}).")
    print("Not covered here: the realjs scripts' fidelity to index.html (the Compassionism")
    print("Simulation source, which is not in this directory), and the Report and Paper prose.")
    return 1 if tally["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
