# Changelog — noise-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the house
rules. The **_Why_** lines record the rationale so a future editor understands the intent.

## Unreleased — second revision, 16 September 2026

### Added
- **E6 — the noise assessment contradicts another document in the same submission**, with the
  five places the contradiction characteristically sits (deliveries and servicing, servicing
  location, access and occupancy, hours, capacity) and a method: tabulate the assumption against
  both documents and quote each. _Why:_ the catalogue was built almost entirely around
  critiquing the acoustic report **against the standards**, which is the part a lay objector is
  least equipped to do. Reading the acoustic report **against the applicant's other documents**
  needs no acoustics at all, and in the source material it produced more findings than any
  single methodological point — an acoustic report assuming one delivery a day where the
  transport statement assumed at least two before 08:30; frontage servicing in the report where
  the drawings put the cellar and kitchen doors on the elevation facing the receptor; an
  outdoor area the planning statement said patrons could not reach, appearing as a source in
  the acoustic report's own appendix. It is promoted to the front of Step 2's cross-cutting
  tests for the same reason. The entry warns against alleging deliberate concealment: the
  discrepancy is the finding, and characterising it costs credibility.

- **A8 — the noise-generating element characterised as ancillary.** _Why:_ scope is settled
  before anything is measured, so a mischaracterisation at this stage removes the principal
  source from the assessment without any argument about decibels ever taking place. This is the
  noise analogue of a rule the companion advanced repo states for commitment analysis — never
  score from the description, because the description is written by the applicant. The entry
  also carries the securing point: ancillary status that matters has to be fixed by condition,
  because a genuinely ancillary use can intensify into a primary one without a further
  application.

- **B11 — external levels reported, internal levels never stated.** _Why:_ the residential
  guideline values are expressed internally, and the step from façade to room depends on an
  assumed attenuation that depends in turn on whether windows are open — so an assessment that
  omits the step has not made the comparison the policy requires, and one that makes it silently
  for the closed-window case has assumed away the ventilation question (**D4**). The entry
  carries an explicit hard limit against the user performing the conversion themselves: the
  skill is barred from producing decibel figures (SKILL.md, Scope), and an objector who supplies
  their own arithmetic hands the applicant a way to dismiss the whole representation. The
  finding is the *absence* of the figure, argued as such.

- **B12 — the authority's own criterion ignored, or borrowed out of its context**, in two
  limbs. _Why:_ the local tier was present in `national-guidance.md` §6 as an instruction to go
  and find the authority's guidance, but had no catalogue entry, so nothing prompted the user to
  check it against the report. Both failures recur and they pull in opposite directions — the
  assessment adopting a more permissive threshold and never mentioning the local document, and
  the assessment citing the authority's own published effect levels where those figures were
  derived from **transport-noise** evidence and are being applied to patron or plant noise. The
  second limb records the rebuttal to expect, because the applicant's technical response in the
  source material ran exactly it: that the local guidance is not expressed as source-specific.
  Silence about provenance does not make a transport-derived criterion applicable to human-source
  noise.

- **C8 — plant assessed as new, and only as new.** _Why:_ predictions rest on manufacturers'
  data for equipment in commissioning condition, while the acoustic features that attract a
  **BS 4142** correction — tonality above all — characteristically emerge as bearings, fan
  mountings and anti-vibration mounts wear. A permission runs for the life of the development,
  not its first month. Pairs with **D2**, since the maintenance regime is the classic measure
  relied on in a conclusion and secured nowhere.

- **A tell under E2: read the contours against the receptor, not against the text.** _Why:_
  where a report contains a contour or iso-line plot, the narrative routinely quotes a level at
  one chosen reception point while a higher contour crosses windows on the same or an adjacent
  elevation. The plot is the applicant's own output and can be checked against the elevations
  with no acoustic competence whatever, which is precisely the kind of finding this catalogue
  should be surfacing.

### Changed
- **Step 2's cross-cutting tests now lead with the cross-document check**, and the
  "what you need first" list adds the **transport statement and planning statement** — named not
  for their own sake but as the documents whose delivery numbers, servicing arrangements,
  capacity and hours the acoustic report has assumed. _Why:_ the previous list gathered the
  acoustic documents thoroughly and the documents that contradict them barely at all, which
  meant the highest-yield check was one the workflow never prompted.

### Sourcing note (second revision)
The additions were abstracted from a further body of real material: an environmental health
consultation response recommending refusal on a licensed-premises change of use, the applicant's
acoustic consultant's technical response to it, the committee report and the decision notice —
read as a complete chain so that the applicant's rebuttals could be seen alongside the original
findings. Per house rule 1 no operator, consultant, council, application reference, place or
person is named, and every entry is stated as a pattern with its own policy, standard or
guidance hook.

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
