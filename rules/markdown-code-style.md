---
name: markdown-code-style
description: Markdown authoring style — structure, spacing, lists, and formatting conventions
trigger: model_decision
---

# Markdown Code Style & Conventions

Consistent formatting and semantic structure make Markdown documents much easier to read, review, and maintain across different editors and platforms.

**Apply when:** writing, editing, or formatting Markdown (`.md`) files.

This style guide follows the [markdownlint](https://github.com/DavidAnson/markdownlint) rule set as a baseline, with a project-wide preference for 2-space indentation and explicit blank lines around code blocks.

## 1. Automated Tooling

Use standard Markdown linters and formatters, such as `markdownlint` or `Prettier`, to maintain consistency.

### 1.1 Formatter Configuration (for example, Prettier)

When using a formatter, ensure it is configured to use **2 spaces** for indentation.

```json
{
  "tabWidth": 2,
  "useTabs": false,
  "proseWrap": "never"
}
```

## 2. Spacing and Alignment

### 2.1 Indentation

Always use **2 spaces** for indentation. Never use tabs.

This rule strictly applies to:

- Nested lists (ordered and unordered)
- Indented code blocks
- Multiline blockquotes

**Correct (2 spaces):**

```markdown
- Item 1
  - Sub-item A
  - Sub-item B
    - Deep sub-item
```

**Incorrect (4 spaces or tabs):**

```markdown
- Item 1
    - Sub-item A
```

### 2.2 Blank Lines

Structure the document visually using blank lines, leaving exactly one empty line where needed.

- Leave one blank line before and after headers (`H1`-`H6`).
- Leave one blank line before and after lists.
- **Critical:** Always leave a blank line between a regular paragraph and a list.
- Leave one blank line before and after code blocks and blockquotes.
- **Critical (Nested):** Even when a code block is nested inside a list item, it must have a blank line before it to ensure correct parsing and visibility.

**Correct:**

````markdown
Group imports in three blocks, separated by blank lines, in this order:

1. Standard library
2. Third-party packages
3. Local / project imports
````

**Incorrect:**

````markdown
Group imports in three blocks, separated by blank lines, in this order:
1. Standard library
2. Third-party packages
3. Local / project imports
````

**Correct (Nested):**

````markdown
- Item 1

  ```bash
  code
  ```

- Item 2
````

Do not use horizontal rules (`---` or `***`) to divide sections. Rely on heading hierarchies and blank lines for visual separation.

## 3. Headings

### 3.1 Hierarchy

Always respect the heading hierarchy. Do not skip levels, such as jumping from `H1` directly to `H3`.

- Use `#` (`H1`) for the document title. There should be only one `H1` per document.
- Use `##` (`H2`) for primary sections.
- Use `###` (`H3`) for sub-sections.

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

Use the hyphen (`-`) as the default marker for unordered lists. Do not mix `*`, `+`, and `-` in the same document.

**Correct:**

```markdown
- First item
- Second item
  - Sub-item
```

### 4.2 Ordered Lists

Use a consistent ordered-list style throughout the document. When the numbering itself matters, write the actual sequence. When the numbering is only structural, you may use `1.` for every item if your formatter or renderer supports it.

**Recommended:**

```markdown
1. First step
2. Second step
3. Third step
```

### 4.3 List Density (Tight vs. Loose)

Choose list density based on the complexity and purpose of the content.

- **Tight lists (preferred for steps):** Do not leave blank lines between items. Use these for short bullet points or sequential operational steps.
- **Loose lists (for complex explanations):** Leave one blank line between all items. Use these only when every item contains multiple paragraphs or a more detailed explanation.

**Correct (Tight Steps with Nested Space):**

````markdown
1. First step.
2. Second step with code:

  ```bash
  command
  ```

3. Third step.
````

**Correct (Loose List for Detailed Info):**

```markdown
- **遇到的問題**：前端 UI 與後端 API 被瀏覽器阻擋。

- **解決方案**：腳本透過函式動態設定白名單。

- **手動設定**：直接在 `.env` 中設定 `OPENCLAW_ALLOWED_ORIGINS`。
```

## 5. Code Blocks and Inline Elements

### 5.1 Fenced Code Blocks

Always use fenced code blocks (` ``` `) instead of indented code blocks so syntax highlighting works correctly. Always specify the language identifier.

**Correct:**

```python
def hello_world():
    print("Hello, world!")
```

**Correct (Nested):**

````markdown
1. First step

  ```python
  print("Indented content")
  ```

2. Second step
````

**Incorrect:**

```text
def hello_world():
    print("Hello, world!")
```

### 5.2 Inline Code

Use single backticks for inline code, variables, file names, or terminal commands mentioned in prose.

**Example:**

To start the server, run the `npm start` command in your terminal. Ensure that `config.json` is properly set up.

## 6. Links and Images

### 6.1 Reference vs. Inline Links

For links that appear multiple times, prefer reference links placed at the bottom of the document. For one-off links, use inline links.

**Inline Link:**

Read the [official documentation](https://example.com/docs).

**Reference Link:**

Read the [official documentation][docs].

[docs]: https://example.com/docs "Optional Title"

### 6.2 Images

Always provide descriptive alt text for accessibility.

**Example:**

````markdown
![Architecture diagram showing the data flow from API to Database](./assets/architecture.png)
````

## 7. Emphasis

- Use `**` for **bold** emphasis.
- Use `_` or `*` for *italic* emphasis, but keep the choice consistent within the same document.
- Use emphasis sparingly and only when it adds meaning.

## 8. Language and Tone

Write clearly and directly. Prefer concise wording, consistent terminology, and parallel sentence structure for lists and headings.

- Prefer active voice when possible.
- Avoid mixing multiple styles in the same document.
- Keep naming consistent for commands, paths, and section titles.

## 9. Summary

Follow these core rules in every Markdown file:

- Use 2 spaces for indentation.
- Leave blank lines around headings, lists, code blocks, and blockquotes.
- Always add a blank line before a nested code block inside a list item.
- Use fenced code blocks with language identifiers.
- Keep heading levels in order.
- Use `-` for unordered lists.
- Keep ordered-list formatting consistent.
- Prefer semantic structure over visual tricks.
