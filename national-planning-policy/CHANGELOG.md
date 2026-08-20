# Changelog — national-planning-policy

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Added
- **Edition register now routes explicit prior-edition requests to the frozen archive at
  `../nppf-2024-12/` (#31), behind an ask-first gate.** _Why:_ the August 2026 re-map made
  the December 2024 edition skills reachable only through git history; users doing
  retrospective work (pre-Aug-2026 decisions, era-pinned analysis) need them on main. The
  gate is deliberately narrow — only an explicit request to *work under* the old framework
  triggers the offer; incidental old paragraph numbers in dated documents keep using the
  current skills plus the crosswalk, and live applications always use the current edition.
  The archive is frozen (no re-mapping, no fix backports — see the new house rule in
  `../CLAUDE.md`), and its skills carry `-nppf-2024-12` name suffixes so installed copies
  cannot collide with current ones.

### Changed
- **The decision-making core is re-mapped to the 17 August 2026 coded-policy edition and
  re-verified against the official PDF (18 Aug 2026).** Every citation now uses the new
  policy codes: s.38(6) frame → Introduction paras 1/3 (with footnotes 1–2); presumption →
  S3–S6; emerging-plan weight and prematurity → DM4; conditions → DM6(1)–(3); obligations →
  DM6(4) + CIL reg 122(2). _Why:_ the whole value of the shared layer is that its citations
  are current; quote-verified against the extracted PDF text rather than memory (house rule
  3), because the restructuring changes substance as well as numbering.
- **The core now describes the new presumption mechanism, not a renumbered tilted
  balance.** The August 2026 edition replaces the para 11(d) out-of-date-policies trigger
  with a location-based presumption: S4 (within settlements — approve unless benefits
  "substantially outweighed") applies regardless of plan status; S5 (outside settlements —
  a closed list of approvable categories, with the old footnote 8 housing-supply triggers
  surviving only as the S5(1)(j) unmet-need gateway and the GB7 grey-belt gateway); the old
  footnote 7 disapplication becomes the S4(2)(c)/S5(2) refusal-policy override; S6 shields
  recent neighbourhood plans; Annex A(2) gives "very limited weight" to plan policies
  materially inconsistent with the new Framework. _Why:_ presenting these as renumberings
  would misstate the law of the balance — the change-of-mechanism is exactly what a
  representation must get right, so the core states the new mechanism and flags each
  substantive difference explicitly (including that "great weight"-style wording changes
  elsewhere make old-edition quotes unsafe).
- **Conditions and obligations rows corrected for substance.** DM6(1) expresses the old six
  tests as four merged limbs (quote the four-limb wording); the NPPF no longer restates the
  CIL reg 122(2) three tests, so the core directs citing the regulation itself. _Why:_
  quoting the six-test or reg-122 formula "from the NPPF" would now be a false attribution
  even though the substance survives.
- **Edition register rewritten:** the 17 August 2026 edition is recorded as in force,
  verified and re-mapped; the register flags that the official text is currently PDF-only
  (⏳ HTML "accessible version" pending — re-check at run time); notes the topic catalogues
  are being re-mapped to the new codes in the same change set; and keeps the rule that
  applications determined before 17 August 2026 are read against the edition in force at
  determination, now pointing at the crosswalk for the translation. _Why:_ the register is
  the single point the companion skills check first, so it must say precisely what has and
  has not been re-verified, and where the old numbers went.
- **Verification protocol and "two layers" section updated to the coded-policy world** —
  the protocol's renumbering warning now cites the August 2026 restructuring as the live
  example and the PDF-only status; the topic-layer pointers use the new chapter codes
  (N1–N6, TR1–TR8, HE1–HE10, F1–F9). README updated to match. _Why:_ the skill must not
  itself carry the stale numbering it warns against.

- **Edition register updated: the NPPF was republished on 17 August 2026**, replacing the
  December 2024 edition with the anticipated coded-policies restructuring. The register now
  records the new edition as in force, marks the decision-making core (still keyed to the
  December 2024 text) as pending re-mapping, and adds the rule that past decisions are read
  against the edition in force at their determination date. _Why:_ verified first-hand on
  the gov.uk publication page (18 Aug 2026), after three independent assessment runs each
  discovered the new edition at run time. Re-mapping the core and every topic catalogue to
  the new policy codes is a repo-wide job tracked in its own issue; until it is done the
  register must say loudly that every stored paragraph number is stale — a wrong-but-precise
  register is exactly the defect the verify-before-citing protocol exists to prevent.
  *(Interim state: superseded within this change set by the re-mapping entries above — the
  core is no longer "pending re-mapping".)*
- **The "two layers" section now names `policy-compliance-assessment` as the owner of the
  *local* tier**, and states the hierarchy explicitly: adopted local policies are the council's
  own and have primacy, the Framework is a material consideration alongside the plan rather than
  above it. _Why:_ with a skill now dedicated to local-plan assessment, this skill needed to say
  where its own boundary lies — and to guard against the failure mode the split invites, where a
  reader takes the most detailed catalogue in the repo (this one) for the most important tier.
- **"When to use" now lists the two new policy skills as callers.** _Why:_ they are the heaviest
  consumers of the edition register — one for the national and emerging tiers of its policy
  table, the other for verifying every citation before a draft is sent.
- **A/B/C paragraph now also points to the `planning-balance` companion skill.** _Why:_
  the balance skill is where the assembled case is weighed; the cross-reference completes
  the chain.

### Added
- **`references/nppf-crosswalk-2026.md` — December 2024 → August 2026 crosswalk** covering
  every NPPF paragraph number the repo's skills actually cited (core, flood, transport,
  heritage, ecology), with concept labels, the new policy codes, and notes distinguishing
  pure renumberings from substantive changes (e.g. TR6(4) inverting the old para 116
  refusal framing; HE6(1) "substantial weight" replacing "great weight"; HE5(2)(c) defining
  substantial harm; N6's new Environmental Delivery Plan / nature restoration levy routes;
  the three-criteria exception test in F6; DM6/reg 122(2)). Marks "no direct successor"
  where a cited provision (paras 11(d), 12, footnote 7) has none, with the nearest policy.
  _Why:_ retrospective work on pre-August-2026 decisions must cite the edition in force at
  determination, and the re-mapping itself needed an auditable record — a table that
  papered over policy changes as renumbering would quietly falsify representations, so the
  notes call out substance changes loudly.

## 0.1.0 — 2026-08-16 — Initial release

### Added
- **The skill itself: a central national-policy layer** with (1) an edition register and a
  verify-before-citing protocol, and (2) the shared decision-making core (s.38(6)/paras
  2, 12, 48; the para 10–11 presumption with footnotes 7 and 8; para 49 emerging-plan
  weight; para 57 conditions tests; para 58 / CIL reg 122(2) obligations tests). _Why:_
  reviewer feedback — NPPF knowledge distributed across the topic catalogues lets skills
  drift out of sync as editions change; the December 2025 draft revision (final expected
  Summer 2026) restructures the Framework into coded policies, so a single re-verification
  point matters more than ever. Structured as a companion *skill*, not a shared reference
  file, so each skill folder stays individually copyable (repo convention).
- **All citations verified against the live gov.uk text on 16 Aug 2026**, not from memory
  (house rule 3). The verification pass immediately caught a live defect: the transport
  catalogue cited the conditions tests as "para 56" (a December 2023 number) — fixed in the
  same change, which is the skill's rationale demonstrated.
- **Two-layers rule stated in the skill:** this layer owns the shared core + register; the
  topic catalogues own their chapters and professional instruments. _Why:_ prevents the
  duplication this skill exists to remove.
