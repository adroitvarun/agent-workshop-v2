"""OPTIONAL HOMEWORK: use a server you've never seen, with one line of connection code.

This one comes from the official MCP servers project, and uv downloads it for you.
Run it as it is, then find another server at https://registry.modelcontextprotocol.io
and swap it in. Read what a server does before running it: it runs on your machine.
"""

import asyncio

from agno.agent import Agent
from agno.tools.mcp import MCPTools

from campus_buddy import MODEL
from campus_buddy.display import show_tools


async def main():
    async with MCPTools(command="uvx mcp-server-time", timeout_seconds=60) as time_tools:
        print(f"Tools: {list(time_tools.functions)}\n")
        agent = Agent(model=MODEL, tools=[time_tools])
        run = await agent.arun("What time is it in Kolkata and in London right now?")
        show_tools(run)
        print(f"\n{run.content}")


asyncio.run(main())
