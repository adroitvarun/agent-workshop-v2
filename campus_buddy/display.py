"""Small helpers that show what an agent did. Agno runs the agent; these just print."""


def show_tools(run) -> None:
    """Print each tool the agent called during a run."""
    tools = run.tools or []
    if not tools:
        print("[no tools called]")
    for t in tools:
        print(f"[tool] {t.tool_name}({t.tool_args}) -> {str(t.result)[:200]}")


def chat(agent) -> None:
    """Chat with an agent in the terminal. Type 'quit' to stop."""
    while True:
        message = input("\nYou: ").strip()
        if message.lower() in {"quit", "exit", "q"}:
            return
        if message:
            agent.print_response(message, stream=True)


async def achat(agent) -> None:
    """The same chat loop, for agents with MCP tools (which are async)."""
    while True:
        message = input("\nYou: ").strip()
        if message.lower() in {"quit", "exit", "q"}:
            return
        if message:
            await agent.aprint_response(message, stream=True)
