# Conversation and Journey Burden

Use this reference to run the conversation without hiding its real cost from the user.

## Atomic response demands

A response demand is any prompt that requires the user to answer, choose, confirm, correct, consent, teach back, or supply permission before progress can continue. Count it even when it has no question mark.

Ask for one conceptual judgment per response demand. A short explanation may precede it, but do not bundle independent decisions.

Count these categories separately:

- discovery;
- risk clarification;
- summary confirmation;
- correction;
- permission or data choice;
- candidate choice;
- teach-back;
- recovery after confusion.

Do not equate a question limit with total journey burden or successful discovery.

## `JOURNEY_BURDEN_LEDGER`

Maintain these fields for the current conversation:

| Field | Counting rule |
|---|---|
| `RESPONSE_DEMANDS` | Count every required user response, grouped by category. |
| `USER_TURNS` | Count user messages in this workflow. |
| `ASSISTANT_TURNS` | Count assistant messages in this workflow. |
| `TOTAL_TURNS` | Sum user and assistant turns. |
| `CONFUSIONS` | Count explicit misunderstanding, uncertainty about instructions, or requests for simpler wording. |
| `CORRECTIONS` | Count user corrections that change a recorded field. |
| `BACKTRACKS` | Count returns to a previously accepted field. |
| `HELP_REQUESTS` | Count explicit requests for explanation or an example. |
| `EXIT_OFFERS` | Record where continue, pause, save, or end was offered. |
| `EXIT_POSITION` | Record where the user actually stopped, if applicable. |
| `INCOMPLETE_REASON` | Record the observable reason; do not infer motivation. |

For `ACTIVE_TIME`, waiting time, reading volume, or timestamps, attach a measurement source:

- `OBSERVED`: the host or transcript exposes a reliable value.
- `USER_REPORTED`: the user reports it.
- `UNAVAILABLE`: no reliable value exists.

Never estimate an exact unavailable measurement and present it as observed.

## Checkpoints

The prototype has no evidence-based burden threshold. Use this testable implementation default without calling it optimal:

- Show a checkpoint after the third response demand and every third response demand thereafter.
- Show one immediately after confusion, correction of the core objective, or an explicit sign of fatigue.
- Show one before any teach-back sequence.

At a checkpoint, display only:

1. what is known;
2. what remains unknown or conflicting;
3. what the user would receive if they stopped now;
4. one choice: continue, pause and save, or end.

The checkpoint choice itself is a response demand.

## Pause, save, and resume

When the user pauses, produce a plain-language handoff containing the current task contract, unknowns, conflicts, candidate state, and ledger totals. State that the next conversation must be given this handoff because this Skill does not guarantee cross-task memory.

When a user resumes from a handoff, treat its contents as `USER_STATED` unless the current environment independently confirms them. Ask one atomic confirmation before relying on a material field.

## Completion boundary

Conversation completion requires both:

- a task contract with no unresolved field that blocks its selected candidate; and
- successful teach-back of the current result, next step, and what remains unproven.

Completion says nothing about implementation, installation, usefulness, general safety, or future behavior.
