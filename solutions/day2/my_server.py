"""One possible Day 2 solution: the attendance coach's tool, now on an MCP server."""

import math

from mcp.server.mcpserver import MCPServer

server = MCPServer("attendance")


@server.tool()
def classes_needed(attended: int, total: int, target_percent: float = 75) -> str:
    """Work out how many more classes in a row a student must attend to reach an attendance target."""
    if total <= 0:
        return "Error: total classes must be more than zero."
    if not 0 < target_percent < 100:
        return "Error: target_percent must be between 0 and 100."
    current = attended / total * 100
    if current >= target_percent:
        return f"Current attendance is {current:.1f}%. Target already met."
    needed = math.ceil((target_percent * total - 100 * attended) / (100 - target_percent))
    return f"Current attendance is {current:.1f}%. Attend the next {needed} classes in a row."


@server.tool()
def classes_can_miss(attended: int, total: int, target_percent: float = 75) -> str:
    """Work out how many upcoming classes a student can miss and stay at the attendance target."""
    if total <= 0 or not 0 < target_percent < 100:
        return "Error: check total and target_percent."
    can_miss = math.floor(100 * attended / target_percent - total)
    return f"You can miss {max(can_miss, 0)} more classes."


if __name__ == "__main__":
    server.run()
