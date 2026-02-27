"""
MCP服务器启动入口 - 支持stdio模式
"""
from server import mcp

if __name__ == "__main__":
    # FastMCP的mcp.run()会自动处理asyncio循环
    mcp.run()