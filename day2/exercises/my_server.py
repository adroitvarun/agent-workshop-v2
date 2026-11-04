"""IN-CLASS EXERCISE, part 1: an MCP server for your agent.

Move a tool from your Day 1 agent into this server, or write a new one.
You don't run this file yourself. my_agent_with_mcp.py starts it for you.
"""

from mcp.server.mcpserver import MCPServer

server = MCPServer("my-server")


@server.tool()
def my_server_tool(text: str) -> str:
    """TODO: say what this tool does and when to use it."""
    return f"TODO: do something useful with {text}"


if __name__ == "__main__":
    server.run()
