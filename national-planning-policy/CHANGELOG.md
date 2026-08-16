# Changelog — national-planning-policy

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
- **A/B/C paragraph now also points to the `planning-balance` companion skill.** _Why:_
  the balance skill is where the assembled case is weighed; the cross-reference completes
  the chain.

## 0.1.0 — 2026-08-16 — Initial release

### Added
- **The skill itself: a central national-policy layer** with (1) an edition register and a
  verify-before-citing protocol, and (2) the shared decision-making core (s.38(6)/paras
  2, 12, 48; the para 10–11 presumption with footnotes 7 and 8; para 49 emerging-plan
  weight; para 57 conditions tests; para 58 / CIL reg 122(2) obligations tests). _Why:_
  reviewer feedback — NPPF knowledge distributed across the topic catalogues lets skills
  drift out of sync as editions change; the December 2025 draft revision (final expected
  Summer 2026) restructures the Framework into coded policies, so a single re-verification
  point matters more than ever. Structured as a companion *skill*, not a shared reference
  file, so each skill folder stays individually copyable (repo convention).
- **All citations verified against the live gov.uk text on 16 Aug 2026**, not from memory
  (house rule 3). The verification pass immediately caught a live defect: the transport
  catalogue cited the conditions tests as "para 56" (a December 2023 number) — fixed in the
  same change, which is the skill's rationale demonstrated.
- **Two-layers rule stated in the skill:** this layer owns the shared core + register; the
  topic catalogues own their chapters and professional instruments. _Why:_ prevents the
  duplication this skill exists to remove.
