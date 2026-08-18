# Planning skills

## The Super Quick Start Guide

Open ChatGPT / Claude / Gemini or other general purpose AI tool and type:

```text
Read the UK planning skills at https://github.com/SeagullTwo/uk-planning-skills.
```

**You can find more prompt examples below — see [How to use](#how-to-use).**

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
| [`policy-compliance-assessment/`](policy-compliance-assessment/) | **Policy foundation.** Identify and verify the **adopted** development plan for the local planning authority (the council's own policies, which have primacy) — adoption dates, superseded/saved policies, the policies map — then assess the application policy by policy and score accordance from **-2** (significant conflict) to **+2** (strongly aligned), with `?` where the evidence submitted cannot answer the policy. NPPF/PPG and emerging plans assessed in a separate, lower-weight tier. |
| [`policy-representation/`](policy-representation/) | Draft the representation from that analysis — **in support or in objection**, as you choose — each point anchored to a quoted adopted policy and the application's own documents, the other side answered, and a clear ask. Won't manufacture policy compliance or conflict to fit a stance. |
| [`national-planning-policy/`](national-planning-policy/) | **Shared layer.** The current NPPF/PPG edition register with a verify-before-citing protocol, plus the decision-making core the other skills share — s.38(6) and the development plan's primacy, the para 11 presumption ("tilted balance"), emerging-plan weight, and the conditions/obligations tests. |
| [`planning-balance/`](planning-balance/) | **Final step.** The "so-what" test: anticipate the decision-maker's planning balance — governing framework, ground-specific gateways, harms vs benefits — and recommend what the representation should actually ask for (refusal, deferral for information, or conditions), or advise that the balance favours approval. |

All England-focused. The skills chain:

1. **`planning-document-search`** fetches the application documents;
2. **`application-triage`** decides which grounds are worth pursuing and routes to —
3. **`policy-compliance-assessment`**, which establishes the adopted development plan and scores
   the application against its policies (the foundation every ground is anchored to), and
4. a topic **representation** skill (`ecological-`, `transport-`, `heritage-`,
   `flood-representation`) which evaluates the technical evidence and drafts the objection;
5. **`policy-representation`** drafts the policy case itself — in **support** or **objection**;
6. **`planning-balance`** runs the final "so-what" test — whether the assembled case actually
   supports refusal, a request for further information, or conditions.

(`national-planning-policy` sits under all of them as the shared NPPF/PPG layer.)

Steps 3–5 are where the two policy skills split the work deliberately: the assessment is
comprehensive so you can review the findings, and the representation is short and selective so a
case officer will act on it.

Considerations without a dedicated skill yet (design, residential amenity, Green Belt,
landscape, trees, air quality…) are covered by the triage skill's framework map, to argue on
the application's own facts.

## How to use

These are **skills for Claude** — instruction sets Claude follows when you ask it to do
the corresponding task. There are two ways to use them.

### 1. In a chat with Claude — no setup

Point Claude at the repo, then work through it in **stages** so you can review each step. Copy
these into Claude, filling in the reference and council.

**1 — Read the skills**

```text
Read the UK planning skills at https://github.com/SeagullTwo/uk-planning-skills.
```

**2 — Fetch the documents for an application**

```text
Using the planning-document-search skill, find and download the documents for planning application [REF] at [COUNCIL] and give me a labelled list.
```

**3 — Work out which grounds are worth objecting on**

```text
Using the application-triage skill, tell me which grounds are worth objecting on for this application — ranked, with non-material concerns (loss of view, property values) set aside. Be honest if there's no strong ground.
```

**4 — Assess it against the adopted local plan**

```text
Using the policy-compliance-assessment skill, identify the adopted development plan for this council and assess the application against its policies — a table of the relevant policies with a score from -2 to +2, and your conclusion on whether it accords with the plan read as a whole.
```

**5 — Draft a representation for one technical ground**

```text
Using the ecological- / transport- / heritage- / flood-representation skill (pick the ground), evaluate the evidence and draft a concise objection — or tell me if there isn't a sustainable one.
```

**6 — Draft the policy representation, in support or objection**

```text
Using the policy-representation skill, draft my representation [in support of / objecting to] this application, based on the policy assessment. Tell me if the policies don't actually support that stance.
```

Working in stages lets you check the triage and the policy assessment before spending effort on a
draft — which is how the skills are meant to be used. Prefer a single command that runs the
objection flow? See the optional `/planning-object` command under *Install* below.

### Worked examples you can try

These use **real, already-decided applications** (all public record), so you can run a skill
end-to-end and check what it produces against the council's actual officer report and decision
notice on the portal. They are illustrations, not live campaigns — swap in your own reference
and council for real use, and start each chat with the "Read the UK planning skills at …"
prompt above so Claude has the skills loaded.

**Fetch the file for an application** (a householder application, granted December 2025):

```text
Using the planning skills at https://github.com/SeagullTwo/uk-planning-skills, find and download the documents for planning application 6/2025/2300/HOUSE at Welwyn Hatfield Borough Council and give me a labelled list.
```

**Full objection flow on one prompt** (a town-centre change of use in a conservation area,
refused at committee in November 2018 — ask for the era's policy context and see if the
skills reach the committee's answer):

```text
Using the planning skills at https://github.com/SeagullTwo/uk-planning-skills, assess whether there are grounds to object to application 6/2018/1881/FULL at Welwyn Hatfield Borough Council, judged against the development plan and national policy in force at the time, and draft a representation on the strongest ground. Do not read the officer's report or decision notice — I want your independent view.
```

**Policy compliance in a conservation area** (a householder scheme refused December 2025 on
a single heritage ground):

```text
Using the planning skills at https://github.com/SeagullTwo/uk-planning-skills, assess application 6/2025/2155/HOUSE at Welwyn Hatfield Borough Council against the adopted development plan — a scored policy table and your conclusion on whether it accords with the plan read as a whole.
```

**A technical ground, honestly assessed** (a major scheme with a full ecology evidence base —
a good test of the "don't object" output, since the ecology evidence may well hold up):

```text
Using the planning skills at https://github.com/SeagullTwo/uk-planning-skills, evaluate the ecology and biodiversity net gain evidence for application DM/25/0445 at Mid Sussex District Council and tell me whether an objection on ecology grounds would be sustainable — be honest if it wouldn't.
```

Decisions and officer reports for all four are on the councils' portals, so you can mark the
skills' homework. Portals do move documents over time; if a reference no longer resolves, any
current application from the same council works the same way.

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

The two policy skills hold **no policy catalogue at all, by design** — local plans are adopted,
superseded and reviewed continuously, so the plan is located and every policy quoted from the
council's own adopted document at run time.

## License

MIT — see [`LICENSE`](LICENSE). Provided as-is, with no warranty; you are responsible for
using these skills in line with each service's terms of use and applicable law.
