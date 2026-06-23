# Transcend

Portable orchestration workflow for coding agents.

`transcend` provides `/transcend` and subcommands that coordinate planning, debugging, frontend implementation, review, browser testing, documentation, optimization, dependency bootstrap, and dependency checks.

## Install

Install this repository as a plugin in the host agent. Codex uses `.codex-plugin/plugin.json` and `.codex/commands/transcend.md`.

### Codex CLI

Codex installs plugins from marketplaces. Add this repo as a marketplace, install `transcend`, then start a new thread:

```bash
codex plugin marketplace add allanbantilan/transcend
codex plugin add transcend@transcend
codex
```

Inside Codex:

```text
/transcend bootstrap
/transcend doctor
```

You can also install from the interactive plugin browser:

```text
codex
/plugins
```

Open the `Transcend` marketplace, install `transcend`, then start a new thread.

The Codex marketplace marks `superpowers` and `ponytail` as installed by default. Codex does not currently expose the same cross-marketplace dependency field as Claude Code, so `/transcend bootstrap` still checks role providers and reports manual steps for unavailable frontend, browser, and PDF tools.

### Claude Code

Claude Code can install `transcend` from this repo as a marketplace plugin:

```text
/plugin marketplace add allanbantilan/transcend
/plugin install transcend@transcend
/reload-plugins
```

Claude Code auto-installs declared plugin dependencies:

- `ponytail@transcend`
- `superpowers@claude-plugins-official`
- `frontend-design@claude-plugins-official`
- `pr-review-toolkit@claude-plugins-official`
- `playwright@claude-plugins-official`

Marketplace-installed plugin commands are namespaced. Run:

```text
/transcend:transcend bootstrap
/transcend:transcend doctor
```

If you want the exact `/transcend` command in one project, use Claude Code's standalone command layout instead. Clone this repo, then copy the command and config into your project:

```bash
git clone https://github.com/allanbantilan/transcend.git
mkdir -p .claude/commands
cp transcend/.claude/commands/transcend.md .claude/commands/transcend.md
cp transcend/transcend.yaml transcend.yaml
```

Then start Claude Code in the project and run:

```text
/transcend bootstrap
/transcend doctor
```

Claude Code also supports skills; if you package this as a skill later, keep `transcend.yaml` as the shared role map.

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
