# Changelog

The Charter's draft history, newest first. Each entry says what changed and why. The git history holds the exact wording of every version.

## Third working draft — 12 October 2026

The Charter becomes a small book. One long document had mixed three kinds of text that should change at different speeds: principles meant to last, the machinery of government, and numbers that need tuning. Kara chose three binding layers, each easier to change than the one above it, and a commentary:

- **The Foundations**, in [CHARTER.md](CHARTER.md): the Preamble and Parts I–V.
- **[The Articles of Terra](articles/README.md)**: nine short Articles on how the Commonwealth works.
- **[The Schedules](schedules/README.md)**: every number and list the Articles use, each with its reason and a range.
- **[The Commentary](commentary/README.md)**: why each part says what it says. It binds no one.

"This Charter" still means the whole binding text, so almost every clause carries over word for word. A script compared every sentence of the second draft with the third: each one either appears word for word or carries a change listed below.

**Where everything went**

| Second draft | Third draft |
| --- | --- |
| Preamble, Parts I–III | The Foundations: Preamble, Parts I–III |
| Part VI | Part IV |
| XI.1, XI.2 | V.1, V.2 |
| XI.3, XI.4, XI.5 | V.4, V.7, V.8 |
| Part IV (1–9), Part V (1–5) | Article 1: 1.1–1.9, then "Business", 1.10–1.14 |
| Part VII (1–7) | Article 2: 2.1–2.7 |
| VIII.8, VIII.10, VIII.13 | 2.8, 2.9, 2.10 |
| VIII's opening and diagram | Article 3's opening and diagram |
| VIII.1–4, VIII.11, VIII.12, VIII.22, VIII.24 | 3.1–3.4, 3.5, 3.6, 3.7, 3.8 |
| VIII.5, VIII.6, VIII.16, VIII.17, VIII.18 | Article 4: 4.1–4.5 |
| VIII.7, VIII.14, VIII.15 | Article 5: 5.1–5.3 |
| VIII.19, VIII.20, VIII.21, VIII.23 | Article 6: 6.1–6.4 |
| Part IX (1–10), VIII.9 | Article 7: 7.1–7.10, 7.11 |
| Part X (1–7) | Article 8: 8.1–8.7 |
| Part XII (1–10) | Article 9: 9.1–9.10 |
| Schedule — World regions | Schedule 3 |

The research notes, thoughts, proposals, open questions and source records all cite the second draft's numbering; this table translates.

**Kara's decisions**

- **Part II** gains a credit line: "The Seven Principles adapt The Satanic Temple's Seven Fundamental Tenets."
- **Part IV** (was VI) gains one: "A utopia of utopias draws on Robert Nozick's framework for utopia, joined here to a floor and a ceiling."
- **The numbers** stay at the second draft's defaults for now, moved into the Schedules.

**The layers (Part V)**

- **V.3 (new), The layers.** The Foundations prevail over the Articles, the Articles over the Schedules, and all three over every planetary act. The Commentary binds no one.
- **V.4 (was XI.3)**, retitled "How the Foundations change". The rule of two-thirds in two votes of all terrans now applies to "an amendment to these Foundations", and the Court checks it against V.7.
- **V.5 (new), How the Articles change.** Two votes of all terrans, at least a year apart, each needing a majority of the votes overall and in a majority of the regions where terrans have joined. That pairs Nevada's two votes with the double majority Switzerland asks of people and cantons. An assembly drafts each change, the Court checks it against the Foundations, and it carries the Guardians' statement.
- **V.6 (new), How the Schedules change.**
    - A planetary act that is not urgent may change a setting within its range, and add or remove hazards. Without that exception, an urgent act could add a hazard and an emergency could follow the same day.
    - The Earth Science Panel's ranges are recorded as it publishes them, and ceiling acts set limits within them. No urgent act may loosen a ceiling limit.
    - The world regions change only as the Foundations do, as in the second draft, since they decide whose majorities count. Everything else in the Schedules changes only as the Articles do.
    - Where an Article shows a number a Schedule sets, it means the Schedule's current value, so tuning a setting never counts as changing an Article.
    - No change to the Articles or Schedules may do what V.7 forbids.
- **V.7 and V.8** are the old XI.4 and XI.5, unchanged.

**What the layers cost.** Every clause now in the Articles, and every number now in Schedule 1, used to need two-thirds in two votes of all terrans a year apart. It now needs a majority in two votes a year apart, overall and in most regions. That covers the emergency limits, the vote of all terrans, the Court, the Ombudsman council, the stages and the right to leave. The year between votes still guards against a change made in one crisis. Whether any of these checks belongs in the Foundations instead is Kara's call.

**Numbers moved to the Schedules**

Every number in the Articles now links to its entry in Schedule 1 (Safeguards) or Schedule 2 (Settings). Safeguards are the numbers a passing majority could use to switch off a check on itself, so they change only as the Articles do. Settings may be tuned by planetary act inside a range. The text shows the current value, and `make check` fails if a linked number ever disagrees with its Schedule. The Foundations keep their own few numbers in their text.

**Other wording changes**

- **2.3 (was VII.3).** "and this Charter changes only by such votes, as Part VIII sets out" becomes "as Article 3 sets out. Only such votes change the Foundations and the Articles (Part V)." Settings and ceiling limits change by panel decisions, so the old sentence would no longer be true of the whole Charter.
- **3.3 (was VIII.3).** "A sixth replaced every six months" becomes "with equal shares replaced every six months", so the sentence stays true if the term is tuned.
- **3.5 (was VIII.11).** The voting age points to Schedule 2.
- **3.6 (was VIII.12).** Adds "and Schedule 4 records both".
- **6.1 (was VIII.19).** The hazard list is Schedule 5.
- **9.9 (was XII.9).** "Part VIII counts only terrans who have joined" becomes "votes, signatures, and draws, the shares of terrans they are measured against, and the Council of Communities' seats by population count only terrans who have joined". It covers what old Part VIII counted, now spread over several Articles.
- **Openings.** Articles 4, 5 and 6 have new one-sentence openings. The others keep their Part's opening.
- **Credits.** Part VIII's credit line is split among Articles 3 to 7, each taking the sentences about its own clauses. "Versioned decisions on open-source projects" becomes its own sentence in Article 3.
- **The diagram** in Article 3 uses the new clause numbers.
- **Cross-references** are renumbered throughout.
- **The front of CHARTER.md** gains a short list of the four layers, and the closing links add the Commentary.

**Numbers filled in**

The second draft left these unset. Each now has a value from the research or the government design, and a reason in its Schedule:

- **4.5.** Members of the independent offices serve fixed terms of eight years, as the European Central Bank's board does.
- **5.3.** A draft rule's objection window is 60 days.
- **6.1.** The panel that confirms an emergency, and each fresh panel that extends one, has 1,000 terrans. They are drawn from a yearly pool of 20,000. The government design suggested 10,000, but ten fresh panels in a year would exhaust that.
- **7.11.** Ombudsmen serve fixed terms of seven years.

Seven numbers stay unset and are marked "not yet set": the protected budget shares and the number of Guardians in Schedule 1; the voting age, the size of a larger organization, the years over which pay is averaged, the cap on spending on a vote, and the thresholds for transparency in Schedule 2. Where the research supports one, each already has a range.

**The Schedules**

- **Schedule 1, Safeguards:** 52 numbers that hold power in check, two not yet set. They change only as the Articles do.
- **Schedule 2, Settings:** 22 numbers a planetary act may tune within a range, five not yet set. A change to the voting age waits for the next voting day, and a change to a body's size or term starts with its next draw.
- **Schedule 3, World Regions:** the second draft's schedule, adding that each terran counts in the region where they live, and a list of where regions count.
- **Schedule 4, The Boundaries (new):** where the Earth Science Panel's ranges and the ceiling's limits will be recorded. None is set yet.
- **Schedule 5, Hazards (new):** three hazards for which an emergency may be declared, all within the planetary powers: pandemics, weapons of mass destruction, and a crisis in the Commonwealth's own money. Peaceful protest, dissent, votes, draws and slow breaches of the ceiling are never hazards, and that part changes only as the Articles do.

**Open questions**

- "The numbers" now points to the Schedules, and a new question asks for the numbers not yet set.
- New questions ask whether two votes with double majorities are the right bar for the Articles, and whether the hazard list is right.
- "Regions" also asks how shares of regions round, since a quarter of ten is two and a half.
- In [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md), the credits for Parts II and VI are ticked, and several "in part" notes are added. New questions there cover:
    - the clash between urgent acts and the long-view test's year-long wait
    - one review panel per draft rule, or a sample of rules
    - single terms for ombudsmen and the independent offices
    - how often the Earth Science Panel reports
    - whether 25 years between reviews is too long

**Defaults to confirm**

- **The bar for the Articles:** two votes of all terrans a year apart, each with a majority overall and in a majority of the regions.
- **Which numbers are safeguards** and which are settings, and each setting's range.
- **The numbers filled in above**, and Schedule 2's rules on when a setting takes effect.
- **The hazard list** in Schedule 5, and what is never a hazard.

**Tools and housekeeping**

- `tools/build_schedules.py` generates Schedules 1 and 2 from `schedules/numbers.yaml`. It checks that every linked number in the Articles names an entry and shows its value, and that every setting sits inside its range.
- `tools/check_links.py` checks that every link between the repository's files resolves.
- `make schedules` runs the first; `make check` now runs the source check, the Schedules check and the link check.
- `tools/build_sources.py` also scans the Commentary and the Schedules for citations, and SOURCES.md notes that its Parts are the second draft's.
- The READMEs of research/, thoughts/, proposals/ and sources/, and the headers of two thoughts files, point to the mapping table above.

## Second working draft — 12 October 2026

The second draft replaces the rule that every terran votes on every planetary question, which the research showed can't work at planetary scale. Its government follows [proposals/modern-terran-government.md](proposals/modern-terran-government.md), with that proposal's defaults and the further choices listed below. It also makes the plain fixes the research found, and the fixes a final review of the draft asked for. Parts II and VI, and every clause not listed here, are unchanged.

**Preamble and Part I**

- **Preamble.** "Toward collapse" becomes "past their safe limits, risking changes that cannot be undone".
- **I.2.** Nations grew with print and literacy, and today's networks can reach every terran.

**Part III**

- **Names.** The nine boundaries use their official names, with plain glosses.
- **The science.** "Moves only as that science does" becomes "never leaves the range it sets". An Earth Science Panel publishes a range every four years, and the ceiling is set within it (VIII.12).
- **Fair shares (new).** A sharing principle, adopted as a Charter amendment, divides the ceiling into fair shares with timelines. Where a limit is already crossed, everyone moves toward their share on that timeline.
- **Credit.** Setting the ceiling draws on the Montreal Protocol.

**Parts IV and V**

- **IV.5.** Rates are set "by planetary act (Part VIII)", not "by vote".
- **Credit.** The wealth limit "adapts" Robeyns' limitarianism.
- **V.3.** "Full-time-equivalent" pay; the lowest pay counts contractors and agency, franchise, and outsourced workers.
- **V.4.** Start-up money is "one of the barriers" that keep cooperatives rare.

**Part VII**

- **VII.2.** Every service and vote has a non-digital route.
- **VII.3**, retitled "Decided by samples, checked by all". Panels drawn by lot decide. Any act except a ceiling act can be sent to a vote of all terrans, and the Charter changes only by such votes.
- **VII.4.** A list of planetary powers, including the Commons Fund. Everything else belongs to communities. The Court rules within 90 days when a quarter of the Council of Communities object.
- **VII.5**, retitled "Open logs". The logs are run by several independent bodies, with blockchain only where no single operator can be trusted.
- **VII.7.** A yearly doughnut account; worsening indicators trigger a Guardian review.
- **Credits.** The Swiss and Nigerian constitutions; Certificate Transparency.

**Part VIII, rebuilt**

The opening, the diagram rebuilt at the first import, and its caption are all replaced. Clauses 1–10 keep their numbers; 11–24 are new.

- **VIII.1.** Three thresholds:
    - 100,000 signatures earn a reasoned answer from the Agenda Council.
    - One million across a quarter of the regions send a proposal to an assembly.
    - 1% sends a proposal the assembly rejected to a vote of all terrans. This route is closed to the ceiling.

    Signatures must be gathered within twelve months. The Stewards, Guardians and member communities may also propose.
- **VIII.2.** Assemblies take the maps as input.
- **VIII.3.** Standing assemblies of 450 for each listed power, a Budget Assembly, and an Agenda Council of 300, all drawn by lot, on three-year terms. Different people recruit, brief and facilitate. The old assembly "for each proposal", which wrote the ballot question, is replaced; VIII.11 now gives the question and summary to the assembly concerned.
- **VIII.4.** Deciding panels of at least 1,000 vote in secret on each act exactly as drafted, after a Court check and after hearing advocates chosen by the assembly's majority and minority. "Except where this Charter requires more" is kept. A rejected act returns once, then waits two years.
- **VIII.5.** An in-person vote is final, whatever the order, and online voting closes first.
- **VIII.6.** Where an audit fails, the paper record is counted by hand, and a new vote follows only if the missing votes could change the result. Five independent bodies hold the voting keys, and any three can act.
- **VIII.7.** Seven Stewards, at most two per region, each on one six-year term:
    - chosen from a certified pool, with the approval of two councils
    - removable by two-thirds of either council
    - a six-month fallback to lot if a seat goes unfilled
    - leading a civil service hired on merit
- **VIII.8.** The separation of powers adds the Council of Communities' second key and rules made only under an act. The Ombudsman council oversees them all.
- **VIII.9.** An Ombudsman council of five, with a red team. Fixed terms, removal only for misconduct, automatic successors, and a protected budget.
- **New VIII.11–24:**
    - a vote of all terrans
    - the ceiling
    - the Council of Communities
    - the Oversight Council
    - rules under an act
    - drawn fairly
    - certified candidates
    - independent offices
    - emergencies expire
    - limits on emergencies
    - continuity
    - decisions are versions
    - urgent acts
    - rules anyone can run
- **Credits.** Ostbelgien, Mongolia, Switzerland (its optional referendum, Federal Council and urgent laws), the IETF, South Africa, open-source projects, and Sweden's Ombudsman. The Earth Constitution is now credited for the Ombudsman council of five rather than for the Stewards.

**Part IX**

- **IX.1.** Appeals to the Planetary Court go "on questions under this Charter", and the Court settles disputes between communities.
- **IX.2.** Fifteen judges, chosen by an assembly drawn by lot for that purpose, from certified candidates. Each serves one twelve-year term, staggered, and is seated automatically. Removal takes two-thirds of the other judges, after an independent review.
- **IX.3.** The inspectors' budget is a fixed share of planetary revenue.
- **IX.10.** "Ombudsman council"; "open logs".
- **Credits.** The Earth Constitution, "though here only a court may order an arrest"; Norway's rehabilitative prisons.

**Part X**

- **Introduction.** "Tens of thousands of generations".
- **X.4.** "Every planetary act", not "every major decision". A Guardian finding of likely serious, irreversible harm means a year's wait and a fresh decision: by a panel, or by a new vote of all terrans if all terrans passed the act.
- **X.7.** "Ombudsman council".
- **Credits.** Guardians from Wales and New Zealand; speaking for nature from Ecuador's rights of nature; the burden of proof from Ecuador's Article 397 and the Wingspread Statement.

**Parts XI and XII**

- **XI.3.** "Two votes of all terrans" where it said "two planetary votes", since panels vote too. An assembly drafts each amendment, the Court checks it against XI.4, and it carries the Guardians' statement.
- **XI.4.** "The ceiling moves only as the science does" becomes "No amendment may set the ceiling outside the range the science supports".
- **New XII.7–10:** proven before binding; a way out if safeguards fail; who counts until stage three; funding until stage two.
- **New schedule** of world regions, not yet chosen.

**Open questions**

- "Paper votes" now asks whether every vote of all terrans should also be on paper.
- "Leaving after stage three" asks about leaving by choice, beyond XII.8.
- Three questions are new: sharing the ceiling, regions, and voting age and service.
- The research link now points to the research index and the government design.

**Defaults to confirm**

The draft makes choices the proposal left open or didn't cover:

- **Sizes and terms:**
    - assemblies of 450, an Agenda Council of 300, an Oversight Council of 150
    - a Council of Communities of 200, by population, at least two per region
    - panels of 1,000, or 3,000 for the ceiling
    - an Ombudsman council of five
    - fifteen judges on twelve-year terms, and seven Stewards on six-year terms
- **Thresholds:** 100,000; one million; 1%; 0.5%; twelve months to gather; a quarter of the regions; 100 days; 90 days.
- **Service by lot** is voluntary, paid and protected.
- **Regions** change only by amendment.
- **Footprint classes** are set per person, yearly, by the Statistics Office.
- **Independent offices and inspectors** have protected budgets.

Credits for Parts II and VI remain open; see [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Public domain dedication — 11 October 2026

The Charter is dedicated to the public domain under CC0 1.0, so anyone may copy, translate, adapt, adopt or enact it without permission or credit. That matches the Preamble: the Charter "belongs to no government". A dedication notice now closes CHARTER.md; the Charter's wording is unchanged. CC0 waives copyright, not trademark, so the names "Terran Charter", "Terran Humanism" and "Terran Commonwealth" fall outside the dedication. The rest of the repository followed the same day: the research, the reasoning, the source records and the tools are CC0 too. See [RIGHTS.md](RIGHTS.md).

## Working draft — 10 October 2026

The working draft, by Kara Zajac, written from the drafting session's research of 9 October 2026 ([research/drafting-session-2026-10-09.md](research/drafting-session-2026-10-09.md)). It has twelve Parts, the Seven Principles, and five open questions for the next draft. [thoughts/research-to-charter.md](thoughts/research-to-charter.md) traces which of the research's recommendations it adopted.

It was imported into this repository the same day. The import made three fixes for what the export dropped, and no wording changes:

- Part VIII's decision-flow drawing, rebuilt as a Mermaid flowchart from its caption and from Parts VIII and X
- the closing "Research" link, pointed at the research doc
- the byline's @-mention markup, made plain text
