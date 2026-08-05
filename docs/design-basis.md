# Accepted Design Basis

This public summary records the implementation baseline without reproducing private debate packets or human test transcripts.

## Human decision

The human judge accepted the design concept for prototype implementation after a separate Attacker and Defender had examined human-observed dialogue evidence. Acceptance closed the debate but did not certify the product or authorize claims of general usefulness or safety.

## Controlling principles

1. Begin with a wish, problem, or concrete example in ordinary language.
2. Separate the desired result, proposed method, unacceptable result, safety or platform constraints, and unknowns.
3. Measure the entire interaction burden rather than a fixed question count.
4. Preserve provenance for every material claim; never present an AI-added condition as a user requirement.
5. Presume normal cooperation while evaluating each request, output, and action independently.
6. Treat dangerous words as risk signals, not sufficient evidence of malicious character or criminal purpose.
7. Preserve explicit high-risk request evidence across softer rewording without claiming access to hidden intent.
8. Allow a concrete benign correction to replace prior ambiguity while preserving correction history.
9. Reject impossible or dangerous methods without dismissing the meaningful wish.
10. Keep alternatives at candidate status until a human performs a predefined trial and observes a result.
11. Keep structure, host loading, behavior fidelity, utility, runtime controls, and installation as separate evidence dimensions.

## Prototype boundary

The first prototype is explicitly invoked and instruction-only. It considers user-owned, non-sensitive text workflows limited to formatting, listing, or faithful summarization. It has no runtime scripts, MCP dependency, network operation, or external process.

Broader wishes may still be distilled into platform-neutral specifications or safe untested alternatives, but the prototype must not present them as working Skills.

## Relationship to the bundled Skill Creator

Skill Companion is not a replacement implementation engine for the bundled Skill Creator. It is an upstream requirements-discovery and candidate-selection layer. It may conclude that no Skill should be built, stop with unresolved requirements, or hand a confirmed platform-neutral candidate to an authoring workflow. Skill Creator remains the appropriate downstream workflow for scaffolding, editing, validating, and iterating an actual Codex Skill.

This boundary prevents a mention of a reusable helper from being treated as proof that a Skill is the correct product form or that implementation is already authorized. Host-visible wording such as `Skill Creation` is retained only as an observed label for a routed creation workflow; it is not evidence of a separately validated product.

## Preserved evidence gaps

- Full-journey burden and comprehension for people with no technical background.
- Stable source attribution and asymmetric high-risk versus benign-correction behavior.
- Real human-task utility of candidate alternatives.

These are post-implementation validation targets, not facts established by the accepted design.

## Post-baseline human-test boundary

Early prototype testing exposed a separate participant and account risk: a host may review or restrict an account when a test fixture itself states a clear attack objective, even when the purpose is evaluation. The human judge therefore prohibited any future request that a person run explicit physical or psychological attack, threat, harassment, humiliation, coercion, or manipulation wording on a personal or general account.

Such cases are now controlled-evaluator-only. If no authorized controlled environment exists, they remain `NOT_RUN`. Any host intervention ends the run as `NOT_SCORABLE_HOST_INTERVENTION`; it is neither a model-behavior pass nor permission to rephrase and retry.

Later low-risk human testing also showed that a model can quote a requirement correctly and then use punctuation or an unlabelled continuation to make a broader AI inference look user-stated. The implementation therefore treats attribution as covering the entire unlabelled block and preserves the exact scope of every material negation. A prohibition on automatic publication, for example, does not prove that the user prohibited all uploading, sharing, sending, or manual publication.

A follow-up regression found that preserving a negation alone is insufficient: one run retained `不要自動發布` but dropped `只` from `只整理自己筆記`, silently broadening the data scope. The implementation therefore protects all material scope qualifiers, including exclusivity, ownership, quantity, permission, obligation, timing, and operating mode.

A later regression exposed the opposite failure: the model preserved every supplied limit but inserted `每次` before `最多三項待辦`, turning an unspecified applicability unit into a user-attributed requirement. Scope preservation is therefore symmetric. The workflow must neither delete nor invent a material qualifier; an unsupplied per-note, per-invocation, per-turn, or overall unit remains `UNKNOWN` until it materially affects the candidate or acceptance check. This avoids both semantic drift and unnecessary novice questioning.

The same regression exposed an evaluation error. The original case did not forbid an invented applicability unit, so its completed run passed the predeclared observables even though the new deviation was real. Evaluation criteria are now frozen before each run: a new issue is recorded separately and may revise a future suite, but cannot retroactively change the old score.
