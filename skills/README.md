# 🛠️ Agent Skills

**Agent Skills** 是可重複使用的知識包（reusable packages of knowledge），用來擴充 AI Agent 的能力。
這是一個跨多個 AI Agent（包含 GitHub Copilot, Antigravity 等）的開放標準（Open Standard）。

每個 skill 都是一個獨立目錄，核心檔案為 `SKILL.md`，內容通常包含：

- **指示 (Instructions)**：教學如何處理特定類型的任務。
- **最佳實踐與慣例 (Best practices and conventions)**：必須遵循的準則與流程。
- **選用腳本與資源 (Optional scripts and resources)**：供 Agent 輔助使用的範例或額外檔案。

> [!NOTE]
> ### 為什麼需要 Agent Skills？ (Key Benefits)
>
> - **特化 Agent 能力 (Specialize)**：針對特定領域的任務打造專屬能力，不需每次重複給予 Context。
> - **減少重複 (Reduce repetition)**：建立一次，就能自動在所有對話中重複使用。
> - **組合能力 (Compose capabilities)**：組合多個 skills 來建立複雜的工作流。
> - **高效載入 (Efficient loading)**：只有當領域任務相關時，才會將內容載入到 Context 中。

> [!IMPORTANT]
> 註：在 Antigravity 中，若是純粹的 **「我現在就要你跑這套固定指令/步驟」**，請考慮使用 Workflows（Slash commands）。Skills 則更偏向於在特定情境下擴充 Agent 的準則與專業。例如：
>
> - git commit message -> Skills
> - deploy to aws -> Workflows

### 目錄 (Table of Contents)

- [1. VS Code Copilot 中的 Agent Skills](#1-vs-code-copilot-中的-agent-skills)
- [2. Antigravity 中的 Agent Skills](#2-antigravity-中的-agent-skills)

## 1. VS Code Copilot 中的 Agent Skills

在 VS Code 中，Agent Skills 的核心概念是 **「自動根據對話情境配對對應的技能」**。除了 VS Code 外，這套標準也可跨平台運行在 GitHub Copilot CLI 與其他相容的 agent 生態系中。

> [!IMPORTANT]
> VS Code Agent Skills 的核心設計是**自動配對**，不需手動呼叫。
> 只要用自然語言描述需求，Copilot 會根據 `SKILL.md` 的 `description` 自動判斷並載入對應 skill。較新版本亦支援透過 slash command 手動觸發。

### Agent Skills vs Custom Instructions

在 VS Code 中，這兩者雖然都是用來自訂 Copilot，但目的與作用範圍完全不同：

| 特性 | Agent Skills | Custom Instructions (Rules) |
| :--- | :--- | :--- |
| **目的** | 教導特化 (Specialized) 的能力與工作流 | 定義專案的 Coding standard（排版、命名等原則） |
| **內容** | Instructions, scripts, examples, resources | 只有 Instructions |
| **範圍** | 針對**特定任務** (Task-specific)，按需動態載入 | **永遠套用** (Always applied) |
| **標準** | 開放標準跨平台 (agentskills.io) | VS Code 專屬 |

**👉 何時該用 Agent Skills？**

- 建立跨 AI 工具可重複使用的能力。
- 需要在指示之外，搭配腳本 (scripts)、範例 (examples) 或其他資源。
- 定義特化的工作流程：如特定的測試、除錯或部署流程。

**👉 何時該用 Custom Instructions (Rules)？**

- 定義專案特定的 Coding standards 或語言慣例。
- 定義 Code review 或 Commit message 的通用準則。
- 需要基於檔案類型 (Glob patterns) 自動套用規則時。

### 1-1. 必要設定與儲存位置

請確認 VS Code 設定已開啟（Preview 功能）：

```ini
chat.useAgentSkills = true
```

支援兩種類型的 skills 儲存位置：

- **Project Skills**: 適合團隊共用，跟著專案版控。

  ```text
  .github/skills/        # ✅ recommended
  ```

- **Personal Skills**: 適合個人工作流。

  ```text
  ~/.copilot/skills/     # ✅ recommended
  ```

### 1-2. 在 VS Code 實際使用範例

假設有以下 skill (`.github/skills/git-commit-helper/SKILL.md`)：

```yaml
---
name: git-commit-helper
description: Generate clear, conventional Git commit messages by analyzing staged Git changes only.
---
```

在 Copilot Chat 中直接輸入自然語言：
> *"請幫我分析 staged 的修改並產生 commit message。"*

Copilot 就會自動載入該 skill 執行任務。如果命中率不高，可以在 prompt 明確提及：
> *"請參考 git-commit-helper 這個 agent skill，幫我產生 commit message。"*

## 2. Antigravity 中的 Agent Skills

在 Antigravity 中，對於 Skills 的官方核心定義為：
**「當你開始對話時，Agent 會看到可用 skills 的清單（包含名稱與描述）。如果某個 skill 看起來與你的任務相關，Agent 就會讀取完整的指示並遵循其內容執行。」**

功能上同樣作為特化任務的擴展，使用體驗是：**「開局自動載入技能清單，遇相關任務主動讀取並遵循。」**

> [!NOTE]
> 註：在 Antigravity 中，若是純粹的 **「我現在就要你跑這套固定指令/步驟」**，請考慮使用 Workflows（Slash commands）。Skills 則更偏向於在特定情境下擴充 Agent 的準則與專業。

### 2-1. 運作機制

1. **背景清單**：對話開始時，系統會自動將可用的 skills 名稱與描述傳給 Agent。
2. **主動讀取**：當 Agent 評估任務時，若發現某 skill 有幫助，會主動調用工具去載入該 skill 完整的 `SKILL.md`（甚至是目錄內的 scripts 與 examples）。
3. **依規執行**：Agent 在了解完整的知識包後，便會嚴格遵循裡頭的指示進行開發或回覆。

### 2-2. 儲存位置與目錄架構

Antigravity 主要推薦存放於個人全域目錄：

```text
~/.gemini/antigravity/skills/    # ✅ recommended
  git-commit-helper/
    SKILL.md
    scripts/        # (可選) 輔助腳本
    examples/       # (可選) 參考實作
```

### 2-3. 在 Antigravity 實際使用範例

設置好 `git-commit-helper` 的 `SKILL.md`（需包含 YAML 的 `name` 與 `description`）後，如同 Copilot，**你通常不需要手動指定**：

> *"請幫我分析暫存區的變更，並產生一個 commit message。"*

Antigravity 收到任務後：

1. 查閱開局任務背景中的技能清單，發現 `git-commit-helper` 相關。
2. 主動讀取 `~/.gemini/antigravity/skills/git-commit-helper/SKILL.md` 獲取規則。
3. 按照文件內定義的 Instructions 與 Conventions 完成任務。
