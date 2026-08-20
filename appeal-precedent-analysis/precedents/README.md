# Precedent corpus

Structured records extracted from published Planning Inspectorate appeal decision letters.
This is the skill's **data layer** (see repo rule: method in `../SKILL.md`, per-instance
facts here). Records are analysis of public decisions — the published letter is always the
authority; **re-verify every quote against the letter before it goes into a submission**.

## Provenance and verification

- Every record is drawn from a decision letter published by the Planning Inspectorate
  (obtainable by appeal reference via the Inspectorate's public appeal services or the
  LPA's planning register).
- Every quote carries the decision letter's paragraph number, and each record carries the
  date its quotes were verified against the letter.
- The seed corpus (25 records) was extracted from June 2026 decision letters, verified
  19 August 2026. All June 2026 decisions applied the **December 2024 NPPF** (paragraph
  numbers) — the 17 August 2026 edition replaced these with coded policies, so every seed
  record carries a framework-currency note. ⏳ Re-check currency at run time via the
  **national-planning-policy** skill.

## Personal data policy

Decision letters are public documents, but records here are kept minimal:

- **included**: appeal reference, decision date, LPA, site address (all part of the formal
  public citation), development description, outcome, procedure;
- **excluded**: appellant and agent names, and any other personal detail — they are not
  needed to cite or verify a decision.

## Record schema

One file per decision, named `<ref>-<slug>.md`:

```markdown
---
ref: "6004388"                  # the published appeal reference, quoted exactly
decision_date: 2026-06-22
lpa: North Warwickshire Borough Council
site: Land between 10 and 32 Birmingham Road, Whitacre Heath
development: Permission in Principle, limited infill residential (1–9 dwellings)
outcome: allowed                # allowed | dismissed | split | conditions-varied
procedure: hearing              # written-representations | hearing | inquiry
nppf_edition: December 2024     # the edition the decision applied
issues: [green-belt, grey-belt, flood-risk, housing-land-supply]
verified: 2026-08-19            # date quotes were checked against the letter
---

**Finding (Y).** What the inspector concluded, in one or two sentences.

**Reasoning (Z).** Why — with the decision's own words, quoted, with paragraph numbers.

**Applies when:** bullets — the facts the reasoning ran on, phrased as testable conditions.

**Distinguish when:** bullets — the differences that would defeat the parallel.

**Framework currency:** which cited instruments/paragraphs are superseded, what the
current equivalent is (via the national-planning-policy crosswalk), and whether the test
survived in substance.
```

Keep the `issues` tags to the shared vocabulary already in use across records (grep before
inventing a new tag).

## Adding records (the pipeline)

1. Obtain the month's decision letters (public record; observe the responsible-use rules in
   the repo — identify yourself, pace requests, never defeat a bot challenge).
2. Read the letter in full; only record findings that were **determinative** of the appeal
   or of a main issue.
3. Extract the record: quote the operative sentences verbatim with paragraph numbers;
   derive "applies when" from the facts the inspector actually relied on, and "distinguish
   when" from the facts the inspector said mattered (including any precedent the inspector
   distinguished).
4. Note the NPPF edition in force at the decision date and write the framework-currency
   note against the current edition.
5. Strip personal names; keep the citation fields.
6. Date-stamp `verified:` and add the record to `INDEX.md`.

A record that merely repeats a policy test with no site-specific reasoning adds nothing —
the policy itself is the better citation. Record decisions whose reasoning *turns facts
into conclusions* in a way a future case can match.
