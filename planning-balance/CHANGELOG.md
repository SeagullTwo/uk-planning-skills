# Changelog — planning-balance

Design decisions per revision, newest first. See `../CLAUDE.md` for the format and the
house rules. The **_Why_** lines record the rationale so a future editor understands the
intent.

## Unreleased

### Changed
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
