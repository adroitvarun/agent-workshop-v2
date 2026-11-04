"""Day 3, step 1: a skill is know-how written in a file. No Python in the SKILL.md.

Watch the [tool] lines. Buddy always sees each skill's name and description, but it
loads the full instructions only when it needs them. That keeps every request cheaper.
"""

from agno.agent import Agent
from agno.skills import LocalSkills, Skills

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import show_tools
from campus_buddy.tools import calculate_cgpa, get_timetable

buddy = Agent(
    name="Campus Buddy",
    model=MODEL,
    tools=[calculate_cgpa, get_timetable],
    skills=Skills(loaders=[LocalSkills(str(REPO_ROOT / "day3" / "skills"))]),
    instructions="You help college students. Be brief and friendly.",
)

for question in [
    "What's my CGPA? I got 9 and 8 in courses of 4 and 3 credits.",  # No skill needed.
    "My Data Structures exam is in 4 days. Make me a study plan.",   # Needs the skill.
]:
    print(f"\n=== {question}")
    run = buddy.run(question)
    show_tools(run)
    print(f"\n{run.content}")
