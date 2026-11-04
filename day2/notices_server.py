"""Day 2, step 3: our own MCP server. It knows nothing about agents or LLMs.

Any MCP client can use it, including Claude Code, Cursor and VS Code, not just our agent.
Normally a client starts this for you. You won't run it directly.
"""

import json
import os

from mcp.server.mcpserver import MCPServer

from campus_buddy import DATA_DIR

server = MCPServer("campus-notices")


def load_notices() -> list[dict]:
    path = os.getenv("NOTICES_FILE", str(DATA_DIR / "notices.json"))
    with open(path) as f:
        return json.load(f)


@server.tool()
def list_notices() -> str:
    """List the campus notice board, with the id and title of each notice."""
    return "\n".join(f"{n['id']}: {n['title']}" for n in load_notices())


@server.tool()
def read_notice(notice_id: int) -> str:
    """Read the full text of one campus notice by its id."""
    for notice in load_notices():
        if notice["id"] == notice_id:
            return notice["body"]
    return f"No notice with id {notice_id}."


if __name__ == "__main__":
    server.run()
