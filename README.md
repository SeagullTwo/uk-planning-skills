# Planning skills

A small collection of skills for working with the UK planning system, each self-contained
in its own folder with a `SKILL.md`, a `README.md`, and supporting reference files.

> **Not legal advice. No warranty.** These skills help a member of the public find public
> planning documents and marshal a well-founded representation. They are not a substitute
> for a solicitor or a professional ecologist, guarantee no outcome, and are provided "as
> is". **Their output requires human review before use.** Anything submitted to a UK local
> planning authority is normally **published on the council's portal in the submitter's
> name** and kept on the record — include only personal details you're content to make
> public.

## Skills

| Skill | What it does |
|---|---|
| [`planning-document-search/`](planning-document-search/) | Retrieve the documents attached to a UK planning application from the council's **public** online planning portal, given the application reference and council. Covers the major portal vendors (Idox, Northgate, Civica, Ocella, Agile, NEC, TerraQuest, StatMap, DEF Atrium…) with a tested per-vendor recipe and a council→portal→vendor registry. |
| [`ecological-objection/`](ecological-objection/) | Evaluate the ecological evidence submitted with a planning application, map each deficiency to the national law/policy/guidance it engages, and draft a concise, well-founded objection — or advise that no sustainable objection exists. England-focused. |

The two are designed to chain: `planning-document-search` fetches the documents that
`ecological-objection` then critiques.

## Principles

Both skills share a posture set out in their own `SKILL.md`:

- **Public records, retrieved as a member of the public would** — targeted retrieval, not
  bulk harvesting; never defeat a bot challenge (stop and use a browser); identify
  yourself, pace requests, honour rate limits and robots.txt.
- **Evidence-bound and honest** — every claim is grounded in the actual documents or cited
  guidance; "don't object" is a valid, valuable output when the submission is sound.
- **Personal-data aware** — planning documents contain third parties' personal data;
  retrieve only what's needed and don't republish or retain beyond the task.

## Freshness

Portal assignments and the ecology guidance catalogue were web-verified in **August 2026**.
Portals migrate and guidance editions turn over, so each skill re-resolves/re-verifies at
run time; items flagged in the reference files are time-sensitive.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; you are responsible for
using these skills in line with each service's terms of use and applicable law.
