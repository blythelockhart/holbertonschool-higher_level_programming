#!/usr/bin/python3
""" Define a square. """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square. """
    def __init__(self, size):
        """ A new square.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Return the area of a square. """
        return (self__size ** 2)

    def __str__(self):
        """ Return a square as a string. """
        square = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return square
