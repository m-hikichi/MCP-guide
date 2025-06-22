# 🔧 venv を使った MCP サーバと Cline の連携手順書

## ✅ 概要

この手順書では、GitHub 上の MCP サンプルプロジェクトを活用し、Python の仮想環境（venv）で MCP サーバを構築し、VS Code 拡張「Cline」と連携して利用する方法を説明します。MCP Inspector による動作確認も行います。

## 1. MCP プロジェクトの取得

### 📦 1.1 GitHub リポジトリをクローン

```bash
git clone https://github.com/m-hikichi/MCP-guide.git
cd MCP-guide
```

> ✅ `${PROJECT_DIR}` = `MCP-guide` のフルパス（例：`C:/Users/yourname/Documents/MCP-guide`）

## 2. Python 仮想環境の構築

### 🐍 2.1 仮想環境を作成

```bash
python -m venv venv
```

### 🔁 2.2 仮想環境を有効化

* **コマンドプロンプト**:

  ```bash
  .\venv\Scripts\activate.bat
  ```
* **PowerShell**:

  ```bash
  .\venv\Scripts\activate.ps1
  ```

## 3. 依存パッケージのインストール（requirements.txt を使用）

仮想環境を有効化したまま、クローンしたプロジェクトに含まれる `requirements.txt` を用いてインストールを実行します：

```bash
pip install -r requirements.txt
```

> ✅ `mcp[cli]` など必要なパッケージがすべて含まれています。

## 4. MCP サーバの起動と Inspector による動作確認

### 🧪 4.1 MCP Inspector の起動

以下のコマンドを実行して MCP Inspector を起動します：

```bash
mcp dev mcp_server.py
```

成功するとブラウザが自動的に開き、[MCP Inspector](http://localhost:6274) が表示されます。

* `Tools` タブで `add` 関数などをテストできます
* `Resources` タブではリソースアクセスの確認が可能です

## 5. Cline 拡張機能との連携

### ⚙️ 5.1 `cline_mcp_settings.json` の編集

VS Code でコマンドパレットを開き、
`> Cline: Configure MCP Servers` を実行し、以下の設定を追加します：

```json
{
  "mcpServers": {
    "local_mcp_server": {
      "command": "${PROJECT_DIR}/venv/Scripts/mcp.exe",
      "args": [
        "dev",
        "${PROJECT_DIR}/mcp_server.py"
      ]
    }
  }
}
```

> ✅ `${PROJECT_DIR}` は MCP-guide ディレクトリのフルパスに置き換えてください  
> ❌ パスに空白は不可  
> ✅ パスに日本語は使用可能  

## 6. Cline 上での使用

1. VS Code のチャットビューを開く
2. MCPサーバを `local_mcp_server` に切り替える
3. `add(a=2, b=3)` のようなツール呼び出しを行い、正しく動作するか確認します
