# Changelog — ecological-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
- **All NPPF citations re-mapped to the 17 August 2026 edition** (coded policies; natural
  environment = chapter 19, N1–N6), each quote-verified against the official PDF on
  18 August 2026: 193(a) → N2(2); 193(b) → N6(1)(b); 193(c) + fn 70 → N6(2) + fn 62;
  193(d)/192(b) → N2(1); 194–195 + fn 7 → N6(1)(a) + the Annex B "habitats site"
  definition. Touched: `national-guidance.md`, `deficiency-catalogue.md` (F4, H1),
  `objection-template.md` (framework list), `SKILL.md`, `README.md`. _Why:_ the December
  2024 paragraph numbers are superseded — citing them is now exactly the superseded-edition
  defect the skill tells users to challenge. Retrospective (pre-17-Aug-2026) decisions and
  the old→new mapping are owned by the `national-planning-policy` register and its
  crosswalk; this skill cross-references rather than duplicates.
- **Substantive reworkings where the mechanism changed, not just the number:** (1) the
  **Environmental Delivery Plan / nature restoration levy route** (N6(1)(a)(ii) habitats
  sites; N6(1)(b)(iii) SSSIs — Planning and Infrastructure Act 2025 Part 3 now in national
  policy) is flagged wherever the skill argues the LPA "cannot conclude" on a protected
  site (SKILL.md step-2 tests, catalogue G3, national-guidance Part 4): a made EDP with
  the levy committed is an alternative policy route an objection must engage with, though
  the EPS derogation-tests analysis (reg 9(3)/55) is unaffected; (2) the **N2(3) weight
  bar** — new cautions in the BNG deficiency section and template notes: do not build a
  point on a blanket local-plan policy requiring above-statutory BNG (no weight except
  up-to-date policies for specific site allocations), while still holding applicants to
  gains they themselves claimed; (3) the old para-194 "presumption does not apply" framing
  replaced by the refusal-directive mechanism (N6 via S4(2)(c)/S5(2)). _Why:_ presenting
  the new codes as a mere renumbering would misstate the policy — the crosswalk discipline
  is to describe the new mechanism where substance changed.

### Added
- **New N-chapter hooks useful to objectors** recorded in `national-guidance.md`:
  N6(1)(c) (a national decision test for Local Nature Reserves / local wildlife and
  geological sites), N6(3) (policy applies to development outside a designation that
  affects its identified value), N2(1)(f) (swift bricks required by default), N2(1)(g)
  (green infrastructure designed against future failure, with long-term management — a
  LEMP/funding hook). _Why:_ these are new or newly explicit in the August 2026 edition
  and strengthen grounds the catalogue already covers (H2, I1).
- **⏳ flags refreshed, verification dated 18 August 2026:** gov.uk offered the August 2026
  NPPF as **PDF only** at verification (HTML pending); EDP/levy commencement and the list
  of made EDPs must be checked at run time; PPG "natural environment" pages still
  cross-refer to old paragraph numbers (read as N2(2)) pending PPG updates; Ramsar safe
  proposition updated to N6(1)(a) + Annex B. _Why:_ evidence-before-assertion — the
  time-sensitive items changed identity with the new edition and needed re-flagging, not
  deleting.

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
- **Renamed the skill folder and `name` from `ecological-objection` to
  `ecological-representation`.** _Why:_ parity with `transport-representation`, and a
  "representation" is the accurate umbrella term — the skill can conclude *not* to object, or
  support conditions, not only object. The drafting content (objections) is unchanged.
- **"What you need first" now says uploaded/pasted/already-downloaded documents work
  directly, and `planning-document-search` is only needed when the user doesn't have
  them.** _Why:_ the old wording ("get them from the council's planning portal") read as
  an instruction to fetch, risking a retrieval detour when the user has already supplied
  the files; it also completes the retrieval skill's fail-fast handover (stop → download
  manually → feed the files back in here).

## 0.1.0 — 2026-08-14 — Initial release

First public-ready version: a skill that (1) evaluates the ecological evidence submitted
with a UK planning application, (2) maps each deficiency to the national law/policy/
guidance it engages, and (3) drafts a concise objection — or advises that none is
warranted. Structure: `SKILL.md` + `references/` (`deficiency-catalogue.md`,
`national-guidance.md`, `house-style.md`, `objection-template.md`). Key design decisions:

### Added
- **The integrity principle as the skill's spine.** Only object where the evidence is
  genuinely inadequate; treat "don't object" as a valid, valuable output; an objection
  built on presentational faults when the method is sound is vexatious. _Why:_ credibility
  with case officers is the asset — manufacturing weak objections burns it, and the source
  material included a deliberate "no objection" example precisely to make this point.
- **Deficiency catalogue as the evaluation engine.** Recurring, defensible grounds
  (evidence currency, survey method/effort/coverage, deferral, internal inconsistency, BNG
  metric integrity, mitigation & hierarchy, lighting & Habitats Regs, irreplaceable
  habitats, management plans), each with *the tell / why it matters / what it breaches /
  the ask*. _Why:_ turns a fuzzy "critique this" into a repeatable checklist tied to
  citable authority.
- **A verified national-guidance catalogue.** Statute, NPPF (Dec 2024 paragraph numbers),
  PPG, case law, and current professional-guidance editions — **web-verified**, with a
  superseded-edition table and ⏳ flags on time-sensitive items. _Why:_ citing the wrong
  NPPF paragraph or a superseded survey-guidance edition undermines the objection; and
  citing a *superseded* edition is itself a common, valid objection ground, so the current
  editions must be right.
- **House style + annotated template** distilled from a human-edited exemplar: measured
  expert voice, material-considerations-only, quote-the-applicant-against-themselves, the
  "resolve by evidence, not condition" spine, and a numbered summary of requests. _Why:_
  a concise, officer-liftable representation is more effective than a long emotive one.

### Changed
- **Scoped to ecology, England-focused, explicitly not legal advice.** _Why:_ honest
  bounds; transport/heritage/flooding are separate matters, devolved policy differs, and
  the tool must not be mistaken for a solicitor.
- **Habitats Regulations citation precision:** the derogation *duty* is reg 9(3); the
  three derogation *tests* are reg 55. _Why:_ legal accuracy — the two are often conflated,
  and this is a law-facing skill.
- **User-protection disclaimers made explicit:** not legal advice; **no warranty** (output
  "as is"); **human review required before submitting**; and a flag that a UK planning
  representation is normally **published on the council's portal in the submitter's name**
  and kept on the record. _Why:_ the skill drafts something a user may submit to a public
  body — they must review it, expect no guarantee, and understand their name becomes public,
  choosing their personal details accordingly.

### Removed
- **All case- and campaign-specific fingerprints removed from the skill.** Genericized the
  worked example's provenance, the named consultant, the specific Local Plan policy numbers
  (→ generic "Local Plan biodiversity/watercourse/hedgerow policies"), site specifics
  ("plot H4" → "a plot"; "99 dwellings" → "the proposed number of dwellings"), and the
  "cite a named inquiry against the same applicant" framing (kept only as generic *guidance
  to exclude* such framing). _Why:_ the skill must be a reusable, neutral tool that carries
  no trace of the particular objection campaign it was distilled from, and must not
  identify any real dispute, applicant, or consultant.
