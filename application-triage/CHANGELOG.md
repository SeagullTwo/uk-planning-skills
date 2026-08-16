# Changelog — application-triage

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
- **Step 2 (decision framework) now points to the companion `national-planning-policy`
  skill** for the edition register, verify-before-citing protocol, and the shared s.38(6)/
  presumption citations — including checking whether the tilted balance is engaged or
  disapplied. _Why:_ one shared register instead of per-skill NPPF snapshots that drift.

### Added
- **New Step 2 — "Establish the decision framework (s.38(6))":** adopted development plan →
  relevant policies → emerging plan and its weight → neighbourhood plan → national policy,
  before scanning for grounds; findings are anchored to named plan policies. _Why:_ reviewer
  feedback — determination legally starts with the development plan, and grounds framed as
  conflict with named plan policies are the strongest an objector can raise; the plan was
  previously an afterthought.
- **Planning history in intake:** previous applications, refusals, appeal decisions on the
  same site, enforcement, extant permissions/conditions, s73s. _Why:_ a previous Inspector's
  decision on the same site can outweigh any generic policy argument.
- **Consultee map in `references/material-considerations.md`** (who speaks to what), with an
  instruction to locate and read the matching response for every engaged consideration.
  _Why:_ generalises the ecology skill's "the LPA ecologist is the strongest anchor" insight
  across the system; a consultee's requested conditions are a ready-made ask.
- **"So-what" test in ranking (A/B/C):** each ground is classified as demonstrated harm (A),
  insufficient evidence (B), or conditionable (C), with an honest view on whether the grounds
  together would plausibly justify refusal. _Why:_ a list of technically valid criticisms is
  not itself a case for refusal; this stops impressive-but-ineffective objections.

### Changed
- **"What you need first" now says uploaded/pasted/already-downloaded documents work
  directly, and `planning-document-search` is only needed when the user doesn't have
  them.** _Why:_ makes explicit that direct document supply is a first-class input, and
  completes the retrieval skill's fail-fast handover (stop → download manually → feed the
  files back in here).

## 0.1.0 — 2026-08-14 — Initial release

First version: the **router** for the representation skills. Given an application, it
identifies the engaged material considerations, ranks them, and routes each to the skill that
handles it. Structure: `SKILL.md` + `references/material-considerations.md`. Key design
decisions:

### Added
- **A router, not a drafter.** _Why:_ the suite had drafting skills but nothing to answer the
  lay user's real first question — "what should I object about?" Triage fills that gap and ties
  the skills together; it hands off rather than drafting.
- **Detection from the document list and site constraints.** _Why:_ the applicant's own
  submitted reports (and their telling *absence*) plus the site's constraints
  (`planning.data.gov.uk`, the EA flood map, the local plan) are the fastest, most reliable
  signal of which considerations are engaged — more reliable than reading every document first.
- **An explicit non-material list, with reframes.** _Why:_ lay objectors most often lose
  credibility by raising non-material concerns (loss of view, property values, competition,
  private disputes). Naming them — and offering a material reframe where one exists — is as
  valuable as naming the good grounds.
- **Honest ranking (decision-critical / supporting / weak) and a "no strong ground" output.**
  _Why:_ consistent with the suite's integrity principle — the point is to spend effort where
  it counts, and sometimes the honest answer is not to object.

### Notes
- Routes to `ecological-representation`, `transport-representation`, `heritage-representation`
  and `flood-representation`; for considerations without a dedicated skill yet (design,
  amenity, Green Belt, landscape, trees, air quality, …) it gives the framework to argue on
  the application's own facts. Add routes here as new representation skills are built.
