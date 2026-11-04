"""Day 4 demo tools. The profile is made up, and no email ever leaves your computer."""

import json

from agno.tools import tool


@tool
def get_my_profile() -> str:
    """Get the student's private profile: name, roll number, date of birth and phone number."""
    return json.dumps({
        "name": "Asha Rao",
        "roll_number": "21CS1047",
        "date_of_birth": "2004-03-17",
        "phone": "+91 98765 00000",
    })


def fake_send(to: str, subject: str, body: str) -> str:
    print(f"\n*** EMAIL SENT (demo, nothing really left your computer) ***\nTo: {to}\nSubject: {subject}\n{body}\n***\n")
    return "Email sent."
