# Documentation policy

Write for people and agents who know nothing about Holler. Help them install it,
use it for everyday work and recover from common problems. Holler serves local
AI agents across coding, design, product, go-to-market and other disciplines.
Use varied examples; do not define the product by one profession or client.
Distinguish an agent's role from the clients Holler can currently connect to.

**Less and correct.** Include a detail only when it helps a reader take an action,
understand a product behavior or make a necessary decision.

## Minimal disclosure

Describe the external product. Do not include internal plans, team conversations,
work assignments, test-run narratives, implementation history, private paths or
release preparation. Keep that material outside this documentation repository.
Do not copy internal documents wholesale and add a disclaimer.

Explain a known limitation by its affected version, observable symptom and next
step. Keep test infrastructure, scenario identifiers, debugging hypotheses and
raw evidence out of the user guide. Minimal disclosure must not hide a limitation
that affects the reader's ability to use the product.

## Accuracy and scope

- Document released behavior. Add a feature's instructions when readers can
  actually install and use it.
- State the version and prerequisites where they change the instructions.
- Verify commands against the released interface. Do not publish proposed or
  untested recovery commands.
- Do not infer a supported version range from a package minimum or one test.
- Do not describe successful installation as proof of working message delivery.
- If a complete user journey is unavailable, state the limitation once and give
  the available next step. Do not fill the gap with speculative instructions.

## Write for the reader

Start with the task and expected result. Define product terms before using them.
Put tool fields in the agent guide; use plain-language instructions in human
guides. Introduce each concept where it becomes useful.

Prefer a short working example to a catalog of possible features. Show only the
permissions and recovery details needed for the action. Examples must not contain
real identities, credentials, message bodies or personal paths.

## Review every change

Ask whether a new reader can follow the page without knowing the team or its
plans. Check that each detail belongs in external documentation, that each command
is available in the stated version, and that the expected outcome is accurate.
Remove sentences that only explain how the product was developed or reviewed.

Automated checks support this review; they cannot establish that a claim is true
or that a user can complete the workflow.
