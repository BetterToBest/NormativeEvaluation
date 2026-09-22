# NEEC Evaluation: Ostrom-Style Commons Governance

**SCRATCH DRAFT — Step 1b, Session 23 (2026-09-17).** Follows Appendix H.9's
submission template, applied to the 26-criterion structure (the published H.9
still describes 25 criteria; see Handoff 20, correction 2). Scored directly
against the fully specified v2 structure (Section 12.3, Appendix H.7 and
H.7v2), as the nine earlier Step 1b systems were. **This is the tenth and last
Step 1b entry; with it, Step 1b closed.** Added to `neec_scores.csv` and the
canonical scoring scripts in Session 25; not yet independently cross-checked
by a second scorer (H.9 Step 6), which remains open per this project's
disclosure norms (`NEEC_CONTRIBUTING.md` §2, Appendix H.6).

Every arithmetic, transcription, and sensitivity claim below is checked by
`verify_ostrom.py`, whose output is captured in `verify_ostrom_output.txt`,
and the summary table is written by that script (`python3 verify_ostrom.py
--fill`), not typed. Comparative claims are stated on the canonical 23-system
corpus and checked by `verify_comparative_claims.py`, which also writes the
corpus table (`--fill`). Research notes are in
`session23_research_notes.md`, written during the research turn per Handoff
21's instruction.

---

## 23 [pending renumbering]. Ostrom-Style Commons Governance

### Overview

**What is scored.** Paper Section 8.1 names this candidate entry "Ostrom-style
commons governance." The scored object is the **governance mechanism**: Elinor
Ostrom's design principles for common-pool-resource institutions, as set out in
*Governing the Commons: The Evolution of Institutions for Collective Action*
(Cambridge, 1990) and refined in her later work, applied to a resource system
embedded in a wider market economy. This follows the scope logic of Georgism /
Land Value Tax, Mutual Credit / LETS, Sovereign Wealth Fund Statism and Islamic
Finance, not the configured-national-economy logic of the three
state-capitalism sub-entries.

**The eight design principles**, as stated by the Ostrom Workshop and the
secondary literature: (1) clearly defined boundaries; (2) congruence between
appropriation and provision rules and local conditions — split by Cox, Arnold
and Villamayor-Tomás into congruence with local conditions and proportional
equivalence between benefits and costs; (3) collective-choice arrangements, so
that most of those affected by the operational rules can modify them; (4)
monitoring, by monitors accountable to the appropriators or drawn from them;
(5) graduated sanctions; (6) cheap and rapidly accessible conflict resolution;
(7) minimal recognition of the right to organise by external authorities; and
(8) nested enterprises, so that larger resource systems are organised in
multiple layers with small local units at the base.

**Scope decisions (recommended in Handoff 22 as D7; confirmed by the user in
Session 23).**

- **Score the governance mechanism, not a country.** Nepal's community forestry
  programme is the principal implementation case at national scale and supplies
  most of the operating evidence, but Nepal's poverty, housing and
  macroeconomic outcomes are not credited to the mechanism except where the
  mechanism is doing the work. The classic long-enduring cases, modern
  fisheries co-management, and community forestry across Asia, Africa and Latin
  America supply the rest.
- **The knowledge and digital commons extension is adjacent, not included.**
  Wikipedia, open-source software, open data and data commons have all been
  analysed with the design principles. They are nonetheless scored as a **scope
  scenario**, not folded in. The reason is stronger here than in Session 22's
  social-finance decision: the Governing Knowledge Commons workshop's own
  position is that knowledge resources may not be common-pool resources at all,
  that a tragedy of the commons may not be the key threat, and that Ostrom's
  design principles are neither natural starting points nor natural conclusions
  for shared knowledge resources. Hess and Ostrom's *Understanding Knowledge as
  a Commons* (MIT Press, 2006) opened the field precisely because the transfer
  is not straightforward. Linåker and Runeson (2022) give the structural
  reason: a natural commons must regulate consumption, whereas a digital
  commons must stimulate both use and provisioning, so subtractability concerns
  maintenance capacity rather than availability. Summary Scores enumerates the
  alternative.
- **Stock or flow (Session 17's sub-distinction), and the archetype.** The
  mechanism is **stock-like** — a forest, an aquifer, a fishery or a pasture is
  an accumulating natural-capital corpus — but it is the corpus's **first
  collectively held, non-severable stock**: no member holds an individual
  transferable claim on it. See "Archetype" below for the second axis this
  entry adds.
- **Scale, stated as a convention rather than left implicit** (D7 required
  this). Ostrom's cases are small-n and local; NEEC's thresholds are
  population-level. The convention applied throughout is **generalisation, not
  best-casing**: the mechanism is scored as though every common-pool resource
  in an economy were governed by an Ostrom-principled institution, and the
  population-scope thresholds are then applied to the resulting economy-wide
  outcome. This is the convention Georgism received — a land-value tax levied
  economy-wide rather than in one municipality. Where the mechanism's reach is
  **structurally bounded** rather than merely small, as at C1.5, the bound is
  scored as a bound and not excused as a scope mismatch.

**The design, in one paragraph.** A common-pool resource is subtractable and
hard to exclude from, which is the condition Hardin's parable treats as fatal.
Ostrom's finding is that resource users have repeatedly built institutions that
avoid both privatisation and central regulation, and that the durable ones
share a specifiable structure: a bounded membership, rules fitted to the
resource and revisable by those they bind, monitoring and graduated sanctions
run by the users themselves, fast and cheap dispute resolution, external
recognition of the right to self-organise, and nesting for larger systems. The
claim made for this design is that it sustains the resource indefinitely, keeps
decision rights with the people who bear the consequences, and does so at lower
cost than either state administration or enclosure.

**The empirical record, in one paragraph.** Cox, Arnold and Villamayor-Tomás
(*Ecology and Society* 15(4): 38, 2010) analysed **91 studies** and found the
principles **well supported empirically**, proposing a reformulation that
splits principles 1 and 2 into eleven. Gutiérrez, Hilborn and Defeo (*Nature*
470: 386–389, 2011) examined **130 co-managed fisheries** across countries at
different development levels, scoring each on eight outcomes: **40% scored
positively on six, seven or all eight, and a further 25% on four or five** —
which means roughly **35% scored positively on three or fewer**. Chhatre and
Agrawal (*PNAS* 106(42): 17667–17670, 2009), on original data from **80 forest
commons in 10 countries**, found that larger forest size and greater local
rule-making autonomy are associated with high carbon storage *and* high
livelihood benefits. The Rights and Resources Initiative puts the footprint at
**up to 2.5 billion people**, including some 370 million Indigenous people, who
depend on land and resources held, used or managed collectively, customarily
covering **at least 50% of the Earth's land**.

**The central disclosure — selection on the dependent variable.** The design
principles were derived from cases that *survived*. Ostrom's sample was
long-enduring CPR institutions and the principles are what those institutions
had in common, which is selection on the dependent variable in the strict
sense. Three things partly answer it and none dissolves it. Cox et al. examined
91 studies including failures; the Ostrom Workshop states the principles are
usually **absent** in failed cases, which is the right test; and Gutiérrez et
al.'s 130-fishery sample was not selected on survival. But the founding
derivation stands, the later literature largely tests the same principles on
similar case types, and Ostrom herself clarified that the principles are **not
a blueprint** and should not be applied cookie-cutter. Handled under Appendix
H.6; it bears on C5.1, C5.2 and C5.4 as Handoff 22 predicted, and on C3.3 and
C5.5 besides.

**The second disclosure — scope, which is larger here than in any previous
entry.** Session 23 flagged twenty of twenty-six criteria as contestable.
That was not twenty independent doubts. It was very largely **one** doubt,
applied twenty times: whether a mechanism that governs a resource should be
read against a criterion that asks about a population. Four of those calls
stated that question outright, and decision D18(b), taken after the first
blind replication, reports them as scope scenarios; decision D26 retired a
fifth (C3.2). Fifteen flags remain, still highly non-independent, so the
exhaustive enumeration required since Session 21 is reported *and* the joint
readings are reported alongside it. The joint readings are the informative
summary; the enumeration bounds them.

**Scale (Appendix H.6, evidentiary tier: real-world implementation at scale).**
Nepal's community forestry programme, with a statutory basis in the **Forest
Act 1993** and Forest Regulation 1995 and origins in the late 1970s, has handed
**2,237,670 hectares** to **22,266 community forest user groups** involving
about **2.9 million households** on the forest department's 2023 figures; the
Department of Forests and Soil Conservation reports 19,361 groups and 1,813,478
hectares, the Ministry of Forests and Environment's 2020 figure is over 23,000
groups and 16.6 million people across more than 2 million hectares (35% of
forested area), and CIFOR reported in December 2024 that **35% of the
population** belongs to a user group, managing 2.4 million hectares. These
figures conflict — different vintages and different counting rules — and the
range is disclosed rather than resolved; no score below rests on one of them.
Globally, roughly **one third of the world's forests** are under community-based,
participatory or decentralised management. Valencia's **Tribunal de las Aguas**
has operated for approximately a millennium and was inscribed on UNESCO's
Intangible Cultural Heritage list in 2009.

**Evidence gaps, stated up front.** The Nepal CFUG figures conflict as
described. No systematic global estimate of household income derived from
commons was retrieved; Chhatre and Agrawal's "more than half a billion users"
is a user count, not an income share. Gutiérrez et al.'s outcome scoring is on
eight fishery-specific outcomes, not on NEEC's criteria, so the ~35% weak-outcome
rate is used as a reliability indicator and not as a criterion-level
measurement. Chhatre and Agrawal's findings are contested on definitions,
variable choice and sample selection by Ternström, Mukhopadhyay and Ghate
(*PNAS* 2010), and that conflict is disclosed at C1.1 and C4.1, where the
finding does carry weight.

---

### Domain 1: Material Security

#### C1.1 Poverty Elimination Capacity: 0.5 (Partial) — flagged as contestable

*Pass threshold: 90% poverty reduction within 20 years under base scenario,
85% under stress testing.*

**The case for a contribution.** A secure commons is a non-market income floor.
Chhatre and Agrawal put forest commons alone at **more than half a billion
users**, and the Rights and Resources Initiative puts the wider figure at up to
2.5 billion people dependent on collectively held land and resources. For
subsistence users this is fuel, fodder, water, food and construction material
obtained without cash, which is the most direct anti-destitution mechanism in
rural economies. Legal recognition of collective tenure demonstrably protects
that floor: RRI records more than **100 million hectares** newly recognised
between 2015 and 2020.

**The case against a pass, which is decisive.** Chhatre and Agrawal's central
distributional finding runs the other way: **community ownership is associated
with low livelihood benefits and high carbon storage, because communities defer
use**, while government ownership carries a higher probability of overuse — low
carbon storage with high livelihood benefits. The mechanism's characteristic
success mode is conservation achieved partly by *restraining consumption*,
which is close to the opposite of a poverty-elimination mechanism. Field
evidence agrees: a 2024 study of four Nepali CFUGs (275 households) found that
a blanket approach and inadequate needs assessment limited livelihood
initiatives, particularly for women, indigenous people and landless users.
Nothing in the record approaches 90% poverty reduction, and the mechanism has
no instrument aimed at it.

**Score: 0.5.** A real, evidenced, and large floor; no elimination capacity.
**Alternative if resolved the other way: 0.0** — on the reading that a
resource-tenure regime is not a poverty mechanism at all and that the deferral
finding shows it trading livelihood flow for resource stock by design.

#### C1.2a Wealth Building for Resilience: 0.0 (Structural Failure) — flagged as contestable

*Pass threshold: $60,000 median wealth accumulation over 20 years for 70%+ of
participants.*

A commons *is* a stock, and it does accumulate — biomass, carbon, fish
abundance, aquifer level. But the member's claim on it is a **use-right, not an
asset**: non-severable, generally non-transferable, and extinguished on exit.
There is no individual balance that grows, nothing that can be borrowed
against, sold, or bequeathed outside the membership rules, and the deferral
finding at C1.1 means the flow that reaches the household is deliberately
restrained. No case in the literature reports household wealth accumulation of
the order the threshold specifies, and the mechanism contains no instrument
that would produce it.

**Score: 0.0.** This is the same call Georgism, Mutual Credit / LETS and
Universal Basic Services received on this criterion. **Alternative if resolved
the other way: 0.5** — on the reading that a collectively held corpus managed
on members' behalf is wealth-building in substance, which is the basis on which
Sovereign Wealth Fund Statism scored 0.5 here.

#### C1.2b Prevention of Exploitative Accumulation: 0.5 (Partial) — flagged as contestable

*Pass threshold: Gini < 0.35 for wealth distribution.*

**Within the resource, accumulation is structurally blocked.** Boundaries
(principle 1), appropriation limits fitted to the resource (principle 2), and
graduated sanctions (principle 5) exist precisely to stop any party from taking
more than its share. No owner can buy the commons out; that is what makes it a
commons.

**Two things stop this being a pass.** First, scope: the mechanism governs one
resource and has no purchase on economy-wide wealth distribution, which is what
the threshold measures. Second, and more seriously, **elite capture is a
standing, named finding in this literature**, not a fringe objection — recorded
across Agrawal and Gupta (2005), Blaikie (2006), Ribot et al. (2006), Sikor and
Nguyen (2007), Nelson and Agrawal (2008) and Warren and Visser (2016), and
present even in Mexico's community forestry, which is promoted as a global
success model. Thapliyal, Mukherji and Malghan (*World Development*, 2019) add
the reverse channel: economic inequality is associated with loss of commons.

**Score: 0.5. Alternative if resolved the other way: 1.0** — on the design
reading, which is the basis on which Mutual Credit / LETS scored 1.0 here.

#### C1.3 Housing Security: 0.5 (Partial)

*Pass threshold: 88% housing stability over 5-year periods, affordability at
80% AMI.*

Commons governance applied to land is the institutional form underneath
**community land trusts**, and the mapping is explicit rather than analogical:
removing land from the market gives the clear boundaries of principle 1, a
board including residents gives the collective-choice arrangements of principle
3, and local control gives the congruence of principle 2. Collective land
tenure is also the actual housing-security mechanism for a large share of the
2.5 billion, which is why the recognition gap is a housing question as well as
an environmental one. What is missing is any affordability instrument — nothing
in the mechanism targets 80% of area median income — and no five-year stability
series for commons-governed housing was retrieved.

**Score: 0.5**, matching Georgism and Universal Basic Services. **Scope
scenario, not a flag (decision D18(b)):** on the reading that community land
trusts are an application of the governance form to land rather than part of
the scored mechanism, which is the basis on which Mutual Credit / LETS and
Sovereign Wealth Fund Statism scored 0.0 here, C1.3 falls to 0.0. That
reading counts an adjacent instrument out of the mechanism's boundary, so it
is reported as a scenario below rather than carried as a contestable call.

#### C1.4 Automation Resilience: 0.5 (Partial) — flagged as contestable

*Pass threshold: poverty < 8% and aggregate demand > 85% of baseline across
30%, 50%, and 70% displacement scenarios.*

A commons share is **not conditioned on employment**. Under any displacement
scenario the fuel, fodder, water and fish keep arriving, because the entitlement
runs from membership and provision obligations rather than from a labour
contract. That is a genuine structural buffer, and it is the same logic on which
Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism and Universal
Basic Services each scored 0.5 here. It is also better evidenced than several of
those, since the non-wage income is observed rather than proposed. What is
absent is any aggregate-demand mechanism, and the deferral finding caps how much
household income the buffer delivers.

**Score: 0.5. Alternative if resolved the other way: 0.0** — on the reading
that a bounded subsistence base for a minority of the population cannot hold
poverty below 8% economy-wide under 70% displacement.

#### C1.5 Universal Wealth Access (narrowed — access breadth only): 0.0 (Structural Failure) — flagged as contestable

*Pass threshold: 80% of the population with an active wealth-accumulation
pathway.*

This is the criterion where the scale convention bites hardest, and it is a
**bound rather than a shortfall**. Principle 1 — clearly defined boundaries,
defining who may appropriate — makes exclusion **constitutive** of the
mechanism. A commons that admits everyone is not an Ostrom-style commons; it is
the open-access resource the whole design exists to prevent. Universality is
therefore precluded by the first principle, not merely unachieved. The observed
reach, up to 2.5 billion of roughly 8 billion people, is under a third, and the
mechanism supplies no route to 80%.

**Score: 0.0**, tracking C1.2a as the Step 1c retrofit requires. **Alternative
if resolved the other way: 0.5** — on the reading that principle 8's nested
enterprises could in principle tile a whole population with adjacent bounded
commons, each universal within its own boundary.

### Domain 2: Human Autonomy

#### C2.1 Freedom from Coercion: 0.5 (Partial)

*Pass threshold: 70% report genuine autonomy in major life decisions.*

Self-governance is the point of the mechanism: under principle 3 the people
bound by the operational rules are the people who write them, which is a real
autonomy gain over both state administration and private enclosure. Two things
hold it to Partial. Graduated sanctions are a coercive apparatus, consented to
but coercive, and Agrawal and Gibson (2001) make the sharper point that
apparent cooperation can be cooperation **imposed on low-power actors** through
social and economic power. And the mechanism governs one resource, not the
major life decisions the threshold asks about.

**Not flagged:** both readings land at Partial. The design reading cannot reach
a pass because the scope is one resource; the critical reading does not reach a
failure because rule-making authority genuinely sits with the users.

#### C2.2 Labor Non-Necessity: 0.0 (Structural Failure) — flagged as contestable

*Pass threshold: unconditional provision covering 100% of basic needs.*

Principle 2's proportional equivalence between benefits and costs **ties
appropriation to provision**: members earn their share by contributing to
maintenance, monitoring and repair. That is a contribution requirement written
into the design, which is the opposite of unconditional provision. Nor does any
commons cover 100% of basic needs; it covers the goods that particular resource
yields.

**Score: 0.0. Alternative if resolved the other way: 0.5** — on the reading
that a subsistence commons is unconditional *relative to the labour market*
even if conditional relative to provision obligations, which is the basis on
which Georgism, Mutual Credit / LETS and Universal Basic Services scored 0.5
here.

#### C2.3 Creative Development Opportunities: 0.5 (Partial)

*Pass threshold: 50% regular creative engagement, 10+ hours a week.*

Rule-crafting is itself sustained civic and institutional creativity, and
principle 2's requirement that rules fit local conditions makes local knowledge
constitutive rather than decorative — the literature on this point is
substantial. But nothing in the mechanism produces creative engagement at the
scale the threshold specifies, and no such measurement exists for commons
members.

**Not flagged:** this is where the excluded knowledge-commons scenario would
move the score, and it is enumerated there rather than flagged here, so that
the scope decision is tested once rather than twice.

#### C2.4 Democratic Participation: 0.5 (Partial) — flagged as contestable

*Pass threshold: 70% participation, 35% of citizen proposals adopted.*

**The strongest case any narrow mechanism in the corpus can make, and it still
falls short.** Principle 3 is very nearly a restatement of the criterion, and
the implementations are not hypothetical. Valencia's Tribunal de las Aguas seats
eight trustees, each elected by one of eight irrigation communities and each
required to farm the land himself, meeting publicly every Thursday with oral
proceedings and unappealable rulings — for approximately a thousand years, and
reportedly without ever needing recourse to the ordinary courts. Nepal's 22,000-plus
user groups write their own operational plans, and the literature routinely
describes the programme as a school of local democracy.

**What holds it to Partial is measured, not speculative.** Bina Agarwal's
**participatory exclusions** (*World Development* 29(10), 2001) is the standing
finding that formal membership does not produce effective voice, and her later
work (*Ecological Economics* 68(11), 2009; *World Development* 38(1), 2010)
shows that women's proportional strength in the governing body determines
whether they participate at all. Gutiérrez et al.'s eight outcomes include
community empowerment, and roughly 35% of their 130 fisheries scored positively
on three or fewer. Neither the 70% participation clause nor the 35%
proposal-adoption clause is demonstrated corpus-wide.

**Score: 0.5 — the closest call in Domain 2. Alternative if resolved the other
way: 1.0**, which is the level Participatory Economics, Degrowth Economics and
Nordic Social Democracy reach on this criterion.

#### C2.5 Exit Rights and Mobility: 1.0 (Pass) — flagged as contestable

*Pass threshold: exit feasible within 3 months without material penalty; the
system continues functioning at partial participation.*

Both clauses are satisfied, the second unusually strongly. Leaving a commons
means ceasing to appropriate; there is no lock-in, no notice period, and no
exit charge. And the system continues at partial participation by
construction — commons institutions are always embedded in a wider economy that
carries most of the measured activity, which is the same structural fact that
earns a pass at C5.3.

**Score: 1.0**, matching Georgism, Mutual Credit / LETS, Sovereign Wealth Fund
Statism, Universal Basic Services and Doughnut Economics. **Alternative if
resolved the other way: 0.5** — on the reading that because the share is
non-severable, a subsistence-dependent member forfeits the livelihood base on
exit, which is a material penalty in substance if not in form.

### Domain 3: System Resilience

#### C3.1 Crisis Response Capacity: 0.5 (Partial)

*Pass threshold: response within 72 hours, scaling with severity, 90%
population coverage, no legislative delay.*

The scaling clause is met in an unusually literal way. Cox's study of the Taos
Valley acequias records that in times of plenty water is apportioned in
proportion to landholding, and therefore to provision obligation, while **in
times of scarcity the rule changes so that every member has enough to survive**.
That is an automatic, severity-scaled, rule-based response requiring no
legislation and no external decision, and it is centuries old. The binding
failure is coverage: 90% of a population is unreachable for a bounded local
institution, and the mechanism provides no crisis instrument outside the
resource it governs.

**Score: 0.5. Scope scenario, not a flag (decision D18(b)):** on the reading
that the coverage clause should be read against the population the
institution governs rather than the national population, C3.1 rises to 1.0.
That reading applies the threshold to a population other than the one the
declared population rule fixes, so it is reported as a scenario below rather
than carried as a contestable call.

#### C3.2 Inflation Control Mechanisms: 0.5 (Partial)

*Pass threshold: long-term inflation ≤ 3%, stress-test ≤ 5%, automatic
adjustment.*

The mechanism has **no monetary function of any kind**: no unit of account,
no credit creation, no reserve, no price-level instrument, no fiscal
channel. The reason is simple absence rather than malfunction.

**Score: 0.5 (decision D26, Session 33).** C3.2's 0.0 band is reserved for
an active inflationary mechanism with no counterbalancing element, not for
inflation left unaddressed. Session 23 scored this entry 0.0 on absence
alone, the corpus's only 0.0 here; with 0.0 no longer open to it, it scores
0.5, the alternative the Session 23 text offered, and the call is no longer
flagged. Non-market access to fuel, fodder, water and food insulates members
from price shocks in precisely those goods, which is a real household-level
hedge even though it is not a price-level instrument, and nothing in the
evidence reaches 1.0. The blind replication (pilot 1) scored 0.5 without a
flag; its record attributes the difference to the self-contradiction in the
anchor that decision D26 resolves. No entry in the corpus now scores 0.0 on
C3.2.

#### C3.3 Multi-Failure Resistance: 0.5 (Partial) — flagged as contestable

*Pass threshold: core functions maintained across 3 of 4 compound stress
scenarios with degradation < 20%.*

**The longevity evidence is the best in the corpus by an order of magnitude.**
Valencia's water tribunal has carried its core function through conquest,
dynastic change, war and dictatorship for roughly a millennium; Törbel's alpine
commons date from the thirteenth century; Araral's *zanjera* case is four
hundred years old; Japanese irrigation institutions and *iriai* forest commons
are of comparable vintage. Compound stress is not a thought experiment for these
institutions, it is their history.

**Against that stands the failure distribution.** Roughly 35% of Gutiérrez et
al.'s 130 co-managed fisheries scored positively on three or fewer of eight
outcomes. Thapliyal et al. (2019) identify a compound stress the classic cases
did not face — rising economic inequality combined with market integration —
and find it associated with loss of commons. Berkes and others argue that this
literature systematically under-models cross-scale linkages, treating external
forces as a black box, which is exactly what a compound-stress test probes.

**Score: 0.5. Alternative if resolved the other way: 1.0** — on the weight of
the survival record.

#### C3.4 Epistemic Adaptability: 1.0 (Pass)

*Pass threshold: 30% parameter adjustability, policy updates within 6 months of
evidence, governance for changes, zero collapses during adjustment.*

Principle 3 **is** a governance procedure for changing the rules, which is the
clause most systems fail. Principle 2 requires the rules to fit local
conditions, and the acequia scarcity rule shows in-period adjustment operating
faster than any six-month window. The framework updates itself as well as its
instances: Cox, Arnold and Villamayor-Tomás reformulated Ostrom's eight
principles into eleven after examining 91 studies, and the Japanese irrigation
literature moderated principle 7 to fit a non-coercive, heavily investing state
and found principles 4 and 5 operating implicitly — the framework flexed and
still explained the outcome. Ostrom's own insistence that the principles are
not a blueprint is a statement of adjustability, not a hedge.

**Not flagged:** the only serious objection, the zero-collapse clause, is about
the survival rate of particular implementations and is scored at C3.3 and C5.1;
the requirement this criterion actually states — governance for changes — is
definitionally met.

#### C3.5 Failure-Mode Transparency: 0.5 (Partial)

*Pass threshold: failure detection within 1 week, diagnosis 80%, correction
70%, externalisation < 10% of total costs.*

Principles 4, 5 and 6 are a detection, diagnosis and correction apparatus
specified at the design level — monitors accountable to the appropriators or
drawn from them, sanctions that escalate with the offence, and conflict
resolution that is cheap and rapidly accessible. On the first three clauses
this is the best-specified failure machinery of any system in the corpus, and
it operates continuously at the scale where deviations are visible within days.

**The fourth clause is where it breaks.** Externalisation is not incidental to
the design; principle 1's boundaries make costs borne by non-members a
designed-in possibility. Stern (*International Journal of the Commons*, 2011)
states the general version: applying principles 7 and 8 to global commons is
very difficult and can be counterproductive, because lower-level units have
both the incentive and the opportunity to externalise the degradation they
cause.

**Score: 0.5. Scope scenario, not a flag (decision D18(b)):** on the
strength of the monitoring and sanctioning apparatus, reading
externalisation against the governed resource rather than against the wider
economy, C3.5 rises to 1.0. The apparatus alone does not carry the fourth
clause, so the reading turns on the frame, and it is reported as a scenario
below rather than carried as a contestable call.

### Domain 4: Ethical Integrity

#### C4.1 Intergenerational Justice: 1.0 (Pass) — flagged as contestable

*Pass threshold: 35% carbon reduction by 2030, resource use ≤ 90% of
regeneration, debt-to-GDP < 80%, positive intergenerational wealth transfer.*

This is the mechanism's flagship criterion and the one where design and
evidence agree most closely. "Long-enduring" means transmitted across
generations of appropriators, which is the property Ostrom selected on; the
institutions in the founding sample are literally defined by having passed the
resource and its rules to successors intact. Resource use at or below
regeneration is the mechanism's own success condition, and the record supports
it: Chhatre and Agrawal find community ownership associated with **high carbon
storage** because communities defer use; Nepal's forest cover rose from 39.6%
to 44.74% over the 2010–2014 survey period against a global trend of loss; and
RRI reports that unrecognised Indigenous territories in the Amazon Basin,
Mesoamerica, the DRC and Indonesia alone store carbon equivalent to roughly
**1.5 times the world's 2015 emissions**. Positive intergenerational transfer is
not a projection here but an observed multi-century fact.

**Score: 1.0. Alternative if resolved the other way: 0.5** — on the reading
that the criterion also carries a debt-to-GDP clause and an absolute-carbon
clause that the mechanism does not address at all, and that Chhatre and
Agrawal's findings are contested by Ternström et al. (2010) on definitions,
variables and sample selection.

#### C4.2 Ecological Compliance: 0.5 (Partial)

*Pass threshold: absolute carbon reductions of 35–45% by 2030, extraction ≤
regeneration, 7 of 9 planetary boundaries respected.*

The middle clause is the mechanism's definition of success and is
well-evidenced, as C4.1 sets out. The outer clauses are not reachable. Seven of
nine planetary boundaries is a **global** test, and the scale limitation here is
stated by the author of the mechanism rather than by its critics: Ostrom's 2009
World Bank paper says plainly that it is much easier to craft solutions for
smaller-scale common-pool resources than for the global commons, and her
polycentric-governance work exists precisely because the local design does not
lift to global scale unmodified. Stern's conclusion is that principle 7 must be
**rewritten** for global commons, with higher-level authorities delegating
authority and supplying knowledge rather than merely permitting self-organisation.
Against a ~35% weak-outcome rate in the fisheries record, an absolute global
carbon path is not in evidence.

**Score: 0.5. Scope scenario, not a flag (decision D18(b)):** on the reading
that extraction at or below regeneration, achieved repeatedly across
resource types and continents, is what ecological compliance means for a
resource-governance mechanism, C4.2 rises to 1.0. That reading applies the
criterion in the mechanism's own frame rather than the economy-wide one, so
it is reported as a scenario below rather than carried as a contestable
call.

#### C4.3 Racial and Gender Equity: 0.5 (Partial) — flagged as contestable

*Pass threshold: disparity reduction of 5 percentage points per 5 years,
disadvantaged groups receiving 150%+ of proportional benefits.*

**Two-sided, and both sides are well documented.** Against: Agarwal's
participatory exclusions are structural rather than incidental, and the pattern
recurs across settings — Nepal's CFUGs serve women, indigenous and landless
users least well (2024); Mexican community forest management excludes women
through tenure discrimination, the gendered division of labour, unequal benefit
distribution and a strictly commercial reading of management plans (2015); and
a Tanzanian study (2020) finds exclusion normalised in everyday discourse **even
in programmes that claim equal participation**. For: the commons is the resource
base of some 370 million Indigenous people, so recognition of collective tenure
is an equity gain accruing directly to among the most disadvantaged; India's
Joint Forest Management programme introduced **affirmative-action quotas** for
women and other marginalised groups on user-group executive committees from the
1990s, a remedy operating inside the mechanism; and Agarwal's own finding is
that women's presence improves forest protection and rule compliance, so the
remedy is not merely fair but effective.

**Score: 0.5** — a documented exclusion problem with documented, working
remedies is a Partial, not a failure and not a pass. **Alternative if resolved
the other way: 0.0** — on the reading that participatory exclusion is a
structural property of bounded, locally governed institutions and that quotas
are an external correction rather than part of the mechanism.

#### C4.4 Power Distribution: 0.5 (Partial) — flagged as contestable

*Pass threshold: wealth Gini < 0.35, 40% of citizen proposals adopted,
democratic accountability for 80% of major decisions.*

On the accountability clause the mechanism is strong and the contrast within
the corpus is sharp: appropriators write the operational rules, monitors are
drawn from or accountable to them, and disputes are settled cheaply and fast.
Session 22's entry is the direct comparison — Islamic finance's investment
account holders have no governance rights over the assets their funds are in,
and scored 0.0 here; commons members have exactly those rights over the
resource their obligations maintain.

**Two things hold it to Partial.** Elite capture, again, as at C1.2b. And the
**recognition gap**, which is a power-distribution fact pointing the wrong way:
communities customarily hold at least 50% of the world's land and governments
legally recognise their ownership of about 10–11%, so the mechanism's principle
7 — minimal recognition by external authorities — is in practice withheld for
roughly four fifths of what it covers. The wealth-Gini clause is outside the
mechanism's reach entirely.

**Score: 0.5. Alternative if resolved the other way: 0.0** — on the reading
that a mechanism whose legal existence depends on authorities that mostly
decline to recognise it cannot be said to distribute power.

#### C4.5 Exploitation Elimination: 0.5 (Partial) — flagged as contestable

*Pass threshold: extraction rates < 10% of GDP, genuine exit rights from
exploitative relationships, residual coercion < 10% of decisions.*

The mechanism removes the rentier from the resource: there is no owner to
collect a rent from appropriators, and no financial claim compounding against
them. That is a real structural achievement and it is why this criterion scores
above the 0.0 recorded for Sovereign Wealth Fund Statism, Doughnut Economics,
Status Quo Market Capitalism and Participatory Economics. But elite capture is
intra-commons extraction by another name; Agrawal and Gibson's point about
cooperation imposed on low-power actors goes directly to the residual-coercion
clause; and the exit right that C2.5 credits is, as that criterion's own flag
records, weak in substance for a subsistence-dependent member.

**Score: 0.5. Alternative if resolved the other way: 0.0** — on the reading
that removing the external rentier while leaving internal capture unaddressed
relocates extraction rather than eliminating it.

### Domain 5: Implementation Viability

#### C5.1 Proven Component Foundation: 1.0 (Pass)

*Pass threshold: 70% of components proven through 20 years of operation at a
scale of 10,000+ participants, with documented outcomes.*

**Every clause is exceeded, most of them by orders of magnitude, and this is the
strongest C5.1 case in the corpus.** Twenty years: Valencia's tribunal has run
for approximately a thousand, Törbel's commons since the thirteenth century,
Nepal's programme for over four decades with a statutory basis since 1993. Ten
thousand participants: Nepal alone involves roughly 2.9 million households.
Documented outcomes: Cox et al.'s 91 studies, Gutiérrez et al.'s 130
co-managed fisheries, Chhatre and Agrawal's 80 forest commons across 10
countries — three independent multi-case datasets with published methods.
Proportion of components proven: there is no unproven component, because the
mechanism is a description of what working institutions already do.

**Not flagged.** The selection-on-survivorship disclosure bears on what the
evidence *means*, and is scored at C3.3, C5.2 and C5.4 where it changes the
answer; it does not put the existence or the documentation of the components in
doubt.

#### C5.2 Staged Transition Pathways: 0.5 (Partial) — flagged as contestable

*Pass threshold: a detailed plan for both staged (4 phases) and rapid (36
months) deployment, with milestones, resources, and risk mitigation. Judge on
specificity.*

The instruction to judge on specificity cuts straight against this mechanism,
because **the framework explicitly declines to be a deployment plan**: Ostrom
clarified that the design principles are not a blueprint and should not be
applied cookie-cutter, and the diagnostic is addressed to analysts rather than
to implementers. What exists instead are national programmes that did deploy in
stages with statutory milestones — Nepal's Forest Act 1993 and Forest
Regulation 1995, under which handover proceeded in phases to more than 22,000
groups over decades, and India's Joint Forest Management programme, which added
representation quotas mid-course.

**Score: 0.5**, matching almost every mechanism-level entry in the corpus.
**Alternative if resolved the other way: 0.0** — on the reading that the
framework's own refusal to specify a pathway is the governing fact, and that
national forestry statutes are implementations of policy rather than of the
scored mechanism.

#### C5.3 Partial and Parallel Deployability: 1.0 (Pass)

*Pass threshold: viable at 30% participation, coexisting with traditional
markets that maintain 90% of economic activity, with a validated scaling
pathway.*

Satisfied by construction and by observation. Commons institutions exist
**inside** market economies and always have; there is no version of this
mechanism that requires the market to be displaced first. Up to 2.5 billion
people, at least 50% of the Earth's land customarily held collectively, and
roughly one third of the world's forests under community-based, participatory
or decentralised management — all coexisting with markets that carry the
overwhelming majority of measured economic activity. The scaling pathway is
principle 8 itself, nested enterprises, and it is validated rather than
proposed: Nepal scaled from nothing to more than 22,000 user groups inside four
decades.

**Not flagged.**

#### C5.4 Political Coalition Potential: 0.5 (Partial) — flagged as contestable

*Pass threshold: 60% support across the political spectrum, 65% opposition to
repeal, 80% survival probability across administration changes.*

The survival clause has better evidence behind it than any other system could
offer: Nepal's programme persisted through a decade of civil conflict and the
replacement of a monarchy by a federal republic; Valencia's tribunal survived
the Reconquista, and every regime since, with its procedure intact. The
ideological reach is unusually wide — local self-governance, collective
ownership, ecological stewardship and Indigenous rights are claims made by
different political traditions about the same mechanism — and Ostrom's 2009
Nobel moved it into mainstream development and conservation practice.

**The recognition gap is the counter-evidence, and it is direct.** If the
coalition were winning, recognition would track use; instead communities hold
at least 50% of the world's land and legally own about 10–11%. RRI records at
least **39 of 73 analysed national governments** expanding recognised community
area between 2015 and 2020 — real progress, and barely more than half the
sample. No survey evidence for the 60% cross-spectrum support or 65%
opposition-to-repeal clauses was retrieved.

**Score: 0.5. Alternative if resolved the other way: 1.0** — on the weight of
the survival record and the breadth of the ideological appeal.

#### C5.5 Cultural Adaptability: 1.0 (Pass)

*Pass threshold: viable across 3 economic contexts and 5 cultural contexts,
with a 40% parameter-flexibility range, validated across diverse
implementations.*

**The strongest C5.5 case in the corpus, and the one criterion on which this
entry scores above CCO-PTF-CIP-SZH.** The 1.0 is joint-best, shared with
Participatory Economics, Mutual Credit / LETS and Islamic finance. Validated
implementations span Swiss alpine pasture, Japanese irrigation and *iriai*
forest commons, the Spanish *huerta*, Philippine *zanjera* irrigation, the
Nepali middle hills, the Maine lobster fishery, Latin American artisanal
shellfisheries, Mexican community forestry, East African and Latin American
forests, and Indonesian *sasi* and *panglima laot* — across subsistence,
middle-income and advanced market economies. Gutiérrez et al. state the breadth
explicitly: 130 fisheries across countries at different development levels,
ecosystems, fishing sectors and resource types. Cox et al. add 91 studies and
Chhatre and Agrawal 80 commons across three continents.

Parameter flexibility is not a tolerance but a **requirement**: principle 2
obliges rules to be fitted to local conditions, so variation across
implementations is the design working rather than drifting. The Japanese case
is the clearest demonstration — the researchers had to moderate principle 7 for
a non-coercive, heavily investing state and found principles 4 and 5 operating
implicitly rather than explicitly, and the framework still accounted for the
outcome.

**Not flagged.**

---

## Summary Scores

<!-- BEGIN GENERATED: summary-table -->
| Criterion | Name | Score | Result |
|---|---|---|---|
| C1.1 | Poverty Elimination Capacity *(flagged)* | 0.5 | Partial |
| C1.2a | Wealth Building for Resilience *(flagged)* | 0.0 | Structural Failure |
| C1.2b | Prevention of Exploitative Accumulation *(flagged)* | 0.5 | Partial |
| C1.3 | Housing Security | 0.5 | Partial |
| C1.4 | Automation Resilience *(flagged)* | 0.5 | Partial |
| C1.5 | Universal Wealth Access (narrowed) *(flagged)* | 0.0 | Structural Failure |
| C2.1 | Freedom from Coercion | 0.5 | Partial |
| C2.2 | Labor Non-Necessity *(flagged)* | 0.0 | Structural Failure |
| C2.3 | Creative Development Opportunities | 0.5 | Partial |
| C2.4 | Democratic Participation *(flagged)* | 0.5 | Partial |
| C2.5 | Exit Rights and Mobility *(flagged)* | 1.0 | Pass |
| C3.1 | Crisis Response Capacity | 0.5 | Partial |
| C3.2 | Inflation Control Mechanisms | 0.5 | Partial |
| C3.3 | Multi-Failure Resistance *(flagged)* | 0.5 | Partial |
| C3.4 | Epistemic Adaptability | 1.0 | Pass |
| C3.5 | Failure-Mode Transparency | 0.5 | Partial |
| C4.1 | Intergenerational Justice *(flagged)* | 1.0 | Pass |
| C4.2 | Ecological Compliance | 0.5 | Partial |
| C4.3 | Racial and Gender Equity *(flagged)* | 0.5 | Partial |
| C4.4 | Power Distribution *(flagged)* | 0.5 | Partial |
| C4.5 | Exploitation Elimination *(flagged)* | 0.5 | Partial |
| C5.1 | Proven Component Foundation | 1.0 | Pass |
| C5.2 | Staged Transition Pathways *(flagged)* | 0.5 | Partial |
| C5.3 | Partial and Parallel Deployability | 1.0 | Pass |
| C5.4 | Political Coalition Potential *(flagged)* | 0.5 | Partial |
| C5.5 | Cultural Adaptability | 1.0 | Pass |

| Domain | Score | Max |
|---|---|---|
| Material Security | 2.0 | 6.0 |
| Human Autonomy | 2.5 | 5.0 |
| System Resilience | 3.0 | 5.0 |
| Ethical Integrity | 3.0 | 5.0 |
| Implementation Viability | 4.0 | 5.0 |
| **Total** | **14.5** | **26.0** |

**Total: 14.5/26 (56%). Structural failures: 3 (C1.2a, C1.5, C2.2). Tier: Partially Adequate.**
<!-- END GENERATED: summary-table -->

### The flagged calls, and what they do to the tier

**Fifteen of twenty-six criteria are flagged** — the second-largest flagged
set in the corpus, after Islamic finance's sixteen. Session 23 flagged
twenty. Decision D18(b), taken after the first blind replication, reports
four of them as scope scenarios, because their alternative readings are
scope questions (C1.3, C3.1, C3.5 and C4.2; see "The scope scenarios"
below), and decision D26 retired a fifth, C3.2, whose alternative is now its
score. Seven flags would raise the score if resolved the other way and eight
would lower it. The eleven unflagged criteria are **C1.3, C2.1, C2.3, C3.1,
C3.2, C3.4, C3.5, C4.2, C5.1, C5.3 and C5.5**.

Resolving each flag independently gives **32,768 combinations**, spanning
**10.5 to 18.0 out of 26** and **0 to 9 structural failures**, and reaching
**all three adequacy tiers**: 9.0% of combinations land in Potentially
Adequate, 65.6% in Partially Adequate, and 25.4% in Structurally Inadequate.
**No structural failure is undisputed** — every one of C1.2a, C1.5 and C2.2
has a stated alternative that removes it, which is weaker than Islamic
finance, where two of five failures were undisputed by any flag.

**By the D13 measure (protocol 6.4), this entry is the least tier-robust in
the corpus**: its joint readings reach all three tiers, spanning 7.5 points
and 9 structural failures, against 5.0 points and 9 failures for Islamic
finance, the second least tier-robust, and no failure is undisputed where
Islamic finance has two. By the secondary statistic, the enumeration's share
of combinations that keep the scored tier (assuming independent calls), the
order of the two reverses: 65.6% of this entry's 32,768 combinations keep
the Partially Adequate tier, against 17.1% of Islamic finance's 65,536.

### The joint readings

The flags are strongly non-independent — most of them turn on the single
scope question set out in the Overview — so the exhaustive enumeration
overstates the real uncertainty by treating fifteen correlated judgments as
fifteen coin flips; the joint readings, not the enumeration, are the
informative summary. Session 23 reported three coherent readings: A, the
long-enduring case, and C, strict population scope, either side of the
scored reading. Both were named for the scope question itself, so with the
scope questions reported as scenarios (decision D18(b)) the entry takes the
two extremes of its register, decision D16's default.

| Reading | Total | % | Failures | Tier |
|---|---|---|---|---|
| Every call resolved upward (seven flags) | 18.0/26 | 69 | 0 | Potentially Adequate |
| As scored | 14.5/26 | 56 | 3 | Partially Adequate |
| Every call resolved downward (eight flags) | 10.5/26 | 40 | 9 | Structurally Inadequate |

The **upward reading produces zero structural failures**, a count that, as
scored, only CCO-PTF-CIP-SZH reaches in the entire corpus. The **spread of
7.5 points and 9 failures, crossing all three tiers**, is what remains of
the selection-and-scope problem once the scope questions are reported
separately; Session 23's spread was 10.0 points and 11 failures. That spread
was the strongest evidence yet produced by this project that the framework
needs an explicit **scope-normalisation rule** — a stated convention for how
a mechanism-scope entry is read against population-scope criteria. This
evaluation adopts one and states it; decision D8 makes such a rule part of
the scoring protocol (see "Scope-normalisation rule" below), and decision
D18(b) separates a scope question from a doubt by a stated test
(`NEEC_OstromCommons_replication_record.md`, section 10.1).

### The scope scenarios

Session 23 flagged four calls whose alternative readings are scope questions
rather than doubts about the evidence: each reads a threshold against a
population, domain or frame other than the one the declared population rule
fixes, or counts an adjacent instrument in or out of the mechanism's
boundary. Decision D18(b), taken after the first blind replication
(`NEEC_OstromCommons_replication_record.md`, section 10.1), reports them as
scenarios, beside the knowledge-commons scenario Session 23 already carried.
None is scored.

| Scenario | Changes | Total | Failures | Tier |
|---|---|---|---|---|
| Knowledge and digital commons counted in | C1.5 0.0 → 0.5; C2.3 0.5 → 1.0 | 15.5/26 | 2 | Potentially Adequate |
| Community land trusts counted out | C1.3 0.5 → 0.0 | 14.0/26 | 4 | Partially Adequate |
| Thresholds read against the governed resource and its members | C3.1, C3.5, C4.2 0.5 → 1.0 | 16.0/26 | 3 | Partially Adequate |

Counting the **knowledge and digital commons** in rather than treating it as
adjacent changes two criteria: **C1.5 rises from 0.0 to 0.5**, because a
non-rival commons can be open to everyone and so escapes principle 1's
boundedness, and **C2.3 rises from 0.5 to 1.0**, because Wikipedia and
open-source software are creative engagement at exactly the scale the
threshold describes. The result is **15.5/26 with 2 structural failures —
Potentially Adequate**: tier-neutral when Session 23 scored it, the scenario
crosses a tier boundary now that C3.2 is no longer a failure (decision D26).
It is *not* scored, for the reason given in the Overview: the Governing
Knowledge Commons workshop's own position is that the design principles do
not transfer straightforwardly to knowledge resources. A future reviewer who
disagrees should change C1.5 and C2.3 and nothing else.

Counting **community land trusts** out of the mechanism, the reading set out
at C1.3, lowers C1.3 to 0.0; the blind replication carried the same boundary
question as a scenario. Reading the coverage, externalisation and compliance
clauses **against the governed resource and its members** rather than the
economy-wide population raises C3.1, C3.5 and C4.2 to 1.0, as set out in
those sections. Neither moves the tier.

### Archetype — a decision made in the evaluation, as D7 required

Commons governance joins **archetype 1, narrow single-mechanism systems**, as
its fifth member after Georgism, Mutual Credit / LETS, Sovereign Wealth Fund
Statism and Islamic finance. But it does not sit comfortably alongside them on
the existing sub-distinction, and two refinements are proposed rather than
forced:

1. **A second axis within archetype 1: intermediation versus direct
   governance.** The four existing members all *intermediate value* — they tax
   a rent, clear a balance, invest a corpus, or finance a venture. Commons
   governance **governs a resource directly**; it is a property-and-decision
   regime, not a value-intermediation mechanism. This is why its Domain 3
   profile is unlike the others': it has no monetary channel at all (C3.2,
   where absence now scores 0.5 under decision D26) while having the
   best-specified failure-detection apparatus (C3.5).
2. **A third position on Session 17's stock/flow sub-distinction.** SWF Statism
   is a **state-held** stock; Islamic finance a **household-held** stock;
   Georgism and Mutual Credit / LETS are flows with no accumulating store.
   Commons governance is the first **collectively held, non-severable** stock —
   a corpus that accumulates but on which no member has an individual,
   transferable claim. That single structural fact drives C1.2a, C1.5 and C2.5,
   and it is the cleanest explanation of why the entry scores low on material
   security while scoring high on intergenerational justice.

---

## Where this sits in the corpus

<!-- BEGIN GENERATED: corpus-table -->
| Rank | System | Score /26 | % | Failures | Tier |
|---|---|---|---|---|---|
| 1 | CCO-PTF-CIP-SZH | 24.5 | 94 | 0 | Potentially Adequate |
| 2 | Participatory Economics | 20.5 | 79 | 1 | Potentially Adequate |
| 3= | Integral | 19.5 | 75 | 3 | Partially Adequate |
| 3= | Nordic Social Democracy | 19.5 | 75 | 2 | Potentially Adequate |
| 5 | Degrowth Economics | 19.0 | 73 | 2 | Potentially Adequate |
| 6 | Market Socialism | 16.5 | 63 | 2 | Potentially Adequate |
| 7 | MMT + Job Guarantee | 15.5 | 60 | 3 | Partially Adequate |
| 8= | Mutual Credit / LETS | 14.5 | 56 | 3 | Partially Adequate |
| 8= | **Ostrom-Style Commons Governance** | 14.5 | 56 | 3 | Partially Adequate |
| 8= | Universal Basic Income | 14.5 | 56 | 7 | Structurally Inadequate |
| 11= | Sovereign Wealth Fund Statism | 14.0 | 54 | 3 | Partially Adequate |
| 11= | State Capitalism / Singapore | 14.0 | 54 | 4 | Partially Adequate |
| 13= | Georgism / Land Value Tax | 13.5 | 52 | 2 | Potentially Adequate |
| 13= | Islamic Finance / Profit-Sharing Banking | 13.5 | 52 | 5 | Partially Adequate |
| 13= | Universal Basic Services | 13.5 | 52 | 3 | Partially Adequate |
| 16 | Fully Automated Luxury Communism | 13.0 | 50 | 10 | Structurally Inadequate |
| 17 | Doughnut Economics | 11.5 | 44 | 8 | Structurally Inadequate |
| 18 | Status Quo Market Capitalism | 10.5 | 40 | 9 | Structurally Inadequate |
| 19= | Centrally Planned Socialism | 10.0 | 38 | 12 | Structurally Inadequate |
| 19= | Stakeholder Capitalism | 10.0 | 38 | 9 | Structurally Inadequate |
| 19= | State Capitalism / China | 10.0 | 38 | 8 | Structurally Inadequate |
| 22 | State Capitalism / Qatar | 9.0 | 35 | 10 | Structurally Inadequate |
| 23 | Libertarian Minarchism | 8.0 | 31 | 15 | Structurally Inadequate |
<!-- END GENERATED: corpus-table -->

All comparative claims below are stated on the canonical 23-system corpus
and checked by `verify_comparative_claims.py`, not transcribed.

**A three-way exact tie at 14.5/26.** Ostrom-style commons governance,
Mutual Credit / LETS and Universal Basic Income all score exactly 14.5/26
(56%), with 3, 3 and 7 structural failures respectively. Like the three-way
tie at 13.5 (Georgism / Land Value Tax, Universal Basic Services and Islamic
finance), it spans two adequacy tiers, so it illustrates the
tier-versus-percentage distinction once more: the same total from two narrow
mechanisms that clear the Partially Adequate bar and from an income-transfer
design that does not. Against Mutual Credit / LETS specifically, this entry
**differs on 4 of 26 criteria, is higher on 2 and lower on 2, and nets
exactly zero**. Until decision D26 it tied Sovereign Wealth Fund Statism and
State Capitalism / Singapore at 14.0.

**Not dominated by anything, CCO-PTF-CIP-SZH included.** The corpus contains
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
Step 1b entry that dominates one of the 13 legacy systems.

**Joint-best cultural adaptability; joint third-best implementation
viability.** Domain 5 scores **4.0/5**, beaten only by CCO-PTF-CIP-SZH and
Islamic finance (4.5 each) and tied with Mutual Credit / LETS, Nordic Social
Democracy and Status Quo Market Capitalism. Domain 1 scores **2.0/6**, beaten
by 14 of the other 22 systems. The resulting **viability-minus-material-security
split of 2.0** is joint third-widest in the corpus, behind Libertarian
Minarchism's 3.0 and Islamic finance's 2.5, level with Doughnut Economics,
Mutual Credit / LETS, Status Quo Market Capitalism and Universal Basic
Services.

**Against the system it is layered onto.** Compared with Status Quo Market
Capitalism it differs on **15 criteria, is higher on 11 and lower on 4, and
gains 4.0 points** — a real improvement, concentrated in ethical integrity
and resilience rather than material security, and the four criteria where it
does worse are the ones where a market economy's monetary and macroeconomic
machinery has no counterpart in a commons.

**Against a nearest neighbour.** Georgism / Land Value Tax is one of the
three systems closest to this entry, each differing from it on only **4
criteria** (the others are Mutual Credit / LETS and Universal Basic
Services). Against Georgism it is higher on 3 and lower on 1, and gains 1.0
— a close pairing of two mechanisms that both govern access to a natural
resource, one by taxing its rent and one by governing its use directly.

---

## Final assessment

**Ostrom-style commons governance scores 14.5/26 (56%) with 3 structural
failures — Partially Adequate.** Domain scores are 2.0 / 2.5 / 3.0 / 3.0 /
4.0. It passes six criteria (C2.5, C3.4, C4.1, C5.1, C5.3, C5.5), records
seventeen Partials, and fails C1.2a, C1.5 and C2.2.

The shape of the result is consistent and explicable. This is a mechanism
for **governing a resource sustainably and accountably across generations**,
and it is extremely good at that: the best-proven components in the corpus,
the widest validated cultural range, the best-specified failure-detection
apparatus, and a survival record measured in centuries. It is not a
mechanism for **provisioning a population**, and the three failures are all
of that kind — no individual accumulating claim, no universal access by
design, no unconditional provision. It has no monetary function either, but
under C3.2's anchor absence is not a structural failure (decision D26). The
one finding that captures both halves is Chhatre and Agrawal's: community
ownership is associated with high carbon storage and **low livelihood
benefits**, because communities defer use. The mechanism succeeds by
restraint, and restraint is not a material-security strategy.

Two qualifications belong in any use of this entry. First, the tier is **not
robust**: by the D13 measure this is the least tier-robust entry in the
corpus, with all three tiers reachable on its joint readings and no
undisputed failure, and a reader who resolves its calls together, upward or
downward, will get a materially different answer, as will one who counts the
knowledge commons in. Second, the reason is **structural rather than
evidentiary** — it is not that the evidence is thin, which it emphatically
is not, but that NEEC has no stated rule for reading a mechanism-scope
system against population-scope criteria, so the scoring convention has to
be supplied by the scorer.

**Scope-normalisation rule (decision D8, adopted for the reproducibility kit,
D3).** Every entry declares its scope (mechanism, configured national economy,
or comprehensive system), and the protocol states how population-scope
thresholds are applied in each case. This entry adopts the generalisation
convention and says so, but a convention chosen by the scorer is exactly what a
replication protocol is supposed to remove. Ostrom-style commons governance is
the entry that makes the omission unmissable, and it is the rule's worked
example.

**Evidence that will date.** Nepal's CFUG figures are moving and already
inconsistent across official sources; RRI's recognition figures cover 2015–2020
and a newer edition will supersede them; the fisheries co-management record has
grown considerably since Gutiérrez et al.'s 2011 cut. A v2.x review should
re-check C1.1, C4.1 and C5.4 against a refreshed RRI edition and any post-2011
systematic review of co-management outcomes.

---

## Reviewer disclosure (per `NEEC_CONTRIBUTING.md` §2 / Appendix H.6)

- **Scored by:** Claude (Anthropic), Session 23, 2026-09-17. **Replicated
  blind once** (pilot 1, 2026-09-19, Claude Sonnet 5): 22 of 26 criteria
  exact, all 26 within one step, the same tier; the four differences are
  attributed in `NEEC_OstromCommons_replication_record.md`.
- **Inserted** into `neec_scores.csv` and the canonical scoring scripts in
  Session 25, with State Capitalism / Qatar and Islamic finance; the corpus
  table above is the canonical 23-system corpus.
- **Revised** in Session 33, after that replication: decision D18(b)
  re-expressed the register (four scope questions reported as scenarios) and
  decision D26 revised C3.2 from 0.0 to 0.5. Both are applied in place by
  `restate_s33.py`; the Session 32 text is kept as
  `NEEC_Ostrom_Commons_scoring_scratch_s32_snapshot.md`.
- **Scope decisions** are stated in the Overview and were confirmed by the
  project owner before research began (D7). Three further decisions were made
  during the work and are disclosed inline: the knowledge/digital commons
  exclusion, the collectively-held non-severable stock classification, and the
  generalisation convention for scale.
- **Contestable calls:** fifteen, listed above with their alternatives; seven
  upward and eight downward. All three tiers are reachable. **The tier is not
  robust in either direction.**
- **Evidence conflicts disclosed:** Nepal CFUG counts across official sources;
  Chhatre and Agrawal versus Ternström et al. (2010) on definitions, variables
  and sample selection.
- **Sources** span the founding literature (Ostrom 1990, 2009, 2010),
  peer-reviewed multi-case empirical work (Cox et al. 2010; Gutiérrez, Hilborn
  and Defeo 2011; Chhatre and Agrawal 2009; Agarwal 2001, 2009, 2010),
  institutional and official reporting (Rights and Resources Initiative; Nepal
  Department of Forests and Soil Conservation; Ministry of Forests and
  Environment; UNESCO), and deliberately sought critical work from more than
  one direction (Agrawal and Gibson 1999, 2001; Saunders 2014; the elite-capture
  literature; Stern 2011; Shin et al. 2022; Ternström et al. 2010). Full
  records in `session23_research_notes.md`.

---

## Summary block

The machine-readable summary of this entry (protocol section 9; schema
`neec-summary-block/1.0`, `summary_block_schema.json`). It is generated from
the canonical corpus and the Session 28 staging (`summary_blocks_s28.json`),
re-expressed by `restate_s33.py` under decisions D18(b) and D26, not typed,
and validated by `neec_entry.py`.

<!-- NEEC-SUMMARY-BLOCK -->
```json
{
  "schema": "neec-summary-block/1.0",
  "key": "Ostrom-Style Commons Governance",
  "code": "OS",
  "display_name": "Ostrom-Style Commons Governance",
  "record": {"documents": ["NEEC_Ostrom_Commons_scoring_scratch.md"], "scored": "Session 23, natively on the v2 structure", "structure": "native-v2"},
  "scope": {"class": "mechanism", "basis": "stated", "population": "The convention applied throughout is generalisation, not best-casing: the mechanism is scored as though every common-pool resource in an economy were governed by an Ostrom-principled institution, and the population-scope thresholds are then applied to the resulting economy-wide", "source": {"file": "NEEC_Ostrom_Commons_scoring_scratch.md", "locator": "document", "phrase": "Commons governance joins archetype 1, narrow single-mechanism systems, as its fifth member after Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism and Islamic finance."}},
  "vector": {
    "C1.1": 0.5, "C1.2a": 0.0, "C1.2b": 0.5, "C1.3": 0.5, "C1.4": 0.5, "C1.5": 0.0,
    "C2.1": 0.5, "C2.2": 0.0, "C2.3": 0.5, "C2.4": 0.5, "C2.5": 1.0,
    "C3.1": 0.5, "C3.2": 0.5, "C3.3": 0.5, "C3.4": 1.0, "C3.5": 0.5,
    "C4.1": 1.0, "C4.2": 0.5, "C4.3": 0.5, "C4.4": 0.5, "C4.5": 0.5,
    "C5.1": 1.0, "C5.2": 0.5, "C5.3": 1.0, "C5.4": 0.5, "C5.5": 1.0
  },
  "summary": {"D1": 2.0, "D2": 2.5, "D3": 3.0, "D4": 3.0, "D5": 4.0, "total": 14.5, "failures": 3, "tier": "Partially Adequate"},
  "flags": [
    {"criterion": "C1.1", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C1.2a", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C1.2b", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C1.4", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C1.5", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C2.2", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C2.4", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C2.5", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C3.3", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C4.1", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C4.3", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C4.4", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C4.5", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C5.2", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}},
    {"criterion": "C5.4", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_ostrom.py", "locator": "FLAGS"}}
  ],
  "joint_readings": [
    {"id": "scored", "label": "as scored", "basis": "scored", "resolve": {}, "result": {"total": 14.5, "failures": 3, "tier": "Partially Adequate"}},
    {"id": "up", "label": "every call resolved upward", "basis": "extremes", "resolve": {"C1.2a": 0.5, "C1.2b": 1.0, "C1.5": 0.5, "C2.2": 0.5, "C2.4": 1.0, "C3.3": 1.0, "C5.4": 1.0}, "result": {"total": 18.0, "failures": 0, "tier": "Potentially Adequate"}},
    {"id": "down", "label": "every call resolved downward", "basis": "extremes", "resolve": {"C1.1": 0.0, "C1.4": 0.0, "C2.5": 0.5, "C4.1": 0.5, "C4.3": 0.0, "C4.4": 0.0, "C4.5": 0.0, "C5.2": 0.0}, "result": {"total": 10.5, "failures": 9, "tier": "Structurally Inadequate"}}
  ],
  "scenarios": [
    {"id": "knowledge-commons", "label": "the knowledge and digital commons counted in", "kind": "scope", "changes": {"C1.5": 0.5, "C2.3": 1.0}, "result": {"total": 15.5, "failures": 2, "tier": "Potentially Adequate"}},
    {"id": "land-trusts-out", "kind": "scope", "label": "community land trusts counted out of the mechanism's boundary", "changes": {"C1.3": 0.0}, "result": {"total": 14.0, "failures": 4, "tier": "Partially Adequate"}},
    {"id": "resource-frame", "kind": "scope", "label": "thresholds read against the governed resource and its members, not the economy-wide population", "changes": {"C3.1": 1.0, "C3.5": 1.0, "C4.2": 1.0}, "result": {"total": 16.0, "failures": 3, "tier": "Partially Adequate"}}
  ]
}
```
<!-- /NEEC-SUMMARY-BLOCK -->
