#!/usr/bin/python3

def add_integer(a, b=98):
    """Return the sum of two integers."""
    if type(a) is  float:
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
