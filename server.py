"""
Idealista7 MCP Server

MCP server for accessing Idealista7 API - Search real estate in Spain, Portugal and Italy

Version: 1.0.0
Transport: stdio
"""
import os
import sys
import json
import httpx
from pathlib import Path
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "2.0.3"
__tag__ = "idealista7/2.0.3"

def _log(msg):
    """输出到 stderr，避免干扰 MCP 的 stdio 通信"""
    print(msg, file=sys.stderr)

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# 从文件加载 OpenAPI 规范
def load_openapi_spec():
    """从 openapi.json 文件加载 OpenAPI 规范"""
    # 尝试多个可能的位置
    possible_paths = [
        Path(__file__).parent / "openapi.json",  # 同目录
        Path(__file__).parent.parent / "openapi.json",  # 上级目录
        Path(__file__).resolve().parent / "openapi.json",  # 绝对路径同目录
    ]
    
    for openapi_path in possible_paths:
        if openapi_path.exists():
            with open(openapi_path, "r", encoding="utf-8") as f:
                return json.load(f)
    
    # 尝试使用 importlib.resources (Python 3.9+)
    try:
        import importlib.resources as pkg_resources
        # 尝试从包中读取
        try:
            files = pkg_resources.files(__package__ or __name__.rsplit('.', 1)[0] if '.' in __name__ else '')
            openapi_file = files.joinpath("openapi.json")
            if hasattr(openapi_file, 'read_text'):
                return json.loads(openapi_file.read_text(encoding='utf-8'))
        except (TypeError, FileNotFoundError, AttributeError):
            pass
    except ImportError:
        pass
    
    # 如果都找不到，抛出详细错误
    raise FileNotFoundError(
        f"无法找到 openapi.json 文件。已尝试的路径: {[str(p) for p in possible_paths]}"
    )


# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "idealista7.p.rapidapi.com"
else:
    _log("⚠️  警告: 未设置 API_KEY 环境变量")
    _log("   RapidAPI 需要 API Key 才能正常工作")
    _log("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://idealista7.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = load_openapi_spec()
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="idealista7",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "idealista7.p.rapidapi.com"
    else:
        _log("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    _log(f"🚀 启动 Idealista7 MCP 服务器")
    _log(f"📦 版本: {__tag__}")
    _log(f"🔧 传输协议: {TRANSPORT}")
    
    # 运行服务器
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()
