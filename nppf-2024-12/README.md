# Archived skills — December 2024 NPPF edition

**Frozen snapshot.** These are the nine NPPF-dependent skills exactly as they stood before
the repository was re-mapped to the 17 August 2026 coded-policies NPPF (issue #16 /
PR #21) — i.e. as written for the **December 2024 NPPF** (paragraph-numbered, in force
12 December 2024 to 16 August 2026). Snapshot taken from commit `eadf859`; the only
changes made to the frozen content are the `-nppf-2024-12` name suffix and the "ARCHIVED"
description prefix in each `SKILL.md`, to prevent collisions with the current skills.

> **Not for live applications.** Applications determined from 17 August 2026 are decided
> under the current NPPF — use the current skills in the repository root for those, even
> when older documents in the case cite old paragraph numbers (the current
> `national-planning-policy` skill carries a December 2024 → August 2026 crosswalk for
> exactly that situation).

## When these archived skills are the right tool

- Retrospective analysis of applications or appeals **decided before 17 August 2026**,
  in the framework the decision-maker actually applied.
- Understanding or checking a pre-August-2026 officer report, decision notice, or
  inspector decision on its own terms.
- Era-pinned test fixtures and academic comparison of the two frameworks.

## How they are invoked

Only on an **explicit** request to work under the December 2024 framework, and only after
confirming that is what the user wants — the rule lives in the current
`national-planning-policy` skill. An incidental mention of old paragraph numbers is not a
request to use these skills. Any output produced with them must say clearly that it cites
a superseded framework.

## Frozen means frozen

- Nothing here is maintained: no re-mapping, no fix backports. Known artefact: this
  snapshot predates the output-style discipline added under issue #22, so drafted output
  may show the older long-paragraph style.
- Future NPPF editions follow the same pattern: snapshot the then-current skills into a
  new `nppf-YYYY-MM/` directory **before** re-mapping (see the house rule in
  `../CLAUDE.md`).

The excluded skills: `planning-document-search` is edition-neutral (use the live copy);
`appeal-precedent-analysis` post-dates the re-map and has no December 2024 edition.
