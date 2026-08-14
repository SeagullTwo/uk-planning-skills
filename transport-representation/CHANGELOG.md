# Changelog — transport-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## 0.1.0 — 2026-08-14 — Initial release

First version, built to the same pattern as the ecological-objection skill: a skill that
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
