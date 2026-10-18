# C2.1 clause 1: Gallup World Poll "freedom to make life choices" (cached Session 70)

Cached: `whr26_statistical_appendix.pdf` (files.worldhappiness.report, the World Happiness Report 2026's statistical
appendix, fetched 2026-10-18), which defines the measure (line 67 of the text extract: "Freedom to make life choices
is the national average of responses to the GWP [Gallup World Poll] question...") and gives the regression
coefficients the Report's happiness model attaches to it, but not a simple country-by-country raw score table for
the four configured economies.

The raw national average by country and year is published through `data.worldhappiness.report`'s interactive table,
whose API (`/api/data`) requires a signed request token ("Invalid or expired request token", HTTP 403 on an
unauthenticated POST, tested 2026-10-18) and is not reachable by a plain fetch. `WHR26_Data_Figure_2.1.xlsx` (also
cached locally during this session, not copied into the repository since it does not carry the raw indicator: its
"Explained by: Freedom to make life choices" column is each country's regression-decomposed *contribution* to the
happiness score, not the raw 0-1 survey share the criterion's measurement text asks for) does not substitute for the
country table either.

Partial figures found by search (2026-10-18, not independently verified against the primary table): the United
States ranks 115th of 140 countries on the freedom factor with 71% reporting satisfaction with their freedom to
choose (a 2025-edition figure, one year before the cached 2026 appendix); China ranks 65th on the same factor; no
figure was found for Singapore or Qatar. These are leads for session 75, not readings.

A future session should either obtain the data app's request token (likely issued client-side by the page's own
JavaScript) or use the Statistical Appendix's regression tables together with the Figure 2.1 decomposition and the
Life Ladder score to back out the raw factor, which this session did not attempt.
