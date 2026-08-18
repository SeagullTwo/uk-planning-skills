# policy-compliance-assessment

Assess a UK planning application against the policies that actually govern it — starting, as
the statutory framework does, with the **formally adopted development plan**.

The skill works in three moves:

1. **Identify and verify the adopted development plan** for the relevant local planning
   authority — the adopted local plan (often several documents), any **made** neighbourhood
   plan, the minerals and waste plans, and in London the spatial development strategy — with
   the adoption dates, the schedule of superseded and saved policies, and the site's position
   on the policies map. "Adopted" is a formal term: a draft, submitted or examined plan is not
   adopted, and neither is a supplementary planning document.
2. **Assess** the proposal against each relevant policy, quoting the requirement and pointing
   at the evidence in the application documents.
3. **Score and conclude** — a policy-by-policy table scored from **-2** (significant conflict)
   to **+2** (strongly aligned), with `?` where the application lacks the evidence the policy
   requires, plus a reasoned conclusion on accordance with the development plan **read as a
   whole**.

Adopted policies are the **local authority's own** — written, examined, adopted and published by
the council, on its own website, under its own numbering — and they carry **primacy** in the
decision. National policy (NPPF/PPG) and any **emerging** plan are assessed in a separate,
explicitly lower-weight tier: material considerations that inform the decision without
displacing the plan.

Two rules do most of the work:

- **The scores are never totalled or averaged.** Accordance with the plan read as a whole is a
  planning judgement; one significant conflict with the spatial strategy can outweigh eight
  compliances on matters of detail, and an average would invert the answer.
- **Missing evidence is not conflict.** Where the application does not contain what a policy
  requires, the honest output is "cannot be assessed" — which supports a different ask.

Feeds **`policy-representation`** (which drafts the representation, in support or objection)
and **`planning-balance`** (which weighs the case). Takes its NPPF/PPG citations from
**`national-planning-policy`** and leaves topic-specific technical evaluation to the
`heritage-`, `transport-`, `flood-` and `ecological-representation` skills.

> **Not legal advice. No warranty. England only.** Policy interpretation is ultimately for the
> decision-maker. Plans are adopted and superseded continuously, so the plan must be
> re-resolved and every policy re-quoted at run time. Output requires human review; see the
> repo README for the full disclaimer.
