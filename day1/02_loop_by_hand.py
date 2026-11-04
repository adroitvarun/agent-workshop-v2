"""Day 1, step 2: an agent is a loop. Here it is with no framework at all."""

import json

from openai import OpenAI

from campus_buddy import OPENAI_MODEL_ID

client = OpenAI()


def get_attendance(course: str) -> str:
    attendance = {"Operating Systems": "31 of 42 classes", "Database Systems": "38 of 40 classes"}
    return attendance.get(course, "Course not found.")


# We describe the tool to the LLM. It never sees the code, only this.
tools = [{
    "type": "function",
    "name": "get_attendance",
    "description": "Get the student's attendance in one course, e.g. Operating Systems.",
    "parameters": {
        "type": "object",
        "properties": {"course": {"type": "string"}},
        "required": ["course"],
    },
}]

messages = [{"role": "user", "content": "Do I meet the 75% attendance rule in Operating Systems and Database Systems?"}]

while True:
    response = client.responses.create(model=OPENAI_MODEL_ID, input=messages, tools=tools)
    messages += response.output  # Keep everything the LLM said, so it has the full history.

    calls = [item for item in response.output if item.type == "function_call"]
    if not calls:  # No tool requested, so this is the final answer.
        print(f"Final answer: {response.output_text}")
        break

    for call in calls:  # The LLM asked. OUR code does the running.
        args = json.loads(call.arguments)
        result = get_attendance(**args)
        print(f"LLM asked for get_attendance({args}) -> we ran it -> {result}")
        messages.append({"type": "function_call_output", "call_id": call.call_id, "output": result})
