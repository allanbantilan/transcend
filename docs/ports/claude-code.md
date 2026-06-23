# Claude Code Port

Claude Code should map `transcend.yaml` roles to slash commands, hooks, subagents, MCP servers, or manual prompts.

Use the same role names:

- `token_optimizer`
- `planner`
- `backend_debugger`
- `frontend_implementer`
- `code_reviewer`
- `browser_tester`
- `pdf_generator`

If Claude Code lacks an entry hook, run `token_optimizer` as the first explicit workflow step. If a provider is unavailable, use the configured fallback. Do not duplicate role mappings outside `transcend.yaml`.
