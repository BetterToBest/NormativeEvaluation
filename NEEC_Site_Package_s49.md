# NEEC site package, for Session 49

Prepared in a claude.ai chat session on 2026-09-24, at the owner's request, from the repository at tag `s48`
(`main` at 5aed860, 283 files). It starts the public version 2.0 site that the design brief
(`NEEC_Site_Design_Brief_s45.md`, decision 45.5) governs, ahead of stage 6, because the owner asked for the site
to be built now and the scores added once they are finalized. It changes no score, criterion, protocol text or
generated corpus file.

## 1. What the package does

- `build_site.py` (new, standard library only) generates the whole site into `docs/` from `criteria.json`,
  `neec_corpus.json`, `neec_scores.csv`, `summary_blocks_s28.json`, `wjp_rol_sf62_2012_2025.csv` (md5 checked),
  the Appendix A.4 weighting script (its `SCHEMES`, imported unmodified and asserted) and the hand-edited sources in
  `site/`. `--check` rebuilds in a temporary directory and compares with `docs/`; `--preview DIR` writes a preview
  that shows the published scores, never to `docs/`. The output is byte-deterministic.
- `docs/` (generated, 77 files): 61 pages (home, Findings, 23 system pages, 29 criterion pages, their two indexes,
  Thresholds, Method, Replicate, Contribute, 404), `data/neec.json`, `data/wjp-sf62.json`, two AI prompt files, `llms.txt`,
  `sitemap.xml`, `.nojekyll`, and the assets.
- The preview build inlines the fonts in its stylesheet, because browsers refuse web fonts loaded by URL from a
  page opened from disk; `docs/` keeps them as files.
- `site/` (hand-edited sources): `config.json` (links, the score gate, short names, weighting schemes, nav, issue
  forms), `thresholds.json` (the judgment-call catalog), `ai_prompt.md` (the prompt template), `pages/*.html` (the
  prose of each page, with `{{placeholders}}` the generator fills), and `assets/` (stylesheet, script, favicon, and
  the self-hosted fonts with their OFL licences: Source Serif 4, subset; IBM Plex Mono, converted to WOFF2 without
  subsetting because Plex has a Reserved Font Name).
- `.github/CONTRIBUTING.md` (replaced; it was a four-line pointer) and six issue forms with `config.yml`, replacing
  `score-challenge.md` and `propose-system.md`.
- `NEEC_Site_Design_Brief_s45.md`: an amendment section at the end records what changes (S1 to S9; S10 is a link).

## 2. Decisions for the record

Record these as 49.1 to 49.10 in the criteria record's decision list (or wherever Session 49 judges right), each
marked as below. None changes a score.

- **S1 (the owner's direction; the gate's mechanics are the chat session's).** The site shows no scores until
  version 2.0's are final. `site/config.json` `scores.publish` is false; the field shows every system and criterion
  with quiet dots, grouped by kind of system, and each score-bearing view says the scores are being finalized, with
  a link to the version 1 site. Setting the gate to true fails the build unless the corpus is on exactly the
  criteria of `criteria.json` and every total, failure count, tier and percent equals `neec_scores.csv` (this is the
  brief's "site data equals the corpus" assertion). *Reason:* beyond the owner's direction, the published totals
  are being re-estimated, and a new public site should not put forward figures the pass is known to lower
  (Handoff 48 records CCO-PTF-CIP-SZH at 24.5/26 published and 18.5/26 after the pass so far, provisionally).
- **S2 (flagged; the owner may reverse).** Navigation: Findings, Systems, Criteria, Thresholds, Method, Replicate,
  Contribute. The brief's Findings item is kept, as the page that holds the visual suite (S9); the computed findings
  also appear on the home page under the field.
- **S3 (the owner's direction; the catalog's contents are the chat session's, flagged).** A Thresholds page, "Set
  your own bar": a live explorer for C4.6 clause 3's bar on the World Justice Project extract (every edition,
  snap points at the adopted 0.77 and the recorded median 0.61, the reference economies of `criteria_v2_s45.py`
  section 5, and the range of bars that keeps their verdicts, computed live); a weighting explorer (A.4's four
  schemes and the reader's own domain weights); a close-calls explorer (the registered joint readings); and a
  catalog of 11 judgment calls: record section 4's consequential choices, 47.1 and 48.1, 48.3, 45.1, and C1.2b's
  wealth Gini bar, which the owner raised. Each entry paraphrases the record and cites its decisions; the build
  checks that each decision and clause exists and prints each clause verbatim from `criteria.json`. The owner
  should read the 11 paraphrases once.
- **S4 (the owner's direction; the route is the chat session's).** "Push back" buttons open GitHub issue forms
  prefilled with the system, criterion or topic. GitHub Discussions is the forum, not an outside service: it is
  free, uses the same account, and keeps moderation in one place. Its links stay hidden until the owner enables
  Discussions and sets `site.discussions` to true.
- **S5 (the owner's direction; the design is the chat session's, flagged).** The Replicate page builds an AI prompt
  in two modes (audit the published scores; score blind, per protocol section 11's rule), for any system and
  criterion, embedding the chosen Pass Thresholds and clauses so that an AI without browsing can proceed. It asks
  for clause-by-clause verdicts, citations opened in the session, the four kinds of divergence (evidence,
  interpretation, scope, protocol; `NEEC_CONTRIBUTING.md` section 2), a disclosure, and a JSON block
  (`"neec_check": "1"`), and routes the result to the AI-check form. It is an informal check; formal blind
  replication still follows the kit.
- **S6 (polish).** Every page is complete without script. `docs/data/neec.json`, `docs/llms.txt`, `sitemap.xml`
  and schema.org Dataset markup on the home page serve search engines and AI systems.
- **S7 (the chat session's).** Harness check 93, `python3 build_site.py --check`, keeps `docs/` equal to its
  sources. The build also asserts the A.4 schemes, the WJP extract's md5, C4.6's bar against the 2025 upper
  quartile (47.1), every local link, every issue form and prefilled field, and the absence of placeholders.
- **S8 (the chat session's, flagged).** `.github/CONTRIBUTING.md` becomes the front door for six routes, with what
  happens to a report: reproduced by a maintainer (the owner and the Claude working sessions); a correction made; a
  judgment recorded as a numbered decision; a score changed only through the recorded pass. It says that, under
  GitHub's terms of service, content added to the repository is licensed under its licence, CC BY 4.0. The forms
  keep the two existing labels (`score-challenge`, `system-proposal`) and use four new ones (`evidence`,
  `push-back`, `ai-replication`, `criterion-proposal`).

- **S9 (the owner's direction; the adaptation is the chat session's, flagged).** The five views of the v1 Visual
  Suite (`NEEC_Visual_Suite_-_Needs_Update_-_Copied_from_Claude_Artifact`; its update `NEEC_Visual_Suite_v2.jsx`)
  are carried into the site, each generated from the data rather than typed:
  (1) *Framework structure*, on the Criteria page and public now: the premises and core criteria are read from Paper
  v1.4, sections 3 and 4 (the build asserts 6 and 14, numbered in order), and each applied criterion's links from
  its derivation in `criteria.json` (all 29 parse; the derivations name N7 three ways, and the diagram uses the
  Paper's title). No links are drawn from the premises, because the Paper gives no premise-by-criterion table.
  (2) *System comparison*, on the Findings page: a bar per total, a ring per structural failure, ordered by total or
  by tier. (3) *Domain analysis*: a radar of up to three systems, with the median of all systems, on the Findings
  page, and each system's own on its page. (4) *Pareto frontier*: any two dimensions, with the frontier computed on
  them. (5) *Key insights*: the computed findings, with one added (the highest total among configured national
  economies).
  *Corrections to v1, made in the adaptation rather than carried over:* (a) v1's radar gave every domain a maximum
  of 5; Domain 1 had 6 (the v2 file already normalized it), and v2.0's maxima are 6, 6, 6, 6 and 5, so the radar
  plots shares of each domain's points. (b) v1's Pareto view plotted total against material security, hard-coded
  three frontier systems, and called them non-dominated "across all dimensions". A two-axis frontier is not the
  all-criteria non-dominated set: on the published corpus, the frontier on those two axes is CCO-PTF-CIP-SZH alone,
  while 12 systems are non-dominated across all 26 criteria. The site states both, computed, and keeps v1's
  "Understanding the Pareto Frontier" explanation at the owner's request (2026-09-25), rewritten to be exact: what
  dominance and the frontier mean; which systems are on the frontier across all criteria; each dominated system
  with the frontier systems that dominate it and on how many criteria; and v1's closing advice ("rational
  policymakers should prefer non-dominated systems"), recast as what dominance does and does not show: preferring
  a dominated system gives up points somewhere and gains none, under the criteria as written, while dominance
  says nothing about what the criteria leave out or about margins. Hovering over a dot on the chart shows its
  details; a click or tap keeps them open, and a second click closes them (Enter from the keyboard).
  (c) v1's insight cards are stale or no longer true on the published corpus: "no systems fall between" the tiers (8
  are Partially Adequate); "half the evaluated systems achieve adequacy" (6 of 23); Nordic Social Democracy's 74%
  on 18.5/25 (now 75% on 19.5/26, provisional); and C1.4 as "most discriminating", which v1 does not define (the
  site reports the most often failed criteria, C1.5 and C2.2 on the published corpus, 11 of 23 each). (d) v1's
  closing panel, "The Choice Before Humanity", is advocacy and is not carried over: the site states findings with
  their limits, which matters more because the author's own design ranks first. The owner may reverse this; the
  panel could live on the Research Hub or the Compassionism pages instead.
  The two v1 suite files are left in place; retiring them once the site is live is the owner's call.

- **S10 (the owner's direction, 2026-09-25).** In the disclosure, "CCO-PTF-CIP-SZH" links to the Research Hub
  (https://bettertobest.github.io/research-hub/) and opens it in a new tab. The link is made in both places the
  disclosure appears: the Method page's Disclosure section and its short form under "Who made this" on the home
  page. The system's own page, and every other mention, are unchanged.

**A clarification for the owner, recorded here.** The owner's message spoke of the open "Gini mark", where "if the
median Gini is used some systems score 1 where they now score 0.5". As in 48.1, that is read as C4.6 clause 3's
World Justice Project bar (0.77, or the median 0.61), which 48.1 settled at 0.77. The median would change the
verdict of that one clause for Qatar and China; it cannot by itself raise a score to 1.0, because C4.6 needs all
three clauses shown and no C4.6 unit has been scored. C1.2b's wealth Gini bar (below 0.35) is a separate bar,
settled in Session 45 with no alternative recorded; it is in the catalog, marked as having no data in the
repository yet.

## 3. Files

106 new (`build_site.py`; 20 under `site/`; 77 under `docs/`; 7 under `.github/ISSUE_TEMPLATE/`; this note), 2
replaced (`.github/CONTRIBUTING.md`, `NEEC_Site_Design_Brief_s45.md`), 2 deleted
(`.github/ISSUE_TEMPLATE/score-challenge.md`, `.github/ISSUE_TEMPLATE/propose-system.md`). After applying:
387 tracked files, before Session 49's own handoff. With the package applied, `run_all_checks.py` still
reproduces `run_all_checks_output.txt` byte for byte (92 checks, verified in the chat session), because no check
reads the new files; check 93 is added in step 4 below.

## 4. Applying this package

For the cloud session that finds `NEEC_repository_s49.zip` at the repository root (CLAUDE.md, Start, step 1).
This is Session 49: apply the package, then continue with Handoff 48, section 6, and land once.

1. On a new branch from main, unzip `NEEC_repository_s49.zip` into the repository root, overwriting; delete
   `.github/ISSUE_TEMPLATE/score-challenge.md` and `.github/ISSUE_TEMPLATE/propose-system.md`; delete the zip;
   `git add -A`. Expect 387 tracked files.
2. Run `python3 build_site.py --check`. Expect `site matches its sources: 77 files, scores not yet published`. If
   it reports a difference, run `python3 build_site.py`, inspect `git diff --stat docs/`, and record the cause.
3. Run the harness and expect no difference:
   `python3 run_all_checks.py > /tmp/out.txt ; cmp /tmp/out.txt run_all_checks_output.txt`.
4. Add check 93 to `run_all_checks.py`, the way the harness adds its other script checks: run
   `python3 build_site.py --check`, require exit status 0, and print its one line. Update the harness's check
   count and summary line, recapture `run_all_checks_output.txt`, and run the harness again.
5. Record S1 to S10 as decisions (section 2), and the corrections in section 5 as corrections if made. Then continue
   with Handoff 48, section 6 ("Next session (49): start here"). If that work changes `criteria.json`, the corpus or
   anything else the site reads, run `python3 build_site.py` and commit `docs/` with it.
6. In Handoff 49, give the owner the one-time steps in section 6 below, and add to its standing notes: any change to
   the site's inputs needs `python3 build_site.py` before the harness.

## 5. Corrections found, not made

These lie outside the site and are left to Session 49:

- `llms.txt` (repository root, hand-maintained) says `criteria.json` holds "the 26 criteria"; it holds 29. It names
  the protocol as version 2.0-draft.5; `README.md` names draft.9.
- `NEEC_CONTRIBUTING.md` says NEEC scores each system on 26 criteria (lines 5, 51 and 102). True of the published
  corpus, not of `criteria.json`; restate when version 2.0 is released.
- `CITATION.cff`: its abstract says 26 criteria, and its `url` points to the version 1 site. When the new site is
  live, the `url` could point to it.

## 6. The owner's steps (one time)

1. Upload `NEEC_repository_s49.zip` at the repository root (**Add file → Upload files → Commit changes** to `main`),
   then start a cloud session with `Continue NEEC.`
2. After Session 49 lands (tag `s49`), turn on Pages: **Settings → Pages → Build and deployment → Deploy from a
   branch → `main` → `/docs` → Save.** The site appears at https://bettertobest.github.io/NormativeEvaluation/
   within a few minutes. From then on, every landing requests a Pages build (`land-session.yml`).
3. Optional: **Settings → General → Features → Discussions.** Then ask a session to set `site.discussions` to true
   in `site/config.json`, which shows the "Discuss it openly" links.
4. Optional: **Issues → Labels → New label** for `evidence`, `push-back`, `ai-replication` and
   `criterion-proposal`, so that reports arrive sorted.
5. Optional: add the new site's address to the Research Hub's NEEC entry.

## 7. Keeping the site current

- **Scores at version 2.0.** When stage 3 has generated the 29-criterion corpus and CSV, set `scores.publish` to true
  in `site/config.json` and name the new summary-blocks file there; the build then checks the corpus against
  `criteria.json` and the CSV, and fills the field, the findings (all computed, none typed), the Findings page's
  charts, the weighting and close-calls explorers, the comparison tool, and every system and criterion page.
  When Paper v2.0 exists, point `sources.paper` at it; the structure diagram is read from it.
- **A new system.** Once inserted into the corpus, it appears everywhere on the next build. Give it a short name
  under `systems` in `site/config.json` (optional; the display name is used otherwise).
- **A new criterion.** Once in `criteria.json` (and, for scores, the corpus), it gets its page, its column and its
  prompt text on the next build.
- **A new judgment call.** Add an entry to `site/thresholds.json` with its criteria, clause, decisions and texts.
  When 48.3 is confirmed or reversed, update `c44-accountability`'s status there.
- **A new explorer.** When the data for another bar (C1.2b's wealth Gini, C2.6's Freedom House scores) are
  committed with an md5 check, the WJP explorer is the pattern: a model function in `build_site.py`, a section in
  `page_thresholds`, a function in `site/assets/neec.js`.
- **Prose.** Edit `site/pages/*.html` and run `python3 build_site.py`. Never edit `docs/` by hand; check 93 fails.
