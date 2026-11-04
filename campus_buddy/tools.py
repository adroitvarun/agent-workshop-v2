"""The tools we write on Day 1, kept here so later days can import them."""

import json

from agno.tools import tool

from campus_buddy import DATA_DIR


@tool
def calculate_cgpa(grade_points: list[float], credits: list[float]) -> str:
    """Calculate a student's CGPA. Use this for any CGPA or GPA question.

    Args:
        grade_points: The grade point earned in each course, e.g. [9, 8, 10].
        credits: The credits of each course, in the same order, e.g. [4, 3, 2].
    """
    if len(grade_points) != len(credits):
        return "Error: grade_points and credits must be the same length."
    if sum(credits) == 0:
        return "Error: total credits cannot be zero."
    earned = sum(g * c for g, c in zip(grade_points, credits))
    return f"CGPA: {earned / sum(credits):.2f}"


@tool
def get_timetable(day: str) -> str:
    """Get the class timetable for one day of the week, e.g. "Monday"."""
    timetable = json.loads((DATA_DIR / "timetable.json").read_text())
    classes = timetable.get(day.strip().capitalize())
    if classes is None:
        return f"No timetable found for {day}."
    return json.dumps(classes) if classes else f"No classes on {day}."
