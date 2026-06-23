# Generic Agent Port

Any coding agent can run Transcend if it can read `transcend.yaml` and execute the command contract.

Minimum host capabilities:

- Read local files.
- Run prompts or tools for configured roles.
- Ask user for credentials interactively.
- Run tests or report missing test providers.
- Commit with user-visible git commands after implementation.

Fallbacks are valid providers when no native plugin, hook, MCP server, or subagent exists.
