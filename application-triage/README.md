# Application Triage

The **router** for the planning representation skills. Given a UK planning application, it
works out which material planning considerations are actually engaged, ranks them, and routes
each to the skill that handles it — or says plainly that there is no strong ground to object.

> **Not legal advice. No warranty.** A starting assessment provided "as is"; **a human must
> review the grounds and evidence before acting.** Anything later submitted to a council is
> published on its portal in the submitter's name.

## What it does

- Reads the application (via the reference + council, or the documents) and its site
  constraints.
- Identifies the engaged material considerations from the proposal, the constraints, and the
  presence or telling *absence* of technical documents.
- **Ranks** them (decision-critical / supporting / weak) and **sets aside non-material
  concerns** (loss of view, property values, competition, private disputes) — with a reframe
  where one exists.
- **Routes** each live ground to its representation skill.

## Contents

| File | What it is |
|---|---|
| `SKILL.md` | The skill: workflow, the integrity principle, and the routing table. **Start here.** |
| `references/material-considerations.md` | The map: each consideration's tells, the skill/framework that handles it, and the non-material concerns to exclude. |
| `CHANGELOG.md` | Design decisions and their rationale, per revision. |

## Pairs with

- **planning-document-search** — fetches the application documents and the constraint signals.
- **ecological-representation**, **transport-representation**, **heritage-representation**,
  **flood-representation** — the drafting skills this one routes to.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; not legal advice.
