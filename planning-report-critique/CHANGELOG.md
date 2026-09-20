# Changelog — planning-report-critique

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
- **New skill: find and rank defects in an assessment someone else wrote**, for a reader
  deciding whether to act. _Why:_ "what is wrong with this report" and "how good is this
  report" are different questions with different readers. A solicitor considering challenge
  wants a short ordered list of things that will stand up; a head of service measuring output
  wants exhaustive rates. Answering both from one skill produced neither well.

### Design decisions

- **Built as a presentation layer over `planning-report-quality`, not as a second
  analysis.** _Why:_ house rule 2, two layers and no duplication. A load-bearing error found
  by the quality pass *is* the most serious item in a critique. Built independently the two
  would drift, and the repo would carry two definitions of "defect".

- **Findings and observations are separated, and every observation must state why it is not
  a finding.** _Why:_ in planning, identifying a true point is never itself a fault —
  relevance and weight are separate judgements made later and by someone else. But a bare
  two-bucket split invites wholesale relabelling that looks disciplined without any thinking
  having happened. Requiring the one-line reason forces the judgement rather than the shuffle.

- **The raise test has three conditions, and the third is the one that does the work.**
  Where the author gave a rational reason for the approach taken, the point has been
  addressed rather than ignored. _Why:_ in testing, a substantial share of asserted defects
  were cases where the report *had* explained itself — why a matter could be conditioned, why
  a survey was needed before rather than after determination — and the critique had not
  registered the explanation.

- **Severity is derived from accuracy × load-bearing, never assigned by feel.** _Why:_ an
  assessor grading severity independently over-grades. In testing, one submission assigned
  four severity-A findings where adjudication supported one. Derivation makes the grade
  reproducible and checkable.

- **`references/conventions-not-defects.md` ships with the skill.** _Why:_ every entry in it
  was asserted as a defect during testing and rejected on adjudication — conditional
  reasoning called circular, orthodox differential treatment called inconsistent, two
  non-contradictory propositions called a contradiction, an authority's statement of its own
  knowledge called unevidenced. Reports are written to professional convention, not to
  formal-logic standards, and this is where that knowledge lives rather than being rediscovered.

- **"The report is sound" is an explicitly valid output.** _Why:_ a critique that
  manufactures findings to look thorough spends the reader's credibility on points that will
  not survive. This mirrors the integrity principle `planning-balance` applies to
  representations.

- **Every finding must state what would cure it.** _Why:_ it is the test of whether the
  finding is real. A defect nobody can articulate a cure for is usually a disagreement about
  judgement wearing a defect's clothes.

- **The summary must name a strength as well as the worst defect.** _Why:_ a critique that
  cannot identify anything the report does well has probably not read it carefully enough to
  be trusted on what it does badly.

- **Explicit prohibition on writing about the author.** _Why:_ this repo produces findings
  about identifiable people's professional work. The reasoning is the subject; competence,
  motive and identity are not.
