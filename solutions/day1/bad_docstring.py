"""Homework solution: same code, clear name and docstring. The LLM now knows when to use it."""

from agno.agent import Agent
from agno.tools import tool

from campus_buddy import MODEL
from campus_buddy.display import show_tools


@tool
def percentage(part: float, whole: float) -> str:
    """Calculate what percentage `part` is of `whole`, e.g. attendance from classes attended and held.

    Args:
        part: The smaller amount, e.g. classes attended.
        whole: The total amount, e.g. classes held.
    """
    return f"{part / whole * 100:.1f}%"


agent = Agent(model=MODEL, tools=[percentage])

run = agent.run("I attended 31 of 42 classes. What's my attendance percentage? Do I meet the 75% rule?")
show_tools(run)
print(f"\n{run.content}")
