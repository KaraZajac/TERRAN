# How a planetary government fails: a threat model

*Research note · planetary government, round 2 · first pass, 11 October 2026 · compiled by Claude, not yet reviewed by Kara*

Modern democracies rarely fall to coups; they erode when elected leaders use emergencies, courts and amendments while keeping the forms of law. Emergencies made erosion 75% more likely in one study, and more executive emergency power went with more disaster deaths, not fewer. Hungary and Poland began to recover only through competitive elections and outside courts, two checks a single planetary polity would lack. An efficient Terran government can streamline voting and administration, but it must keep rival centres, self-expiring emergency powers, funded inspection and a way out.

## What the Charter says now

- **Who decides.** Every terran votes on planetary questions (VII.3, VIII.4), on ballots written by an assembly drawn by lot (VIII.3). Kara's steer of 11 October 2026 drops universal voting on every question; this note covers threats to whatever replaces it.
- **Who acts.** An elected Council of Stewards serves "one fixed term", with "no veto" and "no army" (VIII.7). Its size and removal are unstated.
- **Who checks.** Powers are split four ways (VIII.8). An Ombudsman may investigate anyone (VIII.9, IX.10). A Planetary Court hears anyone, reads by spirit and directs the inspectors (IX.1–3, XI.2).
- **Who guards the long term.** Guardians have automatic successors (X.3) and a protected budget share (X.7). A failed long-view test delays a decision by a year (X.4).
- **Who can leave.** Individuals may leave communities (VI.3, VIII.10); members may leave the Commonwealth only until stage three (XII.4–5).
- **What is missing.** An emergency clause, a list of planetary powers (VII.4), and a funding rule for planetary bodies beyond X.7.

## The threat model in outline

- **Assets:** the floor, the ceiling and the Principles; the repair channels (votes, courts, amendment, exit); watchdogs and their money; the decision pipeline; identity and records.
- **Adversaries:** ambitious Stewards; an over-reaching or captured Court; industries, donors and local elites; insiders who run the machinery; and accidents.
- **Attack paths:** emergencies, legal aggrandizement, capture, lock-in and system failure. Modern designs add algorithmic error, steered AI mediation, staff capture of allotted bodies and digital single points of failure.

## 1. Emergencies: the shortest path to rule by decree

Lührmann and Rooney studied 60 democracies from 1974 to 2016; democracies were 75% more likely to erode under a state of emergency [luhrmann-rooney/2021_autocratization-by-decree].

Extra power did not buy better outcomes. Across up to 122 countries in 1990–2011, an emergency was declared in 23% of country-years [bjornskov-voigt/2021_emergencies-misuse]. The more an emergency constitution favoured the executive, the more people died in natural disasters, controlling for severity. The authors' best explanation is that governments use disasters "as a pretext to enhance their power". Easier declarations meant more harm to basic rights. In the pandemic, unlawful emergencies were more likely in democracies, and permissive provisions raised the risk [bjornskov-voigt/2025_covid-unlawful-emergencies].

V-Dem's Pandemic Backsliding project tracked 144 countries. In March–December 2020 only 14 had no violations; 51 set no time limit on emergency measures; in 29 the legislature's check was severely undermined [edgell/2021_pandemic-backsliding]. The authors found "no relationship between violations of democratic standards and reported Covid-19 mortality". My count from the final data: by June 2021, 47 countries had at some point run open-ended measures, and 36 still did in April–June 2021. In 39 the executive gained broad decree powers or sidelined the legislature [v-dem/2022_pandem-v6-1].

Checks often held. In more than 100 countries, courts, legislatures and subnational governments constrained pandemic executives [ginsburg-versteeg/2021_bound-executive]. Backsliding states derogated more often, but "derogations had mitigating effects once issued" [comstock-heiss-chaudhry/2024_derogations-backsliding].

**Weimar.** Article 48 let the President take whatever measures public order needed and suspend seven basic rights [germany/1919_weimar-constitution]. The Reichstag could demand repeal, but Article 25 let the President dissolve it. On 18 July 1930 Brüning enacted his tax programme under Article 48, and the Reichstag was dissolved [ghdi/1930_bruening-caricature]. Hindenburg declared emergencies "bereitwillig" (readily). On 28 February 1933 an Article 48 decree suspended those rights "bis auf weiteres" (until further notice) [germany/1933_reichstag-fire-decree]. I could not verify the widely quoted yearly counts of decrees and laws for 1930–32.

**Article 15 of the European Convention.** Derogation needs a "public emergency threatening the life of the nation" and measures "strictly required" [echr/2026_guide-article-15]. Some rights can never be suspended. States get "a wide margin of appreciation", and emergencies need not be temporary; Northern Ireland's lasted years. Review bites at the edges. Strasbourg found no real emergency behind the Greek junta's derogation or Yerevan's post-election protests. A curfew under France's terrorism emergency, imposed before the COP21 summit, was not strictly required (*Domenjoud v. France*, 2024). Without public notice, Article 15 does not apply.

**South Africa.** Section 37 allows a state of emergency only by Act of Parliament, when "the life of the nation" is threatened [south-africa/1996_constitution]. It lapses after 21 days unless the National Assembly extends it, for three months at most. The first extension needs a majority of members, later ones 60%. Any competent court may review it, and some rights are non-derogable. For COVID-19 the government used the Disaster Management Act instead, which lets a minister extend a disaster "for one month at a time" [south-africa/2002_disaster-management-act]. It lasted 750 days, to April 2022, without the Assembly votes section 37 requires [creamer-media/2022_state-of-disaster-ends].

**Hungary.** From 2020 the government ruled by decree, first under pandemic law [edgell/2021_pandemic-backsliding], then under a war-related emergency. The new prime minister ended it on 14 May 2026, closing "rule by decree, introduced six years ago" [european-pravda/2026_magyar-ends-emergency]. Days earlier, parliament turned the war-emergency decrees into law, 190 votes to 6, bypassing standard procedure [xpatloop/2026_decrees-elevated-to-law].

**Sunsets and standards.** Sunset clauses are often renewed "without being adequately revisited", becoming "democracy's snooze button" [kouroutakis-ranchordas/2016_snoozing-democracy]. Three US surveillance powers, first due to expire at the end of 2005, were extended repeatedly and lapsed only on 15 March 2020 [crs/2021_fisa-provisions-expired]. The Venice Commission asks for necessity, proportionality, temporariness and "effective parliamentary and judicial control" [venice-commission/2020_states-of-emergency]. Executive emergency acts should lapse with the emergency unless the legislature confirms them. It adds that "amendments to the constitution should not be made during states of emergency".

**Germany.** A state of defence needs two-thirds of Bundestag votes cast [germany/1949_grundgesetz]. If parliament cannot meet, a Joint Committee of legislators from all parties and the Länder acts. It cannot amend the Basic Law, and its laws lapse within six months of the emergency's end. The weak point: electoral terms falling due are extended (Art. 115h).

**Design implication:** Emergencies are the highest-yield attack path, and concentrated emergency power did not save lives. Safe emergency power is fast for days, renewed by others at rising thresholds, reviewable in court, and defined by effect, not label.

## 2. Executive aggrandizement: legal tools, slow erosion

Bermeo defines backsliding as "the state-led debilitation or elimination of the political institutions sustaining an existing democracy" [bermeo/2016_on-democratic-backsliding]. Open-ended coups and blatant vote fraud declined after the Cold War; promissory coups, executive aggrandizement and strategic manipulation rose. In her coup table, 8 of 22 coups in democracies before 1990 promised a return to democracy (36%). In 1990–2014, 11 of 13 did (85%), by my count [bermeo/2016_coded-coups-supplement]. Levitsky and Ziblatt's publisher sums up their thesis: democracies now die by "the slow, steady weakening of critical institutions" [levitsky-ziblatt/2018_how-democracies-die].

Versteeg and colleagues traced 234 incumbents in 106 countries since 2000 [versteeg/2020_term-limit-evasion]. At least a third of those reaching their limit tried to stay; outside the strongest democracies, about half. None ignored the constitution outright, and 66% of attempts used amendment. About a third of attempts failed, mostly because of "widespread popular resistance". Courts were "mostly ineffectual" and more often validated the attempt.

International bodies show the same pattern. FIFA's 2016 reforms limited presidents to three terms [fifa/2024_statutes]. In December 2022 its Council endorsed reading 2016–2019 as not a term, and Infantino plans to stand in 2027 [maduro-donati/2026_infantino-fourth-term]. A win would mean 15 years in office.

**Hungary.** Fidesz–KDNP won 263 of 386 seats (68%) in 2010 [ipu/2010_hungary-election]. The Venice Commission called its habit of writing struck-down laws into the constitution "a systematic approach" [venice-commission/2013_hungary-fourth-amendment]. The 2013 Fourth Amendment also repealed the Court's earlier case law. The future-generations ombudsman, once able to stop damaging laws, became an advisory deputy [fdsd/2014_hungary-ombudsman]. In 2022 the European Parliament called Hungary "a hybrid regime of electoral autocracy" [european-parliament/2022_hungary-electoral-autocracy]. On 12 April 2026 Tisza won 141 of 199 seats (71%) with 53.18% of list votes [bluewin/2026_tisza-two-thirds-final]. Turnout reached a record 79.5% before polls closed, and OSW credits "an electoral system that rewards the winning party" [osw/2026_hungary-election]. A two-thirds majority enabled capture in 2010; another now enables repair.

**Poland.** In October 2015 the outgoing Sejm chose five constitutional judges, two for seats falling vacant after its own term. The President accepted none of their oaths [venice-commission/2016_poland-constitutional-tribunal]. The new majority's amendments "would have endangered not only the rule of law, but also the functioning of the democratic system". From 2017 politicians chose most members of the judicial council [notes-from-poland/2026_krs-veto]. The EU Court imposed €1,000,000 a day in 2021 over the Supreme Court's Disciplinary Chamber [cjeu/2021_poland-daily-penalty-order]. The EU closed its Article 7 case in May 2024, after a change of government [notes-from-poland/2024_article-7-closed]. Repair has stalled. In February 2026 President Nawrocki vetoed a judicial council reform, citing about 3,000 judges it had appointed [notes-from-poland/2026_krs-veto]. He swore in only two of six constitutional judges chosen this year, and the tribunal rejected a Strasbourg interim measure [notes-from-poland/2026_tk-oath-ruling]. In September the governing majority elected a recent minister as a judge [notes-from-poland/2026_berek-elected].

| Safeguard | Hungary, 2010–2026 | Poland, 2015–2026 |
| --- | --- | --- |
| Supermajority for the constitution | Failed: one party won two-thirds of seats | Held: no two-thirds, so capture ran through statutes |
| Constitutional court | Failed: overruled by amendment | Failed: composition disputed since 2015 |
| Head of state's sign-off | Not covered here | Used as a veto by both camps, 2015 and 2026 |
| Watchdogs | Future-generations ombudsman downgraded | Judicial council captured from 2017 |
| Outside courts and money | Partial and slow (see [accountability](accountability.md)) | €1 million a day; partial compliance |
| Elections | Held: opposition won two-thirds in 2026 | Held: government changed in 2023 |
| Repair | Possible through the same two-thirds rule | Blocked by vetoes and a disputed tribunal |

**Design implication:** The likeliest adversaries are inside: an elected executive, a captured court and whoever controls an appointment chokepoint. What held were elections, outside courts and public resistance, so the design must protect those repair channels and plan repair in advance.

## 3. Capture: industries, donors and elites

Stigler held that "as a rule, regulation is acquired by the industry and is designed and operated primarily for its benefit" [stigler/1971_theory-economic-regulation]. I could not open the article. The quote comes from Carrigan and Coglianese, who find his evidence thin but note that concentrated interests hold real advantages [carrigan-coglianese/2016_stigler-theory].

Participation gets captured too. The World Bank put almost $85 billion into local participatory development in a decade [mansuri-rao/2013_localizing-development]. Participants were typically "wealthier, more educated, of higher social status (by caste and ethnicity), male, and more politically connected". In 1990s Uganda, schools received 13% of their non-wage grants; local officials and politicians captured the rest. After newspapers published monthly transfers, schools near newspaper outlets claimed significantly more. In Indonesia, raising audit odds from about 4% to 100% cut missing road funds by about 8 percentage points. Nepotism appears to have risen, and community monitoring had negligible overall effect. The review's model is a "sandwich": a responsive centre plus civic action from below.

Funding rules shape capture. Member dues cover "less than 20%" of WHO's budget [who/2026_how-who-is-funded]; in 2022–23 only 13% was fully predictable [who/2024_sustainable-financing]. WHO says predictable funding helps it "maintain independence from special interests". In 2022 members agreed to raise dues to 50% of the base budget by 2030–31. The United States, paying 22% of dues, left on 22 January 2026 [who/2025_eb156-inf6-us-withdrawal] [hhs/2026_us-withdrawal-who]. The 2026–27 budget fell from $5.3 billion to $4.2 billion, with a gap of about $1.7 billion in May 2025 [enca/2025_who-cuts-budget].

FIFA is the extreme case. Each of its 211 member associations has one vote [fifa/2024_statutes] [fifa/2024_2030-2034-hosts]. In 2015 US prosecutors charged 14 defendants over a 24-year scheme with "well over $150 million in bribes and kickbacks" [us-doj/2015_fifa-indictment]. Alleged schemes reached the 2010 World Cup host vote and the 2011 presidential election. After the 2016 reforms, the 2030 and 2034 hosts were confirmed together, by acclamation, in December 2024. Saudi Arabia was the sole 2034 bidder; Norway abstained over a "flawed" process [express-and-star/2024_fa-backs-saudi-bid].

| Tool against capture | Evidence | Known side effect |
| --- | --- | --- |
| Rotating officials | Lab bribery games in China and Germany: rotation made officials less likely to repay bribes [buhren/2019_staff-rotation-experiment] | Term limits undo what professional legislatures built [kousser/2004_term-limits-professionalism] |
| Drawing by lot | No study found testing whether allotted bodies resist capture better | Whoever runs the body can steer it (section 4) |
| Publishing money flows | Uganda's newspaper campaign raised what schools received | Needs a free press and readers |
| Assessed funding | WHO's reform aims at 50% dues by 2030–31 | One large payer can still leave |
| Frequent random audits | Indonesia: about 8 points less leakage | Nepotism rose |

**Design implication:** Capture follows discretion, money and agenda control. Assessed funding, published flows, frequent random audits and rotation each help, and each needs a check on its known side effect.

## 4. Modern designs, new attack surfaces

Kara wants something more modern than elections and representative assemblies. Modern tools move power to whoever writes the code, trains the model, recruits the panel or runs the platform. Their design belongs to another strand; these are the threats.

**Algorithmic error at scale.** Australia's Robodebt raised welfare debts by income averaging; by December 2014 internal advice had found the proposal unlawful [robodebt-rc/2023_report]. Tribunal rulings against averaging went unpublished, which made them easier to ignore. The Royal Commission called it "a crude and cruel mechanism, neither fair nor legal". In the Netherlands, a system that automatically flagged childcare-benefit claims as risky used nationality as an indicator; the data protection authority fined the tax authority €2.75 million [dutch-dpa/2021_tax-administration-fine]. Costs and remedies are in [executive and administration](executive-and-administration.md).

**Fake participation.** In the 2017 US net neutrality rulemaking, nearly 18 million of more than 22 million public comments were fake [ny-ag/2021_fake-comments-report]. Broadband companies funded 8.5 million that impersonated real people. Another 9.3 million used invented identities, mostly from one student's automated software.

**AI-mediated deliberation.** An AI mediator drafted group statements that 5,734 participants preferred to human mediators' [tessler/2024_ai-common-ground]. Discussants often converged on a shared view: a strength, and a lever for whoever tunes the mediator. Across 76,977 participants and 19 models, post-training and prompting raised persuasiveness by up to 51% and 27% [hackenburg/2025_levers-of-persuasion]. Where they did, they "systematically decreased factual accuracy". Personalised GPT-4 out-argued humans 64.4% of the time where the two differed (N = 900) [salvi/2025_persuasiveness-gpt4]. A September 2026 correction says personalisation's edge over plain GPT-4 was not significant (P = 0.07) [salvi/2026_author-correction].

**Staff capture of allotted bodies.** Whoever recruits, briefs and facilitates an assembly holds agenda power. Moderators shifted participants' views even when voicing opinions only "in a constrained manner" [spada-vreeland/2013_who-moderates-the-moderators]. The authors warn this lets interest groups "hijack" deliberation. The first round found French facilitators wrote debate summaries, and an Irish recruiter broke the sampling method ([deliberation](deliberation.md)); see also [sortition at scale](sortition-at-scale.md).

**Single points of failure.** One faulty CrowdStrike update crashed 8.5 million Windows devices, under 1% of the total, yet hit critical services widely [microsoft/2024_crowdstrike-outage]. The first round found one chip flaw exposed 750,000 Estonian ID cards ([digital voting](digital-voting.md)). Estonia hedges with a "data embassy" in Luxembourg that holds backups and can run critical services [e-estonia/2026_data-embassy]. It rests on another state's territory and immunity; after stage three there is no abroad.

**Design implication:** Treat every model, algorithm, platform and secretariat as an office: plural, published, audited, contestable and replaceable. No single vendor, model or recruiter should sit on the path of every planetary decision.

## 5. One world, no exit

Kant warned that "the wider the sphere of their jurisdiction, the more laws lose in force" [kant/1795_perpetual-peace]. Caplan put at 5% the chance that a world totalitarian government emerges within 1,000 years and lasts 1,000 more [80000-hours/2024_stable-totalitarianism]. His figure falls to 0.1% if the number of countries holds, and rises to 25% with one. That 250-fold gap is one economist's judgement, not a measured risk. Somin adds that free societies can fall to totalitarians "during a crisis", and without exit "there will be nowhere else to go" [somin/2008_perils-of-world-government].

The alternative to one centre is not anarchy. Deudney's publisher summarises his claim: security means avoiding "the extremes of anarchy and hierarchy" [deudney/2007_bounding-power]. In the nuclear era, that requires "mutually restraining world government". Bednar finds robust federations rely on "diverse but complementary safeguards" that "fail under different circumstances" [bednar/2008_robust-federation]. Ostrom's polycentric systems have "many centers of decision making that are formally independent of each other" [ostrom/2009_beyond-markets-and-states]. Switzerland's seven-member Federal Council has a president for one year, "first among equals" [swiss-federal-council/2026_the-federal-council]. Exit designs for after stage three are in [living charter](living-charter.md), options B–E.

**Design implication:** Treat "no exit after stage three" as the top-level risk. Internal rival centres must then do the work of rival states, so some community can always refuse unlawful orders, shelter dissenters or leave.

## 6. Systemic resilience: lessons from safety engineering

Perrow argues that piling on warnings and safeguards fails, because complexity makes failures inevitable [perrow/1999_normal-accidents]. Precautions "may help create new categories of accidents". His two dimensions of risk are complex interactions and tight coupling. Landau argued duplication can be rational: an airliner is "a very redundant system", which explains its reliability [landau/1969_redundancy]. Sagan's title states the counter-case: more nuclear security forces "may produce less nuclear security" [sagan/2004_redundancy-problem].

High-reliability organizations, such as aircraft carriers and emergency rooms, are the model [weick-sutcliffe/2015_managing-the-unexpected]. Their five habits are preoccupation with failure, reluctance to simplify, sensitivity to operations, deference to frontline expertise and commitment to resilience [ahrq/2019_high-reliability]. This pass found no controlled evidence that these habits transfer to governments. Red teams institutionalise doubt: "the independent application of a range of structured, creative and critical thinking techniques" [uk-mod/2021_red-teaming-handbook].

Inspectors general show how fragile independent inspection is. The President may remove one, but must give Congress written reasons "not later than 30 days before the removal" [us/1978_inspector-general-act]. On 24 January 2025, 17 inspectors general were fired by identical two-sentence emails citing "changing priorities" [ap/2025_inspectors-general-not-reinstated]. In September 2025 a judge found the firings likely unlawful but refused reinstatement; the President could simply re-fire them after notice. On 11 October 2026, 27 inspector-general posts were vacant [cigie/2026_ig-vacancies]. IGnet counts 73 statutory inspectors general [cigie/2026_ignet], so about 37% are empty (estimate: 27 ÷ 73). Eight posts have been empty about 622 days, which dates them to late January 2025; four of those have nominees.

**Design implication:** Build for failure, with loosely coupled levels, more than one inspector and automatic acting successors. Protect tenure by for-cause removal, since notice-only protection did not keep inspectors in office.

## 7. Threat model: summary table

| Threat | Precedent | Safeguard | Charter clause | Residual risk |
| --- | --- | --- | --- | --- |
| Emergency becomes rule by decree | Weimar, 1930–33; Hungary, 2020–26 | 21-day limit, rising supermajorities, court review | None | Crises manufactured or prolonged |
| Routing around emergency limits | South Africa's 750-day disaster state | Define emergency power by effect | None | Ordinary law entrenches measures |
| Executive overstays | A third of presidents tried; FIFA | Collegial executive; plain term count; removal | VIII.7 | A planetary mandate is a strong platform |
| Umpire captured or packed | Poland's tribunal; Hungary, 2013 | Fixed size and powers; staggered terms | IX.1–2, XI.2 | The Court is also the main amender |
| Appointment chokepoint | Polish presidents refused oaths | Automatic seating and succession, as in X.3 | IX.2, VIII.9 | Who certifies "qualified" |
| Watchdogs fired or downgraded | US inspectors general; Hungary's ombudsman | For-cause removal; budget share; acting successor | VIII.9, IX.3, IX.10 | Ombudsman selection unstated |
| Donor and industry capture | Stigler; WHO; FIFA | Assessed funding; disclosure; audits; rotation | V.2, VII.6, X.7 | Capacity costs; displacement |
| Elite capture of participation | Uganda: 13% of grants arrived | Central monitoring; published flows; free press | VII.4, VIII.1–2 | The monitoring centre is a target |
| Electoral channel manipulated | Hungary's "electoral autocracy" | Independent election bodies; observers | VIII.4–7 | No outside observers after stage three |
| Algorithmic error at scale | Robodebt; Dutch nationality flag | Lawfulness review; human decision on request | VII.2, VII.5 | Code becomes law in practice |
| Fake or automated participation | 18 million fake FCC comments | Verified identity; anomaly audits | VIII.1–2 | Stolen or sold credentials |
| Steered AI mediation | Persuasion gains cut accuracy | Open models; several mediators; red teams | VIII.2–3 | Subtle steering is hard to detect |
| Staff capture of allotted bodies | Moderator effects; Irish recruiting breach | Split recruiting, briefing and facilitation | VIII.3, IX.2, X.3 | Staff know more than members |
| Digital single point of failure | CrowdStrike; ROCA | Diverse vendors; paper fallback | VII.2, VII.5, VIII.6 | No outside host for backups |
| Safeguards turned into stalls | My analysis: forced re-votes, delays | Targeted recounts; emergency carve-outs | VIII.6, X.4 | Untested |
| Lock-in with no exit | Caplan: 0.1% against 25% | Rival centres; tripwire exit | XII.4–5, XI | Exit against the ceiling |

**Safeguards an efficient design must keep while it streamlines:**

1. **Rival centres** with their own legitimacy, money and courts, so capturing one does not capture all.
2. **Self-expiring emergency powers**, renewed by someone else at rising thresholds, unable to amend the Charter or postpone votes.
3. **A collegial, removable executive** with a term limit that cannot be reread.
4. **An umpire with no single chokepoint**: fixed size and powers, automatic seating, staggered terms.
5. **Independent inspectors** with for-cause tenure, assessed funding and automatic acting successors.
6. **Repair channels no emergency can suspend**: scheduled votes, court access and outside review.
7. **Plural, open, auditable digital and AI infrastructure**, with a non-digital fallback.
8. **A lawful way out**, or a tripwire that restores one when the centre fails.

Planetary votes, assemblies and administration can all shrink. These eight are the load-bearing walls.

## Design patterns that work

- **Time-boxed emergencies with rising supermajorities** (South Africa). Work when emergencies are defined by effect; fail when governments switch to a softer statute.
- **A legislative continuity body** (Germany). Cannot amend the constitution, and its laws lapse; extended electoral terms are its weak point.
- **Public derogation with outside review** (ECHR Article 15). Formal notice seems to restrain abuse; deference lets emergencies run for years.
- **Assessed funding, random audits and published flows** (WHO's reform; Indonesia; Uganda). Need a free press; one large payer can still leave, and corruption can shift into hiring.
- **Complementary safeguards** (Bednar). Work when they fail under different conditions; fail when one party controls them all, as in Hungary.

## Tensions and open problems

- **Speed against safety.** X.4's one-year delay and XI.3's two votes slow everything; emergency carve-outs must not become a standing bypass.
- **Subsidiarity needs a watched centre.** Local participation is captured without central monitoring, yet the monitoring centre is the biggest prize.
- **Rotation against competence.** One-term rules resist capture but shift knowledge to permanent staff, who can capture in turn.
- **Repair against rules.** Undoing capture by the book has taken Poland years; shortcuts look like counter-capture. Hungary's repair needed the same two-thirds majority as its capture.
- **Attractive tools, thin evidence.** AI mediation is popular yet steerable. Sortition's capture resistance and the transfer of high-reliability habits to government are untested.
- **Self-inflicted denial of service.** Under VIII.6, an attacker who can make audits fail can force repeated planetary re-votes. This is my analysis, not a documented case.

## Options for the next draft

These are options, not decisions.

- **Add an emergency clause to Part VIII.** Stewards acting together may declare a listed planetary hazard for up to 21 days, published at once. A body drawn by lot in advance confirms or ends it within 7 days. Extensions run three months at most: the first by majority, later ones by 60%. Any court may review it, and measures lapse with it.
- **Fix the emergency perimeter.** Any measure that suspends a right or bypasses ordinary procedure counts, whatever statute it uses. No emergency may amend the Charter, postpone a scheduled vote or stop the Court or Ombudsman.
- **Exempt short emergencies from X.4.** Measures that lapse with the emergency skip the long-view delay; anything meant to last goes through X.4.
- **Recast VIII.7.** Five to nine Stewards with a rotating chair; "one term" counts any part of a term; removal by supermajority of an allotted body after a Court finding.
- **Harden IX.2.** Write the Court's size and jurisdiction into the Charter, seat selected judges automatically, and stagger terms.
- **Protect the watchdogs (VIII.9, IX.3, IX.10).** A council of ombudsmen, for-cause removal after independent review, a fixed budget share as in X.7, and an automatic acting successor.
- **Add a funding rule to VII.6.** Planetary bodies run on assessed shares; earmarked gifts are capped, and all transfers are published monthly.
- **List planetary powers in VII.4.** The smaller the planetary scope, the smaller the prize.
- **Govern algorithms and AI as offices (VII.2, VII.5, VIII.2–3).** Publish code, models and prompts; review lawfulness before use; give a human decision on request; run at least two independent mediators.
- **Separate the people around assemblies (VIII.3).** Recruiting, briefing and facilitating in different hands, rotated and audited; members may replace facilitators.
- **Add a red-team office.** It publishes an adversarial review of each major planetary proposal before the vote; institutions follow or explain, as in X.5.
- **Add a continuity rule.** If planetary bodies cannot function, a pre-drawn panel acts for at most 90 days, unable to amend the Charter, postpone votes or extend itself.
- **Add a tripwire exit to XII.5.** Communities regain a right to leave if a scheduled vote is postponed, an emergency passes its cap, or the Court cannot sit. Combine with [living charter](living-charter.md) options B–E.
- **Limit forced re-votes in VIII.6.** A failed audit triggers a targeted recount where it failed, not a planetary re-vote.

## Sources

| Source id | Title | Tier | Checked |
| --- | --- | --- | --- |
| luhrmann-rooney/2021_autocratization-by-decree | Autocratization by Decree: States of Emergency and Democratic Decline | primary | partial |
| bjornskov-voigt/2021_emergencies-misuse | Emergencies: on the misuse of government powers | primary | verified |
| bjornskov-voigt/2025_covid-unlawful-emergencies | Covid and the constitution: unlawful states of emergency during the pandemic | primary | partial |
| edgell/2021_pandemic-backsliding | Pandemic backsliding: Violations of democratic standards during Covid-19 | primary | verified |
| v-dem/2022_pandem-v6-1 | Pandemic Backsliding (PanDem) dataset and codebook, v6.1 | primary | verified |
| ginsburg-versteeg/2021_bound-executive | The bound executive: Emergency powers during the pandemic | primary | partial |
| comstock-heiss-chaudhry/2024_derogations-backsliding | Derogations, Democratic Backsliding, and International Human Rights During the COVID-19 Pandemic | primary | partial |
| germany/1919_weimar-constitution | Die Verfassung des Deutschen Reichs (Weimar Constitution), Arts. 25 and 48 | primary | verified |
| ghdi/1930_bruening-caricature | Karikatur Heinrich Brünings (11. Juli 1930), with editors' note | secondary | verified |
| germany/1933_reichstag-fire-decree | Verordnung des Reichspräsidenten zum Schutz von Volk und Staat (28 February 1933) | primary | verified |
| echr/2026_guide-article-15 | Guide on Article 15 of the European Convention on Human Rights | primary | verified |
| south-africa/1996_constitution | South Africa's Constitution of 1996 with Amendments through 2012 | primary | verified |
| south-africa/2002_disaster-management-act | Disaster Management Act 57 of 2002 | primary | verified |
| creamer-media/2022_state-of-disaster-ends | Govt ends National State of Disaster | secondary | verified |
| european-pravda/2026_magyar-ends-emergency | Hungary's Magyar scraps state of emergency introduced by Orbán over threat of war | secondary | verified |
| xpatloop/2026_decrees-elevated-to-law | State of Emergency in Hungary Continues: New Parliament Elevates Decrees to Law | secondary | verified |
| kouroutakis-ranchordas/2016_snoozing-democracy | Snoozing Democracy: Sunset Clauses, De-Juridification, and Emergencies | secondary | verified |
| crs/2021_fisa-provisions-expired | Origins and Impact of the FISA Provisions That Expired on March 15, 2020 | primary | verified |
| venice-commission/2020_states-of-emergency | Respect for Democracy, Human Rights and the Rule of Law during States of Emergency: Reflections | primary | verified |
| germany/1949_grundgesetz | Basic Law for the Federal Republic of Germany (English translation) | primary | verified |
| bermeo/2016_on-democratic-backsliding | On Democratic Backsliding | primary | partial |
| bermeo/2016_coded-coups-supplement | Supplemental material: Types of Coups in Democracies, 1958–2014 | primary | verified |
| levitsky-ziblatt/2018_how-democracies-die | How Democracies Die | secondary | partial |
| versteeg/2020_term-limit-evasion | The Law and Politics of Presidential Term Limit Evasion | primary | verified |
| fifa/2024_statutes | FIFA Statutes, May 2024 edition | primary | verified |
| maduro-donati/2026_infantino-fourth-term | FIFA: Infantino's fourth term puts the organisation's governance to the test | secondary | verified |
| ipu/2010_hungary-election | IPU PARLINE: Hungary, elections held in 2010 | tertiary | verified |
| venice-commission/2013_hungary-fourth-amendment | Opinion on the Fourth Amendment to the Fundamental Law of Hungary, CDL-AD(2013)012 | primary | verified |
| fdsd/2014_hungary-ombudsman | Hungarian Parliament's Deputy Commissioner for Fundamental Rights, the Ombudsman for Future Generations | secondary | verified |
| european-parliament/2022_hungary-electoral-autocracy | MEPs: Hungary can no longer be considered a full democracy | primary | verified |
| osw/2026_hungary-election | Elections in Hungary: the triumph of Péter Magyar | secondary | verified |
| bluewin/2026_tisza-two-thirds-final | Two-thirds majority for Tisza secured - Magyar accused of fraud | secondary | verified |
| venice-commission/2016_poland-constitutional-tribunal | Opinion on Amendments to the Act of 25 June 2015 on the Constitutional Tribunal of Poland, CDL-AD(2016)001 | primary | verified |
| cjeu/2021_poland-daily-penalty-order | CJEU Press Release 192/21, C-204/21 R Commission v Poland | primary | verified |
| notes-from-poland/2024_article-7-closed | EU closes Article 7 rule-of-law proceedings against Poland after seven years | secondary | verified |
| notes-from-poland/2026_krs-veto | President vetoes bill reforming judicial body at heart of Poland's rule-of-law crisis | secondary | verified |
| notes-from-poland/2026_tk-oath-ruling | Polish constitutional court endorses president's right not to swear in new judges | secondary | verified |
| notes-from-poland/2026_berek-elected | Prime minister's "right-hand man" elected as Polish constitutional court judge | secondary | verified |
| stigler/1971_theory-economic-regulation | The Theory of Economic Regulation | primary | unverified |
| carrigan-coglianese/2016_stigler-theory | George J. Stigler, "The Theory of Economic Regulation" (handbook chapter) | secondary | verified |
| mansuri-rao/2013_localizing-development | Localizing Development: Does Participation Work? | secondary | verified |
| who/2026_how-who-is-funded | How WHO is funded | primary | verified |
| who/2024_sustainable-financing | Working toward a sustainably-financed WHO | primary | verified |
| who/2025_eb156-inf6-us-withdrawal | Assessed contributions: draft calculations for the year 2026 (EB156/INF./6) | primary | verified |
| hhs/2026_us-withdrawal-who | HHS Fact Sheet: U.S. Withdrawal from the World Health Organization | primary | verified |
| enca/2025_who-cuts-budget | WHO restructures, cuts budget after US withdrawal | secondary | verified |
| us-doj/2015_fifa-indictment | Nine FIFA Officials and Five Corporate Executives Indicted for Racketeering Conspiracy and Corruption | primary | verified |
| fifa/2024_2030-2034-hosts | Extraordinary FIFA Congress appoints hosts of 2030 and 2034 editions of FIFA World Cup | primary | verified |
| express-and-star/2024_fa-backs-saudi-bid | FA to back Saudi Arabia's bid to host 2034 World Cup | secondary | verified |
| buhren/2019_staff-rotation-experiment | Staff Rotation as an Anti-Corruption Policy in China and in Germany: An Experimental Comparison | primary | partial |
| kousser/2004_term-limits-professionalism | Term Limits and the Dismantling of State Legislative Professionalism | secondary | partial |
| robodebt-rc/2023_report | Report of the Royal Commission into the Robodebt Scheme | primary | verified |
| dutch-dpa/2021_tax-administration-fine | Tax Administration fined for discriminatory and unlawful data processing | primary | verified |
| ny-ag/2021_fake-comments-report | Attorney General James Issues Report Detailing Millions of Fake Comments | primary | verified |
| tessler/2024_ai-common-ground | AI can help humans find common ground in democratic deliberation | primary | partial |
| hackenburg/2025_levers-of-persuasion | The levers of political persuasion with conversational artificial intelligence | primary | verified |
| salvi/2025_persuasiveness-gpt4 | On the conversational persuasiveness of GPT-4 | primary | partial |
| salvi/2026_author-correction | Author Correction: On the conversational persuasiveness of GPT-4 | primary | partial |
| spada-vreeland/2013_who-moderates-the-moderators | Who Moderates the Moderators? The Effect of Non-neutral Moderators in Deliberative Decision Making | primary | partial |
| microsoft/2024_crowdstrike-outage | Helping our customers through the CrowdStrike outage | primary | verified |
| e-estonia/2026_data-embassy | Data embassy | primary | verified |
| kant/1795_perpetual-peace | Perpetual Peace: A Philosophical Essay | primary | verified |
| 80000-hours/2024_stable-totalitarianism | Stable totalitarianism | secondary | verified |
| somin/2008_perils-of-world-government | Perils of World Government | primary | verified |
| deudney/2007_bounding-power | Bounding Power: Republican Security Theory from the Polis to the Global Village | secondary | partial |
| bednar/2008_robust-federation | The Robust Federation: Principles of Design | secondary | partial |
| ostrom/2009_beyond-markets-and-states | Beyond Markets and States: Polycentric Governance of Complex Economic Systems (Prize Lecture) | primary | verified |
| swiss-federal-council/2026_the-federal-council | The Federal Council | primary | verified |
| perrow/1999_normal-accidents | Normal Accidents: Living with High Risk Technologies (updated edition) | secondary | partial |
| landau/1969_redundancy | Redundancy, Rationality, and the Problem of Duplication and Overlap | secondary | partial |
| sagan/2004_redundancy-problem | The Problem of Redundancy Problem: Why More Nuclear Security Forces May Produce Less Nuclear Security | secondary | partial |
| weick-sutcliffe/2015_managing-the-unexpected | Managing the Unexpected: Sustained Performance in a Complex World (3rd edition) | secondary | partial |
| ahrq/2019_high-reliability | High Reliability (PSNet primer) | tertiary | verified |
| uk-mod/2021_red-teaming-handbook | Red Teaming Handbook (3rd edition) | primary | verified |
| us/1978_inspector-general-act | Inspector General Act of 1978, as codified at 5 U.S.C. § 403 | primary | verified |
| ap/2025_inspectors-general-not-reinstated | Federal judge refuses to reinstate eight former inspectors general fired by Trump administration | secondary | verified |
| cigie/2026_ig-vacancies | Inspector General Vacancies (Oversight.gov) | primary | verified |
| cigie/2026_ignet | IGnet: home page | primary | verified |
