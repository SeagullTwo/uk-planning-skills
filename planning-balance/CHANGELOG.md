# Changelog — planning-balance

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
- **The Step 4 balance-statement instruction restructured to enforce the bullet discipline
  (#22): framework sentence → harms as weighted bullets (when more than two) → benefits
  sentence → conclusion-and-ask sentence, replacing "a paragraph, two at most" followed by
  a four-item enumeration.** _Why:_ the old instruction was itself a semicolon-run
  packing four required elements into one prescribed paragraph, and outputs mirrored it —
  the representation skills' house-style discipline ("a bulleted list, not a
  semicolon-run") never reached this skill. The instruction now demonstrates the format it
  wants (repo house rule 9 in `../CLAUDE.md`).
- **Step 1 re-mapped to the August 2026 coded NPPF (verified against the official PDF,
  18 August 2026): the "tilted balance" bullet replaced by the location-based presumption.**
  The governing-framework step now runs plan-led (S3(1)(c), with the Annex A(2) very-limited-
  weight caution on materially inconsistent plan policies) → within-settlement S4
  ("substantially outweighed", regardless of plan status) → outside-settlement S5 categories
  (including the S5(1)(j) unmet-housing-need gateway) → the S4(2)(c)/S5(2) refusal-policy
  override, which succeeds the old footnote 7 disapplication. Consequential updates: the
  heritage gateway says "substantial weight" (HE6(1)) not "great weight"; the transport
  gateway is expressed as the TR6(4) refusal directive; the conditions/obligations ask cites
  DM6 and CIL reg 122(2) directly instead of "the para 57/58 tests"; description and README
  match. _Why:_ the 17 August 2026 NPPF abolished the para 11(d) mechanism in substance, not
  just in numbering — an objector-facing balance skill that still asks "is the tilted balance
  engaged?" would have users arguing a test the decision-maker no longer applies, and the
  "significantly and demonstrably" standard it quoted no longer exists. The outline stays
  brief and defers mechanism and citations to `national-planning-policy` per the two-layers
  rule; the obligations tests are cited to the regulation because the Framework no longer
  restates them.
- **"What you need first" now accepts the `policy-compliance-assessment` output** — the plan
  register, the scored policy table, the weight tiers and the accordance statement — with two
  cautions carried into the balance: the -2 to +2 scores are never totalled or averaged, and
  every `?` (policy requirement that cannot be assessed) is a **(B)**. _Why:_ the new skill
  produces the plan-conflict input this skill previously had to reconstruct from triage. The two
  cautions travel with the data deliberately: a numeric table is exactly the kind of input that
  invites a shortcut, and "accordance with the development plan read as a whole" is the judgement
  this skill exists to make — an average would pre-empt it, and treating a `?` as harm would
  weigh an evidence gap as if it were demonstrated impact.

## 0.1.0 — 2026-08-16 — Initial release

### Added
- **The skill itself: a final planning-balance ("so-what") stage** run after triage and
  the representation skills — governing-framework identification (plan-led vs tilted
  balance, footnote 7 disapplication), ground-specific gateways (Habitats Regulations
  hard stop, Green Belt VSC, heritage harm tests, flood Sequential Test, transport
  "severe" bar), an honest harms-vs-benefits weighing, and a four-outcome recommendation
  (refuse / do not determine yet / conditions / balance favours approval). _Why:_ reviewer
  feedback — a planning decision is not the sum of technical defects, and without a final
  balance question the system can produce an impressive list of valid criticisms that
  would not change the decision. Framed as *anticipating* the decision-maker's balance
  because an objector is not the decision-maker.
- **Benefits scrutinised with the same evidence discipline as harms** (unquantified
  economic claims, unsecured affordable housing → reduced weight). _Why:_ the balance has
  two pans; engaging with benefits honestly is both more credible and a source of
  representation material in its own right.
- **Kept to a single SKILL.md, deferring citations to `national-planning-policy` and the
  topic catalogues.** _Why:_ two-layers house rule — this skill owns the *procedure* of
  the balance; the instruments and current paragraph numbers live in the companion skills.
