---
name: global-rules
description: Unified entry point rules for Antigravity, Claude Code, and Local Repositories.
---

# Global Rules

These are the foundational instructions for AI coding assistants. When operating in this environment, you must adhere to the language-specific styles defined in our centralized rules.

## Language-Specific Coding Style Rules

Detailed rules are maintained in specific directories. You MUST look for the rule files in this priority order:

1. **Local Repository**: `./rules/` (Project-specific rules)
2. **Claude Code (CLI)**: `~/.claude/rules/` (Global fallback)
3. **Antigravity IDE**: `~/.gemini/antigravity/rules/` (Global fallback)

**Language-to-File Mapping:**

- **Python**: `python-code-style.md`
- **Markdown**: `markdown-code-style.md`

> [!IMPORTANT]
> **Tool Instruction:**
>
> 1. **Detect Language**: Identify the language of the file you are about to create or modify.
> 2. **Locate Rules**: Check for the corresponding file in the priority paths listed above.
> 3. **Mandatory Reading**: You **MUST** use `cat` or `read_file` to read the rule file from the **first available path** before generating any code.
> 4. **CLI Context**: If running via Claude Code CLI, explicitly check `~/.claude/rules/[filename]` if the local repository rules are missing.

## General Rules

- **Documentation**: Explain *why*, not just *what*. All comments and docs should be clear and professional.
- **Style Compliance**: Follow the language-specific guide strictly. Override your default behaviors.
- **Tooling**: For Python, respect **Ruff** linting and **uv** package management.
- **Path Handling**: ALWAYS use absolute paths (starting with `~/`) when accessing global rules to avoid context confusion.
- **No Hallucinations**: If a rule file is missing from all specified paths, STOP and ask the user for the location.
