# Changelog — planning-document-search

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines are the point: they record the rationale so a future
editor understands the intent.

## Unreleased

### Added — national coverage: 43 profiles to 282

- **239 authorities harvested from data already collected, with no portal traffic at
  all.** Two joins: 106 Idox portals confirmed by an earlier national probe, and 133 more
  from PlanIt's planning-areas directory. _Why:_ the skill's commonest failure is not
  "could not download" but "did not know the council", and that half is fixable from
  existing data. Coverage of *identity* — name, aliases, ONS/GSS code, portal URL, a
  vendor hint and the applicable recipe — now spans most of the UK.

- **Everything harvested is `status: untested` with `scriptable: false`.** _Why:_ this is
  the whole discipline of the exercise. A portal URL is not a tested retrieval, and 282
  rows that *looked* verified while 239 were joins would be exactly the false-coverage
  failure this repo takes seriously elsewhere. The honest claim is "we know where this
  council's register is", and that is what the data says.

- **`portal.vendor_verified` and `portal.vendor_source` added.** _Why:_ a fingerprinted
  vendor and a guessed one are different claims, and at 282 rows the difference decides
  whether a run starts with the right recipe. The 106 Idox rows are `true` — a probe
  confirmed the advanced-search form. The 133 PlanIt rows are `false`, because PlanIt's
  `scraper_type` is a hint this skill already records as stale at one authority and wrong
  at another; each carries a `silent: true` quirk saying so, since choosing a recipe from
  an unverified label fails in a way that looks like a portal problem rather than a
  wrong-recipe problem.

- **The search-confirmed councils say what was and was not tested.** The 106 Idox rows
  carry a quirk recording that the survey exercised the advanced search successfully and
  **downloaded no documents at all** — so the documents tab, any external DMS and the
  file-GET gating are unverified there. _Why:_ "the search worked" and "retrieval works"
  are different findings, and conflating them is how a registry starts lying.

- **`retrieval.robots` populated where known** — for the Idox set, from a survey that
  read all 116 `robots.txt` files. Eight in ten disallow the search path.

### Known gaps at this revision
- **PlanIt holds 421 planning areas; 210 were fetched.** The remainder stopped at a `429`.
  The cause was ours: a first attempt paginated with a parameter PlanIt silently ignores,
  so 22 requests all returned page one and spent the budget for nothing. The correct
  parameter is `page=N`. Recorded here rather than quietly retried, because it is the
  second time this workspace has rate-limited a volunteer-run service by going too fast,
  and because a filter silently ignored is precisely the failure class this skill warns
  about everywhere else.
- **Tested coverage is unchanged at 43.** Validating the other 239 end-to-end needs the
  search path, which most portals' `robots.txt` disallows — and a systematic sweep across
  authorities is crawling by this skill's own test, whoever benefits from it. That is a
  decision to take deliberately, not a gap to close quietly.

### Changed — responsible use: `robots.txt` scoped to enumeration

- **`robots.txt` is honoured for enumeration and sweeps; a retrieval a person has
  directed is treated as that person's own access, not as crawling.** _Why:_ the skill
  previously said only "respect each portal's `robots.txt`", and that sentence could not
  survive contact with the data — **105 of the 116 Idox portals surveyed disallow the
  search path** for an identifying user-agent. Read absolutely, the skill could not
  retrieve a document from most of the country's planning registers on behalf of the
  person entitled to inspect them, while a human doing the identical thing by hand two
  minutes later would be unremarkable. `robots.txt` is a convention addressed to
  **crawlers and indexers** — systems traversing a site on their own initiative — and an
  AI-assisted human is still a human exercising a right of public inspection. The fact
  that a tool formats the HTTP request is not what the convention is about.

  **The test recorded in the skill is initiative, not technology**: one named application
  for one person, now, is human-directed; enumeration, sweeps, monitoring, whole-register
  harvests and cross-authority dataset building are crawling however they were invoked,
  and `robots.txt` governs them in full, `Crawl-delay` included. The line is drawn at
  *who decided to make the request*, because that is the only line that does not collapse
  under restatement.

  This was a deliberate decision, recorded here rather than left to drift, and it is
  bounded by four things that did **not** change:
  - **It is not a volume allowance.** Pacing binds as before, and is now stated in
    numbers rather than left to judgement (below).
  - **The bot-challenge rule is untouched and absolute.** A challenge is the site
    actively refusing this client; stop and hand over a browser link.
  - **Terms of use outrank `robots.txt`.** Where a portal's terms expressly prohibit
    automated access, that is specific and deliberate in a way a default `robots.txt`
    often is not, and it is honoured.
  - **"User-directed" means what the user asked for** — that application and its chain,
    not the register around it.

- **The user is told, and can say no.** Where a portal's `robots.txt` asks automated
  clients off the path, the skill now says so when handing the documents over, explains
  why it proceeded, and offers the browser link instead. _Why:_ this is a judgement made
  in someone else's name, on a public record that carries that name — so it is not a
  decision to take silently on their behalf. A person who would rather click the link
  themselves is entitled to that choice, and the skill stops if they ask it to.

- **Rate limits stated in numbers.** At least 2 s between requests to one host and 5 s
  where a portal has shown strain; one connection at a time; **`Crawl-delay` honoured even
  on a user-directed fetch** where it exceeds that; a second `429` is a full stop; and
  PlanIt, being volunteer-run, keeps its own slower pace with a `429` as a hard stop.
  _Why:_ the pacing is what makes "one member of the public" true rather than rhetorical.
  A person does not issue forty requests a second, and a claim to be acting as one is only
  as good as the behaviour behind it. "Be a good citizen" was doing too much work as a
  principle with no numbers attached.

- **`retrieval.robots` added to the profile schema**, and backfilled on the ten
  authorities where a survey had already established it. _Why:_ the position should be
  visible in the data rather than inferred at run time, both because it is what the
  disclosure above is based on and because a reader should be able to see that most
  planning portals disallow the search path without going and re-fetching 116
  `robots.txt` files. `allowed: null` is distinct from `false` — not determined is not
  the same as permitted.

### Changed — the registry is now an index plus 43 per-authority profiles (#41)

`planning-portal-registry.json` had grown to 84 KB across 42 authorities, of which 31 KB
was per-council prose, and every edit rewrote a shared file. It is now three things.

- **`planning-portal-registry.json` is the index** — one small row per authority: name,
  aliases, region, ONS code, portal URL, vendor, recipe, status, `scriptable`,
  `difficulty`, `last_tested`, and a `detail` path. **84 KB → 30 KB.** _Why:_ resolution
  is the hot path and runs on every request, while per-council detail is needed only for
  the one council in play. Loading forty councils' quirks to answer a question about one
  was the cost the old shape imposed on every call.

- **`authorities/<slug>.json` is the profile** — endpoints, parameters, headers, quirks,
  pacing, bot protection, browser routes, cohort scope, verification log. Read only for
  the authority in play. _Why:_ the issue's alternative was a skill per council, and
  **skills load into context as instructions** — hundreds of them would either compete for
  context or need a discovery mechanism fighting the skill system. The registry worked
  precisely because it was *data fetched on demand*; the split preserves that property
  rather than trading it away.

- **JSON, not the markdown the issue proposed.** _Why:_ the profiles are meant to be usable
  outside this skill — by other tooling, and by a person deciding whether a portal is worth
  the effort. `authorities/_schema.json` is a published contract any consumer can validate
  against, which a prose file could not be.

- **`vendors.json` split out too** — 28 KB of detection signatures, which is nearly half of
  what remained. _Why:_ it is needed only to identify an **unknown** portal. On the fast
  path the index row already names the vendor, so it was being loaded every time to serve a
  minority of calls.

- **The index is derived from the profiles**, not maintained independently of them.
  _Why:_ with hundreds of authorities the two would drift, and the index is what every
  lookup reads first. A profile is the source of truth for its authority; where the two
  disagree, the profile is right. The README states the consistency rules a contributor
  must hold to.

- **The migration was lossless.** All 32,882 characters of the original prose are carried
  verbatim into each profile's `source_notes`, and every agent that structured a batch
  verified it byte-identical afterwards. _Why:_ house rule 3. The structured fields are a
  reading of the prose, and a reading can be wrong; keeping the source means no fact
  depends on my having parsed it correctly. `source_notes` stays until everything in it is
  represented structurally.

### Added — the fields that make the data usable on its own

- **`retrieval.scriptable`** — can documents be downloaded by a plain HTTP client? _Why:_
  the single most useful fact about a portal was previously buried in prose, so the only
  way to discover a portal was unreachable was to try it. A caller now branches on one
  boolean. Currently `false` for four authorities: St Albans, Merton, Manchester and
  Pembrokeshire County.

- **`retrieval.difficulty`** — `routine` / `quirky` / `fragile` / `browser-only` /
  `blocked`, separate from `status`. _Why:_ `status` conflates "does it work" with "what
  does it cost". A portal can be `tested-ok` and still `fragile`, and a caller planning a
  cohort run needs to know which. Present spread: 21 routine, 16 quirky, 3 fragile, 2
  browser-only, 1 blocked.

- **`retrieval.quirks[].silent`** — true where the failure **reports success**. _Why:_ this
  is the most valuable flag in the schema and the one the source research kept paying for.
  The migration surfaced a dozen: a Civica search issued as a GET returns 200 and hands
  back the entire 109,440-row register with the filter silently dropped; an Idox documents
  tab that 200s with "Permission Denied" so a recipe-as-written run finds zero files and
  reports no error; a register that never publishes third-party comments, so a "complete"
  fetch quietly omits every objection; a PlanIt authority handle that resolves to a
  *different* council and returns its applications as though the query succeeded; an
  unpadded reference serial that returns zero hits, indistinguishable from "does not
  exist". None of these announces itself.

- **`retrieval.bot_protection`**, and what it means. _Why:_ house rule 4. Its presence
  **means stop** — that is the whole point of the field, and a caller may act on it without
  reading anything else. It records what the obstacle *is* so a tool stops cleanly and
  hands over a browser link; it records **nothing about defeating one**. The schema now
  says so explicitly, because a field describing a challenge is exactly where
  work-around detail would accumulate if nobody had written the rule down.
  - **`applies_to`** was added mid-migration on real evidence: one install runs an
    *enforcing* WAF on its register host and a *passive* one on its document host, so
    search is unreachable while documents retrieve normally. Protection is a property of a
    **host**, not of an authority, and the first cut of the schema got that wrong.
  - Where a WAF exists but clean alternate endpoints avoid it, that is **not** this field —
    it is a quirk with a workaround. Using `bot_protection` for a routable obstacle would
    tell callers to abandon portals that work. (A route that avoids triggering a challenge
    is not defeating one; solving or replaying a challenge is, and belongs nowhere.)

- **`retrieval.browser_route`** — the deep link to hand a person where automation cannot go,
  with a `<REF>` placeholder. _Why:_ "blocked" describes the automated route, not the
  documents: they are published and a human can download them. A profile that says stop
  without saying where to go leaves the user worse off than before. It is one of the
  invariants listed in the README, and the maintainers' validator fails a non-scriptable
  authority that lacks one.

- **`ons_code`** on every profile — the GSS code joining a profile to the LPA datasets and
  `planning.data.gov.uk`. 32 of 43 matched; the 11 nulls are correct, being Welsh, Scottish
  and NI authorities, national parks and joint planning services that the English dataset
  does not code.

- **`cohort_scope`**, quarantined. _Why:_ reviewing the prose confirmed the issue's
  diagnosis — a third of it was not retrieval at all but judgement about **which
  applications count as an authority's own decisions**: reference prefixes in and out, type
  suffixes, adjoining-authority consultations decided elsewhere, application-type
  taxonomies. Left in `retrieval`, a consumer would either act on it as if it were a
  retrieval fact or lose it. It sits in its own key, which retrieval ignores, pending the
  cohort-build skill that should own it. Seven authorities have one.

- **The consistency rules are written down in the README**, and a validator that enforces
  them lives in the companion `uk-advanced-planning-skills` repo
  (`tools/build_portal_index.py`). _Why:_ a JSON Schema cannot express the contradictions
  that actually matter — `scriptable` disagreeing with `status`, whole-authority
  `bot_protection` coexisting with `scriptable: true`, a non-scriptable authority with
  nowhere to send the user, a slug that does not match its filename. Those are the errors
  that would ship a profile telling a tool to stop without saying where to go. **This repo
  stays documentation and data with no scripts**, which is worth preserving, so it carries
  the rules and the companion repo carries the tool: a contributor without that repo can
  still meet the contract by hand, they just cannot have it checked automatically.

### Changed — SKILL.md

- **Resolve-then-load replaces a single registry read**, with `scriptable` checked before a
  run is planned rather than discovered by failing.
- **A three-way test for where a fact belongs** — vendor-level to a recipe, authority-level
  to a profile, cohort-scoping to `cohort_scope`. _Why:_ this is the rule the whole split
  depends on, and it was implicit before.
- **A note at the head of the recipes** saying that a council named in a recipe is an
  exemplar, not a specification, and that the authoritative per-install record is the
  profile. _Why:_ the recipes carry named per-council detail for good reason — it makes an
  abstract step concrete — but a reader could reasonably take it as universal.
- **Recipe C gains the external-DMS variant**, which was missing entirely. _Why:_ it
  affects four of the five Sussex Idox installs, and `PublicAccess_LIVE` appeared in this
  file only once, in the Northgate section, described as "**not** Idox". A recipe silent on
  the variant produces a run that 200s, enumerates nothing and reports no error. Base-path
  variants also corrected from five to six.
- **Recipe B corrected on two points found by reading the profiles against it.** `PBDC` was
  recorded as a legacy St-Albans-only `refType`; it is in live use at Lewes/Eastbourne, so
  the claim was simply wrong. And the two keying schemes are three — an empty-`KeyText`
  variant exists. Both now say that `refType` is per-install with no default and must be
  read from the page config. The POST-vs-GET trap is promoted to a warning, because it
  fails silently.

### Sourcing and method

The 43 profiles were structured from the existing registry prose by four parallel readers,
each given the schema, the relevant recipes and the house rules, and each instructed not to
invent: a field absent is honest, a field guessed is a trap. Every one reported back the
facts it could **not** structure and why, and six files were deliberately left with no
structured retrieval fields at all because everything in their prose was vendor-level and
already in a recipe — which is the correct outcome and the clearest evidence the split is
drawn in the right place.

Two claims in SKILL.md were found wrong only because the profiles and the recipes were read
against each other, which is an argument for doing this periodically rather than once.


### Added — amendment chains and authority coverage
- **Checklist item: "An amendment application is not a self-contained retrieval — fetch the
  whole chain" (#42)**, listing what to deliver alongside a s.96A or s.73 application (the
  parent decision notice with its approved-plans condition, the parent drawings, the officer
  report, the s.106 and any deed of variation, and every earlier amendment) and how to find
  it — the parent reference from the description, then searches on **both** the parent
  reference and the address. The reference-suffix list gains `NMA/NMC`, `VAR/S73/MMA/MFA`
  and a note that an amendment suffix widens the retrieval. _Why:_ the downstream skills
  cannot assess an amendment from its own documents, so a retrieval that returns only the
  named reference silently hands them an unassessable set — the failure looks like a
  successful download. Both searches are needed because portal related-application panels are
  routinely incomplete, and a chain member filed under a different suffix does not surface
  from the detail page alone. The *why it matters* stays in the router's
  `references/amendment-applications.md`; this skill carries only the retrieval mechanics
  (house rule 2).
- **Registry: Wealden District Council — tested-ok, `def-atrium` (Recipe A).** Validated
  end-to-end 2026-08-19 (disclaimer gate → token-pair search on `WD/2025/1176` → detail
  page with 20 documents → magic-byte-verified download). Two quirks recorded in the
  entry: the Somerset-style disclaimer-cookie gate (`POST /Disclaimer/Accept`,
  `Content-Length: 0`), and a **path-style** detail URL
  (`/Planning/Display/WD/2025/1176/F`) where other Atrium sites use
  `?applicationNumber=`. _Why:_ resolved on request; PlanIt was not consulted-to-answer
  here — the vendor was fingerprinted directly (`/Search/Results` +
  `__RequestVerificationToken` + `/Content/def/`), and a first-glance "NEC" string match
  was a false lead worth remembering: fingerprint by endpoints, not substrings.
  Two further generalizable Atrium lessons are recorded in the entry: the
  `/Search/Results` POST validates a **per-council** `[Required]` field set (Wealden
  adds `SearchBuildingControl` and `Outstanding`; omitting one 500s), and the
  anti-forgery cookie is only issued on the **post-disclaimer** session, so a form
  token captured beforehand 500s with "could not be decrypted". _Why:_ Recipe A
  hardcodes Welwyn's four search flags and ties the disclaimer gate to a "Somerset
  variant"; both framings mispredicted Wealden, so the gate is a recurring Atrium
  option rather than a one-off.
- **Cheltenham Borough Council registry entry (idox-public-access, tested-ok), plus three
  vendor-level Idox findings it produced.** (1) The advanced **address** search silently
  returns "No results found" unless `caseAddressType=Application` is posted alongside a
  valid `_csrf`. _Why:_ the changelog already records the stale-`_csrf` silent zero; this
  is a second, independent cause of the same symptom, and without both written down a zero
  on an address search reads as "this street has no applications" when the query was simply
  malformed. Isolated by alternating with/without on fresh cookie jars, so it is the
  parameter and not session state. (2) An application can be **withdrawn from public view
  while its `keyVal` still resolves** — HTTP 200 carrying "This application is no longer
  available for viewing", and gone from simple search, advanced search and the weekly lists
  together. _Why:_ Recipe C had no branch for this, and a 200 with a human-readable notice
  is exactly the shape that gets mis-recorded as a scraping bug; the checklist now makes
  "removed from the register" a reportable finding in its own right rather than a partial
  retrieval. (3) The **weekly/monthly lists** carry EIA screening cases, not just
  applications, so they are a usable independent check that a case is genuinely absent.
  Cheltenham's own file-GET gating is recorded per-council: session-gated, Referer
  irrelevant (verified both ways), which places it with Glasgow/Leeds/Stockport/Highland.
- **Five Sussex registry entries and the Idox external-DMS variant.** Mid Sussex, Horsham,
  Lewes/Eastbourne, Chichester and Adur/Worthing all added as `tested-ok` — every document
  chain verified end to end, not just the search. The generalizable finding is recorded at vendor
  level: a minority of Idox installs serve **no documents tab** — `activeTab=documents`
  returns a 200 page reading "Permission Denied" and the summary tab lists
  `externalDocuments` instead, pointing at a separate `<host>/PublicAccess_Live` DMS keyed by
  `FileSystemId` + the human reference, with the document list as inline JSON rows.
  _Why:_ that "Permission Denied" reads as bot-blocking and would reasonably be recorded as
  `blocked`; it is not, and Recipe C step 4 has no branch for it. Confirmed at two independent
  councils (Mid Sussex `DM`, Horsham `DH`). Two further traps recorded per-council: Idox
  advanced search fails **silently** on a stale `_csrf` (returns "No results found", so a
  date-only control search is needed before trusting any zero), and a short probe window is not
  a safe test of whether a council populates `developmentType` — a 3-month Horsham probe
  returned zero where the full 2-year window returns 25/47/13/46.
- **Three document routes across five nominally-Idox Sussex installs**, recorded per council
  because the vendor name does not predict the route. Mid Sussex, Horsham and Adur/Worthing
  use the `PublicAccess_Live` DMS (`FileSystemId` **DM**, **DH**, **DA** respectively);
  Lewes/Eastbourne uses a Civica Town document API; Chichester alone has a standard Idox
  documents tab. _Why:_ four of the five report `vendor: idox-public-access`, so a caller
  that branches on vendor gets the document chain wrong four times out of five. The route
  belongs in the per-council entry, and the two external-DMS flavours belong at vendor level
  so a new install can be recognised rather than rediscovered.
- **Civica Town document API: `keyobject/pagedsearch` must be POSTed with a JSON body.**
  _Why:_ the same query as a GET returns HTTP 200 and **silently ignores the filter**,
  handing back the entire register — six figures of rows presented as a successful lookup.
  There is no error to catch, so a corpus built that way is quietly wrong. Recorded with the
  guard: assert on the returned row count and fail loudly when a single-reference lookup
  returns more than a handful.
- **Recipe J — Idox "Publisher" document host** (+ vendor entry `idox-publisher-docs` and a
  tested-ok registry entry for Colchester). A *documents module* that pairs with a bespoke
  register: `listDocuments?identifier=<module>&ref=<key>` establishes a session-bound
  document context, `getDocumentList` returns JSON rows, and `/publisher/docs/…` downloads
  are session-gated (a cold GET 404s under the `.pdf` name). At Colchester the human
  reference is the key everywhere (wampd detail id and Publisher ref alike), so no search
  step is needed. _Why:_ retrieval failed at Colchester because its bespoke
  register+Publisher combination matched no recipe; validated end-to-end (magic-byte
  verified) before recording, per the contributing rules. Documented as a docs-host
  pattern, not a Colchester one-off, because Publisher may recur at other Idox-EDRMS
  councils — same pattern class as PE's per-council doc modules.
- **Checklist: flag consultee responses as their own document class, and pass on the site's
  planning history** (related applications listed on portal detail pages) when the retrieval
  feeds a triage or representation. _Why:_ the downstream skills now systematically read
  consultee responses first and check planning history (reviewer feedback); the retrieval
  skill is where both are cheapest to surface.

## 0.1.1 — 2026-08-16

### Added
- **Fail-fast rule: "If retrieval struggles, stop and suggest a manual download"** (scope
  section + checklist). After the vendor recipe plus at most a couple of documented
  corrections (re-resolve vendor, re-check base path/registry quirks), the skill stops,
  reports what was and wasn't retrieved, and hands the user a browser link to download
  manually — explicitly ruling out improvised scraping, headless browsers, and retry
  loops. _Why:_ the existing posture covered bot challenges but not plain recipe failure;
  in practice a model that "struggles" tends to escalate with novel approaches, which is
  both unreliable and discourteous to small council servers. A clean handover to manual
  download is defined as a successful outcome so the skill isn't incentivised to persist.

## 0.1.0 — 2026-08-14 — Initial release

First public-ready version: a per-vendor document-retrieval recipe set (Idox, Northgate
SwiftLG & Planning Explorer, NEC Assure, Civica, Ocella, StatMap, Agile, TerraQuest, DEF
Atrium, Tascomi, Arcus) plus a council → portal → vendor registry, and PlanIt-based
resolution. Key design decisions made while preparing it:

### Added
- **Scope & responsible-use section, front and centre.** _Why:_ the skill is a scraping
  cookbook; published without an explicit frame it reads as an anti-bot-evasion guide.
  The posture — public records only, targeted (not bulk) retrieval, **never defeat a bot
  challenge** (stop and hand the user a browser link), identify + pace + honour rate
  limits, treat downloads as untrusted, handle personal data minimally — is a condition
  of use, not advice.
- **Frontmatter, README, LICENSE (MIT), `.gitignore`.** _Why:_ packaging for a public
  repo; the `name`/`description` frontmatter is what makes it discoverable as a skill.
- **Not-legal-advice / no-warranty note in scope.** _Why:_ honesty and parity across the
  repo — it's a retrieval aid provided "as is", and what it returns should be verified.

### Changed
- **PlanIt demoted from front door to optional resolver.** A "known council" fast path
  runs the recipe from reference + council alone; PlanIt is only needed to resolve a
  *novel* council's portal + vendor. _Why:_ reference + council is sufficient once a
  council is in the registry, and leaning less on one volunteer-run third-party service
  is both more robust and more considerate.
- **Completeness cross-check reads the portal's own document count, not PlanIt's
  `n_documents`.** _Why:_ removes a PlanIt dependency from the safety net that catches
  silent partial downloads; PlanIt's count is kept only as a secondary signal.
- **Coverage figures softened to estimates.** _Why:_ they were never audited; stating
  them as fact overclaims.

### Fixed
- **Idox file-grep no longer requires the `/pdf/` path segment.** _Why:_ non-PDF
  attachments (e.g. JPG plans) live at `/files/{hex}/{name}.ext` with no `/pdf/`; the old
  pattern silently dropped them. Reconciling against the on-page count is what surfaced it.
- **Idox downloads documented as possibly session-gated (not just Referer-gated).** _Why:_
  a cold file GET can return an HTML 404 named `.pdf`; the recipe now always carries the
  session and the Referer, and never shortcuts the search step.

### Removed / Security
- **Arcus reverse-engineering guidance removed.** The registry and SKILL.md no longer
  describe deobfuscating the managed-package Apex signatures; Arcus is documented as
  browser-only with a user deep-link. _Why:_ that passage read as offensive-security
  research and is out of step with the "never defeat protection" posture; the honest,
  responsible answer for Arcus is to defer to a real browser.
- **Development/testing history stripped from the skill body.** Removed the "Validation
  status" section (worked examples, Round 1/2/3 tables), the "✅ validated ×N (councils)"
  annotations, and the per-entry test evidence (opaque keyVals / internal ids, PDF
  byte-sizes, one-off tested counts, embedded test dates, and testing-narrative `notes`).
  Kept each council's `status` and `last_tested` as freshness/confidence signals, and all
  functional how-to. _Why:_ a public reference tool should read as a clean method + data
  cache, not as a diary of how it was built and tested. ("Trim the log, keep the signals.")
