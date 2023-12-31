#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """A rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Args:
            value (int): The new width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The hieght of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Args:
            value (int): The new height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Return a string of the rectangle."""
        rectangle = ''
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += '#'
            if i is not self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle = rectangle + ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Bids rectangle farewell when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
