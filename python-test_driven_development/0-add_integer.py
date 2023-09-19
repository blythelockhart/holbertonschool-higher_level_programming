#!/usr/bin/python3
"""Add two integers."""

def add_integer(a, b=98):
    """Return the sum of two integers."""
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
