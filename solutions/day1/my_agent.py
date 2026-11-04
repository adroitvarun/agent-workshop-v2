"""One possible Day 1 solution: an attendance coach."""

import math

from agno.agent import Agent
from agno.tools import tool

from campus_buddy import MODEL
from campus_buddy.display import chat


@tool
def classes_needed(attended: int, total: int, target_percent: float = 75) -> str:
    """Work out how many more classes in a row a student must attend to reach an attendance target.

    Args:
        attended: Classes attended so far.
        total: Classes held so far.
        target_percent: The attendance percentage to reach, usually 75.
    """
    if total <= 0:
        return "Error: total classes must be more than zero."
    if not 0 < target_percent < 100:
        return "Error: target_percent must be between 0 and 100."
    current = attended / total * 100
    if current >= target_percent:
        return f"Current attendance is {current:.1f}%. Target already met."
    needed = math.ceil((target_percent * total - 100 * attended) / (100 - target_percent))
    return f"Current attendance is {current:.1f}%. Attend the next {needed} classes in a row."


agent = Agent(
    name="Attendance Coach",
    model=MODEL,
    tools=[classes_needed],
    instructions="You help students stay above their attendance requirement. Be honest and encouraging.",
)

if __name__ == "__main__":
    chat(agent)
