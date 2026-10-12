# The Schedules

*The third layer of [The Terran Charter](../CHARTER.md) · third working draft, 12 October 2026*

The Schedules hold the numbers and lists the Articles use, so each can be checked, and changed, in one place. Every number carries its reason and a range.

| Schedule | What it holds | How it changes (Part V.6) |
| --- | --- | --- |
| [1. Safeguards](1-safeguards.md) | The numbers that hold power in check, such as term limits, emergency deadlines, petition thresholds, and the sizes of bodies that guard against capture | Only as the Articles do |
| [2. Settings](2-settings.md) | The numbers for tuning, such as the sizes of working bodies, deadlines for answers, and where taxes start | By planetary act, within each setting's allowed range |
| [3. World Regions](3-regions.md) | The regions the Charter counts | Only as the Foundations do |
| [4. The Boundaries](4-boundaries.md) | The Earth Science Panel's range and the ceiling's limit for each planetary boundary | Ranges as the Panel publishes them; limits by ceiling act |
| [5. Hazards](5-hazards.md) | The hazards for which an emergency may be declared, and what is never one | Hazards by planetary act; what is never one as the Articles do |

The Foundations keep their few numbers in their own text: two-thirds in two votes of all terrans, a year apart, to amend them; a science review every four years; and a review of the whole Charter every 25 years. Those change only by amendment (Part V.4).

**Why two kinds of number.** A safeguard is a number a passing majority could use to switch off a check on itself, such as the length of an emergency or a judge's term. So safeguards change only as the Articles do, by two votes of all terrans a year apart. Settings tune how the Commonwealth works, so a planetary act may change them, but only within ranges set in advance. The [Commentary](../commentary/schedules.md) explains the split.

**As data.** Schedules 1 and 2 are generated from [numbers.yaml](numbers.yaml). To change a number, edit its value there, change the linked number in the Articles to match, and run `make schedules`. `make check` fails if the Articles and the Schedules disagree, so the text can't show a number the Schedules don't set.
