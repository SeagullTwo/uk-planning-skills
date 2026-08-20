# Appeal Precedent Analysis

Find and apply relevant **planning appeal decisions** to a UK planning application, so a
representation can argue: *"In appeal decision X, the Inspector found Y because of Z — the
same Z is present here, so consistency in decision-making requires Y, or reasons for
departing from it."*

> **Not legal advice. No warranty.** Provided "as is"; **a human must verify every cited
> decision against the published letter before use.** Anything submitted to a council is
> normally published on its portal in the submitter's name.

## What it does

- Works from a **checked-in corpus of structured precedent records** (`precedents/`)
  extracted from published Planning Inspectorate decision letters, plus any decision you
  supply.
- **Tests comparability** before citing: was the finding determinative, are the operative
  facts present here, is the policy framework still the one the inspector applied, and
  what will the other side use to distinguish it.
- **Grades weight** (same site → same LPA/policy → same test elsewhere → reasoning only)
  and surfaces **adverse precedents** honestly instead of hoping nobody finds them.
- **Drafts the precedent passage** — citation, quoted finding with paragraph numbers,
  evidenced parallel, consistency ask, pre-emption — for the representation skills to use.

## Why the caution

Appeal decisions are material considerations, not binding precedent. The governing
principle is consistency (*North Wiltshire DC v SSE* (1992) 65 P&CR 137): like cases
alike, or reasons given. In a coded sample of 200 June 2026 decision letters, inspectors
distinguished party-cited precedents almost by default ("I do not have full details of
that case before me") — while a directly comparable, properly quoted decision was called
"a material consideration of great weight". This skill is built to produce the second
kind of citation.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The skill: the consistency principle, the six-step workflow, output format |
| `references/comparability-and-weight.md` | The Z-test in detail, weight tiers, the adverse-precedent duty, drafting patterns |
| `precedents/README.md` | Record schema, provenance/verification rules, personal-data policy, how to add records |
| `precedents/INDEX.md` | One-line index of the corpus by topic |
| `precedents/*.md` | The records — 25-seed corpus from June 2026 decisions (all under the December 2024 NPPF; every record carries a framework-currency note) |

## Fits in the chain

`application-triage` → `policy-compliance-assessment` → representation skills → **this
skill** (strengthen the evidenced grounds with decided authority) → `planning-balance`.
Also runs in reverse: to distinguish a decision the applicant or officer relies on.
