---
name: generate-weekly-report
description: 自動掃描指定路徑下的 Git Log，並根據「目標導向」結構生成專業中英文週報
---

# Weekly Report Generator (Generic Template)

此 Workflow 會自動遍歷指定的專案目錄，抓取 Git 日誌並彙整為目標導向的週報格式。

## 使用方式

1. **預設執行**：輸入 `/generate-weekly-report`
    - 若指令中未指定路徑，Agent 會詢問掃描根目錄（預設建議為目前工作目錄）。

2. **指定掃描路徑**：輸入 `/generate-weekly-report path /path/to/projects`
    - 直接指定要掃描的根目錄。

3. **包含額外清單**：輸入 `/generate-weekly-report include /path/to/folder1 /path/to/folder2`
    - 除了根目錄外，額外包含特定路徑。

4. **指定日期**：輸入 `/generate-weekly-report --since 2026-04-01`
    - 抓取特定日期之後的變動。

## 掃描組態 (Configuration)

- **核心掃描屬性**：遍歷指定目錄下的所有第一層子資料夾，若包含 `.git` 目錄則列入抓取範圍。
- **分支偵測**：自動偵測每個 Repo 的當前分支 (`git branch --show-current`)。

### 📌 永久新增儲存庫 (Persistent Custom Repositories)

如果您有專案位在掃描路徑**之外**，請填寫在此表格中：

| 專案名稱 | 路徑 (絕對路徑) | 說明 |
| :--- | :--- | :--- |
| **(手動填寫處)** | | |

## 流程步驟

// turbo-all

### 1. 確定掃描路徑與目標

- **互動步驟**：若未指定掃描路徑，詢問使用者要掃描的根目錄。
- 列出根目錄下的所有目錄。
- 檢查每個目錄內是否包含 `.git` 資料夾以確認為有效的 Git 儲存庫。
- 彙整合併指令參數與表格中的路徑。

### 2. 確認時間範圍 (Date Range Confirmation)

- 若未指定 `--since`，自動計算「最近兩個週三」之間的時間區間。
- **互動步驟**：在開始抓取前，向使用者確認日期範圍（例如：「預設日期範圍為 YYYY-MM-DD ~ YYYY-MM-DD，是否繼續？」）。

### 3. 抓取變動日誌

對於清單中的每個儲存庫：

- 切換至該目錄，執行 `git branch --show-current` 確定分支。
- 執行 `git log --since="<DATE>" --oneline`。
- **過濾機制**：若本週期無變動（0 commits），則從本次報告中略過。

### 4. AI 目標分類與總結

根據專案特性，將分散的 commit 分類至具體的業務目標（AI 應根據 commit 訊息自動推導分類標題）：

> [!IMPORTANT]
> 分類時不應只是條列 commit，應將多個相關的 commit 彙整成一個具有「進度感」的短句。

### 5. 產出報告檔案

- **互動步驟**：詢問使用者報告存檔路徑（若本地無指定預設目錄）。
- 產出檔案名稱：`YYYYMMDD_weekly_report.md`。
- 遵照專案設定的 [Markdown 程式碼風格規範](rules/markdown-code-style.md) 產出內容。

### 6. 完成通知

執行完畢後提供新生成的週報連結。

## 注意事項

- **日期計算**：預設週期為隔週週三，抓取前會進行人工二次確認。
- **分支安全**：僅抓取本地已知變動，不主動進行 `git pull`。
- **目錄權限**：遇到權限不足時應紀錄警告訊息並優雅跳過。
