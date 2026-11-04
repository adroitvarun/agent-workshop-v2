"""Run this before Day 1:  uv run python check_setup.py

It checks your setup one step at a time, and tells you what to fix.
The final step makes one very small LLM call.
"""

import os
import sys


def fail(message: str) -> None:
    print(f"\nFIX THIS: {message}")
    sys.exit(1)


print(f"Python {sys.version.split()[0]}")
if sys.version_info < (3, 10):
    fail("You need Python 3.10 or newer. Use GitHub Codespaces, or run: uv python install 3.12")

try:
    import agno  # noqa: F401
    import mcp  # noqa: F401
    import openai  # noqa: F401

    from campus_buddy import MODEL, OPENAI_MODEL_ID
except ImportError as e:
    fail(f"Missing package ({e.name}). Run: uv sync  and start scripts with: uv run python <file>")
print("Packages: OK")

key = os.getenv("OPENAI_API_KEY", "")
if not key or key == "paste-the-key-here":
    print("API key: not set yet")
    print("\nSetup is fine so far. Your instructor shares the key in class.")
    print("When you have it, run: cp .env.example .env  then paste it into .env and run this again.")
    sys.exit(0)
print("API key: found")

try:
    reply = openai.OpenAI().responses.create(model=OPENAI_MODEL_ID, input="Reply with exactly: ready")
except openai.AuthenticationError as e:
    if e.code == "ip_not_authorized":
        fail("The key is fine, but OpenAI is blocking your network. Tell your instructor about the IP allowlist.")
    fail("OpenAI rejected the key. Copy it again, with no spaces or quotes.")
except openai.RateLimitError:
    fail("Rate or spend limit reached. Wait a minute and retry, then tell your instructor.")
except openai.APIConnectionError:
    fail("Can't reach OpenAI. Check your internet, or try Codespaces.")
print(f"Model ({MODEL}): {reply.output_text}")
print("\nAll good. See you on Day 1!")
