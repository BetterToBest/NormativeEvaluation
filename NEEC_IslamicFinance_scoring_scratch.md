# NEEC Evaluation: Islamic Finance / Profit-Sharing Banking

**SCRATCH DRAFT — Step 1b, Session 22 (2026-09-17).** Follows Appendix H.9's
submission template, applied to the 26-criterion structure (the published H.9
still describes 25 criteria; see Handoff 20, correction 2). Scored directly
against the fully specified v2 structure (Section 12.3, Appendix H.7 and
H.7v2), as the eight earlier Step 1b systems were. This is the ninth of the
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
Research notes for this session are in `session22_research_notes.md`, written
during the research turn per Handoff 21's instruction.

---

## 22 [pending renumbering]. Islamic Finance / Profit-Sharing Banking

### Overview

**What is scored.** Paper Section 8.1 names this candidate entry "Islamic
finance / profit-sharing banking." The scored object is the **mechanism**:
profit-and-loss-sharing finance — *mudarabah* (one party supplies capital,
the other management; profit shared by a pre-agreed ratio, loss borne by the
capital provider absent negligence) and *musharakah* (both contribute
capital; profit by agreed ratio, loss by capital share) — together with the
prohibition of *riba*, layered onto an otherwise-unmodified market economy.
This follows the scope logic of Georgism / Land Value Tax, Mutual Credit /
LETS, and Sovereign Wealth Fund Statism, not the configured-national-economy
logic of the three state-capitalism sub-entries.

**Scope decisions (recommended in Handoff 21 as D5; confirmed by the user in
Session 22).**

- **Score the mechanism, not a country.** Malaysia's dual system is the
  principal implementation case and supplies most of the operating evidence,
  but Malaysia's poverty, housing, and ecological outcomes are not credited
  to the mechanism except where the mechanism is doing the work. Iran, Sudan,
  and Pakistan are used as whole-system or transitioning cases; Gulf and
  Bahraini institutions as sector cases.
- **The Islamic social-finance layer is adjacent, not included.** *Zakat*
  (an annual levy on qualifying wealth), *waqf* (endowment), and *takaful*
  (mutual protection) are not profit-sharing contracts; they are fiscal and
  charitable instruments that happen to share a tradition with the scored
  contracts. They are therefore scored as a **scope scenario**, not folded
  into the mechanism. This is the direct analogue of Georgism's
  Citizen's-Dividend caveat, where the dividend *was* folded in because
  George's own proposal pairs it with the tax; here the profit-sharing
  literature does not make zakat part of the contract set. Summary Scores
  enumerates the alternative.
- **Practice versus design is the central disclosure,** handled under
  Appendix H.6's ambiguous-source procedure: both readings are stated, the
  preponderance is scored, and the consequence of the other reading is given
  inline at every criterion it touches. Details below.
- **Stock or flow (Session 17's sub-distinction).** The mechanism is
  **stock-like**. Profit-sharing investment accounts (PSIAs) are an
  accumulating individually-held corpus, as Sovereign Wealth Fund Statism's
  fund is, rather than a pure flow like a land-value tax or a mutual-credit
  clearing balance. It differs from SWF Statism in that the corpus is held
  by households rather than by a state.
- **Neutrality.** What is evaluated is an economic mechanism, not a religion.
  Criteria whose score could turn on religious law rather than on economic
  structure are flagged explicitly (C4.3 is the only one; see there). "Riba"
  and the contract names are used as the industry's own technical terms.

**The design, in one paragraph.** Interest is prohibited; return must be
earned by bearing commercial risk. Mohammad Nejatullah Siddiqi's founding
two-tier model made *mudarabah* the primary mode, supplemented by
fixed-return modes — markup sale (*murabaha*), leasing (*ijara*), and
forward-purchase contracts (*salam*, *istisna*). Depositors become investment
account holders whose returns vary with the bank's asset performance;
borrowers become partners whose obligations vary with the venture's outcome.
The claim made for this design is that it ties finance to real activity,
distributes losses rather than concentrating them on debtors, and removes the
compounding creditor claim.

**The practice, in one paragraph — the central disclosure.** The fixed-return
modes became the industry's staple on both sides of the balance sheet. On the
asset side, Bank Negara Malaysia's own reporting put *tawarruq* (commodity
*murabaha*, a markup structure) at 22.4% of Malaysian Islamic bank financing
in 2016 and **46% by end-2019**; a Bank for International Settlements-hosted
address on Malaysian Islamic finance states that **more than 70% of financing
in Malaysia and the Middle East is debt-based**. The IFSB's own research
(Working Paper 10, 2019) gives the mechanism: **high regulatory risk weights
on *mudarabah* and *musharakah* assets — excluding diminishing *musharakah*
for home purchase — discourage Islamic banks from placing funds in them.**
The IFSB's *Islamic Financial Services Industry Stability Report 2025* names
"heavy reliance on hybrid instruments such as commodity *murabaha* in some
jurisdictions" as an emerging vulnerability. On the liability side, banks
smooth PSIA payouts through profit equalisation and investment risk reserves
to match market returns, because uncompetitive returns trigger withdrawals —
"displaced commercial risk" in the IFSB's terminology — so the risk-bearing
account behaves like a deposit. Investment account holders have no governance
rights over the assets their funds are in, and IFSB WP-10 records that
neither regulators nor banks regard indirect monitoring by shareholders as an
adequate substitute. Mahmoud El-Gamal's *Islamic Finance: Law, Economics and
Practice* (Cambridge, 2006) gives the standing academic name for the pattern:
"Shari'a arbitrage," in which classical contract forms are used to synthesise
conventional financial products, with what he calls cosmetic rather than real
ownership risk.

**Both readings are live.** The design reading is not a straw man: the
regulator itself treats risk-sharing as the goal and the shortfall as a
problem to fix. BNM launched **i-CITA in September 2025**, with **RM100
million of matching funds**, expressly "to promote wider use of risk-sharing
contracts, such as *mudarabah* and *musyarakah*," and convened an October
2025 scholars' roundtable on using contracts "beyond *tawarruq*." A
mechanism that its own central bank must subsidise into use is one whose
design and practice have come apart; that gap is the finding, and this
document scores the preponderance while enumerating what the other reading
changes.

**Scale (Appendix H.6, evidentiary tier: real-world implementation at
scale).** Global Islamic financial services assets reached **USD 3.88
trillion in 2024**, up 14.9% year on year, with Islamic banking assets up
17.05% (IFSB, 2025). The IFSB's prudential database covers Islamic banks or
windows in more than twenty jurisdictions across every income band. In
Malaysia, **Islamic financing reached 48% of total financing and takaful
participation 24.5% in 2025** (BNM Annual Report 2025) — against a
long-standing government target of 50% parity by 2025, which was therefore
narrowly missed. Malaysia's dual system dates from 1983; Iran converted its
banking system by the Law for Usury-Free Banking Operations (1983, operative
March 1984); Sudan Islamised its financial sector in phases from 1983;
Pakistan's Federal Shariat Court ruled in April 2022 that *riba* must go, and
the 26th Constitutional Amendment (October 2024) fixed the deadline at **1
January 2028**.

**Evidence gaps, stated up front.** No official time series for the
*musharakah* and *mudarabah* share of Malaysian Islamic bank financing was
retrieved; the 46% *tawarruq* figure is the closest official proxy and is
from end-2019. Reported shares of unbanked adults citing religious reasons
range from 4% to 25% across World Bank sources, and that conflict is
disclosed under C1.1. Zakat-effectiveness studies are numerous but the
literature itself reports a shortage of rigorous impact estimates. Where
evidence is secondary or absent, the text says so.

---

### Domain 1: Material Security

#### C1.1 Poverty Elimination Capacity: 0.5 (Partial) — flagged as contestable

*Pass threshold: 90% poverty reduction within 20 years under base scenario,
85% under stress testing.*

The mechanism contains no transfer, no floor, and no poverty target. What it
does contain is an access effect: a population that declines conventional
finance on religious grounds gains a usable alternative, and Islamic
microfinance operates in Malaysia, Pakistan, Bangladesh, and elsewhere. The
size of that population is genuinely disputed in the source material — the
World Bank's *Islamic Finance and Financial Inclusion* working paper reports
that **just 7% of unbanked adults worldwide cite religion**, a World Bank blog
drawing on the 2011 Findex reports about **12% in MENA against roughly 4%
elsewhere**, Brookings reports **13% across selected Muslim-majority
countries**, and a later World Bank experimental paper reports **about 25%**.
The same sources agree that cost, distance, and documentation dominate
religion as barriers. Taking the conflict at face value, the access effect is
real and non-trivial but nowhere near a 90% reduction mechanism.

Malaysia's own poverty record belongs to Malaysian development policy, not to
the contract type, and is not credited here. BNM's social-finance programmes
(*iTEKAD* for microentrepreneurs, expanded in 2025 with *iTEKAD Protection*)
are real but small and are properly part of the adjacent social-finance layer.

Scored 0.5 on H.7's "real but partial reduction" band, alongside Georgism,
Mutual Credit / LETS, Sovereign Wealth Fund Statism, and Universal Basic
Services. **Flagged:** a scorer who holds that an access change is not a
poverty mechanism at all would score **0.0**, taking the total to 13.0/26
with 6 failures and the tier to Structurally Inadequate.

#### C1.2a Wealth Building for Resilience: 0.5 (Partial) — flagged as contestable

*Pass threshold: $60,000 median wealth accumulation over 20 years for 70%+ of
participants.*

A profit-sharing investment account is a genuine, individually held,
accumulating store of value, and Malaysia has a large Shariah-compliant
unit-trust industry alongside it. Access is not gated by membership or prior
capital. That is more than Integral's dissolving credits (0.0) and more than
Georgism's dividend (0.0), and it is why this mechanism is classed as
stock-like under Session 17's sub-distinction.

What holds it at 0.5 rather than 1.0 is that the buffer-building is
indistinguishable in practice from ordinary bank saving: displaced-commercial-
risk smoothing pays account holders a market-benchmarked return, so the
equity upside that distinguishes the design does not reach them. Nothing in
the retrieved evidence shows the threshold's $60,000-for-70% bar being
cleared by the mechanism as opposed to by the host economy. H.7v2's 0.5 band
— "some accumulation mechanism exists but is narrow, indirect, or held
collectively rather than individually" — fits the indirectness.

**Flagged:** treating PSIAs and Shariah-compliant funds as a documented
mechanism reaching most participants gives **1.0**, taking the total to
14.0/26 without changing the failure count or the tier.

#### C1.2b Prevention of Exploitative Accumulation: 0.0 (Structural Failure) — flagged as contestable

*Pass threshold: Gini < 0.35 for wealth distribution.*

This is the first of the three criteria Handoff 21 predicted the
practice-versus-design gap would bear on, and the prediction holds. The design
argument is that risk sharing splits returns between capital and enterprise
rather than guaranteeing the capital holder a claim. The practice is that the
dominant contracts deliver a predetermined markup to the financier, the
liability side pays a smoothed market return, and nothing in the mechanism
caps or claws back concentration. Layered on an unmodified market economy, the
wealth distribution is the market's. H.7v2's 0.0 band — "no structural
prevention mechanism; concentration compounds without limit" — is met, as it
is for Status Quo Market Capitalism and Universal Basic Services.

The strongest counter-argument is that zakat is exactly such a structural
mechanism: an annual levy on qualifying wealth. Under this document's scope
decision zakat is adjacent to the mechanism rather than part of it, so it does
not score here. That decision is the single most consequential one in this
evaluation and is enumerated as a scenario in Summary Scores.

**Flagged:** under the broad scope, or on the view that the riba prohibition
itself restrains creditor accumulation enough to register, this becomes
**0.5**, taking the total to 14.0/26 with 4 failures — still Partially
Adequate.

#### C1.3 Housing Security: 0.5 (Partial)

*Pass threshold: 88% housing stability over 5-year periods, affordability at
80% AMI.*

The mechanism has a real housing product and it is the one place where the
profit-sharing design survived contact with the market at scale: *musharakah
mutanaqisah*, diminishing partnership, in which bank and customer co-own the
property and the customer buys out the bank's share over time. IFSB WP-10
notes it is carved out of the punitive risk weights that suppressed equity
financing everywhere else, which is a plausible explanation for its survival.
Two further borrower protections are structural rather than regulatory: the
financier bears genuine ownership risk during the partnership, and a markup
sale price cannot be increased for late payment, so the obligation cannot
compound after default.

Against that, allocation remains fully market-based, profit rates are
competitive with conventional mortgages rather than below them, and there is
no decommodification, no affordability floor, and no stabiliser. Scored 0.5 —
H.7's "partial protection or a real but incomplete mechanism." Not flagged;
both the presence of a real mechanism and the absence of a stabiliser are
well documented.

#### C1.4 Automation Resilience: 0.0 (Structural Failure) — flagged as contestable

*Pass threshold: poverty < 8% and aggregate demand > 85% of baseline across
30%, 50%, and 70% displacement scenarios.*

The mechanism has nothing to offer this criterion. Changing how credit is
priced and structured leaves distribution running
entirely through wage labour. Under 50% or 70% displacement, a
profit-sharing bank faces exactly what a conventional bank faces, with the
added feature that its investment account holders' returns fall with asset
performance. H.7's 0.0 band — "no mechanism; system structurally requires
wage labor for both income distribution and demand" — applies, as it does to
Status Quo Market Capitalism.

**Flagged:** a scorer could credit PLS investment accounts as a non-wage
income channel that persists under displacement and score **0.5**, as
Georgism, Mutual Credit / LETS, and Sovereign Wealth Fund Statism are
scored. The reason this document does not is that under the practice reading
those accounts pay a smoothed market-benchmarked return — that is, deposit
interest under another name, which Status Quo Market Capitalism already has
and is scored 0.0 for. At 0.5 the total is 14.0/26 with 4 failures, still
Partially Adequate.

#### C1.5 Universal Wealth Access (narrowed — access breadth only): 0.5 (Partial) — flagged as contestable

*Pass threshold: 80% of the population with an active wealth-accumulation
pathway.*

Access to the accumulation vehicles is not membership-gated: anyone may open
a Shariah-compliant savings or investment account, and a PricewaterhouseCoopers
Malaysia study cited by the World Bank found that the majority of Islamic
finance customers in Malaysia are non-Muslim — direct evidence that the
mechanism does not gate on religious affiliation. Against that, the
equity-based products are effectively absent at the bottom of the
distribution: the literature reports that **no Malaysian microfinance
institution offers *musharakah* or *mudarabah* contracts**, leaving
microcredit-style debt instruments in their place, and the unbanked remain
unbanked for cost and documentation reasons the mechanism does not address.

H.7v2's 0.5 band — "access exists but is gated such that a meaningful
population segment is excluded" — fits, with the gate being product
availability rather than membership. Note that this breaks the C1.2a/C1.5
lockstep seen elsewhere in the corpus only in the sense that both sit at 0.5
for different reasons.

**Flagged:** a scorer who weighs the absence of equity products at the bottom
more heavily would score **0.0**, taking the total to 13.0/26 with 6 failures
and the tier to Structurally Inadequate.

---

### Domain 2: Human Autonomy

#### C2.1 Freedom from Coercion: 0.5 (Partial)

*Pass threshold: 70% report genuine autonomy in major life decisions.*

The prohibition on compounding a debt after default is a real reduction in
one well-documented coercion channel — the debt spiral — and asset-backing
requirements bar the pure credit-trading chain. Survival nonetheless remains
contingent on labour-market participation, and the dominant markup contract
creates a fixed obligation that is economically close to a loan. H.7's 0.5
band — "meaningfully reduces coercion relative to a harsher baseline but does
not eliminate it" — applies, as for Status Quo Market Capitalism. Not
flagged.

#### C2.2 Labor Non-Necessity: 0.0 (Structural Failure)

*Pass threshold: unconditional provision covering 100% of basic needs.*

There is no baseline provision of any kind in the mechanism. H.7 notes this
threshold is binary in character. One of the two failures in this evaluation
that no flagged call disputes. Not flagged.

#### C2.3 Creative Development Opportunities: 0.5 (Partial)

*Pass threshold: 50% regular creative engagement, 10+ hours a week.*

The mechanism does not alter working time, and inherits the host economy's
time structure. Scored at the corpus's standard band for market-layered
mechanisms, alongside Georgism, Mutual Credit / LETS, Sovereign Wealth Fund
Statism, and Status Quo Market Capitalism. Not flagged.

#### C2.4 Democratic Participation: 0.5 (Partial) — flagged as contestable

*Pass threshold: 70% participation, 35% of citizen proposals adopted.*

Scored at the corpus's standard band for a mechanism layered on a market
democracy, where the host polity supplies the political rights and
concentrated economic power dilutes them — the same 0.5 given to Georgism,
Mutual Credit / LETS, and Sovereign Wealth Fund Statism.

The reason this is flagged rather than routine is that the mechanism adds a
documented governance deficit of its own. Unrestricted PSIA holders bear
investment risk but have no right to appoint or dismiss directors and no
other voice in governance; the IFSB proposed a governance committee to
supply one. IFSB WP-10 records that **neither the regulators nor the banks
consider indirect monitoring by shareholders sufficient** to make up for it.
Shariah supervisory boards are appointed, not elected, and El-Gamal's
critique of their role as rent-seeking is part of the standing literature.
Capital at risk without a vote is, on its face, a step away from economic
democracy rather than toward it.

**Flagged:** scoring the mechanism's own contribution rather than the host
baseline gives **0.0**, taking the total to 13.0/26 with 6 failures and the
tier to Structurally Inadequate.

#### C2.5 Exit Rights and Mobility: 1.0 (Pass) — flagged as contestable

*Pass threshold: exit feasible within 3 months without material penalty; the
system continues functioning at partial participation.*

In its scored form the mechanism is strictly elective. A dual system means
every customer chooses between Islamic and conventional products at every
transaction; Malaysia has run both side by side for four decades, the Islamic
side reached 48% of financing without compulsion, and the majority of its
customers are reported to be non-Muslim. H.7's 1.0 band — opt-out without
penalty, with the system continuing at partial participation — is met about
as cleanly as anywhere in the corpus, and matches Georgism, Mutual Credit /
LETS, Sovereign Wealth Fund Statism, and Universal Basic Services.

**Flagged:** in the mandatory jurisdictions — Iran since 1984, Sudan, and
Pakistan from 1 January 2028 — there is no exit, and a scorer who treats
those as the mechanism rather than as one deployment of it would score
**0.5**, taking the total to 13.0/26 with the failure count and tier
unchanged.

---

### Domain 3: System Resilience

#### C3.1 Crisis Response Capacity: 0.5 (Partial)

*Pass threshold: response within 72 hours, scaling with severity, 90%
population coverage, no legislative delay.*

This is one of the mechanism's genuine empirical strengths, and the evidence
is IMF-grade. IMF Working Paper 10/201 (Hasan and Dridi) found that features
of the Islamic banking business model limited the hit to profitability in
2008, that credit and asset growth held up better than at conventional banks
through 2008–09 — contributing, in the authors' words, to financial and
economic stability — and that rating agencies' reassessments were generally
more favourable. Beck, Demirgüç-Kunt and Merrouche found higher
intermediation ratios, better asset quality, better capitalisation, and
better stock-market performance through the crisis. The same IMF paper found
the other half of the picture: risk-management weaknesses at some Islamic
banks produced a *larger* profitability decline in 2009.

What this is not is an automatic population-wide stabiliser. There is no
trigger, no coverage guarantee, and no 72-hour response; the resilience is a
bank-level property. H.7's 0.5 band — "some crisis-responsive capacity exists
but is not automatic, is firm-level rather than system-wide" — is the right
home, the same one Market Socialism occupies for cooperative-level
resilience. Not flagged.

#### C3.2 Inflation Control Mechanisms: 0.5 (Partial)

*Pass threshold: long-term inflation ≤ 3%, stress-test ≤ 5%, automatic
adjustment.*

The mechanism supplies no distinct inflation-control instrument; outcomes
track the host monetary framework. IMF Working Paper 16/72 found that low and
stable inflation and a working transmission mechanism are attainable with a
significant Islamic banking segment — Brunei, Bahrain, and Malaysia recorded
the lowest inflation among such countries — while Iran, Sudan, Pakistan, and
Yemen were identified as needing a stronger monetary framework. That
contrast is informative precisely because it cuts across contract type: the
two whole-system cases sit on the weak side, so the inflation record follows
the monetary regime rather than the prohibition of interest. Malaysia's
MYOR-i, mandated for Islamic products from the second half of 2027, is a
benchmark rate, not a price-stability mechanism. H.7's 0.5 band — "relies on
conventional monetary policy without novel safeguards" — applies. Not
flagged.

#### C3.3 Multi-Failure Resistance: 0.5 (Partial)

*Pass threshold: core functions maintained across 3 of 4 compound stress
scenarios with degradation < 20%.*

Asset-backing and the prohibition on trading debt kept Islamic banks out of
the securitisation chain that transmitted the 2008 shock, which is a real
structural source of compound-stress resistance. Set against it: in a dual
system the Islamic segment funds and hedges alongside the conventional one;
the IFSB's 2025 report names heavy commodity-*murabaha* reliance, persistent
structural liquidity surpluses, and sectoral concentration as live
vulnerabilities; and asset-backing concentrates exposure in property and
commodities, which co-move. H.7's 0.5 band — "some resilience from
distributed structure, but interconnection still transmits shocks" — applies.
Not flagged.

#### C3.4 Epistemic Adaptability: 1.0 (Pass) — flagged as contestable

*Pass threshold: 30% parameter adjustability, policy updates within 6 months
of evidence, governance for changes, zero collapses during adjustment.*

The demonstrated record is strong. BNM's Shariah Advisory Council tightened
the requirements on *bay' al-inah* in 2012 and the industry re-engineered its
product set around *tawarruq* within a few years — *tawarruq*'s share of
financing doubled between 2014 and 2016 and reached 46% by 2019 — without
destabilisation. In 2025 alone the SAC enabled *istisna*-based inventory
purchase and *salam*-based agriculture financing, BNM published a working
paper on Shariah analysis of central bank digital currency, issued a policy
document on broader application of *ta'awun* in takaful, opened the Shariah
Contract Framework and Investment Account discussion papers for industry
feedback, and set out the MYOR-i transition roadmap. The Securities
Commission's SRI Sukuk Framework has been revised twice since 2014. That is
rapid, governed, evidence-responsive parameter adjustment, matching the
corpus's 1.0 band as given to Georgism, Mutual Credit / LETS, Sovereign
Wealth Fund Statism, and Universal Basic Services.

**Flagged:** the adaptation has been overwhelmingly *form-level* — finding
compliant wrappers for the same economic substance — which is El-Gamal's
critique exactly, and jurisdictions diverge rather than converge on evidence
(AAOIFI has reservations about organised *tawarruq* that Malaysia's SAC does
not share; Middle Eastern scholars generally reject the *bay' bithaman ajil*
structure popular in Malaysia, Indonesia, and Brunei). A scorer who holds
that form-level adaptation is not evidence-based adaptation would score
**0.5**, taking the total to 13.0/26 with the failure count and tier
unchanged.

#### C3.5 Failure-Mode Transparency: 0.5 (Partial) — flagged as contestable

*Pass threshold: failure detection within 1 week, diagnosis 80%, correction
70%, externalisation < 10% of total costs.*

Two authoritative sources point different ways, and Appendix H.6 requires
both to be stated. IMF Working Paper 15/120 reports that investment account
holders **generally have no control over profit equalisation and investment
risk reserves and in some cases are not informed of the bank's practices in
maintaining them**. IFSB WP-10 reports that Islamic banks **mostly comply
with the disclosure requirements** on the use of those reserves, and IFSB
Guidance Note 3 and BNM's own Guidelines on Profit Equalisation Reserve set
those requirements out. The preponderance is that a disclosure regime exists
and is largely observed, while the smoothing it discloses still has the
effect of hiding the underlying variance in asset returns from the people
bearing it — and ecological and diffuse social costs are externalised exactly
as at any market bank. H.7's 0.5 band — "some failures are visible while
others remain externalized" — fits.

**Flagged:** weighting the IMF finding over the IFSB's, and treating
return-smoothing as active suppression of the mechanism's own central failure
mode, gives **0.0** — the band Stakeholder Capitalism occupies for systemic
failures obscured behind positive messaging, a reading with some force given
the value-based-intermediation framing. That takes the total to 13.0/26 with
6 failures and the tier to Structurally Inadequate.

---

### Domain 4: Ethical Integrity

#### C4.1 Intergenerational Justice: 0.5 (Partial) — flagged as contestable

*Pass threshold: 35% carbon reduction by 2030, resource use ≤ 90% of
regeneration, debt-to-GDP < 80%, positive intergenerational wealth transfer.*

The positive side is a restraint on the accumulation of compounding claims on
future income: interest is prohibited, debt cannot be traded at a discount,
obligations cannot compound after default, and sukuk are tied to identifiable
assets. A mechanism that structurally limits leverage limits one channel of
negative intergenerational transfer. The negative side is that it places no
constraint at all on resource use, and it finances a fossil-heavy economy:
Malaysia was generating only about 3% of its power from renewables as of
recent reporting, with Petronas among Asia's largest oil producers, and
nothing in the contract set changes that. H.7's 0.5 band — "some positive
transfer exists but is incomplete or coexists with significant negative
transfer" — applies, the same band as Nordic Social Democracy.

**Flagged:** treating leverage restraint as an absence of harm rather than a
positive transfer would score **0.0**, taking the total to 13.0/26 with 6
failures and the tier to Structurally Inadequate.

#### C4.2 Ecological Compliance: 0.0 (Structural Failure)

*Pass threshold: absolute carbon reductions of 35–45% by 2030, extraction ≤
regeneration, 7 of 9 planetary boundaries respected.*

Held to absolute-reduction standards, as Appendix H.7 requires. The
mechanism's ecological instruments are allocative labels, not
caps: Malaysia's SRI Sukuk Framework (2014, revised 2019 and 2022), the first
green sukuk in 2017, the SRI Sukuk and Bond Grant Scheme, BNM's Greening
Halal Businesses programme with over 200 SMEs, and value-based
intermediation, under which institutions channelled RM148.6 billion into
VBI-aligned activities in 2024. Every one of these directs capital toward
better projects; none constrains the total. H.7's 0.0 band — "relative or
efficiency metrics substituting for absolute ones" — is the same finding the
corpus records against Stakeholder Capitalism's ESG metrics, and the
structural similarity between proceeds-use labelling and ESG reporting is
close. The second of the two failures no flagged call disputes. Not flagged.

#### C4.3 Racial and Gender Equity: 0.5 (Partial) — flagged as contestable

*Pass threshold: disparity reduction of 5 percentage points per 5 years,
disadvantaged groups receiving 150%+ of proportional benefits.*

**Neutrality note — this is the one criterion whose score could turn on
religious law rather than economic structure, and the scope decision is
stated rather than buried.** The scored object is the set of financial
contracts. Those contracts do not differentiate by race or sex: a *mudarabah*
or *murabaha* has identical terms whoever signs it. Rules of inheritance are
a separate body of law that the profit-sharing literature does not treat as
part of the mechanism, and they are therefore outside this scope, exactly as
Malaysian development policy is outside it.

Within scope, the finding is formal equality without any reparative
mechanism, plus evidence of uneven reach: BNM reporting cited in the
literature notes that Malaysian women entrepreneurs participate insufficiently
in Islamic micro-financing relative to men, and INCEIF work documents a
gender gap in Islamic wealth management in Malaysia. H.7's 0.5 band — "formal
equality without reparative mechanisms" — applies, the band Integral occupies.

**Flagged:** a scorer who folds inheritance rules into the mechanism, or who
weighs the documented participation gap as evidence that formally neutral
contracts replicate existing disparity, would score **0.0**, taking the total
to 13.0/26 with 6 failures and the tier to Structurally Inadequate. Readers
who think the scope decision itself is wrong should contest it through
Appendix I rather than through this score.

#### C4.4 Power Distribution: 0.0 (Structural Failure) — flagged as contestable

*Pass threshold: wealth Gini < 0.35, 40% of citizen proposals adopted,
democratic accountability for 80% of major decisions.*

Economic power is distributed as the host market distributes it, and the
mechanism adds a concentration of its own rather than diffusing one: the
providers of risk capital — investment account holders — have no governance
rights, discretion over the smoothing reserves sits with the bank, and
Shariah authority is exercised by appointed boards. H.7's 0.0 band —
"concentration in a narrow group, whether market-based or bureaucratic" —
applies, the band Status Quo Market Capitalism occupies.

**Flagged:** under the design reading, risk sharing does diffuse returns
between financier and entrepreneur, which would support **0.5** — the band
Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism, and Universal
Basic Services occupy. At 0.5 the total is 14.0/26 with 4 failures, still
Partially Adequate.

#### C4.5 Exploitation Elimination: 0.5 (Partial) — flagged as contestable

*Pass threshold: extraction rates < 10% of GDP, genuine exit rights from
exploitative relationships, residual coercion < 10% of decisions.*

The third criterion Handoff 21 predicted the practice-versus-design gap would
bear on. The design targets creditor extraction directly and explicitly — few
systems in this corpus make elimination of one extractive relationship a
first-order design commitment. Two of its effects are substantive rather than
formal: obligations cannot compound after default, and the pure credit-trading
chain is barred. Against that, the dominant contracts deliver a
predetermined return on advanced funds; an overview of Sudan's and Iran's
systems reports that Iranian *mudarabah* often specifies the bank's profit in
advance regardless of the venture's outcome, which is the design's own
negation; smoothing benchmarks the liability side to market returns; and
capital–labour extraction in the host economy is untouched throughout.

H.7's 0.5 band — "elimination in one relationship type while another
persists," or reduced-but-not-eliminated extraction — is the right reading,
the band Nordic Social Democracy occupies for the same shape of finding.

**Flagged:** the strict form-over-substance reading, on which the prohibition
is satisfied in form while the economic substance of the creditor claim
survives intact, gives **0.0**, taking the total to 13.0/26 with 6 failures
and the tier to Structurally Inadequate. This is the single call most
directly at stake in the practice-versus-design dispute, and the one a second
scorer is most likely to move.

---

### Domain 5: Implementation Viability

#### C5.1 Proven Component Foundation: 1.0 (Pass)

*Pass threshold: 70% of components proven through 20 years of operation at a
scale of 10,000+ participants, with documented outcomes.*

The strongest criterion in the evaluation and the least disputable. Malaysia
has run the mechanism since 1983 and licenses 16 full-fledged Islamic banks
under the Islamic Financial Services Act 2013; Islamic financing is 48% of
total financing there. Globally the industry holds USD 3.88 trillion in
assets and the IFSB's prudential data cover banks or windows in more than
twenty jurisdictions. Iran has operated a converted system since 1984 and
Sudan since the 1980s. Every component named in the design — *mudarabah*,
*musharakah*, diminishing *musharakah*, *murabaha*, *ijara*, *salam*,
*istisna*, sukuk, takaful — is in documented commercial use at scale. Whether
the outcomes match the design's promise is the subject of the rest of this
document; the components themselves are unambiguously proven. Not flagged.

#### C5.2 Staged Transition Pathways: 1.0 (Pass) — flagged as contestable

*Pass threshold: a detailed plan for both staged (4 phases) and rapid (36
months) deployment, with milestones, resources, and risk mitigation. Judge on
specificity.*

Both pathways exist and both are documented with dates. The gradual pathway:
Malaysia's forty-year build, from the first Islamic bank in 1983 through the
Islamic Financial Services Act 2013 to a mandated MYOR-i benchmark transition
from the second half of 2027 and the cessation of KLIBOR by 1 January 2029 —
and Pakistan's, where the Federal Shariat Court's April 2022 judgment was
written into the constitution by the 26th Amendment with a **1 January 2028**
deadline, a Ministry of Finance roadmap, and explicit grandfathering of
existing conventional contracts to maturity. Sudan's conversion proceeded in
documented phases from 1983. The rapid pathway: Iran legislated conversion in
1983 and operated the converted system from March 1984, inside the
threshold's 36 months. BNM has also exported the staged model, supporting 17
jurisdictions in 2025 and running a capacity-building programme for Central
Asian states and Azerbaijan on building dual systems.

Milestones are real enough to be missed: Malaysia's 50%-parity-by-2025 target
came in at 48%. That is evidence the pathway is measurable, not evidence it
is absent.

**Flagged:** a scorer could hold that these are national policy artefacts
rather than the mechanism's own specified plan, that Pakistan's roadmap is
announced rather than executed, and that Iran's rapid conversion is a
contested precedent — scoring **0.5**, taking the total to 13.0/26 with the
failure count and tier unchanged.

#### C5.3 Partial and Parallel Deployability: 1.0 (Pass)

*Pass threshold: viable at 30% participation, coexisting with traditional
markets that maintain 90% of economic activity, with a validated scaling
pathway.*

The dual system is not an argument for partial deployability; it is a
four-decade demonstration of it. Islamic and conventional banking operate
side by side in Malaysia with no co-mingling of funds, the Islamic side at
48% of financing; in most other jurisdictions the mechanism operates at far
lower shares without difficulty; conventional banks run Islamic windows; and
sovereign issuers outside the traditional markets, including the United
Kingdom, Luxembourg, and Hong Kong, have issued sukuk. The scaling pathway
from a single licensed bank to near-parity is documented rather than
modelled. Not flagged.

#### C5.4 Political Coalition Potential: 0.5 (Partial) — flagged as contestable

*Pass threshold: 60% support across the political spectrum, 65% opposition to
repeal, 80% survival probability across administration changes.*

Support is durable where it exists: four decades of consistent Malaysian
policy across changes of government, and a Pakistani constitutional amendment
passed with the required two-thirds majority in both houses. But the coalition
is bounded. In secular and non-Muslim-majority polities the mechanism is
adopted as an instrument — sukuk issuance, window operations — rather than as
an economic programme, and within the tradition it faces real scholarly
opposition, with AAOIFI reservations about organised *tawarruq* and Middle
Eastern rejection of structures Malaysia permits. H.7's 0.5 band — "appeals
strongly to part of the spectrum while facing real resistance from another
part" — applies.

**Flagged:** treating instrument-level adoption by the UK, Luxembourg, Hong
Kong, and seventeen jurisdictions receiving BNM technical support as
demonstrated cross-ideological appeal would score **1.0**, taking the total
to 14.0/26 without changing the failure count or the tier.

#### C5.5 Cultural Adaptability: 1.0 (Pass) — flagged as contestable

*Pass threshold: viable across 3 economic contexts and 5 cultural contexts,
with a 40% parameter-flexibility range, validated across diverse
implementations.*

The evidence clears the stated threshold on each limb. Three income bands:
the United Kingdom and Qatar at the top, Malaysia and Türkiye in the middle,
Bangladesh, Sudan, and the Kyrgyz Republic at the bottom. Five or more
cultural contexts: Southeast Asia, South Asia, the Gulf and wider MENA,
Sub-Saharan Africa, Central Asia, and Europe, with Africa and Central Asia
the fastest-growing regions in 2024. Parameter flexibility well beyond 40%:
the schools of jurisprudence produce materially different permissible product
sets, and jurisdictions choose among them — Malaysia's Shariah Advisory
Council permits organised *tawarruq* on more permissive views while AAOIFI
does not, and *bay' bithaman ajil* is standard in Malaysia, Indonesia, and
Brunei while Middle Eastern scholars generally reject it. Validation across
diverse implementations: the IFSB's prudential database. H.7's 1.0 band —
explicit parameter adjustment for diverse contexts — applies, and the
divergence that looks like incoherence from a Shariah standpoint is precisely
what adaptability looks like from NEEC's.

**Flagged:** the industry remains concentrated in Muslim-majority
jurisdictions, and a scorer who reads that concentration as the narrow range
described by H.7's 0.5 band would score **0.5**, taking the total to 13.0/26
with the failure count and tier unchanged. The evidence cutting the other way
is that the majority of Malaysian Islamic finance customers are reported to
be non-Muslim, which weakens the claim that the mechanism requires a
religious precondition it cannot itself produce — the reasoning behind Market
Socialism's 0.0 here.

---

## Summary Scores

<!-- GENERATED:summary -->
| Criterion | Name | Score | Result |
|---|---|---|---|
| C1.1 | Poverty Elimination Capacity *(flagged)* | 0.5 | Partial |
| C1.2a | Wealth Building for Resilience *(flagged)* | 0.5 | Partial |
| C1.2b | Prevention of Exploitative Accumulation *(flagged)* | 0.0 | Structural Failure |
| C1.3 | Housing Security | 0.5 | Partial |
| C1.4 | Automation Resilience *(flagged)* | 0.0 | Structural Failure |
| C1.5 | Universal Wealth Access (narrowed) *(flagged)* | 0.5 | Partial |
| C2.1 | Freedom from Coercion | 0.5 | Partial |
| C2.2 | Labor Non-Necessity | 0.0 | Structural Failure |
| C2.3 | Creative Development Opportunities | 0.5 | Partial |
| C2.4 | Democratic Participation *(flagged)* | 0.5 | Partial |
| C2.5 | Exit Rights and Mobility *(flagged)* | 1.0 | Pass |
| C3.1 | Crisis Response Capacity | 0.5 | Partial |
| C3.2 | Inflation Control Mechanisms | 0.5 | Partial |
| C3.3 | Multi-Failure Resistance | 0.5 | Partial |
| C3.4 | Epistemic Adaptability *(flagged)* | 1.0 | Pass |
| C3.5 | Failure-Mode Transparency *(flagged)* | 0.5 | Partial |
| C4.1 | Intergenerational Justice *(flagged)* | 0.5 | Partial |
| C4.2 | Ecological Compliance | 0.0 | Structural Failure |
| C4.3 | Racial and Gender Equity *(flagged)* | 0.5 | Partial |
| C4.4 | Power Distribution *(flagged)* | 0.0 | Structural Failure |
| C4.5 | Exploitation Elimination *(flagged)* | 0.5 | Partial |
| C5.1 | Proven Component Foundation | 1.0 | Pass |
| C5.2 | Staged Transition Pathways *(flagged)* | 1.0 | Pass |
| C5.3 | Partial and Parallel Deployability | 1.0 | Pass |
| C5.4 | Political Coalition Potential *(flagged)* | 0.5 | Partial |
| C5.5 | Cultural Adaptability *(flagged)* | 1.0 | Pass |

| Domain | Score | Max |
|---|---|---|
| Material Security | 2.0 | 6 |
| Human Autonomy | 2.5 | 5 |
| System Resilience | 3.0 | 5 |
| Ethical Integrity | 1.5 | 5 |
| Implementation Viability | 4.5 | 5 |
| **Total** | **13.5** | **26** |

**Total: 13.5/26 (52%). Structural failures: 5 (C1.2b, C1.4, C2.2, C4.2, C4.4). Adequacy tier: Partially Adequate.**
<!-- END GENERATED:summary -->

Domain vector: **2.0 / 2.5 / 3.0 / 1.5 / 4.5**.

### The flagged calls, and what they do to the tier

This evaluation carries **16 flagged** contestable calls, the largest set of
any entry in the corpus, ahead of Ostrom-style commons governance's fifteen.
That is not indecision: it is the direct consequence of scoring a mechanism
whose design and practice diverge, which makes most criteria two-sided by
construction. Treating each flag as an independent binary gives **65,536
combinations**, with totals running **8.0-16.0**. Every one of the three
adequacy tiers is reachable, so **the tier is not robust**. By the D13
measure (protocol 6.4), which compares entries on their joint readings, this
entry is the second least tier-robust in the corpus: its joint readings
reach all three tiers, spanning 5.0 points and 9 structural failures. It is
less tier-robust than State Capitalism / Singapore (three tiers, 5.5 points
and 6 failures, from eleven flags) and more tier-robust than Ostrom-style
commons governance (three tiers, 7.5 points and 9 failures, from fifteen
flags, with no structural failure undisputed). The secondary statistic, the
enumeration's share of combinations that keep the scored tier (assuming
independent calls), orders this entry and Ostrom-style commons governance
the other way: 17.1% of this entry's 65,536 combinations keep the Partially
Adequate tier, against 65.6% of Ostrom's 32,768. Here, only **two of the
five structural failures are undisputed** by any flagged call: C2.2 (no
unconditional provision) and C4.2 (no absolute-reduction mechanism).

Independent enumeration overstates the real uncertainty, because the flags
are not independent — most of them turn on the same underlying question.
Three coherent joint readings are therefore given alongside it, and this
document recommends them as the more informative summary:

- **Reading A — as designed.** Credit the mechanism for what
  profit-and-loss sharing is meant to do (C1.2a 1.0, C1.2b 0.5, C1.4 0.5,
  C4.4 0.5): **15.5/26 (60%), 2 failures, Potentially Adequate.**
- **Reading B — as practised, scored here.** **13.5/26 (52%), 5 structural
  failures, Partially Adequate.**
- **Reading C — strict form-over-substance.** Take El-Gamal's critique to its
  conclusion, crediting nothing that the markup contracts deliver in form
  only (C1.1, C1.5, C2.4, C3.5, C4.1, C4.5 all 0.0): **10.5/26 (40%), 11
  failures, Structurally Inadequate.**

The spread between Reading A and Reading C — 5.0 points and nine failures —
is the practice-versus-design gap expressed in NEEC's own units, and is the
most useful single number this evaluation produces.

### The scope scenario

Counting the Islamic social-finance layer (zakat, waqf, takaful) as part of
the mechanism rather than adjacent to it raises C1.1 to 1.0 and C1.2b to
0.5, giving **14.5/26 (56%), 4 failures, Partially Adequate**. The tier does
not move, but the total would tie Mutual Credit / LETS, Universal Basic
Income and Ostrom-style commons governance. Anyone re-scoring this entry
should state which scope they used before comparing totals.

---

## Where this sits in the corpus

<!-- GENERATED:corpus -->
| Rank | System | Score /26 | % | Failures | Tier |
|---|---|---|---|---|---|
| 1 | CCO-PTF-CIP-SZH | 24.5 | 94 | 0 | Potentially Adequate |
| 2 | Participatory Economics | 20.5 | 79 | 1 | Potentially Adequate |
| 3 | Integral | 19.5 | 75 | 3 | Partially Adequate |
| 3 | Nordic Social Democracy | 19.5 | 75 | 2 | Potentially Adequate |
| 5 | Degrowth Economics | 19.0 | 73 | 2 | Potentially Adequate |
| 6 | Market Socialism | 16.5 | 63 | 2 | Potentially Adequate |
| 7 | MMT + Job Guarantee | 15.5 | 60 | 3 | Partially Adequate |
| 8 | Mutual Credit / LETS | 14.5 | 56 | 3 | Partially Adequate |
| 8 | Ostrom-Style Commons Governance | 14.5 | 56 | 3 | Partially Adequate |
| 8 | Universal Basic Income | 14.5 | 56 | 7 | Structurally Inadequate |
| 11 | Sovereign Wealth Fund Statism | 14.0 | 54 | 3 | Partially Adequate |
| 11 | State Capitalism / Singapore | 14.0 | 54 | 4 | Partially Adequate |
| 13 | Georgism / Land Value Tax | 13.5 | 52 | 2 | Potentially Adequate |
| 13 | **Islamic Finance / Profit-Sharing Banking** | 13.5 | 52 | 5 | Partially Adequate |
| 13 | Universal Basic Services | 13.5 | 52 | 3 | Partially Adequate |
| 16 | Fully Automated Luxury Communism | 13.0 | 50 | 10 | Structurally Inadequate |
| 17 | Doughnut Economics | 11.5 | 44 | 8 | Structurally Inadequate |
| 18 | Status Quo Market Capitalism | 10.5 | 40 | 9 | Structurally Inadequate |
| 19 | Centrally Planned Socialism | 10.0 | 38 | 12 | Structurally Inadequate |
| 19 | Stakeholder Capitalism | 10.0 | 38 | 9 | Structurally Inadequate |
| 19 | State Capitalism / China | 10.0 | 38 | 8 | Structurally Inadequate |
| 22 | State Capitalism / Qatar | 9.0 | 35 | 10 | Structurally Inadequate |
| 23 | Libertarian Minarchism | 8.0 | 31 | 15 | Structurally Inadequate |
<!-- END GENERATED:corpus -->

Ranks are competition ranks; "=" in other scoring documents and repeated
rank numbers here both mark a shared total. This entry's row is in bold.

**Findings (all script-checked):**

- **An exact three-way tie at 13.5/26, across two tiers.** Islamic finance,
  Georgism / Land Value Tax, and Universal Basic Services all score exactly
  13.5/26 (52%), with 5, 2, and 3 structural failures respectively —
  Partially Adequate, Potentially Adequate, Partially Adequate. This
  supersedes the Georgism–UBS pair as the corpus's clearest illustration of
  the tier-versus-percentage distinction: three systems, one percentage,
  three failure counts, two tiers. It is worth putting in Section 10.3 of the
  Paper.
- **Best-in-corpus implementation viability, shared with the top-ranked
  system.** Domain 5 of 4.5/5 ties CCO-PTF-CIP-SZH for the highest in the
  corpus, and no other system reaches it. A mechanism with four decades of
  operation, a USD 3.88 trillion asset base, a constitutionally scheduled
  national transition, and demonstrated partial deployability is about as
  implementable as anything NEEC has scored. Its problem is not viability.
- **The second-widest viability-versus-ethics split in the corpus.** Domain
  5 at 4.5/5 sits against Domain 4 at 1.5/5, a 3.0-point gap; the Domain 4
  score is the sixth-lowest of the twenty-three systems (tied with
  Libertarian Minarchism). The other system at the top of Domain 5,
  CCO-PTF-CIP-SZH, scores 4.5 in Domain 4 as well. Only Status Quo Market
  Capitalism, at 4.0 against 0.5, has a wider gap (3.5), and it is the
  comparison the entry invites; the three state-capitalism entries follow
  at 2.5.
- **Not dominated by anything, including CCO-PTF-CIP-SZH.** The mechanism is
  one of the 11 entries CCO-PTF-CIP-SZH does not strictly dominate, and
  C5.5 is the sole reason: Islamic finance scores 1.0 on cultural
  adaptability where CCO-PTF-CIP-SZH scores 0.5, and it is the only criterion
  on which it scores higher. It **strictly dominates Stakeholder
  Capitalism** (higher on 6 criteria, lower on none), the corpus's only case
  of a Step 1b entry dominating one of the 13 legacy systems. The corpus
  holds **14** ordered strict-dominance pairs in all.
- **Against the market baseline.** It differs from Status Quo Market
  Capitalism on 8 criteria and is higher on 7 of them (C2.5, C3.1, C3.3,
  C3.4, C4.1, C4.5, C5.5), for a 3.0-point gain — a real improvement on the
  system it is layered onto, concentrated in resilience rather than in
  material security.
- **Against its tie partners.** It differs from Georgism on 10 criteria
  and from Universal Basic Services on 8, and neither dominates in either
  direction despite the identical totals.
- **Archetype.** This is the fourth member of archetype 1 (narrow
  single-mechanism systems) and the second **stock-like** member, after
  Sovereign Wealth Fund Statism. The two differ in who holds the corpus:
  households here, the state there. Their scores differ on 9 criteria, with
  Islamic finance higher on 4 (C1.3, C4.5, C5.2, C5.5).

---

## Final assessment

Profit-sharing banking is the corpus's clearest case of a system that is easy
to build and hard to make do what it was built for. Its implementation
viability is the highest NEEC has scored anywhere, tied with the framework's
own top-ranked entry; its ethical integrity is sixth-lowest of the
twenty-three. The gap between those two numbers is the whole finding.

The mechanism was designed to replace the creditor claim with a shared stake.
In operation it has largely reproduced the creditor claim in a compliant
wrapper — markup contracts on the asset side, smoothed market-benchmarked
returns on the liability side — while retaining two substantive protections
that are not merely formal: obligations cannot compound after default, and
the pure credit-trading chain is barred. Those are real, and they are why the
entry scores above Status Quo Market Capitalism on seven criteria. They are
also not what the design promised.

The most striking evidence for the gap is not from the mechanism's critics
but from its regulator. When a central bank has to put RM100 million of
matching funds behind a programme to encourage banks to use the contracts
that define the system, and convenes its scholars to discuss contracts
"beyond *tawarruq*," the divergence between design and practice has been
conceded by the institution best placed to know. The IFSB's own research
supplies the cause: the prudential capital treatment of *mudarabah* and
*musharakah* assets makes risk-sharing expensive, and banks respond to
prices. That is a fixable regulatory fact, not a fact about the contracts —
which is exactly why Reading A is worth keeping on the table.

What the mechanism cannot do, on any reading, is bear weight it was never
designed to carry. It has no unconditional provision (C2.2) and no
absolute-reduction ecological constraint (C4.2), the two failures that
survive every contestable call, and on every joint reading but Reading A it
has no answer to automation (C1.4). No other narrow single-mechanism entry in
this corpus fails all three. Scored as a financial-sector reform layered on a
market economy, it
is a competent one. Scored as an economic system, it is not one.

---

## Reviewer disclosure (per `NEEC_CONTRIBUTING.md` §2 / Appendix H.6)

- **Not independently cross-checked.** H.9 Step 6 is open, as for every Step
  1b entry. Given 16 flagged calls and a non-robust tier, this entry is a
  strong candidate for the D2 pilot replication alongside Singapore.
- **Evidence currency.** Malaysian figures are from BNM's Annual Report 2025;
  the global asset figure is IFSB's for 2024; the *tawarruq*-share figure is
  from end-2019 and is the most recent official proxy retrieved. A v2.x
  review should re-check C1.2a, C4.5, and C5.2 once i-CITA has a track record
  and Pakistan's 2028 deadline has passed or slipped.
- **Source-tier mix.** Primary and institutional sources carry the load: BNM,
  IFSB, IMF working papers, the World Bank, the Securities Commission
  Malaysia, and Cambridge University Press. Where a claim rests on a
  secondary source or on a literature review rather than on a primary
  statistic — the >70% debt-based figure, the microfinance and gender
  findings, the Iranian *mudarabah* characterisation — the text says so.
- **Disclosed evidence conflicts.** Two: the share of unbanked adults citing
  religious reasons (4%–25% across World Bank sources, under C1.1), and PSIA
  reserve disclosure (IMF 15/120 against IFSB WP-10, under C3.5). No score
  rests on resolving the first; C3.5 rests on the second and is flagged.
- **Normative-commitment disclosure.** C2.4 and C4.4 follow partly from
  NEEC's stated commitments to democratic participation and diffused power
  (Paper Section 2.2). Readers who reject those commitments should contest
  them at the level of the criteria, through Appendix I.
- **Religious neutrality.** C4.3 is the only criterion whose score could turn
  on religious law rather than economic structure; the scope decision made
  there is stated in the criterion rather than left implicit. No criterion in
  this evaluation scores a religion.

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
  "key": "Islamic Finance / Profit-Sharing Banking",
  "code": "IF",
  "display_name": "Islamic Finance / Profit-Sharing Banking",
  "record": {"documents": ["NEEC_IslamicFinance_scoring_scratch.md"], "scored": "Session 22, natively on the v2 structure", "structure": "native-v2"},
  "scope": {"class": "mechanism", "basis": "stated", "population": "Score the mechanism, not a country.", "source": {"file": "NEEC_Ostrom_Commons_scoring_scratch.md", "locator": "document", "phrase": "Commons governance joins archetype 1, narrow single-mechanism systems, as its fifth member after Georgism, Mutual Credit / LETS, Sovereign Wealth Fund Statism and Islamic finance."}},
  "vector": {
    "C1.1": 0.5, "C1.2a": 0.5, "C1.2b": 0.0, "C1.3": 0.5, "C1.4": 0.0, "C1.5": 0.5,
    "C2.1": 0.5, "C2.2": 0.0, "C2.3": 0.5, "C2.4": 0.5, "C2.5": 1.0,
    "C3.1": 0.5, "C3.2": 0.5, "C3.3": 0.5, "C3.4": 1.0, "C3.5": 0.5,
    "C4.1": 0.5, "C4.2": 0.0, "C4.3": 0.5, "C4.4": 0.0, "C4.5": 0.5,
    "C5.1": 1.0, "C5.2": 1.0, "C5.3": 1.0, "C5.4": 0.5, "C5.5": 1.0
  },
  "summary": {"D1": 2.0, "D2": 2.5, "D3": 3.0, "D4": 1.5, "D5": 4.5, "total": 13.5, "failures": 5, "tier": "Partially Adequate"},
  "flags": [
    {"criterion": "C1.1", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C1.2a", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C1.2b", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C1.4", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C1.5", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C2.4", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C2.5", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C3.4", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C3.5", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C4.1", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C4.3", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C4.4", "scored": 0.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C4.5", "scored": 0.5, "alternatives": [0.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C5.2", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C5.4", "scored": 0.5, "alternatives": [1.0], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}},
    {"criterion": "C5.5", "scored": 1.0, "alternatives": [0.5], "basis": "register", "reading": null, "tracks": null, "source": {"file": "verify_islamicfinance.py", "locator": "FLAGGED"}}
  ],
  "joint_readings": [
    {"id": "A", "label": "as designed", "basis": "stated", "resolve": {"C1.2a": 1.0, "C1.2b": 0.5, "C1.4": 0.5, "C4.4": 0.5}, "result": {"total": 15.5, "failures": 2, "tier": "Potentially Adequate"}},
    {"id": "B", "label": "as practised, scored here", "basis": "scored", "resolve": {}, "result": {"total": 13.5, "failures": 5, "tier": "Partially Adequate"}},
    {"id": "C", "label": "strict form-over-substance", "basis": "stated", "resolve": {"C1.1": 0.0, "C1.5": 0.0, "C2.4": 0.0, "C3.5": 0.0, "C4.1": 0.0, "C4.5": 0.0}, "result": {"total": 10.5, "failures": 11, "tier": "Structurally Inadequate"}}
  ],
  "scenarios": [
    {"id": "social-finance-layer", "label": "the Islamic social-finance layer (zakat, waqf, takaful) counted in", "kind": "scope", "changes": {"C1.1": 1.0, "C1.2b": 0.5}, "result": {"total": 14.5, "failures": 4, "tier": "Partially Adequate"}}
  ]
}
```
<!-- /NEEC-SUMMARY-BLOCK -->
