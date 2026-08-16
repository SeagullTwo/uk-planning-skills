# Changelog — heritage-representation

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## 0.1.0 — 2026-08-14 — Initial release

First version, built to the same pattern as the ecological- and transport-representation
skills: (1) evaluate the heritage evidence, (2) map deficiencies to the statutory duties and
national policy/guidance, and (3) draft a concise representation — or advise that none is
warranted. Structure: `SKILL.md` + `references/` (`deficiency-catalogue.md`,
`national-guidance.md`, `house-style.md`, `objection-template.md`). Key design decisions:

### Added
- **The two heritage framing points as the spine:** *the level of harm drives the test*
  (substantial vs less-than-substantial), and *"less than substantial" is not "neutral"* (the
  statutory duties require considerable importance and weight; the NPPF requires great weight).
  _Why:_ these are the two things applicants and officer reports most often get wrong, and
  where a well-pitched representation has the most leverage.
- **A web-verified guidance catalogue** — the LB & CA Act 1990 duties (ss.66/72 verbatim), the
  NPPF Chapter 16 harm tests **with the Dec 2024 +13 renumbering flagged**, the PPG, Historic
  England GPA/HEAN guidance (with the setting method), and the case law (*Barnwell Manor*,
  *Mordue*, *Palmer*, *Bramshill*, *South Lakeland*). _Why:_ heritage turns on the precise
  statutory duty and the correct harm test; citing the wrong paragraph or missing the "great
  weight" duty loses the point. Time-sensitive items (NPPF under revision; two case citations
  to confirm) are flagged ⏳.
- **Deficiency catalogue** covering significance (assessed, and proportionately, incl.
  setting/group value), harm characterisation, the statutory-weight and public-benefit balance,
  conservation-area preserve-or-enhance, archaeology, and consultee engagement.
- **House style + annotated template** with the bullet / lettered-sub-point discipline built in
  from the start (learned from the transport skill), so drafts are scannable.

### Changed / Security
- **Scoped to heritage, England-focused, explicitly not legal advice; no warranty; human
  review required; public-document-in-your-name flag.** _Why:_ the same user-protection
  disclaimers as the other skills.
- **Built generic and public-safe** — no case/campaign/consultant/place fingerprints; local
  policy references left as `[insert …]`. _Why:_ repo house rules.
