---
name: application-triage
description: >-
  Given a UK planning application, work out which material planning
  considerations are actually engaged and which representation skill(s) to run
  (ecology, transport, heritage, flood risk, …), in what priority order — or
  advise that there is no strong ground to object. The router for the planning
  representation skills. England-focused. Not legal advice; human review required.
license: MIT
---

# Planning application triage

Help a member of the public who has an application in front of them but doesn't know **which
grounds are worth pursuing**. This skill reads the application, identifies the material
considerations that are genuinely engaged, ranks them, and routes each to the representation
skill that handles it — or says plainly that there is no strong objection.

It is the **router** for the representation skills, not a drafting skill itself. It answers
"what should I object about, and how strong is each ground?", then hands off.

## When to use

The user has a planning application (a reference + council, or the documents) and asks
something like: "should I object to this?", "what are the grounds?", "what's wrong with this
application?", "which of these is worth raising?" Use it first, before the topic-specific
skills, whenever the grounds aren't already decided.

## What you need first

- The **application reference and council**, or the **documents themselves** — uploaded,
  pasted, or already-downloaded files work directly; the companion
  **planning-document-search** skill is only needed when you don't have them (it
  retrieves them from the reference + council).
- The **proposal description and application type** (full / outline / reserved matters / s73
  / listed building consent / householder …) — this frames everything.
- The **site's planning constraints** — is it in a conservation area, near a listed building,
  in a flood zone, Green Belt, an AONB/National Landscape, greenfield? Public constraint data
  (e.g. `planning.data.gov.uk` for conservation areas, listed buildings, Article 4 directions;
  the Environment Agency "Flood map for planning" for flood zones) tells you this without the
  application documents.
- The **document list itself** — it is the single best signal. The presence of an *Ecological
  Impact Assessment*, *Transport Assessment*, *Heritage Statement* or *Flood Risk Assessment*
  tells you which considerations the applicant themselves thought were engaged.

## The integrity principle

**Only flag a ground that is genuinely engaged and arguable.** Triage is not a licence to
manufacture objections — if the application is sound, or a consideration is not actually in
play, say so. Two disciplines in particular:

- **Distinguish material from non-material.** Objections must rest on *material planning
  considerations*. Common **non-material** concerns to set aside (or reframe): loss of a
  private view; impact on property values; competition with an existing business; boundary or
  covenant disputes; the identity or motives of the applicant; construction disturbance in
  itself (as opposed to a permanent effect); and moral objections. Tell the user honestly when
  their concern isn't material — and whether it can be reframed as one that is (e.g. "it will
  ruin my view" is not material, but "it is overbearing and harms the character of the street"
  may be).
- **Rank honestly.** Not every engaged ground is a *strong* ground. Say which are decision-
  critical, which are supporting, and which are weak — so the user spends effort where it
  counts.

## Workflow

### Step 1 — Intake
Get the application (reference + council, or documents), the proposal and its **type/stage**,
and the **site constraints** (conservation area, listed buildings, flood zone, Green Belt,
AONB, greenfield/brownfield, protected trees). Retrieve the **document list**.

### Step 2 — Scan for engaged considerations
Work through [`references/material-considerations.md`](references/material-considerations.md).
For each consideration, check the *tells* — the application type, the proposal, the site
constraints, and the presence (or telling *absence*) of the relevant technical document. Note
the evidence for each ground you flag.

### Step 3 — Rank
Grade each engaged ground: **decision-critical / supporting / weak**, on the strength of (a)
how clearly national or local policy is engaged, (b) whether the applicant's evidence looks
thin or is missing, and (c) how much weight the consideration typically carries. Set aside
non-material concerns (with a reframe where possible).

### Step 4 — Route
For each ground worth pursuing, name the representation skill that handles it and hand off:

| Consideration | Skill |
|---|---|
| Ecology / biodiversity / protected species / BNG | **ecological-representation** |
| Transport / highways / access / parking / active travel | **transport-representation** |
| Heritage / listed buildings / conservation areas / archaeology | **heritage-representation** |
| Flood risk / drainage / SuDS | **flood-representation** |
| Other material considerations (design, amenity, Green Belt, landscape, …) | *no dedicated skill yet — see the map for the framework and argue on the documents' own facts* |

Recommend an order (lead with the decision-critical grounds). Note where two skills should
both run (a scheme often engages several).

### Step 5 — Hand off / summarise
Tell the user: the grounds worth objecting on (ranked), which skill will draft each, the
non-material concerns to drop, and — if that's the honest answer — that there is no strong
ground and an objection would not be sustainable.

## Reference files

- [`references/material-considerations.md`](references/material-considerations.md) — the
  catalogue of material considerations: what each is, the tells that it's engaged, the skill
  or framework that handles it, and the common non-material concerns to exclude.

## Scope and limitations

- **Not legal advice; no warranty; output requires human review.** Triage is a starting
  assessment, provided "as is"; a person must confirm the grounds and the evidence before
  acting.
- **England-focused.** Material considerations are broadly similar across the UK but the
  policy framework differs in the devolved nations — flag when the application is outside
  England.
- **A UK planning representation is public and in the submitter's name** — carry that warning
  through to whichever representation skill drafts the objection.
- **"No strong ground" is a valid, valuable output.** Say it when it's true.
