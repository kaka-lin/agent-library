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

### 4. AI 主題分析與智慧分類

AI 應深入分析當週各儲存庫的 Git Log 內容與對話脈絡，提取 3-4 個「主題導向」的分類，而非盲目套用固定模板。分類應能精確反映該週項目的技術重心，常見範例：

1. **核心功能開發與業務邏輯 (Core Features & Business Logic)**
    - 涉及特定產品的功能開發、API 介面調整或核心算法優化。
2. **服務穩定性與效能優化 (Service Stability & Performance Optimization)**
    - 涉及核心引擎修復、記憶體治理、Session 生命週期、及編譯/相依性優化。
3. **基礎設施與維運治理 (Infrastructure & Ops Governance)**
    - 涉及監控系統整合、Docker 部署優化、環境配置與安全性調整。
4. **開發規範與生態自動化 (Dev Standards & Ecosystem Automation)**
    - 涉及工具鏈優化、品牌視覺規範整合、文件自動化等。

**分類與彙整規範**：

- **分類命名**：使用中英文雙語標題，如 `**分類名稱 (English Name)**`。
- **彙整技巧**：不應只是條列 commit，應將多個相關的 commit 彙總成一個具有「進度感」的短句描述。
- **動態調整**：AI 應根據當週實際變動的屬性，靈活選擇最貼切的 3-4 個分類。

### 5. 產出報告檔案

- **互動步驟**：詢問使用者報告存檔路徑（若本地無指定預設目錄）。
- **產出格式與規範**：
  - 產出檔案名稱：`YYYYMMDD_weekly_report.md`。
  - **層級縮排**：遵循 [Markdown 程式碼風格規範](rules/markdown-code-style.md) 的 2 個空格縮排規範。
  - **空行處理**：各區塊（H2, List, Code Block）前後必須保留完整空行以利閱讀與解析。

### 6. 完成通知

執行完畢後提供新生成的週報連結。

## 注意事項

- **日期計算**：預設週期為隔週週三，抓取前會進行人工二次確認。
- **分支安全**：僅抓取本地已知變動，不主動進行 `git pull`。
- **目錄權限**：遇到權限不足時應紀錄警告訊息並優雅跳過。
