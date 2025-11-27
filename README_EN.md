# Idealista7 MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

[![MCP Badge](https://lobehub.com/badge/mcp-full/bachstudio-bach-idealista7)](https://lobehub.com/zh/mcp/bachstudio-bach-idealista7)

An MCP server for accessing Idealista (Spain's largest real estate website) API. Supports searching for homes, apartments, garages, commercial properties, offices and more.

## 🚀 Quick Start with EMCP Platform

**[EMCP](https://sit-emcp.kaleido.guru)** is a powerful MCP server management platform that allows you to quickly use various MCP servers without manual configuration!

### Quick Start:

1. 🌐 Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)**
2. 📝 Register and login
3. 🎯 Go to **MCP Marketplace** to browse all available MCP servers
4. 🔍 Search or find this server (`bach-idealista7`)
5. 🎉 Click the **"Install MCP"** button
6. ✅ Done! You can now use it in your applications

### EMCP Platform Advantages:

- ✨ **Zero Configuration**: No need to manually edit config files
- 🎨 **Visual Management**: Easy-to-use GUI for managing all MCP servers
- 🔐 **Secure & Reliable**: Centralized API key and authentication management
- 🚀 **One-Click Install**: Rich selection of servers in MCP Marketplace
- 📊 **Usage Statistics**: Real-time service call monitoring

Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)** now to start your MCP journey!


---

## Introduction

This is an MCP server for accessing the Idealista7 API, providing real estate search functionality for Spain, Portugal, and Italy.

- **PyPI Package**: `bach-idealista7`
- **Version**: 2.0.0
- **Transport Protocol**: stdio


## Installation

### Install from PyPI:

```bash
pip install bach-idealista7
```

### Install from source:

```bash
pip install -e .
```

## Running

### Method 1: Using uvx (Recommended, no installation needed)

```bash
# Set environment variable
export API_KEY="your_api_key_here"

# Run (uvx will automatically install and run)
uvx --from bach-idealista7 bach_idealista7
```

### Method 2: Run after installation

```bash
# Install
pip install bach-idealista7

# Set environment variable
export API_KEY="your_api_key_here"

# Run (command uses underscore)
bach_idealista7
```

## Configuration

### API Authentication

This API requires RapidAPI key authentication. Get your API key from [RapidAPI](https://rapidapi.com/scraperium/api/idealista7) and set the environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | RapidAPI Key | Yes |




### Using with Cursor

Edit Cursor MCP config file `~/.cursor/mcp.json`:

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

### Using with Claude Desktop

Edit Claude Desktop config file `claude_desktop_config.json`:

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


## Available Tools

This server provides 15 tools:


### `list_home_properties`

Search home/apartment listings. Supports buy/rent, filter by price, size, bedrooms, amenities and more.

**Endpoint**: `GET /listhomes`

**Main Parameters**:

- `order` (string) *Required*: Sort order: relevance|lowestprice|highestprice|mostrecent etc.
- `operation` (string) *Required*: Operation type: sale|rent
- `locationId` (string) *Required*: Location ID, e.g.: 0-EU-ES-28-07-001-079
- `locationName` (string) *Required*: Location name, e.g.: Madrid
- `location` (string) *Required*: Country code: es|pt|it
- `locale` (string) *Required*: Language: es|it|pt|en|ca|de|fr|nl|nb

---


### `list_storage_rooms`

Search storage room listings.

**Endpoint**: `GET /liststoragerooms`

---


### `list_buildings`

Search building listings.

**Endpoint**: `GET /listbuildings`

---


### `list_lands`

Search land listings. Supports urban, building, non-building land filters.

**Endpoint**: `GET /listlands`

---


### `property_details`

Get property details.

**Endpoint**: `GET /propertydetails`

**Parameters**:

- `propertyId` (string) *Required*: Property ID
- `location` (string) *Required*: Country code: es|pt|it
- `language` (string) *Required*: Language: en, es, it, pt, ca, de, fr, nl, nb

---


### `list_garages`

Search garage/parking listings.

**Endpoint**: `GET /listgarages`

---


### `get_sublocations`

Get sublocations within a location.

**Endpoint**: `GET /getlocations`

---


### `get_microsite_profile`

Get real estate agent profile information.

**Endpoint**: `GET /getmicrositeprofile`

---


### `get_microsite_locations`

Get locations where the agent has properties.

**Endpoint**: `GET /getmicrositelocations`

---


### `list_commercial_properties`

Search commercial property listings. Includes shops, industrial buildings, warehouses, etc.

**Endpoint**: `GET /listcommercialproperties`

---


### `list_offices`

Search office listings.

**Endpoint**: `GET /listoffices`

---


### `list_rooms`

Search room rental listings. Supports flatshare-related filters.

**Endpoint**: `GET /listrooms`

---


### `list_new_homes`

Search new home listings.

**Endpoint**: `GET /listnewhomes`

---


### `get_suggestions`

Get location search suggestions (autocomplete).

**Endpoint**: `GET /getsuggestions`

---



## Supported Countries/Regions

- 🇪🇸 Spain (es)
- 🇵🇹 Portugal (pt)
- 🇮🇹 Italy (it)


## Tech Stack

- **Transport Protocol**: stdio
- **HTTP Client**: httpx

## License

MIT License - See [LICENSE](./LICENSE) file for details.

## Development

This server is generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 2.0.0
