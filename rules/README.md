# 📏 Agent Rules

**Agent Rules** 是手動定義的限制條件（manually defined constraints），用來指引 Agent 必須遵循的行為準則。

透過 Rules，你可以引導 Agent 遵循特定於你個人的使用情境、stack 與 coding style。相較於提供多步驟引導的 Workflows，Rules 提供的是**在提示詞層面（prompt level）持久且可重複使用的 Context**。

> [!NOTE]
> 每個 Rule 都是單一個 Markdown 檔案，檔案內的字數限制為 **12,000 字元** (characters)。

## 分類

| 類型 | 範例 | 說明 |
| ---- | ---- | ---- |
| 通用規則 | `global-rules.md` | 跨語言、跨 Agent 的通用入口點 (Router) |
| 語言規則 | `python-code-style.md` | 特定語言的 coding style guide |
| 語言規則 | `markdown-code-style.md` | Markdown 撰寫樣式與排版準則 |

## 部署 Global Rules

`global-rules.md` 是所有 AI Agent 的**唯一入口點**。
不同工具有不同的配置檔名與路徑，請依照下表複製並重新命名：

| 工具 | Local（專案配置） | Global（個人配置） |
| ---- | ---- | ---- |
| Antigravity | `.agent/rules/` | `~/.gemini/antigravity/rules/` |
| Roo Code | `RULES.md` | `~/.roo/` |
| Cursor | `.cursor/rules/*.mdc` | Cursor Settings |
| Claude Code | `CLAUDE.md` | `~/.claude/CLAUDE.md` |

### 部署範例

```bash
# Antigravity (Global)
cp rules/global-rules.md ~/.gemini/antigravity/rules/global-rules.md

# Claude Code (Global)
cp rules/global-rules.md ~/.claude/CLAUDE.md

# Roo Code (Local)
cp rules/global-rules.md ./RULES.md

# Cursor (Local)
cp rules/global-rules.md .cursor/rules/global-rules.mdc
```

## 如何新增 Rule

1. 在此目錄建立 `<name>.md`（例如 `typescript-code-style.md`），檔名請使用 kebab-case
2. 填寫 YAML frontmatter 的 `name` 與 `description`
3. 清楚描述規則的適用範圍與具體限制條件
4. 在 `global-rules.md` 中新增對應語言的連結，讓 AI 知道要去讀它
