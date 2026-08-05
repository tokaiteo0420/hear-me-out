# Task Contract, Teach-Back, and Candidate Artifacts

## Task contract

Create an editable plain-language contract with these fields:

- desired observable result;
- user-proposed method, if any;
- unacceptable results;
- final decision owner;
- inputs and data sources;
- data owner and affected people;
- downstream use;
- required tools, permissions, and external actions;
- observable success;
- observable failure;
- unknowns, conflicts, AI inferences, and safety or platform constraints.

Link every material field to a claim event. Never fill an unanswered material field from tone, occupation, dialect, spelling, or an unrelated answer.

## Plain-language contract view

Show no more than four groups by default:

1. `你說的`;
2. `我暫時理解的，請你修正`;
3. `系統或平台必須遵守的限制`;
4. `還不知道或互相衝突的`.

Put an item in only one visible group while preserving its complete audit dimensions internally.

## Candidate forms

Choose the smallest form that could satisfy the contract:

- wish and unknowns summary;
- manual checklist;
- fill-in template;
- reusable prompt card;
- platform-neutral specification;
- platform-specific but uninstalled Skill draft;
- separately validated and installed Skill.

Do not select the last form without external evidence. Do not select any Skill merely because the project began with the word `Skill`.

Ask which tradeoff matters when it changes the choice: portability, repeated invocation, fewest steps, platform integration, or maintenance burden.

## Prototype Skill-draft boundary

Generate a platform-specific draft in this prototype only when all are true:

- the user explicitly wants a reusable Skill workflow;
- the target is a text-only workflow over user-owned, non-sensitive text;
- behavior is limited to formatting, listing, or faithful summarization;
- activation is explicit;
- scripts, MCP, network, and external processes are unnecessary;
- success and failure are observable;
- no blocking unknown or conflict remains.

Otherwise create a platform-neutral specification or an untested alternative card.

For a platform-specific draft, record a `TARGET_PLATFORM_CONTRACT` with product, version if known, required file format, discovery location, invocation method, validator source, and every unknown. User assertion alone is not environment confirmation.

## Skill draft contents

A candidate Skill draft must state:

- purpose;
- appropriate and inappropriate uses;
- required inputs;
- output format;
- ordered workflow;
- unknown handling;
- limitations;
- data and tools;
- denied-permission and failure behavior;
- stopping conditions;
- beginner invocation and disable instructions;
- matching acceptance cases.

Preserve negations and exclusions exactly. Before delivery, compare the draft against the task contract for omitted requirements, reversed negations, invented tools, and fabricated fallback behavior.

## Teach-back gate

Ask three separate response demands, one at a time:

1. `請用自己的話說說看：你現在會先拿到什麼？`
2. `下一步會發生什麼？`
3. `有哪些事情還沒有發生，或還沒有被證明？`

Judge only whether the answer matches the current contract. Do not require the user's wording to match the AI's wording.

If the user answers only `對`, `知道了`, gives an incorrect answer, or says `不知道`, mark that item `COMPREHENSION_UNRESOLVED`. Explain it with fewer words or one concrete example, then recheck only that item. If it remains unresolved, pause and provide an incomplete handoff.

## Candidate status

Creating text gives at most `ARTIFACT_CANDIDATE_CREATED`. Reading, accepting, or praising it does not prove it useful.

After a predefined small trial is actually performed and an observable result is recorded, the alternative may be labeled `USER_TESTED_ALTERNATIVE_WITHIN_CASE`. State the exact user, case, environment, and result scope; never generalize beyond them.
