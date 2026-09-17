# Finding the agenda and its documents

Committee business is **not on the planning portal**. It sits on a democratic-services
platform on a different hostname, and this repo's
`planning-document-search` registry does not cover these systems.

> **Verified against two councils on 16 September 2026.** Both run ModernGov, and they
> publish in **materially different shapes** — which is the main reason this file exists.
> Treat every recipe here as a pattern to confirm, not a guarantee.

## 0. Which platform?

| Platform | Signature | Share |
|---|---|---|
| **ModernGov** | hostname `<council>.moderngov.co.uk`, or a `/mgListCommittees.aspx` path on the council's own domain | dominant |
| **CMIS** | `/cmis/`, `ieListMeetings.aspx` under a CMIS path | a minority |
| Bespoke / CMS pages | committee pages built into the council website | the tail |

A survey of 296 English planning authorities found **254 ModernGov, 16 CMIS, 26 unknown**
— so the ModernGov recipe covers most of the country, and it is worth getting right.

⏳ **There is no committee-system registry in this repo**, and a base URL derived from a
council's name is a hypothesis rather than a fact: confirm it resolves and serves a
committee list before relying on it. This is the same distinction
`planning-document-search`'s portal registry draws between a probed vendor and one
identified only by fingerprint — and the reason that registry exists is that guessing does
not survive contact with 300 councils.

## 1. ModernGov — the recipe

Four steps, and every URL below is relative to the ModernGov base
(e.g. `https://<council>.moderngov.co.uk`).

### Step 1 — list the committees

```
GET /mgListCommittees.aspx?bcr=1
```

Returns links of the form `mgCommitteeDetails.aspx?ID=<CId>`. Filter the link text for
"planning".

**Expect more than one.** One council in the sample has both a *District Planning
Committee* and a *Planning Committee*; another has a single *Planning Committee*. Area
committees, a strategic committee and a rights-of-way committee are all common. **The item
you care about is on exactly one of them**, and picking the wrong committee produces a
confident review of the wrong meeting.

### Step 2 — list that committee's meetings

```
GET /ieListMeetings.aspx?CId=<CId>&Year=0
```

`Year=0` gives the current municipal year; omit or vary it for past years. Returns links of
the form `ieListDocuments.aspx?CId=<CId>&MId=<MId>&Ver=4`, with the meeting date and time
as the link text.

Both councils list **future** meetings here as well as past ones. A future meeting's page
exists before its pack does — so the page resolving is not evidence the pack is published.

**A cancelled meeting also has a page, and it returns an ordinary 200 with no documents.**
One meeting in the sample renders normally, lists zero documents, and carries the word
`CANCELLED` in the page body. Check for it before concluding anything from an empty document
list — "no documents" has at least three causes and they need different answers. See the
stop-or-ask table in `SKILL.md`.

**Councils run more than one planning committee, and the meeting lists are separate.** One
council in the sample has a *District Planning Committee* and a *Planning Committee*, each
with its own `CId` and its own monthly cycle. Checking one and finding nothing tells you
nothing about the other.

### Step 3 — the meeting's documents

```
GET /ieListDocuments.aspx?CId=<CId>&MId=<MId>&Ver=4
```

Two document namespaces appear in the hrefs, and the distinction is the useful part:

| Pattern | What it is |
|---|---|
| `documents/g<MId>/…pdf` | **meeting-level**: agenda frontsheet, public reports pack, printed minutes |
| `documents/s<DocId>/…pdf` | **item-level**: individual reports, addenda, maps, appeals sheets |

Hrefs are **relative and have no leading slash**, and carry a `?T=<n>` suffix on the
meeting-level documents. A grep anchored on `/documents/` finds nothing; anchor on
`documents/`.

### Step 4 — fetch, and record what existed

Take everything, not just the largest file. See the two shapes below.

### ⚠️ Two ways to get a 403 that is not a block

Both were hit while writing this file, and both look identical to bot protection:

- **No User-Agent, or an unfamiliar one → 403.** A request with no UA is refused outright;
  a browser UA is accepted. Send a browser UA with an identifying comment and a contact
  appended, as `planning-document-search` does.
- **Disabling TLS certificate verification → 403.** This is the nastier one. Turning
  verification off — the reflex when a client hits certificate trouble — changes the
  handshake enough that the request is refused, while the *same* request with the default
  TLS context succeeds. **Do not disable certificate verification here.** If you have,
  turn it back on before concluding the site is blocking you.

Neither produces a challenge page, so neither is `bot_protection` in the portal-registry
sense. They are client faults that present as refusals, and diagnosing one as a block will
send a user to a browser for a portal that works perfectly.

## 2. The two shapes, and why you must detect rather than assume

Both councils below run the same platform and publish quite differently.

### Shape A — one combined pack

```
documents/g<MId>/Agenda frontsheet <date> <committee>.pdf?T=0
documents/g<MId>/Public reports pack <date> <committee>.pdf?T=10
documents/s<id>/<one supporting document>.pdf
```

The officer reports are **inside** the reports pack, consecutively. The meeting page is
short and lists only a handful of documents. **Splitting is required**: use the agenda
frontsheet for the running order and the references, then split the pack on item
boundaries.

### Shape B — per-item documents

```
documents/g<MId>/Agenda frontsheet <date> <committee>.pdf?T=0
documents/g<MId>/Public reports pack <date> <committee>.pdf?T=10
documents/g<MId>/Printed minutes <date> <committee>.pdf?T=1
documents/s<id>/06 <APP REF> Report.pdf
documents/s<id>/06 <APP REF> Addendum Parish Objection.pdf
documents/s<id>/06 <APP REF> Addendum 2 Council Update.pdf
documents/s<id>/06 <APP REF> Map.pdf
documents/s<id>/07 <APP REF> Report.pdf
documents/s<id>/Appeals Sheet <date>.pdf
```

Here the filename convention does much of the work for you: **`<agenda item no> <application
reference> <document type>`**. The item map falls largely out of the file listing, and the
addenda are *visible as separate documents*, which they are not in Shape A.

**A combined pack usually still exists in Shape B.** Do not treat its presence as evidence
you are in Shape A. Decide by whether per-item `s<id>` reports exist, not by whether a pack
does.

### ⚠️ The filename convention is not stable, even at one council

Verified on two meetings of the **same committee**, two weeks apart:

```
06 DC-26-0010 Report.pdf          one meeting: item, ref, and a type word
04 DC-26-0945.pdf                 the next:     item and ref only, no type word
DC-26-0010 - Addendum.pdf         an addendum with NO item number at all
Agenda Update Sheet.pdf           a third council: no item number, no reference
```

So **parse defensively and reconcile, do not pattern-match and trust**:

- Treat the item number and the application reference as the things to extract; treat
  everything after them as a free-text type that may be absent.
- A document with no item number may still belong to an item — match on the **reference**.
- A document with neither may be meeting-level and cover several items at once.
- **Always reconcile against the agenda frontsheet.** It carries the running order and the
  references, and it is the only reliable statement of what the committee will consider. If
  your parse and the frontsheet disagree, the frontsheet is right and your parse is wrong.

### Some meetings have no combined pack at all

One meeting in the sample published an agenda frontsheet, the previous minutes, a single
officer report and an update sheet — **and no "Public reports pack"**. Do not treat the pack
as guaranteed, and do not report "no pack found" as a failure when the item reports are all
present.

## 3. Addenda — the thing most likely to be missed

⚠️ **The late documents are the ones that change the decision, and they are the ones a
naive fetch misses.** They are published after the main pack, sometimes the day before or
the morning of the meeting.

Look for, in the document titles: `Addendum`, `Addenda`, `Late`, `Update`, `Update sheet`,
`Supplementary`, `Additional`. In Shape B they carry the item number, so they attach to an
item unambiguously. In Shape A they may be a single meeting-level document covering several
items at once.

Two rules:

- **Re-check the meeting page on the morning of the meeting**, and record the time you
  checked in the output.
- **Where no addendum exists, say so** rather than staying silent. "No addendum as at
  09:00 on the day" and "we did not look" are different statements, and the reader cannot
  tell them apart unless you say which it is.

## 4. CMIS and bespoke systems

CMIS uses the same `ieListDocuments.aspx` / `ieListMeetings.aspx` page names as ModernGov
— they share an ancestry — but paths and parameters differ per install, and it is a small
enough minority that it is not worth a speculative recipe here. Resolve it by reading the
committee page.

⏳ **Untested.** When a CMIS council is worked, record the recipe here rather than in the
skill body, and note the council it was verified against and when.

For a bespoke system, find the committee page from the council's site, and follow the links
a member of the public would. Do not attempt to generalise from one bespoke install.

## 5. Responsible use

The same posture as `planning-document-search`, and for the same reasons:

- **This is a user-directed retrieval of one meeting's papers**, which is ordinary public
  access. Enumerating every meeting for every council is not, and is out of scope.
- **Pace it** — at least ~2 s between requests to one host, one connection at a time.
- **Identify yourself** with a real contact.
- **Never defeat a bot challenge.** If the committee system challenges the client, stop and
  hand the user the meeting URL.
- **Packs contain third-party personal data** — objectors' names, addresses, sometimes
  signatures. Retrieve what the task needs, report the substance of objections rather than
  who made them, and do not reproduce contact details.
