# 🤖 Agent Library

一個專門收集 **Agent 資源** 的資源庫，包含 Skills、Workflows 和 Rules。

## 📁 目錄結構

```text
agent-library/
├── docs/            # AI Metadata 文件說明
├── rules/           # 編碼風格與 Agent 規則
├── skills/          # 情境觸發的能力模組
└── workflows/       # 多步驟流程編排
```

| 目錄 | 檔案 | 說明 |
| ---- | ---- | ---- |
| `docs/` | `*.md` | 各種 AI Metadata 文件說明與教學（如 `AGENTS.md`, `SKILL.md` 等） |
| `rules/` | `*.md` | 編碼風格、全域規則（各 Agent 共用或專用） |
| `skills/` | `SKILL.md` | 情境觸發的能力模組（跨平台 Agent Skills 標準） |
| `workflows/` | `*.md` | 多步驟流程編排（定義一系列順序執行的任務） |

## 💡 核心差異：Skill vs Workflow

| 比較維度 | 🛠️ Agent Skills (技能) | ⚡ Workflows (操作工作流) |
| :--- | :--- | :--- |
| **本質** | 提供**領域知識**、指導原則、最佳實踐。 | 提供**固定順序**的執行步驟 (SOP)。 |
| **Agent 的自由度** | **高**。Agent 學會這些原則後，會根據當下情境「靈活運用」來達成任務。 | **低**。Agent 被要求當一個無情的執行機器，必須「嚴格遵守」順序執行。 |
| **觸發方式** | **隱性為主 (Implicit)**<br>Agent 根據任務情境自動判斷並載入；部分工具亦支援 `/skill-name` 手動觸發。 | **顯性 (Explicit)**<br>你主動下指令 (Slash commands)，Agent 開始照著步驟執行。 |
| **適用場景** | 解決特定領域的**「How (該遵守什麼原則與風格)」** | 完成重複性高的**「What to do next (下一步做什麼操作)」** |

### 具體情境範例

- **情境 A：幫忙寫 Git Commit Message** 👉 **適合作為 Skill (`git-commit-helper`)**

  你希望 Agent 具備「好 Commit 的專業知識」，自動分析並寫出符合規範的內容，而非呆板的照順序敲指令。

- **情境 B：把做好的網站部署上去** 👉 **適合作為 Workflow (`/deploy-app`)**

  這件事容不得 Agent 發揮創意，順序錯了系統就會壞掉（如先 build 再打包再登入再重啟），是一套固定的標準作業流程。

- **情境 C：分析一個未知的 FastAPI 專案架構** 👉 **適合作為 Skill (`analyzing-fastapi-projects`)**

  你希望 Agent 學會「大神的分析框架與重點」，然後根據專案實際情況靈活給出報告，而不是死板的輸出固定格式。

## 📚 Reference

- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills#_agent-skills-vs-custom-instructions)
- [Agent Skills Marketplace](https://skillsmp.com/)
- [Antigravity Docs: Skills](https://antigravity.google/docs/skills)
- [Antigravity Docs: Rules & Workflows](https://antigravity.google/docs/rules-workflows)
