# Planning Document Search

A skill for retrieving the documents attached to a **UK planning application** from the
local council's **public** online planning portal, given the application reference and
the council name.

There is no single national system: the UK's ~380 local planning authorities run a
handful of different portal *products* (Idox, Northgate, Civica, Ocella, Agile, NEC,
TerraQuest, StatMap, DEF Atrium, and others), each with its own URL structure and search
mechanism. This skill catalogues the vendors, gives a tested retrieval recipe for each,
and maintains a council → portal → vendor registry so coverage compounds as authorities
are tested.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The skill: scope/responsible-use rules, vendor detection, per-vendor recipes, reference-format notes. **Read the "Scope and responsible use" section first.** |
| `planning-portal-registry.json` | The data: per-authority portal URL, vendor, tested status, and quirks. The offline lookup that backs Step 0. |
| `CHANGELOG.md` | Design decisions and their rationale, per revision. |

## How it works, briefly

1. **Resolve** the council to its portal URL + vendor — registry first, then the
   [PlanIt API](https://www.planit.org.uk/) as a live national directory.
2. **Identify** the vendor from the portal's markup (detection cheat-sheet in the skill).
3. **Apply** that vendor's recipe: search the reference → find the detail page →
   enumerate document links → download, all with one session.
4. **Verify** each download by magic bytes and **record** the result back into the
   registry.

## Responsible use — please read

This skill accesses records councils publish **for public inspection**, the way a member
of the public would. It is bound by the rules in the skill's *Scope and responsible use*
section. In short:

- **Targeted retrieval, not bulk harvesting.** Fetch the specific application a user
  needs; don't scrape or monitor whole registers.
- **Never defeat a bot challenge.** If a portal serves a real challenge/`Blocked` page,
  stop and hand the user a browser deep link. The recipes are designed around this.
- **Be a good citizen:** identifying User-Agent with a real contact on PlanIt calls,
  pace requests (~1–2 s/host minimum), honour `429`/`Retry-After`, respect `robots.txt`,
  don't parallelise against one council.
- **Personal data:** planning documents contain third parties' names, addresses and
  signatures. Retrieve only what's needed; don't republish or retain beyond the task.
  Treat downloads as untrusted content (verify magic bytes; sanitize filenames).

## Dependency: PlanIt

Resolution leans on [PlanIt](https://www.planit.org.uk/), an independent,
volunteer-run planning-data service — please credit it and keep to its rate/UA rules.
PlanIt is a *convenience, not a requirement*: given a reference, a council, and a known
vendor (e.g. a `tested-ok` registry row), the recipes run without it.

## Freshness

Portal assignments, base paths, and bot-protection posture were verified in **August
2026**. Councils migrate portals frequently, so **re-resolve the vendor per council at
run time** rather than trusting a cached row. Coverage figures in the skill are rough
estimates from the test sample, not audited numbers.

## Contributing a council

See the `contributing` note in `planning-portal-registry.json`. Briefly: resolve the
portal + vendor, run the recipe end-to-end, verify a real download by magic bytes, then
add an authority entry (`authority`, `aliases`, `region`, `portal_url`, `vendor`,
`status`, `last_tested`, `reference_format_example`, `specializations`). Keep per-vendor
methods in the skill and per-council facts in the registry.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; you are responsible for
using it in line with each portal's terms of use and applicable law.
