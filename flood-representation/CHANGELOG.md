# Changelog — flood-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
- **The NPPF layer is re-mapped to the 17 August 2026 edition** (coded policies: flood chapter
  18, policies F1–F9, plus Annex F; verified 18 Aug 2026 against the official PDF — gov.uk was
  PDF-only, HTML pending ⏳), replacing the December 2024 paragraph citations (170–182) across
  `national-guidance.md`, `deficiency-catalogue.md`, `objection-template.md`, `house-style.md`,
  `SKILL.md` and `README.md`. Mapping: 170 → chapter 18 objective/F7(1); 173–174 → F5; 175 → F5(2);
  177–179 → F6(1)(b)–(2); 181 → F7(2) (SuDS strand split out to F8); footnote 63 → F4;
  182 → F8; Annex 3 → Annex F table 2. _Why:_ the edition in force changed on 17 Aug 2026;
  citing superseded paragraph numbers is exactly the currency defect the skill tells users to
  spot in others' work. Pre-17-Aug-2026 decisions still read against the old edition — that
  rule and the crosswalk live in the companion `national-planning-policy` skill (referenced,
  not duplicated).
- **Substantive reworkings, not just renumbering** — the new edition changes how a flood
  objection is argued, and the files now describe the new mechanisms. _Why for each:_ the text
  changed in substance, and presenting new codes with old mechanics would misstate policy.
  - **Exception Test: two parts → three criteria, all required (F6(1)(b))** — safety-for-lifetime
    and not-increasing-risk-elsewhere are now separate, independently failable criteria; the
    template's worked example and the catalogue's A2 now argue three lettered criteria.
  - **Zone-incompatibility refusal directive (F6(1)(a))** — an incompatible use in the zone is
    now an outright refusal point before any test; added to the catalogue (A4), the SKILL.md
    key tests and the template notes.
  - **Flood Zone 3 split into 3a/3b in the Framework itself (Annex F table 1)**, with the
    vulnerability classification (table 2) and the compatibility matrix (table 3) moved from
    the PPG into the Framework — Annex F is now the primary citation, and the Flood Map's
    inability to show 3b (SFRA territory) is flagged in SKILL.md.
  - **FRA trigger promoted from footnote 63 to policy F4**, with a wider Zone 1 limb (land
    identified in the SFRA *or on the Flood Map for Planning* as at risk from any source, now
    or future) — catalogue B1 updated.
  - **Sequential test mechanics (F5):** new search-area cap (no wider than the development's
    anticipated catchment), a surface-water-only carve-out via layout/design/mitigation
    (F5(2)(b)(ii)), express exemptions (householder, <250 m² extensions, most changes of use),
    and the allocated-site carve-out and SFRA/Flood-Map evidential basis absorbed into policy.
  - **SuDS must be designed in accordance with the National Standards (F8(2)(a))** — the 2025
    Standards are now hooked directly into the Framework (a stronger citation for drainage
    points), and F8(3) adds a watercourse-enclosure/deculverting policy worth citing against
    culverting-led layouts.
- **PPG flood guidance flagged ⏳ as not yet caught up** with the new edition (old
  paragraph/footnote numbering, two-part Exception Test, tables now in Annex F); its Ref IDs
  are kept for the procedural points that remain PPG-only (defences ignored, "reasonably
  available", applicant demonstrates/LPA decides, 5YHLS irrelevant). _Why:_ the PPG is revised
  page-by-page on its own cycle; the ⏳ discipline keeps the catalogue honest about which layer
  currently says what.

### Changed
- **`national-guidance.md` now defers to the companion `national-planning-policy` skill**
  for the NPPF/PPG edition register, the verify-before-citing protocol, and the shared
  decision-making core; this file keeps only the topic layer. _Why:_ reviewer feedback —
  per-skill NPPF snapshots drift out of sync as editions change; one register, checked
  first, keeps the citations consistent (two-layers house rule).

### Added
- **A/B/C outcome discipline:** every point must be classified as **(A)** demonstrated
  unacceptable impact (refusal reason), **(B)** insufficient evidence to reach the necessary
  conclusion (do-not-determine-yet ask), or **(C)** controllable by condition/obligation
  (mitigation ask) — plus a pre-send checklist item that no point asks for refusal where a
  condition would lawfully and satisfactorily do. _Why:_ reviewer feedback — an inadequate
  assessment does not necessarily mean the development is unacceptable, only that the LPA
  cannot presently be satisfied that it is; conflating the two (or over-asking for refusal
  on conditionable points) is the classic credibility mistake in lay objections.

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
