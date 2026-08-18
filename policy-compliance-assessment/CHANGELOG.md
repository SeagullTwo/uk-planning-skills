# Changelog — policy-compliance-assessment

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the house
rules. The **_Why_** lines record the rationale so a future editor understands the intent.

## 0.1.2 — 2026-08-18 — Evidence disciplines from officer-practice benchmarking

### Added
- **Seven "evidence disciplines" in Step 4**, matching observed officer practice: a
  window-by-window openings audit; a planning-history sweep with delta-assessment against
  any extant fallback permission; amenity geometry measured relative to the neighbour, not
  just the plot; multi-source verification of basic site facts including the council's own
  GIS layers; a representations sweep; treating consultee positions as evidence to
  re-derive rather than conclusions to adopt; and a condition-versus-refusal discipline for
  separable detail and missing documents on minor schemes. _Why:_ five blind runs of this
  skill against decided applications (major and householder) matched the real outcome every
  time, and the residual divergences from the officers' delegated/committee reports were
  concentrated in exactly these habits — a missed new opening that the officer conditioned;
  an unswept history that held the controlling fallback or refusal precedent; a
  procedural gap escalated to a refusal reason the officer handled as a condition.
  Codifying them keeps the next assessment's misses from repeating the benchmarked ones,
  while the existing integrity rules (missing evidence is (B), unsecured mitigation is (C))
  already carry the classification these disciplines feed.

## 0.1.1 — 2026-08-18 — Designated-area scoring uplift

### Changed
- **Conservation areas (and other designated heritage assets) now carry an explicit scoring
  uplift.** Step 4 gains a "designated areas raise the bar" discipline, the rubric's -2
  signals and the -1/-2 calibration test gain a designated-area limb, and "under-scoring a
  designated-area conflict" joins the common-errors list. The rule: measure the **cumulative
  volume of physical change** quantitatively from the drawings, and score a character/scale
  criterion failure in a designated area at full strength rather than discounting it to a
  tension because only one limb fails or each alteration looks modest. Citations (s.66/s.72,
  NPPF heritage tests) stay with `heritage-representation` per the no-duplication rule.
  _Why:_ benchmarking a blind run of this skill against a real decided application showed the
  assessment converging with the officer on the operative policies and outcome but scoring the
  design/overdevelopment conflict on a conservation-area building -1 where the officer ran it
  as a standalone full-strength refusal reason grounded in plot metrics taken off the
  drawings. The user's diagnosis — conservation-area status was underweighted — matches how
  decision-makers actually behave: the statutory duty makes cumulative change in a designated
  area refusal material on its own, and the skill's calibration should reflect observed
  officer practice, not treat the designation as one criterion among many.

## 0.1.0 — 2026-08-17 — Initial release

### Added
- **The skill itself: a policy-compliance stage between triage and drafting** — identify and
  verify the adopted development plan, select the relevant policies, assess each against the
  application, score accordance, and conclude on the plan read as a whole. _Why:_ the repo
  could evaluate a *topic's technical evidence* (the four representation skills) and could
  anticipate the *final balance* (`planning-balance`), but nothing owned the step in between —
  the systematic policy-by-policy assessment that s.38(6) makes the starting point of every
  determination. Triage gestured at it in a four-item step; that is enough to route, not enough
  to do the work.
- **Identifying the adopted development plan as an explicit, gated first step**, with its own
  reference file, a plan register output, and a table of what is *not* the development plan
  (SPDs, design guides, draft plans, council strategies, unmade neighbourhood plans). _Why:_
  "adopted" is a formal term and the most common lay error in this area is assessing against
  the wrong document — a consultation draft, a superseded policy, or an SPD treated as policy.
  An assessment built on the wrong plan is not weak, it is void, and a case officer spots it
  immediately. Gating the workflow on this makes the failure mode hard to reach.
- **The superseded/saved-policies and draft-numbering traps called out explicitly.** _Why:_ a
  new plan usually replaces only *some* of its predecessor's policies, and policy numbers
  routinely change between the publication draft and adoption. Both produce citations that look
  authoritative and are wrong, which is worse than citing nothing.
- **A -2 to +2 accordance score with anchored bands and calibration tests** ("if this were the
  only policy in the plan, would the proposal fail on it?" for -1 versus -2). _Why:_ the score
  makes a long analysis scannable and lets the drafting skill lead on what carries weight. The
  anchors and calibration tests exist because an unanchored scale drifts into expressing
  strength of feeling rather than accordance.
- **A separate `?` "cannot be assessed" flag, explicitly not a negative score**, mapped to the
  repo's **(B)** classification. _Why:_ the repo's central discipline is that an evidence gap
  is not demonstrated harm. Folding "the applicant didn't submit the survey" into a -1 or -2
  would smuggle a (B) into an (A) — the classic credibility mistake the representation skills
  are built to avoid — and it also supports the wrong ask ("refuse" instead of "do not
  determine yet").
- **A weight-tier column kept separate from the score**, with a "reduced weight" tier for
  out-of-date adopted policies and separate tiers for national policy, emerging plans and
  guidance. _Why:_ how a proposal stands against a policy and how much that matters are
  different questions. Merging them into a single number hides exactly the reasoning a decision
  turns on — and an out-of-date policy still generates real conflict, just at less weight, so
  silently discounting it would be as wrong as ignoring its status.
- **A "most important policies for determining the application" flag.** _Why:_ that phrase is
  what the national presumption turns on, so the analysis should surface the set explicitly
  rather than leaving a reader to infer it.
- **An explicit no-aggregation rule, with a worked demonstration.** _Why:_ a -2 to +2 scale
  invites a total or a mean, and the arithmetic actively misleads: eight `+1`s on detailed
  standards and one `-2` on the settlement-boundary policy averages positive while the proposal
  is very likely contrary to the plan as a whole. Recording the temptation and the counter-example
  in the rubric is the only way to stop a future editor "improving" the skill by adding a total.
- **National policy and emerging plans assessed in a second, explicitly lower-weight table.**
  _Why:_ the user requirement is that these are considered but subordinate to the adopted plan;
  putting them in a physically separate table makes the hierarchy visible on the page instead of
  relying on a column a reader may skim past.
- **`references/policy-families.md`, keyed by proposal type, using descriptive family names and
  never example policy numbers.** _Why:_ plans differ in numbering and structure, so the
  transferable knowledge is *which families of policy to expect and when they bite*. Printing
  plausible-looking policy references would invite exactly the from-memory citation the skill
  exists to prevent.
- **Explicit "the plan is silent" and "don't stretch a policy" guidance.** _Why:_ a missing
  policy family is a real finding (and may show the plan is out-of-date on the topic), whereas
  pressing an unrelated policy into service is easy to rebut and costs credibility on the
  policies that do fit.

### Changed
- **No citations of its own: the statutory and NPPF layer defers wholly to
  `national-planning-policy`.** _Why:_ two-layers house rule — this skill owns the *procedure*,
  that skill owns the *instruments* and the current paragraph numbers. It also keeps the skill
  intact through the pending NPPF revision, which will renumber everything.
- **s.38 cited without sub-paragraph precision, with a ⏳ run-time verification flag**, and the
  pending national-development-management-policies and supplementary-plans reforms flagged as
  *not assumed to be in force*. _Why:_ house rule 3 — primary sources were unreachable from the
  build environment (legislation.gov.uk and gov.uk were egress-blocked), so the composition of
  the development plan is stated functionally and flagged for verification rather than pinned to
  subsection letters from memory. A note also warns that older reproductions of s.38 circulating
  online still carry the spent regional-strategy reference.
