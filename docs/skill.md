# SKILL.md 說明

## 📌 用途

Skill 是 **可重複使用的功能模組**，用於定義 AI 代理的特定能力。
被 Workflow 或 Agents 呼叫，讓 AI 知道「如何執行特定任務」。

AI 會把 skill 當成：
→「一組明確的操作指令與執行流程」

## 📂 檔案位置

| 工具 | Local（專案配置） | Global（個人配置） |
| ---- | ----------------- | ------------------ |
| **VSCode + Copilot** | `.github/skills/<skill-name>/`<br>`.agents/skills/` | `~/.copilot/skills/`<br>`~/.agents/skills/` |
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Antigravity** | `.agent/skills/` | `~/.gemini/antigravity/skills/` |

## SKILL.md 規範

根據 [Agent Skills 開放規範](https://agentskills.io/) ，SKILL.md 由 **YAML Frontmatter** + **Markdown Body** 組成。

### YAML Frontmatter 欄位

#### 基本欄位

| 欄位 | 必填 | 說明 |
| ---- | :---: | ---- |
| `name` | ✅ | Skill 的唯一識別名稱（小寫字母、數字、連字號） |
| `version` | ❌ | 版本號（如 `1.0.0`） |
| `description` | ✅ | 簡短、明確的功能描述，幫助 AI 決定調用時機 |
| `runtime` | ❌ | 執行環境（如 `python3` / `nodejs` / `bash` / `rest-api`） |
| `repository` | ❌ | 專案來源網址 |
| `argument-hint` | ❌ | [VSCode] 執行時所需的參數提示（如 `[test file] [options]`） |
| `user-invokable` | ❌ | [VSCode] 是否為使用者可手動調用（`true` / `false`） |
| `disable-model-invocation` | ❌ | [VSCode] 是否禁止 AI 自動調用（`true` / `false`） |

#### 輸入輸出定義

| 欄位 | 說明 |
| ---- | ---- |
| `inputs` | 技能所需的輸入參數列表 |
| `inputs[].name` | 參數名稱 |
| `inputs[].type` | 型別（`string` / `number` / `boolean` / `object` / `array`） |
| `inputs[].description` | 參數詳細用途說明 |
| `inputs[].required` | 是否必填（`true` / `false`） |
| `inputs[].default` | 預設值（可選） |
| `outputs` | 技能回傳的輸出結果列表 |
| `outputs[].name` | 回傳欄位名稱 |
| `outputs[].type` | 型別 |
| `outputs[].description` | 回傳結果的含義 |
| `error_codes` | 可能的錯誤代碼列表（可選） |

### Markdown Body 建議區塊

- **📖 技能簡介**：詳細描述功能與定位
- **🎯 調用時機**：AI 何時應該使用此技能
- **🛠 調用規範**：進入點、限制條件
- **📝 實戰範例**：Few-shot Examples
- **⚠️ 安全與邊界**：不應使用的場景

### 範例 1：最簡版

```markdown
---
name: code-review
description: 審查程式碼並提供改進建議
---

# Code Review Skill

當使用者要求審查程式碼時，請使用此技能。

## 操作流程

1. 閱讀提供的程式碼
2. 檢查潛在問題（錯誤、效能、可讀性）
3. 提供具體的改進建議

## 範例

- "幫我審查這段 Python 程式碼"
- "這個函式有什麼問題？"
```

### 範例 2：完整版（Template）

適合需要明確定義輸入輸出的複雜技能：

```markdown
---
name: <unique-skill-id>
version: 1.0.0
description: 簡短、明確的功能描述，幫助 LLM 決定調用時機
runtime: python3

inputs:
  - name: <參數名稱>
    type: string
    description: 參數詳細用途說明
    required: true
  - name: <可選參數>
    type: number
    description: 可選參數說明
    required: false
    default: 10

outputs:
  - name: result
    type: object
    description: 回傳結果的含義

error_codes:
  - code: INVALID_INPUT
    description: 輸入格式不正確，請確認參數類型
  - code: NOT_FOUND
    description: 找不到指定的資源
---

# Skill: <技能顯示標題>

## 📖 技能簡介 (Description)

詳細描述此技能的具體功能、解決的問題以及它在整個系統中的定位。

## 🎯 調用時機 (Trigger/Usage Guidelines)

- 描述 AI 在收到什麼樣的指令時應該考慮使用此技能
- 描述使用此技能的前置條件

## 🛠 調用規範 (Technical Details)

- **進入點**: 函數名稱或 API EndPoint
- **限制條件**: 每分鐘調用次數、最大處理數據量

## 📝 實戰範例 (Few-shot Examples)

### 範例一：標準成功調用

**User:** "使用者輸入的指令範例"
**Action:** `call <name>(<inputs>)`
**Response:** 預期的回傳數據結構

### 範例二：缺少必要參數

**User:** "缺少資訊的指令"
**Assistant:** "我需要您提供 [參數名稱] 才能為您執行此操作。"

## ⚠️ 安全與邊界 (Safety & Constraints)

- 定義 AI 不應該使用此技能的負面場景
- 執行此技能時的安全性警告（如：涉及資料刪除時必須二次確認）

## 📚 相關參考 (References)

- 相關的 API 文件連結或背景知識
```

## 📚 參考來源

- 官方規範：[https://agentskills.io/](https://agentskills.io/)
- 技能市場：[https://skillsmp.com/](https://skillsmp.com/)
