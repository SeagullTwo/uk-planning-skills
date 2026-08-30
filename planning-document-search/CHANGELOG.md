# Changelog — planning-document-search

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines are the point: they record the rationale so a future
editor understands the intent.

## Unreleased

### Added
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
