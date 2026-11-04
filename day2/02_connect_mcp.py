"""Day 2, step 2: connect to someone else's MCP server. We wrote none of its tools.

This one is hosted by Agno and searches their documentation.
"""

import asyncio

from agno.agent import Agent
from agno.tools.mcp import MCPTools

from campus_buddy import MODEL
from campus_buddy.display import show_tools


async def main():
    async with MCPTools(url="https://docs.agno.com/mcp", timeout_seconds=30) as docs:
        print(f"This server gave us these tools: {list(docs.functions)}\n")

        agent = Agent(
            model=MODEL,
            tools=[docs],
            instructions="Answer using the docs tools. Be brief, at most 4 sentences.",
        )
        run = await agent.arun("In Agno, how do I make a tool ask for confirmation before it runs?")
        show_tools(run)
        print(f"\n{run.content}")


asyncio.run(main())
