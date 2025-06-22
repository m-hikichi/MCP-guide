import math
import statistics
from builtins import max as builtin_max
from builtins import min as builtin_min
from builtins import round as builtin_round
from builtins import sum as builtin_sum
from typing import List

from mcp.server.fastmcp import FastMCP

# MCPサーバーインスタンスの作成
mcp = FastMCP("math")


@mcp.tool()
def add(a: float, b: float) -> float:
    """
    Adds two numbers together
    """
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first number
    """
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers together
    """
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second number
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def sum(numbers: List[float]) -> float:
    """
    Adds any number of numbers together
    """
    return builtin_sum(numbers)


@mcp.tool()
def mean(numbers: List[float]) -> float:
    """
    Calculates the arithmetic mean of the numbers
    """
    if not numbers:
        raise ValueError("Cannot compute mean of no numbers.")
    return statistics.mean(numbers)


@mcp.tool()
def mode(numbers: List[float]) -> float:
    """
    Finds the most common number in the input
    """
    if not numbers:
        raise ValueError("Cannot compute mode of no numbers.")
    return statistics.mode(numbers)


@mcp.tool()
def min(numbers: List[float]) -> float:
    """
    Finds the minimum value among the input numbers
    """
    if not numbers:
        raise ValueError("Empty list provided for min.")
    return builtin_min(numbers)


@mcp.tool()
def max(numbers: List[float]) -> float:
    """
    Finds the maximum value among the input numbers
    """
    if not numbers:
        raise ValueError("Empty list provided for max.")
    return builtin_max(numbers)


@mcp.tool()
def floor(number: float) -> int:
    """
    Rounds a number down to the nearest integer
    """
    return math.floor(number)


@mcp.tool()
def ceiling(number: float) -> int:
    """
    Rounds a number up to the nearest integer
    """
    return math.ceil(number)


@mcp.tool()
def round(number: float) -> int:
    """
    Rounds a number to the nearest integer
    """
    return builtin_round(number)


if __name__ == "__main__":
    mcp.run()
