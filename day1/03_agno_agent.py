"""Day 1, step 3: the same agent in Agno. The loop you just wrote is now inside Agent."""

from agno.agent import Agent
from agno.tools import tool

from campus_buddy import MODEL
from campus_buddy.display import show_tools


@tool
def get_attendance(course: str) -> str:
    """Get the student's attendance in one course, e.g. Operating Systems."""  # The LLM reads this.
    attendance = {"Operating Systems": "31 of 42 classes", "Database Systems": "38 of 40 classes"}
    return attendance.get(course, "Course not found.")


agent = Agent(model=MODEL, tools=[get_attendance])

run = agent.run("Do I meet the 75% attendance rule in Operating Systems and Database Systems?")
show_tools(run)
print(f"\nFinal answer: {run.content}")
