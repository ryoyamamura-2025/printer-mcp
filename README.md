# printer-mcp

Windows にインストールされているプリンター一覧を取得する MCP サーバーです。

## セットアップ

Python 3.13 以上と [uv](https://docs.astral.sh/uv/) を用意してください。

```powershell
uv sync
```

## 起動

```powershell
uv run python server.py
```

サーバーは `http://localhost:8000` で起動します。

## 提供するツール

- `list_printers`: プリンター名、ドライバー名、ポート名、状態の一覧を取得します。

Windows の PowerShell コマンド `Get-Printer` を使用するため、Windows 環境で実行してください。
