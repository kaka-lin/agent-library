# Rules 說明

## 📌 什麼是 Rules？

Rules 是手動定義的限制條件（manually defined constraints），用於引導 Agent 遵循特定於你個人使用情境、技術棧與程式碼風格的行為準則。

Rule 本身是一個 Markdown 檔案，你可以在其中輸入限制條件來引導 Agent 進行任務。
> ⚠️ 每個 Rules 檔案的字數限制為 **12,000 字元**。

## 📂 檔案位置與層級

根據你使用的工具（如 Antigravity, Claude Code 等），Rules 主要分為 Global (全域) 與 Workspace (工作區) 兩個層級。

| 工具 | Workspace (工作區) | Global (全域) |
| ---- | ----------------- | ------------------ |
| **Antigravity** | `.agent/rules/` | `~/.gemini/GEMINI.md`<br>`~/.gemini/antigravity/rules/` |
| **Claude Code** | `CLAUDE.md` | `~/.claude/CLAUDE.md` |
| **Cursor** | `.cursor/rules/*.mdc` | Cursor Settings |
| **Roo Code** | `RULES.md` | `~/.roo/` |

## 📝 Rules 檔案格式區分

雖然 Rules 核心都是 Markdown 檔案，但不同工具與層級在**檔案格式**上有不同的要求或擴充能力。

### 1. 通用規則：純 Markdown (以 `GEMINI.md` / `CLAUDE.md` 為例)

這些單一的全域/工作區入口檔案，**不需要任何 YAML Frontmatter**。這類檔案就是單純的文字檔，你只要直接條列開發規範與限制即可，一開啟 Agent 即會載入並當作前置條件（Always On）。

**撰寫範例：**
```markdown
# 專案開發規範

1. 永遠使用 4 個空格進行縮排。
2. 撰寫 Python 時嚴格遵守 PEP 8，方法需加上 type hints。
3. 如果不確定答案，請直接告知，不要產生幻覺。
```

### 2. Antigravity 專屬規則 (以 `.agent/rules/*.md` 為例)

當你使用 Antigravity 並在 `.agent/rules/` 目錄下建立獨立的 Rule 檔案時，Antigravity 提供了一些額外的 **YAML Frontmatter (Option 選項)** 來讓你精細控制這條規則「何時該被啟動」。

這時，你的 Markdown 檔案最上方會包含一組 `---` 包住的設定：

```yaml
---
trigger: always_on      # 定義規則的啟動方式
globs: "**/*.ts"        # 檔案路徑匹配模式 (當 trigger 為 glob 時適用)
description: "簡短描述"   # 用於 Model Decision 模式的判斷依據
name: "typescript_rules" # (可選) 規則的顯示名稱，Antigravity 不強制要求，但建議加上以利跨平台分享
---
```

#### ⚙️ 啟動模式 (`trigger`) 的選項

你可以為單一 Rule 定義以下四種啟動行為：

- **Manual (手動)** (`manual`)：透過在 Agent 的輸入框中使用 `@提及` (如 `@RuleName`) 來手動啟動該規則。
- **Always On (永遠啟用)** (`always_on`)：此規則只要在專案中，永遠會被套用（類似 GEMINI.md 的行為）。
- **Model Decision (模型決策)** (`model_decision`)：基於 `description` 所寫的自然語言描述，由模型自行判斷當下情境是否需要套用此規則。
- **Glob (檔案路徑匹配)** (`glob`)：必須配合 `globs` 屬性。當 Agent 正在處理符合該 pattern (例如 `*.js`, `**/*.ts`) 的檔案時，該規則才會被啟動套用。

**Antigravity Rule 完整撰寫範例：**
```markdown
---
name: react-guidelines
description: Ensure all React components use functional components and hooks.
trigger: glob
globs: "**/*.tsx"
---

# React Guidelines

- Use functional components.
- Do not use class components.
- Prop types must be explicitly defined.
```

## 🔗 特殊功能：@ 提及 (Mentions)

你可以在 Rules 檔案中使用 `@filename` 的語法來引用其他的檔案作為上下文。

- **相對路徑**：如果 `filename` 是相對路徑，它會相對於該 Rules 檔案所在的位置進行解析。
- **絕對路徑**：如果 `filename` 是絕對路徑，它會被優先當作真正的絕對路徑解析；否則會相對於 repository 的根目錄來解析。
  - *範例*：`@/path/to/file.md` 會先嘗試解析為系統上的 `/path/to/file.md`，如果該檔案不存在，則會當作 `workspace/path/to/file.md` 解析。
