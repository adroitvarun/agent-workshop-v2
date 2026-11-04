"""One possible Day 3 solution: an agent using a group project skill."""

from agno.agent import Agent
from agno.skills import LocalSkills, Skills

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import show_tools

QUESTION = "Three of us have a DBMS project due in 10 days. How should we split the work?"

agent = Agent(
    name="Project Buddy",
    model=MODEL,
    skills=Skills(loaders=[LocalSkills(str(REPO_ROOT / "solutions" / "day3" / "skills"))]),
    instructions="You help students run group projects smoothly. Be practical and brief.",
)

run = agent.run(QUESTION)
show_tools(run)
print(f"\n{run.content}")
