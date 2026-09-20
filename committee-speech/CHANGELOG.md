# Changelog — committee-speech

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the house
rules. The **_Why_** lines are the point: they record the rationale so a future editor
understands the intent.

## Unreleased — adopted from a contributed skill, 20 September 2026

Derived from **`planning-committee-speech-builder`**, contributed by **JH** (issue #49). The
speech craft is theirs and survives largely intact; what changed is fit with this repo, and one
thing that had to be removed before it could be public at all.

### Kept, and kept deliberately

These came from the submission and are the reason it was worth adopting. They read like someone
who has watched people speak at a committee and noticed what goes wrong.

- **The framing distinction the whole skill hangs on.** _Why:_ "the objection is read at leisure
  by the officer; the speech is heard once, aloud, under a clock." Everything useful follows —
  select, frame, sequence — and it is stated in one sentence.

- **Respect the room; do not lecture it.** _Why:_ the observation that quoting statute back at
  members, or spelling out appeal costs, reads as preaching and puts backs up. This is real
  practitioner knowledge and it is written down nowhere else in this repo. The reframings are
  kept close to the contributor's own wording, because they are better than a paraphrase.

- **Never let a later speaker claim an earlier speaker's point with "I".** _Why:_ an easy tell
  that a slate was ghost-written, invisible until somebody names it, and it costs credibility at
  the moment an objector can least afford it.

- **Write to the clock**, at 130–150 words a minute with word budgets per slot and the count
  stated in the deliverable. _Why:_ concrete and checkable, and the pace figure is right for a
  nervous member of the public rather than a practised speaker.

- **The ask in the final two sentences.** _Why:_ the best line in the submission — it is the one
  place that is always reached. Somebody has watched a speaker get cut off before their ask.

- **Credibility over volume, and concede what is settled.** _Why:_ matches the integrity posture
  of the rest of the repo, and is the right instinct independently of that: one overstated point
  spoken aloud discredits everything around it.

- **The stage modules**, and the point that arguing at the wrong stage is the commonest and most
  expensive error. _Why:_ correct, and the identification of the unmet-need provisos as the
  strongest objector gateway at outline is a genuinely useful piece of analysis.

- **Cite instruments in full once, then short** — including the subtle point that a written
  "how to use" header must not consume the first mention, because the committee does not hear it.

### Removed — a live application reference and a named council

- **The submission's `description` carried a real, current application reference, and a whole
  section set out one named council's committee tiers, thresholds, slot counts, registration
  deadlines and constitution article, worked through a scheme identifiable from those details.**
  All of it is gone. _Why:_ house rule 1 — never a specific case, and the test is whether it
  would identify a real-world dispute. It would have.

- **It was also a defect on the submission's own terms, and that is the more interesting
  reason.** _Why:_ the skill's own quality check said council facts must match the current
  constitution "not an assumption" — and then supplied exactly the assumption it warned against.
  Constitutions are revised, and the figure that goes stale first is the **registration
  deadline**, which is the one where being wrong costs the user their slot entirely. A worked
  example in a generic skill gets copied as fact.

- **Replaced with a shape, in `references/council-rules.md`, which deliberately contains no
  numbers.** _Why:_ every distinction the original drew is correct and worth keeping — that
  councils run tiered committees with different rules, that the parish slot is usually
  additional, that a cooling-off period must not be asserted unless the constitution contains
  one. Keeping the distinctions and dropping the instances loses nothing and cannot go stale.
  The file also says where to look, which the submission did not.

### Changed — rewired to the skills that actually exist here

- **`planning-objection-builder` does not exist in this repo**; the submission named it three
  times as the source of verified grounds. _Why the instruction survives:_ "compose with the
  written case, do not re-derive it" is right, and the reason given is right — a speech built
  from a fresh read drifts from the objection on file and the officer says so in the reply. Only
  the skill name was wrong. It now points at a table of real skills.

- **`committee-pack-review` is now the primary input**, and it post-dates the submission. _Why:_
  that skill's "if you are minded to refuse" case **is** this skill's ideal input — the strongest
  available grounds, each already carrying a named policy and a note of whether it is evidenced
  or asserted. It also supplies the committee, the slots, the recommendation and the update
  sheet, all of which the submission asked the user to gather by hand. The two chain rather than
  overlap: pack review finds and interrogates, this skill selects and voices.

- **The `docx` output dependency is dropped**, and the deliverable is described by what it has to
  do instead. _Why:_ that skill is not in this repo, and the requirement is really about physical
  form — a speaker stands at a lectern with a printout, so generous spacing and no bullets inside
  spoken text matter more than the file format. Plain text is offered because many councils
  require the words by email in advance.

- **Policy codes are no longer asserted inline.** _Why:_ the submission's framework vocabulary
  was accurate when checked against this repo's own crosswalk — including the distinction that
  development in the *setting* of a protected landscape carries no weight direction, which is an
  easy way to overstate a case aloud. But a skill carrying its own copy of framework citations
  goes stale, which is exactly why `national-planning-policy` holds the edition register and the
  verify-before-citing protocol. Two things are stated flat because they do not move: the
  statutory heritage duty under ss.66 and 72, and development-plan primacy under s.38(6).

### Added

- **A scope section saying, in terms, that this skill argues one side.** _Why:_ it writes
  objector speeches and it should not be coy about it. The justification is that an objector is a
  party, and writing a party's case at their instruction is not the same act as an analysis skill
  quietly taking a side — which is the same ground `policy-representation` stands on. What would
  not be defensible is presenting the output as balanced. **The integrity constraint is what
  makes the advocacy respectable**, so it is stated in the same breath: it will not manufacture a
  ground, and it will say when the honest ask is deferral or conditions rather than refusal.
  Telling a user their case is weaker than they think is the only way the strong points stay
  credible.

- **`planning-balance` wired in as the test of the ask.** _Why:_ the scope section promises the
  skill will say when refusal is not the realistic outcome, and that promise needs a method
  behind it rather than an instinct. `planning-balance` exists to answer exactly that question —
  whether the assembled case supports refusal, deferral or conditions. This skill writes the ask;
  that one tests whether it is the right ask. The submission had no equivalent, because the repo
  it was written against had no equivalent.

- **A late-update-sheet step, which the submission did not have.** _Why:_ this is the gap that
  could actually lose a speech. Late items are published separately, often on the morning, and
  can change the recommendation or answer the ground the speech is built on — and unlike a
  written objection there is no chance to correct it. The practical instruction matters as much
  as the check: **do not rewrite under pressure.** Add one opening sentence acknowledging the
  change, or cut a ground that has been conceded and run short. A speaker reading a hastily
  rewritten script performs worse than one who has practised theirs and adapts a sentence.

- **A role for the parish or town council slot.** _Why:_ the submission mentioned the slot but
  never gave it a job. A parish is a **statutory consultee**, not a member of the public, and its
  standing is the point — it should be given the ground where that standing counts, not spent
  duplicating an objector.

- **Trigger language in the description, and a "when to invoke" list.** _Why:_ installed skills
  trigger from their description, and nobody types "speech builder". They type "what do I say to
  the councillors". Same lesson as the routing work on `committee-pack-review`.

- **A stop-or-ask table.** _Why:_ the submission's failure modes were spread through the prose.
  The rows that matter: no written case yet (stop and build it), no registration deadline (say
  so, never invent one), and the grounds do not support refusal (say so, and write to the
  realistic ask).

- **Third-party personal data guidance.** _Why:_ the submission said "real names where known".
  Naming your own speakers with their consent is fine; other people's objections are reported by
  substance, never by name.

- **Repo structure** — `README.md`, `CHANGELOG.md`, `LICENSE` and a `references/` split, from a
  single 332-line file. _Why:_ house convention, and the stage modules and council rules are
  reference material consulted once rather than method read every run.
