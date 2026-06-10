---
name: git-commit-helper
description: Generate clear, conventional Git commit messages by analyzing staged Git changes only. Tool-agnostic and reusable across editors and AI coding assistants.
---

# Git Commit Helper

## Purpose

Analyze **staged Git changes only** and generate **high-quality commit messages**
following the **Conventional Commits** standard.

This skill is **universal** and designed to work with:

- VS Code Copilot / Copilot Chat
- Antigravity
- CLI-based AI agents
- Any editor or workflow that can access `git diff --staged`

## Scope Assumption

This guide assumes commit messages are written
based on changes visible in `git diff --staged`.

Changes that are not staged — including unstaged
or untracked files — are considered outside the
scope of the commit description.

As a result, commit messages focus only on files
and modifications that appear in the staged diff.

## When to Use

Use this skill when:

- Writing a commit message
- Reviewing **staged** changes before committing
- Enforcing Conventional Commits
- Improving long-term Git history quality

## Expected Input

The assistant should prefer inputs in the following order:

1. `git diff --staged`
2. `git diff` (only if explicitly stated that all changes will be committed)
3. A pasted staged diff or patch

The assistant must **ignore**:

- `git status` untracked files

If no staged diff is provided, ask for clarification **before** generating a commit message.

## Output Format

```text
<type>[optional scope]: <short description>

[optional body]

[optional footer]
```

`(<scope>)` is **optional**. Include it when the change has a single clear area
(module/package/subsystem); omit it for cross-cutting changes or projects
without meaningful sub-areas.

## Commit Types

| Type     | Meaning                              |
|----------|--------------------------------------|
| feat     | New feature                          |
| fix      | Bug fix                              |
| docs     | Documentation                        |
| style    | Formatting / lint (no logic change)  |
| refactor | Refactor without behavior change     |
| test     | Add or update tests                  |
| chore    | Maintenance / tooling / CI           |

### Choosing Between `docs` and Behavioral Types

`docs` applies to documentation *about* code — READMEs, comments, usage guides.

When a file's content *is* the product — prompts, skills, rules, agent
instructions, behavior-as-config — classify by its behavioral impact instead,
because editing the file changes what the artifact actually does:

- New capability or output behavior → `feat`
- Corrected behavior → `fix`
- Restructure with no behavioral change → `refactor`

For example, editing a skill's examples so it starts producing a new commit
form is `feat`, not `docs` — the skill's observable output changes, even though
only Markdown was touched.

## Writing Rules

### Summary Line

- Imperative mood (`add`, `fix`, `remove`)
- ≤ 72 characters (including `type(scope):`)
- Capitalized first letter
- No trailing period
- Must match **staged changes exactly**

### Scope

- Optional, per the Conventional Commits spec.
- Include when the staged change maps to one clear area — it lets readers see
  the blast radius at a glance (e.g. `feat(auth):`, `refactor(db):`).
- Omit when the change spans multiple areas with no single owner, or the
  project has no meaningful sub-areas (e.g. `chore: bump dependencies`).
- Keep scope names consistent within a project; reuse existing ones.

### Body

- Explain **why** the staged change exists
- Describe behavior or structural impact
- Prefer bullet points
- Do **not** mention unstaged or future work

### Footer

- Reference issues: `Refs #123`, `Closes #456`
- Declare breaking changes if applicable

## Examples

Examples come in both forms — with a scope when the change maps to one clear
area, and without when it does not. Match the form to the change, not habit.

### Feature (with scope — single clear area)

```text
feat(auth): add JWT authentication

- Implement token-based login
- Add token validation middleware
- Support refresh tokens
```

### Feature (no scope — cross-cutting change)

```text
feat: make commit scope optional

- Clarify that (scope) is optional per Conventional Commits
- Show examples in both the scoped and scopeless form
```

### Bug Fix (no scope)

```text
fix: prevent crash on null profile data

Add null checks before accessing nested fields.
```

### Refactor (with scope)

```text
refactor(db): simplify query construction

- Extract shared query logic
- Reduce duplication
```

## Multi-file Changes (Staged Only)

```text
refactor(core): restructure authentication module

- Move logic into service layer
- Extract validators
- Update related tests

BREAKING CHANGE: Auth service now requires a config object
```

## Breaking Changes

```text
feat(api)!: change response format

BREAKING CHANGE:
Responses now follow JSON:API specification.
```

## Recommended Workflow

```bash
git add -p
git diff --staged
git commit -m "type: description"   # add (scope) only when it adds clarity
```

## Amend Commits

```bash
git commit --amend
git add forgotten-file
git commit --amend --no-edit
```

## Best Practices

- One logical change per commit
- Commit message must match `git diff --staged`
- If a file is not in `git diff --staged`, it must not be mentioned
- Prefer small, focused commits
- Write for future maintainers

## Checklist

- [ ] Only staged files are described
- [ ] Correct type
- [ ] Scope included when it adds clarity (optional otherwise)
- [ ] Imperative summary
- [ ] ≤ 72 characters
- [ ] Body explains why
- [ ] Breaking changes marked
