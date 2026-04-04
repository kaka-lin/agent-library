---
name: i18n-restructure-md
description: Automatically restructure Markdown documentation into a professional bilingual subfolder hierarchy (en/ and zh-TW/) with mandatory style and terminology checks.
---

# i18n Markdown Restructuring Workflow

Use this workflow when a user requests to "internationalize", "add bilingual support", or "restructure docs for multi-language" in a repository.

## 📋 Mandatory Style Reference

Before writing any line of Markdown, you **MUST** read and adhere to the project's style guide:

- **Style Path**: `~/.gemini/antigravity/rules/markdown-code-style.md`

- **Key Rules**:
  - Leave one blank line **after** every header (H1-H6).
  - Always leave a blank line between a regular paragraph and a list/code block.
  - Use 2 spaces for indentation.
  - **No horizontal rules (`---`)** or unnecessary separators.

## 🛠️ Execution Steps

### 1. Structural Mapping & Identification

- Scan the root directory and `docs/` for all `.md` files.
- Determine the current primary language of the documentation.
- Plan the dual-folder structure: `docs/en/` and `docs/zh-TW/`.

### 2. Directory Initialization

Execute the creation of bilingual subdirectories:

```bash
mkdir -p docs/en/path/to/module docs/zh-TW/path/to/module
```

### 3. Balanced Translation & Data Deep Dive

For every document identified:

- **Mirror the Files**: Create an English version in `docs/en/` and a Traditional Chinese version in `docs/zh-TW/`.

- **Apply Terminology Standard (TW)**:
  - **Clone** (Use the English word directly).
  - **Repository** (Use the English word directly).
  - **Memory** ➡️ **記憶體**.
  - **Data/Database** ➡️ **資料/資料庫**.
  - **Object Storage** ➡️ **物件儲存 (Object Storage)**.
  - **Project** ➡️ **專案**.
  - **Disk** ➡️ **磁碟**.

### 4. Navigation Toggle Injection

Insert a language toggle at the very top of **every** Markdown file (below the H1 header):

```markdown
# [Title]

[English](relative/path/to/en/file.md) | [繁體中文](relative/path/to/zh-TW/file.md)
```

- Ensure relative paths are dynamically calculated to support cross-folder jumping.

### 5. Link Synchronization

Update all internal Markdown links `[text](./local-file.md)` to their new locations within the same language subfolder.

- e.g., A link from `setup.md` to `deep-dive.md` must stay `deep-dive.md` within the `en/` folder.
- Root README links must point to the specific `/docs/en/` or `/docs/zh-TW/` landing pages.

### 6. Final Consistency Audit

- [ ] **No horizontal rules**: Check for any `---` or `<hr>` and remove them.
- [ ] **Spacing**: Check for the "header-to-content" blank line.
- [ ] **Terminology**: Scan for prohibited terms like 「克隆」, 「內存」, or 「儲存庫」.
- [ ] **Broken Links**: Verify all relative paths in the toggle menu.

## ⚠️ Notes for the AI Agent

- **English First**: The root `README.md` should be English, with a `README.zh-TW.md` as the secondary portal.
- **Strict Compliance**: Failure to follow `markdown-code-style.md` is unacceptable for this project.
