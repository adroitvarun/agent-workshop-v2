"""IN-CLASS EXERCISE, part 2: connect your agent to your server.

1. Fill in the TODOs in my_server.py.
2. Copy your agent's name and instructions from Day 1 into this file.
3. Run:  uv run python day2/exercises/my_agent_with_mcp.py
"""

import asyncio
import sys

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.tools.mcp import MCPTools

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import achat

SERVER = f"{sys.executable} {REPO_ROOT / 'day2' / 'exercises' / 'my_server.py'}"


async def main():
    async with MCPTools(command=SERVER, timeout_seconds=30) as my_tools:
        print(f"Tools from your server: {list(my_tools.functions)}")
        agent = Agent(
            name="TODO: your agent's name",
            model=MODEL,
            tools=[my_tools],
            instructions="TODO: your agent's instructions",
            db=SqliteDb(db_file="tmp/my_agent.db"),
            session_id="my-chat",
            add_history_to_context=True,
            num_history_runs=5,
        )
        await achat(agent)


asyncio.run(main())
