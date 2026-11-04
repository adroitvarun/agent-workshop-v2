"""IN-CLASS EXERCISE: teach your agent a skill. You only need to edit a Markdown file.

1. Fill in day3/exercises/my_skills/my-first-skill/SKILL.md.
2. Copy your agent's name and instructions into this file.
3. Change QUESTION to something that should trigger your skill, and run this file.
4. Look for get_skill_instructions in the [tool] lines. Not there? Improve the description.
"""

from agno.agent import Agent
from agno.skills import LocalSkills, Skills

from campus_buddy import MODEL, REPO_ROOT
from campus_buddy.display import show_tools

QUESTION = "TODO: a question that should use your skill"

agent = Agent(
    name="TODO: your agent's name",
    model=MODEL,
    skills=Skills(loaders=[LocalSkills(str(REPO_ROOT / "day3" / "exercises" / "my_skills"))]),
    instructions="TODO: your agent's instructions",
)

run = agent.run(QUESTION)
show_tools(run)
print(f"\n{run.content}")
