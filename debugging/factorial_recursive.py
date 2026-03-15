#!/usr/bin/python3
"""
factorial_recursive.py

This script calculates the factorial of a non-negative integer using recursion.

Usage:
    ./factorial_recursive.py <number>

Example:
    ./factorial_recursive.py 4
    Output: 24
"""

import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer recursively.

    Args:
        n (int): The non-negative integer to compute factorial for.

    Returns:
        int: Factorial of n (n!).

    Raises:
        ValueError: If n is negative.

    Explanation:
        - Base case: 0! = 1
        - Recursive case: n! = n * (n-1)!
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Ensure a number is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <non-negative integer>")
        sys.exit(1)

    # Convert input to integer
    num = int(sys.argv[1])

    # Calculate factorial
    result = factorial(num)

    # Print result
    print(result)
