# Day 1: The Agent Loop

**Today's idea:** an agent is a loop around an LLM, and it's short enough to write yourself.

## What an LLM can't do

An LLM predicts text. On its own, it has three big limits:

- **It doesn't know the present.** Its knowledge stops at a training cutoff. Ask for today's date and you may get a confident, wrong answer.
- **It can't see your data.** It has never seen your timetable, your marks or your files.
- **It can't act.** It can only produce text. It can write that email, but it can't send it.

Older LLMs also got arithmetic wrong all the time. The one we're using handled very large multiplications when we tested it, so we don't rely on that as a demo. Tools are still the right choice for numbers that matter, because code gives the same exact answer every time, and you can check it.

## The loop

Tool calling gets around all three. You tell the LLM which tools exist, and it can ask you to run one.

```
        your question
              |
              v
   +--->  LLM decides
   |          |
   |          +--- "here's my answer" ---> done
   |          |
   |     "run this tool, with these inputs"
   |          |
   |          v
   +---- YOUR code runs the tool and sends back the result
```

The most important detail: **the LLM never runs anything.** It only asks, and your code decides what to do. This comes back on Day 4.

An **agent** is this loop plus tools and instructions. A framework like Agno writes the loop for you, but it's the same loop.

## Today's scripts

| File | What it shows |
|---|---|
| `01_llm_limits.py` | The three limits, live |
| `02_loop_by_hand.py` | The whole loop in about 30 lines of plain Python |
| `03_agno_agent.py` | The same agent in Agno |
| `04_campus_buddy.py` | **Checkpoint:** Campus Buddy with two tools |

```bash
uv run python day1/04_campus_buddy.py
```

## Tools are for the LLM to read

The LLM never sees your function's code. It only sees the name, the parameters and the docstring, so write them for a new teammate who can't read the code.

## Exercise (in class)

Start your own agent in `exercises/my_agent.py`. You'll keep adding to this idea all week, so pick something you'd actually use.

```bash
uv run python day1/exercises/my_agent.py
```

## Homework (10 min)

Run `exercises/bad_docstring.py`, then improve only the tool's name and docstring. What changed?

## Key words

| Word | Meaning |
|---|---|
| **LLM** | The model that predicts text |
| **Tool** | A function the LLM can ask your code to run |
| **Agent** | An LLM in a loop, with tools and instructions |
| **Instructions** | Text that shapes how the agent behaves |
