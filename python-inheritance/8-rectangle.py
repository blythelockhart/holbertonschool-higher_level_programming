#!/usr/bin/python3
""" Define class: BaseGeometry. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ A rectangle. """
    def __init__(self, width, height):
        """ A new Rectangle.
        Args:
            height (int): The height of the rectangle.
            width (int): The width of the rectangle.
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
