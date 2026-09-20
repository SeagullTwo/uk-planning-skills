# Changelog — noise-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the house
rules. The **_Why_** lines record the rationale so a future editor understands the intent.

## Unreleased — third revision, 16 September 2026

Tested against **122 full Planning Inspectorate decision letters** and a fresh currency check of
every instrument the skill cites. The corpus was a **census** of appeals decided January–June
2026 (7,820 decisions, every month complete), filtered to the 323 in which noise was the
determinative issue, and read in full. Method, sourcing and the statistical trap that nearly
went into this revision are recorded at the end of this entry.

### Changed — corrections, where the skill was telling users something the decisions contradict
These come first because they matter more than the additions: each is a place the previous
revision would have led a user to make an argument that loses, or to abandon one that wins.

- **The "environmental health officer is the ally" anchor now says that a no-objection is not
  determinative, and why.** _Why:_ the anchor as drafted invited an objector to give up when
  environmental health had not objected. Across the corpus that is wrong: appeals are regularly
  decided against a development on noise where environmental health raised no objection, and
  inspectors give two reusable reasons — the consultee may have applied a **statutory nuisance**
  test, which is a higher threshold than the planning question about living conditions, and the
  planning judgement belongs to the decision-maker. The relationship is **asymmetric**: an
  objection is powerful, a non-objection is not a bar. The anchor now says so and tells the user
  to test what the consultee actually assessed — commonly plant and internal transmission, not
  people noise, dispersal or loss of respite.

- **D6 split into a *scope* argument and a *performance* argument.** _Why:_ this was the most
  damaging error in the previous revision. It said, of "another regime will deal with it":
  *"Without such evidence, do not run this point."* In practice the argument that succeeds needs
  **no evidence at all** — it is that the other regime asks a different and narrower question
  (licensing is directed at public nuisance, not at securing an acceptable standard of
  residential amenity; statutory nuisance is a higher threshold; permitting regulates the
  installation, not whether the use of land is acceptable). Only the assertion that the regime
  has **failed in this case** needs the "clear evidence to the contrary" standard. The skill was
  warning users off the limb that works. D6 also now records that the point is usually run *by
  the applicant*, so the entry is primarily defensive, and that an absence of formal action
  under another regime is not evidence of no problem while a complaint record is evidence of one.

- **The agent-of-change prohibition narrowed, twice.** _Why:_ "do not cite P4 against a new
  noise-generating use" is right about the **national coded policy**, whose function is to
  protect an established activity — but it was drafted as a blanket rule and two things fall
  outside it. First, the **PPG's "onus on the agent of change"** is a statement about where the
  burden of proof sits, and the agent of change is whoever introduces the change — so it runs in
  **both** directions, and has been applied against a noise generator. Second, **local**
  agent-of-change policies are drafted and applied differently, decision-makers openly disagree
  about whether they reach new noise-generating development, and the direction check therefore
  has to be run against the words of the policy actually cited rather than against the label.
  The blanket rule would have stopped a user making a winning argument.

- **D3's three limbs reordered, and the "permission runs with the land" limb demoted.** _Why:_
  it led the entry, and it appears in **none of the 122 letters**. What decision-makers actually
  act on is that staff cannot control noise **off** the premises, and that a management plan's
  contents — the tone and volume of patrons' conversation, "encouraging" quiet departure — are
  not monitorable or enforceable, with the same objection fatal to a condition requiring the
  plan to be agreed later. The proposition about succession is legally sound and stays, third,
  with a note not to lead with it.

- **B5 re-pitched from "the applicable standard not applied" to "the method is unjustified".**
  _Why:_ the old framing invites an attack that loses. An objection that a named standard should
  have been used and was not is rejected where the consultant took a different but reasoned
  route — measuring the building envelope's actual insulation performance and accounting for the
  source's frequency content, for instance, can be perfectly proper. The deficiency is an
  **unjustified** method. The entry now also distinguishes the instruments' status, because
  **ProPG is not government guidance** and asking for compliance with it as though mandatory
  over-claims.

- **G2 carries two explicit "do not make this attack" warnings** — generic challenges to a
  consultant's competence, and attacks on a report's revision history. _Why:_ both fail
  reliably, and both cost the credibility the specific points depend on. A corrected arithmetic
  error is what competence looks like; a superseded report still being *relied on* is a
  different matter and belongs in E5.

- **E1's care note hardened substantially, and the comparator argument given its own entry
  (E7).** _Why:_ comparator material is the least successful evidence an objector files — it was
  rejected in every attempt across the corpus, usually without its substance being reached. The
  note now requires the document itself to be produced, comparability to be demonstrated
  *before* the comparison is drawn, and E1's predicted-versus-measured-at-the-same-place
  comparison to be distinguished from "here is another site", so it is not dismissed alongside
  them.

- **A direction-of-error check added to the integrity rule.** _Why:_ a genuinely non-obvious
  failure that both objectors and authorities commit — attacking a baseline as understated, when
  a higher baseline makes the development's noise a smaller relative change and helps the
  applicant. The rule is now: work out which way the alleged error moves the answer, and cut the
  point if it moves it in the applicant's favour.

- **The (A)/(B)/(C) classification now states its stage-dependency.** _Why:_ the labels imply
  (B) is the soft option. At application stage it is what it says; **at appeal an unremedied (B)
  is decisive**, because inspectors do not adjourn for better evidence — the burden sits on the
  appellant and an evidential gap is a failure to discharge it. Users should press a (B) with
  that consequence stated, not as a preference for more information.

- **D4 rewritten and strengthened into two limbs.** _Why:_ it was drafted to catch only the case
  where ventilation and overheating are *unassessed*. The decisive holding is stronger and
  different: where the acoustic case **depends** on windows being shut it fails **even where the
  internal target is met**, because the reasoning is about **control, not acoustics** — nobody
  can determine whether an occupier opens a window, and a condition cannot secure it. The entry
  now carries both standard answers to rebut (mechanical ventilation is provided; the occupier
  knew what they were buying) and the cross-check that most often proves it: the applicant's
  **overheating assessment and acoustic assessment assume different window positions**.

- **D5 gains a second failure mode and a stronger framing.** _Why:_ external amenity space
  decides cases **on its own**, with the internal case conceded, and a level at the top of the
  guideline range is treated as marginal rather than compliant — so it is not the makeweight the
  entry implied. The new failure mode is that the acoustic fix ruins the space it protects: a
  barrier tall enough to work can be dominating, and an inner fence subdivides the garden. The
  ask is now usability *after* mitigation, not merely assessment.

- **F2 demoted with a warning not to lead with it.** _Why:_ the absence of engagement with the
  existing operator is a real and common gap in applicants' evidence, and nothing in the corpus
  was decided on it. Where mitigation depends on the existing operator changing how they work,
  the decisive point is the absence of any willingness or mechanism — which is F4.

- **G4 gains a bounded anti-social-behaviour qualification and a note on where the burden
  reverses.** _Why:_ "the clientele" is correctly ruled out as immaterial, but that was
  over-broad. ASB **is** material on a specific framing — that the permission lengthens the
  window in which a documented problem occurs — particularly on police or community-safety
  evidence rather than neighbours' characterisations. Separately, where an **authority** asserts
  a positive need for a restriction beyond the reason it was imposed, the burden is on the
  authority; a user supporting a condition should support it on the ground it was actually
  imposed.

### Added — structural
- **A third direction.** _Why:_ the skill recognised only source (A) and receptor (B). A
  recurring class is **both, internally** — a living room over a neighbour's bedroom, the
  scheme's own parking under its own habitable windows, a shared path past a studio flat's only
  window, communal bin stores, HMO circulation. Section F does not apply and **citing P4 there
  is an error**, because there is no existing activity and no agent of change: the same
  development is on both sides. These attract no noise assessment at all, because assessments
  are commissioned to answer an external question — so the finding is usually that the layout
  has never been assessed for internal transfer.

- **A prior-approval section, placed before the policy material.** _Why:_ this was a correctness
  bug, not a gap. Residential conversions are frequently prior approvals under Class MA, Q or G,
  and on that route **the development plan does not apply** — s.70 of the 1990 Act is not
  engaged, so s.38(6) does not operate and the local plan's noise policies are not the test. The
  skill would have sent a user to cite policy that has no application. The section sets out the
  Class-specific noise tests, the "impractical or undesirable" limb where receptor-side noise
  usually lands, paragraph W's insufficient-information ground, and the scope limit on what can
  be objected to at all.

- **`references/model-conditions.md`.** _Why:_ every **(C)** ask in the catalogue depends on a
  condition, and the skill gave no drafting guidance beyond "be precise". The file records the
  shapes that survive challenge — a physical measure tied to a drawing with a trigger and a
  retention requirement; hours by *area or facility*, by day, with a clearance time and an
  express out-of-hours access prohibition; staff and servicing hours separate from customer
  hours; activity prohibitions where a level cannot control the source; lighting hours separate
  from use hours; plant specification plus verification plus maintenance — and, as importantly,
  what not to ask for: a deferred assessment, a bare numeric limit that has not been shown
  achievable, an "inaudible" standard, a tailpiece, or a trial period without its machinery. It
  also records the most frequent drafting error: **a plant-noise limit does not reach people
  noise**, and accepting one as the answer concedes the case.

### Added — catalogue entries
- **A9** the assessment answers the wrong direction; **A10** only the façade pathway assessed,
  structure-borne and flanking transmission ignored; **A11** area-wide characterisation applied
  to a receptor in a quieter pocket; **A12** enclosure, reflection and the street canyon, and
  the reverse case where activity moves from an enclosed space to an open one.
  _Why A11 in particular:_ "the area is already busy" is the commonest argument applicants run,
  and the commonest way it is defeated is by distinguishing the specific façade from the area's
  designation — a point distinct from A2, because the measurements may be sound and the
  *characterisation* still wrong.
- **B13** the maximum level is a selected rank from the dataset, unexplained. _Why:_ selecting
  the statistic selects the answer, and the sharpest version — a *different* rank for different
  scenarios, with the lower one used for the windows-open case — is visible on the face of the
  document and needs no competing measurement.
- **C9** loss of respite; **C10** the current operator's restraint treated as the level of use;
  **C11** no defined operation, so nothing can be assessed. _Why C9:_ it is the most under-used
  argument available. On an hours application the protected interest is the **predictability**
  of quiet periods, not only the level — harm that no acoustic assessment answers, and that
  needs only the current and proposed hours side by side.
- **D7** neighbours compelled to keep windows shut — the Direction A mirror of D4, which had no
  entry; **D8** mitigation someone else has to maintain; **D9** the mitigation is itself the
  harm. _Why D9:_ the noise case and the design case are assessed by different people in
  different sections of the report, so a barrier that solves the acoustics and wrecks the street
  scene can pass both.
- **E7** the comparator-premises argument and how to defeat it; **E8** "there have been no
  complaints", with the answer in three parts — an absence of complaints is not an absence of
  harm; people do not complain about what is already permitted; and it does not displace the
  decision-maker's duty. _Why E8:_ the middle limb converts the applicant's best point into a
  neutral one on any application to extend hours.
- **G5** the assessment deferred past the grant of permission; **G6** the trial or temporary
  permission. _Why G5 is the most important single addition:_ it was the highest-frequency
  holding in the study and the catalogue had nothing on it, because it is a **sequencing**
  objection and G3 addresses only precision. A condition may be perfectly precise and still
  unlawful here, because the authority cannot know it is capable of being discharged. The entry
  carries the distinction that keeps it honest — deferral *is* proper where the performance
  standard is understood and only workmanship is open.
- **E6** extended with two further contradiction sites: mitigation present in the report and
  absent from the drawings, and the windows-open/windows-shut conflict between the thermal and
  acoustic cases.
- **A3** widened to cover a baseline contaminated by a neighbouring consented source, with
  **"noise creep"** named. _Why:_ naming it is what makes the point land — each permission
  measured against a background raised by the last one is assessed as a smaller change than it
  is, and the ratchet runs one way. A proxy measurement location is recorded as a legitimate
  answer so users do not attack it reflexively.
- **D2** gains the cheapest tell in the catalogue — the applicant's own consultant recommended
  mitigation the application does not include — and the check that a measure *can* be secured at
  all, which it cannot where it lies outside the red line, needs its own permission, or is
  precluded by the application route.
- **The anchors** gain the evidential-burden proposition, promoted to first position, and a
  counterweight to "attack the method": the absence of measurements does not prevent a finding
  of harm, decision-makers decide these cases on their own site-visit observation, and the
  answer to "a site visit is only a snapshot" is evidence that what they will hear is typical.
- **A seven-entry quick index** at the head of the catalogue. _Why:_ the catalogue is now long
  enough that a user could work through it in order and spend their effort on the wrong things.
  Three of the seven need no acoustic competence at all.

### Changed — `national-guidance.md`, currency re-verified 16 September 2026
- **Three citations flagged at the top as discrediting if used:** NPPF paragraph numbers
  (abolished 17 August 2026), **"BS 8233:2026"** (does not exist), and **ETSU-R-97**
  (superseded 19 June 2026 by the DESNZ wind turbine noise guidance). _Why:_ each is a specific,
  checkable error that would let an applicant dismiss a representation without reaching its
  substance, and each was live at the time of writing.
- **The BS 8233 revision resolved.** A draft for public comment issued June 2025, comments closed
  September 2025, the profession objected substantially, and **no revised edition has been
  published**. The note tells the user to cite the 2014 edition, to expect consultants to reason
  from the unpublished draft, and to identify a conclusion that depends on the draft's
  departures as resting on a document that is not the standard.
- **The PPG noise caution upgraded from "stale" to "broken".** Its related-policy references
  still point at 2019 paragraph numbers, against a Framework that has none. The caution now
  separates the guidance's **substance**, which remains operative and is quoted by inspectors,
  from its **signposting**, which locates nothing.
- **An NPSE citation trap recorded.** The phrase "Noise Policy Statement for England" appears
  nowhere in the August 2026 Framework, so NPSE's connection to the SOAEL language now runs only
  through the stale PPG. B10 should therefore be built on **P3(2)(d)** and **Annex B**, with the
  PPG for the hierarchy and NPSE for provenance — an order that does not depend on any one
  instrument surviving the next edition.
- **A further-instruments table added**: BS 5228 (construction and vibration, absent from the
  skill entirely and present in most major applications); the ANC Approved Document O Noise
  Guide and Approved Document O itself, which frame the D4 conflict; ProPG Part 2 for gyms, easy
  to miss because ProPG is treated as a single 2017 document; the joint IOA/CIEH air source heat
  pump advice note; the IOA 2003 pubs-and-clubs guide and the 1995 Pop Code; BS 7445's
  under-review status; BB93 and HTM 08-01 for school and healthcare receptors; and the June 2026
  aviation noise evidence, which moved the annoyance threshold materially.
- **The National Licensing Policy Framework (26 November 2025) added to the licensing
  boundary.** _Why:_ it is more useful to a planning representation than its title suggests — it
  addresses beer gardens and licensed pavement areas directly, applies agent of change within
  licensing, and states that licensing decisions do not undermine planning decisions, which take
  primacy. That is the government's own statement of the **D6 scope argument**, which is better
  than an objector's version of it. The s.182 guidance is flagged as volatile, having moved
  three times in ten months.
- **The people-noise negative re-verified and stated more strongly.** There is still no UK
  standard or national guidance for patron, crowd, outdoor-drinking or beer-garden noise, and
  none was published 2023–2026; BS 4142 expressly excludes entertainment noise and BS 8233
  excludes sources with specific character. _Why it matters:_ the vacuum is filled locally with
  subjective "inaudible" conditions, which is why the catalogue now warns against asking for
  one. What has changed on this topic is the **policy hook** — P4 and the NLPF — not the method,
  which has been static since 2003.
- **A retrieval note**: `www.ioa.org.uk` returns a certificate error and `pub.ioa.org.uk` serves
  the same paths validly. Recorded so nobody clicks through a certificate warning.
- **B12's local-guidance entry gains a provenance caveat.** _Why:_ this qualifies an entry added
  earlier the same day. Local guidance is not all of equal weight — an in-house technical note
  issued by a council department without consultation or adoption may be given only limited
  weight against a well-established national standard. Where the local document is unadopted,
  run the point on the substance of the criterion rather than on the authority's obligation to
  follow its own guidance.

### Method, and a finding that was discarded
- **Corpus.** A census of 7,820 Planning Inspectorate decisions, January–June 2026, every month
  complete and verified against the corpus manifest before use. 651 decisions (8.3%) had noise
  as an issue; **323 (4.1%) had it as the determinative issue** — 275 affecting existing
  neighbours, 50 affecting new occupiers, two both. 122 full decision letters were read: the 19
  concerning patron and outdoor-drinking noise, 53 in which inspectors engaged with the adequacy
  of the noise evidence, and all 50 new-occupier cases.
- **A statistical artefact that was nearly published as a finding, recorded here so a future
  editor does not rediscover it and believe it.** Noise-determinative appeals are dismissed
  **95.4%** of the time against a corpus baseline of 67.7%, and among the 50 new-occupier cases
  there were **zero** allowed. Both look like strong evidence that noise is a powerful ground.
  Neither is. Every determinative issue family runs 96–99% dismissed — character and design
  98.6%, transport 98.5%, ecology 99.2%, occupier conditions 99.4% — because the `determinative`
  coding is taken from **the reason an appeal failed**, so an allowed appeal rarely carries any
  issue coded against it. Noise at 95.4% is at the mildly appellant-*friendly* end of that range.
  Against the relevant base rate, zero allowed in 50 is unremarkable. Reading the letters
  confirmed it independently: several contain inspectors **accepting** the noise case and
  dismissing on something else, and those acceptances are invisible to the tag. **No outcome
  rate from this corpus is quoted anywhere in the skill**, and none should be.
- **Scope limit on the new-occupier material.** 47 of those 50 were minor schemes decided on
  written representations, usually with no acoustic consultant on either side, and the source
  was nearly always a close, uncontrolled commercial neighbour rather than a transport corridor.
  The Direction B material is tuned accordingly; the two majors in the set show the same
  principles applied with far more argument.
- **A tooling failure worth recording.** Git Bash's `grep.exe` was crashing silently on the
  machine used and returning **false negatives** — a sweep that should have hit returned nothing.
  Every search behind this revision was re-run with ripgrep. Treat bare `grep` results on Windows
  as unproven, per house rule F in the companion repo: a tool that reports success is not
  evidence that it worked.

### Sourcing note (third revision)
Patterns were abstracted from published appeal decisions, consultee responses and officer
reports, and generalised to the method. Per house rule 1 **no case reference, operator,
consultant, council, place or person is named anywhere in the skill**, and no entry depends on
any single decision: every one is stated as a pattern with its own policy, standard or guidance
hook, so it stands on its own. Inspectors' formulations informed the drafting but are
paraphrased into general propositions rather than quoted, because a quotation would identify
the decision it came from. Where an entry records that inspectors "routinely" or "reliably"
reach a conclusion, that reflects the corpus reading described above.

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
