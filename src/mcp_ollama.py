import asyncio
import json

from langchain_core.messages import SystemMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


def load_mcp_config(path: str) -> dict[str, any]:
    """
    指定されたJSONファイルからMCPサーバー設定を読み込む

    Args:
        path (str): 設定ファイルのパス

    Returns:
        dict[str, any]: MCPサーバーの設定情報
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file).get("mcpServers", {})


async def run_agent_query():
    # LLM (ollama) の初期化
    llm = ChatOllama(
        base_url="http://ollama:11434",
        model="EZO-Qwen2.5:32b-instruct-q4_K_M",
        temperature=0,
    )

    # MCPサーバの設定読み込み
    config = load_mcp_config("mcp_config.json")

    # MCPクライアントとReActエージェントのセットアップ
    client = MultiServerMCPClient(config)
    tools = await client.get_tools()

    system_prompt = SystemMessage(
        "あなたはMCPサーバーを使用するAIアシスタントです。"
        "Toolの結果を優先して回答として採用してください"
        "回答は日本語でお願いします。"
    )
    agent = create_react_agent(llm, tools, prompt=system_prompt)

    # エージェントにクエリを送信し、結果を出力
    result = await agent.ainvoke({"messages": "(123 + 531) * 987は?"})

    for message in result["messages"]:
        print(f"\n--- {type(message).__name__} ---")
        print(message)


if __name__ == "__main__":
    asyncio.run(run_agent_query())
