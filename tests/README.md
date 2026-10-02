# Tests

Test fixtures and harness for the planning skills. The full design — what "better" means,
how fixtures are chosen, the judging protocol, and the out-of-sample cohort scheme — is in
[`../docs/testing-design.md`](../docs/testing-design.md). Read that first.

## Layout

| Path | What it is |
|---|---|
| `fixtures/<case-slug>/input/` | The application documents a skill run sees, plus `manifest.json` (provenance, sha256s, era pin) |
| `fixtures/<case-slug>/truth/` | Officer report, inspector decision letter, `gold.yaml` — **never passed to a skill run** |
| `harness/` | The plain-Python harness scripts (see the design doc's Implementation section) |
| `harness/contamination.csv` | The ledger of every appeal case whose decision content has ever been read, coded, fixtured or used as a precedent — the out-of-sample sampler excludes these |
| `runs/<git-sha>/<case>/` | Run outputs and manifests (kept for audit) |

## Rules

- Fixture documents are **public records as published by the council**; every fixture
  carries a provenance manifest. See house rule 7's carve-out in `../CLAUDE.md`.
- `truth/` material must never reach a skill run's inputs, and blind runs have network
  tools disabled — the fixture documents are the run's whole world.
- Any case whose decision letter gets read for any purpose is added to
  `harness/contamination.csv` in the same change.
