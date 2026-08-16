# Changelog — ecological-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

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
