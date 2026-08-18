# Changelog — appeal-precedent-analysis

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Added
- **Initial release: the skill, the comparability/weight reference, and a 25-record seed
  corpus of June 2026 appeal decisions.** _Why:_ built off the back of a themes-and-bias
  study of 1,505 June 2026 decision letters (200 read and coded in full). The study showed
  precedents only move decision-makers under narrow conditions, and the skill encodes
  those conditions rather than the naive "X decided Y, so Y" move.
- **The workflow centres on a comparability test (the "Z-test"), not on citation.** _Why:_
  the coded sample showed inspectors distinguish cited precedents almost by default ("I do
  not have full details of these cases... before me"; "each decision is made on its
  individual merits") — 12 of 60 allowed planning appeals in the sample expressly
  distinguished a party's precedent. The one citation observed to receive "great weight"
  was same-street, same-issue, same-policy, and quoted. So the skill tests
  determinativeness, factual match on the operative conditions, framework currency, and
  the available distinctions, before a citation is allowed out of the door.
- **A mandatory adverse-precedent step.** _Why:_ the corpus itself contains near-mirror
  pairs (informal-verge open space ✗ vs poor-quality open space ✓; substandard HMO rooms
  ✗ vs standards-met HMO ✓). A representation citing only its half of a known pair invites
  the officer to complete the pair; surfacing the adverse decision first is both honest
  and tactically sound.
- **Framework-currency field on every record, wired to the national-planning-policy
  crosswalk.** _Why:_ every seed decision applied the December 2024 NPPF, which the
  17 August 2026 edition replaced with coded policies — and some mechanisms changed
  substantively (tilted balance → S3–S6). A precedent citing a superseded mechanism can
  mislead; each record states what survives and what must be re-verified.
- **Data layer is structured records, not decision letters; personal data minimised.**
  _Why:_ repo rule 7 keeps downloaded documents out of the repo, and rule 2 puts
  per-instance facts in data files. Records carry the public citation fields (reference,
  date, LPA, site, outcome) and verbatim quotes with paragraph numbers, verified against
  the letters on a stated date; appellant/agent/inspector names are omitted as unnecessary
  to cite or verify a decision. The published letter remains the authority and the skill
  requires re-verification before use.
- **The consistency principle is stated with its authority (*North Wiltshire DC v SSE*
  (1992) 65 P&CR 137), citation verified against published sources, with a ⏳ run-time
  re-verification flag.** _Why:_ evidence-before-assertion (house rule 3); the case is the
  standard consistency authority and the "or reasons given" limb is exactly the honest
  form of the ask this skill drafts.
- **Weight tiers (same site → same LPA/policy → same test → reasoning-only) with open
  adjustments for recency, procedure, batches and subsequent history.** _Why:_ the study
  found procedure correlates with scrutiny depth (inquiry 59% / hearing 52% / written reps
  30% allowed — a selection effect, disclosed as such), and linked-batch decisions
  masquerade as multiple concurring authorities (the Manchester advert batch); the tiers
  make the claimed weight explicit and defensible.
