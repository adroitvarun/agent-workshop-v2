"""One possible Day 2 solution: the attendance coach connected to its MCP server."""

import asyncio
import sys

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.tools.mcp import MCPTools

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import achat

SERVER = f"{sys.executable} {REPO_ROOT / 'solutions' / 'day2' / 'my_server.py'}"


async def main():
    async with MCPTools(command=SERVER, timeout_seconds=30) as my_tools:
        print(f"Tools from your server: {list(my_tools.functions)}")
        agent = Agent(
            name="Attendance Coach",
            model=MODEL,
            tools=[my_tools],
            instructions="You help students stay above their attendance requirement. Be honest and encouraging.",
            db=SqliteDb(db_file="tmp/my_agent.db"),
            session_id="solution-chat",
            add_history_to_context=True,
            num_history_runs=5,
        )
        await achat(agent)


asyncio.run(main())
