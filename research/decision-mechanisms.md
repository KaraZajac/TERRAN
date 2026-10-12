# Mechanisms for deciding at planetary scale

*Research note · planetary government, round 2 · first pass, 11 October 2026 · compiled by Claude, not yet reviewed by Kara*

No tested mechanism lets eight billion people decide every planetary question, and Kara has now ruled that design out. The evidence favours a division of labour: random samples deliberate and draft, a universal vote survives as a rare veto, and markets only forecast. Its best-evidenced parts (Swiss referendums, Mongolia's mandatory deliberative polls, Brazil's participatory budgets) all sit on elected bodies. Newer tools (liquid delegation, quadratic voting, futarchy, AI mediation) have thin or failed records, and most need verified unique identities.

## What the Charter says now

- **VII.2–3.** Every terran votes with a digital identity held "from birth"; "Every terran votes on the questions before the Commonwealth".
- **VII.4.** Decisions sit "as close as possible" to those affected; planetary matters, "including the ceiling", go to all.
- **VIII.1–4.** A backed proposal goes to online mapping, then to an assembly drawn by lot that writes the ballot. Every terran votes; a majority decides.
- **VIII.7.** A Council of Stewards, "elected by all terrans", administers.
- **IV.5, X.4, XI.3.** Tax rates are set "by vote". A proposal failing the long-view test waits a year for a second vote. Amendments need two-thirds twice, a year apart.
- **Gaps.** No cap on questions, no delegation, no budgeting or forecasting method, no emergency procedure.

**Design target for this round.** Kara called a universal vote on every question "probably an impossible requirement". She wants something more modern than elections and representative assemblies. This note asks which mechanisms could take over each job the universal vote does now. Continuous-participation platforms, e-petitions, open-source governance and rules as code belong to a separate strand.

## Replacing the universal vote: the options by purpose

In the draft, the universal vote does six jobs. It sets the agenda (VIII.1), legitimises drafting (VIII.3–4) and decides (VIII.4). It also sets tax rates (IV.5), weighs the future (X.4) and checks the Stewards by electing them (VIII.7). The table pairs each job with the best-evidenced replacement. It adds one job votes cannot do: measuring what people conclude after deliberating. Grades are defined with the matrix at the end.

| Job | Best-evidenced replacement | Record | Grade | Main failure mode |
|---|---|---|---|---|
| Agenda-setting | Lot-chosen screening council; opinion mapping as input | Mongolia's Deliberative Council screened about 1,100 suggestions in 2023 [stanford-ddl/2026_mongolia-constitutional-amendment]; Ostbelgien ([round 1](deliberation.md)) | B | Whoever staffs and briefs it shapes the agenda |
| Drafting | Assembly drawn by lot, with AI mediation as an aid | Ireland and Oregon ([round 1](deliberation.md)); AI mediation in the lab [tessler/2024_ai-common-ground] | B / C | Staff, facilitators and models shape the text |
| Considered judgment | Deliberative poll of hundreds to thousands | Required before Mongolian amendments since 2017 [stanford-ddl/2026_mongolia-constitutional-amendment]; over 6,300 people in 32 countries in 2022 [cddrl/2023_metaverse-community-forum] | B (advisory) | Briefing bias; effects not fully explained |
| Deciding | A binding sample decision, with a universal vote on demand | Components only: the Swiss optional referendum and deliberative polls, never combined | C | Legitimacy falls if outputs are ignored; known members can be pressured |
| Budgeting | Participatory budgeting locally; quadratic funding for small grant pools | 11,690–11,825 participatory budgets in 2019 [dias/2019_participatory-budgeting-world-atlas]; Gitcoin, $60M+ since 2019 [gitcoin/2024_state-of-public-goods-funding] | B / C | Executive discretion; fake identities |
| Forecasting | Prediction markets as advice | Beat 964 polls 74% of the time, 1988–2004 [berg/2008_prediction-market-accuracy] | B | Whales and capture of the resolution step |
| Oversight | Citizen veto by signatures | Switzerland: most acts take effect without a vote [switzerland-bk/2026_referenden] | A (on a parliament) | Untested on bodies chosen by lot |
| Not recommended | Token voting; binding futarchy; uncapped delegation | DAO concentration [feichtinger/2023_hidden-shortcomings-daos]; Optimism's 2025 test [optimism/2025_futarchy-v1-findings] | D | Plutocracy, gaming, concentration |

One caution runs through the table. Switzerland's veto, Mongolia's polls and Brazil's budgets all feed or check elected officials. Swapping the elected body for a lot-chosen one has no track record at any scale.

Replacing the universal vote also changes who takes part. In Geneva, more than 90% of voters took part at least once in 20 votes [swissinfo/2016_most-swiss-do-vote]. A sample-based system reaches very few people directly.

| Design (estimates) | Seats a year | Chance per adult per year | Chance over 60 adult years |
|---|---|---|---|
| 9 questions, a 1,000-member sample each | 9,000 | 1 in 680,889 | 1 in 11,348 |
| 50 questions, 10,000-member samples | 500,000 | 1 in 12,256 | about 1 in 204 |
| 1,000 samples of 1,000, all levels | 1,000,000 | 1 in 6,128 | about 1 in 102 |

Own arithmetic: of 8,140,897,523 people in 2024 [worldbank/2026_wdi-population], 24.7% were aged 0–14 [worldbank/2026_wdi-population-0-14]. That leaves about 6.13 billion aged 15 or over. The estimates ignore refusals and repeat selection.

**Design implication:** Replace the universal vote job by job, not with one new institution. A sample-based design trades mass participation for representativeness, so it needs visible fairness, published methods and a universal veto to stay legitimate.

## Direct votes and the attention budget

Swiss federal votes show what a mass electorate will bear. Mean turnout below is the average across questions [swissvotes/2026_dataset].

| Period | Questions | Voting days | Questions a year | Mean turnout |
|---|---|---|---|---|
| 1950–1959 | 45 | 32 | 4.5 | 50.8% |
| 1970–1979 | 86 | 32 | 8.6 | 42.2% |
| 1990–1999 | 100 | 29 | 10.0 | 41.7% |
| 2010–2019 | 83 | 31 | 8.3 | 46.9% |
| 2020–Sep 2026 | 63 | 21 | 9.3 | 50.7% |

From 2016 to 2025, the count ranged from 3 to 13 questions a year. In 2026, 10 questions were decided on three days by 27 September, with four more set for 29 November [swissvotes/2026_dataset].

Most Swiss vote selectively. A study linking official turnout records to survey data found selective voters "constitute the bulk of the electorate" [sciarini/2015_selective-participation]. A commune study tracking 15 ballots found most citizens take part only selectively [dermont/2016_taking-turns-ballot-box]. Only about 10% of Geneva voters skipped every vote over five years [swissinfo/2016_most-swiss-do-vote].

The official post-vote surveys show who drops out, and why:

- **June 2021 (3,057 respondents).** Turnout was 93% among the very interested and 10% among the not at all interested. It was 48% at ages 30–39 and 72% at 60–69. Of non-voters, 29% forgot and 11% found the topics too complicated. Between 19% and 27% of voters found a question rather hard to understand [gfs-bern/2021_vox-june-2021].
- **November 2025 (3,349 respondents).** The official booklet was used by 88% of voters. For each question, 81–82% found it rather easy to understand. Of non-voters, 31% forgot and 8% found the topics too complicated [gfs-bern/2026_vox-november-2025]. Turnout was 42.9% [swissvotes/2026_dataset].

The 13 June 2021 booklet ran to 144 pages for five questions. Each question had a two-page "In Kürze" (in brief) summary at the front [swiss-federal-council/2021_voting-booklet-june-2021]. In California, voters facing five insurance initiatives used shortcuts that let the badly informed vote like the well informed [lupia/1994_shortcuts-versus-encyclopedias]. The surveys above measure self-reported difficulty, not tested knowledge.

California shows the cost of volume. Between 1912 and 1 July 2025, 2,152 initiatives were cleared to circulate and 401 qualified. Of the 396 on a ballot, 140 passed (35.35%) [california-sos/2025_initiatives-summary-data]. The 3 November 2026 ballot carries 14 statewide measures [california-sos/2026_qualified-ballot-measures]. Long ballots carry a cost. One study compared the same contest at different ballot positions: facing more decisions first raised abstention and status-quo votes. Without this choice fatigue, abstentions would fall 8% and 6% of the propositions studied would have passed [augenblick-nicholson/2016_choice-fatigue]. In Hesse, turnout fell when a second election followed soon after a first, more so for less important contests [garmann/2017_election-frequency-fatigue].

Switzerland saves attention with a veto. Federal acts face a vote only if 50,000 voters or eight cantons ask within 100 days [switzerland/1999_federal-constitution]. The Federal Chancellery says the great majority of acts take effect without a popular vote [switzerland-bk/2026_referenden]. There were 39 such votes in 2016–2025 [swissvotes/2026_dataset]. Tax laws face the same veto. Voters rejected higher child deductions in 2020 (36.8% yes) and accepted individual taxation in March 2026 (54.3%) [swissvotes/2026_dataset]. The threshold is 0.89% of the 5,591,446 Swiss voters of March 2024 [swissvotes/2026_dataset]. The same share of 6.13 billion people aged 15 or over is about 55 million signatures (estimate).

The Swiss pattern also covers emergencies. Urgent acts can take effect at once but must be time-limited. If a referendum is requested, they lapse after one year unless voters approve; a rejected act cannot be renewed [switzerland/1999_federal-constitution]. Parliament passed the COVID-19 Act 44 days after the government's message, on 25 September 2020. Opponents gathered 90,789 signatures in 98 days, and voters approved it with 60.2% in June 2021. Its second revision took effect on 20 March 2021, the day after passage, and won 62.0% that November [swissvotes/2026_dataset]. Taking effect that fast implies it was declared urgent (my inference from Art. 165).

**Design implication:** If a universal vote survives, ration it to a few fixed days, a cap on questions per day and short official summaries. Make it a veto that citizens trigger, not the default route.

## Random samples that deliberate

A Deliberative Poll surveys a random sample, gathers it for a weekend with balanced briefings and competing experts, then surveys it again [stanford-ddl/2026_what-is-deliberative-polling]. Stanford reports more than 150 in more than 50 countries and jurisdictions [stanford-ddl/2026_what-is-deliberative-polling].

- **America in One Room (2019).** 526 registered voters deliberated over a long weekend; a control group of 844 did not. Republican support for cutting refugee numbers fell from 65% to 34%. Democratic support for a $15 minimum wage fell from 82% to 59% [fishkin/2021_america-in-one-room]. Despite balanced materials, the authors note opinion "shifted markedly in a direction more sympathetic to the plight of the undocumented" [fishkin/2021_america-in-one-room].
- **Mechanisms unclear.** In a 2009 EU-wide poll, deliberators changed views against a control group. Five explanations were tested and "none is satisfactory" [sanders/2012_deliberative-polling-eu].
- **Global scale.** In December 2022, more than 6,300 people from 32 countries deliberated in 23 languages by the lab's own account (its final report says 19; noted on review) on 56 proposals. Fourteen survey firms recruited them, and a control group answered the same questions [cddrl/2023_metaverse-community-forum]. In October 2023, 1,545 people in four countries deliberated on chatbots [stanford-ddl/2026_meta-forum-generative-ai]. In November 2025, 503 people in the United States and India advised six firms [cddrl/2026_industry-wide-forum-ai-agents].
- **A required step.** Since 2017, Mongolian law requires a Deliberative Poll before parliament considers a constitutional amendment. The first, in April 2017, had 669 participants [stanford-ddl/2017_mongolia-first-national-deliberative-poll]. In February 2023, nearly 800 people, sampled by the National Statistical Office, backed enlarging parliament (82% of those with a view). Parliament then grew from 76 to 126 seats [stanford-ddl/2026_mongolia-constitutional-amendment]. These accounts come from the lab that ran the polls.

Online platforms cut the cost. As of fall 2026, Stanford's platform has logged more than 50,000 users and 100,000 hours, in more than 40 languages [stanford-ddl/2026_online-deliberation-platform]. That is about two hours per user (estimate). Reaching a sample takes a wide net. Taiwan texted a survey to 200,000 numbers in 2024 [moda/2024_information-integrity-meeting] to seat 447 deliberators [stanford-ddl/2026_taiwan-information-integrity-poll]. That is 0.22% of those texted (estimate); refusal rates were not published in what I read.

| Cost and scale | Figure | Source |
|---|---|---|
| OECD processes, 1986–2019 | €13,000 to €1.8 million each | [oecd/2020_catching-the-deliberative-wave] |
| Global Assembly, 2021 | US$972,247; 68 hours over 12 weeks | [global-assembly/2022_report-2021] |
| Per seat and per member-hour | About US$9,700 per seat; about US$146 per hour (estimate) | Own arithmetic, 100 seats and 98 × 68 hours |
| Precision of a simple random sample | ±3.1 points at 1,000; ±1.0 at 10,000 (estimate) | Own arithmetic, 95% confidence, p = 0.5 |

Legitimacy hinges on follow-through. In an Irish experiment (N = 1,309), mini-publics raised perceived legitimacy mainly when their recommendations were honoured. It made no difference whether representatives or a referendum overturned them [germann/2024_scaling-up-mini-publics]. In Northern Ireland, the public backed decisions by a citizens' assembly even when they disagreed. Elected politicians opposed giving an assembly decision power [garry/2021_citizens-assemblies-northern-ireland].

**Design implication:** Random samples are the strongest replacement for mass votes in drafting and considered judgment. No sample has yet bound a whole polity, so binding power would need audited recruitment, published briefings and a universal veto behind it. Lot-chosen legislatures are covered in [sortition at scale](sortition-at-scale.md).

## Delegation (liquid democracy)

The theory is less favourable than the pitch. Even if voters delegate only to better-informed voters, local delegation cannot guarantee better decisions than direct voting [kahng/2018_liquid-democracy-algorithmic]. In two experiments, delegation rates were "unexpectedly high", and delegation did worse than both universal voting and abstention [campbell/2022_liquid-democracy-experiments].

| Case | Scale | What happened |
|---|---|---|
| Germany's Pirate Party, LiquidFeedback, 2010–2013 | 13,836 users (January 2015), against 24,438 members | 499,009 votes on 6,517 initiatives; the median user voted 8 times; 54 voted over 1,000 times. Inequality of delegations rose, though super-voters mostly sided with the majority [kling/2015_liquidfeedback-super-voters] |
| Same, February 2015 | 322 active of 5,380 voting members (6.0%) | A critic's count from party data [eisel/2015_liquidfriesland-am-ende] |
| LiquidFriesland, a German district, 2012–2015 | 583 registered | 382 took part at least once; 30 citizens wrote all 76 citizen initiatives [friesland/2015_liquidfriesland-evaluation]. A critic counts over 80,000 eligible [eisel/2015_liquidfriesland-am-ende] |
| Google Votes, 2012–2015 | 15,000 employees, 87,000+ votes | 3.6% of votes were delegated; most votes concerned food [hardt-lopes/2015_google-votes] |
| DAO delegates (Compound, Uniswap, ENS), to 2022 | Three token-governed protocols | 8, 11 and 18 delegates could pass any vote. On Compound and Uniswap, under 10% of tokens voted on average [fritsch/2022_who-controls-daos] |

Delegation needs visibility, which costs secrecy. LiquidFeedback published every vote, "allowing the control of delegates at the expense of non-secret votes" [kling/2015_liquidfeedback-super-voters]. Its authors credit super-voters' restraint partly to "the social control in an enforced public voting" [kling/2015_liquidfeedback-super-voters]. Google's rule was "If I give you my vote, I can see what you do with it" [hardt-lopes/2015_google-votes]. Even advocates note "an unfortunate tendency to concentrate power often excessively" [weyl-tang/2024_plurality].

**Design implication:** Delegation's record is thin. Few used it where offered, and power concentrated where it was used heavily. Public delegate votes clash with VIII.5's secret ballot and invite vote-buying, so pilot it locally, with caps, before any wider role.

## Quadratic voting and funding

Quadratic voting lets people buy extra votes on issues they care about, at a cost that rises with the square of the votes [lalley-weyl/2018_quadratic-voting]. The authors call it "still-nascent" [lalley-weyl/2018_quadratic-voting]. Posner and Weyl's *Radical Markets* (2018) argues that one person, one vote "inhibits democracy" [posner-weyl/2018_radical-markets]. In simulations using California voters' views on four 2016 initiatives, it produced more minority wins and higher average welfare. It also produced more inefficient minority wins [casella-sanchez/2019_storable-votes-quadratic-voting].

Colorado is the main public-sector case:

- **2019.** More than 100 bills sought over $120 million from a $40 million pot. House Democrats ranked them by anonymous quadratic voting, and more than 40 bills were funded. Leaders still overrode the ranking for some bills [colorado-sun/2019_quadratic-voting-budget].
- **2024.** In January, a judge ruled the secret ballot broke the state's open meetings law [colorado-sun/2024_quadratic-voting-ruling]. The method had run for five budget cycles. In April, leaders said it was "no longer an option" and switched to a public form. Republicans had declined to take part over the secrecy [colorado-politics/2024_funding-method-transparency].

Taiwan's Presidential Hackathon used quadratic voting for public input on its top 20 teams, by its advocates' account [weyl-tang/2024_plurality]. I found no participation figures.

Quadratic funding gives each project an amount proportional to the square of the sum of the square roots of its contributions [buterin-hitzig-weyl/2019_flexible-design-public-goods]. Many small donors therefore attract more matching than one large donor. Gitcoin reports more than $60 million distributed since 2019 [gitcoin/2024_state-of-public-goods-funding]. In its October–November 2025 round, about 1,286 donors gave $36,657 to 78 projects, matched by $300,000 [gitcoin/2026_gg24]. That is about $8 of matching per donated dollar (estimate).

Fake identities are the binding constraint. Gitcoin's own 2026 report says "If you can't verify that each participant is a unique human, you can't run a democratic funding mechanism" [gitcoin/2026_identity-binding-constraint]. Over half of a 17,000-donor round in June 2023 were chasing token airdrops. A July 2023 pilot drew fake-account attacks "almost immediately". Gitcoin's identity scoring cut suspicious activity by about 60%, leaving 40% of the attack surface uncovered [gitcoin/2026_identity-binding-constraint].

**Design implication:** These mechanisms capture intensity of preference, but none has a binding public record. Both fail without one verified identity per person, and Colorado shows secret ballots for officials do not survive. They fit prioritisation within fixed budgets, not lawmaking.

## AI-assisted deliberation

- **The Habermas Machine (2024).** 5,734 UK participants preferred its group statements to those of human mediators. Groups converged, and minority critiques were included. A virtual citizens' assembly replicated the results [tessler/2024_ai-common-ground]. The authors warn that participants must be representative and "prepared to contribute in good faith" [tessler/2024_ai-common-ground].
- **Polis with a language model (2023).** Summaries helped. The model's predictions of individual votes were "nearly perfectly statistically calibrated", which the authors call both an opportunity and a serious risk. It also voted more like one opinion group than the other (p = 1.86 × 10⁻⁴). The authors "reject as invalid" replacing participants with simulations [small/2023_llms-polis].
- **Anthropic's Collective Constitutional AI (2023).** About 1,000 Americans wrote 1,127 statements and cast 38,252 votes. Moderation left 275 statements; staff then merged duplicates into principles. Anthropic reports "a large number of subjective judgment calls" [anthropic/2023_collective-constitutional-ai].
- **Taiwan's alignment assemblies (2023–24).** Taiwan's digital ministry partnered with the Collective Intelligence Project from May 2023 [moda/2024_alignment-assemblies]. In March 2024, 447 citizens deliberated on AI and information integrity [stanford-ddl/2026_taiwan-information-integrity-poll]. Groups of 10 used AI-assisted facilitation. Audrey Tang, then the minister, said a coming anti-fraud act would adopt some measures [moda/2024_information-integrity-meeting].
- **Bowling Green, Kentucky (2025).** Nearly 4,000 online responses and more than a million votes were summarised by Google's Sensemaker [techbrew/2025_bowling-green-sensemaker]. In September 2026, Google said input from 8,000 residents shaped a 25-year plan. It now offers the tools to cities free [google/2026_sensemaking-ai-local-governments].

The risks are measured, not hypothetical. Chatbot conversations shifted candidate support by 2–3 points on a 0–100 scale, and about a third of the shift lasted a month. A maximally persuasive set-up moved opinions 16 points, but with less accuracy [vargiu-nai/2025_ai-chatbots-persuade-voters]. Co-writing with a feedback-tuned model made different people's essays more alike [padmakumar-he/2024_llm-writing-diversity]. As of October 2026, every use I found was advisory, and each ran on one company's model or one lab's platform.

**Design implication:** AI cuts the cost of mapping and summarising, where planetary scale bites hardest. It should never vote or speak for people. Models, prompts and moderation rules should be public and contestable, with more than one provider.

## Participatory budgeting

Porto Alegre began participatory budgeting in 1989 [jornal-do-comercio/2021_atlas-op-porto-alegre]. The Workers' Party held the mayoralty for 16 years. After its 2004 defeat, successors weakened the process through the executive's powers [melgar/2014_time-of-closure]. The last new demands were registered in 2016, and assemblies were cancelled in 2017. The 2020–21 world atlas speaks of the process's "prática extinção" (practical extinction) there [jornal-do-comercio/2021_atlas-op-porto-alegre].

The model spread widely. The 2019 atlas counted 11,690 to 11,825 processes, with contributions from 71 countries. It admits counts in up to three countries are overstated, and warns of "an abusive use of the term" [dias/2019_participatory-budgeting-world-atlas]. Portugal ran the first national one in 2017, and South Korea the second, using small groups representing the population. The Philippines' 2012–2016 programme reached over 1,500 cities and about 55,000 investments [dias/2019_participatory-budgeting-world-atlas]. After the pandemic, the 2020–21 atlas found about 4,000 active processes, down from 10,000. Of 8,800 it could check, about 55% had been suspended [jornal-do-comercio/2021_atlas-op-porto-alegre].

| Study | Data | Finding |
|---|---|---|
| Gonçalves (2014) | Brazilian municipalities, 1990–2004 | More spending on sanitation and health; lower infant mortality [goncalves/2014_pb-municipal-expenditures] |
| Touchton and Wampler (2014) | Brazil's largest cities, about 20 years | More health spending and civic groups, lower infant mortality; stronger over time [touchton-wampler/2014_improving-social-well-being] |
| Boulding and Wampler (2010) | Brazil's 220 largest cities | Slightly more on health and education; "little evidence" of better outcomes [boulding-wampler/2010_voice-votes-resources] |

Panels drawn by lot have also weighed whole budgets, not just a set-aside. In 2012, 36 randomly selected residents of Canada Bay, Sydney, met five times over 2.5 months on services and funding. The council agreed they would set service levels for its 2014–18 plan, subject to its final approval [oecd/2020_catching-the-deliberative-wave]. The OECD lists three more Australian cases from 2013–14, but gives no outcome data.

**Design implication:** Participatory budgeting is the best-evidenced budgeting tool, but it is local and depends on an executive that honours it. Its outcome evidence is mixed and mostly Brazilian, so it suits community budgets; whole-budget panels are the nearest model for planetary priorities.

## Prediction markets, futarchy and DAO governance

Hanson's futarchy would "vote on values, but bet on beliefs" [hanson/2013_vote-values-bet-beliefs]. Voters define a welfare measure, and a policy becomes law when markets clearly expect it to raise that measure. He argues manipulators act as noise traders and so do not reduce average accuracy [hanson/2013_vote-values-bet-beliefs].

- **Accuracy.** Iowa Electronic Markets beat 964 polls 74% of the time in 1988–2004 presidential races [berg/2008_prediction-market-accuracy]. Conditional markets reveal beliefs about correlations, but cannot by themselves separate correlation from causation [wolfers-zitzewitz/2004_prediction-markets].
- **Manipulation.** In 2012, one Intrade trader held over a third of all bets on Romney and lost close to $7 million. His orders held prices steady for hours on Election Day. The authors call this "suggestive of manipulation", perhaps to lift campaign morale [rothschild-sethi/2015_intrade-trading-strategies]. In March 2025, a $7 million Polymarket market resolved "Yes" on an event that had not happened. A large token holder had voted in its oracle. Polymarket called it "unprecedented" and refused refunds [theblock/2025_polymarket-uma-attack].
- **Futarchy in practice.** In 2025, Optimism let a play-money market pick five grants. Of the sign-ups, 4,122 suspected bots were removed, leaving 430 forecasters. Its picks gained about $32.5 million more in deposits than the council's, driven by one outlier. Its forecasts were about $200 million too high. Optimism warns decision markets "may incentivize participating projects to game outcomes" [optimism/2025_futarchy-v1-findings]. In late 2025, Gitcoin allocated $350,000 using prediction markets to evaluate 98 code repositories [gitcoin/2026_gg24].
- **Token voting.** The DAO raised about 12 million ether (about $150 million) in 2016. On 17 June an attacker diverted about 3.6 million. A hard fork on 20 July moved all its funds, the diverted ether included, to a recovery address. Its "Curators" held "considerable power" [sec/2017_the-dao-report]. In 17 of 21 DAOs studied, fewer than 10 participants controlled a voting majority [feichtinger/2023_hidden-shortcomings-daos].

**Design implication:** Markets forecast well enough to inform the Guardians, not to decide. Binding futarchy needs one agreed welfare metric, which the doughnut does not yet supply, and it invites gaming of the outcome. Token-weighted voting reproduces plutocracy.

## Design patterns that work

- **Default with a veto.** Acts take effect unless enough citizens demand a vote in time. *Conditions:* a default decider, a fair signature rule, a fixed window. *Failure mode:* untested where the default decider is chosen by lot.
- **Rationed universal votes.** A few fixed days a year, an official booklet, two-page summaries. *Conditions:* neutral information. *Failure mode:* long ballots raise abstention and status-quo votes.
- **A required deliberative step.** Mongolia requires a poll before amendments. An independent council screens topics, and the statistics office draws the sample. *Conditions:* published methods, control groups. *Failure mode:* the organisers report on themselves.
- **Emergency law with a sunset.** Urgent acts take effect at once, lapse within a year unless approved, and cannot be renewed after rejection. *Failure mode:* needs a body able to act fast.
- **Local participatory budgets.** Residents set priorities for part of capital spending. *Conditions:* an executive bound to deliver. *Failure mode:* quiet abandonment, as in Porto Alegre.
- **Maps, not votes, from machines.** Opinion maps and AI summaries feed humans who decide. *Conditions:* open code, human checks, several providers. *Failure mode:* persuasion, bias, single-vendor control.
- **Forecasts as advice.** Prediction markets inform decisions. *Conditions:* real stakes, verified identities, independent resolution. *Failure mode:* whales and capture of the resolution step.
- **Identity first.** Delegation, quadratic voting and quadratic funding all assume one person, one identity. Without it they fail.

## Tensions and open problems

- **Participation against representativeness.** In Geneva, over 90% voted at least once in 20 votes. Samples reach well under 1% of adults in a lifetime (estimates above).
- **Binding samples are untried.** Legitimacy gains depend on outputs being honoured, and no polity has let a sample decide.
- **Secrecy against accountability.** Delegates and officials must vote in the open (Colorado, LiquidFeedback), while VIII.5 promises secret votes.
- **Identity against privacy.** Every weighted or delegated scheme needs unique-person checks. The digital ID strand found universal, private enrolment unsolved ([digital voting](digital-voting.md)).
- **Money in decisions.** Quadratic funding and markets let money weigh in, which sits uneasily with V.2's "No money in votes".
- **Metrics.** Futarchy and the long-view test (X.4) both need agreed measures. The doughnut's indicators are still contested ([floor and ceiling](floor-and-ceiling.md)).
- **AI dependence.** The tools that make planetary deliberation cheap come mostly from a few companies, and they persuade as well as summarise.
- **Evidence transfer.** The strongest results rest on elected bodies, which Kara wants to move beyond.
- **Selecting the Stewards.** Replacing VIII.7's planetary election falls outside this strand. Round 1 found no modern state that chooses its judges by lot.

## Options for the next draft

These are options, not decisions.

- **VII.3, the universal vote.** Replace "Every terran votes on the questions before the Commonwealth" with a two-route rule. Most measures are decided by a body drawn by lot and take effect unless enough terrans demand a vote within a fixed window.
- **VII.3, what still goes to everyone.** Keep universal votes only for Charter amendments (XI.3) and changes to the ceiling. Hold them on a few fixed days a year.
- **VIII.3–4, a deciding sample.** For each planetary measure, a stratified random sample, perhaps 10,000 terrans, deliberates online and votes. Its result binds unless a universal veto is triggered. Components exist; the combination is untested.
- **VIII.3, a check on the assembly.** Run an independent deliberative poll with a control group beside each assembly. If they disagree, the question goes to a universal vote.
- **VIII.1, the agenda.** Add a standing council chosen by lot, like Mongolia's Deliberative Council, to screen proposals and publish its reasons.
- **VIII.2, machine help.** Permit AI summaries and opinion maps as input only. Publish the models, prompts and moderation rules, and use more than one provider. Bar AI from voting, or predicting votes, in place of people.
- **New clause, delegation.** Allow revocable, topic-by-topic delegation only after community pilots. Caps on any delegate's weight, public delegate votes and annual expiry would be preconditions.
- **IV.5, budgeting.** Leave community budgets to participatory budgeting. Set planetary spending priorities by deliberative sample, and use quadratic funding only for small grant pools with verified identities.
- **X.4, forecasting.** Feed the Guardians' impact statements with prediction markets, as advice only. Forecasting tournaments were not reviewed here. Rule out binding futarchy and token-weighted voting.
- **New clause, emergencies.** Allow urgent measures to take effect at once for at most a year. They lapse unless a vote approves them, and cannot be renewed after rejection.
- **VII.2, identity.** State that any weighted or delegated mechanism requires a private, one-per-person credential, or is not used.

## Mechanism × purpose matrix

Grades: **A**, binding at national scale or larger for 10+ years, with outcome data. **B**, real use with measured results, but advisory, local or short-lived. **C**, pilots, experiments, self-reports, or an untested combination of proven parts. **D**, theory only, or a record of failure. A dash means no evidence for that purpose. Attention cost is per participant. Manipulation risk is judged from the cases above.

| Mechanism | Agenda | Drafting | Deciding | Budgeting | Forecasting | Oversight | Attention cost | Manipulation risk |
|---|---|---|---|---|---|---|---|---|
| Universal vote (referendum, initiative) | A | C | A | B | — | A | Low per vote; rises with ballot length | Medium: fatigue, ballot order, money |
| Veto on demand (optional referendum) | — | — | A | B | — | A | Very low unless triggered | Low to medium: signature drives |
| Assembly drawn by lot | B | B | — | C | — | C | Very high for members (days to weeks) | Medium: recruitment, briefing, staff |
| Deliberative poll | B | — | C | — | — | — | Medium (a weekend, or about 2 hours online) | Medium: materials, moderators, sponsors |
| Opinion mapping (Polis-style) | B | C | — | — | — | — | Low | Medium to high: fake accounts, algorithm design |
| AI mediation and summaries | C | C | — | — | — | — | Low | High: persuasion, bias, opacity, vendor control |
| Liquid delegation | C | — | C | — | — | — | Low for delegators; high for delegates | High: concentration, vote-buying, coercion |
| Quadratic voting | C | — | D | C | — | — | Low to medium | High without verified identities; collusion |
| Quadratic funding | — | — | — | C | — | — | Low | High: fake identities, airdrop farming |
| Participatory budgeting | B | — | — | B | — | — | Medium (meetings) | Medium: executive discretion, misuse of the label |
| Prediction markets | — | — | — | — | B | — | Low for the public | Medium: whales, resolution capture |
| Futarchy (decision markets) | — | — | D | C | C | — | Low for the public | High: outcome gaming, fake accounts |
| Token-weighted voting | — | — | D | D | — | — | Low | Very high: plutocracy, exploits |

## Which mechanisms for which level and purpose

| Purpose | Community | Region | Planetary |
|---|---|---|---|
| Agenda-setting | Opinion maps; a standing council chosen by lot | Screening council chosen by lot | Screening council; global opinion maps as input only |
| Drafting | Small assemblies | Citizens' assemblies | Regional assemblies feeding a global one, with Oregon-style pro and con statements |
| Deciding | Direct votes; delegation pilots | Deciding samples with a veto | Deciding samples plus a universal veto; universal votes only for the Charter and the ceiling |
| Budgeting | Participatory budgeting; quadratic voting to rank, with verified identities | Participatory budgeting at scale, as in Portugal; whole-budget panels | Whole-budget sample panels (untested at this scale); quadratic funding for small grant pools only |
| Forecasting | Rarely needed | Prediction markets as advice | Markets advising the Guardians' impact statements |
| Oversight | Veto votes; open records | Veto votes; review panels chosen by lot | Universal veto; votes on emergency measures; independent audits |

## Sources

| Source id | Title | Tier | Checked |
|---|---|---|---|
| swissvotes/2026_dataset | Swissvotes: the database of Swiss federal popular votes (dataset and codebook) | primary | verified |
| gfs-bern/2021_vox-june-2021 | VOX-Analyse Juni 2021 | primary | verified |
| gfs-bern/2026_vox-november-2025 | VOX-Analyse November 2025 | primary | verified |
| swiss-federal-council/2021_voting-booklet-june-2021 | Volksabstimmung vom 13. Juni 2021: Erläuterungen des Bundesrates | primary | verified |
| sciarini/2015_selective-participation | The Underexplored Species: Selective Participation in Direct Democratic Votes | primary | partial |
| dermont/2016_taking-turns-ballot-box | Taking Turns at the Ballot Box: Selective Participation as a New Perspective on Low Turnout | primary | partial |
| swissinfo/2016_most-swiss-do-vote | Most Swiss do actually vote | secondary | verified |
| switzerland-bk/2026_referenden | Referenden (Swiss Federal Chancellery) | primary | verified |
| switzerland/1999_federal-constitution | Federal Constitution of the Swiss Confederation | primary | verified |
| california-sos/2025_initiatives-summary-data | Initiatives: Summary of Data | primary | verified |
| california-sos/2026_qualified-ballot-measures | Qualified Statewide Ballot Measures | primary | verified |
| augenblick-nicholson/2016_choice-fatigue | Ballot Position, Choice Fatigue, and Voter Behaviour | primary | partial |
| garmann/2017_election-frequency-fatigue | Election frequency, choice fatigue, and voter turnout | primary | partial |
| lupia/1994_shortcuts-versus-encyclopedias | Shortcuts Versus Encyclopedias | primary | partial |
| worldbank/2026_wdi-population | World Development Indicators: Population, total (SP.POP.TOTL), 2024 | primary | verified |
| worldbank/2026_wdi-population-0-14 | World Development Indicators: Population ages 0–14 (% of total), 2024 | primary | verified |
| stanford-ddl/2026_what-is-deliberative-polling | What is Deliberative Polling? | primary | verified |
| fishkin/2021_america-in-one-room | Is Deliberation an Antidote to Extreme Partisan Polarization? Reflections on "America in One Room" | primary | verified |
| sanders/2012_deliberative-polling-eu | The Effects of Deliberative Polling in an EU-wide Experiment | primary | partial |
| cddrl/2023_metaverse-community-forum | Results of First Global Deliberative Poll Announced | primary | verified |
| stanford-ddl/2026_meta-forum-generative-ai | Meta Community Forum on Generative AI: results | primary | verified |
| cddrl/2026_industry-wide-forum-ai-agents | People Shaping AI: Industry-Wide Forum on the Future of AI Agents | primary | verified |
| stanford-ddl/2017_mongolia-first-national-deliberative-poll | Mongolia's First National Deliberative Poll on Constitutional Amendments | primary | verified |
| stanford-ddl/2026_mongolia-constitutional-amendment | Deliberative Polling Leads to New Constitutional Amendment in Mongolia | primary | verified |
| stanford-ddl/2026_online-deliberation-platform | Stanford Online Deliberation Platform | primary | verified |
| stanford-ddl/2026_taiwan-information-integrity-poll | Taiwan Deliberation on Utilizing AI to Enhance Information Integrity | primary | verified |
| oecd/2020_catching-the-deliberative-wave | Innovative Citizen Participation and New Democratic Institutions: Catching the Deliberative Wave | primary | verified |
| global-assembly/2022_report-2021 | Report of the 2021 Global Assembly on the Climate and Ecological Crisis | primary | verified |
| germann/2024_scaling-up-mini-publics | Scaling Up? Unpacking the Effect of Deliberative Mini-Publics on Legitimacy Perceptions | primary | partial |
| garry/2021_citizens-assemblies-northern-ireland | The Perception of the Legitimacy of Citizens' Assemblies in Deeply Divided Places? | primary | partial |
| kahng/2018_liquid-democracy-algorithmic | Liquid Democracy: An Algorithmic Perspective | primary | partial |
| campbell/2022_liquid-democracy-experiments | Liquid Democracy. Two Experiments on Delegation in Voting | primary | partial |
| kling/2015_liquidfeedback-super-voters | Voting Behaviour and Power in Online Democracy: A Study of LiquidFeedback in Germany's Pirate Party | primary | verified |
| eisel/2015_liquidfriesland-am-ende | LiquidFriesland endgültig am Ende | secondary | verified |
| friesland/2015_liquidfriesland-evaluation | Evaluierungsbericht LiquidFriesland | primary | verified |
| hardt-lopes/2015_google-votes | Google Votes: A Liquid Democracy Experiment on a Corporate Social Network | primary | verified |
| fritsch/2022_who-controls-daos | Analyzing Voting Power in Decentralized Governance: Who controls DAOs? | primary | verified |
| weyl-tang/2024_plurality | Plurality: The Future of Collaborative Technology and Democracy | secondary | verified |
| lalley-weyl/2018_quadratic-voting | Quadratic Voting: How Mechanism Design Can Radicalize Democracy | primary | partial |
| posner-weyl/2018_radical-markets | Radical Markets: Uprooting Capitalism and Democracy for a Just Society | primary | partial |
| casella-sanchez/2019_storable-votes-quadratic-voting | Storable Votes and Quadratic Voting. An Experiment on Four California Propositions | primary | partial |
| colorado-sun/2019_quadratic-voting-budget | $120 million in requests and $40 million in the bank: how an obscure theory helped prioritize the Colorado budget | secondary | verified |
| colorado-sun/2024_quadratic-voting-ruling | Judge orders Democrats at the Colorado Capitol to stop using secret voting system to allocate state budget | secondary | verified |
| colorado-politics/2024_funding-method-transparency | Colorado Democrats unveil new method, promise transparency in funding bills | secondary | verified |
| buterin-hitzig-weyl/2019_flexible-design-public-goods | A Flexible Design for Funding Public Goods | primary | partial |
| gitcoin/2024_state-of-public-goods-funding | State of Public Goods Funding 2024 | primary | verified |
| gitcoin/2026_gg24 | Gitcoin Grants 24 | primary | verified |
| gitcoin/2026_identity-binding-constraint | Identity Infrastructure: The Binding Constraint on Democratic Funding | primary | verified |
| tessler/2024_ai-common-ground | AI can help humans find common ground in democratic deliberation | primary | partial |
| small/2023_llms-polis | Opportunities and Risks of LLMs for Scalable Deliberation with Polis | primary | verified |
| anthropic/2023_collective-constitutional-ai | Collective Constitutional AI: Aligning a language model with public input | primary | verified |
| moda/2024_alignment-assemblies | Alignment Assemblies (Ministry of Digital Affairs) | primary | verified |
| moda/2024_information-integrity-meeting | Meeting with international AI companies on information integrity alignment assembly | primary | verified |
| techbrew/2025_bowling-green-sensemaker | Bowling Green, Kentucky AI tool: Google Jigsaw Sensemaker | secondary | verified |
| google/2026_sensemaking-ai-local-governments | Using AI to help local governments connect with constituents | primary | verified |
| vargiu-nai/2025_ai-chatbots-persuade-voters | AI chatbots can persuade voters | secondary | verified |
| padmakumar-he/2024_llm-writing-diversity | Does Writing with Language Models Reduce Content Diversity? | primary | partial |
| melgar/2014_time-of-closure | A Time of Closure? Participatory Budgeting in Porto Alegre, Brazil, after the Workers' Party Era | secondary | partial |
| jornal-do-comercio/2021_atlas-op-porto-alegre | Atlas Mundial vê extinção do Orçamento Participativo em Porto Alegre | secondary | verified |
| dias/2019_participatory-budgeting-world-atlas | Participatory Budgeting World Atlas 2019 | primary | verified |
| goncalves/2014_pb-municipal-expenditures | The Effects of Participatory Budgeting on Municipal Expenditures and Infant Mortality in Brazil | primary | partial |
| touchton-wampler/2014_improving-social-well-being | Improving Social Well-Being Through New Democratic Institutions | primary | partial |
| boulding-wampler/2010_voice-votes-resources | Voice, Votes, and Resources: Evaluating the Effect of Participatory Democracy on Well-being | primary | partial |
| hanson/2013_vote-values-bet-beliefs | Shall We Vote on Values, But Bet on Beliefs? | primary | verified |
| berg/2008_prediction-market-accuracy | Prediction market accuracy in the long run | primary | partial |
| wolfers-zitzewitz/2004_prediction-markets | Prediction Markets | secondary | partial |
| rothschild-sethi/2015_intrade-trading-strategies | Trading Strategies and Market Microstructure: Evidence from a Prediction Market | primary | verified |
| theblock/2025_polymarket-uma-attack | Polymarket says governance attack by UMA whale to hijack a bet's resolution is "unprecedented" | secondary | verified |
| optimism/2025_futarchy-v1-findings | Futarchy v1 Preliminary Findings | primary | verified |
| sec/2017_the-dao-report | Report of Investigation Pursuant to Section 21(a) of the Securities Exchange Act of 1934: The DAO | primary | verified |
| feichtinger/2023_hidden-shortcomings-daos | The Hidden Shortcomings of (D)AOs: An Empirical Study of On-Chain Governance | primary | verified |
