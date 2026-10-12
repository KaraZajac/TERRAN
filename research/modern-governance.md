# Beyond the 18th-century template: how modern communities govern themselves

*Research note · planetary government, round 2 · first pass, 11 October 2026 · compiled by Claude, not yet reviewed by Kara*

Global communities that govern themselves without a state still elect councils, but keep them small, narrow and removable. Routine work runs on consent, and all-member votes are rare: Debian's developers have voted on 33 general resolutions since 2003. Newer tools, from policy experiments and sunsets to rules as code and e-petitions, have thin or mixed outcome evidence. Each works only when a named body must respond, and none shows that every terran can vote on every question.

## What the Charter says now

- **VII.2–3.** Every terran holds a digital identity and "votes on the questions before the Commonwealth".
- **VII.4.** Decisions sit close to those affected; planetary matters go to all terrans.
- **VII.5–6.** Decisions, spending and amendments go on open ledgers; transparency scales with power.
- **VII.7 and Part III.** Every institution answers the doughnut test. Success is measured by who is inside the doughnut and the distance to each boundary.
- **VIII.1–4.** Anyone proposes, open discussion maps common ground, an assembly chosen by lot writes the ballot, and every terran votes.
- **VIII.7–8.** An elected Council of Stewards administers for "one fixed term", without a veto. No body holds two powers.
- **X.4–5 and XI.** A long-view test, a "follow or explain" duty, revision as knowledge grows, and a full review every 25 years.

The draft has no rule for routine decisions, no review dates, no way to remove a Steward and no stated feedback loop. Round 1 covered assemblies, initiatives and vTaiwan ([deliberation](deliberation.md)) and online voting ([digital voting](digital-voting.md)).

## 1. How open-source and online communities govern themselves

| Community | Scale | Top body | Removal | Routine decisions | Turnout |
|---|---|---|---|---|---|
| Debian (constitution 1998, v1.9 2022) | 1,045 voting developers, August 2026 [debian/2026_gr-llm-usage] | Project Leader, one-year term; Technical Committee of up to 8 [debian/1998_constitution] | Recall by general resolution; tried in 2006, lost 48 to 277 [debian/2006_gr-recall-leader] | Each developer decides their own work; general resolutions use Condorcet ranking [debian/1998_constitution] | About 33% in the 2026 leader election (339 of 1,039; estimate) [debian/2026_dpl-election] |
| Python (PEP 13, 2018) | 106 eligible core developers, December 2025 [python/2025_pep-8107] | Steering Council of 5, elected after each feature release [python/2018_pep-13] | No-confidence vote by two-thirds of voters [python/2018_pep-13] | Proposals (PEPs); the council acts "as rarely as possible" [python/2018_pep-13] | 70% (74 of 106) [python/2025_pep-8107] |
| Rust (Leadership Council, 2023) | "hundreds of globally distributed people" [rust/2023_rfc-3392-leadership-council] | One representative from each of nine top-level teams [rust/2023_introducing-leadership-council] | Teams choose and replace their representative [rust/2023_rfc-3392-leadership-council] | RFCs only for "substantial" changes, with a ten-day final comment period [rust/2026_rfc-process] | No all-member vote |
| Apache Software Foundation (1999) | 10,100+ committers, 1,190+ members, 290+ projects [asf/2026_homepage] | Board of nine, elected yearly by members [asf/2026_how-it-works] | Annual election; the board can end a project committee [asf/2026_how-it-works] | Lazy consensus: "silence gives assent" [asf/2026_voting-process] | Not found |
| English Wikipedia | 28,773 active editors, September 2026 [wikimedia/2026_active-editors-api] | Arbitration Committee of 15: nine seats filled in 2025, six continuing [wikipedia/2025_arbcom-election] | Seats need 60% support for two years, 50% for one [wikipedia/2025_arbcom-election] | Consensus, which is not "the result of a vote" [wikipedia/2026_consensus-policy] | 1,840 voters, December 2025 [wikipedia/2025_arbcom-election] |

**Debian.** Developers can override the Leader by majority, the Committee by 2:1, and amend the constitution by 3:1 [debian/1998_constitution]. A resolution backed by 2K developers puts a Leader's decision on hold at once [debian/1998_constitution]. At today's size K is 5, so 10 developers suffice (my arithmetic). In February 2014 a Committee vote on the default init system ended in a tie, and the chair's casting vote chose systemd [debian/2014_tc-init-decision]. Developers then added term limits [debian/2014_gr-tc-term-limits]. Each year, up to two of the most senior members leave once past 42 months [debian/1998_constitution]. The vote index lists 33 general resolutions decided from 2003 to 2026, and 28 leader elections since 1999 [debian/2026_vote-index]. In August 2026 developers ranked eight policies on AI-generated contributions, and one beat every rival head to head [debian/2026_gr-llm-usage].

**Python.** Guido van Rossum stepped down as Benevolent Dictator for Life in July 2018 [python/2018_pep-13]. A hard fight over one proposal had worn him out [van-rossum/2018_transfer-of-power]. He wrote: "I am not going to appoint a successor." [van-rossum/2018_transfer-of-power] Core developers voted on rival models, and the first council was elected in January 2019 [python/2018_pep-13]. PEP 13 caps any one employer at two of five seats, and it has been amended in 2019, 2024 and 2025 [python/2018_pep-13].

**Rust.** In November 2021 the whole moderation team resigned. They protested a core team "unaccountable to anyone but themselves" [rust/2021_mod-team-resignation]. The interim "leadership chat" "lacked clear rules and processes for decision making and communication", and in May 2023 it demoted a keynote speaker [rust/2023_rustconf-keynote]. A Leadership Council replaced it on 20 June 2023 [rust/2023_introducing-leadership-council]. It decides by consent: members are asked "do you object?", and a decision needs N−2 sign-offs, no open objection and ten days [rust/2023_rfc-3392-leadership-council]. Terms last one year and end in March or September, so seats change in halves. No affiliation may hold more than two seats [rust/2023_rfc-3392-leadership-council]. The Council "should not take on work beyond what this RFC explicitly assigns to it" [rust/2023_rfc-3392-leadership-council]. And: "All policy decisions should have an evaluation date as part of the policy." [rust/2023_rfc-3392-leadership-council]

**Apache.** Each project committee holds technical authority; the board manages assets and oversight [asf/2026_how-it-works]. A veto on code must carry a technical justification, or it is invalid [asf/2026_voting-process]. The Attic, created in 2008 to retire projects, lists about 105 of them (my count) [asf/2026_attic]. The model leans on unpaid labour. Log4j was maintained by "a group of volunteers" under Apache, and its 2021 flaw became an "endemic vulnerability" [csrb/2022_log4j-review]. The US review board pointed to risks unique to a "thinly-resourced, volunteer-based open source community" [csrb/2022_log4j-review].

**Wikipedia.** Consensus is "Wikipedia's fundamental method of decision-making", judged by "the quality of arguments" [wikipedia/2026_consensus-policy]. The Arbitration Committee imposes binding solutions, mainly in conduct disputes the community cannot settle [wikipedia/2026_arbitration-committee]. Registered, non-bot editors making five or more content edits a month peaked at 53,095 in March 2007. By September 2026 there were 28,773, a fall of 46% (my calculation) [wikimedia/2026_active-editors-api]. Halfaker and colleagues tie the decline to quality-control tools that rejected good newcomers, and to norms that "calcified against changes" [halfaker/2013_rise-and-decline]. Across 683 wikis, Shaw and Hill found oligarchy growing with size [shaw-hill/2014_laboratories-of-oligarchy]. In a 2022 vote across Wikimedia projects, 58.6% of 2,283 counted votes backed a conduct-code enforcement plan [wikimedia/2022_ucoc-vote-results]. Turnout was 3.8% on English Wikipedia, and about 3.5% overall (my estimate from the turnout table) [wikimedia/2022_ucoc-vote-results].

**Design implication:** Copy the shape, not the electorate. Every case limits the vote to active contributors. Even so, turnout runs from 3.5% to 70%, and top bodies have 5 to 15 members with narrow written duties.

## 2. Experimental and adaptive policy

**Experimentalist governance.** Sabel and Zeitlin describe a "recursive" cycle. Framework goals and metrics are set provisionally; local units choose their means, report, and face peer review; then goals and rules are revised [sabel-zeitlin/2012_experimentalist-governance]. They argue it suits "transnational domains, where there is no overarching sovereign" [sabel-zeitlin/2012_experimentalist-governance]. Their lead example, the EU Water Framework Directive, missed its 2015 deadline for good water status. In 2021 only 37% of surface waters had good ecological status, and 29% good chemical status [eea/2024_europes-state-of-water]. The Lisbon Strategy, which leaned on the EU's open method of coordination, also missed its targets. Its employment rate peaked at 66% (2008) against 70%, and R&D reached 1.9% of GDP against 3% [ec/2010_lisbon-strategy-evaluation]. The Commission found that "most Member States have used OMCs as a reporting device rather than one of policy development" [ec/2010_lisbon-strategy-evaluation].

**Policy trials.** Finland paid 2,000 randomly chosen unemployed people €560 a month, tax-free, in 2017–18 [stm/2020_basic-income-results]. In year one there was no employment effect. From November 2017 to October 2018 recipients worked six more days, 78 on average [stm/2020_basic-income-results]. They reported less mental strain and more trust, though Kela could not say with certainty that the basic income caused this [stm/2020_basic-income-results]. But a new "activation model" in 2018 hit both groups unevenly, so year-two effects "cannot be separated" from it [stm/2020_basic-income-results]. The UK's What Works Network, begun in 2013, has 9 centres and 3 affiliates covering over £250 billion of spending [uk-gov/2013_what-works-network]. Yet in 2019 only 9 of 108 major projects, 8% of £432 billion, were robustly evaluated. Another 77, holding 64% of the spend, had no evaluation arrangements [nao/2021_evaluating-government-spending].

**Regulatory sandboxes.** The UK Financial Conduct Authority opened its sandbox in June 2016. Its first two cohorts drew 146 applications; 50 were accepted and 41 tested [fca/2017_sandbox-lessons-learned]. By the regulator's own count, about 90% of first-cohort firms that finished testing moved toward market launch [fca/2017_sandbox-lessons-learned]. By November 2020, 57 countries ran 73 fintech sandboxes, 70% of them in emerging and developing economies [worldbank/2020_regulatory-sandboxes]. Tests ran from two weeks to two years. Some sandboxes drew few applicants, and the World Bank called it "too early to draw definitive conclusions" about their efficiency [worldbank/2020_regulatory-sandboxes].

**Sunsets and automatic review.** Texas reviews state agencies on a cycle and abolishes them unless the legislature continues them. Since 1977, 95 have been abolished, 42 outright [texas-sunset/2026_about]. The commission estimates $1 billion in savings from 1985 to 2023, or $16 per $1 spent; these are its own fiscal-note estimates [texas-sunset/2026_about]. A RAND Europe study for the Bertelsmann Stiftung found "a substantial lack of empirical evidence" and only limited effects [wegrich/2005_sunset-review-clauses]. A sunset, it argued, "will primarily activate the capacities of 'anti-termination coalitions' to mobilize resistance" [wegrich/2005_sunset-review-clauses]. A 2018 study still found a "dearth of empirical studies" [bar-siman-tov/2018_temporary-legislation]. In a randomised test with 1,639 US adults, sunsets "did not increase overall support for laws" [underhill-ayres/2022_sunsets-are-for-suckers]. Emergency law shows a tighter design. The UK Coronavirus Act 2020 expired after two years, with listed exceptions. If the Commons rejected its six-monthly renewal motion, the temporary powers had to end within 21 days [uk/2020_coronavirus-act].

**Design implication:** Experiments, sandboxes and sunsets help only when evaluation is planned, funded and binding on someone. The best-documented sunsets retire bodies, not rules, through a standing reviewer.

## 3. Rules written as code

**The idea.** The OECD defines Rules as Code as an official, machine-consumable version of laws and regulations [oecd/2020_cracking-the-code]. Proponents limit it to "prescriptive rules that you want implemented clearly and consistently, like eligibility criteria, or calculations for taxation and benefits" [oecd/2020_cracking-the-code]. The OECD warns that code could "lock-in" one interpretation of a rule. It also found it "unclear if any RaC initiative" had built in citizen feedback [oecd/2020_cracking-the-code].

**New Zealand.** Better Rules began in early 2018 as a three-week sprint. A legislative drafter, policy analysts and a software developer worked together [nz-dia/2018_better-rules-discovery]. Modelling the Holidays Act exposed that "week" was undefined for people with irregular hours. The team concluded that "not all rules are suitable for machine consumption" [nz-dia/2018_better-rules-discovery]. I did not find the programme's status in 2026.

**France.** Income tax is computed by a program written in a custom language from 1990. Researchers rebuilt its compiler and validated it against the tax office's own tests. The office then began "officially transitioning" to it [merigoux/2021_mlang]. Catala, a language for statutes, found a bug in an official implementation while coding French family benefits [merigoux/2021_catala]. Coding housing benefits exposed a conflict for roommates sharing a bedroom. Officials were asked, but "no legal interpretation was provided to resolve this ambiguity" [goutagny/2024_cutecat]. I could not verify which French agencies run Catala in production as of October 2026.

**Version control of law.** Washington, DC keeps its code in a public Git repository. In 2018 Joshua Tauberer fixed a typo in it with a pull request, and wrote: "This isn't a copy of the DC law. It is an authoritative source." [tauberer/2018_github-pull-request] He cautioned that pull requests will not replace hearings, negotiation or votes [tauberer/2018_github-pull-request]. The repository was last updated on 10 October 2026 [dccouncil/2026_law-xml].

**Failure at scale: Robodebt.** From 2015 to 2019 Australia raised welfare debts by "income averaging", which was neither accurate nor lawful [robodebt-rc/2023_report]. The government refunded $746 million to about 381,000 people and wrote off $1.751 billion in debts [robodebt-rc/2023_report]. The Royal Commission called it "a crude and cruel mechanism, neither fair nor legal" [robodebt-rc/2023_report]. Tribunal rulings against averaging went unpublished, which made them easier to ignore [robodebt-rc/2023_report]. The Commission recommended review rights, plain-language explanations, published "business rules and algorithms" and an audit body [robodebt-rc/2023_report].

**On-chain governance.** DAOs, blockchain organisations run by token votes, are the most literal form of government by code. In 17 of 21 studied in January 2023, fewer than 10 participants controlled a majority of votes [feichtinger/2023_hidden-shortcomings-daos].

**For the floor, the ceiling and taxes.** The Charter's most codeable rules are calculations and thresholds: the wealth limit and tax bands (IV.4–6), pay ratios (V.3) and floor eligibility. The ceiling's science, the Seven Principles and "spirit over letter" are not.

**Design implication:** Publish tax and entitlement rules as official, versioned code beside the text, keep the text authoritative, and fund an independent auditor. Code makes errors fast and uniform, so every automated decision needs a human review path.

## 4. Feedback-driven (cybernetic) government

**The Viable System Model.** Beer's model claims to state the necessary and sufficient conditions for any organisation to stay viable [schwaninger-scheef/2016_test-of-vsm]. It nests "autonomous units within autonomous units". An audit channel, System 3*, checks reported information against the units directly [schwaninger-scheef/2016_test-of-vsm]. The evidence is mostly case studies. The main statistical test used 261 usable questionnaires from managers at one business congress, and its authors concede "this sample is not perfect" [schwaninger-scheef/2016_test-of-vsm].

**Cybersyn.** Built under President Allende (1970–73), Chile's system linked state factories by telex to a central computer and an operations room [medina/2006_designing-freedom; morozov/2014_planning-machine]. It "was never completely implemented" before the 1973 coup [medina/2011_cybernetic-revolutionaries]. During the October 1972 truckers' strike, the telex network helped industries share fuel [morozov/2014_planning-machine]. The screens were drawn by hand, and factory analysis was "only as good as the underlying formal model" [morozov/2014_planning-machine]. Medina's 2006 article examines how its structure reflected the government's socialist ideology [medina/2006_designing-freedom]. Her publisher says the book also shows "the limitations of the Chilean revolution" [medina/2011_cybernetic-revolutionaries]. I read only the publisher's summary, her 2006 abstract and a review, not the book.

**Real-time signals.** Since 2011 the Atlanta Fed's GDPNow nowcast has missed first GDP estimates by 0.77 points on average, with a root-mean-square error of 1.17 [atlanta-fed/2026_gdpnow]. Its makers say this gives no "compelling evidence" that it beats professional forecasters [atlanta-fed/2026_gdpnow]. Google Flu Trends predicted more than double the CDC's rate of flu-like doctor visits in February 2013 [lazer/2014_parable-google-flu]. In England a data-load fault left 15,841 positive Covid-19 cases out of the reported figures for 25 September–2 October 2020 [phe/2020_delayed-reporting].

**Outcome budgeting.** New Zealand's 2019 Wellbeing Budget set five priorities, and every funding bid needed a wellbeing analysis [nz-treasury/2019_wellbeing-budget]. But in 2019 about 98% of spending simply rolled over, and new proposals "account for a tiny fraction of total expenditure" [pce/2021_wellbeing-budgets-faq]. A 2024 review of its mental-health package led with spending: 92% of $1.96 billion was spent or committed by June 2023 [mhwc/2024_budget-investment-report]. A 2025 bill would drop the duty to report against wellbeing objectives; I could not confirm its status in October 2026 [nzccss/2025_public-finance-amendment-bill]. In England's health service, Bevan and Hood showed that governing by targets assumes "problems of measurement and gaming do not matter" [bevan-hood/2006_whats-measured].

**The doughnut test as a loop (VII.7).** The inputs exist, but they lag. PIK's annual Planetary Health Check scores 13 control variables; some of its datasets end in 2023 [pik/2026_planetary-health-check]. The latest global doughnut, published in 2025, covers 2000–2022 with 22 social indicators [deal/2026_what-is-the-doughnut]. A loop could combine the precedents above:

| Step | Mechanism | Precedent | Known failure |
|---|---|---|---|
| Sense | An independent body publishes a doughnut account on a fixed date | PIK's annual check [pik/2026_planetary-health-check] | Data three to four years old |
| Nowcast | Model estimates for the current year, with published error | GDPNow [atlanta-fed/2026_gdpnow] | Drift [lazer/2014_parable-google-flu] |
| Audit | Separate auditors test the data and look for gaming | System 3* [schwaninger-scheef/2016_test-of-vsm]; audit body [robodebt-rc/2023_report] | Gaming [bevan-hood/2006_whats-measured] |
| Trigger | A worsening indicator opens a review with a deadline | Evaluation dates [rust/2023_rfc-3392-leadership-council]; renewal votes [uk/2020_coronavirus-act] | Rubber-stamp renewal [wegrich/2005_sunset-review-clauses] |
| Respond | The named institution acts or explains (X.5) | Dated petition responses [uk-parliament/2026_petitions-help] | Reports without action [ec/2010_lisbon-strategy-evaluation] |

**Design implication:** A doughnut loop is feasible as a yearly accounting cycle with named responders and independent audit. With lags of years, it can steer policy but cannot handle emergencies.

## 5. Continuous-participation platforms

| Channel | Threshold and promise | Submitted | Cleared the threshold | What followed |
|---|---|---|---|---|
| UK Parliament e-petitions, 2019–24 | 10,000 signatures: government response; 100,000: considered for debate [uk-parliament/2026_petitions-help] | 52,031, of which 38,280 (74%) rejected [uk-parliament/2026_archived-petitions-2019-2024] | 1,018 responses, 7.4% of 13,751 published | 213 debated, 1.5% of published [uk-parliament/2026_archived-petitions-2019-2024] |
| Taiwan's Join, to June 2022 | 5,000 supporters: reasoned agency response [bertelsmann/2022_taiwan-join-vtaiwan] | 13,853 | 289 (2.1%) | For example, menstrual cups approved in March 2017 [bertelsmann/2022_taiwan-join-vtaiwan] |
| Decide Madrid (Consul), 2015–18 | 1% of residents over 16 (27,662): binding vote [royo/2020_decide-madrid] | 25,418 | 2 (0.008%) | Both won their votes [royo/2020_decide-madrid] |
| Barcelona budgets (Decidim), 2020–23 | Technical review, then a vote on €30 million [decidim/2026_barcelona-budgeting] | 1,982 | 823 viable; 204 prioritised | 76 funded (3.8%); 64,571 took part [decidim/2026_barcelona-budgeting] |

Shares are my calculations. The UK system mostly serves engagement: "only a very small number lead to specific action" [leston-bandeira/2019_e-petitions]. In Madrid a tree-planting proposal expired with 20,602 of the 27,662 supports needed, and citizens called the process "a waste of time" [royo/2020_decide-madrid]. Turnout in Madrid's binding votes fell from 214,076 people in February 2017 to 9,854 votes in July 2018. The platform survived the 2019 change of government [royo/2020_decide-madrid]. Decidim reports over 500 user organisations; Consul, over 250 cities and organisations, past and present [decidim/2026_homepage; consul-democracy/2026_homepage]. In Catalan towns, officials valued transparency and gathering proposals "rather than deliberation and transfer of sovereignty towards citizens". Yet the platform brought in new participants [borge/2022_decidim-catalonia].

**Design implication:** Standing channels work as agenda-setters with a guaranteed, dated answer. A threshold near 1% of a population stalls nearly everything. A planetary channel should promise a response at a low threshold and deliberation at a higher one.

## Design patterns that work

- **Small, removable councils with capture caps.** Five to fifteen seats, two-thirds no-confidence votes, two-per-employer caps and, in Rust and Wikipedia, staggered terms [python/2018_pep-13; rust/2023_rfc-3392-leadership-council; wikipedia/2025_arbcom-election]. They work with a defined electorate and written duties. They fail through low turnout and creeping oligarchy [shaw-hill/2014_laboratories-of-oligarchy].
- **Escalation ladders.** Individuals decide their own work, a committee settles disputes, and members can override it by 2:1 [debian/1998_constitution]. This works when the top rung is rare. It fails when a split committee falls back on one casting vote [debian/2014_tc-init-decision].
- **Consent with an objection window.** Silence counts as assent after a set period, or a decision passes when most members sign off and nobody objects [asf/2026_voting-process; rust/2023_rfc-3392-leadership-council]. Vetoes need reasons [asf/2026_voting-process]. This works when drafts reach those affected. It fails when absent people are counted as agreeing.
- **A brake held by a few.** Ten Debian developers can freeze a Leader's decision until members vote [debian/1998_constitution]. A small group could delay at will; I found no study of its use.
- **Powers that lapse unless renewed.** Emergency powers carry a two-year expiry and six-monthly renewal votes [uk/2020_coronavirus-act], and agencies face abolition reviews [texas-sunset/2026_about]. This fails when coalitions defend every renewal [wegrich/2005_sunset-review-clauses].
- **Planned ends and independent counts.** Apache retires dead projects by a set process [asf/2026_attic]. Wikipedia uses outside scrutineers, and Debian voters can find their own ballot in the tally [wikipedia/2025_arbcom-election; debian/2026_dpl-election].

## Tensions and open problems

- **Merit versus standing.** Every electorate here is earned, such as 150 article edits for Wikipedia's election [wikipedia/2025_arbcom-election]. I.1 grants standing at birth.
- **Attention.** Turnout ran from about 3.5% to 70% among roughly 100 to 70,000 eligible voters. Nothing here suggests billions will vote often.
- **Unpaid capacity.** Rust found its old core team "has not scaled and has led to burnout" [rust/2023_rfc-3392-leadership-council]. Log4j shows volunteer upkeep failing [csrb/2022_log4j-review].
- **Quality versus openness.** Wikipedia's defences against bad edits drove away good newcomers [halfaker/2013_rise-and-decline].
- **Code versus spirit.** Code can fix one reading of a rule [oecd/2020_cracking-the-code], while Principle VII lets spirit prevail. Who updates the code when the Court reinterprets?
- **Measurement versus gaming.** A binding doughnut test invites gaming of its own indicators [bevan-hood/2006_whats-measured].
- **Experiments versus the floor.** Finland promised that no participant would lose money, a precedent for trials above the floor [finland-toolbox/2020_basic-income-experiment].
- **Sunsets versus XI.4.** Automatic expiry cannot apply to floor rights.
- **Interim rule.** Python went six months without a council, and Rust's interim body failed [python/2018_pep-13; rust/2023_rustconf-keynote]. Part XII needs written interim rules.

## Options for the next draft

- **VII.3 and VIII.4: tiered decisions.** Standing bodies make routine rules by consent, after a public draft and an objection window. All-terran votes cover amendments, ceiling-sharing rules and petition-triggered challenges; see [sortition at scale](sortition-at-scale.md).
- **VIII.1: two thresholds.** A low one earns a dated, reasoned answer; a higher one earns an assembly. Publish the funnel each year.
- **VIII.7: Stewards as a steering council.** Five to nine seats, staggered one-year terms, removal by two-thirds no-confidence, at most two from one employer, and a duty to act sparingly.
- **A new VIII clause: versioned decisions.** Each decision carries a version number, a public history and an evaluation date. Emergency powers lapse unless renewed.
- **VII.5 with IV and V: rules as code.** Publish tax bands, the wealth limit, pay ratios and floor eligibility as official code. The text prevails, with human review and an independent auditor.
- **VII.7: a yearly doughnut account.** An independent statistical body publishes it, and a worsening indicator triggers a review with a deadline under X.5.
- **VI and XII: sanctioned experiments.** Trials need a pre-registered evaluation, nobody below the floor, and no interfering changes mid-trial.
- **XI.5: rolling review.** Review one Part a year as well as the whole every 25 years. Debian has amended its constitution nine times in 24 years [debian/1998_constitution].
- **VIII.8 and IX: retiring institutions.** Every body faces an abolition review on a fixed cycle.

## Modern design principles

1. **A narrow top over nested units:** Apache's board over project committees, and Ostrom's "nested enterprises" [ostrom/2009_beyond-markets-and-states]. Fails when work outside every team's remit piles onto the top body, as in Rust.
2. **Small, removable councils:** Python's Steering Council. Fails when the top answers only to itself, as in Rust in 2021.
3. **Consent for routine, votes for exceptions:** Apache and Rust. Fails when silence is taken for agreement.
4. **Decisions as versions with review dates:** Rust's evaluation dates and DC's code in Git. Fails when reviews become formalities.
5. **Powers that lapse unless renewed:** the UK's 2020 emergency law and Texas. Fails when defenders renew by habit.
6. **Rules as checkable code, text supreme:** France's income-tax compiler. Fails when an unlawful rule is automated, as in Robodebt.
7. **Experiment before scaling:** Finland's trial. Fails when politics confounds the trial or no one evaluates.
8. **Feedback with independent audit:** PIK's annual check and GDPNow's published errors. Fails through gaming, lags and broken data pipelines.
9. **Participation with a guaranteed answer:** UK petitions and Join. Fails when little changes, or when thresholds stall nearly everything, as in Madrid.

Evidence grades: **A** means independent evaluations across many cases agree. **B** means a long record and official data in several cases, with few independent evaluations. **C** means few cases, self-reported results or design documents. **D** means theory only.

| Principle | Strongest precedent | Grade | Failure mode | Where in the Charter |
|---|---|---|---|---|
| Narrow top, nested units | Apache board and committees; Ostrom | B | Unassigned work piles onto the top | VII.4, VIII.7 |
| Small removable councils | Python Steering Council, since 2019 | B | Unaccountable top; oligarchy | VIII.7 |
| Consent for routine | Apache lazy consensus | C | Silence taken as assent | VIII.1–4 |
| Versioned decisions, review dates | Rust Council; Debian constitution v1.0–1.9 | C | Formal reviews | VIII (new), XI |
| Lapsing powers | Texas Sunset; UK Coronavirus Act | B | Coalitions defend renewal | VIII.7, XII |
| Rules as code, text supreme | French income tax (Mlang); DC code | C | Robodebt-style automated error | III, IV, V.3, VII.5 |
| Experiment first | Finland 2017–18 trial | B for one trial; C as a system | Confounding; skipped evaluation | VI, XII |
| Feedback with audit | PIK annual check; GDPNow | C | Gaming, lag, broken pipelines | III, VII.7, X.4–5 |
| Guaranteed-answer participation | UK e-petitions; Join | B | Low conversion; stalled thresholds | VIII.1–2 |

## Sources

| Source id | Title | Tier | Checked |
|---|---|---|---|
| debian/1998_constitution | Constitution for the Debian Project (v1.9) | primary | verified |
| debian/2026_vote-index | Debian Voting Information (vote index) | primary | verified |
| debian/2026_dpl-election | Debian Project Leader Elections 2026 | primary | verified |
| debian/2026_gr-llm-usage | General Resolution: LLM usage in Debian | primary | verified |
| debian/2006_gr-recall-leader | General Resolution: Recall the project leader | primary | verified |
| debian/2014_tc-init-decision | Bug#727708: call for votes on default Linux init system for jessie | primary | verified |
| debian/2014_gr-tc-term-limits | General Resolution: Limiting the term of the technical committee members | primary | verified |
| python/2018_pep-13 | PEP 13 – Python Language Governance | primary | verified |
| python/2025_pep-8107 | PEP 8107 – 2026 Term Steering Council election | primary | verified |
| van-rossum/2018_transfer-of-power | [python-committers] Transfer of power | primary | verified |
| rust/2026_rfc-process | Rust RFCs (process README) | primary | verified |
| rust/2021_mod-team-resignation | mod team resignation (rust-lang/team pull request 671) | primary | verified |
| rust/2023_rustconf-keynote | On the RustConf keynote | primary | verified |
| rust/2023_rfc-3392-leadership-council | RFC 3392: Leadership Council | primary | verified |
| rust/2023_introducing-leadership-council | Introducing the Rust Leadership Council | primary | verified |
| asf/2026_how-it-works | How the ASF works | primary | verified |
| asf/2026_voting-process | Apache Voting Process | primary | verified |
| asf/2026_homepage | Welcome to The Apache Software Foundation | primary | verified |
| asf/2026_attic | The Apache Attic | primary | verified |
| csrb/2022_log4j-review | Review of the December 2021 Log4j Event | primary | verified |
| wikipedia/2026_consensus-policy | Wikipedia:Consensus | primary | verified |
| wikipedia/2026_arbitration-committee | Wikipedia:Arbitration Committee | primary | verified |
| wikipedia/2025_arbcom-election | Wikipedia:Arbitration Committee Elections December 2025 | primary | verified |
| wikimedia/2026_active-editors-api | Wikimedia Analytics API: editors by activity level, English Wikipedia | primary | verified |
| halfaker/2013_rise-and-decline | The Rise and Decline of an Open Collaboration System | primary | verified |
| shaw-hill/2014_laboratories-of-oligarchy | Laboratories of Oligarchy? How the Iron Law Extends to Peer Production | primary | partial |
| wikimedia/2022_ucoc-vote-results | Universal Code of Conduct/Enforcement guidelines/Voting/Results | primary | verified |
| sabel-zeitlin/2012_experimentalist-governance | Experimentalist Governance | primary | verified |
| eea/2024_europes-state-of-water | Europe's state of water 2024: the need for improved water resilience | primary | verified |
| ec/2010_lisbon-strategy-evaluation | Lisbon Strategy evaluation document, SEC(2010) 114 final | primary | verified |
| stm/2020_basic-income-results | Results of the basic income experiment: small employment effects, better perceived economic security and mental wellbeing | primary | verified |
| finland-toolbox/2020_basic-income-experiment | Finland's Basic Income Experiment 2017–2018 | primary | verified |
| uk-gov/2013_what-works-network | What Works Network | primary | verified |
| nao/2021_evaluating-government-spending | Evaluating government spending (summary) | primary | verified |
| fca/2017_sandbox-lessons-learned | Regulatory sandbox lessons learned report | primary | verified |
| worldbank/2020_regulatory-sandboxes | Global Experiences from Regulatory Sandboxes | primary | verified |
| texas-sunset/2026_about | About Us (Texas Sunset Advisory Commission) | primary | verified |
| wegrich/2005_sunset-review-clauses | Effectiveness of sunset legislation and review clauses | secondary | verified |
| bar-siman-tov/2018_temporary-legislation | Temporary legislation, better regulation, and experimentalist governance: An empirical study | primary | partial |
| underhill-ayres/2022_sunsets-are-for-suckers | Sunsets Are for Suckers: An Experimental Test of Sunset Clauses | primary | verified |
| uk/2020_coronavirus-act | Coronavirus Act 2020, sections 89 and 98 (as enacted) | primary | verified |
| oecd/2020_cracking-the-code | Cracking the Code: Rulemaking for humans and machines | primary | verified |
| nz-dia/2018_better-rules-discovery | Better Rules for Government Discovery Report | primary | verified |
| merigoux/2021_mlang | A Modern Compiler for the French Tax Code | primary | partial |
| merigoux/2021_catala | Catala: A Programming Language for the Law | primary | partial |
| goutagny/2024_cutecat | CUTECat: Concolic Execution for Computational Law | primary | verified |
| tauberer/2018_github-pull-request | How I changed the law with a GitHub pull request | secondary | verified |
| dccouncil/2026_law-xml | DCCouncil/law-xml (GitHub repository) | primary | verified |
| robodebt-rc/2023_report | Report of the Royal Commission into the Robodebt Scheme | primary | verified |
| feichtinger/2023_hidden-shortcomings-daos | The Hidden Shortcomings of (D)AOs: An Empirical Study of On-Chain Governance | primary | verified |
| schwaninger-scheef/2016_test-of-vsm | A Test of the Viable System Model: Theoretical Claim vs. Empirical Evidence | primary | verified |
| medina/2011_cybernetic-revolutionaries | Cybernetic Revolutionaries: Technology and Politics in Allende's Chile | secondary | partial |
| medina/2006_designing-freedom | Designing Freedom, Regulating a Nation: Socialist Cybernetics in Allende's Chile | secondary | partial |
| morozov/2014_planning-machine | The Planning Machine | secondary | verified |
| atlanta-fed/2026_gdpnow | GDPNow | primary | verified |
| lazer/2014_parable-google-flu | The Parable of Google Flu: Traps in Big Data Analysis | primary | partial |
| phe/2020_delayed-reporting | PHE statement on delayed reporting of COVID-19 cases | primary | verified |
| nz-treasury/2019_wellbeing-budget | The Wellbeing Budget 2019 | primary | verified |
| pce/2021_wellbeing-budgets-faq | Wellbeing budgets and the environment: A promised land? Frequently asked questions | primary | verified |
| mhwc/2024_budget-investment-report | Where did the $1.9 billion Wellbeing Budget go? | primary | verified |
| nzccss/2025_public-finance-amendment-bill | Public Finance Amendment Bill (NZCCSS submission) | secondary | verified |
| bevan-hood/2006_whats-measured | What's measured is what matters: targets and gaming in the English public health care system | primary | partial |
| pik/2026_planetary-health-check | Planetary Health Check 2026 (full report) | primary | verified |
| deal/2026_what-is-the-doughnut | What is the Doughnut? | primary | verified |
| ostrom/2009_beyond-markets-and-states | Beyond Markets and States: Polycentric Governance of Complex Economic Systems | primary | verified |
| uk-parliament/2026_petitions-help | How petitions work | primary | verified |
| uk-parliament/2026_archived-petitions-2019-2024 | Archived petitions, 2019 to 2024 Parliament | primary | verified |
| leston-bandeira/2019_e-petitions | Parliamentary petitions and public engagement: an empirical analysis of the role of e-petitions | primary | partial |
| bertelsmann/2022_taiwan-join-vtaiwan | Shortcut 8: Trailblazers of digital participation: Taiwan's Join platform and vTaiwan | secondary | verified |
| royo/2020_decide-madrid | Decide Madrid: A Critical Analysis of an Award-Winning e-Participation Initiative | primary | verified |
| decidim/2026_homepage | Decidim (home page) | primary | verified |
| decidim/2026_barcelona-budgeting | Participatory Budgets 2020-2023 in Barcelona | primary | verified |
| consul-democracy/2026_homepage | CONSUL DEMOCRACY (home page) | primary | verified |
| borge/2022_decidim-catalonia | Democratic Disruption or Continuity? Analysis of the Decidim Platform in Catalan Municipalities | primary | partial |
