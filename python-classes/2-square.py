#!/usr/bin/python3
"""Define a Square."""


class Square(object):
    """A square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): Size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
