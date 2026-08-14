---
name: planning-document-search
description: >-
  Retrieve the documents attached to a UK planning application from the local
  council's public online planning portal, given the application reference and
  the council name. Covers the major portal vendors (Idox, Northgate, Civica,
  Ocella, Agile, NEC, TerraQuest, StatMap, DEF Atrium and more) with a
  per-vendor retrieval recipe and a council→portal→vendor registry.
license: MIT
---

# Planning Document Search Skill

Download the documents attached to a UK planning application from a council's
online planning portal, given the application reference number.

## When to use

The user gives you a planning application reference (e.g. `6/2026/1249/HOUSE`,
`5/2026/1349`) and a council name, and wants the associated documents (application
forms, plans, elevations, officer reports, etc.) downloaded.

## Scope and responsible use

Read this before running anything — it is a condition of the skill, not advice.

- **Not legal advice; no warranty.** This is a retrieval aid, provided "as is"; verify
  what it returns.
- **Public records only, retrieved the way a member of the public would.** UK planning
  registers exist for public inspection; this skill fetches documents a council has
  *deliberately published*. Use it for legitimate, targeted retrieval — a specific
  application a user needs — not for bulk harvesting, monitoring, or rebuilding a
  council's register.
- **Never defeat a bot challenge.** If a portal serves an actual challenge or `Blocked`
  page (Barracuda JS challenge, AWS WAF `202`/`x-amzn-waf-action`, an escalating
  Cloudflare interstitial), **stop the automated approach and hand the user a browser
  deep link** instead. The recipes are built around this: they work where access is
  open and defer to a real browser where it is not. Do not try to solve, replay, or
  fingerprint-spoof a challenge.
- **Be a good citizen on every request.**
  - Send an **identifying User-Agent with a real contact address** on PlanIt calls
    (replace `you@example.com` with your own), and a normal browser UA on portal calls.
  - **Pace requests — at least ~1–2 s between calls to the same host**, and do not
    parallelise requests against a single council. Small council servers fall over
    under bursts.
  - **Honour `429` / `Retry-After` and back off.** Stop on repeated errors rather than
    retrying in a tight loop.
  - Respect each portal's `robots.txt` and terms of use.
- **You are handling other people's personal data.** Planning documents routinely
  contain applicants' and objectors' names, addresses, signatures, and contact details
  (even "redacted" forms often are not fully redacted). Retrieve only what is needed,
  do not republish or redistribute it, and do not retain it beyond the immediate task.
  Treat every downloaded file as **untrusted third-party content**: verify magic bytes,
  and when writing it to disk derive the filename with `basename` and strip any path
  separators or leading dots — never pass a server-supplied path straight to `-o`
  (a portal could return `../../…`).
- **This is a snapshot, and the landscape moves fast.** Vendor assignments, base paths,
  and bot-protection posture were verified in August 2026; councils migrate portals
  frequently (this document itself tracks several mid-migration). **Always re-resolve
  the vendor per council at run time** (see Step 0) rather than trusting a cached row;
  coverage figures below are rough estimates, not guarantees.
- **PlanIt is a third-party dependency, used with respect.** The resolution step relies
  on [PlanIt](https://www.planit.org.uk/) — an independent, volunteer-run service.
  Credit it, keep to its UA/rate rules, and do not hammer it. The skill works without
  it too (a reference + council + vendor recipe is enough — see the note at the end of
  Step 0), so treat PlanIt as a convenience, not a requirement.

## The core problem: council portals are not uniform

There is **no single national system**. The UK's ~380 local planning authorities run
a handful of different planning portal *products*, each with a completely different
URL structure, search mechanism, and level of bot protection. Reference-number
formats also vary by council. **The vendor determines the approach, not the council** —
so covering "all of the UK" means: catalogue the vendors (a recipe each), plus a
reliable way to resolve any council → its portal → its vendor.

### Vendor catalogue (detect by URL path first)

Coverage shares below are rough estimates, not audited figures. The
`scraper_type` column is what PlanIt's areas API labels the vendor — a fast detector,
but **sometimes stale or wrong** (Birmingham still says `PlanningExplorer` post-migration;
Manchester is mislabelled `Idox`), so confirm against the markup.

| Vendor | Detect (markup / host) | PlanIt `scraper_type` | Recipe | Bot protection | Coverage |
|---|---|---|---|---|---|
| **Idox Public Access** | `search.do`/`*.do` Struts + `keyVal` + `/files/{hex}/pdf/`. Base path **varies** — detect by endpoints, not path | `Idox` | **C** | Usually none; some Cloudflare (UA); Barracuda cookies sometimes present but *passive* | Dominant (~60%+) |
| **Northgate SwiftLG** | `/swiftlg/apas/run/`; `*.MAINBODY.WPACIS.1` fields | `Swift`/`Northgate` | **D1** | None observed | **Dying** — presume migrated (see note) |
| **Northgate Planning Explorer** | `/Northgate/PlanningExplorer/`; `.aspx` + `__VIEWSTATE` | `PlanningExplorer` | **D2** | Cloudflare (passive); some origin-WAF quirks | Minority, also migrating |
| **NEC Assure ES** | `/NECSWS/ES/Presentation/`; `AssureLogo`; MVC+AJAX | may stalely say `PlanningExplorer` | **H** | None enforcing (F5 LB passive) | Growing (ex-Northgate) |
| **Civica Portal360** | `civica.loader.js`; `Handler.ashx`; `keyobjectsearchandview` | `CivicaJson` | **B** | Per-council — mostly passive/absent; St Albans enforces Barracuda | Minority |
| **Ocella** | `/OcellaWeb/planningSearch` | `Ocella` | **E** | None enforced (passive fingerprint at Arun) | Niche |
| **StatMap horizoNext** ("Mirage") | `*-publicportal.statmap.co.uk`; `/horizonext` SPA; JSON API `/horizoNext/api/` | `Custom` | **F** | None — open JSON API | Small (ex-SwiftLG) |
| **Agile Applications** | `planning.agileapplications.co.uk/<slug>/`; "Citizen Portal Planning"; `*.sunagile.com` CSP | `Agile` | **G** | None — open JSON API (3 headers) | Small, growing (ex-SwiftLG) |
| **TerraQuest PP2** | Next.js + `/__ENV.js` w/ `*.tqinfra.co.uk` API. NI: `planningregister.planningsystemni.gov.uk` | (indexed) | **I** | None — open JSON API (1 header) | All 11 NI authorities |
| **Arcus** (Salesforce) | `*.my.site.com`/`*.force.com`/council CNAME; Lightning SPA; `Server: sfdcedge` | often mislabelled | — browser-only* | Guest Aura curl-able; blocked on unknown apex sigs | Small, growing |
| **DEF Atrium** | `/Search/Results` POST + `__RequestVerificationToken`; `/Planning/Display?applicationNumber=`; `/Document/Download?module=PLA&…`; `/Content/def/` CSS | `Atrium` or `Custom` | **A** | None; Somerset adds a disclaimer-cookie gate | Small (incl. county registers) |
| **Tascomi RSH** (Idox group) | `index.html?fa=<action>` dispatcher; "Regulatory Services Hub" title; `AWSCaptcha.js` | `Tascomi` | — browser-only | **Enforcing AWS WAF challenge** (202 + `x-amzn-waf-action`) | Small, growing (ex-PE) |
| **Custom / bespoke** | none of the above | `Custom` | treat A as a template | Varies | Long tail |

\* Arcus public registers have no anonymous API surface — treat as browser-only and hand
the user a deep link. See the Arcus section.

Detection cheat-sheet for an unknown portal: `.do` actions + `keyVal` = Idox (any base
path); `/swiftlg/apas/run/` = SwiftLG; `/Northgate/PlanningExplorer/` = Northgate PE;
`/NECSWS/ES/Presentation/` = NEC Assure; `/OcellaWeb/` = Ocella;
`*-publicportal.statmap.co.uk` = StatMap; `planning.agileapplications.co.uk/<slug>` /
"Citizen Portal Planning" = Agile; Next.js + `/__ENV.js` on `*.tqinfra.co.uk` =
TerraQuest PP2; Salesforce `*.force.com`/`my.site.com`/`Server: sfdcedge` = Arcus;
`civica.loader.js` = Civica; `/Search/Results` + `__RequestVerificationToken` +
`/Document/Download?module=PLA` = DEF Atrium; `index.html?fa=` dispatcher + "Regulatory
Services Hub" = Tascomi (browser-only); `/CMWebDrawer/` = HP TRIM docs host (append
`&format=json`); `__VIEWSTATE` with none of the above = bespoke WebForms.
**When the portal is a JS/SPA shell, fetch its runtime-config file** (`/__ENV.js`,
`config.js`, or the app bundle) — for the open-API vendors (StatMap, Agile, TerraQuest)
that file hands you the real API host, and often a tenant id/header you'll need.

> **⚠ SwiftLG is being retired fast.** Of four historic SwiftLG councils tested in
> Aug 2026, only Warwickshire still ran it — Mole Valley → StatMap, and Dudley,
> Snowdonia, Pembrokeshire → Agile (old hosts dead or DNS gone). **Presume any
> historic SwiftLG council has migrated until PlanIt's `planning_url` proves
> otherwise.** The successors are open JSON APIs (Recipes F/G), so migration usually
> makes retrieval *easier*, not harder.

## General procedure

**Step 0 — get the portal URL + vendor.** Everything the recipes need is the *portal
URL* and *vendor* for the user's council; the *reference* comes from the user. There are
two paths, and the first one needs no external service at all.

### Fast path — known council: you don't need PlanIt

**If the user gives you a planning reference and a council, and that council is in
[`planning-portal-registry.json`](planning-portal-registry.json) with `status:
tested-ok`, you are done resolving.** The registry row already gives you the portal URL,
the vendor, and the per-council quirks. Go straight to the vendor's recipe and run it
from the user's reference — search the reference → detail/keyVal → documents → download.
**PlanIt is not in the loop for this case.** Reference + council + this skill (registry +
recipe) is sufficient to retrieve the documents; do not call PlanIt just out of habit.

(PlanIt's only remaining offer here would be the `n_documents` completeness figure — and
the recipes get that from the portal's own documents page instead; see the completeness
cross-check in the checklist. Skip PlanIt entirely on the fast path.)

### Resolution path — unknown/novel council: use PlanIt (or a council-site scrape)

If the council is **not** in the registry (or its recorded portal looks stale — councils
migrate), you need to resolve council → portal URL + vendor. Use the **PlanIt API** — the
live national LPA → portal directory — instead of hand-hunting the council website:

```bash
# Council -> portal base URL + vendor family (planning_url, scraper_type):
curl -s "https://www.planit.org.uk/api/areas/json?area_type=planning&auths=<council>" \
  -A "planning-doc-search (contact: you@example.com)"

# Reference -> the council application URL (the `url` field is the portal deep link):
curl -s "https://www.planit.org.uk/api/applics/json?id_match=<ref>" \
  -A "planning-doc-search (contact: you@example.com)"
```

```bash
# Need a fresh/recent application for an authority (e.g. to test with)? —
curl -s "https://www.planit.org.uk/api/applics/json?auth=<council>&pg_sz=3&recent=60" \
  -A "planning-doc-search (contact: you@example.com)"
```

PlanIt rules: **always send an identifying User-Agent** (403 without one) and
**back off on 429** (honour `Retry-After`). PlanIt gives you the council application
URL + vendor but **not** document file links — follow the URL into the portal and
apply the vendor recipe. (`planning.data.gov.uk` is spatial/policy constraints only —
Article 4, conservation areas, listed buildings, local plans — **not** a document
source.)

Two PlanIt caveats: the **areas record can mislead** — Camden's
`planning_url` points at a Socrata open-data dataset, not the portal; the *applics*
records' `other_fields` (`docs_url`, `url`, `comment_url`) are the real portal
pointers, so when the areas record looks odd, pull a recent applic and trust its URLs.
And **merged authorities fragment**: post-2023 Somerset still files current district
applications on the legacy district portals (Mendip/South Somerset Idox) while running
a consolidated DEF Atrium register for county matters — PlanIt lists legacy districts
as separate areas, and the per-application `url`/`docs_url` is the router that tells
you which portal a given reference lives on.

PlanIt shortcuts: applics records often carry
**`other_fields.docs_url`** — the fully-formed Idox documents-tab URL *including the
keyVal* — plus `n_documents` (a free completeness check against your scraped link
count). The `url` field frequently embeds the portal's opaque record id too
(Idox `keyVal=`, Ocella `planningDetails?reference=`, StatMap trailing internal id).
When present you can skip a recipe's search steps and jump straight to the documents
step — but for session-gated vendors (Idox) still hit the search page once first to
get a session cookie. Derive a portal's base path from the areas `planning_url` by
stripping the trailing `/search.do?...` page — do **not** assume `/online-applications/`.

If PlanIt lacks the council, fall back to the council website:

```bash
curl -s -L "https://www.<council>.gov.uk/view-and-track-planning-applications" -A "Mozilla/5.0" \
  | grep -oiE 'href="http[^"]*"' | grep -iE 'planning|search|idox|publicaccess|civica|swiftlg|ocella' | sort -u
```

**PlanIt is a convenience, not a requirement.** All the vendor recipes need is the
**portal URL + vendor**; the reference itself comes from the user. What PlanIt actually
buys you is (a) resolving council → portal URL + vendor without hand-hunting the council
site, and (b) shortcuts — `docs_url`/`keyVal`/internal ids that skip a recipe's search
step, and `n_documents` as a free completeness check. If you already know a council's
portal and vendor (e.g. it is in the registry with `status: tested-ok`), you can run the
recipe directly from the user's reference and **use PlanIt only for the `n_documents`
cross-check** — or skip it entirely. The registry is the offline substitute for (a); the
recipe's own search step is the substitute for (b).

**Steps 1–5 — identify the vendor** (table above) → **search** the reference →
**extract the detail-page / keyVal** → **enumerate document links** → **download**
each with the same session. Then **deliver** the files and **record the result in the
registry** (`status`, `last_tested`, specializations).

---

## Recipe A — DEF Software "Atrium"

Originally documented as "custom ASP.NET" from Welwyn Hatfield; **identified as the DEF
Software Atrium product** — Somerset's consolidated register shares every form and
endpoint (detect: `/Search/Results` POST,
`__RequestVerificationToken`, `/Planning/Display?applicationNumber=`,
`/Document/Download?module=PLA&recordNumber=…&planId=…`, `/Content/def/` CSS,
`def.co.uk` privacy link; PlanIt `scraper_type: Atrium` or `Custom`).

The search form is a server-rendered POST protected by an ASP.NET anti-forgery scheme:
you need **two matching tokens** — the `__RequestVerificationToken` cookie *and* the
hidden form-field token from the page HTML. They are validated as a pair, so steps 1–2
must run against the same cookie jar.

With an exact application number, the search redirects straight to the detail page
(Welwyn) or links to `/Planning/Display?applicationNumber=<enc-ref>` (Somerset — the
human reference is the key; no opaque internal id needed).

**Somerset variant quirks**: a **disclaimer gate** precedes everything — POST
`/Disclaimer/Accept?returnUrl=<path>` with an **explicit `Content-Length: 0` header**
(the front-end 411s a plain empty POST) → sets an `AcceptedDisclaimer` cookie (~1h
expiry) that document downloads require (a cold download 302s back to the disclaimer).
Search-scope flags differ (`SearchPlanning`/`SearchAppeals` + `AdvancedSearch=True`),
and `DateReceivedFrom/To` (`dd/mm/yyyy`) date sweeps work for discovering references.

```bash
# 1. Load homepage: capture session cookie (-c) and the hidden form token
TOKEN=$(curl -s -c whc.txt "https://planning.welhat.gov.uk/" -A "Mozilla/5.0" \
  | grep -o '__RequestVerificationToken" type="hidden" value="[^"]*' \
  | sed 's/.*value="//')

# 2. POST the search — token + app number + the four search-scope flags
curl -s -b whc.txt -c whc.txt -A "Mozilla/5.0" -L \
  "https://planning.welhat.gov.uk/Search/Results" \
  --data-urlencode "__RequestVerificationToken=$TOKEN" \
  --data-urlencode "SearchPlanning=True" \
  --data-urlencode "SearchAppeals=True" \
  --data-urlencode "SearchEnforcement=True" \
  --data-urlencode "SearchTreePreservationOrders=True" \
  --data-urlencode "ApplicationNumber=6/2026/1249/HOUSE" \
  --data-urlencode "Address=" \
  -o results.html

# 3. Extract document download links (un-escape &amp;)
grep -oE 'href="/Document/Download[^"]*"' results.html \
  | sed 's/href="//;s/"$//;s/&amp;/\&/g' | sort -u

# 4. Download each doc, reusing the session cookie. Links differ only in
#    planId / imageId / isPlan / fileName; recordNumber is the internal app id.
curl -s -b whc.txt -A "Mozilla/5.0" -o "ApplicationFormRedacted.pdf" \
  "https://planning.welhat.gov.uk/Document/Download?module=PLA&recordNumber=111526&planId=2173461&imageId=2&isPlan=False&fileName=ApplicationFormRedacted.pdf"
```

Notes:
- Always send a real browser `User-Agent` (`-A "Mozilla/5.0 …"`). Some council
  portals reject curl's default UA.
- The detail page also carries each document's description and created date next to
  the link — grep those out to label the files for the user.
- Verify downloads are real PDFs (`file *.pdf`) — a bot block or session timeout
  returns an HTML error page with a `.pdf` name.

---

## Recipe B — Civica Portal360 (browser-only only where an enforcing Barracuda is present)

**Barracuda is a per-council property, not a Civica one.** Of the four CivicaJson sites
in PlanIt, Ashfield has no WAF, Waverley has passive Imperva Incapsula, and only
St Albans runs *enforcing* Barracuda. So on most Civica sites the JSON API is fully
curl-able — the browser fallback below is needed only when you actually get a
`Blocked` page.

### B (curl) — the JSON API chain

Everything is a JSON POST to the Civica `Handler.ashx` API. Two things are per-site;
**read them from the search page's inline config**, don't hardcode:
- `Civica.APIUrl=` → the API base path (`/civica/Resource/Civica/Handler.ashx/` at
  Ashfield; `/w2webparts/Resource/Civica/Handler.ashx/` at Waverley/St Albans; an
  absolute cross-host URL at Eastbourne).
- `Civica.PortalSettings.PlanningApplicationRefType` → the `refType` (`GFPlanning` at
  Ashfield/Waverley; the old `PBDC` was St-Albans-specific).

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
API="https://planning.ashfield.gov.uk/civica/Resource/Civica/Handler.ashx"   # from Civica.APIUrl
RT="GFPlanning"                                                              # from PlanningApplicationRefType
REF="V/2026/0515"

# 1. Search (JSON POST — NOT the old keyText GET). -> KeyObjects[].KeyNumber
curl -s -b civ.txt -c civ.txt -A "$UA" -H "Content-Type: application/json" \
  "$API/keyobject/pagedsearch" \
  -d "{\"refType\":\"$RT\",\"fromRow\":1,\"toRow\":10,\"searchFields\":{\"FullTextSearch\":\"$REF\"}}"

# 2. Document list for that KeyNumber (KeyText is the constant "Subject")
curl -s -b civ.txt -c civ.txt -A "$UA" -H "Content-Type: application/json" \
  "$API/doc/list" \
  -d "{\"KeyNumb\":244982,\"KeyText\":\"Subject\",\"RefType\":\"$RT\",\"ProcessNo\":\"\",\"PageSize\":50}"

# 3. Download one document by DocNo -> application/pdf
curl -s -b civ.txt -A "$UA" -o "SiteLocationPlan.pdf" \
  "$API/doc/pagestream?DocNo=19338083&pdf=true&filename=SiteLocationPlan.pdf"
```

Notes: a `500` with a JSON error body (LogRef) = wrong params, **not** a block —
distinct from a Barracuda `Blocked` HTML page. Empty `searchFields` returns zero rows
by design. Doc endpoints are defined in `civica.documents.js` under
`<base>presentation/bundle/` (not `civica.common.js`). PlanIt's applics
`url` carries `?RefType=&KeyNo=` for Civica sites — skip step 1.

More Civica facts:
- **Zip-all** — `GET <base>doc/list/zipstream?KeyNumb=<n>&KeyText=<kt>&RefType=<rt>&ProcessNo=`
  returns one zip of the entire document set. Prefer it for whole-application pulls;
  verify `PK` magic + entry count.
- **Two keying schemes**: number-keyed (Ashfield/Waverley — `KeyNumb=<int>` from
  pagedsearch, `KeyText:"Subject"`) vs **reference-keyed** (Great Yarmouth —
  `KeyNumb:0`, `KeyText:"<planning ref>"`, `RefType:"PLANNINGCASE"`). The viewer
  deep-link fragment tells you which: `#VIEW?…&KeyNo=<n>` vs `…&KeyText=<ref>`.
- **Silent search trap**: `FullTextSearch` can be ignored on some installs (Great
  Yarmouth returned the whole 30,992-row register) — always check `TotalRows` ==
  expected; the honoured field there was `searchFields:{"KeyNo":"<ref>"}`.
- `doc/list` rows may lack `FileName` (Waverley) — label from `DocDesc` +
  `FileExtension`; the `filename=` param on pagestream is client-chosen anyway.
- pagestream Content-Type can be `application/PDF` (uppercase) — match
  case-insensitively. Native `.docx` sources are converted to real PDF by `pdf=true`.
- Non-standard **ports** occur (Waverley `:4443`) — take host:port verbatim from
  PlanIt's `planning_url`.

### B (browser) — only when Barracuda actually enforces (St Albans)

`planningapplications.stalbans.gov.uk`. Here the page shell renders but every XHR/API
and document call returns a `Blocked` page. The server sends a
~67 KB obfuscated JavaScript fingerprinting challenge (loaded via a
`<script src="/bnith__…">` tag) that a **real browser must execute**: it computes a
device fingerprint, posts it back, and only then is a clearance cookie issued that
unlocks the API. Consequences:

- The top-level HTML page loads for curl (Barracuda allows the document navigation
  so it can serve the challenge), **but every XHR/API and document call returns a
  `Blocked` page**. No clearance cookie is ever set for a non-JS client.
- Reusing cookies from the HTML fetch does **not** help — there is no valid cookie
  to reuse until the JS challenge is solved.
- A headless browser (Playwright/Puppeteer) *might* work, but Barracuda is
  specifically designed to detect and block headless Chromium, so success is
  unlikely and not worth a heavy install as a first move.

### How to get past it: use a real browser session

1. **Claude in Chrome extension** (preferred if available) — drives the user's real
   Chrome, which passes the challenge invisibly because it's a genuine browser
   session. Requires the extension installed and signed in to the same account.
   (In this session it was "not connected", which blocked the automated route.)

2. **In-app Browser pane** — was **blocked by environment policy** for this domain,
   so unavailable here. Worth trying for other councils.

3. **Hand the user a one-click deep link** — the most reliable fallback. The
   full-text search deep link opens the application directly in the user's own
   browser:

   ```
   https://planningapplications.stalbans.gov.uk/planning/search-applications?civica.query.FullTextSearch=5%2F2026%2F1349
   ```

   (URL-encode the reference: `/` → `%2F`.) Civica deep-links to a specific record
   use the fragment form `#VIEW?RefType=PBDC&KeyNo=<internal-id>`, where `KeyNo` is
   the internal record id exposed in search-result links.

### Useful Civica internals (for when you *do* have a browser session)

- Config globals in the page: `Civica.APIUrl="/w2webparts/Resource/Civica/Handler.ashx/"`,
  `Civica.DocumentViewerUrl="/my-requests/document-viewer"`.
- Search service: `API.KeyObject` → `keyobject/search` and `keyobject/pagedsearch`.
- The planning search/view widget is `keyobjectsearchandview` with `RefType=PBDC`;
  its display fields include `ref_no`, `application_address`, `app_status`,
  `decision_date`, etc.
- JS bundles live under `/civica/Bundles/` (`civica.common.js` holds the API service
  definitions) — useful for discovering endpoint names without a browser.

---

## Recipe C — Idox Public Access

The highest-value recipe — Idox powers the majority of UK LPAs. The base path
**varies** — `/online-applications/` (common), `/idoxpa-web/` (Edinburgh),
`/publicaccess/` (Cardiff) all seen, and the wrong one 403s — so treat it as a
per-council variable and detect Idox by its endpoints (`search.do`, `keyVal`,
`/files/{hex}/pdf/`). Note Idox increasingly lives on **vendor-cloud hostnames**
(`*.idoxcloud`, Cardiff's `*.wales`) rather than council domains, so resolve via
PlanIt rather than guessing `<council>.gov.uk`. It is **session-gated** (a `JSESSIONID`
from the search page is required; results endpoints 500 without it — note JSESSIONID is
HttpOnly: rely on curl's cookie jar, not a Set-Cookie grep) and the search form carries
a `_csrf` token you must echo back (format varies: opaque hex or lowercase UUID).
Validated end-to-end against nine councils in August 2026, including Scottish and Welsh
authorities.

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
BASE="https://planningaccess.york.gov.uk/online-applications"   # <- swap per council; base path VARIES (e.g. Edinburgh /idoxpa-web)
BP=$(echo "$BASE" | sed -E 's#https?://[^/]+##')                # path part, e.g. /online-applications
REF="24/00593/FUL"

# 1. Establish session; capture JSESSIONID (-c) and the _csrf hidden token
curl -s -c idox.txt -A "$UA" "$BASE/search.do?action=simple&searchType=Application" -o s.html
CSRF=$(grep -oE 'name="_csrf"[^>]*value="[^"]*"' s.html | grep -oE 'value="[^"]*"' | sed 's/value="//;s/"//')

# 2. POST the simple search. All four fields are required — WITHOUT
#    searchCriteria.simpleSearch=true the server returns "Too many results".
curl -s -b idox.txt -c idox.txt -A "$UA" -L "$BASE/simpleSearchResults.do?action=firstPage" \
  --data-urlencode "_csrf=$CSRF" \
  --data-urlencode "searchType=Application" \
  --data-urlencode "searchCriteria.simpleSearchString=$REF" \
  --data-urlencode "searchCriteria.simpleSearch=true" \
  -o results.html

# 3. Extract the keyVal (opaque ~13-char token, NOT the human reference).
#    An exact-ref search may 302 to the detail page OR return a one-row results
#    list (both observed) — the grep covers both.
KEYVAL=$(grep -oE 'keyVal=[A-Z0-9]+' results.html | head -1 | cut -d= -f2)

# 4. Documents tab -> scrape file hrefs. PDFs are $BP/files/{32-HEX}/pdf/{name}.pdf
#    but NON-PDF attachments (JPG photos/plans) OMIT the /pdf/ segment
#    ($BP/files/{32-HEX}/{name}.jpg — Leeds had 4 of 6 docs like this), so do
#    NOT anchor the grep on /pdf/. Also grep against $BP, NOT a hardcoded
#    /online-applications/ — either mistake silently yields missing files.
#    Reconcile your link count against the documents tab's own total (it lists
#    one row per document) — see the completeness cross-check in the checklist.
DOCS="$BASE/applicationDetails.do?activeTab=documents&keyVal=$KEYVAL"
curl -s -b idox.txt -c idox.txt -A "$UA" "$DOCS" -o docs.html
grep -oE "$BP/files/[A-Fa-f0-9]+/[^\"]+" docs.html | sort -u > files.txt

# 5. Download each file WITH a Referer header = the documents-tab URL.
#    Some councils (verified: RBWM, Greater Cambridge) 404 the file without it;
#    harmless on the councils that don't need it, so always send it.
HOST=$(echo "$BASE" | grep -oE 'https://[^/]+')
while read -r f; do
  name=$(basename "$f")
  curl -s -b idox.txt -A "$UA" -e "$DOCS" "$HOST$f" -o "$name"
done < files.txt
```

Idox gotchas:
- **Base path varies** — **five** variants observed: `/online-applications/` (common),
  `/idoxpa-web/` (Edinburgh), `/publicaccess/` (Cardiff), `/PlanningData-live/`
  (Stockport), `/wam/` (Highland). Derive it from PlanIt's `planning_url`; never
  hardcode it in greps (see step 4).
- **keyVal is opaque and per-application** — scrape it from the results/detail link;
  you cannot construct it from the reference. (PlanIt often hands it to you in
  `docs_url` / `url` — see the PlanIt shortcuts above.)
- **File-GET gating varies three ways — always send BOTH the session jar and the
  Referer**: *session-gated* (Glasgow, Leeds, Stockport, Highland — a cold GET returns
  an HTML 404 under the `.pdf` name, Referer irrelevant), *Referer-gated* (RBWM,
  Greater Cambridge — 404 without `-e <documents-tab URL>`), or *neither* (York,
  Tendring, East Suffolk, Edinburgh). Consequence: never "optimise away" the
  `search.do` session step when jumping via PlanIt's `docs_url`.
- **Non-PDF attachments lack the `/pdf/` path segment** — grep `/files/{hex}/` without
  anchoring on `/pdf/`, verify magic bytes per file, and reconcile the link count
  against the **documents tab's own row count** (this is what catches silent misses).
  PlanIt `n_documents`, when you have it, is a secondary check only — it can lag
  (Highland 8 vs 9 real; Dudley 20 vs 22) so treat it as a lower bound, and note PlanIt
  omits `docs_url` entirely on applications it has seen zero documents for.
- **Session ~30 min idle timeout**; refresh (`search.do`) on long crawls.
- **Pace requests ~1–2s** — small council servers throw transient `000`/`500` on bursts.
- **WAF minority** — most Idox sites take plain curl; a few are behind Cloudflare
  (pass with the real browser UA above) and a rare few behind an *enforcing* Barracuda
  (browser-only, like Civica — see Recipe B). **Barracuda cookies ≠ blocked**: East
  Suffolk sets `BNIS_`/`BNES_` cookies in passive mode and plain curl works fine — the
  actionable signal is an actual served JS challenge or `Blocked` page, not BN* cookies.
- **recaptcha markup ≠ CAPTCHA enforced** — Idox comment/copy-request widgets carry
  recaptcha classes; search and downloads are unaffected.

---

## Recipe D — Northgate (two distinct products)

### D1 · SwiftLG APAS (`/swiftlg/apas/run/`) — ⚠ dying fast

Oracle-backed register, plain curl + cookie jar, no bot protection — **but presume any
historic SwiftLG council has migrated** (3 of 4 tested had: Mole Valley → StatMap;
Dudley, Snowdonia, Pembrokeshire → Agile). Confirm the portal still answers on
`/swiftlg/apas/run/` via PlanIt before applying this. Validated end-to-end at
Warwickshire; the whole chain is **stateless** (works cold, no cookies/CSRF/Referer).

- **Search**: POST `WPHAPPCRITERIA` with `APNID.MAINBODY.WPACIS.1=<ref>` and
  `SEARCHBUTTON.MAINBODY.WPACIS.1=<any non-empty value>` — the SEARCHBUTTON param
  **must be present** (omitting it returns a 110-byte stub); other fields omittable.
  Results render **inline in the POST response** (`WPHAPPSEARCHRES.displayResultsURL`
  is only the re-display/pagination URL). To find refs without PlanIt (which can't
  resolve county councils): date-sweep with `REGFROMDATE`/`REGTODATE.MAINBODY.WPACIS.1`
  (`dd/mm/yyyy`).
- **Detail**: `GET WPHAPPDETAIL.DisplayUrl?theApnID=<REF>` (`theApnID` is literally the
  reference, slashes unencoded). **Do NOT tab-hunt with `theTabNo`** — skinned installs
  render all tabs in one page and non-1 values throw `WCHINTERROR`; fetch with
  `theTabNo=1` (or omit) and grep the whole page for document links.
- **Documents**: hrefs are `<SKIN>DISPLAYMEDIA.showImage?theSeqNo=<n>&theApnkey=<key>&theModule=1`
  (the handler prefix is per-council skin — `WCH` at Warwickshire vs the generic `WPH`).
  This returns a **72-byte meta-refresh stub**, which `curl -L` does *not* follow —
  parse `URL=../MediaTemp/{apnkey}-{seqno}.pdf` out of it, then `GET` that with `-L`
  (it 302s to `/swiftlg/MediaTemp/…`) to get the PDF.

### D2 · Planning Explorer (`/Northgate/PlanningExplorer/`)

Classic ASP.NET WebForms — round-trip `__VIEWSTATE`, `__VIEWSTATEGENERATOR` **and**
`__EVENTVALIDATION` (all three), same cookie jar (`ASP.NET_SessionId`).

- GET `GeneralSearch.aspx`, capture the three hidden tokens (VIEWSTATE can be
  ~96–115 KB — build the POST body with a script, not shell args).
- **Reference lookup: POST the MINIMAL field set** — the three tokens +
  `txtApplicationNumber=<ref>` + `csbtnSearch=Search` (`rbGroup` optional). Every extra
  empty field is WAF-bait: Runnymede's origin WAF 403s any POST containing an empty
  `cboSelectDateValue`. (The `txtProposal` + date-range route is for proposal/date
  sweeps, not reference lookups.)
- Search 302s to `Generic/StdResults.aspx?...&PS=10&XMLLoc=/…/XMLtemp/<session>/<guid>.xml`.
  **Robust `PARAM0` source: skip `StdResults` entirely** — take `XMLLoc` from the 302
  `Location` header and GET that XML directly (same cookie jar); `<PK>` in it *is*
  `PARAM0`. This works even where `StdResults` is WAF-blocked (Runnymede 403s it
  wholesale) and is cleaner than scraping results HTML. Caveat: the `Location` header
  can contain **raw spaces** — percent-encode it yourself; don't rely on `curl -L`.
- Detail page on skinned sites is `Generic/StdDetails.aspx?…&TYPE=PL/PlanningPK.xml&PARAM0=<id>&XSLT=…`
  (the opaque key is **`PARAM0`**, not `keyVal`). Keep slashes literal in the
  `TYPE`/`XSLT`/`XMLSIDE` params — required at Wandsworth (`%2F` → 500), harmless at
  Runnymede. Detail hrefs carry literal CRLF/tabs — strip whitespace.
- **The documents module varies per authority** — both councils examined replaced the
  standard Northgate one, differently, and both work **cold** (no prior session needed
  if you have the ref):
  - *Wandsworth*: bespoke cross-host IAM — `planning2` host, `comments.aspx?case=<ref>`,
    WebForms category-expand postbacks, then `IAM/IAMLink.aspx?docid=<n>` → 302 → PDF.
  - *Runnymede*: NEC "Public Access" MVC on a `docs.<council>` host (a naming collision
    — **not** Idox) — `…/PublicAccess_LIVE/SearchResult/RunThirdPartySearch?FileSystemId=PL&FOLDER1_REF=<ref>`
    (constructible from the ref); the doc list is embedded in the HTML as
    `var model = {…Rows:[{Guid,Doc_Type,Date_Received,Doc_Ref2}]}`; download
    `GET …/Document/ViewDocument?id=<Guid>` (param must be `id` — check Content-Type).
  - *Camden*: **HP TRIM / Content Manager "CMWebDrawer"** on a `camdocs.<council>` host —
    fully constructible from the ref, stateless:
    `GET /CMWebDrawer/PlanRec?q=recContainer:%22<enc-ref>%22&format=json` (ServiceStack
    JSON: `Results[].Uri`, `RecordTitle`, `TotalResults`/`HasMoreItems`, `&pageSize=`
    honoured) then `GET /CMWebDrawer/Record/<Uri>/file/document?inline` → PDF. The
    HTML view double-lists each doc — dedupe on record id. The `&format=json` trick
    likely generalises to any TRIM WebDrawer council.

  PlanIt's `docs_url` points at whichever module a council uses — record it per council.
- WAF: Cloudflare has **three modes** on PE sites: absent (Wandsworth), **passive**
  (Runnymede — any UA passes; the old "empty/default UA gets 403" claim did not
  reproduce), and **score/rate-based enforcing** (Camden's register: the first ~2 curl
  requests reach origin, then *everything* — including previously-working URLs — gets
  the interactive challenge). On a score-based site, grab what you need in the first
  requests; "worked a minute ago, 403 now" = escalation, don't burn retries. Watch also
  for an *origin* WAF with narrow triggers (Runnymede's `StdResults`/
  `cboSelectDateValue` blocks above).
- NEC's `Redirection/redirect.aspx` deep links (PlanIt `url` for some PE councils)
  redirect via a **JavaScript stub, not a 302** — parse `document.location.href` out of
  the body; `curl -L` won't follow.
- **NB migration:** the PE fleet is dying but its successors are **diverse** —
  Birmingham → NEC Assure (Recipe H), Merton → Tascomi (browser-only), Stockport →
  Idox (Recipe C), Camden → cosmetically NEC (`/NECSWS/` paths) but still PE
  underneath. Re-detect the vendor per council; don't assume NEC.

---

## Recipe E — Ocella (`/OcellaWeb/planningSearch`)

Niche, plain server-rendered pages, and **completely stateless** — no session, CSRF,
keyVal, or Referer required anywhere (keep a jar + browser UA + pacing as hygiene).
`$BASE` = e.g. `https://www1.arun.gov.uk/aplanning/OcellaWeb`.

1. **Shortcut** — with an exact reference, skip search entirely:
   `GET $BASE/planningDetails?reference=<REF>&from=planningSearch` (raw ref *with*
   slashes works as-is). PlanIt's applics `url` field for Ocella councils **is** this
   deep link ready-made.
2. Otherwise `POST $BASE/planningSearch` with `reference=<REF>&action=Search`
   (other fields may be empty). **Exact reference only** — broad searches (e.g.
   location-only) silently re-render the empty form with no error. Extract detail
   links: `grep -oE 'planningDetails\?reference=[^"]*'`. Quirk: the postcode field is
   dotted (`OcellaPlanningSearch.postcode`); form dates are `dd-mm-yy` (8 chars).
3. Documents list: `GET $BASE/showDocuments?reference=<REF>&module=pl` (the detail
   page presents this as a POST form, but plain GET works; optional `&filterBy=TYPE`).
   Each row carries category, date (`dd-mm-yy`) and description — use them to label files.
4. Download: `GET` each `viewDocument?file=…&module=pl` href **verbatim from
   showDocuments** (don't construct: `file` is a URL-encoded server-side Windows path,
   `dv_pl_files%5C<REF-with-underscores>%5C<filename>`, spaces as `+`). Verify `%PDF-`.

Arun also injects a *passive* Barracuda fingerprint script (`bnith__`/`x-bni-*`
cookies) that never blocked anything — same lesson as East Suffolk: only an actual
`Blocked` page means blocked.

Ocella gotchas:
- **Grep tolerance**: skinned installs emit non-canonical attribute spacing —
  Hillingdon writes `href ="viewDocument?…"` (space before `=`), so `grep 'href="'`
  silently finds zero links. Match the endpoint name (`viewDocument\?file=`) or use
  `href *=` — a lesson that applies to every server-rendered recipe.
- **The documents module can be outsourced** (Great Yarmouth): `showDocuments` returns
  an **empty 200 page** (no error) while search/detail stay Ocella — documents moved to
  a Civica Portal360 host (reference-keyed Recipe B, RefType `PLANNINGCASE`). Before
  trusting `showDocuments`, check the detail page for a "View Documents" button opening
  another host (`window.open`), and check whether PlanIt's `docs_url` points off-host —
  that's the automatic tell. Same pattern class as PE's per-council doc modules and
  Agile's DMS switch.
- PlanIt shortcuts: `url` = ready `planningDetails` deep link **and**
  `other_fields.docs_url` = ready `showDocuments` link — both steps skippable. The
  applics `reference` field can be null (ref lives in `uid`).

## Recipe F — StatMap horizoNext / "Mirage"

Newer vendor appearing where SwiftLG sites retire. Detect: hostname
`*-publicportal.statmap.co.uk`, path `/horizonext`, title "StatMap Mirage". React SPA
over an **open JSON API** — no session, cookies, or CSRF. PlanIt labels these
`scraper_type: Custom`. `$API` = `https://<council>-publicportal.statmap.co.uk/horizoNext/api`.

1. Reference → internal id:
   ```bash
   curl -s -A "$UA" -H "Content-Type: application/json" \
     "$API/publicportal/planningApplications/pageRequest" \
     -d '{"pageSize":10,"offset":0,"filter":{"parts":[{"filterItems":[{"columnName":"appRef","operator":"=","value":"MO/2026/01108"}]}]}}'
   # -> {"records":[{"id":"130846","name":"MO/2026/01108",...,"total":1}]}
   ```
   **Only** the `filter.parts[].filterItems[]` shape is honoured — any other filter
   shape is *silently ignored* and returns the entire register (~123k records, ~54 MB):
   always send `pageSize` and check `total` == expected. The reference must be the
   exact zero-padded form (`MO/2026/1108` → 0 hits). PlanIt's applics `url` ends in
   the internal id, which lets you skip this step.
2. (Optional) detail: `GET $API/publicportal/planningApplications/{id}`.
3. Documents: `POST $API/mirage/attachments/P_APPLICATION/{id}` with body `{}` and
   JSON content-type (a bodyless/null POST 400s) → `attachments[]` with
   `id`/`name`/`description` (+ heavy base64 thumbnails; ignore them).
4. Download is **two hops**: `GET $API/mirage/attachments/download/{attId}` returns
   JSON `{fileName, url}` where `url` is on a *different* base path
   (`/publicportal-horizonService/attachments/{attId}/download`); GET that url = the
   PDF. (`/show` variant = inline view.)
5. SPA deep links (`…/horizoNext/publicportal/planningapplications/<id>`) 404 to
   direct GET — scrape via the API only.

## Recipe G — Agile Applications "Citizen Portal"

The other common SwiftLG successor. Detect: host
`planning.agileapplications.co.uk/<slug>/`, title "Citizen Portal Planning",
`*.sunagile.com` CSP; PlanIt `scraper_type: Agile`. SPA over a shared multi-tenant
**open JSON API** — no cookies/session/CSRF; the tenant is selected by an `x-client`
header. **Warning:** the portal host returns the 2.5 KB SPA shell with HTTP 200 for
*every* path (including fake `/api/*`) — never probe it for data; the API is a separate
host.

```bash
API="https://planningapi.agileapplications.co.uk"
# Resolve the client CODE (NOT always the URL slug — pcnpa -> PEMBROKESHIRECOAST):
CODE=$(curl -s -A "$UA" "https://identity.agileapplications.co.uk/api/client/get?url=snowdonia" \
  | grep -oE '"code":"[^"]*"' | head -1 | cut -d'"' -f4)
H=(-H "x-client: $CODE" -H "x-service: PA" -H "x-product: CITIZENPORTAL")   # all three required

# 1. ref -> internal id (or take it from PlanIt applics url tail and skip)
curl -s -A "$UA" "${H[@]}" "$API/api/application/search?reference=NP5%2F50%2F12N"   # -> results[].id
# 2. detail + 3. document list
curl -s -A "$UA" "${H[@]}" "$API/api/application/20774/document"   # -> [{documentHash,name,description,...}]
# 4. download — path-form needs NO headers (hash is self-authorizing)
curl -s -A "$UA" "$API/api/application/document/$CODE/<documentHash>" -o form.pdf
```

- Missing any of the three headers → `401 "Client has not beeing selected"` (sic);
  `x-service` must be `PA` (not `PLANNING`).
- **Per-tenant `DMS` switch** (from `GET identity…/api/service/configuration`, key
  `DMS`): `SHAREPOINT` → documents via the API above. `EXTERNAL`/`IAW` → the documents
  tab is just an **iframe of `DMS_URL + <ref>`** pointing at a *council-hosted* DMS
  (Pembrokeshire → NEC PublicAccess `RunThirdPartySearch`, same product as Runnymede's
  doc host). PlanIt's `docs_url` is that iframe link pre-built.
- Outage signature (don't misread as a block): `500` on every data call while
  `/api/system/checkserver` 200s and the external DMS host is TCP-dead = council
  backend down; retest later.

## Recipe H — NEC Assure "ES"

Where Northgate PE fleets are migrating (NEC Software Solutions = ex-Northgate). Detect:
path `/NECSWS/ES/Presentation/Planning/OnlinePlanning/`, `AssureLogo` branding,
ASP.NET MVC + AJAX. PlanIt may **stalely** report `PlanningExplorer` — trust its
`planning_url`, not the label. Everything keys off the **human reference**
(URL-encoded, slashes → `%2F`); the internal key is never needed. Docs/downloads work
cold (stateless).

1. Deep link (skip search): `GET …/OnlinePlanning/OnlinePlanningOverview?applicationNumber=<enc-ref>`
   (PlanIt `url`/`docs_url` are exactly this).
2. Docs list: `POST …/OnlinePlanning/GetOnlineDocuments?applicationNumber=<enc-ref>&currentPageIndex=0&IsDatePublishSortedDescending=true&pageSize=200`
   (params in the query string, empty body). **`currentPageIndex` is 0-based** — index
   `1` returns the correct total but *zero rows* ("No record(s) found"), a silent trap.
3. Download: `GET …/OnlineDisplayDocument/DisplaySearchDocument/<name>?applicationNumber=<enc-ref>&FileName=<name>&fileType=.pdf&aspectGuid=<32-hex>`
   — scrape hrefs verbatim (un-escape `&amp;`); `aspectGuid` is per-document, not
   constructible. (Bulk zip: `POST …/OnlineDisplayDocument/DownloadDocumentImages`.)

Search without a deep link is fussy (needs the full ~71-field jQuery-serialized form);
prefer the PlanIt deep link.

## Recipe I — TerraQuest "Planning Portal 2" (covers all 11 NI authorities)

One register covers **all of Northern Ireland** (`planningregister.planningsystemni.gov.uk`,
since Dec 2022; the `LA01`–`LA11` ref prefix identifies the council, `LA04`=Belfast).
Generic detection for any PP2 site: Next.js shell + a `/__ENV.js` runtime-config file
whose API is on `*.tqinfra.co.uk`. Open JSON API, anonymous, no cookies/WAF — but with
two novel traps.

```bash
BASE="https://planningregister.planningsystemni.gov.uk"
ENVJS=$(curl -s -A "$UA" "$BASE/__ENV.js")                 # ALWAYS fetch this first
API=$(echo "$ENVJS"   | grep -oE '"NEXT_APP_PLANNING_REGISTER_API":"[^"]*"' | cut -d'"' -f4)
TENANT=$(echo "$ENVJS"| grep -oE '"NEXT_APP_PP_TENANT_ID":"[^"]*"'          | cut -d'"' -f4)
T=(-H "TQ-Tenant: $TENANT")   # MANDATORY on every API call

# 1. ref -> applicationId (or take the id from PlanIt applics url tail and skip)
curl -s -A "$UA" "${T[@]}" --get "$API/applications" \
  --data-urlencode "SearchTerm=LA04/2026/1407/F" --data-urlencode "SearchStatus=0" \
  --data-urlencode "PageNumber=1" --data-urlencode "PageSize=10"   # -> applications.items[].applicationId
# 2. detail INCLUDES the document list (supportingDocuments[])
curl -s -A "$UA" "${T[@]}" "$API/application/711859"
# 3. per document: resolve the SAS url and download IMMEDIATELY (expires ~5 min)
URI=$(curl -s -A "$UA" "${T[@]}" "$API/application/711859/6290101" | grep -oE '"documentUri":"[^"]*"' | cut -d'"' -f4)
curl -s -A "$UA" "$URI" -o form.pdf   # Azure Blob SAS — no headers needed on the blob GET
```

- **Trap 1 — silent tenant failure:** a missing/wrong `TQ-Tenant` header does *not*
  error; search returns empty `items[]` and detail returns literal `null`,
  indistinguishable from "not found". Always re-read the GUID from `/__ENV.js`.
- **Trap 2 — SAS expiry:** `documentUri` is a ~5-minute Azure Blob SAS URL; resolve and
  download one document at a time, never batch-collect URIs first.
- `SearchStatus` must be the **integer** `0`/`1`/`2` (string `"All"` is rejected).
  Docs are **not all PDFs** (.docx common) — verify magic bytes per file.

## Arcus (Salesforce) — browser-only; hand the user a deep link

Public registers on Arcus are Salesforce Experience Cloud (Lightning) SPAs on
`*.my.site.com`/`*.force.com` or a council CNAME (`Server: sfdcedge`). There is **no
supported public API** for the register data: search, detail, and document listings run
through the Arcus managed package's custom Salesforce controllers, which are not exposed
to an anonymous HTTP client the way the open-API vendors are. Plain curl gets a
JavaScript app shell, not data.

**Do not try to reverse-engineer or replay the managed-package internals.** For Arcus
councils, the right outcome is to **hand the user a browser deep link** and let the
official site render it:

- PlanIt's applics `url` is the record deep link `…/pr/s/detail/<18-char-recordId>`;
- or the register landing `…/pr/s/register-view?c__r=Arcus_BE_Public_Register` (no known
  parameter to pre-fill a search).

PlanIt is unreliable for Arcus (it can mislabel `scraper_type` and carries no
`docs_url`/`n_documents`), but its `url` field is a good deep link. Known Arcus councils
include Manchester, Haringey, Bromley, Wiltshire, Anglesey, Powys, Ashford, and Salford.

---

## Reference-number formats (for search / normalisation)

No national standard — each LPA sets its own; feed the **exact original string
(including slashes)** back into a portal. Common shapes:

- `YY/NNNNN/TYPE` — year / serial / type, e.g. `25/01234/FUL`, `26/03301/LBC`
  (most Idox/Northgate).
- `AREA/YYYY/NNNN/TYPE` — leading district digit, e.g. `6/2026/1249/HOUSE`; type
  sometimes dropped: `5/2026/1349`.
- `PREFIX/YY/NNNN/TYPE` — council prefix + year + serial + type, e.g. `DC/26/2860/FUL`
  (East Suffolk).
- `PREFIX/NN/NNNNN` — 2-letter council prefix, e.g. `MO/2011/1449`; StatMap Mole
  Valley now uses `MO/YYYY/NNNNN` with a **zero-padded 5-digit serial**
  (`MO/2026/01108` — the unpadded form gets zero hits).
- `PARISH/NNN/YY/TYPE` — parish prefix with year *third*, e.g. `A/124/26/NMA`,
  `FP/101/26/T` (Ocella/Arun).
- `YYYY/NNNN` — bare year/serial, no type, e.g. `2026/2894` (Wandsworth);
  `YYYY/NNNNN/PA` (Birmingham/NEC).
- `P/YY/NNNN[/TYPE]` — e.g. `P26/0883`, `P26/0896/PNA` (Agile/Dudley).
- `NP<area>/<ward>/<serial><letter>` — Welsh national-park style, no year, e.g.
  `NP5/50/12N` (Snowdonia); `NP/YY/NNNN/TYPE` (Pembrokeshire Coast).
- `LA<NN>/YYYY/NNNN/TYPE` — Northern Ireland; `LA01`–`LA11` = the council
  (`LA04`=Belfast), e.g. `LA04/2026/1407/F`.
- `PLA-YYYY-NNNNNN` — Arcus internal id, e.g. `PLA-2026-001211` (distinct from the
  council's classic ref).
- Appeals (national, PINS): `APP/<code>/<letter>/YY/NNNNNNN` — not an LPA ref.
- Planning Portal submission id: `PP-NNNNNNNN` — applicant's national id, not the LPA ref.

Common type suffixes: **FUL** full · **HOUSE/HH** householder · **OUT** outline ·
**RES/REM** reserved matters · **LBC** listed building · **CAC** conservation area ·
**ADV** advertisement · **TPO/TCA** trees · **LDC/CLD/CLE** lawful development cert ·
**PA/PD** prior approval · **DOC/CND** discharge/vary conditions · **NMA** non-material
amendment · **COU** change of use. Normalisation: uppercase; leading 2 digits are the
receipt year (watch `19` vs `20` rollover on old refs).

---

## The registry (`planning-portal-registry.json`)

Coverage of "all UK LPAs" is data, not prose. The companion file
[`planning-portal-registry.json`](planning-portal-registry.json) is the growing
lookup that maps each authority → portal URL → vendor, and — crucially — records
**per-authority specializations** discovered by testing (quirks, tokens, blockers,
deep-link formats). The skill recipes are the *methods*; the registry is the *data*.

**Resolution order** for a new request (council + reference):
1. Look up the authority in the registry. If present and `status: tested-ok`, apply
   its recorded specializations directly and run the recipe from the user's reference —
   fastest path, and **no PlanIt call needed** (this is the Step 0 fast path).
2. If not present, resolve the portal URL + vendor via PlanIt's areas API (or, failing
   that, the council site → "view/track planning applications"), identify the **vendor**
   from its detection signature, and apply that vendor's recipe.
3. **Record the result back into the registry**: set `vendor`, `portal_url`,
   `status`, `last_tested`, `reference_format_example`, and write anything
   non-obvious under `specializations`. This is how coverage compounds — every
   tested council makes the next one in the same vendor family cheaper.

**Status vocabulary** (see the file's `conventions`): `untested`, `tested-ok`,
`browser-only`, `blocked`, `partial`, `broken`.

Keep the per-vendor recipe knowledge in *this* file and the per-council facts in the
*registry*; don't duplicate one into the other.

## Gotchas / checklist

- [ ] **Reference format varies by council** — pass it through exactly as given;
      don't normalise slashes or suffixes.
- [ ] **Always set a browser User-Agent.**
- [ ] **Keep one cookie jar** across search + download (`-b`/`-c` on every call).
- [ ] **`file *.pdf` after download** to confirm they aren't HTML error/block pages —
      and don't assume PDF: some vendors (TerraQuest) serve `.docx` too. Check magic
      bytes per file.
- [ ] **Sanitize the output filename** — server-supplied names are untrusted. Take
      `basename`, strip path separators and leading dots, and write into a fixed target
      directory; never pass a scraped path straight to `-o` (guards against `../…`
      traversal). Downloaded files are untrusted third-party content.
- [ ] **A `Blocked` / bot-challenge page = stop the curl approach** and switch to a
      real browser session (Chrome extension, in-app pane, or hand the user a link).
      But a **WAF cookie (`BN*`, `incap_*`, `__cf_bm`) or a `500`/`recaptcha` marker is
      NOT a block** — only an actual challenge/`Blocked` page is. Most WAFs are passive.
- [ ] **Know the two challenge signatures that never say "Blocked"**: AWS WAF managed
      challenge returns **HTTP 202** with `x-amzn-waf-action: challenge` (and an
      *empty body* on XHR-style hits — looks like an empty response, not a block;
      Tascomi/Merton). Cloudflare can be **score-based**: first requests pass, then
      everything 403s including URLs that just worked (Camden) — front-load the
      requests you need and treat later 403s as escalation.
- [ ] **A TLS/connection-layer failure is an IP block, not a portal property** —
      repeated curl exit 35 (TCP connects, ClientHello gets EOF, no HTTP, no page)
      after initially-successful requests = the front-end dropped your IP.
      **If on a VPN, suspect VPN-exit-IP reputation first** (Swansea and Highland
      NetScalers did exactly this to a NordVPN IP and recovered instantly off-VPN);
      retest from a residential IP before recording the council as hostile.
- [ ] **Completeness cross-check — count the documents the portal itself reports, and
      confirm your enumerated links match.** This is the check that catches silent
      scraping misses (wrong grep, skinned `href ="` markup, outsourced doc modules
      serving empty 200 pages). Get the expected count **from the portal, not PlanIt**:
      most documents pages state a total or render one row per document (count the rows),
      and the open-API vendors return a `RowCount`/`total`/`TotalResults` field. Use
      PlanIt's `n_documents` only as a secondary check when you happen to have it (and
      treat it as a lower bound — it can lag, e.g. Highland 8 vs 9, Dudley 20 vs 22). If
      the counts disagree, you are missing files — widen the grep and re-enumerate.
- [ ] **When the portal is a JS/SPA shell, find its runtime-config** (`/__ENV.js`,
      `config.js`, app bundle) for the real API host, tenant id, and any required
      header — and never probe the SPA host for data (it may 200 with an empty shell
      on every path).
- [ ] **Watch for silent failures on the open-API vendors** — a missing tenant
      header/param can return empty results or `null` rather than an error (TerraQuest,
      StatMap, Agile). Verify a `total`/count, don't trust an empty list.
- [ ] **Verify the vendor before trusting PlanIt's `scraper_type`** — it can be stale
      (Birmingham) or wrong (Manchester). Its `planning_url`, `url`, and `docs_url` are
      reliable; the label is a hint.
- [ ] **Distinguish a council backend outage from a block** — `500` everywhere while a
      health endpoint 200s and the doc host is TCP-dead = outage; retest later.
- [ ] **Label the files** using the description/date shown next to each link.
- [ ] **Report anything not retrieved** rather than silently returning a partial set.

## Coverage

Which authorities have been checked — with each council's `status` and `last_tested` —
is recorded in [`planning-portal-registry.json`](planning-portal-registry.json). Treat it
as a living cache: portals migrate, so re-resolve the vendor per council at run time
rather than trusting a cached row.
