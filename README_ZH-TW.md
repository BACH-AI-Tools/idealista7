# Idealista7 MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

[![MCP Badge](https://lobehub.com/badge/mcp-full/bachstudio-bach-idealista7)](https://lobehub.com/zh/mcp/bachstudio-bach-idealista7)

用於存取 Idealista（西班牙最大房產網站）API 的 MCP 伺服器。支援搜尋房屋、公寓、車庫、商業地產、辦公室等多種房產類型。

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-idealista7`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個 MCP 伺服器，用於存取 Idealista7 API，提供西班牙、葡萄牙、義大利的房產搜尋功能。

- **PyPI 套件名**: `bach-idealista7`
- **版本**: 2.0.0
- **傳輸協定**: stdio


## 安裝

### 從 PyPI 安裝:

```bash
pip install bach-idealista7
```

### 從原始碼安裝:

```bash
pip install -e .
```

## 執行

### 方式 1: 使用 uvx（推薦，無需安裝）

```bash
# 設定環境變數
export API_KEY="your_api_key_here"

# 執行（uvx 會自動安裝並執行）
uvx --from bach-idealista7 bach_idealista7
```

### 方式 2: 安裝後作為命令執行

```bash
# 安裝
pip install bach-idealista7

# 設定環境變數
export API_KEY="your_api_key_here"

# 執行（命令名使用底線）
bach_idealista7
```

## 配置

### API 認證

此 API 需要 RapidAPI 金鑰認證。請在 [RapidAPI](https://rapidapi.com/scraperium/api/idealista7) 取得 API 金鑰後設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | RapidAPI 金鑰 | 是 |




### 在 Cursor 中使用

編輯 Cursor MCP 配置檔案 `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "bach-idealista7": {
      "command": "uvx",
      "args": ["--from", "bach-idealista7", "bach_idealista7"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### 在 Claude Desktop 中使用

編輯 Claude Desktop 配置檔案 `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "bach-idealista7": {
      "command": "uvx",
      "args": ["--from", "bach-idealista7", "bach_idealista7"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```


## 可用工具

此伺服器提供以下 15 個工具:


### `list_home_properties`

搜尋房屋/公寓列表。支援買賣/租賃，可按價格、面積、臥室數量、設施等多種條件篩選。

**端點**: `GET /listhomes`

**主要參數**:

- `order` (string) *必需*: 排序方式: relevance|lowestprice|highestprice|mostrecent 等
- `operation` (string) *必需*: 操作類型: sale|rent
- `locationId` (string) *必需*: 位置 ID，如: 0-EU-ES-28-07-001-079
- `locationName` (string) *必需*: 位置名稱，如: Madrid
- `location` (string) *必需*: 國家代碼: es|pt|it
- `locale` (string) *必需*: 語言: es|it|pt|en|ca|de|fr|nl|nb

---


### `list_storage_rooms`

搜尋儲藏室列表。

**端點**: `GET /liststoragerooms`

---


### `list_buildings`

搜尋建築物列表。

**端點**: `GET /listbuildings`

---


### `list_lands`

搜尋土地列表。支援城市用地、建築用地、非建築用地篩選。

**端點**: `GET /listlands`

---


### `property_details`

取得房產詳細資訊。

**端點**: `GET /propertydetails`

**參數**:

- `propertyId` (string) *必需*: 房產 ID
- `location` (string) *必需*: 國家代碼: es|pt|it
- `language` (string) *必需*: 語言: en, es, it, pt, ca, de, fr, nl, nb

---


### `list_garages`

搜尋車庫/停車位列表。

**端點**: `GET /listgarages`

---


### `get_sublocations`

取得某個位置下的子位置列表。

**端點**: `GET /getlocations`

---


### `get_microsite_profile`

取得房產仲介的個人資料資訊。

**端點**: `GET /getmicrositeprofile`

---


### `get_microsite_locations`

取得房產仲介有房源的位置列表。

**端點**: `GET /getmicrositelocations`

---


### `list_commercial_properties`

搜尋商業地產列表。包括店鋪、工業建築、倉庫等。

**端點**: `GET /listcommercialproperties`

---


### `list_offices`

搜尋辦公室列表。

**端點**: `GET /listoffices`

---


### `list_rooms`

搜尋出租房間列表。支援合租相關篩選。

**端點**: `GET /listrooms`

---


### `list_new_homes`

搜尋新房列表。

**端點**: `GET /listnewhomes`

---


### `get_suggestions`

取得位置搜尋建議（自動補全）。

**端點**: `GET /getsuggestions`

---



## 支援的國家/地區

- 🇪🇸 西班牙 (es)
- 🇵🇹 葡萄牙 (pt)
- 🇮🇹 義大利 (it)


## 技術棧

- **傳輸協定**: stdio
- **HTTP 客戶端**: httpx

## 授權

MIT License - 詳見 [LICENSE](./LICENSE) 檔案。

## 開發

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具生成。

版本: 2.0.0
