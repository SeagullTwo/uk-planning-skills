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
| [`transport-representation/`](transport-representation/) | Evaluate the transport/highways evidence (Transport Assessment/Statement, Travel Plan, parking, street layout, and mitigation secured at outline), map each deficiency to the national/local transport policy and guidance it engages, and draft a concise representation — or advise that none is warranted. England-focused. |

The skills chain: `planning-document-search` fetches the documents that a representation
skill (`ecological-objection`, `transport-representation`) then critiques.

## How to use

These are **skills for Claude** — instruction sets Claude follows when you ask it to do
the corresponding task. There are two ways to use them.

### 1. In a chat with Claude — no setup

Point Claude at this repo (or paste a skill's `SKILL.md`) and ask in plain language.
Examples:

- *"Using the planning-document-search skill, find and download the documents for
  application [ref] at [council]."*
- *"Use the ecological-objection skill on this application — read the ecology reports,
  tell me if there's a sustainable objection, and draft one."*

Give Claude the **application reference and the council**, or the **documents themselves**.
The skills chain: `planning-document-search` fetches the documents, then a representation
skill critiques them.

### 2. Install so they trigger automatically (Claude Code)

Copy a skill's folder to where Claude Code discovers skills, and it will trigger by its
`description` without being named:

- **Personal (all your projects):** `~/.claude/skills/<skill-name>/`
- **Project (shared via a repo):** `<project>/.claude/skills/<skill-name>/`

Each skill already has the `SKILL.md` frontmatter (`name`, `description`) that discovery
needs — so it's just a copy. After that, a prompt like *"object to this application on
ecology grounds"* invokes the skill automatically.

### Before you rely on the output

Read the disclaimer at the top: **not legal advice, no warranty, and the output needs
human review.** Anything you submit to a council is normally published on its portal in
your name.

## Principles

The skills share a posture set out in their own `SKILL.md`:

- **Public records, retrieved as a member of the public would** — targeted retrieval, not
  bulk harvesting; never defeat a bot challenge (stop and use a browser); identify
  yourself, pace requests, honour rate limits and robots.txt.
- **Evidence-bound and honest** — every claim is grounded in the actual documents or cited
  guidance; "don't object" is a valid, valuable output when the submission is sound.
- **Personal-data aware** — planning documents contain third parties' personal data;
  retrieve only what's needed and don't republish or retain beyond the task.

## Freshness

Portal assignments and the ecology and transport guidance catalogues were web-verified in **August 2026**.
Portals migrate and guidance editions turn over, so each skill re-resolves/re-verifies at
run time; items flagged in the reference files are time-sensitive.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; you are responsible for
using these skills in line with each service's terms of use and applicable law.
