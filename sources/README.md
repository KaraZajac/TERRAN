# Source records

One YAML file per research note (`research/<name>.md` pairs with `sources/<name>.yaml`), with one record per source. [SOURCES.md](../SOURCES.md) is generated from these files: run `make sources` after any change, and `make check` to confirm it's current.

## Record format

```yaml
- id: raworth/2012_safe-and-just-space
  title: "A Safe and Just Space for Humanity: Can We Live Within the Doughnut?"
  authors: ["Kate Raworth"]
  publisher: "Oxfam"
  date: "2012-02"
  url: "https://…"
  tier: primary
  kind: report
  parts: ["III"]
  supports: "What the research note uses this source for."
  checked:
    by: claude
    on: "2026-10-10"
    result: verified
    note: "What was opened, and where on the page the claim is."
```

| Field | Rule |
| --- | --- |
| `id` | `<author-or-org>/<year>_<slug>`, lowercase. Notes cite it in square brackets: `[raworth/2012_safe-and-just-space]`. Laws use the jurisdiction: `wales/2015_future-generations-act`. |
| `authors` | People only; leave it out for institutional works. |
| `date` | `"YYYY"`, `"YYYY-MM"` or `"YYYY-MM-DD"`, quoted. |
| `tier` | `primary`: the law, treaty, ruling, original paper, official data, or an organization's own text. `secondary`: scholarship and journalism. `tertiary`: encyclopedias and aggregators. |
| `kind` | `book`, `article`, `report`, `law`, `treaty`, `court`, `dataset`, `web` or `news`. |
| `parts` | The Charter parts the source informs: `Preamble`, `I` to `XII`, or `OQ` for the open questions. |
| `checked.result` | `verified`: the claim was found on the fetched page. `partial`: only part of it was, or only an abstract or landing page could be reached; a note starting `CONTRADICTED:` means the page says something materially different. `unverified`: the page could not be opened. |
| `checked.by` | Who made the check. Every check so far is machine-performed, by `claude`. `by: kara` marks Kara's own check and is only ever written by her. |

## How checks are made

- Cite only pages actually opened and read. A search snippet is not a source.
- Confirm figures and quotes against the page's raw text, not a summary of it.
- Match content, not status codes. Some sites answer 200 with placeholder or unrelated pages.
- Sites that block plain HTTP clients usually open with `curl_cffi` impersonating Chrome. Failing that, try a Wayback Machine snapshot.

## Merging

The same source can appear in several files. `tools/build_sources.py` merges records by `id`, combining their parts and keeping the strongest check.

The script fails on invalid records and on citations that don't resolve to a record. It warns about uncited records and about one URL filed under two ids.
