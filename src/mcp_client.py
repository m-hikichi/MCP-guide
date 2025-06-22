import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession


async def main():
    # mcp_server.py をPythonで実行
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],
    )

    # サーバ接続のためのクライアントストリームを確立
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # 初期化処理
            await session.initialize()

            # "hello_world" ツールの呼び出し
            result = await session.call_tool("add", {"a": 2, "b": 3})
            print("Tool result: ", result.content)


if __name__ == "__main__":
    asyncio.run(main())
