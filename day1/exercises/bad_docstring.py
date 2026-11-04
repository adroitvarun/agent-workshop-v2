"""HOMEWORK (10 min): see why docstrings matter.

Run this as it is, and watch what the agent does with a useless description.
Then improve only the name and docstring, and run it again. Don't touch the code
inside the function. What changed, and why?
"""

from agno.agent import Agent
from agno.tools import tool

from campus_buddy import MODEL
from campus_buddy.display import show_tools


@tool
def do_thing(x: float, y: float) -> str:
    """Does the thing."""
    return f"{x / y * 100:.1f}%"


agent = Agent(model=MODEL, tools=[do_thing])

run = agent.run("I attended 31 of 42 classes. What's my attendance percentage? Do I meet the 75% rule?")
show_tools(run)
print(f"\n{run.content}")
