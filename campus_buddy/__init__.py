"""Shared helpers for the workshop. Importing this also loads your .env file."""

import os
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(__file__).resolve().parent / "data"

load_dotenv(REPO_ROOT / ".env")

# Agno sends basic usage analytics by default. Students' runs stay out of that.
os.environ.setdefault("AGNO_TELEMETRY", "false")

# Format is "provider:model". Change WORKSHOP_MODEL in .env to switch.
MODEL = os.getenv("WORKSHOP_MODEL", "openai:gpt-6-luna")

# The plain OpenAI SDK on Day 1 wants only the part after the colon.
OPENAI_MODEL_ID = MODEL.split(":", 1)[-1]
