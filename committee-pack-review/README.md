# Committee pack review

Forensic scrutiny of a planning committee pack before the meeting: find it, split it, work
out which items matter, interrogate those, and give the reader the strongest case in each
direction.

A pack lands a few working days before the meeting — one agenda, several applications,
often several hundred pages, and a deadline that is the meeting itself. This skill does
the pack-level work; the per-report analysis belongs to skills that already exist.

## When to use it

**You do not have to know it is called "committee pack review".** Use it whenever an
application is going before members and you want to know what is wrong with the officer's
case — "review the officer's report", "are there grounds to challenge the recommendation?",
"help me prepare for planning committee", or just "analyse this application" where the
application turns out to be at committee.

| Your situation | Start with |
|---|---|
| Application going to committee, pack published | **`committee-pack-review`** |
| Going to committee, pack not published yet | `planning-document-search` → `application-triage`, then come back |
| New or live application, no committee in prospect | `planning-document-search` |
| "Should I object at all?" | `application-triage` |
| One officer report needs a full audit | `planning-report-critique` / `planning-report-quality` |
| Scoring against the development plan | `policy-compliance-assessment` |
| The final planning balance | `planning-balance` |

Given only a reference and a council, the skill works out whether it is at committee before
choosing a path — the presence of an officer report is the strongest signal, since delegated
decisions do not get one. If it cannot tell, it asks rather than guessing.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The skill: the six steps, the deliverable, the output contract, and the integrity rules. **Start here.** |
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

## The deliverable

**A designed HTML page, offered before it is built.** The output carries a triage table,
weighting pivots, a claims table, ranked community points and two advocacy cases that must
read as equals — markdown flattens all of that into one column, and the two cases stop
looking independent the moment they are two headings in a row. It is also read on a phone the
night before a meeting, and it gets forwarded. Markdown stays correct where the reader asks
for it or the host cannot publish a page.

**The run says which model produced it**, in the provenance line, and stops to ask if it is
not a frontier model. Sustained forensic reading across several hundred pages is where a
smaller model fails in the way that matters here — a confident, well-formed report with
findings that are not in the papers.

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
