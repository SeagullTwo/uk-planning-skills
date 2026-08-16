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
| [`planning-document-search/`](planning-document-search/) | **Retrieve** the documents attached to a UK planning application from the council's **public** online planning portal, given the application reference and council. Covers the major portal vendors (Idox, Northgate, Civica, Ocella, Agile, NEC, TerraQuest, StatMap, DEF Atrium…) with a tested per-vendor recipe and a council→portal→vendor registry. |
| [`application-triage/`](application-triage/) | **Router.** Given an application, work out which material considerations are engaged, rank them, and route each to the representation skill that handles it — or advise there is no strong ground. Sets aside non-material concerns (loss of view, property values). |
| [`ecological-representation/`](ecological-representation/) | Evaluate the **ecology / biodiversity** evidence (EcIA, protected-species surveys, BNG), map deficiencies to national law/policy/guidance, and draft a concise objection — or advise none is warranted. |
| [`transport-representation/`](transport-representation/) | Evaluate the **transport / highways** evidence (Transport Assessment/Statement, Travel Plan, parking, street layout, secured mitigation), map deficiencies to policy/guidance, and draft a representation. |
| [`heritage-representation/`](heritage-representation/) | Evaluate the **heritage / historic-environment** evidence (Heritage Statement, setting and archaeology assessments) for listed buildings, conservation areas, monuments and non-designated assets, and draft a representation. |
| [`flood-representation/`](flood-representation/) | Evaluate the **flood-risk and drainage** evidence (Flood Risk Assessment, Drainage/SuDS strategy, Sequential/Exception Tests), map deficiencies to national policy, and draft a representation. |

All England-focused. The skills chain:

1. **`planning-document-search`** fetches the application documents;
2. **`application-triage`** decides which grounds are worth pursuing and routes to —
3. a **representation** skill (`ecological-`, `transport-`, `heritage-`, `flood-representation`)
   which evaluates the evidence and drafts the objection.

Considerations without a dedicated skill yet (design, residential amenity, Green Belt,
landscape, trees, air quality…) are covered by the triage skill's framework map, to argue on
the application's own facts.

## How to use

These are **skills for Claude** — instruction sets Claude follows when you ask it to do
the corresponding task. There are two ways to use them.

### 1. In a chat with Claude — no setup

The simplest way — **copy this into Claude**, filling in the reference and council:

```text
Read the UK planning skills at https://github.com/SeagullTwo/uk-planning-skills, then use them to help me with planning application [REF] at [COUNCIL]: fetch the documents, work out which grounds are worth objecting on, and draft the representations.
```

Claude will read the skills from the repo and follow them. Or ask for one skill at a time:

- *"Using the planning-document-search skill, find and download the documents for
  application [ref] at [council]."*
- *"Use the ecological-representation skill on this application — read the ecology reports,
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

An installed skill is **also a slash command**: as well as auto-triggering, you can invoke it
by name — `/planning-document-search`, `/application-triage`, `/heritage-representation`, and so
on. For a single command that runs the whole flow (retrieve → triage → draft), the optional
[`commands/`](commands/) folder adds **`/planning-object [ref] [council]`** — see
[`commands/README.md`](commands/README.md).

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

Portal assignments and the representation skills' guidance catalogues (ecology, transport, heritage, flood) were web-verified in **August 2026**.
Portals migrate and guidance editions turn over, so each skill re-resolves/re-verifies at
run time; items flagged in the reference files are time-sensitive.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; you are responsible for
using these skills in line with each service's terms of use and applicable law.
