# /transcend

Read `transcend.yaml` first. Treat it as the single source of truth for roles, providers, fallbacks, bootstrap behavior, doctor checks, credentials, workflow, and commit policy.

## Command Routing

- `/transcend`: run full workflow from `transcend.yaml`.
- `/transcend plan`: run planner only; store spec and plan locally; no commit.
- `/transcend debug`: run backend debugger only.
- `/transcend frontend`: run frontend implementer only.
- `/transcend review`: run code reviewer only.
- `/transcend test`: run browser tester only; prompt for credentials when needed.
- `/transcend doc`: run PDF generator only.
- `/transcend optimize`: run token optimizer only.
- `/transcend bootstrap`: best-effort install/check for current host.
- `/transcend doctor`: verify config, providers, fallbacks, wrappers, browser/PDF availability, and policies.

## Required Behavior

1. Apply `token_optimizer` throughout.
2. Never assume or hardcode credentials.
3. Never auto-commit planning artifacts.
4. Use configured fallbacks when providers are missing.
5. Fail closed only when a required role has no provider and no fallback.
6. Commit completed implementation work as one logical task using Conventional Commits.
7. Keep host-specific behavior outside the shared role map.

## Bootstrap

For `/transcend bootstrap`, install only providers supported by the current host. Prompt before authenticated or private installs. Report manual steps for unsupported providers.

If a role provider is missing, offer only alternatives listed in `trusted_alternatives` in `transcend.yaml`. Each offered alternative must include an install command and a verification command. Install the selected alternative before using it, then run its verification command. If install or verification fails, stop and ask the user to pick another trusted alternative or provide a custom provider with install command, verification command, and role mapping.

## Doctor

For `/transcend doctor`, verify `transcend.yaml`, command routing, role names, required providers or fallbacks, trusted alternatives, credential policy, and commit policy. Report degraded optional roles separately from blocking required roles.
