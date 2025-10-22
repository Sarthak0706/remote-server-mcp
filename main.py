from fastmcp import FastMCP
import random
import json


mcp=FastMCP("Simple Calculator Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Returns the sum of two numbers.
    Args:
    a:first number
    b:second number
    Returns:
    sum of a and b
    """
    return a + b

@mcp.tool()
def random_number(min_val: int=1, max_val: int=100) -> int:
    """Generates a random integer between min_val and max_val.
    Args:
    min_val:minimum value(default:1)
    max_val:maximum value(default:100)
    Returns:
    random integer between min_val and max_val
    """
    return random.randint(min_val, max_val)


@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple server that provides basic arithmetic operations and random number generation.",
        "tools": ["add", "random_number"],
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)