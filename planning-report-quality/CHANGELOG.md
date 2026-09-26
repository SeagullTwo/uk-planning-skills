# Changelog — planning-report-quality

## Unreleased

### Added — a policy verdict must quote the policy (#64)

Step 1 now requires the "source checked" quote for a **policy citation** to come from the
**primary text** — Framework, PPG page, development plan — and states that a skill summary,
a crosswalk or any secondary source is not a source of record. Where the primary text was
not consulted the verdict is *unverifiable on the file*, not *incorrect*.

_Why:_ in use, two Severity A findings against an officer report were both wrong, and both
traced to the same root: the source quote settling a policy question was
`national-planning-policy`'s one-line summary rather than the policy. One of those summaries
dropped the sentence that reversed it (fixed separately under #62). A summary is a
compression and a compression can invert what it compresses, so no amount of care in reading
the summary would have caught it — the rule has to be about *which document you open*. The
step also now says to read the whole policy rather than the sentence that answers the
question, because that is the specific shape the failure took.

### Added — steelman before recording a determinative error (#64)

Every `incorrect` × `determinative` verdict must carry one sentence giving the strongest
reading on which the author would be right, and the reason it fails — both in the output.
Cannot write the second half, cannot record the verdict.

_Why:_ the Standpoint section already said a sound report can support a decision you
disagree with, but **nothing in the method operationalised it**. Every step invited a defect
to be recorded and no step asked whether the author might be right, which is a method
optimised for defect discovery — and its errors are not randomly distributed, they all point
at the author. The run that prompted this produced three wrong findings, three in the same
direction, none caught by the skill's own checks. The steelman is deliberately placed at the
highest-severity verdict only: it is cheap, it is the step a good opponent performs anyway,
and it is where a false positive costs the user most.

### Added — the counts table carries the other direction (#64)

New row: **claims tested and discharged** — checked against primary source and found
correct, particularly any the pass initially suspected and then cleared. "How to read these
numbers" now says a pass with many load-bearing errors and nothing discharged has probably
not tested in both directions.

_Why:_ the output format could only record defects, so a pass that verified the author was
right had no way to say so and nothing to show for the work. That also removed the only
available signal that a pass had gone one-eyed.

### Changed — Limits states the directional bias (#64)

_Why:_ the existing limits were honest about materiality being opinion but silent on the
skew, and the output of this skill goes to planning committees under a heading saying the
officer's reasoning is defective. A false positive there spends the user's credibility the
moment someone opens the Framework, so the reader needs to be told the error count is a list
to verify rather than a score.

## Moved to this repo — 17 September 2026

### Changed
- **Moved from the gated `uk-advanced-planning-skills` repo and relicensed MIT.** _Why:_ it
  moved with `committee-pack-review`, which hands flagged items to it. A pack review that
  says "this report warrants a full audit" and has nowhere to send the reader is a dead end
  at exactly the point the work gets serious, so the pair had to land on the same side of the
  split as the skill that escalates to them.

- **References to skills that stayed gated were removed, not left dangling.** _Why:_ a public
  skill pointing at skills a reader cannot obtain reads as a paywall inside the method. The
  dependency blocks now name only skills in this repo, and `planning-document-search` is
  named where retrieving the report and the documents it relies on was previously assumed.

## [initial] — 2026-08-29

### Added
- **New skill: claim-by-claim measurement of a written planning assessment.** Four axes —
  accuracy, materiality, weight, load-bearing — plus a separate omissions pass. _Why:_ the
  toolkit could assess a scheme against policy, but had no way to assess whether an
  *assessment* of that scheme was any good. That gap was filled ad hoc
  each time it came up, which is how the same conflations kept recurring.

### Design decisions

- **The four axes map to grounds of challenge, not to a bespoke rubric.** Material error of
  fact, immaterial consideration taken into account, conclusion unsupported by evidence, and
  failure to take a material consideration into account. _Why:_ it gives the numbers an
  external referent. "These are the ways a report gets quashed, counted" answers the
  where-did-this-come-from question in a way "our five dimensions out of five" does not.

- **Accuracy and materiality are never combined.** _Why:_ source research produced a single
  precision figure of 0.51 for work that was 80% accurate — the difference being observations
  that were true but immaterial, counted identically with observations that were wrong. Two
  different failings reported as one number, and the number described the author unfairly.
  In planning practice, identifying a true point is never itself a fault; whether it carries
  weight is a later and separate judgement.

- **No composite score, and no plan to add one.** _Why:_ a composite recombines exactly what
  the axes separate. Where one number is needed, the load-bearing error count is a count of
  quotable things rather than an average, and it can be verified by reading a handful of rows.

- **Unevidenced assertions count against accuracy.** _Why:_ an assertion the file does not
  support is not before the decision-maker and cannot be checked by a reader. That a human
  author knows something from experience explains why the gap arises; it does not make the
  gap harmless. Recorded because the alternative was actively argued for and rejected: in
  testing, one author's score moved from 96% to 80% on this decision alone, and the lower
  figure is the truer one.

- **Judgements get no accuracy verdict.** _Why:_ a judgement can be reasoned or unreasoned,
  never correct or incorrect. Testing one for truth is a category error, and it is the most
  common way a review of an assessment goes wrong — the reviewer demands proof of something
  that was never a matter of proof and reports its absence as a defect.

- **The tests never short-circuit.** A claim failing accuracy still receives materiality,
  weight and load-bearing verdicts. _Why:_ the case that matters most is a wrong claim the
  recommendation depends on, and dropping failed claims out of the pipeline is precisely what
  hides it.

- **The enumeration rule is stated in the skill and repeated in the output.** _Why:_ "claims
  tested" is itself a judgement. Two assessors extract different denominators from the same
  report, and rates built on unstated denominators look precise while meaning nothing. In
  testing, the same assessor re-reading identical text moved its own denominator by 30%.

- **Scope defaults to the whole report, declared in the output.** _Why:_ errors in the
  description of development and the consultation summary propagate into the assessment. A
  narrower scope is allowed but must be named, and rates across different scopes are not
  comparable.

- **Materiality is labelled opinion, accuracy is labelled measurement.** _Why:_ in source
  testing, accuracy reproduced closely across repeat scoring while the material/immaterial
  boundary moved substantially on identical text. The skill says so rather than presenting
  both at the same confidence.
