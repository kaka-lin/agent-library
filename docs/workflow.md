# WORKFLOW.md 說明

## 📌 用途

Workflow 是 **多步驟流程編排**，允許你定義一系列的步驟，引導 Agent 順利完成一組重複性的任務（repetitive set of tasks），例如部署服務或是回覆 PR comments。

相較於 Rules 提供在提示詞層面（prompt level）持久且可重複使用的 Context，Workflows 提供的是在 **操作軌跡層面（trajectory level）** 的結構化步驟或提示，引導模型完成一系列相互關聯的任務或動作。

這些流程會被儲存為 Markdown 檔案，為你提供一個簡單且可重複的方式來執行關鍵流程。

> ⚠️ 每個 Workflow 檔案的字數限制為 **12,000 字元**。

## 📂 檔案位置

Antigravity 支援直接放在專案內，或是全域配置：

| 工具 | Workspace (工作區) | Global (全域) |
| ---- | ----------------- | ------------------ |
| **Antigravity** | `.agent/workflows/` | `~/.gemini/antigravity/global_workflows/` |

> [!NOTE]
> 建立 Workflow 可以透過編輯器的 GUI：
> Open the Customizations panel -> Navigate to the Workflows panel -> Click + Global 或 + Workspace。
> 你也可以要求 Agent 直接幫你生成 Workflow (Agent-Generated Workflows)！

## ⚙️ 運行機制與特色

1. **Slash Command 觸發**：儲存後，可以透過在 Agent 輸入框中使用 `/workflow-name` （其中的 `workflow-name` 即為檔名）的格式來呼叫（Invoke）。
2. **循序執行 (Sequential processing)**：觸發後，Agent 會依序處理 workflow 中定義的每一個步驟，執行動作或產生對應回應。
3. **支援組合呼叫 (Call other Workflows)**：你可以在一個 workflow 內部呼叫另一個 workflow！例如：`/workflow-1` 的指令內可以包含 `Call /workflow-2` 與 `Call /workflow-3`。

## 📝 檔案格式與撰寫範例

Workflow 檔案為 Markdown 格式，包含 **YAML Frontmatter** 與一系列帶有具體指示的步驟。檔名即為 slash command 的名稱（例如 `test.md` → `/test`）。

- `description`（必填）：簡短描述，用於 slash command 清單顯示
- `name`（可選）：Antigravity 不強制要求（會以檔名作為識別），但建議加上以利跨平台分享

```yaml
---
name: [workflow 名稱]
description: [簡短描述，例如 how to deploy the application]
---
[具體的執行步驟]
```

### 範例 1：最簡版（檔名為 `test.md`，觸發指令為 `/test`）

```markdown
---
name: test
description: 執行專案的 lint 檢查與單元測試
---

# 執行專案測試

1. 執行 lint 檢查：`npm run lint`
2. 執行單元測試：`npm test`
3. 檢查測試覆蓋率是否達標
```

### 範例 2：完整版（含呼叫其他 Workflow，檔名為 `production-release.md`）

```markdown
---
name: production-release
description: 驗證、建置、部署應用程式的完整流程
---

# Production Release Workflow

## 前置檢查
1. 確認當前分支為 `main`
2. 確認沒有未提交的變更：`git status`

## 測試與建置
3. Call /test
4. 如果測試通過，建置生產版本：`npm run build`

## 部署準備
5. 根據 commits 產生 changelog
6. 等待使用者確認後推送到 `production` 分支
```

## 📚 參考來源

- Antigravity 官方文件：[https://antigravity.google/docs/rules-workflows](https://antigravity.google/docs/rules-workflows)
