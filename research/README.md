# Research

The evidence behind the Charter, Part by Part.

The notes cite the Charter by the twelve Parts of its first and second drafts. The third draft moved most of those clauses into the Articles of Terra, and the [changelog](../CHANGELOG.md#third-working-draft--12-october-2026) maps each Part to its new place.

## The drafting session's research

[drafting-session-2026-10-09.md](drafting-session-2026-10-09.md) is the research the working draft was written from, kept verbatim. It covers pay ratios, wealth taxes and hard caps, organizations' political rights, digital ID and online-voting security, global enforcement, and guardians for the future. [drafting-session-checks.md](drafting-session-checks.md) checks each of its links against the claim the link supports. [../thoughts/research-to-charter.md](../thoughts/research-to-charter.md) traces its recommendations into the Charter.

## Round one: the Charter, Part by Part

These are a first pass, made on 10 October 2026, one note per area of the Charter. Each note covers:

- the precedents its Parts credit or echo
- what the record says about them
- where the Charter matches or departs from them
- options for the next draft

Each note's sources are in the matching file in [sources/](../sources/README.md).

| Note | Charter | Covers |
| --- | --- | --- |
| [lineage.md](lineage.md) | Preamble, II, VI | Where the Preamble, the Seven Principles and the utopia of utopias come from: humanist manifestos, global charters and rights texts, Nozick's framework for utopia, and the movement's name |
| [floor-and-ceiling.md](floor-and-ceiling.md) | Preamble, III, VII.7 | Raworth's doughnut, the planetary boundaries and their current status, safe and just boundaries, measuring progress, and whether everyone can be inside at once |
| [wealth-and-tax.md](wealth-and-tax.md) | IV | Limitarianism, wealth taxes in practice, global coordination, paying in shares, beneficial ownership, the commons, and the numbers behind the $10M limit |
| [business.md](business.md) | V | Corporate personhood, money in politics, pay-ratio rules, worker ownership and cooperatives, and codetermination |
| [deliberation.md](deliberation.md) | VII, VIII | Citizens' assemblies, vTaiwan and Pol.is, initiatives, sortition at scale, direct democracy and minorities, subsidiarity, and the Stewards and the Ombudsman |
| [digital-voting.md](digital-voting.md) | VII, VIII | Estonia, the security record of internet and blockchain voting, coercion, audits, digital identity from birth, open ledgers, and transparency for the powerful |
| [accountability.md](accountability.md) | IX | The EU's enforcement ladder, standing and judges, independent inspectors, personal liability and ecocide, unarmed policing, and Nordic prisons and restorative justice |
| [long-view.md](long-view.md) | X | Wales' Future Generations Act, river guardians and rights of nature, other future-generations bodies, precaution, long horizons, and the Guardians' design |
| [commonwealth.md](commonwealth.md) | I, XII | The Constitution for the Federation of Earth, world federalism and its critics, nations and communication, joining from anywhere, disarmament, the ICC, and the transition thresholds |
| [living-charter.md](living-charter.md) | XI | Unamendable clauses, amendment rules compared, generational review, reading by spirit, and exit and secession |
| [money.md](money.md) | IV, open questions | Supranational money, alternatives to one currency, and indexing a planet-wide limit to prices |

## Round two: an efficient Terran government

Made on 11 October 2026 from Kara's brief: an efficient form of Terran-wide government. Every terran voting on every question is ruled out, and the brief asks for something more modern than the 18th-century template. Each note ends in design patterns and options; three also add a design sketch. The proposal built from them is [../proposals/modern-terran-government.md](../proposals/modern-terran-government.md).

| Note | Covers |
| --- | --- |
| [scale-and-federalism.md](scale-and-federalism.md) | How governing scales; how many decisions a large polity makes; what universal voting would cost in attention; a minimum planetary core |
| [polycentric-governance.md](polycentric-governance.md) | Ostrom's polycentricity; functional and personal (non-territorial) jurisdictions; bottom-up confederations; the Montreal Protocol, the IETF and ICANN as planetary precedents |
| [sortition-at-scale.md](sortition-at-scale.md) | Legislatures by lot: designs, permanent allotted bodies in practice, selection statistics, capture, costs and throughput |
| [executive-and-administration.md](executive-and-administration.md) | Collegial executives, merit-based civil services, independent agencies, digital government at scale, and the cost of a thin planetary core |
| [decision-mechanisms.md](decision-mechanisms.md) | What can replace the universal vote, job by job: direct votes, delegation, quadratic voting, deliberative polls, AI mediation, participatory budgets, prediction markets |
| [failure-modes.md](failure-modes.md) | A threat model: emergencies, backsliding, capture, new attack surfaces in modern designs, the no-exit risk, and the safeguards to keep |
| [modern-governance.md](modern-governance.md) | How open-source communities govern themselves, experimental policy, rules as code, feedback-driven government, participation platforms |

## Round three: isonomy and the qualified lot

Made on 12 October 2026 from Kara's brief: name the form of government an isonomy, and modernise government by lot so that anyone can qualify in a field, with some bodies drawn by lot from the qualified. The notes cite the third working draft's numbering. The proposal built from them is [../proposals/isonomy.md](../proposals/isonomy.md).

| Note | Covers |
| --- | --- |
| [isonomy.md](isonomy.md) | The word and its early uses, Herodotus' constitutional debate, how Athens used lot and election, who counted, modern readings (Hayek, Arendt, Karatani), and names for government by lot today |
| [qualified-lot.md](qualified-lot.md) | Drawing by lot among the qualified: the IETF's nominating committee, lotteries in research funding, Florence and Venice, earned and lapsing membership, the epistocracy debate, capture by practitioners, and lived experience |
| [mixed-panels.md](mixed-panels.md) | What happens when ordinary people and experts sit in one body: lay judges, mixed citizen–politician assemblies, experts inside deliberation, status in small groups, and designs that keep experts advising |

## How the research was done

Round one was split into eleven strands, one per note, run in parallel. A twelfth pass checked the drafting session's research, and a review pass re-checked the claims the synthesis files lean on. Round two added seven strands, and round three three more. As of 12 October 2026 the three rounds had produced 1,305 sources after merging duplicates: 947 primary, 315 secondary and 43 tertiary, of which 1,084 are verified, 204 partial and 17 unverified ([SOURCES.md](../SOURCES.md) has the live counts). Every strand worked to the same rules:

- **Opened, not searched.** Claims rest only on pages that were opened and read; search snippets don't count. A source that mattered but couldn't be opened is cited only to say so, and is marked unverified.
- **Primary first.** Strands preferred the statute, treaty, ruling, original paper or official statistics, and used scholarship and journalism for evaluation.
- **Raw text for figures.** Numbers and quotes were confirmed against the page's raw text, fetched with `curl_cffi` impersonating Chrome where sites block plain clients. They were not taken from a model's summary of the page.
- **Content, not status.** A page that answers but shows something else counts as not found.
- **Evidence against counts too.** Each note reports evidence that cuts against the Charter's choices as plainly as evidence for them, and ends with options rather than decisions.
- **Honest provenance.** Every check is recorded as machine-performed (`checked.by: claude`) with its date and result. None of it is Kara's own verification.
