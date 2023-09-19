#!/usr/bin/python3
"""Define a Square."""


class Square:
    """A square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): Size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)

    def size(self):
        """Return the size of the square."""
        return self.__size

    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square."""
        if size == 0:
            print()
        else:
            for i in range(size):
                print("#".format(i), end="")
