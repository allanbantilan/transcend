#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "transcend.yaml"
COMMAND = ROOT / ".codex" / "commands" / "transcend.md"
README = ROOT / "README.md"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_config() -> dict:
    if not CONFIG.exists():
        fail("missing transcend.yaml")
    try:
        return json.loads(CONFIG.read_text())
    except json.JSONDecodeError as exc:
        fail(f"transcend.yaml is not JSON-valid YAML: {exc}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    config = load_config()
    roles_config = config.get("roles")
    commands = config.get("commands")
    workflow = config.get("workflow")

    require(isinstance(roles_config, dict) and roles_config, "roles missing")
    require(isinstance(commands, dict) and commands, "commands missing")
    require(isinstance(workflow, list) and workflow, "workflow missing")
    require("bootstrap" in commands, "bootstrap command missing")
    require("doctor" in commands, "doctor command missing")
    require("commit_policy" in config, "commit policy missing")
    require("alternative_policy" in config, "alternative policy missing")
    trusted_alternatives = config.get("trusted_alternatives")
    require(isinstance(trusted_alternatives, dict) and trusted_alternatives, "trusted alternatives missing")

    roles = set(roles_config)

    for name, command in commands.items():
        for role in command.get("roles", []):
            require(role in roles, f"command {name} references unknown role {role}")

    for role, alternatives in trusted_alternatives.items():
        require(role in roles, f"trusted alternatives reference unknown role {role}")
        require(isinstance(alternatives, list) and alternatives, f"trusted alternatives for {role} missing")
        for index, alternative in enumerate(alternatives, start=1):
            require(alternative.get("provider"), f"trusted alternative {role}[{index}] missing provider")
            require(alternative.get("install"), f"trusted alternative {role}[{index}] missing install")
            require(alternative.get("verify"), f"trusted alternative {role}[{index}] missing verify")

    require(COMMAND.exists(), "missing .codex/commands/transcend.md")
    command_text = COMMAND.read_text()
    require("transcend.yaml" in command_text, "command doc must reference transcend.yaml")
    for name in commands:
        require(f"/transcend {name}" in command_text or name == "run", f"command doc missing /transcend {name}")

    require(README.exists(), "missing README.md")
    readme = README.read_text()
    require("Conventional Commits" in readme, "README missing Conventional Commits policy")
    require("Credentials" in readme, "README missing credentials policy")

    print("OK: transcend config, command docs, and policies verified")


if __name__ == "__main__":
    main()
