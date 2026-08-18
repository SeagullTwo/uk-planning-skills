# Slash commands

In current Claude Code, **an installed skill is already a slash command.** Once you copy a
skill from this repo into `~/.claude/skills/<name>/` (personal) or a project's
`.claude/skills/<name>/`, you can either let Claude pick it automatically from your request, or
invoke it by name:

- `/planning-document-search`
- `/application-triage`
- `/policy-compliance-assessment` · `/policy-representation`
- `/ecological-representation` · `/transport-representation` · `/heritage-representation` ·
  `/flood-representation`
- `/national-planning-policy` · `/planning-balance`

So you do **not** need a wrapper command for a single skill — the skill *is* the command.
(Custom commands and skills are the same system now: a `.claude/commands/x.md` and a
`.claude/skills/x/SKILL.md` both create `/x`; if a name clashes, the skill wins.)

## The one wrapper worth having

`planning-object.md` is an optional **orchestration** command — one shortcut that runs the whole
flow across several skills (retrieve → triage → assess policy → draft), which no single skill
does on its own:

| Command | What it does |
|---|---|
| `/planning-object [ref] [council]` | Fetch the documents, triage the grounds, assess the application against the adopted development plan, and draft objections for every live ground |

The command is **objection-only**, as its name says. To write in **support**, or to run the policy
analysis on its own, invoke the skills directly — `/policy-compliance-assessment` then
`/policy-representation` — and say which stance you want.

### Install

Copy it to where Claude Code discovers commands (personal, or a project you share):

```bash
mkdir -p ~/.claude/commands
cp commands/planning-object.md ~/.claude/commands/
```

It invokes the skills, so install the skills too (see the top-level README). Then, for example:

```
/planning-object 24/00431/FULL, Hull City Council
```
