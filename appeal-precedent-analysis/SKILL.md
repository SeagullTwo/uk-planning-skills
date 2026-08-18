---
name: appeal-precedent-analysis
description: >-
  Find and apply relevant planning appeal decisions to a UK planning
  application, so a representation can say: "In appeal decision X, the
  Inspector found Y because of Z — the same Z is present here, so consistency
  in decision-making requires Y (or reasons for departing from it)." Works
  from a checked-in corpus of structured precedent records extracted from
  published Planning Inspectorate decision letters, tests each candidate
  precedent for genuine comparability (same determinative issue, comparable
  material circumstances, still-current policy framework), grades its weight,
  surfaces adverse precedents honestly, and drafts the precedent passage for
  the representation skills to use. Run after application-triage and
  policy-compliance-assessment have identified the grounds.
---

# Appeal precedent analysis

Use published appeal decisions as material considerations in a representation on a UK
planning application — properly: tested for comparability, cited by reference with the
decision's own words, and framed through the consistency principle rather than as binding
precedent.

> **Not legal advice. No warranty.** Provided "as is"; **a human must verify every cited
> decision against the published letter before use.** Anything later submitted to a council
> is normally published on its portal in the submitter's name.

## The consistency principle (what a precedent is, legally)

There is no doctrine of binding precedent in planning. A previous appeal decision is a
**material consideration**, and the operative principle is consistency: in *North Wiltshire
DC v Secretary of State for the Environment* (1992) 65 P&CR 137 (Mann LJ at 145), like cases
should be decided in a like manner so that there is consistency in the appellate process —
but the decision-maker must always exercise their own judgment, so a like case may be decided
differently **provided reasons are given**. ⏳ Verify the citation at run time before quoting
it in a submission.

Two consequences drive everything below:

- the persuasive form of the argument is **not** "X decided Y, therefore Y" — it is "X
  decided Y because of Z; Z is present here; deciding differently without addressing X
  would be inconsistent";
- the argument only runs if the cases really are alike **on the point that decided X**, so
  the work of this skill is the comparability test, not the citation.

Inspectors' own practice confirms this (observed across a coded sample of 200 June 2026
decision letters):

- precedents cited without their full facts are dismissed almost as a reflex — "I do not
  have full details of that case before me… each decision is made on its individual merits";
- the precedents that carried weight — in one case "**a material consideration of great
  weight**" — were directly comparable: same street or same site, same issue, same policies,
  quoted from the decision itself;
- councils' own precedent citations are distinguished just as readily, which cuts both ways:
  expect the applicant to do to your precedent what you would do to theirs.

## When to use

- After **application-triage** and **policy-compliance-assessment** have established the
  grounds and the governing policies, to reinforce a ground with decided authority.
- When rebutting an applicant's (or council officer's) reliance on an appeal decision —
  run the same comparability test in reverse to distinguish it.
- When a **prior appeal exists on the appeal site itself or nearby** — always check: a
  same-site decision is the strongest precedent there is, for either side.
- Not useful before the grounds exist: a precedent cannot create a ground, only strengthen
  one.

## What you need first

- The application's facts: proposal, site, constraints, the engaged policies (from
  **policy-compliance-assessment**), and the ground the precedent should support.
- The precedent corpus in [`precedents/`](precedents/) — structured records extracted from
  published decision letters (see the schema in `precedents/README.md`), plus any decision
  the user supplies directly.
- The **national-planning-policy** skill's edition register and crosswalk
  (`references/nppf-crosswalk-2026.md` there) — most stored precedents predate the
  17 August 2026 coded NPPF and cite superseded paragraph numbers.

## Workflow

### Step 1 — Frame the target proposition
State, in one sentence, what the representation needs a precedent **for**: the finding Y
("a full-width box dormer is not subordinate"; "unsecured habitats mitigation bars
permission") and the ground it supports. A precedent search without a target proposition
returns noise.

### Step 2 — Gather candidates
Search the corpus by the frontmatter keys (issue tags, development type, outcome,
constraint context), and check for:

- decisions on the **appeal site itself** or in the same street/settlement (search the
  council's portal and PINS records too — the corpus is a seed, not the universe);
- decisions applying the **same policy or its close analogue** (same wording matters more
  than same council);
- decisions in **both directions** — collect adverse candidates now, not after drafting.

### Step 3 — Test comparability (the Z-test)
For each candidate, answer four questions from the record and, where it matters, the full
decision letter. Details and worked examples: `references/comparability-and-weight.md`.

1. **Was Z determinative in X?** The reasoning must have decided the appeal (or that issue),
   not been an aside. A finding the inspector made *obiter*, or on an issue the appeal did
   not turn on, persuades no one.
2. **Is Z actually present here?** Match the *conditions* the record lists ("applies when"),
   against the application's documents — not the vibe. If the inspector's reasoning relied
   on a site fact (an unlit lane, a screened boundary, a failed marketing campaign), the
   representation must show the same fact with its own evidence.
3. **Is the framework still the one X applied?** Check the record's edition fields against
   the **national-planning-policy** register. A precedent applying a superseded mechanism
   (e.g. the pre-August-2026 "tilted balance") may survive as reasoning or may not survive
   at all — the record's *framework currency* note says which; re-verify at run time.
4. **What distinguishes this case from X?** List the differences the applicant (or officer)
   will raise — the record's "distinguish when" bullets are the starting point. If a
   difference goes to the reason Z operated, the precedent fails; say so and drop it.

### Step 4 — Grade the weight
Grade each surviving precedent so the representation leads with the strongest:

- **Tier 1 — same site** (or a linked/adjoining site): the consistency principle at full
  strength; a decision-maker departing from it must explain why.
- **Tier 2 — same LPA, same policy, comparable context**: strong, especially if recent and
  post-dating the current plan.
- **Tier 3 — same policy wording or national test, elsewhere**: persuasive for how a test
  is applied (e.g. what "subordinate" or "surplus open space" requires), not for outcome.
- **Tier 4 — reasoning only**: use the logic without leaning on the citation.

Recency, procedure (an inquiry decision tested evidence more thoroughly than written
representations), and whether the decision has been judicially considered all adjust the
grade — see `references/comparability-and-weight.md`.

### Step 5 — Face the adverse precedents
Search the corpus (and the same-site history) for decisions pointing the **other way** and
deal with them in the representation, not in the hope no one finds them:

- if distinguishable, distinguish them expressly, on the record's terms;
- if not distinguishable, the ground is weaker than triage thought — report that honestly
  back to the planning-balance step rather than suppressing it.

### Step 6 — Draft the precedent passage and hand off
Draft the passage for the representation skill that owns the ground (heritage, flood,
transport, ecology, or policy-representation). The canonical shape:

1. **the citation** — full published reference, decision date, and site, so the case can be
   pulled up: "Appeal ref ⟨X⟩, ⟨site⟩, decision of ⟨date⟩";
2. **the finding, in the decision's own words** — quote the operative sentences with their
   paragraph numbers; never paraphrase what can be quoted;
3. **the parallel, evidenced** — "the same ⟨Z⟩ arises here: ⟨this application's document,
   paragraph/drawing⟩ shows ⟨fact⟩";
4. **the consistency ask** — "consistency in decision-making requires the same conclusion,
   or reasons for departing from it";
5. **the pre-emption** — one or two sentences answering the obvious distinction before it
   is made.

Attach or link the full decision letter where the portal allows it — the observed failure
mode is the inspector or officer discounting a precedent because its details were not
before them.

## Output format

1. **Precedent match table** — one row per surviving candidate: reference · date · tier ·
   the Y/Z proposition · the matching facts here · the distinctions to pre-empt. Keep each
   cell to one or two short sentences; overflow goes in a bulleted note below the table
   keyed to the reference.
2. **Adverse precedent note** — what was found, and whether it is distinguished or
   concessive; "none found" is stated, not implied.
3. **Drafted precedent passages** — one per ground, in the five-part shape above, ready for
   the representation skill.
4. **Verification note** — which quotes were checked against which letters and when; which
   records carry stale-framework flags needing run-time re-verification.

**Output style.** Enumerations of three or more items go in a bulleted or numbered list,
never strung through a paragraph with semicolons; one point per paragraph, paragraphs
short (see repo house rule 9).

## The precedent corpus (data layer)

Per-decision records live in [`precedents/`](precedents/) — schema, sourcing rules and the
personal-data policy are in `precedents/README.md`. The records are **analysis, not the
decisions themselves**: every quote carries its paragraph number and a verification date,
and the published letter remains the authority — pull it and re-verify before submitting.
To add records (e.g. from a new month's decisions), follow the pipeline in
`precedents/README.md`.

## Reference files

- [`references/comparability-and-weight.md`](references/comparability-and-weight.md) — the
  Z-test in detail, the weight tiers with adjustments, the adverse-precedent duty, drafting
  patterns, and the observed inspector practice this skill is calibrated against.

## Scope and limitations

- **Not legal advice, and no warranty.** Whether a precedent applies is ultimately a matter
  of planning judgment for the decision-maker; contested comparability is a matter for a
  planning professional or solicitor; provided "as is", no outcome guaranteed.
- **Human review is necessary before use.** A person must read every cited decision letter
  in full — the records are extracts, and an unread precedent is a liability, not an asset.
- **England-focused.** Appeal mechanics and the policy framework cited are England's; the
  devolved nations differ — flag and adjust outside England.
- **Evidence-bound.** Quote decisions verbatim with paragraph numbers; never invent, embellish
  or round up a finding. If the record and the letter disagree, the letter wins — fix the
  record.
- **Time-sensitive.** Policy editions turn over (most recently the August 2026 NPPF
  recoding) and decisions can be quashed on legal challenge — re-verify the framework
  currency and, for load-bearing precedents, check the decision still stands. ⏳
- **A precedent strengthens a ground; it does not create one.** If the underlying ground is
  weak, say so — "no sufficiently comparable precedent" is a valid, valuable output.
- **A UK planning representation is public and in the submitter's name** — carry that
  warning through to whichever skill drafts from this analysis.
