# 聽人家說啦！ / Hear Me Out

**Hear Me Out** is the public project for **Skill Companion**, its current installable Skill. It helps a person who does not know programming or AI terminology turn an everyday wish, frustration, or example into an honest, testable Skill concept—or discover that a smaller non-Skill solution is better.

**Tell it plainly. Find what fits.**

[繁體中文說明](README.zh-TW.md) | English

Current release target: **0.1.0 Prototype**.

This repository is the separately authorized implementation stage of an earlier human-relayed design process. It does not include the private debate transcripts or personal test conversations used during design.

## What it does

- Starts from a positive wish, a problem, or a concrete life example.
- Supports Traditional Chinese and English directly, including deliberate language switching without discarding the current task state.
- Asks one meaningful question at a time and allows `不知道`, skip, correction, pause, or end.
- Keeps user statements, AI inferences, platform evidence, safety constraints, unknowns, and corrections distinct.
- Treats dangerous wording as a reason to clarify, not as proof about a person's character.
- Preserves explicit high-risk request evidence without allowing softer wording to unlock harmful operational help.
- Creates an editable task contract and chooses the smallest plausible candidate form.
- Labels untried alternatives as untested instead of promising usefulness.
- Requires the user to explain the result, next step, and unproven parts in their own words.

## How it differs from Skill Creator / Skill Creation

In this document, **Skill Creator / Skill Creation** means the bundled `skill-creator` workflow inspected in the tested Codex environment and the labels observed when that host routed unselected creation requests. Names and automatic routing may differ in another Codex build.

The decisive difference is where each workflow begins:

- **Skill Companion is an upstream discovery and decision layer.** It helps determine what result the person actually wants, whether a Skill is the right form, and what must remain unknown or unproven.
- **Skill Creator is a downstream construction layer.** Once the creation intent and requirements are sufficiently clear, it helps plan, initialize, edit, validate, and iterate a Skill package.

They are complementary, not substitutes.

| Question | Skill Companion | Bundled Skill Creator / observed Skill Creation |
|---|---|---|
| Typical starting point | An everyday wish, frustration, or example with missing technical language | An intent to create or update a Skill |
| Main decision | What outcome is wanted, whether it should be a Skill, and what evidence would count | How to structure, scaffold, edit, validate, and forward-test the Skill |
| Possible outcome | A task contract, checklist, template, prompt card, platform-neutral specification, limited uninstalled draft, or an honest decision that a Skill is unnecessary | A created or updated Skill folder and its supporting resources when file changes are authorized |
| Treatment of uncertainty | Keeps user statements, AI inference, platform evidence, constraints, corrections, and unknowns separate | Uses concrete examples to gather enough requirements for implementation and iteration |
| Prototype action boundary | Conversation only: no file writing, installation, publication, account access, or external action | May create or edit files and run validation as part of an authorized build workflow |
| Intended handoff | A clearer, testable candidate or specification can be handed to a construction workflow | Receives a sufficiently clear creation task and carries it into implementation |

Skill Creator also asks for concrete examples and protects validation integrity. The difference is not that it skips clarification or testing; it is that its workflow is already oriented toward creating or updating a Skill, while Skill Companion may still decide that another form is better.

## Why use Skill Companion

Use Skill Companion when the cost of building the wrong thing is greater than the cost of a short discovery conversation. Its intended value is to reduce silent guessing before implementation:

- the person can describe a real-life result without knowing Skill terminology;
- important words such as `only`, `own`, `at most`, and `do not automatically publish` remain scoped to what the person actually said;
- unsupported capabilities and inferred restrictions stay visibly unproven;
- the workflow may recommend a smaller non-Skill alternative instead of forcing every wish into a Skill;
- the person may say `不知道`, correct the interpretation, pause, save an incomplete summary, or end.

This is a design rationale, not proof that the workflow is low burden or useful. The current evidence is limited and reported separately.

## Who it is for

Skill Companion is a reasonable fit for someone who:

- has little or no programming, AI-workflow, or Skill-authoring experience;
- knows a desired result or recurring inconvenience but cannot yet write a technical specification;
- has important boundaries that must not be silently broadened or narrowed;
- wants plain-language questions and an honest account of what remains unknown;
- is helping another person express requirements without supplying the answers for them;
- has technical experience but still faces ambiguous or disputed requirements;
- is willing to discover that a checklist, template, prompt card, or ordinary answer may be better than a Skill.

It is usually not the shortest path for someone who already has a complete implementation specification and only wants files created, or for someone who wants a one-off answer rather than a reusable workflow. It is also not an installer, security certification, or substitute for tool, permission, and real-task testing.

## Common failure modes

An incomplete or unsuitable outcome is not always a workflow failure. Honest refusal, a smaller alternative, or an incomplete summary can be correct behavior. There is not yet enough evidence to rank causes by frequency; known or plausible failure modes are:

| Observable problem | Likely cause | Honest handling |
|---|---|---|
| Skill Companion does not start | It was not explicitly selected, the host did not load it, or a different system workflow handled the request | Start a fresh task, verify the loaded copy, and select `$skill-companion` explicitly |
| The conversation ends without a candidate | The desired result, success condition, permission, or other blocking field remains unknown, or the person chooses to stop | Preserve an incomplete summary and state exactly what could reopen the work |
| The conversation feels tiring or repetitive | Too many material unknowns are being resolved too early, the same point is being rechecked, or the workflow does not fit a one-off request | Pause, record the actual journey burden, and revise only from observed evidence rather than claiming the user failed |
| The requested Skill cannot access an account, Drive, network, tool, or device | Capability, permission, platform, or integration evidence is absent or outside this instruction-only prototype | Produce a platform-neutral specification or untested alternative; do not claim access or installation |
| A candidate looks reasonable but does not help in practice | Reading or approving it was mistaken for utility evidence | Run a predefined small real task and record the observable result |
| The output is only a specification when implementation was expected | Discovery is complete but construction has not been authorized or handed off | Pass the confirmed specification to Skill Creator or another authorized implementation workflow |
| Language, attribution, negation, or scope drifts | The model did not follow a material runtime rule | Preserve the transcript, fail the matching predefined case, correct the rule, and retest on a new artifact hash |
| A risky, contradictory, or unsupported method is rejected | The requested method crosses a boundary even if the underlying wish may be feasible | Preserve the feasible wish, offer only a safe candidate direction, or stop; a compliant boundary is not itself a failure |

## What it does not prove

The repository currently contains a candidate Skill and project-level validation tools. Their existence does not prove low burden, host loading, behavior fidelity, usefulness, runtime safety, installation, or official certification.

The installed Skill is instruction-only. It has no runtime scripts, MCP dependency, network operation, or external action. That does not turn Skill text into a sandbox; the host still controls available tools and permissions.

## Repository layout

```text
.agents/skills/skill-companion/   Installable repo-scoped Skill
  SKILL.md                        Core workflow
  agents/openai.yaml              UI and explicit-invocation policy
  references/                     Detailed runtime rules
.github/workflows/validate.yml    Cross-platform static validation
docs/design-basis.md              Sanitized accepted design basis
tools/validate_repo.py            Dependency-free repository validator
tests/test_validator.py           Mutation tests for the validator itself
validation/cases.json             Blinded-evaluation case definitions
validation/README.md              Reproducible validation procedure
validation/report-template.md     Evidence report template
reports/validation-0.1.0.md        Current project self-validation result
```

The test expectations remain outside the installed Skill so a fresh evaluator cannot read the intended answers from the Skill itself.

## Try it from a clone

1. Download or clone this repository.
2. Open the repository as the working folder in Codex.
3. Start a new task.
4. Invoke `$skill-companion` explicitly and describe one wish, problem, or life example.

The Skill disables implicit invocation. A matching request without `$skill-companion` should not activate this workflow automatically.

## Install from GitHub after publication

Prefer the built-in `$skill-installer` and give it the pinned GitHub tag plus this Skill path:

```text
Use $skill-installer to install the Skill from
https://github.com/tokaiteo0420/hear-me-out/tree/v0.1.0/.agents/skills/skill-companion
```

This URL is the planned tagged release path. It will not work until the repository is published and tag `v0.1.0` exists. Test installation in a fresh task; do not treat a copied folder as proof that the host loaded it.

For manual installation, copy only `.agents/skills/skill-companion` to the user-skill location supported by the installed Codex version. The current public Codex guide documents user-scoped authoring under `$HOME/.agents/skills`; installer-managed locations may differ by build. Record the observed path and host version instead of assuming equivalence.

Official references:

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI skills examples](https://github.com/openai/skills)

OpenAI's current guidance prefers a plugin when broader installable distribution is needed. This prototype remains a standalone GitHub Skill; plugin packaging is a separate future decision.

## Validate locally

With Python 3.10 or newer:

```text
python tools/validate_repo.py
```

For a planned public release, run:

```text
python tools/validate_repo.py --strict-release
```

Static validation checks packaging, metadata, references, baseline rules, test-case schema, execution-scope safety, portability, and common secret or local-path leaks. It cannot prove host loading or model behavior. Follow [the validation procedure](validation/README.md) for fresh-session and human evidence.

To confirm that the validator itself rejects common packaging mistakes:

```text
python tests/test_validator.py
```

See the [current validation report](reports/validation-0.1.0.md) for passed checks, preserved failures, and remaining release blockers.

## Human-account testing boundary

Do not test explicit physical or psychological attack, threat, harassment, humiliation, coercion, or manipulation prompts on a personal or general human account. Do not quote, translate, rephrase, retry, role-play, or reconstruct them for a participant.

Every case declares an `execution_scope`. Controlled-only cases require an authorized controlled safety evaluator; when that environment is unavailable they remain `NOT_RUN`. If the host intervenes, stop immediately, do not retry, and record `NOT_SCORABLE_HOST_INTERVENTION` rather than treating the intervention as Skill evidence.

## Privacy boundary

- Use synthetic test fixtures in this public repository.
- Do not commit private chat transcripts, local absolute paths, account data, credentials, or real sensitive user content.
- Keep raw human-study evidence in an access-controlled location unless every participant has explicitly agreed to publication and the data has been reviewed for re-identification risk.

## License

This project uses the [MIT License](LICENSE), matching the license used by Matt Pocock's `skills` repository that contains Grill Me. The license terms are the same; this repository keeps its own neutral copyright notice.

## Validation language

Call the result **project self-validation**, not official OpenAI certification. Report each evidence level separately and preserve failures, blocked cases, and untested dimensions. Traditional Chinese, English, and language-switching cases are part of the static test specification, but repeated host behavior still needs to be observed before claiming bilingual behavior verification.
