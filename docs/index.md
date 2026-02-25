# AI Metadata 文件說明

> [!NOTE]
> 本文件最後更新日期：2026-02-25
> 各工具功能可能隨版本更新而有所變動，請以官方文件為準。

本系列文件整理並說明 **AGENTS.md / SKILL.md / WORKFLOW.md / RULES.md** 的用途、結構、格式、差異與在各 AI 工具中的使用方式。

## 各種 AI Metadata 文件說明與比較

| 文件 | 扮演角色 | 類比 | 核心功能 |
| ---- | -------- | ---- | -------- |
| [AGENTS.md](./agents.md) | 專案全域入口 | 專案的 AI 版 README | 告訴 AI：這是什麼專案、該怎麼工作 |
| [SKILL.md](./skill.md) | 單一功能模組說明 | API 說明書 | 描述單一功能與 I/O |
| [WORKFLOW.md](./workflow.md) | 自動化流程 | Pipeline YAML | 定義多步驟任務（多 Skill 的 orchestration） |
| [RULES.md](./rules.md) | 共同規範 | Coding Style Guide | 所有 AI 代理都需遵守的規範 |

> 💡 **一句話記住**：AGENTS = 專案背景、SKILL = 能力、WORKFLOW = 流程、RULES = 規範

## 各工具支援度比較

### 支援的 Metadata 類型

| 工具 | AGENTS.md | SKILL.md | WORKFLOW.md | RULES.md |
| ---- | :-------: | :------: | :---------: | :------: |
| **VSCode + Copilot** | ✅ | ✅ | ✅ | ❌ |
| **Cursor** | ✅ | ⚠️ 部分 | ⚠️ 部分 | ❌ |
| **Claude Code** | ✅ | ✅ | ✅ | ❌ |
| **Roo Code** | ✅ | ⚠️ 部分 | ⚠️ 部分 | ✅ |
| **Antigravity** | ✅ | ✅ | ✅ | ✅ |

### 設定檔位置

| 工具 | Local（專案配置） | Global（個人配置） |
| ---- | ----------------- | ------------------ |
| **VSCode + Copilot** | `AGENTS.md`<br>`.github/copilot-instructions.md`<br>`.github/skills/`<br>`.github/agents/xxx.agent.md`<br>`.agents/skills/` | `~/.copilot/copilot-instructions.md`<br>`.copilot/skills/`<br>`.copilot/agents/xxx.agent.md`<br>`~/.agents/skills/` |
| **Cursor** | `.cursor/rules/*.mdc` | **Cursor Settings** (Rules for AI UI)<br>`~/.cursorrules` |
| **Claude Code** | `CLAUDE.md` | `~/.claude/config.json`<br>`~/.claude/CLAUDE.md` |
| **Antigravity** | `.agent/rules/`<br>`.agent/workflows/`<br>`.agent/skills/` | `~/.gemini/GEMINI.md`<br>`~/.gemini/antigravity/rules/`<br>`~/.gemini/antigravity/workflows/`<br>`~/.gemini/antigravity/skills/` |

### 解析優先級

當專案中同時存在多個 metadata 檔案時，各工具的處理方式：

| 優先級 | 說明 |
| ------ | ---- |
| **1. 工具專屬檔案優先** | 各工具會優先讀取自己的專屬設定檔（如 Cursor 讀 `.cursorrules`，Claude Code 讀 `CLAUDE.md`） |
| **2. Local 優先於 Global** | 專案內的設定會覆蓋個人全域設定 |
| **3. AGENTS.md 作為補充** | 當專屬檔案不存在時，多數工具會 fallback 讀取 `AGENTS.md` |

> [!TIP]
> **建議策略**：維護一份 `AGENTS.md` 作為通用基礎，再針對常用工具補充專屬設定檔。這樣可以確保任何 AI 工具都能理解你的專案。

### 推薦做法

1. **從 AGENTS.md 開始** - 每個專案都應該有一個 AGENTS.md 作為 AI 的入口點
2. **保持簡潔** - 避免過長的描述，AI 更容易理解簡潔的指令
3. **使用標準格式** - Skills 和 Workflows 需遵循 YAML frontmatter 格式（AGENTS.md 和 GEMINI.md 則為純 Markdown，不需 frontmatter）
4. **定期更新** - 當專案架構改變時，同步更新 metadata 檔案
5. **版本控制** - 將所有 metadata 檔案納入版本控制

### 避免的事

1. **不要過度複雜化** - 不需要定義每個小功能為 Skill，過度拆分會讓 AI decision tree 變亂。
2. **不要重複定義** - 避免在多個檔案中重複相同的規則

    ```text
    如：RULES.md 只寫規範，AGENTS 別再放一次。
    ```

3. **不要包含敏感資訊** - API keys、密碼等不應出現在 metadata 中
4. **不要假設 AI 知道一切** - 明確寫出你的期望和限制，該說明的請清楚寫在 AGENTS.md。
