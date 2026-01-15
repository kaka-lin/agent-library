---
name: Git Commit Helper
description: Generate clear, conventional Git commit messages by analyzing git diffs or staged changes. Tool-agnostic and reusable across editors and AI coding assistants.
---

# Git Commit Helper

## Purpose

Analyze Git changes and generate **high-quality commit messages** following the **Conventional Commits** standard.

This skill is **universal** and designed to work with:

- VS Code Copilot / Copilot Chat
- Antigravity
- CLI-based AI agents
- Any editor or workflow that can access `git diff`

---

## When to Use

Use this skill when:

- Writing a commit message
- Reviewing staged changes before committing
- Enforcing Conventional Commits
- Improving long-term Git history quality

---

## Expected Input

The assistant may analyze one or more of:

- `git diff --staged`
- `git diff`
- `git status`
- `git diff --stat`
- A pasted diff or patch

If no diff is provided, infer intent from context and ask for clarification only if necessary.

---

## Output Format

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

---

## Commit Types

| Type     | Meaning |
|----------|--------|
| feat     | New feature |
| fix      | Bug fix |
| docs     | Documentation |
| style    | Formatting / lint (no logic change) |
| refactor | Refactor without behavior change |
| test     | Add or update tests |
| chore    | Maintenance / tooling / CI |

---

## Writing Rules

### Summary Line

- Imperative mood (`add`, `fix`, `remove`)
- ≤ 50 characters
- Capitalized first letter
- No trailing period

### Body

- Explain **why** the change exists
- Describe impact or behavior changes
- Prefer bullet points
- Avoid repeating the summary

### Footer

- Reference issues: `Refs #123`, `Closes #456`
- Declare breaking changes

---

## Examples

### Feature

```
feat(auth): add JWT authentication

- Implement token-based login
- Add token validation middleware
- Support refresh tokens
```

### Bug Fix

```
fix(api): prevent crash on null profile data

Add null checks before accessing nested fields.
```

### Refactor

```
refactor(db): simplify query construction

- Extract shared query logic
- Reduce duplication
```

---

## Multi-file Changes

```
refactor(core): restructure authentication module

- Move logic into service layer
- Extract validators
- Update related tests

BREAKING CHANGE: Auth service now requires a config object
```

---

## Breaking Changes

```
feat(api)!: change response format

BREAKING CHANGE:
Responses now follow JSON:API specification.
```

---

## Recommended Workflow

```bash
git add -p
git diff --staged
git commit -m "type(scope): description"
```

---

## Amend Commits

```bash
git commit --amend
git add forgotten-file
git commit --amend --no-edit
```

---

## Best Practices

- One logical change per commit
- Avoid vague summaries
- Prefer small, focused commits
- Write for future maintainers

---

## Checklist

- [ ] Correct type
- [ ] Clear scope
- [ ] Imperative summary
- [ ] ≤ 50 characters
- [ ] Body explains why
- [ ] Breaking changes marked
