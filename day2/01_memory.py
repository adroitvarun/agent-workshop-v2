"""Day 2, step 1: memory. Conversations are saved to a SQLite file.

Try this: tell Buddy your name and favourite subject, type 'quit', and run the
script again. Then ask "what's my name?". The program restarted, but the file didn't.
"""

from agno.agent import Agent
from agno.db.sqlite import SqliteDb

from campus_buddy import MODEL
from campus_buddy.display import chat
from campus_buddy.tools import calculate_cgpa, get_timetable

buddy = Agent(
    name="Campus Buddy",
    model=MODEL,
    tools=[calculate_cgpa, get_timetable],
    instructions="You help college students. Be brief and friendly.",
    db=SqliteDb(db_file="tmp/buddy.db"),  # Where conversations are stored.
    session_id="my-chat",                 # Same id = same conversation after a restart.
    add_history_to_context=True,          # Send past messages to the LLM on each turn.
    num_history_runs=5,                   # Only the last 5 turns, to control cost.
)

if __name__ == "__main__":
    print("Type 'quit' to stop.")
    chat(buddy)
