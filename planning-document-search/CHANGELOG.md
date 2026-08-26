# Changelog — planning-document-search

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines are the point: they record the rationale so a future
editor understands the intent.

## Unreleased

### Added
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
