# Idealista7 MCP Server

[English](./README_EN.md) | 简体中文 | [繁體中文](./README_ZH-TW.md)

[![MCP Badge](https://lobehub.com/badge/mcp-full/bachstudio-bach-idealista7)](https://lobehub.com/zh/mcp/bachstudio-bach-idealista7)

用于访问 Idealista（西班牙最大房产网站）API 的 MCP 服务器。支持搜索房屋、公寓、车库、商业地产、办公室等多种房产类型。

## 🚀 使用 EMCP 平台快速体验

**[EMCP](https://sit-emcp.kaleido.guru)** 是一个强大的 MCP 服务器管理平台，让您无需手动配置即可快速使用各种 MCP 服务器！

### 快速开始：

1. 🌐 访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 注册并登录账号
3. 🎯 进入 **MCP 广场**，浏览所有可用的 MCP 服务器
4. 🔍 搜索或找到本服务器（`bach-idealista7`）
5. 🎉 点击 **"安装 MCP"** 按钮
6. ✅ 完成！即可在您的应用中使用

### EMCP 平台优势：

- ✨ **零配置**：无需手动编辑配置文件
- 🎨 **可视化管理**：图形界面轻松管理所有 MCP 服务器
- 🔐 **安全可靠**：统一管理 API 密钥和认证信息
- 🚀 **一键安装**：MCP 广场提供丰富的服务器选择
- 📊 **使用统计**：实时查看服务调用情况

立即访问 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 开始您的 MCP 之旅！


---

## 简介

这是一个 MCP 服务器，用于访问 Idealista7 API，提供西班牙、葡萄牙、意大利的房产搜索功能。

- **PyPI 包名**: `bach-idealista7`
- **版本**: 2.0.0
- **传输协议**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-idealista7
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 设置环境变量
export API_KEY="your_api_key_here"

# 运行（uvx 会自动安装并运行）
uvx --from bach-idealista7 bach_idealista7
```

### 方式 2: 安装后作为命令运行

```bash
# 安装
pip install bach-idealista7

# 设置环境变量
export API_KEY="your_api_key_here"

# 运行（命令名使用下划线）
bach_idealista7
```

## 配置

### API 认证

此 API 需要 RapidAPI 密钥认证。请在 [RapidAPI](https://rapidapi.com/scraperium/api/idealista7) 获取 API 密钥后设置环境变量:

```bash
export API_KEY="your_api_key_here"
```

### 环境变量

| 变量名 | 说明 | 必需 |
|--------|------|------|
| `API_KEY` | RapidAPI 密钥 | 是 |




### 在 Cursor 中使用

编辑 Cursor MCP 配置文件 `~/.cursor/mcp.json`:

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

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:

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

此服务器提供以下 15 个工具:


### `list_home_properties`

搜索房屋/公寓列表。支持买卖/租赁，可按价格、面积、卧室数量、设施等多种条件筛选。

**端点**: `GET /listhomes`

**主要参数**:

- `order` (string) *必需*: 排序方式: relevance|lowestprice|highestprice|mostrecent 等
- `operation` (string) *必需*: 操作类型: sale|rent
- `locationId` (string) *必需*: 位置 ID，如: 0-EU-ES-28-07-001-079
- `locationName` (string) *必需*: 位置名称，如: Madrid
- `location` (string) *必需*: 国家代码: es|pt|it
- `locale` (string) *必需*: 语言: es|it|pt|en|ca|de|fr|nl|nb

---


### `list_storage_rooms`

搜索储藏室列表。

**端点**: `GET /liststoragerooms`

---


### `list_buildings`

搜索建筑物列表。

**端点**: `GET /listbuildings`

---


### `list_lands`

搜索土地列表。支持城市用地、建筑用地、非建筑用地筛选。

**端点**: `GET /listlands`

---


### `property_details`

获取房产详细信息。

**端点**: `GET /propertydetails`

**参数**:

- `propertyId` (string) *必需*: 房产 ID
- `location` (string) *必需*: 国家代码: es|pt|it
- `language` (string) *必需*: 语言: en, es, it, pt, ca, de, fr, nl, nb

---


### `list_garages`

搜索车库/停车位列表。

**端点**: `GET /listgarages`

---


### `get_sublocations`

获取某个位置下的子位置列表。

**端点**: `GET /getlocations`

---


### `get_microsite_profile`

获取房产中介的个人资料信息。

**端点**: `GET /getmicrositeprofile`

---


### `get_microsite_locations`

获取房产中介有房源的位置列表。

**端点**: `GET /getmicrositelocations`

---


### `list_commercial_properties`

搜索商业地产列表。包括店铺、工业建筑、仓库等。

**端点**: `GET /listcommercialproperties`

---


### `list_offices`

搜索办公室列表。

**端点**: `GET /listoffices`

---


### `list_rooms`

搜索出租房间列表。支持合租相关筛选。

**端点**: `GET /listrooms`

---


### `list_new_homes`

搜索新房列表。

**端点**: `GET /listnewhomes`

---


### `get_suggestions`

获取位置搜索建议（自动补全）。

**端点**: `GET /getsuggestions`

---



## 支持的国家/地区

- 🇪🇸 西班牙 (es)
- 🇵🇹 葡萄牙 (pt)
- 🇮🇹 意大利 (it)


## 技术栈

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 许可证

MIT License - 详见 [LICENSE](./LICENSE) 文件。

## 开发

此服务器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具生成。

版本: 2.0.0
