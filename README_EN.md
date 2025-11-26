# Idealista7 MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

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

This is an automatically generated MCP server using [FastMCP](https://fastmcp.wiki) for accessing the Idealista7 API.

- **PyPI Package**: `bach-idealista7`
- **Version**: 1.0.0
- **Transport Protocol**: stdio


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
# 运行（uvx 会自动安装并运行）
uvx --from bach-idealista7 bach_idealista7

# 或指定版本
uvx --from bach-idealista7@latest bach_idealista7
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-idealista7

# 运行（命令名使用下划线）
bach_idealista7
```

## Configuration

### API Authentication

This API requires authentication. Please set environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | API Key | Yes |




### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "idealista7": {
      "command": "python",
      "args": ["E:\path\to\idealista7\server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Note**: Replace `E:\path\to\idealista7\server.py` with the actual server file path.


## 可用工具

此服务器提供以下工具:


### `list_home_properties`

List home properties with the requested parameters. Buy/Rent \u003e Homes. Filters are optional parameters, please make sure the request follows the rules in each parameter.  Boolean parameters should be true always if you want to use them. To make them false, don't include them in the requests (leave blank).

**端点**: `GET /listhomes`


**参数**:

- `order` (string) *必需*: Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors Default is relevance.

- `operation` (string) *必需*: Search sales or rentals. Pick between: sale|rent

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `maxItems` (string) *必需*: Number of items to return. Set 0 to return the item's count, fast response. Max Value is 40, anything above will be ignored.

- `location` (string) *必需*: One of the following values: es|pt|it

- `locale` (string) *必需*: The language of the ads. Pick between: es|it|pt|en|ca|de|fr|nl|nb

- `micrositeShortName` (string): Get ads from a specific real estate. For example if the URL from the real estate is: https://www.idealista.com/pro/cajal-gestion-inmobiliaria/ The parameter micrositeShortName should be cajal-gestion-inmobiliaria

- `minPrice` (string): Minimum price to search.

- `maxPrice` (string): Maximum price to search.

- `minSize` (string): Minimum size to search in m2.

- `maxSize` (string): Maximum size to search in m2.

- `flat` (string): Example value: 

- `onlyFlats` (string): Example value: 

- `penthouse` (string): Example value: 

- `duplex` (string): Example value: 

- `chalet` (string): Example value: 

- `independantHouse` (string): Example value: 

- `semidetachedHouse` (string): Example value: 

- `terracedHouse` (string): Example value: 

- `countryHouse` (string): Example value: 

- `apartamentoType` (string): Example value: 

- `villaType` (string): Example value: 

- `loftType` (string): Example value: 

- `cortijoType` (string): Example value: 

- `atticStudioType` (string): Example value: 

- `casaBajaType` (string): Example value: 

- `bedrooms0` (string): Example value: 

- `bedrooms1` (string): Example value: 

- `bedrooms2` (string): Example value: 

- `bedrooms3` (string): Example value: 

- `bedrooms4` (string): Example value: 

- `bathrooms1` (string): Example value: 

- `bathrooms2` (string): Example value: 

- `bathroom3` (string): Example value: 

- `newDevelopment` (string): Example value: 

- `good` (string): Example value: 

- `renew` (string): Example value: 

- `furnished` (string): Furnishings parameter. ONLY valid when operation=rent. Pick between. Indifferent: leave blank (default) | Furnished: furnished | Only furnished kitchens: furnishedKitchen

- `petsAllowed` (string): Example value: 

- `airConditioning` (string): Example value: 

- `builtinWardrobes` (string): Example value: 

- `elevator` (string): Example value: 

- `exterior` (string): Example value: 

- `garage` (string): Example value: 

- `garden` (string): Example value: 

- `swimmingPool` (string): Example value: 

- `terrance` (string): Example value: 

- `storeRoom` (string): Example value: 

- `accessible` (string): Example value: 

- `luxury` (string): Example value: 

- `hasPlan` (string): Example value: 

- `virtualTour` (string): Example value: 

- `bankOffer` (string): Example value: 

- `topFloor` (string): Example value: 

- `intermediateFloor` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M

- `longTermResidential` (string): Example value: 

- `shortTerm` (string): Example value: 

- `isBareOwnership` (string): Example value: 

- `isTenanted` (string): Example value: 

- `isIllegallyOccupied` (string): Example value: 

- `isFree` (string): Example value: 



---


### `list_storage_rooms`

List Storage Rooms

**端点**: `GET /liststoragerooms`


**参数**:

- `order` (string) *必需*: Example value: 

- `operation` (string) *必需*: Example value: 

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `maxItems` (string) *必需*: Example value: 

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `micrositeShortName` (string): Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `minSize` (string): Example value: 

- `maxSize` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `list_buildings`

List Buildings

**端点**: `GET /listbuildings`


**参数**:

- `order` (string) *必需*: Example value: 

- `operation` (string) *必需*: Example value: 

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `maxItems` (string) *必需*: Example value: 

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `micrositeShortName` (string): Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `minSize` (string): Example value: 

- `maxSize` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `list_lands`

List Lands

**端点**: `GET /listlands`


**参数**:

- `order` (string) *必需*: Example value: 

- `operation` (string) *必需*: Example value: 

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `maxItems` (string) *必需*: Example value: 

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `micrositeShortName` (string): Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `minSize` (string): Example value: 

- `maxSize` (string): Example value: 

- `urban` (string): Example value: 

- `buildingLand` (string): Example value: 

- `nonBuildingLand` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `property_details`

Get more details about a property.

**端点**: `GET /propertydetails`


**参数**:

- `propertyId` (string) *必需*: Property Id.

- `location` (string) *必需*: One of the following values: es|pt|it

- `language` (string) *必需*: The language of the ad. Pick between: en, es, it, pt, ca, de, fr, nl, nb



---


### `list_garages`

List garages

**端点**: `GET /listgarages`


**参数**:

- `order` (string) *必需*: Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors Default is relevance.

- `operation` (string) *必需*: Example value: 

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `maxItems` (string) *必需*: Example value: 

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `micrositeShortName` (string): Get ads from a specific real estate. For example if the URL from the real estate is: https://www.idealista.com/pro/cajal-gestion-inmobiliaria/ The parameter micrositeShortName should be cajal-gestion-inmobiliaria

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `minSize` (string): Example value: 

- `maxSize` (string): Example value: 

- `motorcycleParking` (string): Example value: 

- `automaticDoor` (string): Example value: 

- `security` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `get_sublocations`

Get sublocations inside another location.

**端点**: `GET /getlocations`


**参数**:

- `locationId` (string) *必需*: Location Id that has the flag divisible=true.

- `location` (string) *必需*: One of the following values: es|pt|it

- `propertyType` (string) *必需*: Changes the 'total' field which indicates the number of properties of this type. Note: bedrooms only works with rent operation.

- `operation` (string) *必需*: Changes the 'total' field which indicates the number of properties with this operation.



---


### `get_microsite_profile`

Get Microsite profile information

**端点**: `GET /getmicrositeprofile`


**参数**:

- `micrositeShortName` (string) *必需*: Microsite ShortName is the identifier of every real estate profile. You may find it in the URL: idealista.com/pro/sierra-blanca-estates-realty/

- `location` (string) *必需*: Example value: 



---


### `get_microsite_locations`

Get the locations where the microsite/profile has properties.

**端点**: `GET /getmicrositelocations`


**参数**:

- `micrositeShortName` (string) *必需*: Example value: sumainmobiliaria

- `location` (string) *必需*: One of the following values: es|pt|it

- `locale` (string) *必需*: Language: es|it|pt|en|ca|de|fr|nl|nb

- `operation` (string) *必需*: Example value: sale

- `locationId` (string) *必需*: Example value: 0-EU-ES-28



---


### `list_commercial_properties`

List Commercial Properties.

**端点**: `GET /listcommercialproperties`


**参数**:

- `order` (string) *必需*: Example value: 

- `operation` (string) *必需*: Example value: 

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `maxItems` (string) *必需*: Example value: 

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `minSize` (string): Example value: 

- `maxSize` (string): Example value: 

- `premises` (string): Example value: 

- `industrialBuilding` (string): Example value: 

- `saleWarehouseOnly` (string): Example value: 

- `saleWarehouseWithBusinessTransfer` (string): Example value: 

- `saleWarehouseThirdPartiesRented` (string): Example value: 

- `accommodation` (string): Example value: 

- `barsAndNightclub` (string): Example value: 

- `catering` (string): Example value: 

- `foodTrade` (string): Example value: 

- `tobaccoShop` (string): Example value: 

- `pharmacy` (string): Example value: 

- `newsstand` (string): Example value: 

- `retail` (string): Example value: 

- `educationalCenter` (string): Example value: 

- `aestheticAndBeauty` (string): Example value: 

- `sportsFacilities` (string): Example value: 

- `professionalServices` (string): Example value: 

- `laboratory` (string): Example value: 

- `storehouse` (string): Example value: 

- `otherCommercialActivities` (string): Example value: 

- `shoppingcenter` (string): Example value: 

- `street` (string): Example value: 

- `mezzanine` (string): Example value: 

- `underground` (string): Example value: 

- `ontopfloor` (string): Example value: 

- `otherLocations` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `list_offices`

List office properties with the requested parameters. Buy/Rent \u003e Offices. Filters are optional parameters, please make sure the request follows the rules in each parameter.

**端点**: `GET /listoffices`


**参数**:

- `order` (string) *必需*: Example value: 

- `operation` (string) *必需*: Search sales or rentals. Pick between: sale|rent

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `maxItems` (string) *必需*: Example value: 

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `minSize` (string): Example value: 

- `maxSize` (string): Example value: 

- `layout` (string): Distribution parameter. Pick between: Indifferent: leave blank (default) Open plan: openPlan Divided by walls: withWalls

- `buildingType` (string): Type of building parameter. Pick between: Indifferent: leave blank (default) Exclusively for offices: exclusive Mixted use: mixed

- `hotWater` (string): Example value: 

- `airConditioning` (string): Example value: 

- `elevator` (string): Example value: 

- `heating` (string): Example value: 

- `accessible` (string): Example value: 

- `exterior` (string): Example value: 

- `garage` (string): Example value: 

- `security` (string): Example value: 

- `hasPlan` (string): Example value: 

- `bankOffer` (string): Bank-owned

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 24h: T (Rent operation only) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `list_rooms`

List renting rooms with the requested parameters. Buy, Rent \u003e Rooms or Share \u003e Homes.

**端点**: `GET /listrooms`


**参数**:

- `order` (string) *必需*: Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors Default is relevance.

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `maxItems` (string) *必需*: Example value: 

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `newGender` (string): 'You are' parameter (your gender). Pick between: male|female

- `smokingPolicy` (string): Pick between: Indiferent: leave blank (default) | Smoking allowed: allowed | Smoking is not allowed: disallowed

- `petsPolicy` (string): Pets. Pick between: Indifferent: leave blank (default) Pets allowed: allowed Pets not allowed: disallowed

- `availableFrom` (string): Date the room is available. Pick between: Any date: leave blank (default) Available now: now +1 month since now: 1m +2 months since now: 2m +3 months since now: 3m +4 months since now: 4m +5 months since now: 5m

- `housemates1` (string): Example value: 

- `housemates2` (string): Example value: 

- `housemates3` (string): Example value: 

- `couplesAllowed` (string): Example value: 

- `childrenAllowed` (string): Example value: 

- `streetViewWindow` (string): Example value: 

- `privateToilet` (string): Example value: 

- `airConditioning` (string): Example value: 

- `elevator` (string): Example value: 

- `terrace` (string): Example value: 

- `exterior` (string): Example value: 

- `accessible` (string): Example value: 

- `hasHouseKeeper` (string): Example value: 

- `garden` (string): Example value: 

- `swimmingPool` (string): Example value: 

- `topFloor` (string): Example value: 

- `intermediateFloor` (string): Example value: 

- `groundFloor` (string): Example value: 

- `occupation` (string): Flat sharing with... Pick one of these: Indifferent: leave blank (default) With workers: workers With students: students

- `gayPartners` (string): Example value: 

- `ownerNotLiving` (string): Example value: 

- `privateOwner` (string): Example value: 

- `sinceDate` (string): Publication Date Parameter. One of the following values. Indifferent: leave blank (by default) | Last 48h: Y (Buy operation only) | Last week: W | Last month: M



---


### `list_new_homes`

List new home properties with the requested parameters. Buy/Rent \u003e New home. Filters are optional parameters, please make sure the request follows the rules in each parameter.

**端点**: `GET /listnewhomes`


**参数**:

- `order` (string) *必需*: Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors Default is relevance.

- `operation` (string) *必需*: Search sales or rentals. Pick between: sale|rent

- `locationId` (string) *必需*: Example value: 0-EU-ES-28-07-001-079

- `maxItems` (string) *必需*: Example value: 40

- `locationName` (string) *必需*: Example value: Madrid

- `numPage` (string) *必需*: Example value: 1

- `location` (string) *必需*: Example value: 

- `locale` (string) *必需*: Example value: 

- `minPrice` (string): Example value: 

- `maxPrice` (string): Example value: 

- `housesOrChalets` (string): Example value: 

- `flats` (string): Example value: 

- `bedrooms0` (string): Example value: 

- `bedrooms1` (string): Example value: 

- `bedrooms2` (string): Example value: 

- `bedrooms3` (string): Example value: 

- `bedrooms4` (string): Example value: 

- `rentToOwn` (string): Example value: 

- `finished` (string): Example value: 

- `stateSubsidized` (string): Example value: 

- `bankOffer` (string): Example value: 



---


### `get_suggestions`

Get location suggestions (autocomplete)

**端点**: `GET /getsuggestions`


**参数**:

- `prefix` (string) *必需*: Example value: madrid

- `location` (string) *必需*: One of the following values: es|pt|it

- `propertyType` (string) *必需*: Changes the 'total' field which indicates the number of properties of this type. Note: bedrooms only works with rent operation.

- `operation` (string) *必需*: Changes the 'total' field which indicates the number of properties with this operation.



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

This server is automatically generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 1.0.0
