# Committee pack review

Forensic scrutiny of a planning committee pack before the meeting: find it, split it, work
out which items matter, interrogate those, and give the reader the strongest case in each
direction.

A pack lands a few working days before the meeting — one agenda, several applications,
often several hundred pages, and a deadline that is the meeting itself. This skill does
the pack-level work; the per-report analysis belongs to skills that already exist.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The skill: the six steps, the output contract, and the integrity rules. **Start here.** |
| `references/finding-the-pack.md` | How to find the agenda and its documents — ModernGov recipe, the two publishing shapes, and where addenda hide. |
| `references/output-template.md` | The output contract, with the reasoning for its ordering. |
| `CHANGELOG.md` | Design decisions and their rationale, per revision. |

## Six things that define it

- **It is forensic, not descriptive.** The officer report is the council's case for its own
  recommendation. This skill tests it — defects, omissions, internal conflicts, policies
  cited but never applied, statutory duties not discharged, alternatives not engaged with.
  Finding none is a legitimate result; not looking is not.

- **It advocates both ways, and refuses to balance.** Each flagged item ends with two cases
  — the strongest available case for approving and the strongest for refusing — **built
  independently**, neither conceding to the other, with no closing paragraph weighing them
  up. Anyone wanting a balance already has one in the officer report, and
  `planning-balance` produces one properly.

- **Weight is the member's to set, and the output says where.** Members can lawfully weigh
  the same material considerations differently from the officer and reach a different
  decision without anything in the report being wrong. Every flagged item separates the
  weightings fixed by law or national policy from those at large, quotes the officer's
  chosen weight, and says which the conclusion actually turns on.

- **It separates what the report proved from what it took on trust.** On a large application
  the conclusions on noise, biodiversity, landscape, transport and drainage each rest on a
  document the applicant commissioned. The output names the load-bearing ones, says what
  depends on each, and says who tested it — including where the answer is nobody, or where a
  consultee's own wording hedges it ("sufficient information *at this stage*"). It does not
  re-run the technical work; it asks the question that would test the claim.

- **The community's objections get worked on their merits**, ranked, and **each anchored to
  a policy by number**. A member who thinks the public has a point can then cite it in the
  chamber. The ones with no planning anchor are said to have none, factually, rather than
  quietly dropped.

- **Triage is still the product, and the deadline is the meeting.** A twelve-item agenda
  where two items matter is the normal case, so the output must contain items marked "no
  scrutiny needed". Deadlines and the speaking cut-off go at the **top** — a brilliant
  critique delivered after registration closes is worthless. And addenda are re-checked on
  the morning, with the time recorded, because a late item can change the recommendation
  outright.

## What it does not do

It does not audit a single officer report assertion by assertion — that is
`planning-report-quality`, and the ranked defect list built from it is
`planning-report-critique`, which this skill hands flagged items to. It does not strike a
balance between the two cases it builds; for that, use `planning-balance`. It does not advise a committee member how to vote: that is
`councillor-fact-pack`'s territory (proposed, issue #39), under predetermination and costs
constraints this skill does not carry. It never predicts the outcome of a vote, and it never
forecasts what an appeal would do.

## Pairs with

- **`planning-report-critique`** — the deep read on an item triage has flagged.
- **`planning-report-quality`** — the measurement underneath that critique.
- **`planning-document-search`** — for application documents that are not in the pack, which
  is a different system and a different skill.
- **`policy-compliance-assessment`** — scoring a scheme against the development plan.
- **`planning-balance`** — the balance this skill deliberately refuses to strike.

## Licence

MIT — see [`LICENSE`](LICENSE). Provided as is, with no warranty. **Not legal advice**;
output requires human review before it is acted on.
