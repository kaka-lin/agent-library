# 🤖 Agent Skills Library

一個專門收集 **Agent Skills** 的資源庫。
此 repository 存放各種功能導向的 `SKILL.md` 文件，用來教 Copilot / Agent 在什麼情境下，應該如何系統性地執行任務。

## Agent Skills 使用教學

- `VS Code skills`: **「讓 Agent 自己知道什麼時候該怎麼做」；**
- `Antigravity workflows`: **「我現在就要你跑這套流程」。**

### 1. VS Code: Agent Skills

Agent Skills 是用來教 Copilot Agent **「在什麼情境下、用什麼流程與資源做事」** 的規範文件。
每個 skill 都是一個目錄，核心檔案為 `SKILL.md`。

在 VS Code 中，**你不需要也不能用 slash command 呼叫 skill**，
只要用自然語言描述需求即可，Copilot 會根據 `description` **自動載入符合的 skill**。

> [!IMPORTANT]
> VS Code Agent Skills **不是 Slash Commands**。
> Copilot 會根據 `SKILL.md` 的 `description` 自動判斷並載入對應 skill。

#### 1-1. 必要設定

請確認 VS Code 設定已開啟（Preview 功能）：

```ini
chat.useAgentSkills = true
```

#### 1-2. Skills 儲存位置

VS Code 支援 **兩種類型的 skills**：

- ##### Project Skills:
    放在 repository 中，會跟著專案一起 version control，適合團隊共用。

    ```text
    .github/skills/        # ✅ recommended
    .claude/skills/        # legacy（向下相容）
    ```

- ##### Personal Skills:

    只存在於你的使用者環境，適合個人工作流

    ```
    ~/.copilot/skills/     # ✅ recommended
    ~/.claude/skills/      # legacy（向下相容）
    ```

> [!NOTE]
> **什麼時候用哪一種？**
>
> - **Project Skills**：團隊共用、流程共識、需要 code review
> - **Personal Skills**：個人習慣、自用 workflow、不適合放進 repo

#### 1-3. Skills 目錄範例

```text
.github/skills/
  analyzing-fastapi-projects/
    SKILL.md
```

或個人 skills：

```
~/.copilot/skills/
  analyzing-fastapi-projects/
    SKILL.md
```

#### 1-4. VS Code 中如何實際使用 Skill

假設你已經有以下 skill：

```yaml
name: analyzing-fastapi-projects
description: Provides a structured workflow to analyze FastAPI codebases...
```

直接在 VS Code Copilot Chat 中輸入自然語言：

```text
請幫我分析這個 FastAPI 專案的整體架構，
我想知道 request pipeline、主要模組與開發流程。
```

Copilot 會根據 `description` 自動載入 `analyzing-fastapi-projects` skill，
並依照 `SKILL.md` 中定義的步驟執行分析。

> [!TIP]
> 如果發現 Copilot 沒有載入你預期的 skill，
> 可以在 prompt 中 明確提及 skill name 來提高命中率，例如：
>
> 請使用 analyzing-fastapi-projects 這個 agent skill，
> 幫我系統性地分析這個 FastAPI 專案的架構與 request pipeline。

### 2. Antigravity IDE: Workflows

Antigravity 的 workflow 是 **明確可呼叫的流程腳本**，屬於 command 型 Agent 能力，適合「一鍵執行完整流程」。

#### 2-1. Workflow 儲存位置

```text
/Users/kaka/.gemini/antigravity/global_workflows
```

#### 2-2. 如何使用 Workflow

Antigravity 採取 `Slash Command` 呼叫，在 Antigravity 的輸入框中直接輸入：

```text
/workflow-name
```

例如：

```text
/analyzing-fastapi-projects
/docker-healthcheck
```

這是 **Antigravity workflow 的標準用法**。

## 📚 Reference

- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills#_agent-skills-vs-custom-instructions)
- [Agent Skills Marketplace](https://skillsmp.com/)
