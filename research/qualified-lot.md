# The qualified lot: drawing by lot among the qualified

*Research note · planetary government, round 3 · first pass, 12 October 2026 · compiled by Claude, not yet reviewed by Kara*

Drawing by lot among the qualified has worked where the gate is a published pass mark, the pool is large and public, and anyone can check the draw. The IETF has drawn its nominating committee by lot since 1993, and at least five research funders have drawn among proposals that pass a quality screen. Both rest on one premise: peer judgement can screen out weak candidates, and evidence shows it cannot reliably rank strong ones. Florence and Venice show the failure: a fair draw from a pool the powerful control changes little. The best-documented open pool, the IETF's, skews toward North America and Europe, men, a few large employers and fluent English speakers. The evidence fits a qualified lot for technical review and the Guardians' scientific half; drafting by lot is untested. It supports criteria set by bodies drawn from all terrans, several free routes in, expiry, affiliation caps, and the last word for the common lot.

## What the Charter says now

- **4.4.** Candidates for Steward, judge, ombudsman and the independent offices "are certified against criteria published in advance by planetary act". "Anyone who meets the criteria may enrol on an open roster." Each certifying panel has "a majority drawn by lot from all terrans and experts drawn from the rosters".
- **4.5, 7.2, 7.11 and 5.1.** The independent offices and the Ombudsman council are drawn by lot from certified candidates. An assembly drawn by lot chooses judges from them, and Stewards come from a certified pool.
- **4.3.** Draws use public seeds and three or more operators; draws from all terrans are stratified by region, age, gender, education and language.
- **8.3.** Half the Guardians are drawn from all terrans and half "nominated by scientific bodies". Which bodies, without nations, is unanswered (strain 2 in [pressure points](../thoughts/pressure-points.md)).
- **3.3.** Assemblies drawn from all terrans study proposals "with experts and Guardians" and draft law. The draft does not say who picks the experts.

Kara's working design adds a second lot: a common lot from all terrans decides; a qualified lot from open, earnable, expiring pools does craft work. This note covers the qualified lot; companion notes cover [isonomy](isonomy.md) and [mixed lay–expert panels](mixed-panels.md). Round 2 covered the IETF's lottery ([polycentric governance](polycentric-governance.md)), open-source councils ([modern governance](modern-governance.md)) and merit civil services ([executive and administration](executive-and-administration.md)).

## The IETF's nominating committee

The IETF's nominating committee (NomCom) picks candidates for leadership posts, which other bodies confirm. Its ten voting members are drawn from eligible volunteers by a method that uses random data unknown until the day, is checkable by anyone, and yields an ordered list for replacements [ietf/2020_rfc-8713]. RFC 3797 hashes the results of named public lotteries: "Three or four would be a good number of sources. Ten is too many." For the first three committees, from 1993, a member of the clergy drew names from a receptacle; an algorithm took over in 1997 [ietf/2004_rfc-3797].

| Rule | Who may volunteer |
|---|---|
| RFC 8713 (2020) | Attended three of the last five meetings; in practice, in person [ietf/2020_rfc-8713; ietf/2023_rfc-9389] |
| RFC 8989 (experiment, 2021) | Any one of three paths: three of five meetings, online counting for online meetings; working-group chair or secretary in the past three years; author or editor of two IETF-stream RFCs in the past five years [ietf/2021_rfc-8989] |
| RFC 9389 (2023, current) | The three paths kept; online attendance means logging in to at least one session [ietf/2023_rfc-9389] |

Each path is a rolling window, so eligibility lapses on its own. RFC 8989 rejected drafts, list mail and reviews as "not truly indicating effective IETF participation", and allowed "no qualitative evaluation" [ietf/2021_rfc-8989]. People on the bodies the committee fills may not volunteer, and members cannot be chosen for posts their own committee fills [ietf/2020_rfc-8713].

| Cycle | Volunteers | Note |
|---|---|---|
| Early 2000s | About 100 | [ietf/2004_rfc-3797] |
| 2020 | 135 | Under the proposed paths, 842 people were eligible by attendance and 1,541 by chairing or authorship [ietf/2021_rfc-8989] |
| 2022 | 267 | 8 qualified by chairing or authorship alone; the rest by attendance (my count) [ietf-nomcom/2022_final-list-of-volunteers] |
| 2023 | 268 | Volunteers from meeting registration were "not initially added" [ietf-nomcom/2023_final-eligible-volunteers] |
| 2024 | 163 | After a software bug was fixed, only 100 were eligible at one point [ietf-nomcom/2024_help-with-call-for-volunteers; ietf-nomcom/2024_final-list-of-volunteers] |
| 2025 | 192 | [ietf-nomcom/2025_eligible-volunteers] |
| 2026 | 168 | My count of the final list [ietf-nomcom/2026_final-list] |

**Affiliation.** No more than two of the ten may share a primary affiliation; the chair skips down the ordered list [ietf/2020_rfc-8713]. Chairs count subsidiaries as their parent, and find blank or "independent" entries hard to judge [ietf-nomcom/2025_update-on-volunteers].

**Capture.** RFC 9389 calls capture "the most potent threat". Counting online attendance cut the cost of an eligible volunteer from three trips "of around five days each" to "zero financial cost". For even odds of six seats an attacker needs "roughly 60% of the volunteer pool". A sudden surge of unknown volunteers is "an early-warning sign". One person can now qualify several online identities; for that, the RFC points to the recall procedure [ietf/2023_rfc-9389].

**Checks in practice.** In 2022 a chair withdrew a draw because "nobody can repeat my results" [ietf-nomcom/2022_selection-is-wrong]. In 2024 a stray line break in the seed file changed the result, and a corrected draw followed the same day [ietf-nomcom/2024_selection-results-correction].

**Design implication:** Use machine-checkable pass marks with several lapsing routes, publish the pool with affiliations, and allow challenges. Most volunteers take the cheapest route.

## Lotteries among qualified applicants in research funding

In partial, or focal, randomisation, reviewers sort proposals into worthy and not, and a draw chooses among the worthy [rori/2023_experimental-funders-handbook].

| Funder and scheme | Since | Screen | Draw | Scale |
|---|---|---|---|---|
| Health Research Council of New Zealand (HRC), Explorer Grants | 2013 | Three assessors judge set criteria, yes or no | All fundable proposals randomly ordered | NZ$150,000 each; 56 of 394 applications funded, 2013–2019 [liu/2020_lottery-acceptability-survey; hrc/2025_explorer-grant-guidelines-2026] |
| Swiss National Science Foundation (SNSF), all schemes | 2021, after a pilot | Panels rank as usual | Only proposals that "cannot be further differentiated"; filmed physical draw | 9 of 278 proposals in one 2021 round [snsf/2021_drawing-lots-tie-breaker] |
| Volkswagen Foundation, Experiment! | 2017–2021 | Office check, then an anonymous jury of eight to ten | About half of grantees drawn from the jury's pool | 117 of 2,748 applications funded [simon/2025_lottery-drum-experiment] |
| Austrian Science Fund (FWF), 1000 Ideas | 2019 | Double-blind review and a jury | A subset drawn from proposals deemed worthy | 107 of 1,135 applications, five calls [vingre/2026_fwf-1000-ideas-evaluation] |
| British Academy/Leverhulme Small Research Grants | 2022, extended to 2028 | Fellows apply a quality threshold; about 60% pass | Random above the threshold | Applications up from about 600 to over 1,100 a round [british-academy/2025_partial-randomisation-extended] |

**Can screen, cannot rank.** Among 102,740 NIH grants scored in the top 20 percentiles, the score explained 0.98% of the variance in productivity [fang/2016_nih-percentile-scores]. When 43 reviewers rated 25 strong NIH applications, they showed no agreement; the outcome "depended more on the reviewer to whom the grant was assigned than the research proposed" [pier/2018_low-agreement-nih-reviewers]. SNSF fellowship panels agreed only "poor to fair" [heyard/2022_funding-line-bayesian-lottery]. A 2018 review of 105 papers, as RoRI summarises it, found "a paucity of evidence for the effectiveness of peer review" and "strong evidence of bias against innovative research" [woods/2021_randomisation-scoping-rori-wp4]. Between equal proposals, judgement risks "the subconscious biases of evaluators" [snsf/2021_drawing-lots-tie-breaker]. Lot is "a useful supplement – but not an alternative – to peer review" [volkswagenstiftung/2020_eight-theses-random-element].

**Acceptance is conditional.** Of 126 HRC applicants surveyed, 63% found the lottery acceptable for Explorer Grants and 25% did not; for other grants the split was 40% to 37%. Winners approved more (78%) than those the panel declined (44%). Ten respondents would fund "stand out applications" on merit and draw only among the rest [liu/2020_lottery-acceptability-survey]. Of Experiment! grantees, 88% said lotteries help avoid conflicts of interest, yet 70% feared lower-quality projects [simon/2025_lottery-drum-experiment]. At the FWF, about half of awardees and of unfunded applicants linked the lottery to low quality, and only 60% of awardees knew it existed [vingre/2026_fwf-1000-ideas-evaluation]. Critics fear stigma, lost trust in peer judgement [rori/2023_experimental-funders-handbook], and administrators' biases replacing reviewers' [woods/2021_randomisation-scoping-rori-wp4].

**Effects are modest.** After Experiment! added its lottery, early-career grantees rose from about 42% to 47%, on "relatively small" numbers [simon/2025_lottery-drum-experiment]. The Foundation reports "very similar research outputs and outcomes" from lottery and jury picks [dora/2025_vw-partial-randomization]. Under the FWF's lottery, novelty counted for more and past citations for less [vingre/2026_fwf-1000-ideas-evaluation]. British Academy awards to researchers of Asian or Asian British heritage rose from 11% to 17% [british-academy/2025_partial-randomisation-extended]. Most HRC applicants saved no time: 75% said the lottery made no difference, as they still had to pass the screen [liu/2020_lottery-acceptability-survey]. Real-world studies "remain rare" [woods/2021_randomisation-scoping-rori-wp4].

The HRC drew with a spreadsheet's Rand() function [liu/2020_lottery-acceptability-survey], uncheckable from outside; the SNSF films its draws [snsf/2021_drawing-lots-tie-breaker].

**Design implication:** A pass mark set in advance, then an equal draw, wins acceptance where candidates near the line look alike and stakes are small. Expect calls to fund stand-outs on merit.

## Lot among the pre-approved: Florence and Venice

**Florence.** From 1328 Florence filled its highest offices by drawing names from purses after periodic scrutinies of eligible candidates, who had to belong to a guild [herlihy/2000_online-tratte-overview]. Commissions voted on names by secret ballot, and only the scrutineers knew who had passed. A name became public only when drawn, and its holder took office only if, say, his taxes were paid. Signoria terms lasted two months [fubini/2014_cosimo-de-medici-regime]. With short terms, the system "guaranteed comparatively broad participation" and limited rent-extraction for decades [belloc/2024_medici-quiet-coup].

Control came through the gate. Scrutinies were due about every five years, but "it could be to the advantage of the group in power to delay holding a scrutiny". From about 1387 a small purse of men thought loyal supplied half the priors from the major guilds [herlihy/2000_online-tratte-overview]. Under the Medici, from 1434, a government-named commission ran the scrutinies. For the Signoria, the *accoppiatori* who filled the purses gained "large discretionary power" and kept the purses themselves, instead of the friars of Santa Croce [belloc/2022_medici-institutional-capture]. They often filled offices *a mano*, picking trusted names, "without, however, marking an official departure from the city's constitutional system" [fubini/2014_cosimo-de-medici-regime]. The pool even widened: over 100 of about 500 families first held office, yet surname and faction came to predict office far more than before. After the capture, office-holding went with faster wealth growth, and the Republic paid higher interest to lenders with more terms in office [belloc/2022_medici-institutional-capture; belloc/2024_medici-quiet-coup]. The standard accounts by Rubinstein and Najemy could not be opened [rubinstein/1966_government-of-florence-medici; najemy/1982_corporatism-and-consensus].

**Venice.** From 1268 to 1797 Venice elected its doge in ten rounds that alternated lot and election. Lot shrank each college and approval votes rebuilt it (30, 9, 40, 12, 25, 9, 45, 11, 41); the last 41 chose the doge with 25 approvals or more. Only Great Council members aged 30 or over took part, never two of one family in a college. The design "offers some resistance to corruption of voters", but the list of council families was "closed" in 1297, and 70 of the 75 doges chosen this way came from families seated that year [mowbray/2007_electing-doge-venice].

**Design implication:** A draw is only as fair as its pool, and whoever writes the list holds the power, even as the list grows. Florence's list was secret; the IETF's is published.

## Earnable, lapsing membership in open communities

**Debian.** Anyone can contribute to Debian; full membership, with a vote and upload rights, is earned. Applicants for upload rights "should have a track record of maintaining packages for at least six months" [debian/2026_new-members-corner]. Two members must sign the applicant's key after meeting them in person and seeing ID [debian/2026_nm-step2-identification]. Applicants must understand Debian's Social Contract and Free Software Guidelines well enough to express them "in their own words" [debian/2026_nm-step3-philosophy]. Developers who retire properly become "emeritus" and can return by a shortened process; others are "removed" and start again [debian/2026_developers-reference-duties].

**Wikipedia.** English Wikipedia grants administrator rights "indefinitely", but removes them after 12 months with no edits or actions, or fewer than 100 edits in 60 months. Former administrators can usually ask for the tools back, and the policy warns against "token edits to avoid loss of administrative permissions" [wikipedia/2026_administrators-policy].

**Design implication:** Beyond round 2's [modern governance](modern-governance.md), what matters is the life cycle: entry by shown work and stated principles, lapse by inactivity, a cheap way back, and a guard against token activity.

## Rule by the knowledgeable: the epistocracy debate

Jason Brennan calls democracy "the rule of the ignorant and the irrational" and argues that epistocracy, "the rule of the knowledgeable", may be better [brennan/2016_against-democracy]. A review lists his variants: votes only for those who pass a basic knowledge test; extra votes for them; extra weight for knowledgeable members of under-represented groups; and an "enfranchisement lottery" [somin/2016_democracy-vs-epistocracy]. He also proposes a "government by simulated oracle" [lopez-guerra/2020_enfranchisement-lottery]. I could not open the book itself, so its full list, including any veto by the knowledgeable, is unconfirmed [brennan/2016_against-democracy]. The reviewer, Ilya Somin, expects governments to tilt tests and lotteries "in ways that overrepresent supporters of the party in power" [somin/2016_democracy-vs-epistocracy].

Claudio López-Guerra reverses the order: draw first, then build competence. Before each election all but a random sample would lose the vote, and the sample would go through "a competence-building process". Because the sample starts as a microcosm, this "neutralizes potential complaints about unjust biases". He accepts as "true" Somin's objection that "whoever designs the jury deliberation process will have enormous opportunity and incentive to skew it", but notes that tests can be skewed too [lopez-guerra/2020_enfranchisement-lottery].

David Estlund holds that expertise can justify power only if it is "acceptable from all reasonable points of view" [estlund/2008_democratic-authority]. His "demographic objection" holds that any test of expertise tends to select a demographically narrow group whose biases undermine the general welfare [christiano/2024_sep-democracy].

Hélène Landemore argues that "more is smarter", which for assemblies of capped size favours random selection [landemore/2013_deliberation-cognitive-diversity]. She draws on Hong and Page's "diversity trumps ability" result [christiano/2024_sep-democracy]. Their framing is itself a qualified lot: 1,000 applicants score 60% to 90% on a test, "so that they are all individually capable"; should an organisation hire the 20 next-best or 20 at random? In one simulation run, ten random agents scored 94.7 together, against 93.2 for the ten best [hong/2004_diverse-problem-solvers]. Abigail Thompson replies that the theorem "is incorrect as stated", trivial once corrected, and that the simulation shows "the benefits of randomness, not 'diversity'" [thompson/2014_diversity-trump-ability].

**Design implication:** The debate has two orders: qualify then draw (the IETF, the funders, the qualified lot), and draw then train (López-Guerra, the Charter's assemblies). The demographic objection bites hardest on the first, so decisions belong with the common lot.

## Experts governing their own field: capture

North Carolina's dental board had six practising dentists, elected by other dentists, among its eight members. It sent at least 47 cease-and-desist letters to cheaper non-dentist teeth whiteners, who stopped offering the service. The US Supreme Court held, 6–3, that a board where "a controlling number of decisionmakers are active market participants" is immune from antitrust law only under active state supervision: "When a State empowers a group of active market participants to decide who can participate in its market, and on what terms, the need for supervision is manifest." The Court cited "structural risk", not bad faith; the dissent noted an earlier case upheld a scheme that "gave decisive power to market participants" [us-supreme-court/2015_nc-dental-v-ftc].

A 2015 US Treasury, Council of Economic Advisers and Labor Department report found about 25% of US workers in state-licensed jobs, up from under 5% in the early 1950s. Licensed workers earned 10% to 15% more than comparable unlicensed ones, and stricter licensing raised prices in 9 of 11 studies. There was "less evidence" that licensing restricts supply. Board members from the profession are "more likely than public members to favor the interests of their profession". California put public-member majorities on some boards in the 1970s, yet "there is little reliable empirical evidence regarding the effectiveness of this reform" [us-treasury/2015_occupational-licensing-framework].

**Design implication:** Let experts qualify, but do not let those who gain from restricting entry write the entry rules. The evidence that lay members cure capture is thin.

## Lived experience as qualification

England's Care Quality Commission (CQC) takes "Experts by Experience" on inspections. They need "recent personal experience (within the last eight years)" of using, or caring for someone who uses, the services it regulates; it lists 20 kinds. A contractor runs the programme on a three-year contract from April 2026 [cqc/2026_experts-by-experience]. That contractor, Choice Support, has worked with the CQC since 2010, and recruits, trains and manages the experts as paid staff [choice-support/2026_cqc-experts-by-experience].

The role has proved fragile. The share of social care inspections with an expert fell from 72% in late 2014 to 23% in early 2016, after most regional contracts moved to a new provider, and was 57% in late 2017 [disability-news-service/2018_exe-inspections-fallen]. In 2019 experts said one contractor paid £9 an hour and the other £15, and complained of poor training [accessable/2019_cqc-exe-contracts].

In research, the UK Standards for Public Involvement ask whether barriers "such as payment for time or accessible locations" have been addressed; one user wrote, "Diversity is a weakness in PPI" [nihr/2023_uk-standards-inclusive-opportunities]. An NIHR-funded network pays £27.50 an hour, but warns that payment may affect welfare benefits [nihr-arc-eoe/2026_public-contributor-payment-guide].

**Design implication:** Lived experience is a route experts lack, and recency windows suit it. It needs paid time that keeps people's benefits, training, and contracts that cannot quietly cut pay or coverage.

## Who ends up qualified

**Region, gender and language.** In the IETF's 2023 survey, North America and Europe each supplied about 40% of participants and Asia 11%; 7.84% of respondents were women. Asian and Latin American participants reported weaker spoken English, and meeting costs hampered those from Asia, Africa and Latin America [ietf/2024_community-survey-2023]. By 2025 women were 9.82% of regular participants, up from 5.42%, and former leaders raised "corporate capture" [ietf/2026_community-survey-2025].

**Employers.** By my count, 94 of the 192 NomCom volunteers in 2025 (49%) named one of six firms, led by Huawei companies (30) and Cisco (20) [ietf-nomcom/2025_eligible-volunteers]. In 2026, 98 of 168 (58%) named one of seven, led by Huawei (31) and Cisco (27) [ietf-nomcom/2026_final-list]. The affiliation cap limits seats, not the pool's makeup.

**Access.** Debian's key-signing rule assumes a member nearby; its guide asks developers on holiday to offer key signing, especially in places "where we don't have any developers yet" [debian/2026_developers-reference-duties].

**Pool growth.** Pools grew once lotteries began: British Academy applications by about 70% [british-academy/2025_partial-randomisation-extended], and Experiment! from 704 applications in four years to 2,748 in five [simon/2025_lottery-drum-experiment]. Growth means more screening: in 2013 the HRC judged 99 of 116 applications ineligible [liu/2020_lottery-acceptability-survey].

**Scientists without nations.** IPCC authors are nominated by governments, observer organisations and the Bureau, which balances gender, region and developing countries. Review is open: first-stage expert reviewers "self-nominate and are accepted by the IPCC on the basis of relevant expertise", and every comment and response is published [ipcc/2026_preparing-reports].

**Design implication:** Publish each pool's makeup, expect skew, and decide in advance whether to stratify; quotas on a skewed pool make chances unequal ([sortition at scale](sortition-at-scale.md)).

## Which work suits a qualified lot

Drafting help is the clearest gap. In France's climate convention, expert groups of six and 19, appointed by the organisers' committee, helped write proposals; some experts were seen "unduly pushing for certain measures or discarding others", and members drew up only about a fifth of the measures [giraudet/2022_co-construction-ccc]. A qualified lot would change who picks such helpers, not whether they are needed.

| Work | Lot the evidence points to | Basis |
|---|---|---|
| Deciding acts (3.4), the agenda (3.3), oversight (5.2) | Common | Value choices; qualified pools skew |
| Writing qualification criteria (4.4) | Common, advised by practitioners | Practitioner boards restrict entry |
| Certifying candidates (4.4) | Mixed | See [mixed panels](mixed-panels.md) |
| Drafting aid (3.3) | Qualified, answerable to the assembly | Untested; replaces helpers picked by organisers |
| Technical review and impact statements (8.4) | Qualified, from an open roster | Needs expertise; the IPCC opens review to volunteers |
| Independent offices (4.5) | Qualified, as now | No change |
| Guardians' scientific half (8.3) | Qualified, from a roster of scientists | Ends the dependence on nations |

## Design patterns that work

- **Pass mark, then an equal draw** (HRC, British Academy, Volkswagen, FWF, IETF). Fails when screeners also decide who enters the pool, as in Florence.
- **Several cheap, checkable routes** (IETF). Fails when the cheapest route swamps the rest, or lets one person qualify several identities.
- **Rolling windows with a way back** (IETF, Debian, Wikipedia, CQC). Fails on token activity.
- **A public, ordered pool, public seeds and a challenge period** (IETF). Caught errors in 2022 and 2024.
- **Affiliation caps that count subsidiaries** (IETF; also Python and Rust in [modern governance](modern-governance.md)). Fails on vague "independent" labels.
- **Outsiders write the entry rules** (public members on licensing boards; supervision after the dental board case). Plausible but unmeasured.
- **Paid, trained lived-experience roles with recency rules** (CQC, NIHR). Fails when contractors cut pay and coverage.
- **A broader body keeps the last word** (the IETF's confirming bodies; the HRC's Council; the FWF's Scientific Board).

## Tensions and open problems

- **Open against cheap to fake.** Lower barriers widen the pool and the attack surface together [ietf/2023_rfc-9389].
- **Qualified against representative.** Any pass mark tracks advantage; stratifying a skewed pool gives up equal chances.
- **Threshold against stand-outs.** Lot assumes those above the bar are interchangeable; many applicants want clear winners chosen on merit.
- **Who writes the bar.** Practitioners know the craft but restrict entry; evidence on lay members is thin.
- **Expiry against continuity.** Short windows invite token activity; long ones entrench incumbents. No source tests the right length.
- **Acceptance and pay.** Lotteries win acceptance for small, risky grants, most among winners; paid service can cost people benefits.
- **Scale.** The evidence comes from pools of about 100 to 1,100 a round and small grants; nothing tests a planetary roster or drafting by lot.
- **Not found or not opened.** Rubinstein's, Najemy's, Estlund's and Brennan's books, and the British Academy's independent analysis.

## Options for the next draft

- **Article 4, new clause: two lots.** Name the common lot (all terrans, 4.3) and the qualified lot (open rosters, 4.4), and list which bodies each fills; deciding, agenda, oversight and criteria panels stay common.
- **4.4: rosters for craft work.** Extend rosters to drafting aides, technical reviewers and scientists, each with at least two free routes, such as a credential, a record of work or lived experience, and identity checks that need no member nearby.
- **4.4: expiry.** A roster place could lapse after a set window without qualifying activity, say five years, with a short way back.
- **4.4: who sets the bar.** A panel drawn from all terrans could propose each roster's criteria, advised by practitioners, for adoption by planetary act. No body of practitioners would set its own entry rules; refusals stay appealable to the Court.
- **4.3: qualified draws.** Publish each pool in draw order with affiliations, allow a challenge week, and draw an ordered reserve. Cap any employer or institution at two seats in ten, counting subsidiaries. Decide per roster whether to stratify by region and language.
- **Conflicts.** Drawn experts would declare interests and step aside where they or their employers gain.
- **3.3: drafting aid.** Option A: draw each assembly's drafting aides and reviewers from rosters, rotating and answerable to the assembly. Option B: keep hired staff under an allotted oversight council, as [sortition at scale](sortition-at-scale.md) suggests.
- **8.3: the scientific half.** Option A: draw it from a roster of scientists qualified under 4.4, with field and region strata and an institution cap. Option B: keep nominations, with lot from the roster as the fallback ([long view](long-view.md)).
- **The last word.** Say that qualified lots draft, review, certify and advise, and the common lot decides (3.4).
- **Monitoring and pay.** The Statistics Office could publish each roster's makeup yearly and flag surges; pay, set centrally, should not cost people benefits.
- **Proven before binding (9.7).** Run each qualified lot as advisory first, with the Audit Office checking its pools.

## Sources

| Source id | Title | Tier | Checked |
|---|---|---|---|
| ietf/2020_rfc-8713 | RFC 8713: IAB, IESG, IETF Trust, and IETF LLC Selection, Confirmation, and Recall Process | primary | verified |
| ietf/2021_rfc-8989 | RFC 8989: Additional Criteria for Nominating Committee Eligibility | primary | verified |
| ietf/2023_rfc-9389 | RFC 9389: Nominating Committee Eligibility | primary | verified |
| ietf/2004_rfc-3797 | RFC 3797: Publicly Verifiable Nominations Committee (NomCom) Random Selection | primary | verified |
| ietf-nomcom/2022_final-list-of-volunteers | Final list of volunteers (NomCom 2022–2023) | primary | verified |
| ietf-nomcom/2022_selection-is-wrong | NomCom selection is wrong | primary | verified |
| ietf-nomcom/2023_final-eligible-volunteers | NomCom 2023 Final Announcement of Eligible Volunteers | primary | verified |
| ietf-nomcom/2024_help-with-call-for-volunteers | Help with call for volunteers | primary | verified |
| ietf-nomcom/2024_final-list-of-volunteers | Updated and final list of volunteers for NomCom 2024-2025 | primary | verified |
| ietf-nomcom/2024_selection-results-correction | Correction in NomCom 2024 Volunteer Selection Results | primary | verified |
| ietf-nomcom/2025_eligible-volunteers | NomCom 2025-2026 Announcement of Eligible Volunteers | primary | verified |
| ietf-nomcom/2025_update-on-volunteers | NomCom 2025-2026 Update on Volunteers | primary | verified |
| ietf-nomcom/2026_final-list | NomCom 2026-2027 Announcement of Eligible Volunteers - Final list | primary | verified |
| ietf/2024_community-survey-2023 | IETF Community Survey 2023 | primary | verified |
| ietf/2026_community-survey-2025 | IETF Community Survey 2025 | primary | verified |
| rori/2023_experimental-funders-handbook | The experimental research funder's handbook (2nd edition) | secondary | verified |
| liu/2020_lottery-acceptability-survey | The acceptability of using a lottery to allocate research funding: a survey of applicants | primary | verified |
| hrc/2025_explorer-grant-guidelines-2026 | 2026 Explorer Grant Application Guidelines | primary | verified |
| snsf/2021_drawing-lots-tie-breaker | Drawing lots as a tie-breaker | primary | verified |
| simon/2025_lottery-drum-experiment | Everyone Is Equal in the Lottery Drum | primary | verified |
| vingre/2026_fwf-1000-ideas-evaluation | Evaluation of the Austrian Science Fund (FWF) 1000 Ideas programme | primary | verified |
| british-academy/2025_partial-randomisation-extended | Partial randomisation trial extended | primary | verified |
| fang/2016_nih-percentile-scores | NIH peer review percentile scores are poorly predictive of grant productivity | primary | verified |
| pier/2018_low-agreement-nih-reviewers | Low agreement among reviewers evaluating the same NIH grant applications | primary | verified |
| heyard/2022_funding-line-bayesian-lottery | Rethinking the Funding Line at the Swiss National Science Foundation: Bayesian Ranking and Lottery | primary | verified |
| woods/2021_randomisation-scoping-rori-wp4 | Experiments with randomisation in research funding (RoRI Working Paper No. 4) | secondary | verified |
| volkswagenstiftung/2020_eight-theses-random-element | 8 Theses for Introducing a Random Element | primary | verified |
| dora/2025_vw-partial-randomization | Insights on Partial Randomization in Research Funding: Learnings from the Volkswagen Foundation | secondary | verified |
| herlihy/2000_online-tratte-overview | Online Tratte of Office Holders 1282–1532: Brief Historical Overview | secondary | verified |
| fubini/2014_cosimo-de-medici-regime | Cosimo de' Medici's regime: his rise to power (1434) | secondary | verified |
| belloc/2024_medici-quiet-coup | The Medici's quiet coup | primary | verified |
| belloc/2022_medici-institutional-capture | Wealth Accumulation and Institutional Capture (CEPR DP17456) | primary | verified |
| rubinstein/1966_government-of-florence-medici | The Government of Florence under the Medici (1434 to 1494) | secondary | unverified |
| najemy/1982_corporatism-and-consensus | Corporatism and Consensus in Florentine Electoral Politics, 1280–1400 | secondary | unverified |
| mowbray/2007_electing-doge-venice | Electing the Doge of Venice: Analysis of a 13th Century Protocol | secondary | verified |
| debian/2026_new-members-corner | Debian New Members Corner | primary | verified |
| debian/2026_nm-step2-identification | Step 2: Identification | primary | verified |
| debian/2026_nm-step3-philosophy | Step 3: Philosophy and Procedures | primary | verified |
| debian/2026_developers-reference-duties | Debian Developer's Reference, chapter 3: Debian Developer's Duties | primary | verified |
| wikipedia/2026_administrators-policy | Wikipedia:Administrators | primary | verified |
| brennan/2016_against-democracy | Against Democracy | primary | partial |
| somin/2016_democracy-vs-epistocracy | Democracy vs. Epistocracy | secondary | verified |
| lopez-guerra/2020_enfranchisement-lottery | Democrats, Epistocrats, and the Enfranchisement Lottery | primary | verified |
| christiano/2024_sep-democracy | Democracy (Stanford Encyclopedia of Philosophy) | tertiary | verified |
| estlund/2008_democratic-authority | Democratic Authority: A Philosophical Framework | primary | partial |
| landemore/2013_deliberation-cognitive-diversity | Deliberation, cognitive diversity, and democratic inclusiveness | primary | partial |
| hong/2004_diverse-problem-solvers | Groups of diverse problem solvers can outperform groups of high-ability problem solvers | primary | verified |
| thompson/2014_diversity-trump-ability | Does Diversity Trump Ability? | secondary | verified |
| us-supreme-court/2015_nc-dental-v-ftc | North Carolina State Board of Dental Examiners v. Federal Trade Commission, 574 U.S. 494 (2015) | primary | verified |
| us-treasury/2015_occupational-licensing-framework | Occupational Licensing: A Framework for Policymakers | primary | verified |
| cqc/2026_experts-by-experience | Experts by Experience | primary | verified |
| choice-support/2026_cqc-experts-by-experience | CQC Experts by Experience | primary | verified |
| disability-news-service/2018_exe-inspections-fallen | Watchdog's use of service-user inspection scheme has fallen sharply since 2015 | secondary | verified |
| accessable/2019_cqc-exe-contracts | Care watchdog criticised over abandoned bid to replace service-user contracts | secondary | verified |
| nihr/2023_uk-standards-inclusive-opportunities | UK Standards for Public Involvement: Inclusive Opportunities | primary | verified |
| nihr-arc-eoe/2026_public-contributor-payment-guide | ARC East of England Public Contributor Payment Guide (version 6) | primary | verified |
| ipcc/2026_preparing-reports | Preparing Reports | primary | verified |
| giraudet/2022_co-construction-ccc | “Co-construction” in deliberative democracy: lessons from the French Citizens' Convention for Climate | primary | verified |
