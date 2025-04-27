from mcp.server.fastmcp import FastMCP

# MCPサーバーインスタンスの作成
mcp = FastMCP("demo")


# MCPツールとして hello_world 関数を登録
@mcp.tool()
def hello_world(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
