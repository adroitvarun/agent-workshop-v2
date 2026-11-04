# Day 3: Skills, Teams and Tracing

**Today's idea:** teach an agent how to do something, split up work only when you need to, and learn to read what it actually did.

## Skills

A skill is a folder with a `SKILL.md` file in it: step-by-step know-how, written in plain English.

```
exam-prep-planner/
  SKILL.md           <- name, description, and the instructions
  references/        <- extra detail, loaded only if needed
```

The agent always sees each skill's name and description, but loads the rest only when it needs it. So you can give an agent many skills without paying for all of them on every request.

Agent Skills is an open standard, and many tools can use the same `SKILL.md`, including several coding agents. What you write today isn't tied to Agno.

**Skills can include scripts, which an agent may run.** Treat someone else's skill like someone else's code, and read it before you use it. Ours contain only instructions.

| | **Tool** | **MCP server** | **Skill** |
|---|---|---|---|
| **Gives the agent** | An ability | Abilities from elsewhere | Know-how |
| **Written in** | Code | Code | Mostly plain English |
| **Example** | Calculate a CGPA | Read the notice board | How to build a study plan |

## Teams

A team has a leader who passes work to specialists.

**Start with one agent.** A team costs more and is harder to debug, because every extra agent means extra LLM calls. Split only when members truly need different tools or instructions.

## Tracing

A trace records each step of a run: every LLM call and tool call, in order, with timings. When an agent does something odd, this is how you find out why. You can't fix what you can't see.

## Today's scripts

| File | What it shows |
|---|---|
| `01_skill.py` | The skill loads for a study plan, but not for a CGPA question |
| `02_team.py` | A researcher and a planner working together |
| `03_tracing.py` | The same team, with its run printed as a tree |
| `04_campus_buddy.py` | **Checkpoint:** Buddy with everything so far |

```bash
uv run python day3/04_campus_buddy.py
```

## Exercise (in class)

Write a skill for your agent in `exercises/my_skills/my-first-skill/SKILL.md`, then run:

```bash
uv run python day3/exercises/my_agent_with_skill.py
```

## Optional homework

Polish your agent. Want to show it tomorrow? Tell your instructor today.
