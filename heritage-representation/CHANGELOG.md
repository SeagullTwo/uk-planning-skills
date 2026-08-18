# Changelog — heritage-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed — re-mapped to the NPPF published 17 August 2026 (coded policies HE1–HE10)
- **Every NPPF citation re-mapped from December 2024 paragraph numbers to the August 2026
  policy codes**, quote-verified against the official PDF on 18 August 2026 (gov.uk was
  PDF-only at that date; HTML pending — flagged ⏳): 207→HE5(1); 208→HE5(2)–(4); 209→HE4(3);
  212→HE6(1); 213→HE4(2)+HE6(3)+HE6(6); 214→HE6(5); 215→HE6(4); 216→HE7; 217–218→HE5(5)+HE10.
  _Why:_ the Framework was restructured, not renumbered — a stale paragraph citation is
  exactly the defect the skill criticises applicants for.
- **"Great weight" replaced by "substantial weight" (HE6(1)) throughout** (SKILL.md framing
  points and checklist, deficiency catalogue B1/C2/C3/D1, house style, template, README).
  _Why:_ the phrase "great weight" does not appear in the new edition; quoting it would
  misstate current policy. HE6(3) ("any harm … a matter of considerable importance and
  weight") is cited alongside it, since the new edition writes the *Barnwell Manor*
  formulation into policy.
- **The "less than substantial harm" category reworked out of the method.** The Aug 2026
  edition abolishes the two-category gateway: HE6(4) weighs *any* harm against public
  benefits; only the newly *defined* substantial-harm threshold — harm that would "seriously
  affect a key element of the asset's significance" (HE5(2)(c)) — switches in the stricter
  HE6(5) test. The framing points now read "harm below the substantial threshold is not
  neutral"; catalogue C1 adds the failure-to-classify deficiency (HE5(2) requires the effect
  to be classed positive / no effect / harm / total loss) and drops the pre-2026 judicial
  "vitiated or very much reduced" gloss in favour of the policy definition; the worked
  example's harm point was rewritten to the new mechanism. _Why:_ this is a change in how a
  heritage objection is argued, not just cited — presenting HE6(4) as a renumbered para 215
  would rebuild the abolished gateway.
- **Case-law framework hooks annotated** (statute and holdings untouched): *Bramshill* and
  *Forge Field* are keyed to the abolished category label — notes explain the surviving
  principle maps onto HE6(1)/(3)–(4); *Mordue*'s "works through the NPPF paragraphs" now means
  applying HE4–HE10 (or the old edition for pre-17-Aug-2026 decisions). _Why:_ the cases
  remain good law on the s.66/s.72 duties, but citing them in the old vocabulary against the
  new Framework invites the response that the category no longer exists.
- **Retrospective rule cross-referenced, not duplicated:** decisions made before 17 August
  2026 are read against the edition in force at determination — pointers added (SKILL.md
  Step 3, catalogue vocabulary note and new entry C3a, template notes, README, catalogue
  header) to the national-planning-policy skill's edition register and
  `references/nppf-crosswalk-2026.md`, which own the rule. _Why:_ two-layers house rule.

### Added — new-edition material with no Dec 2024 predecessor
- **Catalogue C3a — assessment drafted against a superseded edition** (either direction).
  _Why:_ for months after a republish, Heritage Statements argued under the wrong framework
  will be common, and a stale policy basis is itself a defensible deficiency.
- **New Framework hooks now catalogued:** HE4(4) (enabling development, formerly PPG/GPA4
  only); HE5(3) (effect on significance, not scale — answers "it's only a small scheme");
  HE5(4) (decision-maker must be satisfied the assessment is accurate); HE6(2)/HE7(1)
  (positive effects to be supported); HE7(3) (substantial harm/total loss test for
  non-designated assets); HE8 (World Heritage Sites); HE9 (conservation-area decisions,
  positive contributors — E2's policy hook); HE10(3) (statues/memorials); the HE1–HE3
  plan-making layer; the HE6(5)/S4(2)(c) refusal-directive interaction with the presumption.
- **Two vocabulary/nuance flags:** HE6(4) now *names* example public benefits (vacant
  listed-building reuse; energy efficiency and low-carbon heating) — D1 tells the drafter to
  contest their evidence and weight, not their status; and HE10(1)(b) softens "should not be
  a factor" to "should not be a **decisive** factor" for preservation by record — F2 and the
  catalogue quote the new wording. _Why:_ both are traps for an objection drafted from the
  old text.
- **Concepts with no successor flagged:** "optimum viable use" no longer appears in the NPPF
  (PPG-only — Part 3 note, ⏳ PPG pages may lag the new codes); the old para 215 wording that
  named it is gone. Historic England guidance still using the old vocabulary flagged ⏳ in
  Part 6.

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

First version, built to the same pattern as the ecological- and transport-representation
skills: (1) evaluate the heritage evidence, (2) map deficiencies to the statutory duties and
national policy/guidance, and (3) draft a concise representation — or advise that none is
warranted. Structure: `SKILL.md` + `references/` (`deficiency-catalogue.md`,
`national-guidance.md`, `house-style.md`, `objection-template.md`). Key design decisions:

### Added
- **The two heritage framing points as the spine:** *the level of harm drives the test*
  (substantial vs less-than-substantial), and *"less than substantial" is not "neutral"* (the
  statutory duties require considerable importance and weight; the NPPF requires great weight).
  _Why:_ these are the two things applicants and officer reports most often get wrong, and
  where a well-pitched representation has the most leverage.
- **A web-verified guidance catalogue** — the LB & CA Act 1990 duties (ss.66/72 verbatim), the
  NPPF Chapter 16 harm tests **with the Dec 2024 +13 renumbering flagged**, the PPG, Historic
  England GPA/HEAN guidance (with the setting method), and the case law (*Barnwell Manor*,
  *Mordue*, *Palmer*, *Bramshill*, *South Lakeland*). _Why:_ heritage turns on the precise
  statutory duty and the correct harm test; citing the wrong paragraph or missing the "great
  weight" duty loses the point. Time-sensitive items (NPPF under revision; two case citations
  to confirm) are flagged ⏳.
- **Deficiency catalogue** covering significance (assessed, and proportionately, incl.
  setting/group value), harm characterisation, the statutory-weight and public-benefit balance,
  conservation-area preserve-or-enhance, archaeology, and consultee engagement.
- **House style + annotated template** with the bullet / lettered-sub-point discipline built in
  from the start (learned from the transport skill), so drafts are scannable.

### Changed / Security
- **Scoped to heritage, England-focused, explicitly not legal advice; no warranty; human
  review required; public-document-in-your-name flag.** _Why:_ the same user-protection
  disclaimers as the other skills.
- **Built generic and public-safe** — no case/campaign/consultant/place fingerprints; local
  policy references left as `[insert …]`. _Why:_ repo house rules.
