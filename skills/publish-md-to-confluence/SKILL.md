---
name: publish-md-to-confluence
description: Use when asked to publish, push, upload, or sync a Markdown (.md) file to Confluence, or to turn a repo doc into a Confluence/wiki page.
---

# Publish Markdown to Confluence

## Overview

Publish a Markdown file to a Confluence page using [`md2cf`](https://github.com/iamjackg/md2cf)
run via `uvx` — no install, no custom converter. `md2cf` converts Markdown to
Confluence storage format and calls `/wiki/rest/api/content` itself. Re-running
the same command **updates the same page** (it matches by title), so it doubles
as the sync path.

## When to Use

- "把這份 md 放上 Confluence" / "publish X.md to Confluence" / "sync doc to wiki".
- A repo doc (architecture, runbook, design) needs a Confluence page.

Not for: Notion, Google Docs, or Confluence Server/Data Center with SSO-only
(no API token) — those need a different auth path.

## Prerequisites

- `uv` installed (provides `uvx`). No other install needed.
- A Confluence **Cloud** site and an [API token](https://id.atlassian.com/manage-profile/security/api-tokens).
- The target **space key** (e.g. `ENG`).

## Auth (Cloud vs Server)

Confluence **Cloud**: username = your account **email**, password = the **API
token** (basic auth). Do NOT use `--token` — that flag is Server/DC bearer PAT.
`CONFLUENCE_HOST` is the **REST API base**, not the site root — it must end with
`/wiki/rest/api` (e.g. `https://<site>.atlassian.net/wiki/rest/api`).

Credentials go in a **local `.env`**, never in this skill's git-tracked files.
Copy the bundled template and fill in your values:

```bash
cd <this-skill-dir>
cp .env.example .env          # .env is gitignored — never commit it
$EDITOR .env                  # fill in host / email / token / space
set -a; source .env; set +a   # load into the shell before running md2cf
```

Only `CONFLUENCE_PASSWORD` (the token) is secret; the other three aren't. If you
prefer not to store the token at all, omit it — `md2cf` prompts for the password
interactively when `-p` / `CONFLUENCE_PASSWORD` is absent.

## Workflow

1. **Dry-run first** — uploads nothing, but still needs valid host/space/creds
   (it queries the space to render):

    ```bash
    uvx md2cf --dry-run -t "Page Title" path/to/doc.md
    ```

2. **Publish / update** — `-a` sets the parent page by title; omit for top level:

    ```bash
    uvx md2cf -t "Page Title" -a "Parent Page" path/to/doc.md
    ```

3. **Re-sync after edits** — same command updates the same page. Add
   `--only-changed` to skip unchanged pages.

## Two Gotchas (handle before publishing)

- **Mermaid blocks render as source, not diagrams.** `md2cf` uploads a
  ` ```mermaid ` fence as a plain code block. If Confluence has no Mermaid app,
  pre-render with the bundled helper (needs `npx`), then publish its output —
  `md2cf` uploads the PNGs as attachments:

    ```bash
    python <this-skill-dir>/render-mermaid.py docs/ARCHITECTURE.md /tmp/out
    uvx md2cf -A <parent-id> -t "Title" /tmp/out/ARCHITECTURE.md
    ```

- **Relative repo links become dead links.** `](../app/foo.py)` doesn't resolve
  in Confluence. Rewrite them to the git remote's web URL first. For this repo
  (GitLab), from a doc in `docs/`:

    ```bash
    sed 's#](\.\./#](https://gitlab.svc.langlive.tech/mct/ai-eden-service/-/blob/main/#g' \
      docs/ARCHITECTURE.md > /tmp/doc.confluence.md
    uvx md2cf -t "Page Title" /tmp/doc.confluence.md
    ```

    Adjust the host/path/branch and the `../` depth to the doc's location.
    Non-repo relative links won't be caught — check the dry-run output.

## Common Mistakes

- Using `--token` for Cloud → 401. Use `-u email -p api-token`.
- `CONFLUENCE_HOST` not ending in `/wiki/rest/api` on Cloud → 404 on `space/<KEY>`.
- Expecting Mermaid to render → it won't; see gotchas.
- Pasting the API token into the command line (leaks to shell history) → use the
  env var, or let `md2cf` prompt for the password interactively.
