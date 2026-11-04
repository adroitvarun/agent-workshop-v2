"""Day 1, step 1: an LLM is just an API call. Let's see what it can't do."""

from datetime import date

from openai import OpenAI

from campus_buddy import OPENAI_MODEL_ID

client = OpenAI()


def ask(question: str) -> None:
    response = client.responses.create(model=OPENAI_MODEL_ID, input=question)
    print(f"Q: {question}\nA: {response.output_text}\n")


# 1. It doesn't know the present. Same question, three times. Do the answers agree?
for _ in range(3):
    ask("What is today's date? Reply with only the date.")
print(f"(Actual date: {date.today():%B %d, %Y})\n")

# 2. It can't see your data.
ask("What classes do I have tomorrow?")

# 3. It can't act. Did an email actually go anywhere?
ask("Email my professor saying I'll be late to class.")
