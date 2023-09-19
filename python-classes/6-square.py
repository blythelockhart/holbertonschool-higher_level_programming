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
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """return the area of the square."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """return the size of the square."""
        return self.__size

    @size.setter
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

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (int): Value of the position of the square.
        """
        if type(value) is not tuple \
            or value[0] is not int \
            or value[1] is not int \
            or value[0] < 0 \
            or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
