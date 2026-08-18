# Changelog — transport-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed — NPPF August 2026 re-mapping (18 August 2026)
- **All NPPF citations re-mapped from December 2024 paragraph numbers to the August 2026
  edition's coded policies** (transport: Chapter 15, TR1–TR8), quote-verified against the
  official PDF on 18 August 2026 (gov.uk page PDF-only at that date; HTML pending ⏳).
  Mapping applied: 109 → chapter objective/TR1/TR3/TR6(2); 111(d) → TR1(1)(d) (plan-making)
  with the decision-side design duty at TR4(1)(a)–(b); 112–113 → TR2 (plan-making) and
  TR4(1)(e) (decisions); 115 → TR3(1)/TR4; 116 → TR6(4); 117 → TR4(1)(a)–(d);
  118 → TR6(1)–(2); conditions six tests (para 57) → DM6(1) (now four limbs). _Why:_ the
  Framework was republished 17 August 2026 with policy codes replacing paragraph numbers;
  citing the old numbers would cite a superseded edition — the exact drift this repo's
  verification discipline exists to prevent. The edition-at-determination rule and the full
  crosswalk live in the companion `national-planning-policy` skill (cross-referenced, not
  duplicated, per the two-layers rule).
- **The severity gateway reworked as a refusal directive, not a renumbering.** Old para 116
  *capped* refusals ("should **only** be prevented or refused on highways grounds if…");
  TR6(4) *directs* them ("Development proposals **should be refused if** they would have a
  severe adverse impact on the transport network (in terms of capacity and congestion,
  including cumulative impacts), or an unacceptable impact on highway safety"), expressly
  covering the construction phase, with "residual … following mitigation" replaced by
  "taking into account any mitigation measures proposed as well as any wider network
  improvements". Every place the skill leant on the old "only … severe" formulation
  (SKILL.md framing rules and A/B/C classification, deficiency-catalogue framing rule,
  house-style "winnable tests", README, objection-template notes, national-guidance Part 1)
  now describes the new mechanism: the evidential bar is unchanged ("severe" still
  undefined, still hard to prove — so the aim-at-the-winnable-tests advice stands), but
  where severity or a safety impact *is* evidenced, TR6(4) directs refusal and the S3–S5
  presumption yields (S4(2)(c)/S5(2)). _Why:_ presenting an inverted mechanism as a mere
  renumbering would misstate how the test is argued — the crosswalk's own discipline
  requires describing the new mechanism where substance changed.
- **New Aug 2026 hooks added to the catalogue:** TR1(2) local significant-movement
  thresholds; TR3(2)/TR1(1)(b) Connectivity Tool "should be used" (turns selective tool use
  into a policy point); TR6(2) travel-plan fallback options (a Travel Plan without a
  fallback mechanism is now non-compliant); TR6(3) assessment checklist (times of day,
  cumulative impacts, multimodal trips); TR4(1)(c) safety of women and girls; TR8 public
  rights of way. _Why:_ these are new decision-side hooks a representation can cite;
  omitting them would leave the catalogue mapped but stale.
- **National Design Guide / National Model Design Code demoted to ⏳-flagged status.**
  The Aug 2026 NPPF no longer names them — its design hook is Manual for Streets + the
  Design and Placemaking PPG (TR4(2) fn 46; DP3 fn 45). Framework-list and mapping text now
  point at the guidance the NPPF actually names; NDG/NMDC kept in Part 7 as extant
  documents (and ATE tool criteria) with a verify-before-citing flag. _Why:_ citing them
  as the NPPF's design references would be evidence-before-assertion failure; but they are
  not withdrawn, so they stay listed with their changed status flagged rather than deleted.

### Fixed
- **Conditions six-tests citation corrected from NPPF para 56 to para 57.** _Why:_ para 56
  was the December 2023 number; the December 2024 edition renumbered the chapter (as this
  file's own edition note records). Caught by the verification pass that built the
  `national-planning-policy` skill — the drift it exists to prevent.

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
- **Enforced the bullet / lettered-sub-point drafting discipline** in `house-style.md` and
  the `objection-template.md` worked example (bulleted framework list; bulleted list of
  omissions in the worked point 1; explicit rule to use `(a)/(b)/(c)` for multi-limb points
  and to avoid semicolon-chained lists). _Why:_ a live test draft came out noticeably denser
  than the ecology skill's output — long paragraphs, semicolon-run lists, no bullets. The
  house style always intended "break dense material out," but the template's worked example
  modelled the denser style, so the skill reproduced it. Fixing the exemplar and the rule
  makes the cleaner layout the default, not a matter of luck.
- **"What you need first" now says uploaded/pasted/already-downloaded documents work
  directly, and `planning-document-search` is only needed when the user doesn't have
  them.** _Why:_ the old wording ("get them from the council's planning portal") read as
  an instruction to fetch, risking a retrieval detour when the user has already supplied
  the files; it also completes the retrieval skill's fail-fast handover (stop → download
  manually → feed the files back in here).

## 0.1.0 — 2026-08-14 — Initial release

First version, built to the same pattern as the ecological-representation skill: a skill that
(1) evaluates the transport/highways evidence submitted with a UK planning application,
(2) maps each deficiency to the national/local transport policy and guidance it engages, and
(3) drafts a concise representation — or advises that none is warranted. Structure:
`SKILL.md` + `references/` (`deficiency-catalogue.md`, `national-guidance.md`,
`house-style.md`, `objection-template.md`). Key design decisions:

### Added
- **The integrity principle plus two transport-specific framing rules.** _Why:_ (a) only
  object where the evidence is genuinely inadequate — "don't object" is a valid output; (b)
  **don't fight the settled parts** — on reserved-matters/s73 the principle and access are
  fixed, so the fight is over *delivery* of the secured mitigation; (c) **pick the winnable
  test** — capacity/congestion refusal needs a "severe" residual cumulative impact (a high
  bar), so aim at sustainable-transport, active-travel, inclusive-design and evidence-
  adequacy grounds instead. These three rules are what keep transport objections credible.
- **Deficiency catalogue** distilled from worked representations: accessibility measured from
  the access not the dwellings; inflated walking benchmarks; no route-quality or external
  connectivity audit; no LTN 1/20 analysis / no forecast flows; public transport unassessed;
  dated/selective trip data and monitoring from part-built sites; cycle parking double-counted
  with car parking; opportunistic and inequitable parking; shared-surface/inclusive-design
  gaps; failure to deliver outline mitigation; s73 loosening of banked infrastructure
  triggers; internal inconsistencies; and the decision-maker's own duty.
- **The "spine" argument as a distinct, reusable ground:** a highway-authority "no objection"
  addresses safety and capacity only; transportational sustainability is the LPA's
  responsibility as decision-maker. _Why:_ this recurs across strong representations and is
  the point most often missing from officer reports.
- **House style + annotated template** matching the ecology skill: measured expert voice,
  material-considerations-only, quote-the-assessment-against-itself, accept the settled parts,
  numbered summary of requests, and an optional "if minded to approve" set of enforceable
  safeguards (milestone-linked caps, works secured up front, monitoring with teeth, committee
  determination).

### Changed / Security
- **Scoped to transport, England-focused, explicitly not legal advice; no warranty; human
  review required; public-document-in-your-name flag.** _Why:_ honest bounds and the same
  user-protection disclaimers carried by the other skills — the tool drafts something a user
  may submit to a public body in their own name.
- **Built generic and public-safe from the start.** No case-, campaign-, consultant- or
  place-specific fingerprints; local policy references left as `[insert …]` placeholders and
  any "named inquiry against the same applicant/consultancy" framing kept only as generic
  *guidance to exclude* it. _Why:_ per the repo house rules, the skill must be a reusable,
  neutral tool that identifies no real dispute, applicant or consultant.
