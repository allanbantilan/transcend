# Transcend

Portable orchestration workflow for coding agents.

`transcend` provides `/transcend` and subcommands that coordinate planning, debugging, frontend implementation, review, browser testing, documentation, optimization, dependency bootstrap, and dependency checks.

## Install

Install this repository as a plugin in the host agent. Codex uses `.codex-plugin/plugin.json` and `.codex/commands/transcend.md`.

After install:

```bash
/transcend bootstrap
/transcend doctor
```

## Commands

- `/transcend`: full workflow.
- `/transcend plan`: planner only; local spec and plan; no commit.
- `/transcend debug`: backend diagnosis only.
- `/transcend frontend`: frontend implementation only.
- `/transcend review`: simplification and review only.
- `/transcend test`: headless browser regression; prompts for credentials.
- `/transcend doc`: generate test assessment document.
- `/transcend optimize`: token optimization only.
- `/transcend bootstrap`: best-effort dependency install/check.
- `/transcend doctor`: verify role mappings, providers, fallbacks, and policies.

## Configuration

All roles, providers, fallbacks, install notes, workflow steps, credential rules, and commit rules live in `transcend.yaml`.

Do not duplicate role mappings in host-specific files.

## Credentials

Credentials are requested interactively only. They are never assumed, hardcoded, logged, or stored by default.

## Conventional Commits

Implementation commits use Conventional Commits. One logical task equals one commit.

Examples:

- `feat: add customer territory filtering`
- `fix: prevent duplicate activity sync`
- `refactor: simplify request limit validation`
- `docs: update API response examples`
- `test: add coverage service unit tests`
- `chore: upgrade laravel to 12.x`
- `build: update docker image versions`
- `ci: add deployment workflow`
- `perf: optimize activity export query`
- `style: format code with pint`
- `revert: revert territory fallback logic`

## Portability

Reference tools are role examples, not hard dependencies. Map each role to whatever the host supports: plugin, skill, hook, subagent, MCP server, command prompt, local script, or manual fallback.
