---
name: git-commit-helper
description: 透過分析僅限於「暫存（staged）」的 Git 變更，生成清晰且符合約定式提交（Conventional Commits）規範的提交訊息。此工具不限於特定編輯器，可跨 AI 編碼助手使用。
---

# Git Commit Helper

## 目的

分析**僅限於暫存（staged）的 Git 變更**，並根據 **約定式提交（Conventional Commits）** 標準生成高品質的提交訊息。

此技能具**有通用性**，旨在支援：

- VS Code Copilot / Copilot Chat
- Antigravity
- 基於 CLI 的 AI 代理
- 任何可以存取 `git diff --staged` 的編輯器或工作流

---

## 範圍假設

本指南假設提交訊息是基於 `git diff --staged` 中可見的變更撰寫的。

未暫存（unstaged） 的變更（包括未追蹤的文件）均被視為超出本次提交說明的範圍。

因此，提交訊息僅專注於出現在暫存差異（staged diff）中的檔案與修改。

---

## 使用時機

適用於以下情境：

- 撰寫提交訊息（Commit Message）
- 在提交前審閱**已暫存**的變更
- 強制執行「約定式提交」規範
- 提升長期 Git 紀錄（History）的品質

---

## 預期輸入

助手應按以下順序優先採用輸入資訊：

1. `git diff --staged`
2. `git diff`（僅在明確說明「所有變更都將被提交」時使用）
3. 貼上的暫存差異內容或補丁（Patch）

助手必須**忽略**：

- `git status` 中的未追蹤檔案

若未提供暫存差異，請在生成提交訊息**之前**要求使用者澄清。

---

## 輸出格式

\`\`\`
<類型>(<範圍>): <簡短描述>

[選填正文]

[選填頁腳]
\`\`\`

---

## 提交類型 (Commit Types)

| 類型     | 意義                                 |
|----------|--------------------------------------|
| feat     | 新功能 (New feature)                 |
| fix      | 修復 Bug (Bug fix)                   |
| docs     | 僅文件更動 (Documentation)           |
| style    | 格式、標點符號、空格（不影響邏輯）   |
| refactor | 重構（既非修正 Bug 也非新增功能）    |
| test     | 新增或更新測試                       |
| chore    | 維護、工具、CI 設定等                |

---

## 撰寫規則

### 摘要行 (Summary Line)

- 使用**祈使句**（如 `add` 而非 `added`，`fix` 而非 `fixed`）
- 字數 ≤ 50 個字元
- 首字母大寫，末尾不加句點
- 必須**精確符合暫存的變更**

### 正文 (Body)

- 解釋**為什麼**要進行這項暫存的變更
- 描述行為或結構上的影響
- 優先使用列點說明
- **不可**提及未暫存或未來的工作

## 頁腳 (Footer)

- 引用相關議題（Issue）：`Refs #123`, `Closes #456`
- 若有「重大變更」，請在此聲明

---

## 範例

### 新功能 (Feature)

```text
feat(auth): 新增 JWT 驗證功能

- 實作基於 Token 的登入機制
- 新增 Token 驗證中間件
- 支援 Refresh Token
```

### 修復 (Bug Fix)

```text
fix(api): 防止設定檔資料為空時當機

在存取巢狀欄位前加入空值檢查（null checks）。
```

### 重構 (Refactor)

```text
refactor(db): 簡化查詢構建邏輯

- 提取共用的查詢邏輯
- 減少程式碼重複
```

---

## 多檔案變更（僅限暫存部分）

```text
refactor(core): 重構身份驗證模組

- 將邏輯移至服務層 (Service layer)
- 提取驗證器 (Validators)
- 更新相關測試

BREAKING CHANGE: 身份驗證服務現在需要傳入設定物件
```

---

## 重大變更 (Breaking Changes)

```text
feat(api)!: 更改回應格式

BREAKING CHANGE:
API 回應現在遵循 JSON:API 規範。
```

---

### 建議工作流程

```bash
git add -p
git diff --staged
git commit -m "type(scope): description"
```

---

## 修改提交 (Amend)

```bash
git commit --amend
git add forgotten-file
git commit --amend --no-edit
```

---

## 最佳實踐

- 每個提交僅包含一個邏輯上的變更
- 提交訊息必須與 `git show` 的內容一致
- 如果檔案不在 `git show` 中，則絕不能被提及
- 傾向於小而集中的提交
- 為未來的維護者撰寫訊息

---

## 檢查清單

- [ ] 只描述已暫存的檔案
- [ ] 正確的 commit type
- [ ] 明確的 scope
- [ ] 摘要使用命令式語氣
- [ ] 摘要 ≤ 50 字元
- [ ] 正文是否解釋了原因（Why）
- [ ] 是否已標記重大變更
