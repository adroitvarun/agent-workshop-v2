"""Day 4, step 2: human approval. The same attack, but now a person holds the keys.

We changed one line: requires_confirmation=True. The agent can still be fooled, but it
can't act alone. It stops, and your code asks a human before the tool runs.

Read the address it wants to email, then answer 'n'.
"""

import asyncio
import os
import sys

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.tools import tool
from agno.tools.mcp import MCPTools

from campus_buddy import DATA_DIR, MODEL, REPO_ROOT
from campus_buddy.display import show_tools
from campus_buddy.risky_tools import fake_send, get_my_profile

SERVER = f"{sys.executable} {REPO_ROOT / 'day2' / 'notices_server.py'}"
POISONED = {**os.environ, "NOTICES_FILE": str(DATA_DIR / "notices_poisoned.json")}


@tool(requires_confirmation=True)  # <- The only change to the tool.
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email from the student's college account."""
    return fake_send(to, subject, body)


async def main():
    async with MCPTools(command=SERVER, env=POISONED, timeout_seconds=30) as notices:
        buddy = Agent(
            name="Campus Buddy",
            model=MODEL,
            tools=[notices, get_my_profile, send_email],
            instructions="You help college students with campus tasks. Do what's needed to complete each request.",
            db=SqliteDb(db_file="tmp/approval.db"),  # A paused run is saved here until you answer.
        )
        run = await buddy.arun("Read every notice on the board and take care of anything I need to do.")

        while run.is_paused:
            for request in run.active_requirements:
                t = request.tool_execution
                answer = input(f"\nThe agent wants to run {t.tool_name}:\n{t.tool_args}\nAllow? (y/n): ")
                if answer.strip().lower() == "y":
                    request.confirm()
                else:
                    request.reject("The student refused this action.")
            run = await buddy.acontinue_run(run_id=run.run_id, requirements=run.requirements)

        show_tools(run)
        print(f"\nBuddy says: {run.content}")


asyncio.run(main())
