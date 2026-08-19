# Testing design for the planning skills

How we test that a change to the skills makes their output **better** — and catch it when a
change quietly makes it worse. Two complementary test types share one judging machinery:

1. **In-sample regression** — a fixed set of 20 known applications, run on every candidate
   skill version and compared against the current version.
2. **Out-of-sample evaluation** — frozen, randomly drawn cohorts of *never-seen* appeal
   cases, scored blind against the real officer and inspector outcomes.

Design principles that apply to both:

- **Judge, don't diff.** LLM output varies run to run; textual comparison is meaningless.
  Both versions' outputs are scored and the scores compared — and the baseline is re-judged
  fresh each time, so judge drift can't masquerade as regression.
- **"Better" means more, clearer, honest** — more factual points covered, in clearer and
  simpler language, with no manufactured grounds. Coverage is the goal; clarity is a gate;
  honesty is an assertion that fails the run outright.
- **Ground truth over vibes.** Every test case is an application that was actually decided
  — ideally at appeal — so the officer report and the inspector's decision letter supply an
  authoritative list of what a good analysis should have found.
- **Era-pin everything.** Policy editions turn over (most recently the August 2026 NPPF
  recoding); every fixture records the NPPF edition, development-plan state and document
  snapshot date it is assessed against, and runs are instructed to assess "as at" that
  date. Without pinning, tests rot silently.

---

## Test type 1 — in-sample regression

### Purpose

Stop a skill edit from degrading output on known ground. This is the test you run before
merging a skill change. It detects *meaningful* movement, not one-point noise — its job is
to catch failure modes like the semicolon-run style creep (issue #22), a dropped analysis
step, or a new instruction that suppresses honest "no strong ground" answers.

### Fixtures — 20 applications

Composition (agreed 2026-08-19):

- **5 major housing applications** — 20–100 homes each;
- **5 householder extension applications**;
- **10 others** forming a representative spread — ecology/habitats, flood, transport,
  heritage, HMO ×2 (one refused on standards, one allowed on fallback — a deliberate
  mirror pair), prior approval (Class MA), open space, noise/amenity, specialist
  accommodation (C2).

Selection rules:

- **Decided at appeal.** Officer report + inspector decision letter = two layers of ground
  truth per case; a case where they disagreed is kept deliberately (genuinely contestable
  cases are the interesting ones).
- **Mixed outcomes** — 10 allowed / 10 dismissed overall — so gold checklists exist for
  both objector-side and applicant-side accuracy, and a version cannot score well by
  leaning one way.
- **Include the honesty traps**: at least one case where the right answer is "no strong
  ground" and one where the right stance is support. A version that manufactures an
  objection on either **fails the run outright**, regardless of its other scores.
- **Retrievable documents** — the LPA's portal must be fetchable by
  `planning-document-search` (registry-blocked portals disqualify a candidate).

Each fixture directory contains:

- the application document set (as downloaded, verified by magic bytes, sha256 manifest);
- a **provenance manifest** — portal URL, snapshot date, appeal reference, NPPF edition
  and plan state at the pinned date;
- the **gold checklist** (see scoring) and the officer report / decision letter, stored
  separately from the input documents so blind runs cannot see them;
- the **assertions** for that case (expected stance; "cannot-assess" flags expected).

A proposed seed slate of 20 cases drawn from the May–June 2026 appeal corpus is at the end
of this document.

### Harness

- **Runner**: for each fixture, invoke the skill chain headlessly with a pinned model and
  a pinned skill version (git SHA); outputs land in `runs/<sha>/<case>/`. The chain and
  prompts used are recorded per run.
- **Tiers**: a 3-case smoke subset for quick iteration; the full 20 before merge.
- **Comparison protocol**: blind pairwise A/B judging — the judge sees both versions'
  outputs for the same case with order randomised and no version labels; three passes;
  majority verdict per case. Judge model and prompts are pinned and checked in — **the
  judge prompts and gold checklists are the real test suite** and are versioned like code.

### Scoring — "better", operationalised

1. **Factual coverage (primary).** Each fixture's gold checklist lists the factual and
   analytical points a good assessment finds — distilled from the officer report,
   inspector letter, and (for the seed slate) our June coding. Examples: "identifies the
   CA and applies s.72(1)"; "spots the missing daylight assessment"; "identifies the PD
   fallback and quantifies the delta". Scoring rules:
   - the judge must **quote the output line** that covers each point — no credit for gist;
   - a **hallucination penalty**, partly mechanical: every cited policy code is checked
     against the fixture's pinned policy set; an invented citation is minus-scored
     automatically.
2. **Clarity and simplicity (gate, not goal).** Mostly deterministic, so it cannot drift:
   - average sentence length and a readability score;
   - the **semicolon-run detector** from issue #22 (prose paragraphs >300 chars with 2+
     semicolons; table cells >250 chars) — count must not increase;
   - one judge question: "can a busy case officer extract each point at a glance?"
   Clarity is a *gate* rather than a co-equal goal to avoid Goodhart's law: a version must
   not win by getting terser while covering less.
3. **Honesty assertions (pass/fail).** The no-strong-ground and support fixtures; plus
   "flags cannot-assess rather than guessing" on a fixture with a known evidence gap.

### Verdict rule

A candidate version passes when **all** of the following hold:

- aggregate factual coverage ≥ baseline;
- no single case regresses by more than one gold point;
- clarity metrics within bounds (no semicolon-run increase; readability not worse than a
  set tolerance);
- every honesty assertion passes.

---

## Test type 2 — out-of-sample evaluation

### The stability problem, and the design answer

Random selection is right for unbiasedness but unstable: two runs on different random
cases aren't comparable. The fix is to separate *how cases are chosen* (random) from *how
they are used* (frozen):

1. **Temporal split for purity.** A skill version has a cutoff date (its last edit). The
   out-of-sample pool is decisions *decided after that date* — the strongest anti-leakage
   guarantee available, and it also defends against the underlying model having seen older
   decisions in training. The monthly PINS corpus refills the pool indefinitely.
2. **Seeded random draw, then freeze.** Per quarter (or per significant release), draw a
   cohort — n≈20, lightly stratified to mirror the in-sample buckets — from the pool with
   a **recorded seed**, and freeze it as a named cohort (e.g. `OOS-2026-Q4`). Within a
   cohort, every version sees identical cases.
3. **Paired judging for power.** Compare versions case-by-case on the same cohort (paired
   wins/losses). Pairing removes case-difficulty variance — the actual source of the
   instability that makes small random samples noisy — and is a bigger stability lever
   than sample size.
4. **Burn and refresh.** The moment a case's decision letter is read to diagnose a failure,
   the case is contaminated (it will inform the next edit). After diagnosis, the whole
   cohort **retires into the regression fixture pool** — already-studied cases make
   excellent in-sample material — and a fresh cohort is drawn from newer decisions.
   Out-of-sample stays honest; the in-sample set grows for free.
5. **Contamination ledger.** One checked-in file lists every case reference ever read,
   coded, fixtured, or added to the precedent corpus (the 200 coded June letters, the 25
   precedent records, each fixture, each retired cohort). The sampler excludes it.
6. **Optional sealed cohort.** One cohort that is only ever *scored*, never diagnosed — a
   long-horizon honesty check that survives many releases and catches gradual overfitting
   to the kinds of failures we diagnose.

### Blind protocol and scoring

- Fetch the application documents only; run the chain as if the application were live
  (never reading the officer report, decision notice, or appeal correspondence — the same
  discipline as the 2026-08 blind benchmark exercise); *then* reveal the ground truth.
- Score, in order of statistical usefulness:
  1. **Issue recall (primary)** — did the blind run identify the issues the inspector
     found determinative? Many points per case → tight comparisons even at n=20.
  2. **Outcome concordance (secondary)** — coarse at n=20 (±20pp), a headline trend, not
     a gate. Where the inspector overturned the officer, matching the officer is *not*
     scored as failure — it is evidence the case was genuinely contestable.
  3. The same clarity metrics and hallucination checks as test type 1.

### Disclosed biases

- Appealed cases over-represent refusals and contested schemes — acceptable for
  representation skills, whose use case *is* contested applications, but stated.
- Only cases from fetchable portals can be tested — a mild coverage bias, stated in each
  cohort manifest.
- Procedure mix matters: written-representations cases dominate the pool (~95%); cohort
  stratification should not accidentally oversample hearings/inquiries.

---

## Shared machinery and operations

- **One judging stack** (blind pairwise A/B, 3 passes, pinned judge model, versioned
  prompts) serves both test types.
- **Mechanical metrics module** (readability, semicolon-run detector, citation-existence
  check) runs identically on both.
- **When to run**: smoke subset during iteration; full in-sample before merging any skill
  change; out-of-sample per release or per quarter.
- **Baselines**: the current `main` outputs are regenerated (not replayed) for each
  comparison, and both sides are judged in the same session.
- **Cost note**: a full in-sample run is 20 × the skill chain, twice (candidate +
  baseline), plus judging — budget accordingly; the smoke subset exists so iteration
  doesn't pay that price.

## Implementation

The harness is a small set of plain Python scripts plus checked-in data. No framework —
each script does one job and is runnable alone.

### Layout

```
tests/                              # or the sibling test-data repo (see Open decisions)
  fixtures/<case-slug>/
    input/
      documents/*.pdf               # the application documents, as downloaded
      manifest.json                 # provenance: portal URL, snapshot date, sha256 per
                                    # file, appeal ref, era pin (NPPF edition, plan state)
    truth/                          # NEVER passed to a skill run
      officer-report.pdf
      decision-letter.pdf
      gold.yaml                     # gold checklist, assertions, pinned policy set
  harness/
    fetch_fixture.py                # finalise a fixture after documents are fetched
    run_case.py                     # run the skill chain headlessly on one fixture
    metrics.py                      # deterministic metrics (no LLM)
    judge.py                        # LLM judging: coverage vs gold + pairwise A/B
    compare.py                      # the regression verdict: candidate vs baseline
    sample_cohort.py                # OOS: seeded stratified draw from the corpus index
    contamination.csv               # the ledger of every case ever seen
  runs/<git-sha>/<case>/            # outputs + run manifests (kept for audit)
```

### The scripts

- **`fetch_fixture.py`** — fixture *assembly* is skill-assisted, not fully scripted:
  documents are fetched in a normal session using `planning-document-search` (the portal
  recipes are the skill's job; re-implementing every vendor in the harness would duplicate
  them). The script then finalises: verifies magic bytes, computes sha256s, writes
  `manifest.json`, and refuses to finalise if any `truth/` file is missing or the era pin
  is unset.
- **`run_case.py --case <slug> --skills <path-or-sha>`** — runs the chain headlessly
  (`claude -p` with a fixed prompt template) against a git worktree of the skills at the
  requested SHA. Two integrity rules it enforces:
  - **network tools disabled for the run** (no WebSearch/WebFetch) — otherwise the model
    could simply look up the appeal outcome; the fixture documents are the whole world;
  - `truth/` is never mounted into the run's working directory.
  It writes the outputs plus a run manifest (model id, skill SHA, prompt template hash,
  date) to `runs/<sha>/<case>/`.
- **`metrics.py <output-dir>`** — pure Python, deterministic: sentence length, readability,
  the issue-#22 semicolon-run detector (prose paragraphs and table cells), and the
  citation-existence check (every cited policy code must appear in `gold.yaml`'s pinned
  policy set — unknown citations are counted as hallucinations).
- **`judge.py --a <run> --b <run> --gold <gold.yaml>`** — the LLM judge, called via the
  API with a pinned model: scores each gold point (quote required) for both outputs,
  runs the blind pairwise comparison with A/B order randomised by seed, three passes,
  majority verdict; emits a per-case JSON scorecard.
- **`compare.py --candidate <sha> --baseline main --cases smoke|all`** — the entry point:
  runs both versions on the selected fixtures (regenerating the baseline, never replaying
  old outputs), calls `metrics.py` and `judge.py`, applies the verdict rule, and writes a
  human-readable report plus a machine verdict. Exit code 0/1 so it can gate a merge.
  Judging and running are cached per `(sha, case, prompt-hash)` so re-runs are cheap.
- **`sample_cohort.py --frame <month-range> --n 20 --seed <s> --name <cohort>`** — the
  out-of-sample sampler: reads the corpus `index.csv` files, applies the temporal split,
  excludes everything in `contamination.csv`, stratifies, draws with the recorded seed,
  and writes a cohort manifest. A cohort's fixtures are then assembled with
  `fetch_fixture.py` like any other.

### Cost and cadence

- A full in-sample comparison = 20 cases × the chain × 2 versions + judging — a
  material token spend, so it is **manually triggered** (pre-merge for skill changes),
  with the 3-case smoke subset for iteration. Not wired to CI initially.
- The judge model id, seed, and prompt hashes are recorded in every scorecard, so any
  verdict can be reproduced or audited later.

## Open decisions

- **Where fixtures live.** Application documents contain applicant names and addresses.
  Options: (a) `tests/fixtures/` in this repo, amending house rule 7 (planning documents
  are public records, like the precedent corpus's decision letters); (b) a sibling
  private test-data repository the harness clones. **Recommendation: (b) if this repo may
  go public; (a) if it stays personal.** Decision pending.
- **Judge model pinning policy** — pin per-cohort (stable within a comparison) and record
  the model version in every run manifest; revisit when the pinned model is deprecated.

---

## Proposed seed slate (in-sample, 20 cases)

Drawn from the May–June 2026 appeal corpus; every case has an officer report and an
inspector decision letter. All were decided under the December 2024 NPPF — fixtures are
era-pinned accordingly. *Proposed, pending fixture download and final confirmation.*

### Majors (20–100 homes; 3 allowed / 2 dismissed)

| Appeal ref | Homes | LPA (application ref) | Outcome |
|---|---|---|---|
| 6004354 | 30 | Tendring (25/01011/OUT) | Allowed |
| 6004924 | 44 | Basingstoke & Deane (24/00787/FUL) | Allowed |
| 6003023 | 90 | Broxbourne (07/25/0222/F) | Allowed |
| 6004359 | 37 | Fenland (F/YR25/0129/O) | Dismissed |
| 6005389 | 56 flats | Liverpool (23F/0694) | Dismissed |

Reserves: 3373051 Wychavon (63, allowed, hearing); 3377572 East Devon (65, dismissed,
hearing); 6002824 Cotswold (54, allowed).

### Householder extensions (3 allowed / 2 dismissed)

| Appeal ref | LPA (application ref) | Outcome | Exercises |
|---|---|---|---|
| 6007017 | Three Rivers (25/1793/RSP) | Dismissed | Dormer subordination; LDC fallback |
| 6004631 | Bradford (25/04212/HOU) | Dismissed | Green Belt cumulative additions |
| 6003049 | Buckinghamshire (25/01942/APP) | Allowed | CA windows; survey evidence |
| 6006299 | High Peak (HPK/2025/0492) | Allowed | Design context (symmetry) |
| 3373143 | Lewes (LW/25/0253) | Allowed | Flood: annexe FRA, EA re-consultation |

### Others (5 allowed / 5 dismissed)

| Appeal ref | LPA (application ref) | Outcome | Covers |
|---|---|---|---|
| 6004999 | Tewkesbury (25/00855/FUL) | Dismissed | Habitats mitigation; backland character |
| APP/C3620/W/25/3374870 | Mole Valley (MO/2024/1993/PLA) | Dismissed | Grey belt; National Landscape; ecology gaps |
| 6005080 | Wolverhampton (25/01284/FUL) | Dismissed | HMO space standards |
| 6004335 | Portsmouth (25/01089/FUL) | Allowed | HMO fallback; Solent nutrients |
| 6002147 | Isle of Wight (25/01315/FUL) | Dismissed | Heritage: listed-building setting |
| 6005125 | Derby (25/00877/PNRIA) | Allowed | Class MA prior approval; technical evidence |
| 6003242 | Cornwall (PA25/06277) | Dismissed | Open space; self-build |
| 6003932 | Barnet (25/0574/RCU) | Allowed | Competing acoustic evidence; retrospective |
| 6005371 | Havering (P1470.25) | Allowed | C2 need; evidence discipline |
| 6003813 | Derbyshire Dales (25/00426/FUL) | Allowed | Transport/parking evidence |

Notes on the slate:

- St Albans (Green Belt householder archetype) was excluded because its portal is
  registry-blocked; Bradford covers the archetype.
- Several slate cases are also precedent-corpus records — deliberate: their content is
  already deeply analysed, which makes gold-checklist authoring fast and accurate.
- The honesty-trap fixtures (no-strong-ground; support-stance) are assigned when gold
  checklists are written: allowed cases where the council's refusal collapsed at appeal
  are natural support-stance fixtures.
