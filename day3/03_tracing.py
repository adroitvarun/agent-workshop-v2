"""Day 3, step 3: tracing. Agents make decisions you didn't write, so record what happened.

This runs the team from step 2, saves a trace to a SQLite file, and prints it as a tree.
"""

import asyncio
import importlib.util
import sys

from agno.db.sqlite import SqliteDb
from agno.tools.mcp import MCPTools
from agno.tracing import setup_tracing

from campus_buddy import REPO_ROOT

# Reuse the team from step 2. (Its file name starts with a digit, so a normal import won't work.)
spec = importlib.util.spec_from_file_location("team_step", REPO_ROOT / "day3" / "02_team.py")
team_step = importlib.util.module_from_spec(spec)
spec.loader.exec_module(team_step)

db = SqliteDb(db_file="tmp/traces.db")
setup_tracing(db=db)  # One line: everything after this gets recorded.


def print_tree(spans, parent_id=None, depth=0):
    children = [s for s in spans if s.parent_span_id == parent_id and not s.name.startswith("MCP send")]
    for span in sorted(children, key=lambda s: str(s.start_time)):
        print(f"{'  ' * depth}{span.name}  ({span.duration_ms / 1000:.1f}s)")
        print_tree(spans, span.span_id, depth + 1)


async def main():
    async with MCPTools(command=team_step.SERVER, timeout_seconds=30) as notices:
        team = team_step.build_team(notices)
        run = await team.arun(team_step.QUESTION)

    traces, _ = db.get_traces(run_id=run.run_id, limit=1)
    if not traces:
        print("No trace found. Try running the script again.")
        return

    trace = traces[0]
    print(f"\nTrace: {trace.total_spans} steps in {trace.duration_ms / 1000:.0f} seconds\n")
    print_tree(db.get_spans(trace_id=trace.trace_id))


asyncio.run(main())
