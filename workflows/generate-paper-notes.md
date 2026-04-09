---
name: generate-paper-notes
description: 讀論文並生成 README.md（簡介）與 paper_notes.md（詳細筆記）的完整流程
---

# Paper Notes Generator

讀一篇論文（arXiv 或 PDF），自動產出兩個 Markdown 檔案：

- **README.md**：高階概覽，讓讀者快速掌握重點
- **paper_notes.md**：詳細的論文筆記，涵蓋架構、訓練策略、實驗結果等

## 使用方式

```text
使用者提供：論文的 arXiv 連結或 PDF 路徑，以及要輸出的目標目錄
```

## 流程步驟

### 1. 閱讀論文全文

使用 `read_url_content` 讀取論文的 arXiv HTML 版本（優先），或請使用者提供 PDF。

- 逐 chunk 閱讀，確保涵蓋所有 section（Abstract、Introduction、Architecture、Training、Experiments、Conclusion 等）
- 記錄每個 section 的核心要點

### 2. 確認目標目錄結構

確認或建立以下目錄結構：

```text
<目標目錄>/
├── README.md          ← 簡介與快速概覽
├── paper_notes.md     ← 詳細論文筆記
└── images/            ← 論文圖片（如有需要）
```

### 3. 生成 README.md（簡介）

`README.md` 應包含以下結構，保持**精簡**，讓讀者能在 1 分鐘內掌握論文重點：

```markdown
# <論文/模型名稱> Notes

<一段話描述：這是什麼、解決什麼問題、核心創新點>

## 模型 / 方法概覽

<用表格或列點呈現模型家族、變體、關鍵規格>

## 核心架構

<用 text block 畫出簡化的架構流程圖>
<列點說明每個關鍵元件的角色>

> [!NOTE]
> 詳細的架構設計、訓練策略與實驗結果，請參閱 [論文詳細筆記](./paper_notes.md)。

## References

<arXiv 連結、GitHub repo、HuggingFace 模型頁面等>
```

### README.md 撰寫原則

- 一句話能說完的事不要用兩句
- 用表格整理可比較的規格
- 架構用 `text` block 流程圖呈現，搭配關鍵元件列點說明
- 末尾用 `[!NOTE]` 引導讀者到 `paper_notes.md`

### 4. 生成 paper_notes.md（詳細筆記）

`paper_notes.md` 應按照**論文的 section 順序**組織，涵蓋所有重要技術細節：

```markdown
# <論文名稱> 論文詳細筆記：<副標題>

<概述段落：背景動機與問題定義>

<圖片：論文的 overview/introduction 圖>

## 1. <對應論文 Section> (英文標題)

<詳細技術內容>

## 2. 核心架構設計 (Architecture)

<圖片：架構圖>
<架構描述、各元件說明>
<參數規格表（如適用）>

## 3. 訓練策略 (Training Strategies)

<分階段描述訓練流程>
<結構化輸出範例（如適用）>

## N. 性能評估與基準測試 (Benchmarks)

<評估維度、基線系統、關鍵數據>

## N+1. 總結 (Conclusion)

<核心成果、開源資訊>
```

### paper_notes.md 撰寫原則

- 章節編號與標題使用 `## N. 中文標題 (English Title)` 格式
- 子章節使用 `### N.M 中文標題 (English Title)` 格式
- 技術術語使用 backticks：`模型名稱`、`技術名詞`
- 關鍵概念使用粗體：**重要概念**
- 適當使用 `[!NOTE]`、`[!IMPORTANT]` 等 GitHub alerts 補充說明
- 圖片使用 HTML `<p align="center">` 置中，並附圖片來源
- 數據比較盡量使用表格
- 用具體範例與 `text` block 解釋抽象概念（如 slot-filling 機制）
- 英文術語不強制翻譯，保留原文（如 timestamps、embeddings）以利閱讀

### 5. 下載與放置論文圖片

如果論文有重要的架構圖或說明圖：

- 從論文 GitHub repo 或 arXiv 下載相關圖片
- 放置在 `images/` 子目錄
- 在 md 檔中使用相對路徑引用：`./images/<圖片名稱>.png`
- 圖片使用以下格式置中並標註來源：

  ```html
  <p align="center">
    <img src="./images/<圖片名稱>.png" alt="示意圖" />
    <br>
    <sub>圖片來源：<a href="<來源URL>">來源名稱</a></sub>
  </p>
  ```

### 6. 格式檢查

完成後進行最終格式檢查：

- [ ] 標題層級正確（H1 → H2 → H3，不跳級）
- [ ] 無多餘空行（section 之間只保留一個空行）
- [ ] 圖片位置合理（圖片在上，文字描述在下，引用「如上圖」）
- [ ] 無 `---` 分隔線（使用空行分隔 section 即可）
- [ ] `README.md` 的 `[!NOTE]` 正確連結到 `paper_notes.md`
- [ ] 術語風格統一（不混用中英翻譯）
- [ ] 內容與論文一致，無遺漏重要 section

### 7. 請使用者審閱

使用 `notify_user` 請使用者審閱 `README.md` 和 `paper_notes.md`，附上：

- 兩個檔案的路徑
- 簡要的結構說明

## 注意事項

- **語言**：預設使用**繁體中文**撰寫筆記，技術術語保留英文原文
- **圖片**：如論文有 GitHub repo，優先從 repo 下載高品質圖片
- **準確性**：所有數據和描述必須忠實反映論文內容，不添加論文中沒有的資訊
- **補充說明**：可在 `[!NOTE]` 區塊中添加有助理解的補充資訊（如計算推導、概念解釋），但需標明是補充資訊。
