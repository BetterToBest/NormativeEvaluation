# NEEC Evaluation: State Capitalism / Singapore (GLC Developmental Capitalism)

**Scoring document — Step 1b; scored in Session 19 (2026-09-16), natively on
the v2 structure; in the canonical corpus (`neec_scores.csv`) since Session
20.** Follows Appendix H.9's submission template. Scored directly against
the fully specified 26-criterion v2 structure (Section 12.3, Appendix
H.7v2), as the five earlier Step 1b systems and State Capitalism / China
were. This is the second of the three state-capitalism sub-entries specified
in Paper Section 8.1 (v1.2 decision). Its row was added to `neec_scores.csv`
in Session 20; it is not yet a Part I entry of the Report (the Step 5
revision adds it). It has not been independently cross-checked by a second
scorer (H.9 Step 6) — flagged as open, per this project's disclosure norms
(`NEEC_CONTRIBUTING.md` §2, Appendix H.6). The arithmetic, transcription and
sensitivity claims below were checked by `verify_singapore.py`, against the
17-system corpus it was written for (its output is captured in
`verify_singapore_output.txt`, and the harness re-runs it on this document
as it stood before decision D18(a)); since D18(a), the flag register, joint
readings and scenario are checked from this document's summary block by
`neec_entry.py`, and every comparative claim is checked on the canonical
corpus by `verify_comparative_claims.py` (protocol 8.2).

As in Session 18, the work spanned two chat turns: research in the first,
and verification and write-up in the second, after the user said "Continue."

---

## 20 [pending renumbering]. State Capitalism / Singapore

### Overview

**What is scored.** Paper Section 8.1 defines this sub-entry as
government-linked-company (GLC) developmental capitalism: state-linked
holding companies (Temasek, GIC) operating on commercial logic within a
dominant-party but electorally contested political system. This evaluation
scores the Republic of Singapore's political economy as configured at the
evaluation date (September 2026), informed by its record since independence
in 1965. Where the historical record differs materially from the current
configuration, both are described. China's scope logic (Handoff 18) is
reused.

**The system's shape.** Four institutions carry most of the load:

- **State holding companies.** Temasek was incorporated in 1974 with an
  initial portfolio of S$354 million in 35 companies (National Library
  Board). It is wholly owned by the Minister for Finance, as is GIC, which
  manages the government's reserves (Temasek FAQ). Both are Fifth Schedule
  entities under the Constitution: a draw on Temasek's past reserves needs
  the President's approval, and so do appointments to and removals from its
  board (Temasek FAQ). Temasek's annual report says its portfolio companies
  are run by their own boards and management, without direction from Temasek
  (US State Department, citing Temasek).
- **Public housing on state land.** HDB flats are 99-year leases on land
  owned by the Singapore Land Authority (Propkaki). They house 77.2% of
  resident households (SingStat, via Global Property Guide), and 91.2% of
  resident households owned their home in 2025 (Trading Economics).
- **Mandatory individual savings.** The Central Provident Fund (CPF) holds
  individual accounts earmarked for housing, healthcare, and retirement.
- **A large non-resident workforce.** Of 6.11 million people in June 2025,
  4.20 million were residents (3.66 million citizens and 0.54 million
  permanent residents) and 1.91 million were non-residents (Population in
  Brief 2025). The Ministry of Manpower (MOM) counted 1,222,700 Work Permit
  holders in December 2025, including 316,900 migrant domestic workers —
  about a fifth of the total population.

**Scope boundaries, and why.**

- **Population scope — a decision flagged for the user's confirmation.** The
  criteria refer to "population" and "participants." This evaluation counts
  everyone who lives and works inside the system, non-residents included,
  because the low-wage Work Permit workforce is a designed, load-bearing
  feature of the model (C1.4, C4.5), not an incidental population. This
  parallels China's treatment of hukou migrants. A citizen-and-PR-only
  reading changes two scores (C1.5 and C4.5); its consequence is checked in
  Summary Scores.
- **China and the Gulf sovereign-wealth-fund states remain separate
  sub-entries.** Sovereign Wealth Fund Statism excluded Singapore's funds by
  design; its Norway/Alaska evaluation is used here only as a comparator.
- **The 1959–1965 self-government and merger period** is used only as
  history (C5.2).

**A contested label, used here as taxonomy only.** Singapore's government is
generally opposed to the term "GLC" and prefers "state-owned enterprise,"
stressing that these firms operate on an equal basis with local and foreign
businesses (US State Department, Investment Climate Statement).
Peer-reviewed studies find that Singapore's GLCs were no less profitable
than matched private firms over 1964–1998 (Feng, Sun & Tong, *Journal of
Banking & Finance*, 2004) and that Temasek-linked firms carried higher
valuations and better governance than a control group (*Journal of
Multinational Financial Management*). Critics on the left describe a labour
regime built on migrant workers and a state-aligned union movement (C4.5);
civil-liberties critics focus on political constraints (C2.1, C2.4). Section
8.1's "state capitalism" is used as this corpus's taxonomic term, not as an
endorsement of any framing.

**The normative-commitment disclosure.** As with China, several scores below
(C2.1, C2.4, C4.4) follow partly from NEEC's stated commitments to freedom
from coercion, democratic participation, and diffused power (Paper Section
2.2). Readers who reject those commitments should contest them at the level
of the criteria, through Appendix I. An analysis in *The Diplomat* (2026)
argues that global press-freedom rankings miss the political and cultural
logic behind Singapore's approach to journalism; this evaluation notes that
view and takes the framework as specified.

**Evidentiary tier (Appendix H.6): real-world implementation.** Official
statistics are extensive, and unlike China's, no official series was found
to have been suppressed. The gaps lie in what is not measured or published:
there is no official poverty line (C1.1), and consolidated figures for
state-owned enterprises, and any list of them, are not published (US State
Department). Where evidence is secondary or absent, the text says so.

**Where this system sits relative to the corpus.** Like China, it is a whole
existing national political economy rather than a reform proposal or a
single mechanism. See Final Assessment for an archetype proposal.

---

### Domain 1: Material Security

#### C1.1 Poverty Elimination Capacity: 0.5 (Partial) — flagged as contestable

**Rationale:** Appendix C.1 prescribes the basic-needs-basket method for
high-income countries — a locally costed budget for housing, food,
healthcare, utilities, transport, and other essentials — rather than a World
Bank dollar line. Singapore has no official poverty line. It applies
scheme-specific income thresholds and generally aims assistance at roughly
the poorest fifth of households (Chow and Lin; NUS Social Service Research
Centre). Absolute poverty persists only in small pockets and is not a
prevailing concern (Peng, 2025, University of Malaya working paper).

The closest local counterpart to C.1's basket is the Minimum Income Standard
(MIS) research led by Ng Kok Hoe (Lee Kuan Yew School of Public Policy) with
Teo You Yenn and colleagues. Their 2023 update put monthly budgets for 2022
at about S$1,492 for a single person aged 65 or older, S$3,369 for a single
parent with a young child, and S$6,693 for partnered parents with two
school-age children. Measured against those budgets:

- The median work income of cleaners, labourers, and related workers reached
  52% of the relevant MIS budget in 2022, up from 48% in 2020 (LKYSPP,
  Global-is-Asian).
- ComCare Long-Term Assistance paid about 43% of the single-elderly budget
  and reached 0.6% of older people, down from 0.9% in 2020. The Silver
  Support Scheme covered 10–20% of the budget (MIS 2023 report).
- ComCare Short-to-Medium-Term Assistance reached 20,825 families in 2024,
  9% fewer than in 2023, with a median payout of S$380 per beneficiary for a
  median of six months; Long-Term Assistance reached 3,240 families (MSF
  trends report, via Malay Mail). In 2023 the two schemes together reached
  about 1.86% of resident households (Peng, 2025).

The Ministries of Finance, Manpower, and Social and Family Development have
said the MIS research relies on simplifying assumptions that risk
overstating needs (as summarized in an SUTD student paper, 2024). A claim
that about 30% of working households fall below the MIS budgets circulates
online; it was not traced to a primary report, and this score does not rely
on it.

The wider transfer system is substantial. Resident households received about
S$7,300 per household member in government transfers in 2025, and households
in 1- and 2-room HDB flats about S$16,519 (Financial Horse, summarizing
SingStat). Transfers and taxes lowered the market-income Gini from 0.452 to
0.379 (Mothership, reporting SingStat and MOF). Non-residents, including
1.22 million Work Permit holders, sit outside the resident income
statistics, and core schemes are restricted to citizens and PRs (the
Jobseeker Support scheme, for example; e2i).

No documented poverty-reduction rate exists to compare with the 90% Pass
Threshold, so this score rests on reasoned estimation (H.6). The continuous
estimate is about 0.4–0.6: extreme deprivation is close to absent among
residents, but a sizeable low-wage segment remains well below the locally
costed basket, the last-resort scheme is narrow, and the lowest-paid fifth
of the population is outside the measured system altogether.

**Score Justification:** Partial (0.5). **Flagged as contestable:** measured
against an extreme-poverty line — the reading behind China's own flagged
alternative and the CPS precedent's 1.0 — the result would be near-complete
elimination. This evaluation follows Appendix C.1's high-income rule, just
as China's entry followed its middle-income rule. Consequence, checked:
14.5/26, failure count and tier unchanged.

#### C1.2a Wealth Building for Resilience: 1.0 (Pass) — flagged as contestable

**Rationale:** Singapore has the strongest individually held accumulation
mechanism in the Step 1b cohort: owner-occupied public housing combined with
mandatory CPF savings. The resident home-ownership rate was 91.2% in 2025
(Trading Economics). HDB resale prices rose about 51% over the past decade
and 177% over twenty years (Smart Wealth, summarizing HDB data). UBS's
*Global Wealth Report 2026* put median wealth per adult at US$96,434 at
end-2025, 20th in the world (*The Straits Times*; The Independent
Singapore). That clears the $60,000 Pass Threshold by a wide margin.

Four qualifications make this a flagged Pass rather than a clean one:

- **Lease decay.** An HDB flat returns to the state at the end of its lease
  with no compensation (Propkaki; Home & Decor). In the second quarter of
  2026, flats with under 60 years remaining sold for about 25.8% less per
  square foot than flats with 90 or more years left (Propkaki). CPF use is
  pro-rated when the remaining lease does not cover the youngest buyer to
  age 95 (Winfred Quek), and in 2018 the then National Development Minister
  reminded residents that the redevelopment scheme would reach only a few
  estates (Home & Decor). Over the criterion's 20-year horizon most owners
  still gain; over a full lease, the asset declines to zero.
- **Liquidity.** CPF balances are earmarked for housing, healthcare, and
  retirement rather than serving as a general-purpose shock buffer (stated
  from the scheme's design; not separately sourced in this session).
- **Concentration in one asset.** The HDB resale price index fell 0.10%
  quarter-on-quarter in Q1 2026, its first quarterly decline since Q2 2019
  (Global Property Guide) — small, but a reminder that the buffer sits
  mostly in one asset class.
- **Breadth.** Residents are about 69% of the population (4.20 of 6.11
  million). Work Permit holders, about 20%, cannot own HDB flats, which are
  restricted to citizens and eligible PRs (Global Property Guide), and have
  no pathway to long-term residency (HOME, 2025). Counting higher-paid
  Employment Pass and S Pass holders as having private pathways, this
  evaluation estimates that roughly 75% of the population has a genuine
  mechanism — near the threshold's 70% bar (reasoning, not a citable
  figure).

**Score Justification:** Pass (1.0) — a genuine, documented, individually
held mechanism reaching most participants, with median wealth far above the
threshold. This follows the Market Socialism and Nordic anchors. It differs
from China's 0.5, which rested on a falling asset, restricted rural land
rights, and hukou gates. **Flagged as contestable:** a reader weighting
lease decay, illiquidity, and the exclusion of a fifth of the population
would score 0.5. Consequence, checked: 13.5/26, failure count and tier
unchanged.

#### C1.2b Prevention of Exploitative Accumulation: 0.5 (Partial)

**Rationale:** The Ministry of Finance estimates Singapore's wealth Gini at
0.55 — above its income inequality, but below the 0.6–0.7 range it cites for
the United Kingdom, Japan, and Germany (MOF Occasional Paper, 2026, as
reported by Mothership). That places Singapore below the "social democracy:
0.65–0.75" band Section 12.3 uses. Two structural features limit particular
concentration channels: residential land is state-owned and leased rather
than sold (C1.2a), and foreign buyers pay a 60% Additional Buyer's Stamp
Duty on any home (Global Property Guide).

The top of the distribution is pulling away. UBS's mean wealth per adult
(US$527,217, sixth in the world) is about 5.5 times the median, compared
with 3.4 times in Hong Kong and 6.5 in the United States (Investing Iguana,
summarizing UBS). UBS counts roughly 244,000 US-dollar millionaires in
Singapore (Financial Horse). A 2021 opinion column citing Credit Suisse
reported that the top 1% held about a third of the nation's wealth (Malay
Mail). That figure is older and secondary, and it sits in tension with MOF's
Gini estimate; both are disclosed.

**Score Justification:** Partial (0.5) — real limits in the land channel and
an official wealth Gini below the social-democratic band, but no mechanism
holding concentration under 0.35 and a widening gap at the top. This matches
Nordic Social Democracy's and China's 0.5.

#### C1.3 Housing Security: 1.0 (Pass)

**Rationale:** Public housing on state land is the system's signature
achievement. HDB flats house 77.2% of resident households, and 91.2% of
resident households own their home (C1.2a). Rough sleeping is rare. The
Ministry of Social and Family Development (MSF) counted 496 rough sleepers
on one night in July 2025, 6.4% fewer than in 2022 (MSF) — roughly 0.01% of
the population. Independent counts that also included shelter residents
found about 1,000 homeless people in both 2019 and 2021 (Ng Kok Hoe,
LKYSPP). Disagreements with family or co-tenants were the most common reason
given for sleeping rough, cited by half of those surveyed (MSF).

Affordability pressure is real and disclosed. A median-priced resale HDB
flat in 2025 required a monthly household income of roughly S$5,872–11,876,
depending on flat type (Dollars and Sense), and 1,594 HDB flats resold for
S$1 million or more in 2025 (Smart Wealth). The government said in 2024 that
resale flats remained affordable for the vast majority of buyers (Malay
Mail). Some groups sit outside the core mechanism: young single people are
often ineligible for subsidised housing (Malay Mail, 2025), and Work Permit
holders live in employer-arranged accommodation, including dormitories whose
occupancy MOM described as high in 2023 (MOM parliamentary reply).

**Score Justification:** Pass (1.0) — strong structural provision and
regulation, with a documented stability rate far above the threshold for the
resident population, and no evidence located of material housing instability
among non-residents while employed. This matches the CPS and Nordic anchors.
Not flagged: the affordability and eligibility limits bear mainly on who
enters the system and at what price, not on stability once housed, and the
stability evidence is unusually strong.

#### C1.4 Automation Resilience: 0.5 (Partial)

**Rationale:** Singapore has built a real but limited displacement buffer:

- **Jobseeker Support.** Launched in April 2025 for citizens, with PRs
  following in early 2026, it pays up to S$6,000 over six months, starting
  at S$1,500 and tapering, capped at previous income, and conditional on
  job-search activity (MOM; WSG; e2i). MOM expects about 60,000 residents a
  year to qualify, over 60% of the involuntarily unemployed. A consultancy
  guide describes it as a shift after decades in which the government
  resisted unemployment benefits over work-incentive concerns (Mavenside,
  2026).
- **Training.** About 606,000 people took part in state-supported
  SkillsFuture training in 2025 (Vertical Institute, citing SWDA).
- **Fiscal capacity for emergencies.** Reserve draws funded large wage
  subsidies in 2020 (C3.1).
- **A foreign-workforce margin.** The Work Permit workforce grew about 44%
  between December 2020 (848,200) and December 2025 (1,222,700) (MOM). With
  so much low-wage employment on renewable permits, a fall in labour demand
  can be absorbed partly by not renewing permits. That is a buffer for
  residents that is itself an exclusion, not a decoupling of income from
  work (reasoning, not a citable finding).

The IMF lists labour-market disruption among the downside risks of AI
adoption (2025 Article IV). Unemployment was 2.0% in 2025 (IMF, 2026). No
evidence was located that these tools would hold poverty under 8% at NEEC's
50–70% displacement severities; the main payment ends after six months.

**Score Justification:** Partial (0.5) — a new, conditional, time-limited
buffer plus training and fiscal capacity, without decoupling income from
employment. This matches Nordic's and China's 0.5.

#### C1.5 Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial)

**Rationale:** Among residents, access is close to universal: CPF membership
and HDB eligibility reach nearly every citizen and PR household, and 91.2%
of resident households own their home. Access is gated by pass type,
however. HDB ownership is restricted to citizens and eligible PRs,
foreigners pay 60% stamp duty on any home (Global Property Guide), and Work
Permit holders — about a fifth of the population — have no pathway to
long-term residency (HOME). Migrant-worker advocates report that first-time
construction workers commonly pay S$13,000–16,000 in recruitment fees (HOME
and TWC2, as reported by The Online Citizen, 2026), which makes early
asset-building unlikely. This is the gated-access pattern of H.7v2's Market
Socialism anchor.

**Score Justification:** Partial (0.5) under this evaluation's population
scope. **The population-scope decision is a scenario, not a flag** (protocol
3.4, decision D18(a)): scoring citizens and permanent residents only would
score 1.0 here on the Nordic anchor and raise C4.5 to 0.5, giving 15.0/26
with 3 failures (Partially Adequate). Summary Scores reports this scenario
beside the joint readings.

**Domain 1 = 0.5 + 1.0 + 0.5 + 1.0 + 0.5 + 0.5 = 4.0/6 (67%)**

---

### Domain 2: Human Autonomy

#### C2.1 Freedom from Coercion: 0.5 (Partial) — flagged as contestable

**Rationale:** Three kinds of pressure operate, none with the severity
documented for China.

- **Economic compulsion.** Survival rests mainly on employment. General
  unemployment support began only in 2025 (C1.4), and last-resort assistance
  is narrow (C1.1).
- **Political and legal constraint.** Freedom House rates Singapore Partly
  Free, at 48/100 (political rights 19/40, civil liberties 29/60), in
  *Freedom in the World 2025*. It gives 1 point out of 4 each to freedom of
  assembly, freedom for NGOs, freedom for trade unions, independent media,
  and judicial independence. It reports continued use of the
  online-falsehoods law (POFMA) against targets including an opposition
  party leader and an anti-death-penalty group, and nine executions in 2024,
  all but one for drug trafficking. Reporters Without Borders (RSF) ranked
  Singapore 123rd of 180 in 2026, with its legal-environment indicator at
  164th (The Online Citizen).
- **Labour.** Strikes in essential services such as transport require 14
  days' notice. After an illegal two-day strike by bus drivers from mainland
  China at SMRT in 2012, about 29 strikers were deported and four were
  jailed for around six weeks (Wikipedia, citing contemporary reports).
  Migrant-worker advocates describe a large power imbalance that arises
  because workers depend on employers for their permits, often carry
  recruitment debt, and fear deportation (HOME and TWC2). MOM received 120
  reports of Training Employment Pass abuse in 2025 (Business & Human Rights
  Resource Centre). During COVID-19, dormitory residents accounted for 82.4%
  of cases as of August 2021 and were subject to apps tracking their
  movements (Columbia University WEAI, summarizing Kathiravelu).

Against this, Freedom House scores personal autonomy relatively well — 3 of
4 each for freedom of movement, property and business rights, personal
social freedoms, and equality of opportunity. No evidence was located of
state-organized coerced labour of the kind UN experts documented for China.

**Score Justification:** Partial (0.5) — economic compulsion with a harsher
political overlay than the Status Quo anchor, but not the substitution of a
comparably severe form of coercion that H.7's 0.0 anchor describes.
**Flagged as contestable:** a reader treating the employer-tied,
debt-financed permit regime for a fifth of the population, together with the
constraints on assembly, unions, and speech, as coercion of comparable
severity would score 0.0. Consequence, checked: 13.5/26 with 5 failures,
tier unchanged on its own (see Summary Scores for the joint case).

#### C2.2 Labor Non-Necessity: 0.0 (Structural Failure)

**Rationale:** Support is deliberately tied to work or job search. Jobseeker
Support requires job-search activity and ends when a job is found (MOM).
ComCare short-term help lasts a median of six months, and about 49% of
households that left it in 2021 returned within three years (MSF, via Malay
Mail). The Workfare Income Supplement pays only those in work, and the
Silver Support Scheme targets seniors with low lifetime incomes (MOF, via
Mothership). In 2012 the then head of the national union federation, later
Manpower Minister, said a minimum wage was not something Singapore embraced
(People's World).

Jobseeker Support is a real time-limited, conditional benefit — the language
of H.7's 0.5 band. It does not move this score, for consistency: Status Quo
Market Capitalism scored 0.0 despite US unemployment insurance, and
Singapore's scheme (at most S$6,000 over six months, capped at prior income)
is not more generous. Nordic's 0.5 rests on generous, comprehensive
conditional provision.

**Score Justification:** Structural failure (0.0) — no baseline independent
of labour-market participation, by design. This matches the Status Quo and
MMT + Job Guarantee anchors, and China's 0.0.

#### C2.3 Creative Development Opportunities: 0.5 (Partial)

**Rationale:** This evaluation retrieved no Singapore-specific data on
creative engagement or working hours, so the score rests on reasoned
estimation (H.6). Two constraints are documented indirectly: Freedom House
scores both media independence and academic freedom at 1 of 4, and advocates
describe very long working days for some migrant workers (C2.1). Nothing
located suggests structural suppression of creative activity of the kind
H.7's 0.0 anchor (CPS) describes; cultural life operates under content
regulation rather than a state monopoly on production.

**Score Justification:** Partial (0.5) — engagement exists but is
constrained, the Status Quo pattern. Not flagged, but this is the least
evidenced score in this evaluation.

#### C2.4 Democratic Participation: 0.5 (Partial) — flagged as contestable

**Rationale:** Elections are competitive and matter at the margin. In May
2025 the People's Action Party (PAP), in power since 1959, won 87 of 97
seats and 65.57% of the vote, up from 61.2% in 2020 (The Asia Group; CNBC).
The Workers' Party kept its 10 seats and gained two non-constituency seats
(LKYSPP, Global-is-Asian). The opposition first won a multi-member group
constituency in 2011 (Al Jazeera). Consultation is real: the Jobseeker
Support scheme drew on public feedback from the Forward Singapore exercise
and on a union–employer taskforce (MOM; HR Asia).

The playing field is uneven. Freedom House scores the fairness of the
electoral framework and its administration at 1 of 4, and the election of
the head of government at 1 of 4, and says the framework the PAP built
constrains the growth of opposition parties. The editor of an independent
Singaporean outlet argues that POFMA and the foreign-interference law give
partisan politicians too much discretion (Jom, 2024).

**Score Justification:** Partial (0.5) — real multiparty elections and
consultation, with citizens' influence diluted by an incumbent-designed
electoral and legal framework. This fits the Status Quo band (formal rights,
diluted influence), although the source of dilution differs. It is not
China's 0.0: a lawful, if steep, path to opposition gains exists. **Flagged
as contestable:** a reader treating 67 years without a change of governing
party, and the framework Freedom House describes, as foreclosing meaningful
participation would score 0.0. Consequence, checked: 13.5/26 with 5
failures, tier unchanged on its own.

#### C2.5 Exit Rights and Mobility: 0.5 (Partial)

**Rationale:** Formal exit is available. Freedom House scores freedom of
movement 3 of 4, and 221,600 citizens were living overseas in 2025
(Population in Brief, via Malay Mail). But the system imposes differential
treatment by status. Work Permit holders depend on employers for their right
to remain and have no pathway to residency (HOME); HDB ownership and
Jobseeker Support are limited to citizens and PRs (Global Property Guide;
e2i); and permanent residents pay 5% stamp duty on a first home where
citizens pay none (Global Property Guide). Because CPF accounts are
individual, the system's funding does not depend on near-universal
participation in the way H.7's Nordic 0.0 anchor describes (reasoning, not a
citable finding).

**Score Justification:** Partial (0.5) — formal exit alongside
system-imposed differential treatment, which fails the threshold's
no-differential-treatment clause. This matches China's and Status Quo's 0.5.
Two institutional features often discussed under this heading —
national-service obligations and ethnic quotas in public housing — were not
researched in this pass and are not relied on.

**Domain 2 = 0.5 + 0.0 + 0.5 + 0.5 + 0.5 = 2.0/5 (40%)**

---

### Domain 3: System Resilience

#### C3.1 Crisis Response Capacity: 0.5 (Partial)

**Rationale:** The 2020 response was exceptionally fast and large. Three
budget packages arrived within about two months, together close to S$60
billion, or about 12% of GDP (KPMG), and four budgets committed close to
S$100 billion in all (Lexology). The Jobs Support Scheme raised its wage
subsidy for local workers from 25% to 75% (KPMG), and wage-support payouts
reached S$600 million by the end of March and S$5.6 billion by May (Dollars
and Sense). The President approved draws on past reserves of up to S$52
billion for 2020; actual draws over FY2020–2022 came to S$42.9 billion
(Yahoo Finance; Malay Mail). The first-ever draw, in 2009 (S$4.9 billion
approved, S$4.0 billion used), was put back in 2011 (Yahoo Finance). The IMF
credited a coordinated and sizable response; GDP contracted 5.4% in 2020 and
unemployment peaked at 3.5% (IMF, 2021).

The response was not automatic. Each package required a budget in Parliament
and, for reserve draws, presidential assent, and wage support covered local
workers.

**Score Justification:** Partial (0.5) — among the fastest and largest
discretionary responses in the corpus, but not the automatic,
legislation-free trigger the Pass Threshold describes (Nordic's automatic
stabilizers). This matches China's and Sovereign Wealth Fund Statism's 0.5.

#### C3.2 Inflation Control Mechanisms: 1.0 (Pass) — flagged as contestable

**Rationale:** Monetary policy works through a named and distinctive
mechanism: a policy band for the Singapore dollar's trade-weighted exchange
rate (the S$NEER). The Monetary Authority of Singapore (MAS) tightened five
times in a row between October 2021 and October 2022 (UOB, via FXStreet;
MAS), tightened again in April 2026 (ING), and saw core inflation average
0.7% in 2025 (MAS, January 2026). In 2022, core inflation averaged 4.1% and
headline inflation 6.1% (BIS Papers No. 142). Inflation expectations remain
anchored (IMF, 2026).

**Score Justification:** Pass (1.0) — a specific, named mechanism, long-run
inflation within the threshold, and core inflation below the 5% stress bar
during the 2022 global shock. This follows Status Quo's and China's 1.0.
**Flagged as contestable:** read on headline inflation, 2022's 6.1% exceeded
the 5% stress bar, and a reader applying the threshold that way would score
0.5. Consequence, checked: 13.5/26, failure count and tier unchanged.

#### C3.3 Multi-Failure Resistance: 0.5 (Partial)

**Rationale:** Singapore came through the one recent compound shock —
pandemic, supply disruption, and recession together — with a 5.4%
contraction in 2020 (IMF, 2021) and a recovery that outpaced its peers (IMF,
2025). Degradation stayed well inside the threshold's 20%. The IMF describes
ample buffers and strong banks, with non-performing loans at 1.1% (IMF,
2026).

Exposure is structural, though. The IMF lists geoeconomic fragmentation (a
threat to Singapore's role as a global financial centre), a possible
correction in AI-related investment, climate change, and population ageing
among its risks (IMF 2025, 2026). The resident fertility rate is 0.97
(Population in Brief 2025). The pandemic also exposed a concentrated failure
point in the labour-housing model: dormitory residents made up 82.4% of
cases by August 2021 (C2.1).

**Score Justification:** Partial (0.5) — large buffers and a good record in
one compound shock, but a single observed episode cannot establish the
threshold's three-of-four-scenarios test, and the economy's openness
transmits shocks. This matches the Market Socialism band and China's 0.5.

#### C3.4 Epistemic Adaptability: 1.0 (Pass) — flagged as contestable

**Rationale:** The record shows repeated, deliberate recalibration without
destabilization:

- A 1985 privatization strategy and a 1987 divestment committee reviewed 91
  first-tier GLCs and recommended listing, privatizing, or winding up many
  of them (*Asian Survey*, 2024).
- Climate targets moved from an emissions-intensity pledge (2015) to a peak
  target (2020) to absolute levels for 2030 and 2035 (EDB; NCCS).
- A carbon tax began in 2019 and is rising (C4.2).
- Non-binding anti-discrimination guidelines became law in 2025 (C4.3).
- Unemployment support, long resisted, arrived in 2025 after public
  consultation (C1.4).
- The reserves framework was used in two crises, and the 2009 draw was
  repaid (C3.1).

Two weak points are disclosed. Changes are governed democratically, but
under a dominant-party supermajority (C2.4). And some evidence-based
proposals have been slow or refused: an official poverty line, despite calls
in Parliament (The Independent Singapore, reporting Workers' Party MP Jamus
Lim); a national minimum wage (C2.2); and, for decades, unemployment
support.

**Score Justification:** Pass (1.0) — demonstrated capacity for
evidence-based parameter change without collapse, matching the Market
Socialism anchor and Sovereign Wealth Fund Statism's 1.0. It differs from
China's 0.5, which rested on centralization and the abrupt exit from
zero-COVID. **Flagged as contestable:** a reader weighting slow
social-protection reform and dominant-party control of change would apply
the Status Quo band (0.5). Consequence, checked: 13.5/26, failure count and
tier unchanged.

#### C3.5 Failure-Mode Transparency: 0.5 (Partial) — flagged as contestable; explicit contrast with China

**Rationale — what is visible.** Official data are extensive and regularly
published, including household income and transfers (SingStat), population
and foreign-workforce counts (NPTD; MOM), and rough-sleeper counts and
assistance trends (MSF). Temasek is not legally required to disclose
financial information but has published an annual review since 2004 (Temasek
FAQ). Corruption at the top is prosecuted: former Transport Minister S.
Iswaran was sentenced to a year in prison in 2024 (Freedom House). Pandemic
case data, including the dormitory outbreak, were public (C2.1).

**Rationale — what is obscured.**

- **Unmeasured failure.** There is no official poverty line (C1.1). An
  opposition MP has asked how success against poverty can be judged without
  one (The Independent Singapore).
- **Unconsolidated state-enterprise data.** Consolidated figures for
  state-owned enterprises are not public, and no list of them is published
  (US State Department).
- **Constrained criticism.** POFMA orders have been issued against critics
  (C2.1), and RSF ranks Singapore's legal environment for journalism 164th
  of 180.
- **A contested corruption outcome.** In January 2023 the Corrupt Practices
  Investigation Bureau (CPIB) gave stern warnings, in lieu of prosecution,
  to six former senior managers of Keppel Offshore & Marine over about US$55
  million in bribes linked to Petrobras contracts. It cited evidentiary
  difficulties: documents held abroad and key witnesses who could not be
  compelled to testify in Singapore (CPIB). The company had paid US$422
  million under an international settlement (Malay Mail). The government
  defended the decision in Parliament (Prime Minister's Office); critics
  asked how it squared with Singapore's zero-tolerance policy (The Online
  Citizen).
- **Externalized costs.** Emissions (C4.2), and recruitment debts that
  migrant workers incur before arriving (C4.5).

**Why this contrasts with China.** China's 0.0 rested on documented
concealment of its signature failure modes — epidemic onset, disaster tolls,
suspended statistical series. No comparable pattern was located for
Singapore; its gaps lie mainly in what goes unmeasured or undisclosed, and
in constraints on critics. Freedom House scores government openness and
transparency at 2 of 4.

**Score Justification:** Partial (0.5) — many failures are surfaced and
corrected, while poverty, consolidated state-enterprise data, and some
criticism are not. This matches the Market Socialism and Sovereign Wealth
Fund Statism band. **Flagged as contestable:** a reader treating POFMA, the
absence of any poverty measure, and non-public enterprise data as active
suppression would apply the Stakeholder Capitalism anchor (0.0).
Consequence, checked: 13.5/26 with 5 failures, tier unchanged on its own.

**Domain 3 = 0.5 + 1.0 + 0.5 + 1.0 + 0.5 = 3.5/5 (70%)**

---

### Domain 4: Ethical Integrity

#### C4.1 Intergenerational Justice: 0.5 (Partial)

**Rationale:** The positive transfer is structural. The Constitution
protects past reserves, including those held by Temasek and GIC, behind a
presidential veto (Temasek FAQ; National Library Board). Past reserves have
been drawn on in only two crises, and the 2009 draw was repaid (C3.1).

The negative transfers are also real. Under current policies, emissions rise
to 56–57 MtCO2e in 2030, and the 2030 target of 60 MtCO2e is 30% above 2010
levels (Climate Action Tracker). The resident fertility rate is 0.97, there
are 2.4 working-age citizens for every senior (Population in Brief 2025),
and the IMF expects ageing to strain fiscal resources (2025). Lease decay
(C1.2a) also transfers housing value back to the state over time. This
evaluation did not retrieve a current gross-debt figure and does not assess
the threshold's debt clause.

**Score Justification:** Partial (0.5) — this is H.7's Nordic anchor almost
exactly: sovereign funds as positive transfer, with emissions above
sustainable levels. Not flagged. Sovereign Wealth Fund Statism's 1.0 does
not carry over, because that entry scored the fund mechanism on its own,
whereas this entry scores a whole economy, emissions included, as Nordic's
did.

#### C4.2 Ecological Compliance: 0.0 (Structural Failure) — flagged as contestable

**Rationale:** H.7 requires absolute-reduction standards. On that basis:

- **The 2030 path rises.** Climate Action Tracker (CAT) rates the target
  "Highly insufficient" against modelled domestic pathways: emissions at the
  60 MtCO2e target would be 30% above 2010 and rising rather than falling.
- **Relative targets came first.** The 2015 pledge was a 36% cut in
  emissions intensity from 2005 levels by 2030, and a 2020 update set a peak
  of 65 MtCO2e around 2030 (EDB). The 2009 pledge was measured against
  business as usual and was exceeded (NCCS).
- **The carbon price is too low for the task.** The tax rose from S$5 to
  S$25 per tonne in 2024 and is scheduled to reach S$45 in 2026–27 and
  S$50–80 by 2030 (Rajah & Tann); CAT still judges it far below
  1.5°C-compatible prices.

The counter-evidence is why this call is flagged. The 2035 contribution sets
an absolute range of 45–50 MtCO2e, with the lower bound on a linear path to
net zero by 2050 (NCCS). Singapore does not subsidize fossil fuels (Rajah &
Tann). It plans at least 2 GW of solar by 2030, about 6 GW of
clean-electricity imports by 2035, and an end to unabated coal power by 2040
(Enerdata). The government describes Singapore as alternative-energy
disadvantaged (NCCS).

**Score Justification:** Structural failure (0.0) — a growth-oriented
economy whose 2030 target allows emissions above 2010 levels, with no path
to the 35–45% absolute cut the Pass Threshold requires. This matches
China's, Sovereign Wealth Fund Statism's, and Status Quo's 0.0. **Flagged as
contestable:** a reader weighting carbon pricing, absolute post-2030
targets, and geographic constraints would apply the Nordic anchor (0.5).
Consequence, checked: 14.5/26 with 3 failures, tier unchanged on its own.

#### C4.3 Racial and Gender Equity: 0.5 (Partial) — flagged as contestable

**Rationale — ethnicity.** Citizens are 75.5% Chinese, 15.1% Malay, 7.6%
Indian, and 1.8% other (Population in Brief 2025, via Malay Mail). In the
2020 census, median monthly household income from work per household member
was S$1,594 for Malays, against S$2,603 for Chinese and S$2,521 for Indians.
Malay incomes grew fastest over the decade, but the gap remains large
(Karyawan, a Malay-Muslim community publication, citing census data).
Transfers are strongly progressive by income and housing type (C1.1). That
reaches Malay households disproportionately, but it is not designed as
reparative. Freedom House scores equal treatment of population segments 2 of
4.

**Rationale — gender and nationality.** The Workplace Fairness Act, passed
in January 2025 and completed by a dispute-resolution law in November 2025,
is Singapore's first anti-discrimination statute. It covers characteristics
including sex, pregnancy, caregiving responsibilities, race, religion, and
nationality, and applies first to employers with at least 25 staff (WTW;
MOM; Jones Day). The women's rights group AWARE welcomed it but called it a
missed opportunity to address the gender pay gap (AWARE, 2025). Nationality
also structures the two-tier labour regime (C4.5).

**Score Justification:** Partial (0.5) — genuine, newly legislated
anti-discrimination effort and class-based redistribution that benefits a
disadvantaged group indirectly, but no mechanism of disproportionate
reparative benefit and large persisting ethnic disparities. This fits H.7's
0.5 anchor (formal equality without reparative mechanisms). **Flagged as
contestable:** read literally, H.7's 0.0 anchor — formally neutral policy
amid large documented disparities — also fits. (That anchor's cited example,
Status Quo, is published at 0.5, an inconsistency already logged in Handoff
18.) Consequence, checked: 13.5/26 with 5 failures, tier unchanged on its
own.

#### C4.4 Power Distribution: 0.0 (Structural Failure) — flagged as contestable

**Rationale — political power.** One party has governed since 1959, and
Freedom House describes domination of the political system by the PAP and
the Lee family. The PAP holds 87 of 97 seats (C2.4). The national union
federation is closely tied to the ruling party; Prime Minister Lee Hsien
Loong called the relationship symbiotic in 2017 (People's World). Formal
accountability exists: party leadership changed hands in 2004 and 2024, and
a former minister was jailed (C3.5).

**Rationale — economic power.** Household wealth is broadly held (C1.2a),
but productive capital is concentrated in holding companies wholly owned by
the Minister for Finance (Temasek FAQ), which hold large stakes across major
firms. Ho Ching, the wife of then Prime Minister Lee Hsien Loong, was
Temasek's chief executive in the 2000s (NBC News/AP, 2009). The top of the
private wealth distribution is also pulling away (C1.2b).

Against the threshold: the wealth Gini is well above 0.35; no evidence was
located on the share of citizen proposals adopted; democratic accountability
for major decisions is partial; and removal of the governing party, though
formally possible, has never happened.

**Score Justification:** Structural failure (0.0). The continuous estimate
(about 0.15–0.35) straddles the rounding boundary and is disclosed as such,
per H.3. Neither form of power is structurally diffused: political power
sits with a long-dominant party, and commanding-heights capital sits with
state holding companies under that party's control. **Flagged as
contestable:** a reader treating broad household ownership plus competitive
elections as partial diffusion would apply the 0.5 band. Consequence,
checked: 14.5/26 with 3 failures, tier unchanged on its own.

#### C4.5 Exploitation Elimination: 0.0 (Structural Failure)

**Rationale:** Extraction is structural, chiefly through a large low-wage
workforce with little bargaining power:

- **Scale.** There were 1.22 million Work Permit holders in December 2025,
  including 482,600 in the construction, marine, and process sectors and
  316,900 domestic workers (MOM).
- **Debt and dependence.** First-time construction workers commonly pay
  S$13,000–16,000 in recruitment fees (HOME and TWC2), and domestic workers
  face salary deductions to repay agency fees, sometimes with fewer rest
  days in that period (HOME, 2026). Workers brought in on training passes
  have been assigned low-skilled jobs with long hours (TWC2, via the
  Business & Human Rights Resource Centre).
- **No independent counterweight.** Collective representation runs through a
  union federation closely tied to the ruling party (C4.4), and strikes are
  rare and legally constrained (C2.1).
- **Low pay at the bottom, for residents too.** The median work income of
  cleaners and labourers covered about half of a basic household budget in
  2022 (C1.1).

Counterweights exist: sectoral progressive wage schemes, which economists
credit with narrowing inequality (Malay Mail, 2022); an expanded dormitory
law, acknowledged by HOME and TWC2; and nationality among the protected
characteristics in the Workplace Fairness Act (C4.3).

**Score Justification:** Structural failure (0.0) — extraction is
load-bearing through a debt-financed, employer-tied non-resident workforce
without independent collective bargaining. This matches the Status Quo,
China, and Sovereign Wealth Fund Statism anchors; Nordic's 0.5 rests on the
independent collective bargaining that is absent here. Not flagged as a
call, but it is the one failure that the population-scope decision moves:
under a citizen-and-PR-only scope this score would rise to 0.5 (see Summary
Scores).

**Domain 4 = 0.5 + 0.0 + 0.5 + 0.0 + 0.0 = 1.0/5 (20%)**

---

### Domain 5: Implementation Viability

#### C5.1 Proven Component Foundation: 1.0 (Pass)

**Rationale:** The system has operated since independence in 1965 — 61 years
— for a population now above six million, with extensively documented
outcomes (Domains 1 and 3). Its components have also been transplanted.
China's Housing Provident Fund was modelled on Singapore's CPF (*Land Use
Policy*, 2020), piloted in Shanghai in 1991 and extended nationwide in 1995
(*International Real Estate Review*; *Habitat International*, 2004). The
China–Singapore Suzhou Industrial Park adapted more than 110 regulations and
standards between 1994 and 2019 and had sent about 3,800 officials to
Singapore for training by 2019 (Liu et al., *Public Administration and
Development*, 2021).

**Score Justification:** Pass (1.0) — a long, well-documented track record
at national scale, plus documented transfer. As with Status Quo and China,
this certifies track record, not adequacy, which Domains 1–4 assess.

#### C5.2 Staged Transition Pathways: 0.5 (Partial)

**Rationale:** Parts of the model have documented, sequenced histories:
Temasek's 1974 incorporation from existing state holdings (National Library
Board), the 1985–1987 privatization programme (*Asian Survey*), and a
structured transfer of administrative know-how to Suzhou (C5.1). Three
limits keep this below a Pass:

- **The political precondition did not arise through ordinary competition.**
  In February 1963, Operation Coldstore detained more than 100 left-wing
  politicians, trade unionists, and activists without trial (accounts range
  from 113 to about 130), severely weakening the leadership of the Barisan
  Sosialis, the PAP's main rival (Wikipedia; Mothership; RSIS). The official
  account presents it as a security operation against a communist front.
  Revisionist historians argue that it was politically motivated, and a 2015
  RSIS commentary defends the mainstream account against that view (RSIS;
  *Armstrong Undergraduate Journal of History*, 2026).
- **City-state scale.** The pathway unfolded in a small, urban jurisdiction
  without a rural hinterland (reasoning).
- **No NEEC-formatted dual plan** — staged and rapid, with milestones —
  exists.

**Score Justification:** Partial (0.5) — documented sequences and a
demonstrated transfer method, but no pathway from the pluralist starting
point most prospective adopters would occupy. This matches China's and
Sovereign Wealth Fund Statism's 0.5.

#### C5.3 Partial and Parallel Deployability: 1.0 (Pass)

**Rationale:** The model coexists with private and foreign firms by design.
The government states that its enterprises operate on an equal basis with
local and foreign businesses (US State Department), and Temasek describes
its portfolio companies as run by their own boards (US State Department,
citing Temasek; see Overview). Most resident households live in HDB flats,
but a private property market operates alongside. The state's share can be
dialled down, as the 1980s divestments showed (*Asian Survey*). Components
have been adopted abroad piecemeal (C5.1), although they have worked less
well outside the full configuration: China's Housing Provident Fund has not
matched the CPF–HDB system's effects (Beihang University policy-transfer
study), and the Temasek model's influence on Chinese state asset management
was limited (*Asian Survey*, 2024).

**Score Justification:** Pass (1.0) — designed to coexist with markets and
demonstrably adoptable in parts, matching Sovereign Wealth Fund Statism and
Status Quo. It differs from China's 0.5, which rested on the comprehensive
form's need for near-total political control; Singapore's economic
institutions do not require that. The weaker transplant results bear on C5.5
rather than here.

#### C5.4 Political Coalition Potential: 0.5 (Partial) — flagged as contestable

**Rationale:** Domestic support is strong and repeatedly tested at the
ballot box. The PAP's vote share was 60.1% in 2011 (its lowest since
independence), 69.9% in 2015, 61.24% in 2020, and 65.57% in 2025 (Malay
Mail; The Asia Group). Trust in government stood at 77% in 2024 and rose
during the pandemic (Civil Service College, citing Edelman).

Three caveats apply:

- **High trust does not discriminate between regime types.** In Edelman's
  2024 ranking, Singapore's 77% placed fourth, behind Saudi Arabia, China,
  and the United Arab Emirates (Gulf News).
- **Support is uneven and cooling.** Low-income earners' average trust in
  institutions runs 18 points below that of higher earners (Civil Service
  College), and the share of Singaporeans expecting the next generation to
  be better off fell from 42% to 31% between 2025 and 2026 (Edelman, as
  reported).
- **Two parts of the threshold cannot be tested.** Survival across a change
  of governing party has never been observed, and support is measured under
  an electoral framework Freedom House rates as partly unfair (C2.4). In
  pluralist democracies, the model's political constraints would repel
  liberal and left constituencies (C2.1).

**Score Justification:** Partial (0.5) — strong, durable domestic majorities
and real international emulation (C5.1), set against untested survival under
alternation and cross-spectrum resistance to the political model. This is a
stronger case than China's but lands in the same band. **Flagged as
contestable:** a reader treating six decades of 60%-plus vote shares in
contested elections as meeting the Nordic anchor would score 1.0.
Consequence, checked: 14.5/26, failure count and tier unchanged.

#### C5.5 Cultural Adaptability: 0.5 (Partial)

**Rationale:** The model operates across three major ethnic communities
(C4.3) and has been partly transferred to a very different setting, China,
with mixed results. The Suzhou park adapted and diffused Singapore's rules
(C5.1), and a Harvard Kennedy School teaching case on the project is titled
"Same Bed, Different Dreams," signalling the partners' divergent aims. The
Housing Provident Fund underperformed its model (C5.3). No low-income
replication was located, and the city-state configuration may not generalize
(reasoning).

**Score Justification:** Partial (0.5) — real, partial transfer across
contexts, concentrated in East Asia. This matches China's and CPS's 0.5.

**Domain 5 = 1.0 + 0.5 + 1.0 + 0.5 + 0.5 = 3.5/5 (70%)**

---

## Summary Scores

**Domain Totals:**

- Material Security: 4.0/6 (67%)
- Human Autonomy: 2.0/5 (40%)
- System Resilience: 3.5/5 (70%)
- Ethical Integrity: 1.0/5 (20%)
- Implementation Viability: 3.5/5 (70%)

**Overall Score: 14.0/26 (54%)**

*Explicit sum, per Appendix H.4: 4.0 + 2.0 + 3.5 + 1.0 + 3.5 = 14.0.*

*Score distribution: 6 criteria at 1.0 (C1.2a, C1.3, C3.2, C3.4, C5.1,
C5.3), 16 at 0.5, and 4 at 0.0. Check: 6(1.0) + 16(0.5) + 4(0.0) = 6 + 8 + 0
= 14.0, matching the domain sum exactly.*

**Structural Failures:** 4 criteria at 0.0 — C2.2, C4.2, C4.4, C4.5.

**Adequacy:** Partially Adequate (3 to 5 structural failures; Section 8.3,
Appendix H.5).

**Sensitivity of every flagged call** (each resolved alone; all figures
checked by `verify_singapore.py`):

| Criterion | Primary | Alternative reading | Total | Failures | Tier |
|---|---|---|---|---|---|
| C1.1 | 0.5 | 1.0 — extreme line / CPS precedent | 14.5 | 4 | Partially Adequate |
| C1.2a | 1.0 | 0.5 — lease decay, illiquidity, excluded fifth | 13.5 | 4 | Partially Adequate |
| C2.1 | 0.5 | 0.0 — permit regime plus political constraints | 13.5 | 5 | Partially Adequate |
| C2.4 | 0.5 | 0.0 — no alternation since 1959 | 13.5 | 5 | Partially Adequate |
| C3.2 | 1.0 | 0.5 — headline inflation of 6.1% in 2022 | 13.5 | 4 | Partially Adequate |
| C3.4 | 1.0 | 0.5 — slow social-protection reform | 13.5 | 4 | Partially Adequate |
| C3.5 | 0.5 | 0.0 — POFMA and unmeasured poverty as suppression | 13.5 | 5 | Partially Adequate |
| C4.2 | 0.0 | 0.5 — carbon price / Nordic analogy | 14.5 | 3 | Partially Adequate |
| C4.3 | 0.5 | 0.0 — literal reading of the 0.0 anchor | 13.5 | 5 | Partially Adequate |
| C4.4 | 0.0 | 0.5 — broad ownership plus elections | 14.5 | 3 | Partially Adequate |
| C5.4 | 0.5 | 1.0 — six decades of majorities | 14.5 | 4 | Partially Adequate |

**Tier robustness — by the D13 measure (protocol 6.4), the third least
tier-robust entry in the corpus, after Ostrom-style commons governance and
Islamic finance, and in both directions.** Its joint readings reach all
three tiers, spanning 5.5 points and 6 structural failures. The secondary
statistic, assuming independent calls: 64.1% of the 2,048 combinations of
its eleven flagged calls keep the Partially Adequate tier. By that share
alone the order changes: Universal Basic Services and MMT + Job Guarantee
(50.0% each) would rank as less tier-robust than this entry, although their
joint readings reach only two tiers, and Ostrom-style commons governance
(65.6% of 32,768) as more tier-robust, although its joint readings reach all
three. No single flagged call changes the tier. But only two failures (C2.2
and C4.5) are undisputed by any flagged call, and C4.5 moves only under the
population-scope reading below. The tier therefore depends jointly on six
calls:

- **Upward.** If both flagged failures (C4.2 and C4.4) resolve to 0.5 and
  nothing else moves, failures fall to 2 and the system becomes Potentially
  Adequate, at 15.0/26.
- **Downward.** With both flagged failures held, any two of C2.1, C2.4,
  C3.5, and C4.3 resolving to 0.0 bring failures to 6 — Structurally
  Inadequate, at 13.0/26.

Stated generally: with two undisputed failures, the tier is Partially
Adequate exactly when between one and three of those six calls stand at 0.0;
the primary reading has two. All upward readings together give 16.0/26 with
2 failures (Potentially Adequate), and all downward readings together give
10.5/26 with 8 failures (Structurally Inadequate). China's joint readings
spanned two tiers; this evaluation's span all three. Each call is
individually argued, but readers should treat the Partially Adequate finding
as the midpoint of a genuinely wide range rather than a settled placement.

**The population-scope decision, checked jointly.** Scoring citizens and PRs
only raises C1.5 to 1.0 and C4.5 to 0.5, giving 15.0/26 with 3 failures —
still Partially Adequate. Combined with every upward flag, the result is
17.0/26 with 1 failure (Potentially Adequate).

**On the canonical CSV.** Consistent with the scratch-before-insert
discipline, this evaluation was added to `neec_scores.csv` in a dedicated
insertion pass, Session 20, together with Sovereign Wealth Fund Statism and
State Capitalism / China — the three-system batch that Handoffs 17 and 18
proposed. The insertion adopted the display name this evaluation proposed,
`State Capitalism / Singapore (GLC Developmental Capitalism)`, which follows
the China entry's pattern so that the sibling sub-entries sort together.

---

## Final Assessment

**Key Strengths:**

- **Domain 1 (4.0/6) is the highest of the seven Step 1b systems,** and
  Singapore is the first Step 1b system to pass C1.2a or C1.3: the broadest
  individually held housing and savings mechanism the cohort has produced.
- **Domain 3 (3.5/5):** fast, large crisis response backed by
  constitutionally protected reserves, a distinctive inflation mechanism,
  and demonstrated adaptability.
- **Domain 5 (3.5/5):** a 61-year record, documented transfer abroad, and
  designed coexistence with markets.

**Key Deficiencies:**

- **Domain 4 (1.0/5) is the weakest domain,** tying Stakeholder Capitalism for fourth-lowest in the corpus, above only Status Quo, China and State Capitalism / Qatar. Two of its three failures (C4.2, C4.4) are flagged; C4.5 is not.
- **C2.2:** support is conditioned on work by design.
- **The non-resident workforce** — about a fifth of the population — is the
  thread running through C1.5, C2.1, C2.5, and C4.5, and the reason the
  population-scope decision matters.

**Three comparative findings (every formal claim checked by
`verify_singapore.py`).**

1. **An exact tie with Sovereign Wealth Fund Statism.** Both score 14.0/26,
   in the same tier, with different failure counts (3 and 4). The vectors
   differ on 7 criteria and share two failures (C4.2, C4.5). Singapore gains
   in Material Security (+1.5, from housing and wealth building) and System
   Resilience (+0.5), loses in Human Autonomy (−1.0) and Ethical Integrity
   (−1.0), and matches it in Implementation Viability. Sovereign Wealth Fund
   Statism set Singapore aside by design; scored on its own terms, the
   economy best known for its state investors lands on exactly the same
   total as the fund mechanism. This is a third kind of tie illustration for
   the corpus: Georgism/UBS/Islamic finance (same total; 2, 3 and 5 failures, in two tiers), China/CPS/Stakeholder Capitalism (same total, radically different profiles), and Singapore/SWF Statism (same total and tier; 4 and 3 failures).
2. **Singapore strictly dominates China, its state-capitalism sibling.** It
   scores at least as high on all 26 criteria and higher on 8, and every
   domain total is higher (+1.0, +1.0, +1.0, +0.5, +0.5). Its four failures
   are a subset of China's eight, and the four China failures it avoids
   (C2.1, C2.4, C3.5, C4.3) are exactly its four downward-flagged calls. The
   tier gap between the two siblings therefore rests on precisely those
   contested calls.
3. **Corpus position.** Only CCO-PTF-CIP-SZH dominates this system, and it dominates two: China and State Capitalism / Qatar. In the 23-system corpus it is tied 11th–12th with Sovereign Wealth Fund Statism.

**An archetype proposal (for the user's confirmation — not a decision
taken).** China and Singapore are the first two Step 1b systems that are
whole existing national political economies, and neither fits the three
archetypes named during Step 1b. Handoff 18 left open whether such entries
should sit with the Report's Systems 1–5. With two instances now, and the
Gulf entry to come, this evaluation proposes naming a fourth archetype,
**"configured national political economy,"** alongside the three already
named.

**Notes for the Gulf sub-entry.** Reuse the population-scope logic
(non-resident workforces are central to that model too), the
configured-system scope, and the two-directional tier check. Sovereign
Wealth Fund Statism and this entry are now its two natural comparators.
Section 8.1 leaves open whether the Gulf entry scores a composite or a
single representative jurisdiction; that choice should be made and justified
first.

---

## Reviewer disclosure (per NEEC_CONTRIBUTING.md §2 / Appendix H.6)

This is a first-pass scoring by a single AI reasoner (Claude), based on
about twenty-five web searches and two page fetches in Session 19 rather
than a systematic literature review — a narrower research pass than China's
(about forty-five searches). It has not yet been independently cross-checked
by a second scorer (H.9 Step 6). The source mix:

- **Singapore official sources:** the Ministry of Finance (Occasional Paper,
  2026); SingStat; the National Population and Talent Division; the Ministry
  of Manpower (including a parliamentary reply); the Ministry of Social and
  Family Development; the Monetary Authority of Singapore; the National
  Climate Change Secretariat; the Economic Development Board; the CPIB; the
  Prime Minister's Office; Temasek; the National Library Board; the Civil
  Service College; Workforce Singapore and related agencies; and NTUC.
- **Multilateral institutions:** the IMF (2021, 2025, and 2026 Article IV
  consultations) and the Bank for International Settlements.
- **Peer-reviewed and academic work:** the MIS research team (LKYSPP and
  NTU); *Public Administration and Development*; *Asian Survey*; *Journal of
  Banking & Finance*; *Journal of Multinational Financial Management*; *Land
  Use Policy*; *Habitat International*; *International Real Estate Review*;
  a Beihang University policy-transfer study; a University of Malaya working
  paper; NUS research notes; an SMU Lien Centre paper; RSIS; the Harvard
  Kennedy School case program; and LKYSPP commentary.
- **Independent research and ratings:** Freedom House, Reporters Without
  Borders, Climate Action Tracker, UBS (via press reports), Edelman (via the
  Civil Service College and press reports), the US State Department, and The
  Asia Group.
- **Civil society:** HOME, TWC2, AWARE, and the Business & Human Rights
  Resource Centre.
- **News and specialist outlets, named inline where used:** including CNBC,
  Reuters (via Yahoo Finance), Malay Mail and Bernama, Mothership, the
  *South China Morning Post*, The Online Citizen, The Independent Singapore,
  *The Diplomat*, Jom, *The Straits Times* (via PressReader), law-firm and
  consulting briefings (Rajah & Tann, KPMG, WTW, Jones Day, Fragomen,
  Lexology), and personal-finance and property sites.
- **Perspectives from several directions:** official defences (MOF, CPIB,
  the Prime Minister's Office, NTUC); a defence of Singapore's media model
  (*The Diplomat*); left critiques of the labour regime (World Socialist Web
  Site, Waging Nonviolence, People's World, HOME, TWC2); civil-liberties
  critiques (Freedom House, RSF, Jom); and peer-reviewed findings favourable
  to GLC performance.

**Limitations, stated plainly.**

- No free-market or conservative critique of the GLC model — for example, on
  crowding out private firms — was retrieved. This is the largest gap in the
  source mix.
- Several figures come through secondary reporting: UBS wealth figures,
  Edelman figures, the Credit Suisse top-1% share (from an older opinion
  column), MOF's wealth Gini (via Mothership), and advocacy-reported
  recruitment fees. No Pass or Failure rests solely on any one of them.
- Two institutional facts are stated from the schemes' design rather than a
  source retrieved this session: CPF membership is tied to citizenship or
  permanent residence, and CPF balances are earmarked. National-service
  obligations and ethnic quotas in public housing were not researched and
  are not relied on.
- No data on working hours or creative engagement were retrieved (C2.3), and
  no current gross-debt figure (C4.1).
- Freedom House's 2025 edition (covering 2024) was used; the 2026 edition's
  Singapore scores were not retrieved.
- The evaluator's training knowledge predates part of the evaluation window.
  Events in 2025–2026 rest entirely on the sources cited.

**The clearest candidates for independent disagreement** are the eleven
flagged calls in Summary Scores, and above all the six whose joint status
sets the tier: C4.2 and C4.4 upward, and C2.1, C2.4, C3.5, and C4.3
downward. A reader who rejects NEEC's democratic and anti-coercion
commitments (Section 2.2) will dispute C2.1, C2.4, and C4.4 at the level of
the criteria themselves; Appendix I is the route for that disagreement. A
reader who scores citizens and PRs only should apply the joint
population-scope reading. A reader who prefers MOF's wealth Gini to the
older top-1% figure may view C1.2b and C4.4 more favourably.

**Pre-existing corpus issues touched in passing** (not actioned here):

1. The Paper's H.7 C4.3 anchor inconsistency (Handoff 18, finding 2) bears
   directly on this entry's C4.3 flag, as noted there.
2. The hard-coded paths in `verify_swf.py` and `verify_ubs.py` remain.
   `verify_singapore.py` uses the portable lookup that `verify_china.py`
   introduced.

---

## Summary block

The machine-readable summary of this entry (protocol section 9; schema
`neec-summary-block/1.0`, `summary_block_schema.json`). It is generated from
the canonical corpus and the Session 28 staging (`summary_blocks_s28.json`),
not typed, and validated by `neec_entry.py`.

<!-- NEEC-SUMMARY-BLOCK -->
```json
{
  "schema": "neec-summary-block/1.0",
  "key": "State Capitalism / Singapore",
  "code": "SG",
  "display_name": "State Capitalism / Singapore (GLC Developmental Capitalism)",
  "record": {"documents": ["NEEC_StateCapitalism_Singapore_scoring_scratch.md"], "scored": "Session 19, natively on the v2 structure", "structure": "native-v2"},
  "scope": {"class": "configured_national_economy", "basis": "stated", "population": "This evaluation counts everyone who lives and works inside the system, non-residents included,", "source": {"file": "NEEC_StateCapitalism_Qatar_scoring_scratch.md", "locator": "document", "phrase": "Qatar is the third instance of the fourth Step 1b archetype, \"configured national political economy\" (confirmed in Session 20), after China and Singapore."}},
  "vector": {
    "C1.1": 0.5, "C1.2a": 1.0, "C1.2b": 0.5, "C1.3": 1.0, "C1.4": 0.5, "C1.5": 0.5,
    "C2.1": 0.5, "C2.2": 0.0, "C2.3": 0.5, "C2.4": 0.5, "C2.5": 0.5,
    "C3.1": 0.5, "C3.2": 1.0, "C3.3": 0.5, "C3.4": 1.0, "C3.5": 0.5,
    "C4.1": 0.5, "C4.2": 0.0, "C4.3": 0.5, "C4.4": 0.0, "C4.5": 0.0,
    "C5.1": 1.0, "C5.2": 0.5, "C5.3": 1.0, "C5.4": 0.5, "C5.5": 0.5
  },
  "summary": {"D1": 4.0, "D2": 2.0, "D3": 3.5, "D4": 1.0, "D5": 3.5, "total": 14.0, "failures": 4, "tier": "Partially Adequate"},
  "flags": [
    {"criterion": "C1.1", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": "extreme-line / CPS-precedent reading", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C1.2a", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": "lease-decay / illiquidity / excluded-fifth reading", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C2.1", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": "permit regime plus political constraints as comparable coercion", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C2.4", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": "no alternation since 1959 as foreclosing participation", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C3.2", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": "headline-inflation stress-test reading (6.1% in 2022)", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C3.4", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": "slow social-protection reform / dominant-party governance", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C3.5", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": "POFMA and unmeasured poverty as active suppression", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C4.2", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": "carbon-price / Nordic-analogy reading", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C4.3", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": "literal reading of the H.7 0.0 anchor", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C4.4", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": "broad ownership plus elections as partial diffusion", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}},
    {"criterion": "C5.4", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": "six decades of contested majorities as cross-spectrum support", "tracks": null, "source": {"file": "verify_singapore.py", "locator": "FLAGGED"}}
  ],
  "joint_readings": [
    {"id": "scored", "label": "as scored", "basis": "scored", "resolve": {}, "result": {"total": 14.0, "failures": 4, "tier": "Partially Adequate"}},
    {"id": "up", "label": "every flagged call resolved upward", "basis": "extremes", "resolve": {"C1.1": 1.0, "C4.2": 0.5, "C4.4": 0.5, "C5.4": 1.0}, "result": {"total": 16.0, "failures": 2, "tier": "Potentially Adequate"}},
    {"id": "down", "label": "every flagged call resolved downward", "basis": "extremes", "resolve": {"C1.2a": 0.5, "C2.1": 0.0, "C2.4": 0.0, "C3.2": 0.5, "C3.4": 0.5, "C3.5": 0.0, "C4.3": 0.0}, "result": {"total": 10.5, "failures": 8, "tier": "Structurally Inadequate"}}
  ],
  "scenarios": [
    {"id": "citizens-and-PRs-only", "label": "citizens and permanent residents only; the scored scope counts every resident", "kind": "scope", "changes": {"C1.5": 1.0, "C4.5": 0.5}, "result": {"total": 15.0, "failures": 3, "tier": "Partially Adequate"}}
  ]
}
```
<!-- /NEEC-SUMMARY-BLOCK -->
