---
name: global-rules
description: Unified entry point rules for all AI agents. Instructs agents to read language-specific style guides before generating code.
---

# Global Rules

These are the foundational instructions for any AI coding assistant (Cursor, Copilot, Antigravity, Claude, etc.) operating in this environment.

## Language-Specific Coding Style Rules

Detailed coding style rules are maintained in a dedicated rules directory. 
Depending on the AI agent you are using, you must look for the language-specific rule file in the following locations:

- **Antigravity**: `~/.gemini/antigravity/rules/`
- **Roo Code**: `~/.roo/`
- **Cursor**: `.cursor/rules/`
- **Claude Code**: `~/.claude/`
- **Local Repository**: `rules/` (if operating directly within the repository)

**When writing, reviewing, or refactoring code in a specific language, you MUST ALWAYS consult the corresponding rule file from the appropriate directory above first and follow it strictly.**

Current language-specific rules:

- **Python**: [`python-code-style.md`](./python-code-style.md)
- **Markdown**: [`markdown-code-style.md`](./markdown-code-style.md)

> [!IMPORTANT]
> **Tool Instruction:**
> Whenever you detect that the user wants you to write code in a specific language, you MUST use your file-reading tool (e.g., `view_file`, `cat`, or equivalent) to read the exact contents of the corresponding rule file listed above before you begin generating or modifying code.

## General Rules

- **Documentation**: Ensure all generated code is properly documented and commented. Explain *why*, not just *what*.
- **Style Compliance**: Code must follow the language-specific style guide listed above. Do not blindly use your default formatting if it contradicts the explicit rules.
- **Atomic Commits**: If you are generating commit messages or helping with version control, keep changes small, focused, and aligned with Conventional Commits.
- **No Hallucinations**: If you do not know the answer or lack access to a specific file, say so clearly instead of guessing structural details.
- **Absolute Paths**: When using tools that accept file path arguments, ALWAYS prefer absolute file paths if known, or clearly state the working directory context.
