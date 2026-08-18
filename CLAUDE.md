# Repository guidance for Claude

This repo is a collection of **skills** for working with the UK planning system. Each
skill is self-contained in its own folder. Read this before changing anything here.

## Layout

```
<skill-name>/
  SKILL.md          # the skill: purpose, when-to-use, method/how-to. Has YAML frontmatter (name, description).
  README.md         # human-facing overview
  LICENSE           # MIT
  CHANGELOG.md      # design decisions per revision — UPDATE THIS with every substantive change
  references/       # supporting reference files (optional)
  <data files>      # e.g. planning-portal-registry.json — per-instance DATA, kept separate from method
```

Repo root also has a top-level `README.md` and `LICENSE`.

## House rules for changing a skill

1. **Keep skills generic and public-safe.** These are (or may become) public. Never
   introduce:
   - personal data (names, addresses, emails, phone numbers);
   - references to a specific campaign, case, applicant, consultant, or a named
     inquiry/appeal;
   - place- or region-specific fingerprints presented as if the skill is *about* that
     place. (Real councils/portals may appear as *functional coverage data* — that is the
     tool's data, not a campaign fingerprint. The test is: would this identify a
     particular real-world dispute or person? If yes, don't add it.)
   When in doubt, write the generic pattern and put the specific example behind a
   placeholder (`[insert …]`).

2. **Two layers, no duplication.** Method/how-to lives in `SKILL.md` (and `references/`);
   per-instance facts live in the data file (e.g. the registry). Don't copy one into the
   other. A per-council quirk goes in the registry; the vendor recipe goes in SKILL.md.

3. **Evidence before assertion.** Don't claim something works or is current unless it was
   verified: downloads verified by magic bytes; legal/policy/guidance citations verified
   against source (not from memory) and dated; time-sensitive facts flagged (⏳) with a
   "re-verify at run time" note. Prefer "this is how X behaves" over a testing-diary
   ("validated at Y on DATE") — see rule 6 on what belongs in the changelog vs the skill.

4. **Responsible-use posture is a constraint, not decoration.** Public records only;
   never defeat a bot challenge (stop and hand the user a browser link); identify
   yourself, pace requests, honour rate limits and robots.txt; treat downloads as
   untrusted; handle third-party personal data minimally. Skills are **not legal advice**,
   carry **no warranty** (provided "as is"), and their output **requires human review
   before use**. Where a skill produces something a user might submit to a public body,
   flag the consequence — e.g. a **UK planning representation is normally published on the
   council's portal in the submitter's name** and kept on the record, so the user chooses
   what personal detail to include. Don't weaken any of this when editing.

5. **File operations: copy → verify → delete.** When moving or restructuring files, copy
   to the new location, verify the copy (byte-compare / parse / spot-check), and only then
   delete the original. Don't `mv`/`sed -i` destructively in one unreviewable step; prefer
   reviewable edits (everything is in git — diff before finalizing).

6. **Every substantive change updates the skill's `CHANGELOG.md` — with the rationale.**
   The changelog records *why* a design choice was made, not just what changed. Keep the
   skill body free of development/testing history; that narrative belongs in the changelog.
   See the format below.

7. **Don't commit local or work-product files.** `.claude/settings.local.json`, scratch
   output, downloaded documents, and campaign work products stay out of the repo
   (`.gitignore` covers the known ones).

8. **Freshness.** Portals migrate and guidance editions turn over. Re-resolve/re-verify at
   run time; note verification dates in the reference files, not as a coverage boast.

9. **Output style: bullets, not semicolon-runs.** Every skill that produces a report,
   summary or representation must instruct its output style, and the instruction must
   demonstrate it: enumerations of three or more items go in a bulleted or numbered list,
   never strung through a paragraph (or a table cell) with semicolons; one point per
   paragraph, paragraphs short. The representation skills carry this in
   `references/house-style.md`; analysis skills state it in their output-format section.
   When writing a skill's output instructions, don't pack the required elements into a
   single prose sentence — the model mirrors the register of its instructions, so an
   instruction written as a semicolon-run produces output written as semicolon-runs.

## CHANGELOG format

Each skill's `CHANGELOG.md` follows this shape. Newest entry on top. Each entry is dated
and lists notable changes, and — this is the point — the **rationale** for the
design-affecting ones.

```markdown
## [version or label] — YYYY-MM-DD

### Changed / Added / Removed / Fixed
- **What changed.** _Why:_ the rationale / design choice behind it.
```

Use `Added`, `Changed`, `Removed`, `Fixed`, `Security` groupings as needed. A one-line
mechanical fix needs a one-line entry; a design decision (e.g. "made PlanIt optional",
"removed the Arcus reverse-engineering guidance") gets its reasoning recorded so a future
editor understands the intent and doesn't undo it.
