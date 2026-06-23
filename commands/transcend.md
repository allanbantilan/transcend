# /transcend

Read `transcend.yaml` first. Treat it as the single source of truth for roles, providers, fallbacks, bootstrap behavior, doctor checks, credentials, workflow, and commit policy.

Run this command as the full workflow. Route subcommands from `transcend.yaml`: `plan`, `debug`, `frontend`, `review`, `test`, `doc`, `optimize`, `bootstrap`, and `doctor`.

Required behavior:

1. Apply `token_optimizer` throughout.
2. Never assume or hardcode credentials.
3. Never auto-commit planning artifacts.
4. Use configured fallbacks when providers are missing.
5. Fail closed only when a required role has no provider and no fallback.
6. Commit completed implementation work as one logical task using Conventional Commits.
7. Keep host-specific behavior outside the shared role map.
