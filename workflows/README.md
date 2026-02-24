# ⚡ Agent Workflows

**Workflows** 允許你定義一系列的步驟，引導 Agent 順利完成一組重複性的任務（repetitive set of tasks），例如部署服務或是回覆 PR comments。

相較於 Rules 提供持久且可重複使用的 prompt-level context，Workflows 則是在 **操作軌跡層面（trajectory level）** 提供結構化的步驟與提示，引導模型完成一系列相互關聯的任務或動作。這些流程會被儲存為 Markdown 檔案，為你提供一個簡單且可重複的方式來執行關鍵流程。

> [!NOTE]
> 每個 Workflow 包含標題 (title)、描述 (description) 與一系列指引 Agent 的步驟，單一檔案的字數限制為 **12,000 字元** (characters)。

> [!IMPORTANT]
> 註：在 Antigravity 中，若是純粹的 **「我現在就要你跑這套固定指令/步驟」**，請考慮使用 Workflows（Slash commands）。Skills 則更偏向於在特定情境下擴充 Agent 的準則與專業。例如：
>
> - git commit message -> Skills
> - deploy to aws -> Workflows

## 運行機制與特色

1. **Slash Command 觸發**：儲存後，可以透過在 Agent 輸入框中使用 `/workflow-name` 的格式來呼叫（Invoke）。
2. **循序執行 (Sequential processing)**：觸發後，Agent 會依序處理 workflow 中定義的每一個步驟，執行動作或產生對應回應。
3. **支援組合呼叫 (Call other Workflows)**：你可以在一個 workflow 內部呼叫另一個 workflow！例如：`/workflow-1` 的指令內可以包含 `Call /workflow-2` 與 `Call /workflow-3`。

## Workflow 儲存位置

Antigravity 支援直接放在專案內，或是全域配置：

- **Personal Workflows (Global):**

    ```text
    ~/.gemini/antigravity/workflows/
    ```

- **Project Workflows (Local):**

    ```text
    .agents/workflows/    # 或 .agent/, _agents/, _agent/ 依專案習慣
    ```

## 檔案格式

每個 workflow 為一個 `.md` 檔案，格式如下：

```yaml
---
description: [簡短描述，例如 how to deploy the application]
---
[具體的執行步驟 1...]
[具體的執行步驟 2...]
```

## 如何新增 Workflow

1. 在目錄建立 `<name>.md`（例如 `deploy-app.md`），該檔名即為 slash command 的名稱（`/deploy-app`）。
2. 填寫 YAML frontmatter 的 `description`。
3. 撰寫詳細的步驟說明。
