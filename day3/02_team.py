"""Day 3, step 2: a team. A leader passes work to specialists, and combines their results.

A team costs more and is harder to debug than one agent. Only split when each
member really needs different tools or instructions. Most tasks don't need this.
"""

import asyncio
import sys

from agno.agent import Agent
from agno.skills import LocalSkills, Skills
from agno.team import Team
from agno.tools.mcp import MCPTools

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.tools import get_timetable

SERVER = f"{sys.executable} {REPO_ROOT / 'day2' / 'notices_server.py'}"
QUESTION = "My Operating Systems exam is coming up. Find the date and my OS classes, then make a study plan."


def build_team(notices) -> Team:
    researcher = Agent(
        name="Researcher",
        role="Finds exam dates from the notice board and classes from the timetable.",
        model=MODEL,
        tools=[notices, get_timetable],
        instructions="Report only the facts you find. Don't make plans.",
    )
    planner = Agent(
        name="Planner",
        role="Writes study plans from facts the researcher found.",
        model=MODEL,
        skills=Skills(loaders=[LocalSkills(str(REPO_ROOT / "day3" / "skills"))]),
        instructions="Use the exam-prep-planner skill.",
    )
    return Team(
        name="Study Team",
        model=MODEL,
        members=[researcher, planner],
        instructions="First ask the Researcher for facts, then ask the Planner for the plan.",
    )


async def main():
    async with MCPTools(command=SERVER, timeout_seconds=30) as notices:
        team = build_team(notices)
        await team.aprint_response(QUESTION, stream=True)


if __name__ == "__main__":
    asyncio.run(main())
