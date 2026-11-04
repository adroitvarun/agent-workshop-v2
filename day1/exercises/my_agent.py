"""IN-CLASS EXERCISE: start your own agent.

You'll add to this file on Days 2 and 3, so pick something you'd actually use.
Ideas: mess menu helper, placement prep coach, gym tracker, expense splitter.

1. Write one tool below. Keep it simple: a calculation or a small lookup.
2. Give it a docstring. The LLM only knows what the docstring tells it.
3. Fill in the instructions, then run:  uv run python day1/exercises/my_agent.py
"""

from agno.agent import Agent
from agno.tools import tool

from campus_buddy import MODEL
from campus_buddy.display import chat


@tool
def my_tool(text: str) -> str:
    """TODO: say what this tool does and when to use it."""
    return f"TODO: do something useful with {text}"


agent = Agent(
    name="TODO: name your agent",
    model=MODEL,
    tools=[my_tool],
    instructions="TODO: who is this agent, and how should it behave?",
)

if __name__ == "__main__":
    chat(agent)
