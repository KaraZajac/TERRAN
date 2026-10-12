# Schedule 2 — Settings

*Generated from [numbers.yaml](numbers.yaml) by `make schedules`: edit the YAML, not this file · [All Schedules](README.md) · [The Terran Charter](../CHARTER.md)*

These numbers tune how the Commonwealth works. A planetary act that is not urgent may set each one anywhere within its allowed range. Moving a range, or setting a number outside it, is a change made only as the Articles change (Part V.6). Where a setting has no value yet, the first act that sets it must stay within its range, and a setting with no range yet needs a change made as the Articles change. A change to the voting age takes effect only after the next yearly voting day. A change to the size or term of a body applies from its next regular draw or appointment, and never shortens or lengthens a term being served. The values, the ranges and these rules bind; the reasons explain.

## Article 1 — The Culture of Enough

| Number | Value | Allowed range | Used in | Why |
| --- | --- | --- | --- | --- |
| <a id="wealth-tax-free"></a>Wealth free of wealth tax | $2 million | $1.5 million to $3.4 million | 1.5 | Sits between the thresholds of France's old wealth tax, about $1.46 million per household, and Spain's solidarity tax, about $3.4 million per person [oecd/2018_net-wealth-taxes; spain/2022_ley-38-2022]. Dutch respondents put a "riches line" at €1 million to €3 million [robeyns-et-al/2021_riches-line]. |
| <a id="wealth-tax-start"></a>Starting rate of the wealth tax | 1% | 0.2% to 2.2% | 1.5 | Starting rates in the research run from the 0.2% first band of Spain's state scale to Denmark's former 2.2%. Norway's is 1%, and Spain's solidarity tax starts at 1.7%. The UK's Wealth Tax Commission called 1% high by international standards [wtc/2020_final-report]. How fast the rate rises matters more than where it starts. |
| <a id="spending-cap"></a>Cap on a terran's spending on a vote | Not yet set | — | 1.11 | A cap must leave room to speak: Strasbourg found a £5 limit on one campaigner disproportionate [echr/1998_bowman-v-uk]. |
| <a id="pay-ratio-tax"></a>Where the steep tax on pay starts | 50 times the lowest pay | 50 to 75 times | 1.12 | Every pay-ratio tax in the research starts between 50 and 100 times median pay, such as US bill S. 2818 at 50 and Portland at 100 [us-senate/2025_s2818-tax-excessive-ceo-pay; portland/2026_city-code-7-02-500]. Dividing by the lowest pay makes 50 times stricter than any of them. The range stays below today's cap of 100 times; if the cap falls, this range must fall with it. |
| <a id="pay-averaging"></a>Years over which the highest pay is averaged | Not yet set | three to five years | 1.12 | Averaging smooths one-off awards, so one unusual year doesn't set the ratio. US bill S. 2818 averages over five years [us-senate/2025_s2818-tax-excessive-ceo-pay]. |
| <a id="larger-organization"></a>Workers at which an organization counts as larger | Not yet set | 50 to 500 workers, counted across a group | 1.14 | Laws that give workers a third of the board apply it above 50 workers in Norway and above 500 in Germany [etui/2026_norway; germany/2004_drittelbeteiligungsgesetz]. Counting across a group stops a firm splitting itself to avoid the line. Unions and nonprofits are organizations too, so the line reaches them. |

## Article 2 — Working Together

| Number | Value | Allowed range | Used in | Why |
| --- | --- | --- | --- | --- |
| <a id="transparency"></a>Wealth or power above which more is open to view | Not yet set | — | 2.6 | No evidence for a threshold. On rough estimates, about 23 million adults hold more than $2 million, and 2.9 million more than $10 million, so either line could serve. The EU Court of Justice struck down general public access to ownership registers [cjeu/2022_wm-sovim]. |
| <a id="coc-size"></a>Council of Communities | 200 delegates | 150 to 250 delegates | 2.10 | The Earth Constitution's House of Counsellors has 200 [wcpa/1977_earth-constitution]. Planetary bodies with a seat for each member are of the same order: the ITU has 194 member states, and the Montreal Protocol 198 parties [itu/2026_about; untc/2026_montreal-protocol-status]. |
| <a id="coc-term"></a>A delegate's longest term | four years | two to four years | 2.10 | Switzerland's Federal Council serves four years. Delegates can also be recalled, as the IETF can recall its leaders by petition [ietf/2020_rfc-8713]. |

## Article 3 — How Terrans Decide

| Number | Value | Allowed range | Used in | Why |
| --- | --- | --- | --- | --- |
| <a id="answer-signatures"></a>Signatures that earn a reasoned answer | 100,000 | 100,000 to 500,000 | 3.1 | The UK answers a petition at 10,000 signatures and considers it for debate at 100,000, and Taiwan's Join platform answers at 5,000 [uk-parliament/2026_petitions-help; bertelsmann/2022_taiwan-join-vtaiwan]. Among eight billion people, 100,000 is still a low bar. The research advises a response at a low threshold and deliberation at a higher one, so the range stays well below the million that reaches an assembly. |
| <a id="answer-days"></a>Deadline for that answer | 90 days | 30 to 90 days | 3.1 | No precedent in the research: the UK and Taiwan promise dated answers, and the notes record no deadline. |
| <a id="voting-age"></a>Voting age | Not yet set | 16 to 18 | 3.1, 3.5, 5.3 | The research counts adults from about 18, while Paris's citizens' assembly and the European Citizens' Panels take people from 16 ([sortition at scale](../research/sortition-at-scale.md)). Every share of terrans in these Schedules moves with it, so its range is fixed in advance. |
| <a id="assembly-size"></a>Each standing assembly, and the Budget Assembly | 450 terrans | 300 to 600 terrans | 3.3 | Guerrero's Lottocracy (2024) proposes single-issue bodies of 450 [greene/2026_review-guerrero-lottocracy]. At 450, an assembly's split matches all terrans' within about 4.6 points, 19 times in 20. |
| <a id="agenda-size"></a>Agenda Council | 300 terrans | 150 to 450 terrans | 3.3 | Guerrero's 2021 design uses bodies of 300 [guerrero/2021_single-issue-legislatures], accurate within about 5.7 points. Whoever staffs and briefs it shapes the agenda, so 3.3 rotates them. |
| <a id="assembly-term"></a>Term on an assembly or the Agenda Council | three years | two to three years | 3.3 | Guerrero's 2021 design uses three-year terms [guerrero/2021_single-issue-legislatures], Bouricius about three [bouricius/2013_multi-body-sortition], and Gastil and Wright two or five [gastil/2018_legislature-by-lot]. Ostbelgien's decree set eighteen months, though at times too few former members volunteered to keep its rotation. |
| <a id="assembly-rotation"></a>How often a share of members is replaced | six months | six to twelve months | 3.3 | Guerrero's 2021 design replaces a third of each body every year [guerrero/2021_single-issue-legislatures]. Ostbelgien's decree set a third every six months, though in practice the rhythm slipped [pdg/2025_buergerdialog-evaluation-2019-2024]. |
| <a id="rejected-wait"></a>Bar on an act rejected twice | two years | two to three years | 3.4, 3 (diagram) | No precedent in the research. The nearest is Switzerland, where a refused urgent act can't be renewed. A shorter bar would let an assembly resubmit an act until some panel passes it. |

## Article 5 — The Stewards

| Number | Value | Allowed range | Used in | Why |
| --- | --- | --- | --- | --- |
| <a id="oversight-size"></a>Oversight Council | 150 terrans | 150 to 300 terrans | 5.2 | France's climate convention had 150 members, and French majorities backed a permanent assembly of 150 with a veto ([sortition at scale](../research/sortition-at-scale.md)). |
| <a id="oversight-term"></a>Oversight Council term | two years | eighteen months to two years | 5.2 | Ostbelgien's decree set eighteen-month terms for its council, though in practice its rotation slipped [pdg/2025_buergerdialog-evaluation-2019-2024]. Two years spans a full round of Steward appointments. |
| <a id="rule-panel"></a>Panel reviewing a draft rule | 200 terrans | 150 to 450 terrans | 5.3 | The EU Conference's citizens' panels had 200 members each ([sortition at scale](../research/sortition-at-scale.md)). The research advises reviewing a sample of delegated rules rather than convening a jury for each, while 5.3 gives every draft a panel; the open questions ask which is meant. |
| <a id="objection-window"></a>Objection window for a draft rule | 60 days | 28 to 100 days | 5.3 | In 2024 the EU put 108 draft rules out for four weeks' comment [european-commission/2025_comitology-report-2024], and Montreal Protocol adjustments bind six months after they circulate [unep/1987_montreal-protocol-article-2]. A window counts silence as consent, which fails when absent people are counted as agreeing. |

## Article 6 — Emergencies

| Number | Value | Allowed range | Used in | Why |
| --- | --- | --- | --- | --- |
| <a id="emergency-pool"></a>Emergency pool, drawn each year | 20,000 terrans | 20,000 to 50,000 terrans | 6.1 | Athens drew a yearly pool of 6,000 jurors and a panel from it for each case [bouricius/2013_multi-body-sortition]. Each panel is fresh, the longest emergency needs six panels of 1,000, and continuity panels draw on the pool too, so 20,000 leaves room for more than one emergency in a year. |
