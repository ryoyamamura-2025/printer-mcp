import json
import subprocess
from mcp.server.mcpserver import MCPServer

async def log_mcp_request(ctx, call_next):
    print(f"\n[MCP] method = {ctx.method}")
    print(f"[MCP] params = {ctx.params}")

    result = await call_next(ctx)

    print(f"[MCP] result = {result}")
    
    return result


mcp = MCPServer(
    "printer-mcp",
    middleware=[log_mcp_request]
)

# @mcp.tool()
# def ping() -> str:
#     """Check whether the MCP server is reachable"""
#     return "pong"

@mcp.tool()
def list_printers() -> list[dict]:
    """List printers installed on this Windows PC."""

    command = """
    ConvertTo-Json -InputObject @(
        Get-Printer |
        Select-Object Name, DriverName, PortName, PrinterStatus
    ) -Compress
    """

    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        stateless_http=True,
        json_response=True
    )