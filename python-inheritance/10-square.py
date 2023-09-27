#!/usr/bin/python3
""" Define class: Square. """


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """ A square. """
    def __init__(self, size):
        """ A new Square.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
