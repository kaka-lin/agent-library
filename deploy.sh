#!/usr/bin/env bash
# Sync this repo (the source of truth) into every runtime.
#   - skills/ : folders → rsync-copied (merges alongside each runtime's other
#     skills, e.g. gstack's; --delete is per-skill so it only touches ours).
#   - rules/  : single files, 100% owned here → symlinked (zero-drift: edit once,
#     every runtime sees it live; re-run only when a NEW rule file is added).
# Idempotent — safe to re-run. `.env` files ARE synced too, so the copy in this
# repo (gitignored) is the single source for creds. Don't share this repo with
# others as-is — deploy would push your tokens onto their machines.
set -euo pipefail

SRC="$(cd "$(dirname "$0")/skills" && pwd)"

# ponytail: targets hardcoded — add a line here if a new runtime appears.
TARGETS=(
  "$HOME/.claude/skills"
  "$HOME/.gemini/antigravity/skills"
  "$HOME/.gemini/antigravity-ide/skills"
  "$HOME/.gemini/antigravity-backup/skills"
  "$HOME/.gemini/config/skills"
)

for t in "${TARGETS[@]}"; do
  if [ ! -d "$t" ]; then
    echo "skip (missing): $t"
    continue
  fi
  for skill in "$SRC"/*/; do
    rsync -a --delete "$skill" "$t/$(basename "$skill")/"
  done
  echo "synced skills → $t"
done

# Rules: symlink each rule file into every runtime's rules dir. Only the actual
# rule files — global-rules.md is injected into each CLAUDE.md/GEMINI.md
# separately, and README.md is repo docs, so neither is linked here.
RULES_SRC="$(cd "$(dirname "$0")/rules" && pwd)"
# Auto-discover every rule file — new rules need no edit here, just re-run.
# Skip the two that aren't per-runtime rules: README.md (repo docs) and
# global-rules.md (injected into each CLAUDE.md/GEMINI.md, not the rules dir).
RULE_SKIP=" README.md global-rules.md "
RULE_TARGETS=(
  "$HOME/.claude/rules"
  "$HOME/.gemini/antigravity/rules"
  "$HOME/.gemini/antigravity-ide/rules"
  "$HOME/.gemini/antigravity-backup/rules"
  "$HOME/.gemini/config/rules"
)

for t in "${RULE_TARGETS[@]}"; do
  if [ ! -d "$t" ]; then
    echo "skip (missing): $t"
    continue
  fi
  for src in "$RULES_SRC"/*.md; do
    f="$(basename "$src")"
    case "$RULE_SKIP" in *" $f "*) continue ;; esac
    ln -sfn "$src" "$t/$f"
  done
  echo "linked rules → $t"
done
