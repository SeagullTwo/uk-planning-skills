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
| `planning-portal-registry.json` | The **index**: one small row per authority — name, aliases, ONS code, portal URL, vendor, status, `scriptable`, and the path to its profile. Loaded every time. |
| `authorities/<slug>.json` | The **profile**: everything specific to one authority — endpoints, parameters, headers, quirks, pacing, bot protection, browser routes, verification log. Loaded only for the authority in play. |
| `authorities/_schema.json` | The contract the profiles validate against. Every field carries a description saying what it is for. |
| `vendors.json` | How to recognise each portal product, and which recipe applies. Needed only when identifying an **unknown** portal. |
| `CHANGELOG.md` | Design decisions and their rationale, per revision. |

**Why the split.** The index resolves *which* council and *which* vendor; the profile is
fetched once you know. That keeps the hot path to a single small load instead of pulling
every council's quirks into context to answer a question about one.

**The index is derived from the profiles.** A profile is the source of truth for its
authority; the index row restates a handful of its fields so a lookup needs one small
read. When you change a profile, update its index row to match — they must not drift, and
where they disagree the profile is right.

## Using the data without the skill

The profiles are plain JSON against a published schema, so they are usable on their own —
by other tooling, or by a person deciding whether a portal is worth the effort. Two fields
carry most of that weight:

- **`retrieval.scriptable`** — can documents be downloaded by a plain HTTP client?
  **Tri-state, and the third state is the common one.** `true` = verified here. `false` =
  tried and could not (browser-only, blocked, broken), so don't start an automated run.
  **`null` = not tested yet, which is not the same as `false`** — attempt it and record
  what happens. Most authorities are `null`; flattening that into `false` would turn the
  registry into a list of reasons not to try.
- **`retrieval.difficulty`** — what it costs when it *does* work: `routine` (the recipe as
  written), `quirky` (needs the recorded per-authority adjustments), `fragile` (timeouts,
  rate limits, partial failures), `browser-only`, `blocked`. A portal can be `tested-ok`
  and still `fragile`.

**`ons_code`** carries the GSS code, which joins a profile to the LPA datasets and to
`planning.data.gov.uk`. It is `null` where one does not apply — national parks, joint
planning services, and authorities outside England.

**`retrieval.quirks[]`** is the per-authority trap list. Entries flagged **`"silent": true`**
are the ones that matter most: failures that *report success*. A search whose filter is
silently ignored so the whole register comes back; a register that never publishes
third-party comments, so a "complete" fetch quietly returns no objections. A run that hits
one of these looks clean and is wrong.

**`portal.committee_papers`** names the committee system (usually Modern.gov), its host and
the planning committee id(s), where committee reports, update sheets and minutes are
published there rather than on the portal. Where it is set, a portal-only retrieval of a
committee decision is incomplete.

Where a portal is hard, the profile says so in terms: `bot_protection` names the obstacle
and what a non-browser client actually sees, and `browser_route.url_template` gives the
deep link to hand a person instead. **It never records a way around a challenge** — the
point of that field is to make a tool stop cleanly, not to help it continue.

## How it works, briefly

1. **Resolve** the council in the index to its portal URL + vendor — index first, then the
   [PlanIt API](https://www.planit.org.uk/) as a live national directory.
2. **Load that authority's profile** and check `scriptable` before planning anything. If
   it is `false`, hand the user the browser route instead of starting a run.
3. **Identify** the vendor from the portal's markup, where the council is new
   (detection signatures in `vendors.json`).
4. **Apply** that vendor's recipe with the profile's endpoints, headers and quirks laid
   over it: search the reference → find the detail page → enumerate document links →
   download, all with one session.
5. **Verify** each download by magic bytes and **record** the result — the index row and
   the profile's `verification` log.

## Responsible use — please read

This skill accesses records councils publish **for public inspection**, the way a member
of the public would. It is bound by the rules in the skill's *Scope and responsible use*
section. In short:

- **Targeted retrieval, not bulk harvesting.** Fetch the specific application a user
  needs; don't scrape or monitor whole registers.
- **Never defeat a bot challenge.** If a portal serves a real challenge/`Blocked` page,
  stop and hand the user a browser deep link. The recipes are designed around this.
- **Be a good citizen:** identifying User-Agent with a real contact on PlanIt calls,
  pace requests (~1–2 s/host minimum), honour `429`/`Retry-After`, don't parallelise
  against one council.
- **`robots.txt` is honoured for enumeration; a user-directed retrieval is not crawling.**
  `robots.txt` addresses crawlers and indexers — systems traversing a site on their own
  initiative. Fetching the documents on an application a person has named is that person
  acting through a tool, and an AI-assisted human is still a human exercising the right to
  inspect a public register. **The test is initiative, not technology:** one named
  application for one person is human-directed; sweeps, monitoring, whole-register
  harvests and cross-authority dataset building are crawling, and `robots.txt` governs
  them in full, `Crawl-delay` included. This changes nothing else — pacing still binds, a
  bot challenge still means stop, and terms of use that expressly prohibit automated
  access are a stronger signal than a default `robots.txt` and are honoured.
- **You are told when it applies.** Where a portal's `robots.txt` asks automated clients
  off the path, the skill says so when it hands the documents over, explains why it
  proceeded, and offers the browser link instead. It is your name on the request, so it
  is your call — and if you say stop, it stops.
- **Paced so the claim is true rather than rhetorical:** at least 2 s between requests to
  one host (5 s where a portal has shown strain), one connection at a time, `Crawl-delay`
  honoured even on a user-directed fetch, and a second `429` is a full stop. A person does
  not issue forty requests a second.
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

Resolve the portal + vendor, run the recipe end-to-end, verify a real download by magic
bytes, then write `authorities/<slug>.json` against `_schema.json` and add or update its
row in the index.

**The invariants a profile must satisfy.** `_schema.json` enforces the shape; these are the
consistency rules it cannot express, and they are the ones that matter:

- `retrieval.scriptable` must agree with `retrieval.status` — `false` for `browser-only`,
  `blocked` and `broken`; `true` for `tested-ok`.
- A profile that is **not** `scriptable` must carry a `browser_route` — telling a caller to
  stop without saying where to send the user leaves them worse off than before.
- `bot_protection` and `scriptable: true` may only coexist where `applies_to` limits the
  protection to one host.
- `slug` must match the filename, and be unique.
- `portal.vendor` must be one of the index's `conventions.vendor_ids`.
- Every quirk needs a non-empty `summary` — it is the line a human skims.

**Before you write anything down, decide which of three kinds it is.** This is the rule
that keeps the files small and stops a recipe forking into forty divergent copies:

1. **True of the vendor** — every Idox install, every Atrium install → a **recipe in
   `SKILL.md`**, written once. Never copy it into a profile.
2. **True of this authority's portal** — its hostname, its `FileSystemId`, a header this
   install needs, a parser trap in its metadata, its rate limit → **the profile**.
3. **About which applications count as this council's own decisions** — reference prefixes
   in and out, type suffixes, adjoining-authority consultations decided elsewhere → **not
   retrieval at all.** It goes in the profile's `cohort_scope` key, which retrieval
   ignores, pending a skill that should own it.

Two standards of proof worth keeping to: `status: tested-ok` means a real file was
downloaded end to end, and `verification[].verified_download: true` means it was checked
by magic bytes. Don't assert either from a status code alone.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; you are responsible for
using it in line with each portal's terms of use and applicable law.
