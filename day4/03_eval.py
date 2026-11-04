"""Day 4, step 3: evals. Tests for agents. The same question can get different answers.

Two checks: did it use the right tool, and was the answer right?
An eval only covers the cases you wrote, so add a new one whenever your agent gets something wrong.
"""

from agno.agent import Agent
from agno.eval.accuracy import AccuracyEval
from agno.eval.reliability import ReliabilityEval
from agno.models.utils import get_model

from campus_buddy import MODEL
from campus_buddy.tools import calculate_cgpa, get_timetable

QUESTION = "I got 9, 8 and 10 in courses of 4, 3 and 2 credits. What's my CGPA?"

buddy = Agent(
    model=MODEL,
    tools=[calculate_cgpa, get_timetable],
    instructions="You help college students. Always use a tool for numbers.",
)

# Check 1: did it call the tool, instead of doing the maths in its head?
run = buddy.run(QUESTION)
reliability = ReliabilityEval(agent_response=run, expected_tool_calls=["calculate_cgpa"]).run(print_results=True)

# Check 2: is the answer right? A second LLM marks it, because the wording varies.
accuracy = AccuracyEval(
    agent=buddy,
    input=QUESTION,
    expected_output="The CGPA is 8.89",
    model=get_model(MODEL),  # Without this it uses a pricier default model.
    num_iterations=1,
).run(print_results=True)

passed = reliability is not None and reliability.eval_status == "PASSED" and accuracy is not None and accuracy.avg_score >= 8
print(f"\nOverall: {'PASS' if passed else 'FAIL'}")
