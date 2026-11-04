"""Day 3 checkpoint: Buddy with memory, tools, MCP and a skill. All in one agent.

Try: "Make me a study plan for my next exam."
"""

import asyncio
import sys

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.skills import LocalSkills, Skills
from agno.tools.mcp import MCPTools

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import achat
from campus_buddy.tools import calculate_cgpa, get_timetable

SERVER = f"{sys.executable} {REPO_ROOT / 'day2' / 'notices_server.py'}"


async def main():
    async with MCPTools(command=SERVER, timeout_seconds=30) as notices:
        buddy = Agent(
            name="Campus Buddy",
            model=MODEL,
            tools=[calculate_cgpa, get_timetable, notices],
            skills=Skills(loaders=[LocalSkills(str(REPO_ROOT / "day3" / "skills"))]),
            instructions="You help college students. Be brief and friendly. Check the notice board for dates and news.",
            db=SqliteDb(db_file="tmp/buddy.db"),
            session_id="my-chat",
            add_history_to_context=True,
            num_history_runs=5,
            add_datetime_to_context=True,
        )
        print("Type 'quit' to stop.")
        await achat(buddy)


asyncio.run(main())
