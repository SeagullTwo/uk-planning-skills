# Changelog — noise-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the house
rules. The **_Why_** lines record the rationale so a future editor understands the intent.

## Unreleased — first revision, 1 September 2026

### Added
- **The skill, in the standard topic-representation shape**: `SKILL.md` plus
  `references/{deficiency-catalogue, national-guidance, house-style, objection-template}.md`.
  _Why:_ noise and residential amenity were the largest gap in the repo — the triage skill
  listed "noise and disturbance" among the considerations with **no** dedicated skill, while
  being one of the commonest grounds a member of the public actually has. Matching the
  established shape (rather than inventing a new one) keeps the chain
  document-search → triage → topic skill → planning-balance working without special cases.

- **Two explicit directions, established before anything else.** **Direction A** — the
  development is the noise *source*; **Direction B** — the development is the *receptor*. The
  SKILL.md leads with it, the catalogue confines its agent-of-change section (F) to Direction
  B, and the README repeats the warning. _Why:_ this is the single most consequential framing
  error in noise objections. NPPF **P4** protects *existing* activities from restriction by
  *new* development, so an objector complaining about a new noise-generating use next door who
  cites the agent-of-change principle is citing the policy that protects the applicant. The two
  directions also engage genuinely different evidence bases (BS 4142 and character-of-source
  reasoning versus BS 8233 / ProPG / the AVO Guide), so a skill that blurred them would give
  bad advice in both.

- **A deficiency catalogue organised by where assessments actually fail** — A scope and
  baseline, B method and metrics, C operation and worst case, D mitigation and control, E
  evidence and credibility, F agent of change, G procedure and conditions. _Why:_ the sibling
  skills organise by policy test, which works where the policy has discrete gateways (the flood
  Sequential/Exception Tests, the heritage harm categories). Noise policy has no such gateways
  — **P3** states one unacceptability test — so organising by *test* would produce a single
  undifferentiated list. Organising by the stage of the assessment at which the error occurs
  matches how the documents are actually read, and lets the user work through a report in
  order.

- **"Attack the method, not the decibel" as the framing rule.** _Why:_ an objector has no
  measurements and cannot out-argue a consultant on level. The defensible, and repeatedly
  successful, ground is that the assessment does not answer the question the policy asks. This
  also keeps the skill inside its competence: it critiques someone else's acoustics and is
  expressly barred (SKILL.md, Scope) from producing, estimating or "correcting" decibel figures.

- **B10 — no LOAEL/SOAEL identified — as a first-class deficiency.** _Why:_ the August 2026
  Framework puts the effect-level language **into policy**: P3(2)(d) requires that development
  "not result in levels of noise exposure which would have a **significant observed adverse
  effect**", and Annex B defines the significant observed adverse effect level. That converts
  what used to be a PPG/NPSE methodological expectation into a policy test an assessment can be
  shown to have failed to address, on the face of the document. It is the strongest new hook
  the edition change created for this topic.

- **B9 — uncertainty exceeding the margin — and E1 — predicted versus actual.** _Why:_ these
  are the two points a lay objector can make from documents alone, without competing
  measurements. B9 is made entirely from the applicant's own report. E1 uses the applicant's
  own predictions at earlier sites against their own later measurements, which is evidence
  rather than argument. E1 carries an explicit like-for-like caution because a mismatched
  comparison is worse than no comparison.

- **An explicit (A)/(B)/(C) classification of every point**, carried through the catalogue and
  the template. _Why:_ adopted from `transport-representation`, where it prevents the classic
  credibility failure of asking for refusal on evidence that only supports "not yet
  determinable". It matters more here, not less: most noise findings are **(B)**, and noise is
  unusually amenable to **(C)** — hours, capacity, boundary limits, plant specifications and
  verification testing are all precisely conditionable.

- **An honest treatment of the other-regimes assumption (D6, and framing rule 2).** _Why:_
  P3(3) and DM7(1) direct the decision-maker to assume separate regimes operate effectively
  unless there is *clear evidence to the contrary*. A skill that encouraged "environmental
  health can deal with it later" arguments would send users into a directly adverse policy. The
  entry therefore states the rule against the user first, then sets out exactly what rebuts it
  (complaint history, unresolved enforcement, breached conditions, a consultee saying the
  controls have not worked) and says not to run the point without that evidence.

- **D3 — reliance on operator management measures — with the two-limb answer.** _Why:_
  permission runs with the land and not the operator, so measures depending on a particular
  operator's practices do not bind the use; and DM6(1)(c) requires conditions precise enough to
  be enforced. Framing the ask as "convert the commitment into an enforceable condition" is both
  more likely to succeed than seeking refusal and more useful to the case officer.

- **A materiality guard in the house style and in Step 5.** The skill explicitly rules out
  objections to the clientele a use attracts, the operator's identity or conduct, competition
  and property values. _Why:_ noise objections fail on tone more often than on substance, and
  these are the specific non-material lines that most often creep into them. Ruling them out in
  the drafting instructions — not merely in a limitations section — is what keeps them out of
  the output.

- **"Watch the ratchet" as the third framing rule**, pointing at
  `application-triage/references/amendment-applications.md`. _Why:_ noise-generating uses are
  characteristically expanded an increment at a time — a temporary permission made permanent, a
  capacity increase, an hour at a time, a condition varied — and each increment is assessed
  against a baseline that already includes the last one. The cumulative read is where that is
  caught, and the method already exists in the repo rather than needing restating here.

- **A licensing boundary that signposts and stops.** _Why:_ noise disturbance is often live in
  both regimes at once, and users will arrive with both in mind. But the Licensing Act 2003 has
  different objectives, parties, deadlines and procedure, and this is a planning-skills repo —
  so the skill names the boundary, tells the user a parallel application may exist, points them
  at the licensing authority, and does not attempt to draft for that regime.

### Verification (1 September 2026)
- **All NPPF citations quote-verified against the 17 August 2026 edition** (official PDF;
  gov.uk still PDF-only, HTML accessible version pending ⏳). Noise sits in **Chapter 17,
  "Pollution, public protection and security"** — **P3** (living conditions and pollution),
  **P4** (impact of development on existing activities / agent of change), with **P3(3)** and
  **DM7** on other regimes, **DM6(1)** on conditions, **DM2** and **Annex C** on information
  requirements, **DP3(2)(b)** on overheating, and **Annex B** for the SOAEL definition. _Why:_
  every pre-August-2026 paragraph number for noise (191–194 in December 2024; 185/187 in 2021;
  123 in 2012) is stale, and those numbers are exactly what the officer reports, consultee
  responses and appeal decisions a user brings will contain — so the catalogue has to translate
  rather than repeat them.
- **S4(2)(c) checked, and the negative recorded in `national-guidance.md`.** Neither P3 nor P4
  is among the national decision-making policies that direct refusal in specific circumstances
  (checked across the whole August 2026 text, not just Chapter 17), so inside a settlement a
  noise objection runs on P3's unacceptability language and the development plan, not on a
  policy-level refusal trigger. _Why:_ the transport skill can lean on TR6(4) as a refusal
  directive; a future editor might assume noise has an equivalent, and it does not. Recording
  the absence prevents an over-pitched (A). The same check found the one route that **is**
  available — **DP3(3)** is a refusal directive, so a noise failing that is also a design or
  liveability failing (D4, the closed-windows case, against DP3(2)(b) on overheating) can be
  pitched through DP3(3) as well; noted with a caution against stretching it.
- **PPG "Noise" (gov.uk/guidance/noise--2) verified: last updated 22 July 2019**, paragraph IDs
  `30-001-20190722` to `30-017-20190722`. Flagged ⏳ because it pre-dates the coded Framework
  and still cross-refers to superseded paragraph numbers — cite it for substance, not for its
  NPPF references.
- **Standards verified:** BS 4142:2014+A1:2019 current (A1 published 30 June 2019);
  **BS 8233:2014 current but under revision** (BSI project 2023-00544, no revised edition
  published — flagged ⏳); ProPG (May 2017) current; AVO Guide v1.1 (January 2020) current;
  IEMA *Guidelines for Environmental Noise Impact Assessment* v1.2 (November 2014) current
  edition; NPSE (March 2010) not withdrawn; WHO 1999 / 2009 night noise / 2018 European
  guidelines. _Why:_ rule 3 of the house rules — evidence before assertion. The BS 8233
  revision is the item most likely to move first and would change the Direction B internal
  targets, so it is flagged rather than merely cited.
- ***Roper v Tussauds Theme Parks Ltd* [2007] EWHC 624 (Admin)** included with an explicit
  health warning: it is a **statutory nuisance** case, persuasive on the proposition that the
  character of noise matters and not only its absolute level, and is **not** a planning
  authority. _Why:_ it circulates widely in environmental-health consultation responses and
  users will meet it; including it with its limits stated is better than leaving the skill
  silent while the user cites it as though it decided a planning appeal.

### Sourcing note
The catalogue's recurring patterns were abstracted from a body of real consultee responses,
officer reports and appeal decisions on noise assessments for noise-generating uses, and
generalised to the method rather than the case. Per house rule 1, no operator, consultant,
council, application reference, place or person is named anywhere in the skill, and no entry
depends on any particular dispute; every entry is stated as a pattern with its own policy or
standard hook so it stands on its own.
