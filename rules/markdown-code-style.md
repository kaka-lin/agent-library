---
name: markdown-code-style
description: Markdown authoring style — structure, spacing, lists, and formatting conventions
activation: model_decision
---

# Markdown Code Style & Conventions

Consistent formatting and semantic structure make Markdown documents much easier to read, review, and maintain across different editors and platforms.

**Apply when:** writing, editing, or formatting Markdown (.md) files.

## 1. Automated Tooling

Use standard Markdown linters (e.g., `markdownlint` or `Prettier`) to maintain consistency.

### 1.1 Config

When configuring a formatter like Prettier, use the following rules to enforce 4-space indentation and disable automatic wrapping that breaks version control diffs.

```json
{
  "tabWidth": 4,
  "useTabs": false,
  "proseWrap": "never"
}
```

## 2. Spacing and Alignment

### 2.1 Indentation

Always use **4 spaces** for indentation. Never use tabs.

This rule strictly applies to:
- Nested lists (ordered and unordered)
- Indented code blocks
- Multiline blockquotes

**Correct (4 spaces):**

```markdown
- Item 1
    - Sub-item A
    - Sub-item B
        - Deep sub-item
```

**Incorrect (2 spaces or Tabs):**

```markdown
- Item 1
  - Sub-item A
```

### 2.2 Blank Lines

Structure the document visually using blank lines (leaving exactly one empty line).
- Leave one blank line before and after headers (H1-H6).
- Leave one blank line before and after lists.
- **Critical:** Always leave a blank line between a regular paragraph and a list. If there is no blank line, some parsers will merge the list into the preceding paragraph.

**Correct:**

```markdown
Group imports in three blocks, separated by blank lines, in this order:

1. Standard library
2. Third-party packages
3. Local / project imports
```

**Incorrect:**

```markdown
Group imports in three blocks, separated by blank lines, in this order:
1. Standard library
2. Third-party packages
```

- Leave one blank line before and after code blocks and blockquotes.

**Do not use horizontal rules (`---` or `***`) to divide sections.** Rely purely on heading hierarchies and blank lines for visual separation.

## 3. Headings

### 3.1 Hierarchy

Always respect the heading hierarchy. Do not skip levels (e.g., do not jump from H1 directly to H3).

- Use **# (H1)** for the document title (only one per document).
- Use **## (H2)** for primary sections.
- Use **### (H3)** for sub-sections.

### 3.2 Spacing in Headings

Always leave exactly one space between the `#` characters and the heading text.

**Correct:**

```markdown
## 1. Introduction
```

**Incorrect:**

```markdown
##1. Introduction
##  1. Introduction
```

## 4. Lists

### 4.1 Unordered Lists

Use the hyphen `-` as the default marker for unordered lists. Do not mix `*`, `+`, and `-` in the same document.

**Correct:**

```markdown
- First item
- Second item
    - Sub-item
```

### 4.2 Ordered Lists

Use `1.` for all items in an ordered list to make reordering easier, letting the Markdown engine handle the numbering, OR number them sequentially if preferred by the project. Consistency is key.

**Recommended:**

```markdown
1. First step
2. Second step
3. Third step
```

## 5. Code Blocks and Inline Elements

### 5.1 Fenced Code Blocks

Always use fenced code blocks (` ``` `) instead of indented code blocks for syntax highlighting and readability.

Always specify the language identifier.

**Correct:**

```python
def hello_world():
    print("Hello, world!")
```

**Incorrect:**

```
def hello_world():
    print("Hello, world!")
```

### 5.2 Inline Code

Use single backticks for inline code, variables, file names, or terminal commands mentioned in prose.

**Example:**
To start the server, run the `npm start` command in your terminal. Ensure that `config.json` is properly set up.

## 6. Links and Images

### 6.1 Reference vs. Inline Links

For links that appear multiple times or when dealing with very long URLs that break paragraph readability, prefer **Reference Links** placed at the bottom of the document. For standard, one-off links, use inline links.

**Inline Link:**
Read the [official documentation](https://example.com/docs).

**Reference Link:**
Read the [official documentation][docs].

[docs]: https://example.com/docs "Optional Title"

### 6.2 Images

Always provide descriptive alt text for accessibility and broken-link fallbacks.

**Example:**
```markdown
![Architecture diagram showing the data flow from API to Database](./assets/architecture.png)
```

## 7. Emphasis

- Use `**` for **bold** text (strong emphasis).
- Use `*` for *italic* text (emphasis).
- Use `_` only when the formatting requires it to avoid escaping issues within specific parsers.
- Do not mix `**` and `__` for bolding in the same document.

## 8. Best Practices Checklist

1. **4 Spaces** — Strictly enforce 4 spaces for tabs and list indentation.
2. **No Horizontal Rules** — Use heading hierarchies (`#`, `##`, `###`) and single blank lines for section separation. Never use `---`.
3. **One H1 per document** — Serve as the main document title.
4. **Blank Lines** — Surround headings, lists, and code blocks with a single empty line.
5. **Language Identifiers** — Always tag fenced code blocks (e.g., ` ```python `).
6. **Consistent Markers** — Stick to `-` for unordered lists.
7. **Semantic Alt Text** — Always include descriptive alt text for images.
8. **Prose Wrapping** — Let text editors handle soft-wrapping; avoid hard-wrapping lines manually to keep Git diffs clean.
