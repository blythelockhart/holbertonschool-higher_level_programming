#!/usr/bin/python3
"""Define a Sqaure."""


class Square:
    """A square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): Size of the square.
            position (int, int): Position of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area of the square."""
        return (self.__size ** 2)

    def size(self):
        """return the size of the square."""
        return self.__size

    def size(self, value):
        """Set the new size of the square.

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
            for i in range(self.__size):
                print('#', end="")
            print()

    def position(self):
        """Return the position of the square."""
        return self.__position

    def position(self, value):
        """Set the position of the square.

        Args:
            value (int): Value of the position of the square.
        """
        if type(position) is not tuple or
        self is not int or
        value is not int or
        self < 0 or
        value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
