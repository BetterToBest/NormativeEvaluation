# NEEC Replication Record — Ostrom-Style Commons Governance, pilot 1

**Status.** The replication record that protocol 11.5 requires for the first
blind replication (decision D2). Session 32, written 2026-09-21 from the pilot
returned on 2026-09-19. Written by the maintainers — Claude in the NEEC
Project, who can read the original scoring and is therefore **not blind** — from
the two scoring documents and the output of `compare_replication.py`. The six
generated sections below are written and checked by `compare_replication.py
--record`; everything else is attribution and consequence, and is open to the
owner's review.

---

## 1. The pilot

| | |
|---|---|
| Target | Ostrom-Style Commons Governance (code `OS`), scored natively on the v2 structure in Session 23 |
| Original | `NEEC_Ostrom_Commons_scoring_scratch.md`, the canonical entry |
| Replication | `NEEC_OstromCommons_replication_scoring.md` (code `OSR`) |
| Replicator | Claude Sonnet 5 in an incognito claude.ai chat outside the NEEC Project: no project files, no memory; a single blind pass on 2026-09-19 |
| Kit | `neec_replication_kit_OS.zip` (MD5 `81a254e8`), rebuilt byte for byte by `build_replication_kit.py OS` |
| Comparison | `compare_replication.py`, run in the kit's layout, with the canonical corpus supplied separately |

**Validation (protocol 11.3).** Both blocks validate as candidates against the
kit's 22-entry corpus. The original block is the canonical entry: its key, code,
display name and vector match the canonical corpus file. The kit's corpus is the
canonical corpus with exactly the target withheld. The replicator did not return
its `neec_entry.py --candidate` output as a file, but the peer matrix pasted in
its document matches the tool's output, re-run here, in every cell and figure.

**A blindness leak, reported by the replicator and confirmed.** The kit's blind
copy of the protocol marks, in section 3.1, where the target was withheld from
the list of declared examples: *...Islamic finance and one example withheld from
this blind copy (the "narrow single-mechanism" archetype).* The marker
stands inside the **mechanism** list and names the **archetype**, so it
discloses, before any analysis, the scope class and archetype of the target —
the very question the pilot was built to test (11.6). The replicator disclosed
this in its overview and its reviewer disclosure, and states that its own
analysis independently supports the classification. That statement cannot be
checked. The class agreement in section 6 below is therefore **not evidence
that the protocol's scope rule is reproducible**; every other comparison is
unaffected by it. The defect lies in `build_replication_kit.py`, not in the
replicator's conduct (revision R8, section 10).

---

## 2. Result at a glance

<!-- BEGIN GENERATED: summary -->
| | Original | Replication |
|---|---|---|
| Material Security | 2.0 | 1.5 |
| Human Autonomy | 2.5 | 2.5 |
| System Resilience | 2.5 | 3.0 |
| Ethical Integrity | 3.0 | 2.0 |
| Implementation Viability | 4.0 | 4.0 |
| **Total** | **14.0/26 (54%)** | **13.0/26 (50%)** |
| Structural failures | 4 (C1.2a, C1.5, C2.2, C3.2) | 5 (C1.2a, C1.4, C1.5, C2.2, C4.3) |
| Tier | Partially Adequate | Partially Adequate |
| Flagged criteria | 20 | 5 |
| Undisputed failures | 0 | 3 (C1.2a, C1.5, C2.2) |
<!-- END GENERATED: summary -->

The two scorings agree on the tier, on 22 of 26 criteria exactly, and on all
26 within one step. The four differences are the subject of section 4.

---

## 3. The vectors

<!-- BEGIN GENERATED: vectors -->
| Criterion | Original | Replication | Difference | Original's alternatives | Replication's alternatives |
|---|---|---|---|---|---|
| C1.1 | 0.5 | 0.5 |  | 0.0 | — |
| C1.2a | 0.0 | 0.0 |  | 0.5 | — |
| C1.2b | 0.5 | 0.5 |  | 1.0 | 1.0 |
| C1.3 | 0.5 | 0.5 |  | 0.0 | — |
| C1.4 | **0.5** | **0.0** | -0.5 | 0.0 | 0.5 |
| C1.5 | 0.0 | 0.0 |  | 0.5 | — |
| C2.1 | 0.5 | 0.5 |  | — | — |
| C2.2 | 0.0 | 0.0 |  | 0.5 | — |
| C2.3 | 0.5 | 0.5 |  | — | — |
| C2.4 | 0.5 | 0.5 |  | 1.0 | 1.0 |
| C2.5 | 1.0 | 1.0 |  | 0.5 | — |
| C3.1 | 0.5 | 0.5 |  | 1.0 | — |
| C3.2 | **0.0** | **0.5** | +0.5 | 0.5 | — |
| C3.3 | 0.5 | 0.5 |  | 1.0 | — |
| C3.4 | 1.0 | 1.0 |  | — | — |
| C3.5 | 0.5 | 0.5 |  | 1.0 | — |
| C4.1 | **1.0** | **0.5** | -0.5 | 0.5 | — |
| C4.2 | 0.5 | 0.5 |  | 1.0 | 1.0 |
| C4.3 | **0.5** | **0.0** | -0.5 | 0.0 | 0.5 |
| C4.4 | 0.5 | 0.5 |  | 0.0 | — |
| C4.5 | 0.5 | 0.5 |  | 0.0 | — |
| C5.1 | 1.0 | 1.0 |  | — | — |
| C5.2 | 0.5 | 0.5 |  | 0.0 | — |
| C5.3 | 1.0 | 1.0 |  | — | — |
| C5.4 | 0.5 | 0.5 |  | 1.0 | — |
| C5.5 | 1.0 | 1.0 |  | — | — |
<!-- END GENERATED: vectors -->

<!-- BEGIN GENERATED: agreement -->
| Measure | Result |
|---|---|
| Exact matches | 22 of 26 |
| Differences | 4: C1.4, C3.2, C4.1, C4.3 (replication higher on 1, lower on 3) |
| Within one step (0.5) | 26 of 26 |
| Failure status agrees | 23 of 26 |
| Cohen's kappa (values as categories) | 0.719 |
| Krippendorff's alpha (interval) | 0.803 |
| Differences inside the original's register | 4 of 4 |
| Differences inside the replication's register | 2 of 4 |
| Differences inside neither register | 0 |
| Replication's vector is a combination of the original's register | yes |
| Original's vector is a combination of the replication's register | no |
<!-- END GENERATED: agreement -->

Cohen's kappa and Krippendorff's alpha are reported descriptively. Twenty-six
criteria of one entry are not a sample of independent items and two scorers
are not a sample of scorers: the statistics describe this comparison and
estimate nothing.

---

## 4. The four disagreements, attributed (protocol 11.5)

Protocol 11.5 attributes each disagreement to **evidence** (the scorers relied on
different facts), **interpretation** (the same facts and the same rules, read
differently where the rules leave the reading to the scorer), **scope** (a
different class, population rule or boundary) or **protocol** (the protocol's
text leaves open, or answers two ways, the question that decides the score). The
test applied here: a disagreement is attributed to the protocol when a stated
rule would have forced the two scorers to the same value on the same facts.

<!-- BEGIN ATTRIBUTION -->
| Criterion | Original | Replication | Attribution | The deciding question | Revision |
|---|---|---|---|---|---|
| C1.4 | 0.5 | 0.0 | interpretation | Is an in-kind subsistence buffer, reaching only a resource's members and never tested against displacement, "a buffer or partial mechanism" (0.5) or no mechanism (0.0)? | none |
| C3.2 | 0.0 | 0.5 | protocol | Does the 0.0 anchor band cover a mechanism that simply has no monetary function, or only an active inflationary mechanism? The band's text says the first; its note says the second. | R3, decision D26 |
| C4.1 | 1.0 | 0.5 | protocol | Can a mechanism score 1.0 when it meets the anchor's description structurally but two clauses of a conjunctive Pass Threshold lie outside its reach? | R4 |
| C4.3 | 0.5 | 0.0 | protocol | Does documented, replicated implementation failure count against "the system's own logic" (2.1), and is a remedy imposed by the state inside the mechanism? | R2 |
<!-- END ATTRIBUTION -->

No disagreement is attributed to **evidence**: the two documents draw on
overlapping sources and neither disputes a fact the other relies on. None is
attributed to **scope**: the class and the population rule are identical, and the
one boundary question each document met is carried as a scenario or a flag, not
as a different score (sections 5 and 6).

### C1.4 Automation Resilience — interpretation

Both documents record the same facts: a commons share is not conditioned on
employment, so fuel, fodder, water and fish keep arriving under displacement;
the buffer reaches only the resource's members; there is no aggregate-demand
mechanism; and no case has been tested against the criterion's displacement
scenarios. The original scores 0.5, on the logic that gave Georgism, Mutual
Credit / LETS, Sovereign Wealth Fund Statism and Universal Basic Services 0.5
here. The replication scores 0.0, arguing that "component-validated" reasoning
(4.1) cannot borrow confidence the components never earned on this question. The
disagreement is a reading of the same facts against the anchors, and the
protocol leaves that reading to the scorer; each document flags the other's
value, so the register on each side carries the doubt. One observation, not an
attribution: the 0.5 band's text — "a buffer or partial mechanism exists but is
not designed for or shown to survive the higher-severity scenarios" — describes
the facts both documents state, while the 0.0 band — "system structurally
requires wage labor for both income distribution and demand" — does not
describe a membership entitlement. The anchor text leans toward the original's
value. No revision is proposed.

### C3.2 Inflation Control Mechanisms — protocol

The original scores 0.0 because the mechanism "has no monetary function of any
kind", adding that "the reason is simple absence rather than malfunction". The
replication scores 0.5, citing the anchor's instruction to reserve 0.0 for an
active inflationary mechanism "rather than merely 'unaddressed.'" Both readings
are in the anchor (`criteria.json`, C3.2, band 0.0), which contradicts itself: its
first sentence admits "No credible inflation-control mechanism is specified",
and its note then reserves the band for an active inflationary mechanism with no
counterbalancing design element. The original follows the first sentence (and
protocol 2.1's generic 0.0: "no structural mechanism addresses the criterion");
the replication follows the note. The original's own stated reason is the case
the note excludes.

Two further points. The replication reached the original's alternative *value*
but not its alternative *reading*: the original's alternative credits a
household-level hedge against price shocks in the governed goods, which the
replication does not mention. A difference that lies inside a register is not
thereby a difference the register anticipated. And the note is already known to
be stale — its "no system in the 13 scores 0.0 here" predates the corpus of 23;
Correction 7 carries it. Resolving the contradiction changes a canonical score,
so it is raised as decision **D26** (section 10).

### C4.1 Intergenerational Justice — protocol

The original scores 1.0: the design principles were drawn from institutions
defined by passing the resource and its rules to successors intact, resource use
at or below regeneration is the mechanism's own success condition, and the
anchor's 1.0 band asks that preservation be "structural, not incidental". Its
flag states the alternative, 0.5, "on the reading that the criterion also
carries a debt-to-GDP clause and an absolute-carbon clause that the mechanism
does not address at all". The replication scores 0.5 for exactly that reason:
the carbon-trajectory and debt-to-GDP clauses lie outside the sectors the
mechanism governs, so the transfer is real but incomplete (the 0.5 band).

The protocol does not settle which governs when an anchor's description is met
but clauses of a conjunctive Pass Threshold lie outside a mechanism's reach.
Section 2.1 makes 1.0 "a claim that the threshold is cleared" and 2.3 scores
against the Pass Threshold, which favours the replication; 4.6 supplies the
anchors that describe each band, and the 1.0 band's description favours the
original. The corpus holds
precedent both ways: Sovereign Wealth Fund Statism scores 1.0 here on its
explicit intergenerational-transfer rationale, while three of the replication's
four declared peers score 0.5. A rule written for this criterion alone would
bear on every 1.0 in the corpus that rests on a multi-clause threshold, so R4
begins with an audit of those scores, not with a rule.

### C4.3 Racial and Gender Equity — protocol

Both documents cite Agarwal's participatory exclusions, and between them they
document the exclusion of women, Dalits, landless and Indigenous users across
several countries.
The original scores 0.5 because the exclusion comes with "documented, working
remedies" — India's Joint Forest Management quotas on user-group committees,
and collective-tenure recognition as a gain to some of the most disadvantaged
people in the world. The replication scores 0.0: membership rules tied to
tenure, residency or customary status transmit existing disparities forward,
and the quotas produce token rather than substantive inclusion. Each flags the
other's value, and each frames the pivot the same way — a structural failure or
a correctable implementation shortfall.

That is the question the replicator logged as a protocol ambiguity: whether
documented, replicated implementation failure counts against "the system's own
logic", in 2.1's definition of 0.0. The original's alternative adds a second
open question — whether quotas set by the state are "an external correction
rather than part of the mechanism" — which 3.2 would treat as a boundary
question. The protocol answers neither, and each decides the score (R2).

---

## 5. The flags

<!-- BEGIN GENERATED: flags -->
| Criterion | Original (scored → alternatives) | Replication (scored → alternatives) | Relation |
|---|---|---|---|
| C1.1 | 0.5 → 0.0 | 0.5, not flagged | original only |
| C1.2a | 0.0 → 0.5 | 0.0, not flagged | original only |
| C1.2b | 0.5 → 1.0 | 0.5 → 1.0 | same |
| C1.3 | 0.5 → 0.0 | 0.5, not flagged | original only |
| C1.4 | 0.5 → 0.0 | 0.0 → 0.5 | mirrored |
| C1.5 | 0.0 → 0.5 | 0.0, not flagged | original only |
| C2.2 | 0.0 → 0.5 | 0.0, not flagged | original only |
| C2.4 | 0.5 → 1.0 | 0.5 → 1.0 | same |
| C2.5 | 1.0 → 0.5 | 1.0, not flagged | original only |
| C3.1 | 0.5 → 1.0 | 0.5, not flagged | original only |
| C3.2 | 0.0 → 0.5 | 0.5, not flagged | original only |
| C3.3 | 0.5 → 1.0 | 0.5, not flagged | original only |
| C3.5 | 0.5 → 1.0 | 0.5, not flagged | original only |
| C4.1 | 1.0 → 0.5 | 0.5, not flagged | original only |
| C4.2 | 0.5 → 1.0 | 0.5 → 1.0 | same |
| C4.3 | 0.5 → 0.0 | 0.0 → 0.5 | mirrored |
| C4.4 | 0.5 → 0.0 | 0.5, not flagged | original only |
| C4.5 | 0.5 → 0.0 | 0.5, not flagged | original only |
| C5.2 | 0.5 → 0.0 | 0.5, not flagged | original only |
| C5.4 | 0.5 → 1.0 | 0.5, not flagged | original only |

Flagged by both: 5 of 20 flagged criteria (Jaccard 0.250); 3 same, 2 mirrored, 0 other.
<!-- END GENERATED: flags -->

The five criteria both documents flag carry the same doubts: three with the
same alternative, and C1.4 and C4.3 in mirror, each side flagging the other's
value. The original flags fifteen more. Of those, two — **C3.2 and C4.1** — are
where the replication in fact took the other value, unflagged. The broad
register was informative exactly there, and the narrow one missed both of its
own disagreements with the original: the replication's vector is a combination
of the original's register, but the original's vector is not a combination of
the replication's.

The count of flags is not the measure of an entry's uncertainty (protocol 6.4),
and the pilot does not show that the original's other thirteen unshared flags
were unwarranted; one scorer's silence is weak evidence. It does show that
**four of the original's flags carry scope questions rather than doubts** —
the matter decision D18(b) deferred to this pilot (section 10.1).

---

## 6. Scope

<!-- BEGIN GENERATED: scope -->
| | Original | Replication |
|---|---|---|
| Scope class | mechanism (stated) | mechanism (stated) |
| Scenarios | `knowledge-commons` (scope): C1.5 → 0.5, C2.3 → 1.0 — 15.0/26, 3 failures, Partially Adequate | `no_housing_extension` (scope): C1.3 → 0.0 — 12.5/26, 6 failures, Structurally Inadequate |
| Declared peers | none declared | Georgism / Land Value Tax, Mutual Credit / LETS, Sovereign Wealth Fund Statism, Islamic Finance / Profit-Sharing Banking |
<!-- END GENERATED: scope -->

**Class and rule.** Both documents declare the mechanism class and the rule
"generalisation, not best-casing". For the reason given in section 1, the class
agreement is not evidence that the classification is reproducible. The rule's
agreement is expected: protocol 3.2 now fixes it, where the original chose it.

**Boundaries.** Each document met one boundary question and handled it
differently. The original counts community land trusts **in** — "the mapping is
explicit rather than analogical" — and flags the reading that counts them out
(C1.3, 0.5 → 0.0). The replication also counts them in, and carries the reading
that counts them out as a **scope scenario** (`no_housing_extension`, C1.3 → 0.0),
as protocol 3.2 prescribes for "counting an adjacent instrument in or out of the
mechanism's boundary". The same question, on the same criterion, with the same
value: a flag in one document and a scenario in the other. The original's second
boundary question, the knowledge and digital commons, is counted out and reported
as a scenario; the replication does not raise it.

The scenario matters more to the replication than to the original. Counting land
trusts out moves the replication from 5 failures to 6 — Structurally Inadequate —
and the original from 4 to 5, Partially Adequate either way.

**Peers.** The original declares none; it was scored before decision D9
required a declaration. The replication declares Georgism / Land Value Tax,
Mutual Credit / LETS, Sovereign Wealth Fund Statism and Islamic Finance /
Profit-Sharing Banking, and says it chose them by the "narrow single-mechanism"
archetype read from protocol examples, since the protocol never defines the term
(R5).

---

## 7. Joint readings and the D13 measure

<!-- BEGIN GENERATED: readings -->
| Side | Reading | Basis | Total | Failures | Tier |
|---|---|---|---|---|---|
| Original | `A` | stated | 19.5/26 | 0 | Potentially Adequate |
| Original | `B` | scored | 14.0/26 | 4 | Partially Adequate |
| Original | `C` | stated | 9.5/26 | 11 | Structurally Inadequate |
| Replication | `scored` | scored | 13.0/26 | 5 | Partially Adequate |
| Replication | `reform_optimistic` | stated | 14.0/26 | 4 | Partially Adequate |
| Replication | `extremes_down` | extremes | 13.0/26 | 5 | Partially Adequate |
| Replication | `extremes_up` | extremes | 15.5/26 | 3 | Partially Adequate |

- **Original, D13:** reach 3 tier(s) (PA/Part/SI); span 10.0 points / 11 failures; not tier-robust; enumeration 1,048,576 combinations, 46.7% keep the scored tier (assumes independent calls).
- **Replication, D13:** reach 1 tier(s) (Part); span 2.5 points / 2 failures; tier-robust; enumeration 32 combinations, 100.0% keep the scored tier (assumes independent calls).
<!-- END GENERATED: readings -->

The original's readings A and C span all three tiers because they resolve the
population-scope question — the founding literature's resource frame against
full population scale — through the register. The replication, with that
question fixed by rule, reaches one tier. Protocol 11.6 expected the pilot's
disagreement to "concentrate in the scope question". In the scored vectors it
did not: none of the four disagreements is a scope question. The scope question
appeared instead as a difference in **how uncertainty was expressed** — twenty
flags spanning three tiers on one side, five flags and a boundary scenario on the
other.

---

## 8. What the pilot shows

1. **The scored vectors reproduce closely.** 22 of 26 exact, 26 of 26 within one
   step, failure status agreeing on 23 of 26, the same tier.
2. **Every disagreement lies inside the original's register**, and the
   replication's vector is a combination of it. The original's register
   contained an independent scorer's answer; the replication's did not contain
   the original's.
3. **Three of the four disagreements trace to questions the protocol leaves
   open** — an anchor that contradicts itself (C3.2), an unstated relation
   between anchors and conjunctive thresholds (C4.1), and an unstated treatment of
   replicated implementation failure (C4.3). The fourth (C1.4) is a reading the
   protocol leaves to the scorer, flagged in mirror on both sides.
4. **The line between a flag and a scope question is not yet operational.** Both
   scorers carried C4.2's frame question — the mechanism's own domain or the
   whole economy — as a flag, and the original carried three more such questions
   (C1.3, C3.1, C3.5). Protocol 3.4 states the principle but gives no test.

## 9. What the pilot does not show

- **Reliability across scorers in general.** One replicator, one pass, and the
  same model family as the original's scorer. Shared training can produce shared
  readings; agreement between two Claude models may overstate the agreement a
  human scorer or another model family would reach.
- **That the scope classification is reproducible**, because of the leak
  (section 1).
- **Independence from the corpus.** The replicator calibrated against the kit's
  22 entries, as protocol 5 requires; peer calibration pulls a draft toward its
  peers, and the original was scored before calibration was required.
- **Anything about the attribution itself.** The attributions in section 4 are
  the maintainers', and the maintainers wrote the original.

---

## 10. Consequences

### 10.1 Decision D18(b): decided — the register is re-expressed

Protocol 3.4(b) carried the entry's twenty flags as scored until this pilot,
because sorting them into scope questions and doubts looked like new scoring
judgment. The pilot supplies an independent check of a sort, and the decision
taken is to **re-express the register by a stated test, applied to each flag's
own stated alternative reading** — the text the original wrote, not new
judgment about the evidence. The test, proposed as protocol text (R1):

> A flag's alternative reading is a **scope question** when it (i) reads the
> criterion's threshold against a population, domain or frame other than the one
> the declared population rule fixes — for a mechanism, the resource or
> membership it governs in place of the economy-wide population — or (ii) counts
> an adjacent instrument, programme or extension in or out of the mechanism's
> boundary. A scope question is reported as a scenario and leaves the register.
> An alternative reading that joins such a clause to a doubt stays a flag if the
> doubt alone reaches the alternative value, and stays a flag when the text does
> not settle whether it does.

`d18b_reexpression_s32.py` applies it, locating each deciding phrase exactly
once in the original. Four flags are scope questions: **C1.3** (land trusts
counted out: boundary), **C3.1** (coverage read against the governed population),
**C3.5** (externalisation read against the governed resource) and **C4.2**
(compliance read in the mechanism's own frame). Two are borderline and stay:
**C4.3**, whose boundary clause is joined to a doubt the blind replication showed
reaching 0.0 on its own, and **C5.2**, where the text does not settle it. The
pilot bears on the four directly: the replication carried C1.3's question as a
scenario, scored C3.1 and C3.5 at the original's values without doubt under the
fixed rule, and — like the original — carried C4.2's frame question as a flag.

**No score changes.** The script's results, which the application pass will
restate in the document:

| | As scored | Re-expressed |
|---|---|---|
| Flags (calls) | 20 (20) | 16 (16) |
| Joint readings | A 19.5 / 0 failures; B 14.0 / 4; C 9.5 / 11 | up 18.0 / 0; scored 14.0 / 4; down 10.0 / 10 |
| D13 | 3 tiers; 10.0 points, 11 failures | 3 tiers; 8.0 points, 10 failures |
| Enumeration | 1,048,576 combinations; 46.7% keep the tier | 65,536; 56.8% |
| Scenarios | knowledge commons (15.0 / 3) | knowledge commons (15.0 / 3); land trusts out (13.5 / 5); resource frame (15.5 / 4) |
| D13 position in the corpus | least tier-robust | least tier-robust |
| Flag count against the corpus | largest (Islamic finance 16) | tied with Islamic finance |

Readings A and C were named for the scope question — "the long-enduring case",
"strict population scope" — so the re-expressed entry takes the two extremes of
its register, decision D16's default. **Sensitivity:** moving either borderline
flag out as well leaves the entry the least tier-robust; moving both makes
Islamic finance the least tier-robust and this entry the second. Under the same
test the replication's own C4.2 flag is also a frame question; without it the
replication is still tier-robust (4 flags; 2.0 points, 2 failures).

**Application** is a restatement in place (decisions D12, D14) and follows in the
next data-changing pass, by generator, with pinned inputs: the document's flagged
calls, joint readings, scenarios and block; the claims verifier's assertions that
change ("twenty of twenty-six", "the largest flagged set"); protocol 3.4(b), 3.5
and 6.4; and the kit builder's signature figures. Ostrom's Part I entry in Paper
v2.0 waits for it.

### 10.2 Decision D26 (new): the C3.2 anchor — recommended

The contradiction in C3.2's 0.0 band must be resolved one way. **Recommended:**
the note governs — it is the more specific instruction, and it names the
"unaddressed" case and excludes it. The band is reworded to reserve 0.0 for an
active inflationary mechanism with no counterbalancing element (with Correction
7's stale count removed), and the corpus is brought into line. Ostrom-Style
Commons Governance is the only entry scored 0.0 on C3.2, and its stated reason
is absence, so its C3.2 becomes **0.5**: 14.5/26, 3 failures, Partially Adequate
(tier unchanged), and its C3.2 flag lapses, since 0.0 is no longer open to it.
With D18(b), its register becomes 15 flags (up 18.0 / 0 failures, down 10.5 / 9;
3 tiers, 7.5 points, 9 failures; 32,768 combinations, 65.6% keep the tier) and
its corpus position stays least tier-robust. One stated result would change: the
knowledge-commons scenario, now tier-neutral, would reach Potentially Adequate
(15.5/26, 2 failures), so the document's "tier-neutral" sentence is among those
the application restates. The alternative — the band's first
sentence governs, and the note is struck — would keep Ostrom at 0.0 and open 0.0
to any entry with no inflation mechanism of its own, which would require
re-examining every mechanism-class entry now at 0.5. D26 changes a canonical
score; it is applied with D18(b), by generator, unless the owner decides
otherwise.

### 10.3 Protocol revisions (for v2.0-draft.5)

| | Section | Revision | From |
|---|---|---|---|
| R1 | 3.4 | The scope-or-doubt test quoted in 10.1 | C1.3, C3.1, C3.5, C4.2; D18(b) |
| R2 | 2.1, 4.1 | How documented, replicated implementation failure bears on "the system's own logic"; a remedy imposed from outside the mechanism is a boundary question (3.2) | C4.3; replicator's ambiguity 2 |
| R3 | 4.6, `criteria.json` | C3.2's 0.0 band reworded per D26; Correction 7 applied to it | C3.2 |
| R4 | 2.3 | Whether a conjunctive Pass Threshold is cleared clause by clause, and how a clause outside a mechanism's reach counts. **First** an audit of every corpus 1.0 on a multi-clause threshold (Sovereign Wealth Fund Statism's C4.1 among them); the rule follows the audit | C4.1 |
| R5 | 5.1 | "Archetype" defined by a table of the corpus's archetypes and their members, so that peers can be declared by rule | replicator's ambiguity 3 |
| R6 | 3.2 | An extension belongs to the scored mechanism when the founding literature maps it to the mechanism's design explicitly; one the literature disputes is scored out, with a scenario counting it in — the practice both documents followed (land trusts in; knowledge commons out) | replicator's ambiguity 1 |
| R7 | 11.6 | The pilot's result, with a pointer to this record | section 7 |
| R8 | 11.2 (D24) | In a blind copy, a withheld example is dropped from its list without a marker at that point where the marker would disclose the withheld fact; the header says that a class list was shortened, not which | section 1 |

R8 changes `build_replication_kit.py` for future kits only; the issued OS kit
stays reproducible byte for byte from the pinned Session 30 protocol.

### 10.4 The next pilot

The self-referential concern the Paper answers in its section 10.5 — the
project's owner designed CCO-PTF-CIP-SZH and co-authors the framework that scores
it — is the concern a replication can test most directly, and this pilot did not
test it. The recommended second pilot is **CCO-PTF-CIP-SZH**, run by a replicator
outside the Claude model family (another AI system, a human scorer, or a
Runpod-hosted model orchestrated from a NEEC-blind session, per Handoff 31's
D25), from a kit built with R8 applied.
