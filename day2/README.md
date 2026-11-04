# Day 2: Memory and MCP

**Today's idea:** agents get far more useful when they remember, and when they can plug into systems you didn't build.

## Memory

An LLM forgets everything between calls. "Memory" means we save the conversation and send the recent part back with each new message.

That's why it has a cost: more history means more tokens on every call. So we keep only the last few turns (`num_history_runs=5`).

## MCP (Model Context Protocol)

Without a standard, every app needs custom code to work with every tool. MCP is the shared plug, a bit like USB-C for agents:

```
  Your agent  ---+                     +---  Notice board server (we write this)
  Claude Code ---+----  MCP  ----------+---  Time server (someone else's)
  Cursor      ---+                     +---  GitHub, databases, and so on
```

- A **server** offers tools. It knows nothing about LLMs.
- A **client** (your agent) connects to it and finds out which tools exist.
- Write a server once, and any MCP client can use it.

MCP is now run by a neutral foundation under the Linux Foundation, and major AI companies support it.

**When to use what:** write a plain tool when only this agent needs it. Use MCP to share tools between apps, or to use tools someone else already built.

**Be careful:** a local MCP server is code running on your machine, and its text goes straight to your LLM. Only use servers you trust. Day 4 shows why.

## Today's scripts

| File | What it shows |
|---|---|
| `01_memory.py` | Buddy remembers you, even after a restart |
| `02_connect_mcp.py` | Connecting to a server someone else runs |
| `notices_server.py` | Our own MCP server (started for you by the next script) |
| `03_buddy_with_mcp.py` | **Checkpoint:** Buddy with memory, tools and MCP |

```bash
uv run python day2/03_buddy_with_mcp.py
```

## Exercise (in class)

Add a tool to your own MCP server in `exercises/my_server.py`, then connect your agent to it.

```bash
uv run python day2/exercises/my_agent_with_mcp.py
```

## Optional homework

Run `exercises/second_server.py` to use a server you've never seen. Then try another from the [MCP Registry](https://registry.modelcontextprotocol.io).

**Want to go further?** [`bonus/rag_knowledge.py`](../bonus/rag_knowledge.py) lets an agent search a document. That technique is called RAG.
