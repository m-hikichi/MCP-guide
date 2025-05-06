from mcp.server.fastmcp import FastMCP

# MCPサーバーインスタンスの作成
mcp = FastMCP("demo")


# MCPツールとして hello_world 関数を登録
@mcp.tool()
def hello_world(name: str) -> str:
    return f"Hello, {name}!"


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    2つの値を受け取り、その和を返す関数。
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    2つの値を受け取り、その積を返す関数。
    """
    return a * b


if __name__ == "__main__":
    mcp.run()
