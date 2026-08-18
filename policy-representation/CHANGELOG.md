# Changelog — policy-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the house
rules. The **_Why_** lines record the rationale so a future editor understands the intent.

## Unreleased

### Changed
- **NPPF hooks updated for the August 2026 coded edition (verified against the official
  PDF, 18 August 2026).** Step 4 now names the presumption as the location-based S3–S6
  scheme, and the "no unverified NPPF paragraph number" rule (Step 4, and
  `references/house-style.md`'s leave-out list) is generalised: any NPPF *paragraph number*
  is now itself a stale-edition tell, since the current edition cites by policy code. The
  objection template's framework bullet now says national policy is cited by policy code as
  a material consideration "alongside" the plan rather than flatly "at less weight". _Why:_
  the 17 August 2026 NPPF replaced paragraph numbers with coded policies, so the drafting
  checkpoints must treat the numbering style itself as a verification signal; and Annex A(2)
  of the new edition gives very limited weight to plan policies materially inconsistent with
  its decision-making policies, making an unqualified "at less weight than the plan" claim in
  a submitted letter capable of being simply wrong — the neutral s.38(6) framing is what the
  companion `national-planning-policy` core supports. Citations themselves stay deferred to
  that skill per the two-layers rule.

## 0.1.0 — 2026-08-17 — Initial release

### Added
- **The skill itself: a policy-led representation drafter taking `policy-compliance-assessment`'s
  scored table as input.** _Why:_ the four topic representation skills draft on a *technical*
  ground (ecology, transport, heritage, flood) and each owns its own deficiency catalogue. None
  of them drafts the **policy case** — conflict with, or accordance with, named adopted
  development-plan policies — which is the strongest kind of point a representation can make and
  the one a case officer must address in the report. Splitting the analysis (previous skill) from
  the drafting (this skill) also lets the user review the policy findings before any letter
  exists.
- **Support as a first-class stance, not an afterthought.** Both skeletons, both worked examples
  and the house-style rules cover support and objection at the same standard. _Why:_ the repo
  had only ever drafted objections, and a support letter is not an objection with the polarity
  flipped — it needs a declaration of interest, an "objections answered" section, and asks for
  conditions that *secure the benefits relied on*. Treating support as a trivial inversion would
  produce the kind of content-free "I think this is a good scheme" letter that councils rightly
  disregard.
- **The stance/evidence split as the governing principle:** the stance is the user's to choose,
  the evidence is not. Includes a mismatch check before drafting and three honest routes when the
  requested stance runs against the analysis (draft the supportable points only; adopt a fitting
  hybrid stance; the opposite stance). _Why:_ a representation belongs to the person submitting
  it, so refusing to draft a stance would be the wrong call — but so would inventing a policy
  case to fit it. Naming the tension and resolving it procedurally keeps both the user's autonomy
  and the repo's evidence discipline intact. It also mirrors the existing skills' posture that
  "don't object" is a valid output, extended to "the policies don't support the letter you want".
- **A rule that no point may overstate its score**, with `?` (cannot be assessed) never written
  as a demonstrated breach and `-1` never written as a mandatory-requirement failure. _Why:_ the
  scoring rubric's honesty is only worth having if it survives the trip into prose; this is where
  a careful analysis would otherwise be inflated at the last step.
- **A "declare an interest" rule for support letters** (applicant, agent, relative, employee,
  prospective purchaser, competitor, campaign involvement) and an explicit instruction to write in
  the user's own words rather than submit a circulated template. _Why:_ undisclosed interests and
  identical form letters are the recognised failure modes of support campaigns, and both get the
  representation discounted when noticed. Declaring the interest costs nothing and protects the
  weight of everything else in the letter.
- **A "the other side, answered" section required in both stances.** _Why:_ a representation that
  argues only one way reads as advocacy. In objection, engaging the claimed benefits (and noting
  which are unsecured or unquantified) is itself strong material; in support, answering the
  objections is the only thing that makes the letter useful to the officer.
- **The three-to-six point limit, with `0`s and peripheral `-1`s dropped.** _Why:_ the analysis is
  deliberately comprehensive; the letter must not be. Filler dilutes the points that decide the
  application, and a padded representation signals that the writer cannot tell which policies
  matter.
- **Development plan policies lead; national policy supports; emerging policy leads only where
  nothing adopted covers the point.** _Why:_ the adopted plan has primacy, and a representation
  that opens on the NPPF while the local plan sits in the background inverts the statutory
  hierarchy — and invites the reply that the writer has not read the plan.
- **The ask table mapped onto `planning-balance`'s outcomes** (grant / grant with conditions /
  refuse / do not determine yet). _Why:_ the two skills must not give the user different
  vocabularies for the same conclusion, and the A/B/C classification already flows from the
  analysis through to the ask.

### Changed
- **No citations of its own: NPPF/PPG references, the presumption and the conditions and
  obligations tests are taken from `national-planning-policy` at run time.** _Why:_ two-layers
  house rule, and the drafting stage is exactly where a stale paragraph number would do the most
  damage — the check list requires run-time verification before the draft leaves the skill.
- **Reference files kept to two (`house-style.md`, `representation-templates.md`) rather than
  cloning the four-file topic-skill layout.** _Why:_ this skill has no deficiency catalogue and no
  topic guidance catalogue to own — the policies come from the council's plan as per-instance data
  and the national layer lives elsewhere, so a `deficiency-catalogue.md` and a
  `national-guidance.md` would have nothing legitimate in them.
- **`representation-templates.md` (plural) rather than the family's `objection-template.md`.**
  _Why:_ the file holds two skeletons and two worked examples because the skill has two stances;
  the singular name would have understated the support path and invited a future editor to treat
  it as secondary.
