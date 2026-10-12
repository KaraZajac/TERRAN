# TERRAN

**The Terran Charter, and the thinking, research and sources behind it.**

The Charter sets out the founding principles of Terran Humanism:

- Terrans are one people, without nations.
- Every terran is owed enough to live with dignity, and no one may push the planet past its limits.
- Between that floor and that ceiling lies a safe and just space, where every terran is free to build their own utopia.

The Terran Commonwealth it describes grows by choice and in stages, never by force.

**Read it:** [CHARTER.md](CHARTER.md), the working draft of 10 October 2026, by Kara Zajac.

## What's here

| Path | What it holds |
| --- | --- |
| [CHARTER.md](CHARTER.md) | The Charter itself: the living text. |
| [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) | Questions for the next draft, and what the research says about each. |
| [proposals/](proposals/README.md) | Worked designs for the next draft, starting with a modern, efficient Terran government. |
| [thoughts/](thoughts/README.md) | The reasoning: how the research became clauses, how the draft is built, and where it's under strain. |
| [research/](research/README.md) | The drafting session's research, checks on its sources, a research note for every Part, and a second round on how to govern a planet. |
| [SOURCES.md](SOURCES.md) | Every source cited, with what it supports and how it was checked. Generated. |
| [sources/](sources/README.md) | The source records behind SOURCES.md, one YAML file per research note. |
| [CHANGELOG.md](CHANGELOG.md) | The Charter's draft history. |
| [RIGHTS.md](RIGHTS.md) | What the public domain dedication covers, and what it doesn't. |

## Working on it

- **Change the Charter** by editing CHARTER.md, then add a line to CHANGELOG.md saying what changed and why. Part VII.5 asks for amendments to be recorded on an open, tamper-evident ledger; until the Commonwealth has one, this repository's history serves.
- **Add a source** to the matching file in `sources/` and cite it in a note by its id in square brackets. Then run `make sources` to validate the records and regenerate SOURCES.md. The record format is in [sources/README.md](sources/README.md).
- **Mind who checked what.** Every source record says who checked it and when. The first pass, on 10 October 2026, was machine-performed by Claude; none of it is Kara's own verification.

## License

Everything in this repository, from the Charter to the research and the tools, is dedicated to the public domain under [CC0 1.0](LICENSE). Anyone may copy, translate, adapt, adopt or enact it, without permission or credit. [RIGHTS.md](RIGHTS.md) says what CC0 does and doesn't cover.
