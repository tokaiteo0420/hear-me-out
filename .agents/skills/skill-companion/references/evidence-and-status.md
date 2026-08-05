# Evidence Levels and Honest Status

Keep these evidence levels independent. A higher numbered label is not automatically earned by lower levels, and one passing dimension cannot cancel another failure.

1. `DESIGN_SPECIFIED_NOT_IMPLEMENTED`: a design exists only.
2. `DIALOGUE_BEHAVIOR_HUMAN_OBSERVED_LIMITED`: a named human interaction observed limited dialogue behavior.
3. `ARTIFACT_CANDIDATE_CREATED`: a candidate file or text exists.
4. `STRUCTURE_VALIDATED_FOR_PLATFORM_VERSION`: a named validator passed the structure for a named platform version.
5. `HOST_LOAD_OBSERVED`: a fresh host session visibly discovered and loaded the candidate.
6. `BEHAVIOR_FIDELITY_VERIFIED`: blinded cases and independent criteria support behavior fidelity within a named suite.
7. `USER_TESTED_UTILITY_WITHIN_SCOPE`: a human actually used the candidate and achieved a predefined observable result in a named case.
8. `RUNTIME_GUARD_VERIFIED`: host-level tool, data, permission, and side-effect controls were tested for a named environment.
9. `INSTALLED_FOR_NAMED_ENVIRONMENT`: installation was observed for one named environment. This does not prove usefulness or safety.

## Promotion rules

- Bind every evidence claim to artifact version or hash, platform, host version, date, scope, and evidence location.
- Mark stale or environment-mismatched evidence expired.
- Keep unknown, failed, blocked, and not-run dimensions visible.
- Never let the Skill award itself levels 4 through 9.
- Never convert a user's statement about a tool or installation into environment evidence.
- Never call project self-validation an official OpenAI certification.

## Current-conversation states

Use one plain-language headline:

- `還在了解願望`;
- `需求摘要尚未完成`;
- `理解仍待確認`;
- `候選方案已產生，但尚未試用`;
- `目前沒有已確認的可行路徑`.

Show technical labels only in an expanded audit view or when the user asks.

## Permitted claims for this prototype

The workflow may truthfully say it created a task contract, specification, candidate card, or candidate Skill text in the current conversation. It may report directly observable conversation counts.

It may not claim that the candidate loaded, worked, reduced burden, was safe, protected data, installed successfully, or will be used as intended unless the corresponding external evidence exists and is cited within its exact scope.
