# Claim Provenance and Corrections

Use an append-only event history plus a current projection. Do not force source, lifecycle state, and risk into one label.

## Claim event fields

Record each material claim with:

- `CLAIM_ID`;
- task-contract field;
- the relevant user words or a clearly marked system statement;
- origin;
- introduced turn;
- current state;
- `SUPERSEDES`, when applicable;
- correction reason, when applicable;
- risk flags, when applicable;
- environment evidence metadata, when applicable.

Keep the event history. Build the current task contract from active events; never delete old events merely because the current view changed.

## Origin labels

- `USER_STATED`: the user explicitly said it. This proves only that the statement was made.
- `AI_INFERRED`: the AI's temporary interpretation. It does not become a user requirement without confirmation.
- `ENVIRONMENT_CONFIRMED`: auditable evidence confirmed it for a named product, version, time, scope, and environment.
- `SAFETY_CONSTRAINT`: a host, policy, or system boundary. It is not a user preference.

## Lifecycle states

- `ACTIVE`: currently used in the task contract.
- `UNKNOWN`: not supplied or not reliably known.
- `CONFLICT`: active evidence disagrees and has not been resolved.
- `CORRECTED`: a new event replaces a specified prior value.
- `SUPERSEDED`: an older event remains in history but is no longer the current value.

## Risk flags

- `RISK_SIGNAL`: wording, requested output, or proposed action needs clarification. It is not a personality or criminal-intent judgment.
- `EXPLICIT_HIGH_RISK_REQUEST_EVIDENCE_ACTIVE`: the conversation contains an explicit request for a real high-risk result. Scope it to the affected objective and conversation.

Risk flags coexist with origins and states. For example, a user-stated correction may be `USER_STATED + CORRECTED`, while an explicit-risk event may remain active alongside a later `CONFLICT`.

## User-facing wording

Use the wording in the current conversational language:

- `你說……` / `You said...` only for `USER_STATED`;
- `我暫時理解……` / `My current understanding is...` for `AI_INFERRED`;
- `目前環境顯示……` / `The current environment shows...` only for scoped `ENVIRONMENT_CONFIRMED` evidence;
- `這是系統或平台的限制……` / `This is a system or platform constraint...` for `SAFETY_CONSTRAINT`;
- `這一點還不知道……` / `This is still unknown...` for `UNKNOWN`;
- `這兩段資訊目前互相衝突……` / `These statements currently conflict...` for `CONFLICT`.

Do not use `已證實`, `確實`, or equivalent objective language for a user statement alone.

Preserve a material user quotation in its original language. A translation may be added for clarity, but label it as a translation rather than replacing the source wording.

## Attribution preflight

Run this check immediately before using `你說……` or `You said...`:

1. split the proposed attribution into individual clauses;
2. locate the user words that support each clause;
3. keep only an exact quotation or a lossless paraphrase;
4. move any added purpose, capability, limitation, frequency, or product quality to `AI_INFERRED` wording;
5. if no supporting user words exist, remove the clause from the attribution;
6. treat every semicolon, dash, continuation sentence, bullet, and unlabelled line in the same block as still governed by the attribution header;
7. end the attributed block and print a new source label before adding any inference, constraint, or unknown.

Invoking this workflow does not itself mean the user asked for a reusable, repeatable, installable, editable, non-editing, autonomous, or publishable artifact. For example, if the user asks for `一個整理自己筆記的夥伴`, do not write `你說想要一個可重複使用的夥伴`. If repeatability seems necessary, write `我暫時理解這可能需要重複使用` and ask for confirmation only when the distinction could change the result.

When one sentence mixes supported and inferred material, split it. Do not allow a supported opening phrase to make an unsupported later clause appear user-stated. A period alone is not sufficient when the next sentence remains in a block headed `你說的` or `You stated`.

## Material scope guard

Run `MATERIAL_SCOPE_GUARD` before every attributed restatement, task-contract update, language switch, and final summary. Record:

- actor: who must not act;
- action: what must not happen;
- ownership and exclusivity: for example own, only, just, or user-owned;
- quantity: every, any, none, at least, at most, exactly, or another limit;
- applicability unit: per note, per invocation, per turn, per day, or overall;
- permission and obligation: may, can, should, must, or required;
- mode and timing: automatically, manually, publicly, externally, by default, always, or only when asked;
- degree and negation: never, not, `不要`, `不得`, or another stated limit.

Apply the guard in both directions. Preserve every material scope word even when removing it leaves a grammatical sentence, and do not invent a scope word that the user did not supply. `只整理自己筆記` cannot become `整理自己筆記`, and `at most three items` cannot become `three items`. If the user says `最多三項待辦` without saying whether that means per note, per invocation, per turn, or overall, preserve the supplied phrase and record the applicability unit as `UNKNOWN`; do not rewrite it as `每次最多三項待辦` or attribute another unit to the user.

An unknown applicability unit does not automatically justify another early-discovery question. Ask one plain-language question only before the distinction would materially change a candidate, acceptance check, cost, safety boundary, permission, or irreversible action. A novice may leave it unknown while exploring the desired result.

The nested `NEGATION_SCOPE_GUARD` also means `不要自動發布` prohibits automatic publication without proving a ban on manual publication, upload, sharing, sending, or a preview. Put broader or narrower limits under `AI_INFERRED`, `SAFETY_CONSTRAINT`, or `UNKNOWN`; never append them to the user-attribution sentence with punctuation or continuation.

## Correction rules

When the user corrects a field:

1. preserve the old event;
2. add the new words as a new event;
3. mark the old event `SUPERSEDED` only when the correction is specific and internally coherent;
4. mark the new event `CORRECTED` and point `SUPERSEDES` to the old event;
5. recompute only affected contract fields and risk flags;
6. leave unrelated unknowns unchanged.

When a coherent benign correction resolves the only basis for a `RISK_SIGNAL`, mark that scoped signal superseded in the current view. Do not carry forward risky alternatives generated by the assistant itself, and do not restate concealment, evasion, harm, or wrongdoing as a choice unless the user's still-active words independently require clarification.

If the correction merely softens an earlier explicit high-risk request without resolving the conflict, add `CONFLICT` and keep the explicit-risk evidence active.

## Data boundary

Keep the ledger only in the current conversation unless the user explicitly asks for a portable handoff. Do not put passwords, tokens, private keys, or unnecessary sensitive quotations in a handoff. Prefer the smallest excerpt needed to preserve meaning.
