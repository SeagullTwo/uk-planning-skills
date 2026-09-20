# Changelog — committee-pack-review

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines are the point: they record the rationale so a future
editor understands the intent.

## Unreleased — discovery and routing, 20 September 2026

From external review of the skill. The diagnosis was that the skill is capable of the work
but cannot be **reached** from the way people actually ask for it, and that is right.

- **The frontmatter description now leads with the user's vocabulary, not the repo's.**
  _Why:_ installed skills trigger from their description, so the description is the discovery
  mechanism and it was written as a summary of what the skill does rather than of when to use
  it. It opened "Forensic scrutiny of a planning committee pack", and **nobody outside this
  repository says "committee pack"**. They say they have a planning application, an officer's
  report, or a committee meeting coming up. The description now carries those phrasings
  explicitly, including the case where someone supplies only a reference and a council.

- **A "When to invoke this skill" section, with the instruction not to wait for the skill to
  be named.** _Why:_ a routing rule inside the skill catches the case where the description
  got it part-way there but the model is deciding between neighbours. The single most useful
  line is the negative one — do not require the user to know the terminology.

- **How to establish committee stage is now specified, not just required.** _Why:_ the review
  said to "first determine whether the application is before a committee" without saying how,
  and an unspecified check produces a guess. Four signals, cheapest first, and the strongest
  is the simplest: **an officer report exists at all.** Delegated decisions do not get one.

- **The routing table has five branches, not two.** _Why:_ "at committee or not" is the wrong
  shape. The case the binary misses is **going to committee with the pack not yet published**,
  which is common and needs the ordinary workflow *now* plus a warning that the speaking
  deadline often falls before the pack can be read. Also: already-decided, which this skill
  handles retrospectively provided it says so, and **cannot tell — ask.** One question beats
  running the wrong workflow against a deadline.

- **A "Working one step at a time" section**, because that is how users ask for this and the
  skill said nothing about it. Do the current step, show the evidence, say what could not be
  established, ask before continuing, and never silently run the whole thing and present a
  conclusion. It also names the four things that must stay visibly apart — the papers, the
  officer's reasoning, this skill's findings, and the user's own position — because **those
  blur fastest in conversation**, where the user's view arrives mid-way and starts colouring
  what gets reported.

- **One exception overrides the pausing: deadlines are surfaced in full at step one.** _Why:_
  a step-by-step run that reaches the speaking cut-off on step five has cost the user the only
  thing they could still act on. This is the skill's own deadline rule applied to the
  conversational mode, and it is the kind of interaction that would otherwise defeat it.

- **The repo README did not list this skill at all**, nor `planning-report-critique` or
  `planning-report-quality`. _Why it matters:_ discovery was failing one level above the
  description — a reader scanning the skills table could not see that committee-stage work was
  covered. All three added, with a "which skill do I start with?" table and a worked example,
  and the documented chain now says in terms that it is for an application you are assessing
  yourself and that the starting point changes once it reaches committee.

## Unreleased — 20 September 2026

Three changes from issue #57.

### Changed — the defect section is now "Possible defects, issues and omissions"

- **"Possible" qualifies the heading; the entries underneath are unchanged and still stated
  flat.** _Why:_ the distinction is the whole point of the change, and the skill says so
  explicitly so a future editor does not soften the findings to match the heading. A finding
  that hedges itself cannot be acted on — "the report arguably may not have fully addressed
  the statutory duty" is unusable at a committee meeting, where the reader has ninety seconds
  to make a point. *Wrong*, *thin* and *missing* stay as they are.

- **What the heading concedes is real, and specific to this document's standing.** _Why:_ the
  review is a reading of the *published* papers by someone who has not seen the whole file,
  has not put any of it to the author, and has had no reply. A point that looks like an
  omission may be answered in a document that was never published; a conflict may have a
  reason the report did not give. Naming that on the heading is what earns the right to state
  each entry plainly underneath — it buys the flatness rather than diluting it.

### Added — offer an HTML report, and use the host's design skill

- **A designed HTML page is now the offered deliverable**, proposed in one line and built on
  a yes rather than assumed. _Why:_ three properties of this output, none decorative. It is
  read under time pressure on a phone the night before a meeting, so the ordering the method
  insists on — deadlines, then triage, then detail — only pays off if the page is navigable.
  It carries a lot of structured material: a triage table, a pivots table, a claims table with
  a four-state tested column, ranked community points each carrying a policy. And it gets
  forwarded to a parish council or a ward member, with the fixed disclaimer travelling with
  it.

- **Two design constraints are stated because they are method, not taste.** _Why:_ the two
  advocacy cases must be given **visually equal weight** — if one reads as the recommendation
  because it is longer or better set, the independence the method spent a whole revision
  establishing is thrown away at the last step. And **no semantic red/green for
  refuse/approve**, which reads as bad/good and converts a neutral document into a
  recommendation. Two distinct hues of equal saturation, neither carrying a verdict.

- **Markdown stays correct** where the reader asks for it, where the host cannot publish a
  page, or where the output is going into a document someone else will edit. _Why:_ the
  format follows the reader, and a skill that can only emit one thing is worse at both.

### Added — say which model produced it, and stop if it is not a frontier model

- **The model is established before the read starts, not named at the end.** _Why:_ this
  skill asks for sustained forensic reading across several hundred pages — holding an
  officer's reasoning against its own appendices, noticing a policy listed and never applied,
  catching that a consultee's summary softens their actual response. That is the work a
  smaller or faster model does worst, and it fails in the specific way that matters here:
  **a confident, well-formed report with findings that are not in the papers.** A thin summary
  would be obvious; fabricated defects are not, because this output's entire form is built to
  look authoritative. Checking at the end would mean the read has already happened.

- **It asks, it does not refuse.** _Why:_ the user may have good reasons and it is their call.
  What they must not do is find out afterwards. One line naming the model and the risk, then
  their decision.

- **Never guess the model; write "model not recorded" instead.** _Why:_ an invented
  provenance line is worse than an absent one, and this is the same rule the skill already
  applies to speaking deadlines — a wrong one is acted on, an absent one is checked.

- **This is the disclaimer's last paragraph made operational.** _Why:_ that paragraph already
  tells the reader output varies with the model, its version and the effort applied. Until now
  nothing in the run recorded which one it had, so the reader was told the output was
  model-dependent and not told what the dependency was.

## Unreleased — first revision, 16–17 September 2026

### Changed — moved to this repo, and relicensed MIT (17 September 2026)

The skill was built in the gated `uk-advanced-planning-skills` repo and moved here before
first release. It is now MIT, like everything else in this repo.

- **`planning-report-critique` and `planning-report-quality` moved with it**, and the
  hand-offs to them are unchanged. _Why:_ this skill's method has a deliberate stopping point
  — triage flags the items that repay a close read, and a full assertion-by-assertion audit of
  one report is a different exercise. That stopping point only works if there is somewhere to
  send the reader. Leaving those two behind would have left the skill saying "this report
  warrants a full audit" in three places with nothing to point at, which is a dead end at
  exactly the moment the work gets serious.

- **The hand-offs to skills that stayed gated were removed rather than left dangling.**
  _Why:_ a public skill that points at skills a reader cannot obtain is worse than one that
  does not point at all — it reads as a paywall inside the method. Those references were
  escalations from triage rather than dependencies, so nothing the skill relies on was lost.

- **Every remaining cross-reference is to a skill in this repo**, and they are real
  dependencies rather than courtesies: `planning-report-critique` and
  `planning-report-quality` for the deep read, `planning-document-search` for the documents a
  report relies on that are not in the pack, `policy-compliance-assessment` for
  development-plan scoring, and `planning-balance` for the balance this skill refuses to
  strike. The hand-off on balance matters most — it is what lets the skill decline to balance
  without leaving the reader stranded.

- **Two rationales that had cited the gated repo's rules now state the principle directly.**
  _Why:_ the rule about never scoring from the applicant's own account of their scheme is
  sound wherever it is written down, and the reasoning has to stand on its own for a reader
  who has never seen the other repo. The base house rules (1, 2, 9) are unchanged and still
  cited by number, because they are this repo's.

- **The committee-platform survey stays; the dataset reference goes.** _Why:_ the finding —
  254 ModernGov, 16 CMIS, 26 unknown out of 296 English planning authorities — is useful and
  public-safe functional coverage data under house rule 1. The CSV it came from lives in the
  other repo, so the reference file now says plainly that **there is no committee-system
  registry here** and that a base URL guessed from a council name is a hypothesis to confirm.
  Naming the gap is more useful than pointing at a file the reader cannot open.

## Unreleased — first revision, 16 September 2026

### Changed — reoriented as forensic scrutiny plus two-way advocacy (17 September 2026)

The skill was drifting toward producing a second, shorter officer report. This revision
fixes the orientation and states it in the skill text rather than leaving it implied.

- **The stance is now stated up front, in its own section: forensic, advocatory, and
  deliberately not balanced.** _Why:_ the previous text described the outputs without ever
  saying what the document is *for*, which left every ambiguous call resolving toward
  even-handed summary — the safest-looking output and the least useful one. The test now
  written into the skill: *if the output could be dropped into the officer report without
  anyone noticing, it has failed.*

- **Balance is explicitly out of scope and handed off.** _Why:_ the reader already has a
  balance. It is in the officer report they are holding, and `policy-compliance-assessment`
  and `planning-balance` produce one properly. Producing a third is duplication in the exact
  form house rule 2 exists to prevent, and it displaces the thing only this skill does.

- **The two cases are now built *independently*, with a stated test.** _Why:_ "the case each
  way" was being written as one balancing exercise under two headings — each list quietly
  conceding to the other, which is how an advocate's case stops being an advocate's case.
  The test — *if you cannot write the approval case without first checking what the refusal
  case said, they are not independent* — is checkable while writing. Both cases now get
  equal effort, neither concedes, and the no-closing-paragraph rule is restated.

- **Scrutiny is explicitly licensed, and the defect taxonomy extended.** _Why:_ the earlier
  text called this section "weaknesses in the report", which reads as optional and invites
  the reviewer to find none. It is now "what the papers do not settle", it is a required
  pass, and it names what to look for: unevidenced assertions, policies cited but never
  applied, internal conflicts between summary and assessment, statutory duties not
  discharged, missing material, and **alternatives the report does not engage with**. Two
  new marks alongside wrong/thin/missing: `conflicting` and `unexamined alternative`.

- **The scheme description is capped at two or three lines.** _Why:_ committee members have
  a fact pack and objectors have read the report. Re-describing the scheme is the single
  easiest way to fill a page with what the reader already has, and it was the section most
  likely to expand.

### Added — a disclaimer at the top of the output, not the foot (17 September 2026)

- **A required disclaimer block, above the deadlines, bold and boxed.** _Why:_ the skill now
  produces a document that **reads with more authority than it has earned**, and that is a
  direct consequence of the reorientation. It quotes the council's own papers back at them,
  names defects, and ends with two cases written at full advocacy strength. A reader arriving
  at "the strongest reasons to refuse are…" without having been told what they are holding
  will take it for a professional opinion. Making the output more useful made this necessary;
  the two changes are the same change.

- **It goes above the deadlines**, which breaks the skill's own "deadlines first" rule, and
  the rule is worth breaking here. _Why:_ the deadline is what a reader can act on, and
  keeping it first has been the ordering principle since the first revision. But a limitation
  a reader meets *after* the conclusions has not limited anything, and the two cases are the
  part most likely to be lifted, forwarded, read aloud at a meeting or quoted in a newsletter.
  The compromise is length: the disclaimer must stay tight enough that the deadline block
  still sits in the first screenful, and this is the one place in the output where brevity
  beats completeness. Full terms are repeated at the foot.

- **The wording is fixed text, supplied by the repo owner, and is reproduced verbatim.** The
  skill now instructs that it must not be paraphrased, summarised, reordered or added to.
  _Why:_ the disclaimer's own last paragraph supplies the argument — *output of any AI skill
  will vary depending on the underlying model used, the model version, and the model effort;
  two runs may produce different output*. If that is true of the document, the one part of it
  that must not vary is the part that states its limits. A disclaimer regenerated from a
  specification each run says something slightly different each run, and the reader has no way
  of knowing which version they were handed. Everything else in the output is the model's to
  compose; this is not, and it is the only block in the skill written as fixed text rather
  than as a list of things to cover.

- **Five short paragraphs**, one of them new to this revision: **model variability, and that
  output is governed by the model provider's terms**. _Why:_ no earlier draft of the
  disclaimer said that the document is not reproducible. It is the limitation most specific to
  how this output is actually made, and it is the one a reader is least likely to infer —
  "machine-generated" reads to most people as *automated*, which implies consistency, rather
  than as *non-deterministic*.

- **Length still matters, and it held.** _Why:_ the block competes with the speaking deadline
  for the reader's first attention, and a disclaimer long enough to skim past has disclaimed
  nothing. The supplied wording is four sentences plus a lede, which is shorter than the
  six-bullet version it replaced.

- **"Findings are about documents, not about people" moved to the foot**, not dropped. _Why:_
  the repo's own framing is that an analysis skill which fails returns a confident, wrong,
  defamatory sentence, so the point is worth making — and saying it is what makes it fair to
  keep using *thin*, *missing* and *internally inconsistent* plainly. But it is guidance on how
  to **read** the findings rather than a limitation on relying on them, and the top block is
  reserved for the second kind.

- **Nothing is said about predetermination or the member code of conduct**, and the skill now
  says so explicitly. _Why:_ members know the rules they are bound by. A skill that recites
  them back reads as patronising, reads as advice it is not giving and is not qualified to
  give, and spends scarce space at the top of the document on the one thing that reader did
  not need from it. The skill's own refusal to advise on the vote stays — it is a rule
  governing the skill, not a caution to print.

- **The snapshot point also stays out of the block**, because the retrieval time and the
  re-check instruction sit immediately below it in the deadlines block, with real times
  attached rather than stated in the abstract.

### Added — the applicant's claims the recommendation rests on (17 September 2026)

- **A required pass and its own output block, between the defects and the community
  comments.** _Why:_ on a major application the officer's conclusions on noise, biodiversity,
  landscape, transport, daylight, drainage, air quality and viability each rest on a document
  the applicant commissioned and paid for. The report cites them and rarely distinguishes
  between a claim a consultee has tested and one it has merely received. The principle that
  you never score from the applicant's own account of their scheme reaches their evidence
  too, not only their description of development. It is not fraud and it is usually not wrong —
  it is **advocacy in technical form**, and the committee is entitled to know which
  conclusions depend on it.

- **Five fields per claim, and the fourth is the one that works.** "Who tested it" has four
  states, not two: independently verified, **accepted without examination** (a "no objection"
  with nothing showing interrogation — silence from a consultee is not endorsement), **hedged
  acceptance** (the consultee's own qualifier: "sufficient information *at this stage*",
  "*appears* to be low risk"), and untested. _Why:_ collapsing these into verified/unverified
  loses the most common case by far, which is a consultee who has looked at a document and
  said something carefully limited about it. Quoting the hedge is quoting the consultee
  telling the reader how far they went.

- **Four named shapes to look for.** _Why:_ they recur and each is checkable in the pack
  without expertise. A **modelled future presented as a finding** (ask for the assumption, not
  the number). A **benefit in the balance that nothing secures** — read the benefit, then look
  for it in the conditions and heads of terms; this is the most common instance and the
  easiest to verify. A **gain deferred to a post-permission condition**, where the benefit is
  counted now and the proof arrives later. And an **impossibility asserted rather than
  demonstrated** — "on-site mitigation is not possible" — which closes off options and is
  usually the applicant's position adopted into the report's voice.

- **Hard limit: do not re-run the technical work.** _Why:_ naming a claim as load-bearing and
  untested is a fact about the papers; declaring the noise assessment wrong or recomputing a
  biodiversity metric is expertise this skill does not have. One wrong technical assertion
  discredits every finding around it. The output stops at the question that would test the
  claim — one question, answerable at the meeting or by a condition.

- **Three or four claims on a major, often none on a householder.** _Why:_ a claim earns its
  place only if the recommendation moves when the claim moves. An inventory of every submitted
  document is not this pass, and it buries the ones that matter — the same failure the triage
  rule exists to prevent, one level down.

- **The three scrutiny sections now have a stated distinction**, written into the skill: a
  **defect** is something the report got wrong, a **pivot** is something the report presents as
  settled that is in fact a judgement, and a **claim** is something the report has taken on
  trust. _Why:_ all three are things the papers do not settle, but they are attributed
  differently and they are answered differently — by correction, by re-weighting, and by
  asking a question. Filing one as another misdirects the reader about who is responsible and
  what would fix it.

### Changed — the per-item section order is now fixed (17 September 2026)

- **Summary → defects → community comments and their policies → the case to approve → the case
  to refuse → what you could do.** _Why:_ the two cases are *built from* everything above them,
  so they come last and a reader can trace every ground back up the page. Putting them higher
  makes the scrutiny read as supporting material for a position already taken. A reader who
  wants only conclusions still reads two sections; a reader who distrusts them checks the two
  above first.

- **The addendum moved up into the summary**, from its old position between the findings and
  the cases. _Why:_ it changes what every section below it is about. Reporting it after the
  defects means the defects were written against a superseded text and the reader has to
  re-read them.

- **The weighting pivots sit inside the defects block rather than in a section of their own.**
  _Why:_ it is the same act of scrutiny. A defect is something the report got wrong; a pivot
  is something the report presents as settled that is in fact a judgement. Both are things the
  papers do not settle, which is what that section is called.

### Verification — the claims pass, re-run on both meetings (17 September 2026)

The pass was applied to all four items and produced load-bearing findings on every one,
including the householder application, which is the case it was least expected to help.

- **On the householder item it found the strongest single finding in that review.** The
  heritage balance weighs harm against two public benefits — removing a car from the street
  and the opportunity for EV charging. The recommended conditions are four: plans, time,
  materials, porous surface. **Neither benefit is secured by anything.** That is checkable in
  the pack in under a minute and it was invisible until the pass asked where the benefits
  were held.
- **The "who tested it" field did the work, exactly as designed.** The most useful rows on the
  major applications were the hedged ones: an ecology adviser accepting "sufficient
  information **at this stage**" for a biodiversity gain deferred to a post-permission
  condition, and an environmental protection officer recording that a location "**appears** to
  be low risk with regard to noise" as the only support for a national-policy compliance
  finding. Neither is a "no objection" and neither is an endorsement; a two-state
  verified/unverified field would have lost both.
- **It found an absent consultee.** On a site inside a National Landscape, where national
  policy fixes substantial weight, the only landscape evidence was the applicant's own
  appraisal and the consultee list contained no landscape adviser at all. That surfaced only
  because the pass asks who tested each claim rather than what the report concluded — the
  report reads as complete.
- **Including a verified claim in each block mattered.** Two rows record evidence a consultee
  genuinely examined. Without them the block reads as a list of complaints about the
  applicant, and the untested rows lose their force by association — the same reason the
  triage rule requires a skip list.
- **The cap held.** Two claims on the householder item, three and four on the majors. An
  earlier draft listing every submitted document buried the EV-charging finding among routine
  documents that nobody disputes.

### Verification — re-run on both test meetings after the reorientation (17 September 2026)

Both meetings were re-worked from the retrieved packs under the new passes. The reorientation
changed the output substantially, and in one case reversed a conclusion:

- **The empty refusal list disappeared.** On the single-item agenda the previous run had
  concluded that no ground carried both a policy anchor and evidence on the file. The new
  passes produced **eight**, none invented: a national policy attaching *substantial weight* to
  a designated landscape, sitting alongside a report that had disapplied the local policy
  delivering it for an inconsistency it never identified; a 13.94% on-site biodiversity net
  loss counted as a benefit because the statutory minimum was bought off site; eight
  development plan policies removed from the decision by assertion; and an addendum reinstating
  in condition reasons the policies the report had discounted. **The earlier "no ground"
  finding was wrong, and it was wrong because the skill was only looking for defects.** This is
  the single strongest argument for the weighting pass: an allocated, consultee-supported
  scheme is exactly the case where a defect-only review reports nothing and a member reading it
  concludes, falsely, that no route exists.

- **The community pass earned its place immediately.** Anchoring objections to named policies
  turned "the site is in an area of outstanding natural beauty" — one line in a summary of
  seven letters — into the item's strongest available refusal ground, because the policy it
  attaches to fixes the weight rather than leaving it at large. On the three-item agenda it
  also surfaced that a parish council's highway objection rested on a primary school opposite
  the site, and that the word "school" appears nowhere in the report's highways assessment.

- **Separating the parish council out mattered on both agendas**, and in opposite directions:
  objecting on one item where the public also objected, and not objecting on another where the
  public did.

- **Two councils, two shapes, both handled**: one live meeting five days ahead with three items
  and no addendum, one retrospective single-item meeting whose update sheet changed three
  conclusions. The retrospective case forced a genuinely different opening section — the
  deadline has passed, and the outcome is *not* in the pack, so the review says so rather than
  inferring it from the recommendation.

### Added — weighting pivots: where a member may lawfully differ (17 September 2026)

- **A required pass (Step 5b) separating weight fixed by law or national policy from weight
  at large, quoting the officer's chosen weight, and saying whether the conclusion turns on
  it.** _Why:_ this was the substantive gap. Members can place different weight on the same
  material considerations and reach a different decision **without anything in the report
  being wrong** — that is the ordinary operation of planning judgement, not an irregularity.
  A review that reports only errors therefore implies, falsely, that a member who finds no
  error has no route to a different decision. Most items have no reportable defect; almost
  all have a pivot.

- **The officer's weighting adjective is quoted, not paraphrased.** _Why:_ "significant
  weight", "limited weight", "moderate adverse" — the adjective *is* the decision, and it is
  the thing a member is being invited to adopt. Paraphrasing it hides what is actually being
  asked of them.

- **A hard limit stated alongside it.** _Why:_ re-weighting a material consideration is open
  to a member; treating an immaterial consideration as material is not, and neither is
  disregarding a weight the law fixes. Without the limit this section reads as an invitation
  to decide on anything at all, which would be both wrong and dangerous to act on. Private
  views, property values, competition and the applicant's identity are named, because they
  are what actually comes up.

- **The empty-list rule now routes through the pivots first.** _Why:_ "no ground is evidenced
  on the file" and "no route to this outcome exists" are different statements, and the skill
  had been writing the first as though it meant the second. Where a pivot is live, the route
  is a re-weighting rather than a defect, and it must be given as one.

### Added — the community's case, worked on its merits (17 September 2026)

- **A required per-item section ranking community representations by planning merit, each
  anchored to a named policy — an adopted plan policy by number, or a national policy by
  code.** _Why:_ this is the most useful thing in the skill that nobody else in the pack is
  doing. Objectors write in ordinary language about real effects; the officer summarises
  them in a paragraph that routinely loses the two or three with genuine planning force. A
  member who thinks the community has a point cannot act on "residents are concerned about
  traffic" — they need the policy number so they can say it out loud in the chamber. An
  entry with no policy number has failed its job.

- **Grouped by concern, not by correspondent, with volume reported separately.** _Why:_
  forty letters making one point is one point. But it is also evidence the point is locally
  contested, which is a different fact and worth reporting as one rather than being netted
  away.

- **Representations with no planning anchor are listed as such, factually, not omitted.**
  _Why:_ an objector told which of their points will not land is better served than one left
  to find out at the meeting, and a member needs to know which concerns the committee is not
  permitted to act on. Silently dropping them looks like agreement.

- **Where the report records an anchored objection without engaging with it, that is a
  finding.** _Why:_ recording and answering are different acts, and the gap between them is
  exactly where a committee's attention is worth spending.

- **Working from the officer's summary alone is a stated coverage limitation.** _Why:_ house
  rule D. The summary is the council's characterisation of the objections, and any ranking
  built on it inherits whatever it left out — which, given the failure mode above, is
  systematically the points with force.

- **A parish or town council is reported separately as a statutory consultee.** _Why:_
  folding it into a volume count of public objections misstates what it is.

### Fixed — no forecasting what an appeal would do (17 September 2026)

- **Every prediction about appeal outcome and costs is removed, and the prohibition is now
  explicit in SKILL.md and the output template.** No "this would not survive an appeal", no
  "an inspector would be likely to", no appeal-risk rating, and no costs consequence attached
  to the condition-cure fact. _Why:_ the skill already refused to predict the committee vote,
  on the grounds that forecasting a decision nobody has taken yet reads as campaign material
  and undermines the analysis around it. It then went on to predict the appeal — the same
  error one step downstream, and a worse one, because a refusal ground labelled as doomed is
  a ground the reader has been steered away from. **How members respond to a ground is theirs
  to determine.** The skill's job is to give them the strongest reasons in each direction and
  what each rests on.

- **The rule as stated: describe the ground, do not forecast its fate.** _Why:_ it draws the
  line where it can actually be applied while writing. "The conservation officer maintains an
  objection" and "this could be secured by condition" are both facts about the ground and stay
  in. "Therefore the council would lose on appeal" is a prediction about a future decision and
  goes out — including when it is true, because it is not the skill's to make.

- **The empty-list wording changed** from "no ground that would survive an appeal" to "no
  ground on these papers carries both a policy anchor and evidence on the file". _Why:_ the
  empty-list rule is worth keeping and the old phrasing was the single most load-bearing
  forecast in the skill. The replacement says the same useful thing as a statement about the
  papers in front of the reader, which is checkable, rather than about a hearing that has not
  happened.

### Added — the case each way (17 September 2026)

- **Each item now carries two lists: "If you are minded to approve, you can do so on the
  basis…" and "If you are minded to refuse, the strongest reasons are…"** _Why:_ a reader
  facing a committee decision needs to know the best argument in each direction. The officer
  report gives them one side properly argued and the other summarised; objectors give them the
  reverse. Nobody sets out both, and that is the most useful thing this skill can produce.

- **Stated flat, without couching or balancing.** _Why:_ hedged output is useless at the
  moment it is needed — the night before a meeting. No "on the one hand", and no closing
  sentence weighing the two lists against each other. The reader weighs them; the skill states
  them.

- **Each ground carries three facts, which are properties of the ground rather than
  caveats**: the policy it hangs on, whether it is evidenced on the file or asserted and by
  whom, and — for a refusal ground — whether a condition could cure it. _Why:_ under s.38(6)
  a ground with no policy anchor is an opinion rather than a reason; "the council's
  conservation officer finds mid-scale harm" and "objectors consider it harmful" are both
  facts and are not the same fact; and whether a condition could deliver the same outcome as a
  refusal is something a member will want to know before choosing between them. The
  condition-cure fact is stated flat, with no consequence attached to it — see **Fixed** below.

- **An empty list must be written as one.** _Why:_ this is the discipline that makes the rest
  credible, and it follows from writing straight rather than cutting against it. The factual
  answer to "the strongest reasons to refuse are…" is sometimes "no ground on these papers
  carries both a policy anchor and evidence on the file" — and the skill must say so as a
  statement about the papers, then say what each candidate ground actually rests on. A skill
  that always finds reasons to refuse is a campaigning tool and will be discounted as one on
  the item where the reasons are real. _(Wording corrected the same day — see **Fixed**
  below. The original rule asked for "there are none that would survive an appeal", which
  is a forecast and is now prohibited.)_

- **Both cases, no recommendation.** _Why:_ setting out both is not choosing between them.
  Which case is better, and which a member should adopt, stays with `councillor-fact-pack`
  under the predetermination constraints this skill does not carry, and predicting the vote
  remains out of scope. Giving both directions equal treatment is what keeps this neutral.

### Verification (17 September 2026)
Re-ran both test meetings with the new section. It produced a refusal case resting on the
council's own specialist maintaining an objection, with a note that the harm cannot be
conditioned away because it arises from the purpose of the development; and, on two other
items, the honest answer that **no candidate refusal ground carried both a policy anchor and
evidence on the file** — one foreclosed by a site allocation with unanimous consultee support,
one where every live point is curable by condition. Producing "there is nothing here" twice out
of four items is the outcome the empty-list rule exists to make possible.

### Changed — fixes from testing against two further meetings (17 September 2026)

The skill was run against two meetings other than the ones it was built from — one live
(five days ahead), one retrospective. It produced usable reviews of both, and falsified three
things it asserted.

- **"The table must contain `none` rows" is qualified.** _Why:_ on the live agenda all three
  items were referred to committee **because** they were contested — the council's trigger is
  a threshold of objections against the officer recommendation — so there was no routine
  business to skip, and the rule as written would have forced a `none` onto a contested item.
  That is worse than having no skip list: it sends the reader past the item the referral
  trigger flagged. The rule now holds for normal agendas and requires an explicit sentence
  where an agenda genuinely has none. The referral reason is also now named as a triage input,
  since it states plainly that the officer and the public disagree.

- **Addenda are no longer identified by keyword.** _Why:_ the second council titles its late
  items an **"Agenda Update Sheet"**, and a search for "addendum" misses it entirely. The
  method is now to work from the document list — anything that is not the frontsheet, pack,
  minutes, map or item report is a candidate, read its first page — with keywords kept as a
  net rather than a filter. The near-miss was luck: "update sheet" happened to be in the
  original word list.

- **An empty document list has at least three causes, and a cancelled meeting is one.** _Why:_
  a third meeting considered for the test turned out to be cancelled. Its page renders
  normally, returns an ordinary success response, lists zero documents, and carries the word
  CANCELLED in the body. A run that reads zero documents as zero business reports that nothing
  is on the agenda — confidently and wrongly. Now a stop-or-ask row distinguishing cancelled,
  not-yet-published, and wrong-committee.

- **The filename convention is not stable, even at one council.** _Why:_ two meetings of the
  same committee a fortnight apart use `06 <ref> Report.pdf` and `04 <ref>.pdf`; an addendum
  at the same council carries no item number at all. The reference file now says to extract
  the item number and reference and treat the type as optional free text, to match on
  reference where the item number is absent, and to reconcile against the agenda frontsheet,
  which is the only reliable statement of what the committee will consider.

- **A combined reports pack is not guaranteed.** One meeting published a frontsheet, minutes,
  one officer report and an update sheet, with no pack at all. "No pack found" is not a
  failure where the item reports are present.

- **Never supply a speaking deadline you do not have.** _Why:_ the deadline was not retrieved
  with the live pack, and the obvious temptation is a plausible-looking date. A wrong deadline
  is acted on; an absent one is checked. Both SKILL.md and the output template now require the
  gap to be stated and the reader sent to the council's page.

- **Councils run more than one planning committee, with separate meeting lists.** Recorded in
  the reference file: checking one and finding nothing says nothing about the other.

### Verification (17 September 2026)
Reviews produced for two meetings on two councils, both retrieved and read end to end. The
method surfaced, among other things, a case where a council's own conservation specialist
maintained an objection after amendment while the report recommended approval without citing
the statutory heritage duty, and a late update sheet that changed a report's amenity
conclusions from "significant harm" to "unacceptable harm" — aligning them with the policy
test the report itself quotes. Both are the kind of finding the skill exists to surface, and
neither is visible from the main reports pack alone.

### Added
- **The skill, scoped at the pack rather than the report.** _Why:_ auditing a single officer
  report is a well-understood exercise, and `councillor-fact-pack` is proposed for committee
  members (issue #39). Neither handles the pack **as an artefact** — finding it on a system
  that is not the planning portal, splitting it, and deciding where a reader's limited
  attention goes. That is the gap, and keeping the skill to it is what stops it duplicating
  work done better elsewhere.

- **Triage as the product, with a required "does not repay scrutiny" section.** _Why:_ the
  normal case is a twelve-item agenda where two items matter. A review that flags everything
  has told the reader nothing and costs them the evening. Making the skip list a mandatory
  output section is what forces the judgement to actually be made — it cannot be quietly
  omitted.

- **Deadlines first in the output, before any analysis.** _Why:_ this skill's deadline is a
  fixed hour, not "before determination", and the speaking registration cut-off usually
  falls days before the meeting. A critique delivered after registration closes is worthless
  however good it is, so the thing the reader can still act on goes at the top. Every other
  skill in these repos can afford to put its conclusions first; this one cannot.

- **Addenda treated as a first-class concern**, with a re-check instruction and a
  requirement to state the time checked. _Why:_ this is the failure the skill most needs to
  prevent. Late items are published separately from the main pack, often the morning of the
  meeting, and can change the officer recommendation outright. A review built on the reports
  pack alone looks complete and can be wrong about what the committee is being asked to
  decide — a silent failure of exactly the kind the companion repos catalogue. The output
  must also distinguish "no addendum as at 09:00" from "we did not look", because a reader
  cannot otherwise tell which they have been given.

- **Two publishing shapes documented, with an instruction to detect rather than assume.**
  _Why:_ the two councils used as test cases run the **same platform** and publish
  differently — one a single combined reports pack requiring a split, the other per-item
  PDFs named `<item no> <application reference> <document type>` with addenda as separate
  visible documents. Testing against two councils on one platform was deliberate, and it
  immediately falsified the assumption that a platform recipe implies a document shape. A
  combined pack usually exists in both shapes, so its presence is not the discriminator —
  the presence of per-item reports is.

- **An item map, reconciled against the agenda frontsheet, before anything is read.**
  _Why:_ a split that runs two reports together loses an item silently, and the review then
  reads as complete while omitting one of the decisions being taken. Reconciling against
  the frontsheet's running order is the cheap guard, and it is the standard discipline for
  any document set assembled from a container.

- **Retrieval guidance in its own reference file**, covering the committee-system platforms
  rather than the planning portal. _Why:_ committee business sits on a democratic-services
  platform — ModernGov at roughly 254 of 296 English planning authorities, CMIS at 16 — on
  a different hostname from the planning portal, and the portal registry in
  `planning-document-search` does
  not cover it. Keeping the recipe in a reference file rather than the skill body matches
  the house rule on method versus data, and leaves room for CMIS and bespoke systems to be
  added as they are worked.

- **No committee-system registry, and the gap flagged rather than papered over.** _Why:_ a
  base URL derived from a council's name is a hypothesis, not a fact. The reference file says
  so and tells a user to confirm one resolves before relying on it — the same distinction
  `planning-document-search`'s portal registry draws between a probed vendor and one
  identified only by fingerprint.

- **An explicit refusal to predict the vote**, and a hand-off to `councillor-fact-pack` for
  anyone wanting advice on how members should decide. _Why:_ predicting an outcome would
  make the output read as campaign material and undermine the parts of it that are analysis.
  Advising a member how to vote raises predetermination questions this skill is not built to
  carry.

### Verification (16 September 2026)
- **ModernGov recipe verified end to end against two councils**: committee list → meeting
  list → meeting documents, with the `documents/g<MeetingId>/` (meeting-level) and
  `documents/s<DocId>/` (item-level) namespaces confirmed on both. Hrefs are relative with
  **no leading slash**, which is recorded because a grep anchored on `/documents/` silently
  returns nothing.
- **Both councils publish future meetings** whose pages resolve before the pack exists, so
  a page loading is not evidence that papers are published. Recorded as a stop-or-ask row.
- CMIS is **untested** and is flagged as such rather than given a speculative recipe.

### Sourcing note
The recipes were verified against live public committee systems at two district councils.
Per house rule 1 the councils appear only as **functional coverage data** — which platform,
which document shapes — in the same way real councils appear in the portal
registry. No application, applicant, officer, member or site is named anywhere in the
skill, and no example depends on a particular case.
