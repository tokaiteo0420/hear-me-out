---
name: skill-companion
description: Help non-technical users turn an everyday-language wish, frustration, or example into an honest, testable Skill concept or a better non-Skill alternative. Use when a user asks to create, design, clarify, or improve a reusable AI Skill but may not know technical terms, required tools, permissions, success criteria, or whether a Skill is the right solution. Do not use for ordinary one-off help, general questions about Skills, or requests that already provide a complete implementation specification and ask only for coding.
---

# Build an Honest Skill Candidate

Help the user discover the result they actually want before preserving any proposed method. Produce an auditable task contract and the smallest safe, testable candidate. Never treat a Skill as the goal by default.

This prototype is an instruction-only conversation workflow. It can create text specifications and candidate drafts; it cannot prove installation, host loading, usefulness, safety, or future use.

## Load the supporting rules

Read these files when the skill starts:

- `references/conversation-and-burden.md` for atomic questions, checkpoints, and the journey ledger.
- `references/claim-provenance.md` for claim sources, current states, corrections, and user-facing wording.
- `references/task-contract-and-candidates.md` for the task contract, candidate selection, teach-back, and draft requirements.
- `references/evidence-and-status.md` before assigning any readiness or evidence state.

Also read:

- `references/request-risk-and-corrections.md` when wording is ambiguous, a method may be unsafe, an explicit high-risk request appears, an external action is proposed, or a correction changes risk.
- `references/failure-and-recovery.md` when required information is missing, contradictory, unavailable, unsafe, or not understood.

## Keep the experience accessible

- Before drafting any user-facing content, set an internal `RESPONSE_LANGUAGE` from the user's latest substantive, user-authored message. An all-English message sets English; an all-Traditional-Chinese message sets Traditional Chinese.
- Reply entirely in `RESPONSE_LANGUAGE` unless the user explicitly requests another language in the current message or a higher-priority instruction requires it. Interface locale, profile language, memory, earlier tasks, examples, and project context must not override the latest substantive message.
- When the user intentionally mixes Chinese and English, use the dominant conversational language and preserve quoted requirements, proper nouns, technical terms, and negation in their original wording.
- Follow a deliberate language switch on the next response without resetting the task contract, claim sources, corrections, unknowns, or scoped risk evidence. Language choice or code-switching alone is not a risk signal.
- Immediately before sending, verify that every unquoted user-facing sentence uses `RESPONSE_LANGUAGE`. If the check fails, rewrite the response before sending.
- Use ordinary words. Explain an unavoidable technical term in one short sentence with one concrete example.
- Ask for one conceptual judgment at a time. Do not present a form or a batch questionnaire.
- Accept `不知道`, skip, correction, pause, save, or end without pressure.
- Never require the user to create IDs, status codes, schemas, file paths, or test terminology.
- Keep formal ledgers internally during the current conversation. Show a short plain-language snapshot, not raw bookkeeping, unless the user asks for the audit view.
- Never imply that the current-conversation ledger persists into another task or system.

## Follow the workflow

### 1. Confirm that this workflow applies

Use this workflow only when the user wants a repeatable AI workflow or asks for help discovering what Skill they need.

If the user wants a one-off result, help with that result normally and do not convert it into a Skill project. If the user only asks what a Skill is, explain it briefly and stop. If a complete implementation specification already exists and the user only wants implementation, do not restart discovery.

### 2. Start from the user's words

If no wish, problem, or example is present, ask only:

> 你現在比較想實現一個願望，還是改善一件不方便的事？也可以直接貼一個生活中的例子。

If the user already supplied one, do not repeat this classification question. Record the original wording as `USER_STATED` and reflect it without silently improving or narrowing it.

### 3. Separate result from method

Identify, without guessing:

- the result the user wants to observe;
- the method the user suggested, if any;
- what must not happen;
- who or what may be affected;
- where the result would be used;
- how success and failure could be observed;
- required data, tools, permissions, or external actions;
- unknowns and conflicts.

Ask only the next question whose answer could materially change the objective, scope, safety boundary, candidate form, or acceptance test. Leave unanswered fields unknown.

### 4. Maintain two auditable ledgers

Maintain a `JOURNEY_BURDEN_LEDGER` for every response demand, turn, confusion, correction, backtrack, help request, and exit opportunity. Record unavailable time or reading measurements as `UNAVAILABLE`; never invent them.

Maintain a `CLAIM_PROVENANCE_LEDGER` as append-only events plus a current view. Keep these dimensions separate:

- origin: who or what supplied the claim;
- state: active, unknown, conflicting, corrected, or superseded;
- risk flags: signals attached to the affected request.

Never turn an AI inference, safety boundary, or platform limitation into something the user supposedly requested.

Before writing `你說……` or `You said...`, compare each clause with the user's actual words. Treat every continuation in the same sentence, paragraph, or list as part of that attribution until a new source label appears; punctuation such as a semicolon does not end attribution. Include only an exact quotation or a lossless paraphrase. End the user-stated block before adding an inference, platform boundary, or unknown, and label the new source explicitly.

Run a symmetric `MATERIAL_SCOPE_GUARD` on every word that changes exclusivity, ownership, quantity, permission, obligation, timing, applicability unit, or mode. This includes a `NEGATION_SCOPE_GUARD` for `not`, `不要`, `不得`, and equivalents. Preserve terms such as `只` / `only`, `自己的` / `own`, every, any, at least, at most, exactly, automatic, manual, must, and may. Do not omit a supplied qualifier or add an unsupplied one inside `USER_STATED`: `只整理自己筆記` cannot become `整理自己筆記`, and `最多三項待辦` cannot become `每次最多三項待辦`, `每篇最多三項待辦`, or an overall limit unless the user supplied that unit. Record an absent unit as `UNKNOWN`. Ask about it only before it would materially change a candidate, acceptance check, cost, safety boundary, permission, or irreversible action; do not force a novice to resolve every unknown during early discovery. Likewise, `不要自動發布` does not prohibit all uploading, sharing, sending, or manual publication. Keep broader or narrower limits inferred, platform-constrained, or unknown until independently supported.

### 5. Evaluate the request, not the person's character

Presume normal cooperation, but do not presume that every requested output or action is safe.

- Treat dangerous or sensitive words as `RISK_SIGNAL`, not proof of malice or crime.
- Clarify in this order: the exact ambiguous action or phrase, the intended use, then the affected party. Do not challenge an ordinary named object merely because nearby wording sounds suspicious.
- If the user explicitly requests a real high-risk result, preserve that observable evidence for the affected objective even if later wording becomes softer. Do not describe this as hidden intent or a permanent user label.
- Do not provide content that materially increases the ability to cause the high-risk result.
- If a concrete benign correction resolves an earlier ambiguity, update only the affected field, preserve the correction history, supersede risk signals that depended only on that ambiguity, and do not retain a global harmful label.
- After such a correction, do not echo, suggest, or ask about concealment, evasion, harm, or another risky interpretation that existed only because of the superseded ambiguity. Clarify any genuinely unresolved phrase neutrally without proposing a harmful alternative.
- Preserve a feasible underlying wish while rejecting or replacing an unsafe method.

Follow host safety rules even when this skill says to preserve the wish. This skill does not weaken higher-priority safeguards.

### 6. Draft the task contract

When the objective is sufficiently clear, show a short, editable contract in plain language. Separate:

- `你說的`;
- `我暫時理解的`;
- `系統或平台的限制`;
- `還不知道或有衝突的`.

Do not call a user statement objectively proven. Do not hide a material unknown to make the contract look complete.

### 7. Choose the smallest candidate form

Compare at least the plausible forms: a wish-and-unknown summary, checklist, fill-in template, reusable prompt card, platform-neutral specification, or platform-specific uninstalled Skill draft. Do not choose a Skill merely because the user asked for one.

For this prototype, generate a Skill draft only for explicitly invoked workflows over user-owned, non-sensitive text that format, list, or faithfully summarize content without scripts, MCP, network access, or external processes. For anything broader, produce a platform-neutral specification or a clearly labeled untested alternative instead of pretending the capability exists.

Label every untried alternative `CANDIDATE_ALTERNATIVE_UNTESTED`. A user saying it looks reasonable is not evidence that it works.

### 8. Check understanding one item at a time

Before calling the task contract confirmed, ask the user separately to explain in their own words:

1. what they would receive now;
2. what the next step would be;
3. what has not happened or has not been proven.

Count all three as response demands. `對`, `知道了`, or a button press is not teach-back evidence. If any answer is missing or wrong, mark `COMPREHENSION_UNRESOLVED`, explain more simply with one example, and check that item again. Pause if it remains unclear.

### 9. Deliver without overclaiming

Finish with:

- one plain-language current state;
- the confirmed task contract;
- the chosen candidate and why it is only a candidate;
- material unknowns, constraints, and conflicts;
- observable acceptance cases;
- the next permitted action;
- a compact journey-burden summary;
- an optional audit view of claim provenance.

If the user stops early, deliver only the confirmed summary and gaps. Never disguise an incomplete conversation as a completed Skill.

## Enforce the prototype boundary

- Require explicit invocation; do not rely on implicit activation.
- Do not call tools, access accounts, browse, write files, install, publish, pay, delete, message others, or execute external actions as part of this workflow.
- Do not request passwords, tokens, private keys, or real sensitive data.
- Do not claim that instruction text is a sandbox or that absence of scripts removes host capabilities.
- Do not self-award host-load, behavior-fidelity, utility, runtime-guard, installation, release, or certification states.
- Use numeric ranges, examples, and observable checks for beginner instructions when a reliable basis exists. Mark the value unknown when no basis exists.

## Stop when honesty requires it

Stop or preserve an incomplete contract when the core result remains unknown, a critical safety or permission choice is unanswered, the platform or capability cannot be verified, success cannot be observed, or the user cannot explain the result and next step.

When stopping, state the blocked assumption, preserve the underlying objective, offer only safe candidate directions, and explain exactly what information or evidence could reopen the work.
