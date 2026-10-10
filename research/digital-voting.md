# Digital identity, online voting and open ledgers

*Research note · Charter Parts VII.2, VII.5, VII.6, VIII.5, VIII.6 and the "Paper votes" open question · first pass, 10 October 2026 · compiled by Claude, not yet reviewed by Kara*

Part VIII.5 follows Estonia's revoting rule, but its wording contradicts itself and overstates what revoting can do. Part VIII.6 rightly splits voting keys, yet two elections since November 2025 lost every electronic vote through key-handling failures. No system yet delivers secret, verifiable, failure-tolerant and changeable votes together online, which supports keeping paper for Charter votes. A compulsory birth-issued ID that gates voting (VII.2–3) runs against Jamaica's 2019 ruling and the EU's voluntary wallet.

## What the Charter says

- **VII.2–3:** "Every terran holds a secure digital identity from birth", and votes "using their secure digital identity".
- **VII.5:** Decisions, spending and amendments go on "open, tamper-evident ledgers, using blockchain wherever it truly helps."
- **VII.6:** Openness rises with wealth or power; "Everyday private life stays private."
- **VIII.5:** The identity "never reveals how they voted". "A later vote replaces an earlier one, and a vote cast in person replaces any cast online", so a pressured vote "can always be changed".
- **VIII.6:** Results are audited before taking effect; a failed audit means a new vote. Charter votes are "also cast on paper". Keys are "held by several independent bodies, so no single failure can lose a vote."
- **Open question:** keep amendments on paper until online voting is "fully secured", or go all-digital?

Part VII credits Estonia's digital government; VIII.5–6 credit no precedent.

## Precedent map

| Charter clause | Precedent | What the Charter keeps | What it changes |
| --- | --- | --- | --- |
| VII.2–3 | Estonia's ID card (2002) and X-Road (2001) | One secure ID for voting and services | Issued from birth, worldwide, with no state registry behind it |
| VII.2 | India's Aadhaar; EU Digital Identity Wallet | Universal ID at scale | Silent on biometrics, purpose limits and voluntariness; EU use is voluntary by law |
| VII.5 | Certificate Transparency logs; Estonia's KSI | Tamper-evident public records | Names "blockchain"; CT and KSI are hash-tree logs, not blockchains |
| VII.6 | Norwegian and Finnish tax lists; Ukraine's e-declarations | Wealth and income open to view | Scales with power; Norway exposes everyone, Ukraine only officials |
| VIII.5 | Estonia's i-voting: revoting plus paper override | Online revoting; in-person vote wins | "Later replaces earlier" is order-based; Estonia's rule is paper-wins |
| VIII.6 | Risk-limiting audits; end-to-end verifiable voting with threshold keys | Audit before effect; split keys | "Failed audit means new vote"; "several bodies" with no threshold |

## Estonia: ID card, X-Road and i-voting

X-Road launched in 2001 [niis/2026_x-road-history], the first ID card was issued on 28 January 2002 [laasik/2014_estonian-id-card], and online voting began in 2005 [estonia-seo/2026_i-voting-statistics].

| Election | I-voters | Share of participating voters | I-votes cancelled by a paper vote | Repeat i-votes replaced | Voters who verified their i-vote |
| --- | --- | --- | --- | --- | --- |
| Riigikogu 2023 | 313,514 | 51.1% | 1,332 | 10,787 | 5.5% |
| European Parliament 2024 | 153,848 | 41.7% | 578 | 3,627 | 9.9% |
| Local 2025 | 270,818 counted | 45.6% (270,818 of 594,117; my calculation) | not published | about 8,000 annulled in total | not published |

Sources: 2023–2024 rows [estonia-seo/2026_i-voting-statistics]; 2025 counts [err/2025_ekre-e-vote-recount]; 8,000 annulled [err/2026_annulled-e-votes].

**Rules.** Voters may re-vote online until Saturday evening of election week; the last i-vote counts [estonia-seo/2026_internet-voting-in-estonia]. A paper vote cancels all the voter's i-votes, even later ones [estonia-seo/2026_i-voting-faq]. Since 2021 this also works on election day [estonia-seo/2026_internet-voting-in-estonia] [err/2021_polling-stations-flexible] [err/2025_supreme-court-declines-ekre].

**History.** A May 2005 bill allowed paper overrides on election day until 16:00. After a presidential veto, changes were limited to advance polls, six to four days before voting day [estonia/2005_supreme-court-3-4-1-13-05]. In 2019, online voting closed two hours before the last advance polls, leaving time to vote on paper [krips-willemson/2019_coercion-resistant-remote-voting]. Springall et al. describe an election-day override in 2013 [springall/2014_estonian-i-voting-security], which the other sources do not support.

**Courts.** The President had vetoed revoting as unequal. On 1 September 2005 the Supreme Court upheld it as "an essential supplementary guarantee" of free, secret voting [estonia/2005_supreme-court-3-4-1-13-05]. It found "no other equally effective measures", while calling booths the most effective protection. On 30 March 2023 the court rejected all Riigikogu election complaints, two of EKRE's for lateness [err/2023_supreme-court-election-complaints]. But it said e-voting rested too much on subordinate rules, and the essentials belong in law. Parliament amended the election acts in May 2024, also allowing smart-device voting and Smart-ID [err/2024_e-voting-regulation-changes].

In October 2025 the court ruled that publishing source code after the test vote broke the law [err/2025_supreme-court-source-code]. The 2027 timetable now requires it five days before the test [estonia-seo/2026_riigikogu-2027-schedule]. EKRE said the auditor could not confirm ballot-box integrity at the recount, and sought a third count [err/2025_ekre-e-vote-recount]. Observers from the NGO Fair Elections said the auditor had not checked that the published code was the code running [err/2025_observers-e-voting]. The election office says its 8,000 annulled e-votes could not have been altered undetected [err/2026_annulled-e-votes].

**Mobile voting.** The 2024 law lets the electoral service allow smart-device voting once risks are managed [err/2024_e-voting-regulation-changes]. The Academy of Sciences' cybersecurity committee found no high or critical risks, but six medium ones, including proving the mobile app authentic [ria/2025_i-voting-20-years]. As of 10 October 2026, I found no decision allowing it for the March 2027 election.

**Security.** Springall et al. rebuilt the system in a lab after observing the 2013 election [springall/2014_estonian-i-voting-security]. They showed client malware that silently changed votes despite the verification app, and a counting-server attack, and urged Estonia to stop. In late August 2017, researchers warned of a flaw in 750,000 ID cards issued after 17 October 2014 [err/2017_id-card-security-risk]. The ROCA flaw let anyone derive a private key from the public key [nemec/2017_roca]. A worst-case 2048-bit key took under 100 CPU-years, about $40,000 on AWS. Separately, the police board said supplier Gemalto had generated private keys outside the chip for over 700,000 cards [err/2018_ppa-gemalto-claim]. It claimed €152 million and settled for €2.2 million in 2021 [ppa/2021_gemalto-settlement].

Differs from the drafting-session research: it says a paper vote cancels an online one. That is right, but since 2021 it also applies on election day, and paper wins regardless of order.

**For the Charter:** VIII.5 copies Estonia's intent but not its precedence rule (see Tensions). Estonia's courts found its legal basis thin (2023) and its code release late (2025), so procedure needs drafting too. ROCA and Gemalto show one ID scheme can fail for most holders at once.

## The expert record on internet and blockchain voting

The US National Academies (2018) urged human-readable paper ballots, and risk-limiting audits before certification [nasem/2018_securing-the-vote]. They advised against returning marked ballots over the Internet for now, pending "very robust guarantees of security and verifiability". Blockchains, they wrote, "introduce additional security vulnerabilities"; malware can change a vote before it reaches the chain.

| Date | Swiss e-voting event |
| --- | --- |
| 25 Feb–24 Mar 2019 | Public intrusion test of Swiss Post's new verifiable system |
| 12 Mar 2019 | Researchers find a universal-verifiability flaw after the code release |
| 29 Mar 2019 | System withdrawn for the 19 May vote |
| 26 Jun 2019 | Federal Council drops plans for regular use; trials to be redesigned |
| 3 Mar 2023 | Trials resume in Basel-Stadt, St Gallen and Thurgau, under ordinances in force since 1 July 2022 |
| 8 Mar 2026 | Basel-Stadt cannot decrypt 2,048 e-votes |
| Jun–Sep 2026 | Lucerne and Neuchâtel licensed; about 222,000 voters (3.95%) eligible for 29 November 2026 |

Sources: [switzerland-fch/2026_e-voting-media-releases] [switzerland-fch/2026_neuchatel-licence].

The 2019 flaw let a mix server holding trapdoor values forge a valid-looking shuffle proof that altered votes [lewis-pereira-teague/2019_ceci-nest-pas-une-preuve]. Since 2004, 15 cantons have run over 300 trials, always for part of the electorate [switzerland-fch/2026_e-voting-overview]. Basel-Stadt's lost votes came from Swiss abroad and voters with disabilities [basel-stadt/2026_e-voting-external-analysis]. The Chancellery blamed irregular handling of PIN-protected USB sticks holding the decryption key, not Swiss Post's system [switzerland-fch/2026_basel-stadt-incident]. Outcomes were unaffected, but voters' political rights were violated. Other cantons relied on a strict four-eyes rule and added storage media types and checklists [switzerland-fch/2026_june-vote-authorisations].

Differs from the drafting-session research: it says Basel-Stadt's failure involved "no attacker". The Chancellery said human error could not be excluded, and the prosecutor opened a criminal case on initial suspicion [switzerland-fch/2026_basel-stadt-incident]. I found no published result of the canton's external analysis as of 10 October 2026.

Voatz, a blockchain-backed phone app, was used in West Virginia in 2018. Specter, Koppel and Weitzner found flaws letting attackers "alter, stop, or expose" a vote; West Virginia dropped it for 2020 [specter/2020_voatz-security-analysis]. Trail of Bits found 79 issues, a third high-severity, with 34 technical issues still unfixed [trailofbits/2020_voatz-report]. Park, Specter, Narula and Rivest warn that online and blockchain voting "would greatly increase the risk of undetectable, nation-scale election failures" [park/2021_bad-to-worse]. They report turnout effects from slightly negative to slightly positive, and say Estonian online voting may favour richer, better-educated voters.

**For the Charter:** This record supports paper for high-stakes votes. Switzerland's cautious path, with a capped electorate, public tests and published code, still failed in 2026 on key handling. Blockchain fixes none of these problems and adds new ones.

## Coercion, revoting and the in-person override

Juels, Catalano and Jakobsson define coercion-resistance: a coercer demanding a vote, an abstention or the voter's keys cannot tell whether the voter complied [juels/2002_coercion-resistant-elections]. Krips and Willemson call Estonia's scheme pure revoting [krips-willemson/2019_coercion-resistant-remote-voting]. Its main weakness is a coercer who stays until voting ends. Voters far from a polling place, a main reason for online voting, then cannot vote freely. Insiders could also see who abstained, and an attacker can use revoting to overwrite a vote. Park et al. add that revoting fails if the coercer can watch until polls close, "because they live together" [park/2021_bad-to-worse].

VoteAgain shows revoting resists coercion only if filtering out superseded ballots is deniable [lueks/2020_voteagain]. Filtering by a trusted party is deniable but not verifiable; earlier verifiable designs needed quadratic work. VoteAgain scales to millions, but assumes the coercer leaves before polls close and trusts a tally server. Springall et al. judged Estonia strong against in-person coercion but open to spyware and server-side secrecy attacks [springall/2014_estonian-i-voting-security].

**For the Charter:** Revoting plus in-person override is what Estonia has used nationally since 2005. It fails against household coercion and for voters far from a booth, and its filtering cannot be publicly checked. Estonia's dispute over 8,000 annulled e-votes is that problem in practice.

## Audits, verifiability and distributed keys

A risk-limiting audit hand-checks random paper ballots until they confirm the outcome, or escalates to a full hand count [lindeman-stark/2012_gentle-introduction-rlas]. It "cannot harm correct outcomes", but needs voter-verified paper; paperless systems "cannot be audited this way". Workload depends on the margin, not the electorate. About 97 ballots could confirm California's 2008 presidential result among 13.7 million at a 10% risk limit. At a 52% winning share, the expected sample is 3,860.

End-to-end verifiable systems publish encrypted ballots and proofs anyone can check. Helios needs every trustee to decrypt, and its own FAQ advises against public-office use [helios/2026_faq]. Scantegrity II ran Takoma Park's binding 2009 election; about 66 of 1,728 voters, almost 4%, checked their codes in time [carback/2010_scantegrity-takoma-park]. ElectionGuard's "guardians" create the key jointly; a quorum decrypts, and each guardian shares a recovery method [electionguard/2026_glossary]. In its 2022 Preston, Idaho pilot, 40% of voters opted in, and a hand count was the official tally [electionguard/2022_preston-idaho].

Shamir's scheme splits a key so any k of n shares rebuild it, while k − 1 reveal nothing [shamir/1979_how-to-share-a-secret]. With n = 2k − 1 it survives losing k − 1 shares. In November 2025 the IACR voided its Helios election after one of three trustees lost a key; it moved to 2-of-3 [iacr/2025_election-update].

| Charter guarantee | Best current technique | Known limit |
| --- | --- | --- |
| Secret ballot | Encrypt on the device; split the decryption key | Revoting keeps identity linked to ballots until tally [estonia/2005_supreme-court-3-4-1-13-05] |
| Verifiable count | Paper with risk-limiting audits; end-to-end proofs | Catching device malware relies on voters checking their own ballots; 4–10% do [carback/2010_scantegrity-takoma-park] [estonia-seo/2026_i-voting-statistics] |
| No single failure | Threshold keys with backups | Key handling lost whole elections in 2025 (every share required) and 2026 (USB sticks holding the key) [iacr/2025_election-update] [switzerland-fch/2026_basel-stadt-incident] |
| Changeable vote | Revoting plus in-person override | Fails against a coercer present until close [krips-willemson/2019_coercion-resistant-remote-voting] |
| All four, online | None known [nasem/2018_securing-the-vote] [park/2021_bad-to-worse] | Universal verifiability with receipt-freeness needs private channels; with unconditional privacy, it needs every voter to vote [chevallier-mames/2010_incompatible-properties] |

**For the Charter:** "Several independent bodies" must mean a k-of-n threshold with tested recovery. With paper, a failed audit leads to a hand count that corrects the result, so no re-run is needed. Without a threshold, a re-run rule invites attack: destroy one share, force a new vote. "Guardians", ElectionGuard's term for key holders, would clash with Part X.

## Digital identity from birth

About 800 million people lacked official ID in 2024; 2.8 billion lacked a government digital ID usable online [worldbank-id4d/2025_global-dataset]. UIDAI reports 145.32 crore (1.45 billion) Aadhaar enrolments and 2,632.51 crore eKYC transactions [uidai/2026_homepage-counters]. Biometric checks in India's largest social programme cut corruption, but 1.5–2 million eligible people lost benefits at some point [muralidharan/2020_identity-verification-standards]. The authors blame mainly how the transition was managed.

Differs from the drafting-session research: it gives 1.38 billion people; UIDAI's counter now reads 1.45 billion enrolments, which are not the same as living holders. Its "12% failure rate" and "3 million voters" figures rest on Wikipedia, and I did not verify them.

India's 2023 amendment, passed in August, requires birth certificates, for people born afterwards, for school admission, voter lists and government jobs [prs/2023_births-deaths-amendment]. PRS warns unregistered children could be barred from school and later from voting; birth registration was 93% in 2019. On 26 September 2018 India's Supreme Court struck down section 57, which let private firms demand Aadhaar [thequint/2018_aadhaar-section-57]. Aadhaar stayed mandatory for tax filing. In April 2019 Jamaica's Full Court unanimously voided its national ID law [jamaica/2019_robinson-v-attorney-general]. It objected to compulsory biometrics, denial of services and weak limits on profiling: "The danger of a 'big brother state'… is real."

EU law makes the digital identity wallet "voluntary" and bars disadvantaging non-users [eu/2024_regulation-2024-1183]. It requires selective disclosure and pseudonyms, bars issuers and others from tracking use, and requires unlinkability where identification is unnecessary. In June 2024, 16 cryptographers said the draft design fell short and urged BBS anonymous credentials [eudi-cryptographers/2024_arf-feedback]. The thread shows a live dispute over post-quantum security. Estonia's Data Tracker shows citizens how their data were used, in registers that implement it [ria/2026_data-tracker].

**For the Charter:** A universal ID meets a real need. But "from birth" plus voting through the ID makes it compulsory in practice and a gate to the vote. Jamaica struck that model down, India narrowed it, and the EU keeps its wallet optional. The draft is silent on enrolling people with no state registry, and on preventing duplicate identities.

## Open ledgers: blockchain or transparency log?

NIST IR 8202 notes that in one widely cited "Do you need a blockchain?" flowchart, most paths lead to "no" [nist/2018_ir-8202]. It urges checking whether existing technology does better. Nothing stops false data entering a chain, and recorded data can be deprecated but never removed. Certificate Transparency (RFC 6962, 2013; RFC 9162, 2021) uses append-only Merkle-tree logs [ietf/2013_rfc-6962] [ietf/2021_rfc-9162]. Logs do not prevent misissuance but "ensure that interested parties … can detect" it, and anyone can monitor them. Chrome checks site certificates against its CT policy [chrome/2026_ct-policy]. Estonia's KSI publishes root hashes of per-second global hash trees [buldas/2013_keyless-signatures-infrastructure]; e-Estonia calls it "blockchain inspired" [e-estonia/2026_ksi-blockchain].

**For the Charter:** CT and KSI give tamper-evidence without tokens or mining. The hard parts are independent log operators, public monitors, and keeping personal data off permanent logs. A ledger proves what was recorded, not that it is true.

## Transparency that scales with power

| Scheme | Who is exposed | Access | Evidence |
| --- | --- | --- | --- |
| Norway tax lists | Adult taxpayers with a tax assessment | Online after login; up to 500 views a month; the person sees who looked [skatteetaten/2026_search-the-tax-lists] | 2001 online release: reported income rose about 3% more among business owners where access changed most [bo-slemrod-thoresen/2015_taxes-on-the-internet]; happiness gap between rich and poor up 29% [perez-truglia/2020_income-transparency-well-being] |
| Norway, 2014 change | Same | Searches no longer anonymous | Searches fell 88%; the author concludes the lists were used mainly to look up social contacts [perez-truglia/2019_income-transparency-nber-wp] |
| Finland | Every individual taxpayer | Tax-office terminals and phone only; media get electronic data; no internet publication [vero/2026_public-individual-income-tax-info] [vero/2026_how-to-search-public-tax-info] | None found in this pass |
| Ukraine e-declarations | Officials and families, about 1.7% of the population | Public online register since 1 September 2016, personal data redacted [imf/2026_ukraine-asset-declaration-system] | See below |

Sweden's records are requested by phone, non-anonymously, which makes them far less used than Norway's [perez-truglia/2019_income-transparency-nber-wp]. Ukraine receives about 700,000 declarations a year, a "wall of data" for a small verification team [imf/2026_ukraine-asset-declaration-system]. Declarations were suspended under martial law and restored in October 2023. The IMF found a fixed quota of 1,000 checks a year chased minor violations rather than senior officials. In 2020 the Constitutional Court struck down criminal penalties for false declarations; parliament restored them [euronews/2020_ukraine-restores-anti-corruption-law]. In January–August 2026, risk-based checks found violations in 571 of 574 declarations, leading to 125 criminal proceedings [nacp/2026_full-verifications-2026].

**For the Charter:** The evidence favours VII.6's scaled design over Norway's universal one. Universal disclosure deters some evasion but mostly feeds curiosity and widens well-being gaps; logging viewers cut snooping. Disclosure without verification capacity yields data walls, and some disclosures need security exemptions.

## Tensions and open problems

- **VIII.5 contradicts itself.** "A later vote replaces an earlier one" lets an online vote cast after an in-person vote replace it, against the next clause. Estonia's rule is paper-wins, whatever the order [estonia-seo/2026_i-voting-faq].
- **"Always" overclaims.** Revoting fails against a coercer present until close, or for voters far from a booth [krips-willemson/2019_coercion-resistant-remote-voting] [park/2021_bad-to-worse].
- **"Never reveals" needs qualifying.** Revoting keeps identity attached to encrypted ballots until filtering, so secrecy rests on the key holders [estonia/2005_supreme-court-3-4-1-13-05].
- **Key custody can cause the failure VIII.6 aims to prevent.** Basel-Stadt and the IACR each lost a whole electronic vote to key handling [switzerland-fch/2026_basel-stadt-incident] [iacr/2025_election-update].
- **A re-vote rule creates a lever.** Without a threshold, losing or destroying one key share can force a new vote.
- **The ID gates the vote.** If voting requires the digital ID (VII.3), anyone without one is disenfranchised; India's birth-certificate rule shows the risk [prs/2023_births-deaths-amendment].
- **Global enrolment is unaddressed.** One ID per person "from anywhere" (XII.1), without state registries, invites duplicates; biometric deduplication raises Jamaica-type objections [jamaica/2019_robinson-v-attorney-general].
- **Scale.** Estonia's peak was 313,514 i-voters, and Switzerland admits about 222,000 voters. A planetary system would face state-level attackers, as Springall et al. warned [springall/2014_estonian-i-voting-security].
- **Who online voting serves.** Basel's lost votes belonged to citizens abroad and disabled voters [basel-stadt/2026_e-voting-external-analysis].
- **Ledgers versus privacy.** Blockchain data cannot be removed, which clashes with IX.10's privacy exception [nist/2018_ir-8202].
- **VII.6 has no thresholds.** Without them it reads like Norway's universal lists, against "everyday private life stays private".

## Options for the next draft

- **VIII.5 precedence:** "An in-person vote is final and replaces any online vote, whenever cast. Among online votes, the last counts. Online voting closes before in-person voting does."
- **VIII.5 wording:** "can be changed until voting closes" instead of "can always be changed".
- **VIII.6 keys:** a k-of-n threshold (say 3-of-5), public key ceremonies, backup media and recovery drills.
- **VIII.6 audits:** with paper, a failed audit triggers a full hand count; a new vote only if the record is lost.
- **VIII.6 code:** publish code before any test vote, and verify that the running code matches it.
- **VII.2 identity:** a right, not a duty; non-digital routes to every service and to the vote; anonymous credentials to prove eligibility.
- **VII.2 enrolment:** parents may register a birth; each person activates their digital credential at an age of consent.
- **VII.5 ledgers:** "tamper-evident public logs run and monitored by several independent bodies"; blockchain only where no single operator can be trusted.
- **VII.6 thresholds:** disclosure lines by wealth and office, viewer logs, funded verification and security exemptions.
- **Paper votes A, paper governs:** Charter votes on hand-marked paper in person, with a risk-limiting audit. Strongest evidence base, but costliest and hardest for remote voters.
- **Paper votes B, dual channel:** online voting allowed, but the paper count is official for Charter votes, as in Preston, Idaho.
- **Paper votes C, conditional switch:** paper until named tests pass: public intrusion tests, threshold keys, verifiable deniable revoting, a failure-free election cycle. The switch itself needs a two-thirds paper vote.
- **Paper votes D, all-digital:** end-to-end verifiable online voting throughout. Cheapest, but against the National Academies' advice and the research here.
- **Paper votes E, risk-scaled:** paper for amendments and planetary votes; verifiable online voting for community votes; paper re-checks for close results.

## Sources

| Source id | Title | Tier | Checked |
| --- | --- | --- | --- |
| estonia-seo/2026_i-voting-statistics | Statistics about Internet voting in Estonia | primary | verified |
| estonia-seo/2026_internet-voting-in-estonia | Internet voting in Estonia | primary | verified |
| estonia-seo/2026_i-voting-faq | Questions about i-voting | primary | verified |
| estonia-seo/2026_riigikogu-2027-schedule | Election activities and deadlines – Election of the Riigikogu 2027 | primary | verified |
| niis/2026_x-road-history | X-Road history | primary | verified |
| laasik/2014_estonian-id-card | The Estonian ID card | secondary | verified |
| estonia/2005_supreme-court-3-4-1-13-05 | Constitutional judgment 3-4-1-13-05 | primary | verified |
| err/2021_polling-stations-flexible | Voting at polling stations becomes more flexible from 2021 | secondary | verified |
| err/2023_supreme-court-election-complaints | Riigikohus lükkas kõik valimiskaebused tagasi | secondary | verified |
| err/2024_e-voting-regulation-changes | Riigikogu passes changes to e-voting regulation | secondary | verified |
| err/2025_ekre-e-vote-recount | EKRE requests local election e-vote recount | secondary | verified |
| err/2025_supreme-court-source-code | Supreme Court: e-voting source code must be published before test vote | secondary | verified |
| err/2025_supreme-court-declines-ekre | Supreme Court declines to hear EKRE local elections e-vote complaint | secondary | verified |
| err/2025_observers-e-voting | Observers say e-voting organization could be improved | secondary | verified |
| err/2026_annulled-e-votes | Electoral office: It was impossible to manipulate annulled electronic votes | secondary | verified |
| ria/2025_i-voting-20-years | I-voting: 20 years of progress | primary | verified |
| ria/2026_data-tracker | Data tracker | primary | verified |
| springall/2014_estonian-i-voting-security | Security Analysis of the Estonian Internet Voting System | primary | verified |
| nemec/2017_roca | ROCA: Vulnerable RSA generation (CVE-2017-15361) | primary | verified |
| err/2017_id-card-security-risk | Potential security risk could affect 750,000 Estonian ID cards | secondary | verified |
| err/2018_ppa-gemalto-claim | Police claim €152 million from ID card producer Gemalto | secondary | verified |
| ppa/2021_gemalto-settlement | A settlement agreement has been signed between the Police and Border Guard Board and Gemalto AG | primary | verified |
| krips-willemson/2019_coercion-resistant-remote-voting | On practical aspects of coercion-resistant remote voting systems | primary | verified |
| nasem/2018_securing-the-vote | Securing the Vote: Protecting American Democracy | primary | verified |
| switzerland-fch/2026_e-voting-media-releases | Media releases (e-voting) | primary | verified |
| switzerland-fch/2026_e-voting-overview | E-Voting | primary | verified |
| switzerland-fch/2026_basel-stadt-incident | E-Voting-Versuchsbetrieb: Weiteres Vorgehen nach dem Vorfall in Basel-Stadt | primary | verified |
| switzerland-fch/2026_june-vote-authorisations | E-Voting: Zulassungen für die Abstimmung vom 14. Juni 2026 erteilt | primary | verified |
| switzerland-fch/2026_neuchatel-licence | Der Bundesrat bewilligt den Einsatz von E-Voting im Kanton Neuenburg | primary | verified |
| basel-stadt/2026_e-voting-external-analysis | E-Voting: Basel-Stadt gibt Analyse … in Auftrag | primary | verified |
| lewis-pereira-teague/2019_ceci-nest-pas-une-preuve | Ceci n'est pas une preuve | primary | verified |
| specter/2020_voatz-security-analysis | The Ballot is Busted Before the Blockchain | primary | partial |
| trailofbits/2020_voatz-report | Our Full Report on the Voatz Mobile Voting Platform | primary | verified |
| park/2021_bad-to-worse | Going from bad to worse: from Internet voting to blockchain voting | primary | verified |
| juels/2002_coercion-resistant-elections | Coercion-Resistant Electronic Elections | primary | partial |
| lueks/2020_voteagain | VoteAgain: A scalable coercion-resistant voting system | primary | verified |
| lindeman-stark/2012_gentle-introduction-rlas | A Gentle Introduction to Risk-limiting Audits | primary | verified |
| helios/2026_faq | Helios Voting FAQ | primary | verified |
| carback/2010_scantegrity-takoma-park | Scantegrity II Municipal Election at Takoma Park | primary | verified |
| electionguard/2026_glossary | ElectionGuard glossary | primary | verified |
| electionguard/2022_preston-idaho | Preston, Idaho 2022 | primary | verified |
| shamir/1979_how-to-share-a-secret | How to Share a Secret | primary | verified |
| iacr/2025_election-update | Election 2025 Update | primary | verified |
| chevallier-mames/2010_incompatible-properties | On Some Incompatible Properties of Voting Schemes | primary | verified |
| worldbank-id4d/2025_global-dataset | ID4D Global Dataset | primary | verified |
| uidai/2026_homepage-counters | UIDAI homepage (Aadhaar dashboard counters) | primary | verified |
| muralidharan/2020_identity-verification-standards | Identity Verification Standards in Welfare Programs | primary | partial |
| thequint/2018_aadhaar-section-57 | Sec 57 of Aadhaar Act Struck Down | secondary | verified |
| prs/2023_births-deaths-amendment | The Registration of Births and Deaths (Amendment) Bill, 2023 | secondary | verified |
| jamaica/2019_robinson-v-attorney-general | Julian Robinson v Attorney General of Jamaica | primary | verified |
| eu/2024_regulation-2024-1183 | Regulation (EU) 2024/1183 (European Digital Identity Framework) | primary | verified |
| eudi-cryptographers/2024_arf-feedback | Cryptographers' Feedback on the EU Digital Identity's ARF | primary | verified |
| nist/2018_ir-8202 | Blockchain Technology Overview (NISTIR 8202) | primary | verified |
| ietf/2013_rfc-6962 | RFC 6962: Certificate Transparency | primary | verified |
| ietf/2021_rfc-9162 | RFC 9162: Certificate Transparency Version 2.0 | primary | verified |
| chrome/2026_ct-policy | Chrome Certificate Transparency Policy | primary | verified |
| buldas/2013_keyless-signatures-infrastructure | Keyless Signatures' Infrastructure | primary | partial |
| e-estonia/2026_ksi-blockchain | KSI blockchain | primary | verified |
| skatteetaten/2026_search-the-tax-lists | Search the tax lists | primary | verified |
| bo-slemrod-thoresen/2015_taxes-on-the-internet | Taxes on the Internet: Deterrence Effects of Public Disclosure | primary | partial |
| perez-truglia/2020_income-transparency-well-being | The Effects of Income Transparency on Well-Being | primary | partial |
| perez-truglia/2019_income-transparency-nber-wp | The Effects of Income Transparency on Well-Being (NBER WP 25622) | primary | verified |
| vero/2026_public-individual-income-tax-info | Public information on individual income taxes | primary | verified |
| vero/2026_how-to-search-public-tax-info | How to search the public information on income taxes and real estate taxes | primary | verified |
| imf/2026_ukraine-asset-declaration-system | Ukraine: Enhancing the Asset Declaration System for Public Officials | primary | verified |
| nacp/2026_full-verifications-2026 | Full verifications of declarations: in 8 months of 2026 | primary | verified |
| euronews/2020_ukraine-restores-anti-corruption-law | Ukraine's parliament defies court ruling and restores anti-corruption legislation | secondary | verified |
