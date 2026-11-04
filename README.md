# AI Agents Workshop

Build a working AI agent of your own in 4 days, 1 hour a day. You need basic Python (functions and lists). You don't need any experience with LLMs or agents.

| Day | Topic | What you add to your agent |
|---|---|---|
| [1](day1/) | **The agent loop:** write it by hand, then in Agno | Its purpose and first tool |
| [2](day2/) | **Memory and MCP:** remember things, and plug into other systems | Memory and its own MCP server |
| [3](day3/) | **Skills, teams and tracing:** teach know-how and see inside | A skill |
| [4](day4/) | **Trust:** prompt injection, human approval and evals | Protection for risky actions |

In class we build **Campus Buddy**, a student assistant, one step at a time. In the exercises you build your own agent alongside it.

## Setup (do this before Day 1)

This takes about 5 minutes, and you'll need a free [GitHub](https://github.com) account.

### Option A: GitHub Codespaces (recommended)

Nothing to install, and it runs in your browser.

1. On this repo's GitHub page, select **Code > Codespaces > Create codespace on main**.
2. Wait for it to finish setting up. This can take a few minutes the first time.
3. In the terminal at the bottom, run:

```bash
uv run python check_setup.py
```

Stop the codespace when you finish each day, because idle time counts toward your free monthly hours.

### Option B: Your own computer

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and [git](https://git-scm.com/downloads).
2. Run these commands:

```bash
git clone https://github.com/adroitvarun/agent-workshop-v2
```

```bash
cd agent-workshop-v2
```

```bash
uv sync
```

```bash
cp .env.example .env
```

```bash
uv run python check_setup.py
```

### Adding the API key

The check will say the key isn't set yet, and that's expected. Your instructor shares it in class. Paste it into the `.env` file, then run the check again.

**Treat the key like a password.** Don't commit it, post it or share it outside the class, because every request costs real money. `.env` is already set up so git ignores it.

## Running the code

Always run scripts from the repo's top folder, starting with `uv run python`:

```bash
uv run python day1/01_llm_limits.py
```

## If you get stuck

| Problem | Fix |
|---|---|
| `OPENAI_API_KEY` missing, or an error about credentials | Check that `.env` exists in the top folder and contains the key |
| `ModuleNotFoundError` | Run `uv sync`, and start scripts with `uv run python` |
| `429` error or rate limit | Wait a minute and try again. If it keeps happening, tell your instructor |
| You fell behind or missed a day | Every day ends with a working checkpoint: `day1/04_campus_buddy.py`, `day2/03_buddy_with_mcp.py`, `day3/04_campus_buddy.py`, `day4/04_campus_buddy.py` |
| An exercise won't work | Working answers are in [solutions/](solutions/). Try it yourself first |

## After the workshop

The class API key stops working after Day 4. To keep your agent running, follow [Using your own key](day4/README.md#using-your-own-key-after-today).

This repo pins exact package versions because agent frameworks change quickly. If you upgrade, expect some code to need changes.
