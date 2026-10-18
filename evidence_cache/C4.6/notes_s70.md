# C4.6 clauses 1-2: mortality series and liability law (cached Session 70)

## Clause 1: pollution mortality, 20-year window

Cached from the WHO Global Health Observatory API (ghoapi.azureedge.net, fetched 2026-10-18; raw JSON in this
directory):

- `SDGPOISON.json` (indicator SDGPOISON, unintentional-poisoning death rate, age-standardized, per 100,000): a full
  2000-2023 panel (24 years) for all four configured economies (CHN, QAT, SGP, USA). This indicator alone supports a
  20-year comparison.
- `SDGWSHBOD.json` (indicator SDGWSHBOD, unsafe WASH services death rate, SDG 3.9.2): only 2019 is populated for
  these four economies (12 rows total, one year). No 20-year comparison is possible from this series alone.
- `SDGAIRBOD.json`: the indicator code implied by the SDG 3.9.1 name returns zero rows; it appears retired or
  renamed.
- `air42.json` (indicator AIR_42, ambient air pollution attributable death rate, age-standardized): only 2021 is
  populated for these four economies. No 20-year comparison.

This confirms, with the actual API responses now cached (rather than asserted from a prior session's unsuccessful
attempt), the finding already in STATE.md ("the WHO SDG series is short... clause 1 is not shown for any economy"):
of the three SDG sub-indicators the clause sums, only unintentional poisoning has a usable 20-year series; ambient
and household air pollution and unsafe-WASH mortality are each pinned to a single recent year in the GHO API as
queried this session. A session with more time could: (a) query the GHO API's other air-pollution indicator codes
(AIR_4, AIR_41, AIR_43, etc., listed in `who_air.json`-style queries) for a longer run, since AIR_42 is not the
only candidate; (b) try the IHME Global Burden of Disease results tool, which this session found reachable
(vizhub.healthdata.org, ghdx.healthdata.org and www.healthdata.org all returned HTTP 200/302, unlike the "IHME series
was unreachable" of Session 65) but whose query API was not explored this session for lack of time.

## Clause 2: liability law

No single comprehensive source was found for all four economies this session. Leads only (not primary text):

- **United States:** federal tort and product-liability law is state-law-based (no single federal statute); search
  turned up no on-point citation this session beyond the general common-law background already known from the
  corpus's other liability discussions (C1.2b, C4.5).
- **China:** the Tort Liability Law (2009, now folded into the 2021 Civil Code's Book VII on tort liability) states
  strict liability for environmental polluters (Article 1229 of the 2021 Civil Code, formerly Tort Liability Law
  Article 65): "compliance with environmental rules is not a defense" (search summary, lehmanlaw.com and others,
  2026-10-18; statutory text not fetched). Standing for environmental public-interest litigation was expanded by
  2017 Civil Procedure Law amendments to authorized social organizations and procuratorates; a named claim decided
  and paid within a 20-year window (as the clause requires) was not identified this session.
- **Singapore, Qatar:** not searched this session beyond the C2.6 note above; open for session 77.

This is a lead list only, in the same spirit as C2.6's `law_in_force_notes_s70.md`.
