# Changelog — flood-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
- **"What you need first" now says uploaded/pasted/already-downloaded documents work
  directly, and `planning-document-search` is only needed when the user doesn't have
  them.** _Why:_ makes explicit that direct document supply is a first-class input, and
  completes the retrieval skill's fail-fast handover (stop → download manually → feed the
  files back in here).

## 0.1.0 — 2026-08-14 — Initial release

First version, built to the same pattern as the other representation skills: (1) evaluate the
flood-risk and drainage evidence, (2) map deficiencies to national policy/guidance and the
tests, and (3) draft a concise representation — or advise that none is warranted. Structure:
`SKILL.md` + `references/` (`deficiency-catalogue.md`, `national-guidance.md`, `house-style.md`,
`objection-template.md`). Key design decisions:

### Added
- **Two anchors as the spine:** *the statutory consultees (Environment Agency, Lead Local Flood
  Authority) are your allies* — read their responses first and build on any objection; and *the
  two hard requirements* — safe for the development's lifetime, and no increase in flood risk
  elsewhere. _Why:_ flood objections succeed when they align with the consultees and press the
  two requirements that policy makes non-negotiable, rather than asserting "it will flood."
- **Lead with the Sequential Test.** _Why:_ it is the first hurdle and can defeat an application
  on its own (reasonably available lower-risk sites), before any site-specific FRA detail.
- **A web-verified guidance catalogue** — the NPPF flood policies and the Sequential/Exception
  Tests, the PPG flood zones and vulnerability classes, the EA/LLFA roles and standing advice,
  climate-change allowances, and the SuDS standards — with time-sensitive items flagged ⏳ (NPPF
  numbering; the Schedule 3 mandatory-SuDS status; climate allowances).
- **Deficiency catalogue** covering the Sequential/Exception Tests, FRA adequacy (all sources,
  current data, climate change, safe access, residual risk), not increasing risk elsewhere
  (floodplain storage, runoff), SuDS and the drainage hierarchy, foul capacity, and consultee
  engagement.
- **House style + annotated template** with the bullet / lettered-sub-point discipline built in
  from the start, so drafts are scannable.

### Changed / Security
- **Scoped to flood risk, England-focused, explicitly not legal advice; no warranty; human
  review required; public-document-in-your-name flag.** _Why:_ the same user-protection
  disclaimers as the other skills.
- **Built generic and public-safe** — no case/campaign/consultant/place fingerprints; local
  policy references left as `[insert …]`. _Why:_ repo house rules.
