#!/usr/bin/python3
""" A Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ A Rectangle. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ A new rectangle.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): The x variable.
            y (int): The y variable.
            id (int): The id.
        """
        self.value_validate(width, 'width')
        self.value_validate(height, 'height')
        self.value_validate(x, 'x')
        self.value_validate(y, 'y')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ The width. """
        return self.__width

    @property
    def height(self):
        """ The height. """
        return self.__height

    @property
    def x(self):
        """ The x variable. """
        return self.__x

    @property
    def y(self):
        """ The y variable. """
        return self.__y

    @width.setter
    def width(self, i):
        """ Set the new width.
        Args:
            i (int): The new width.
        """
        self.value_validate(i, 'width')
        self.__width = i

    @height.setter
    def height(self, i):
        """ Set the new height.
        Args:
            i (int): The new height.
        """
        self.value_validate(i, 'height')
        self.__height = i

    @x.setter
    def x(self, i):
        """ Set the new x variable.
        Args:
            i (int): The new x variable.
        """
        self.value_validate(i, 'x')
        self.__x = i

    @y.setter
    def y(self, i):
        """ Set the new y variable.
        Args:
            i (int): The new y variable.
        """
        self.value_validate(i, 'y')
        self.__y = i

    def value_validate(self, value, attr):
        """ Validate a value.
        Args:
            value (int): Value to be validated.
            attr (str): Name of the value.
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(attr))
        if attr in ('width', 'height'):
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attr))
        if attr in ('x', 'y'):
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attr))

    def area(self):
        """ Return the area of the rectangle. """
        return self.__width * self.__height

    def display(self):
        """ Print the rectangle. """
        for m in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """ Override the '___str___' method. """
        strng = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return strng

    def update(self, *args, **kwargs):
        """ Assign an argument to each attribute.
        Args:
            id (int): The id.
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): The x variable.
            y (int): The y variable.
        Kwargs:
            Kwargs are arguments that match keywords.
        """
        arg = ['id', 'width', 'height', 'x', 'y']
        kwarg = kwargs.items()
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        else:
            for kw, val in kwarg:
                if hasattr(self, kw):
                    setattr(self, kw, val)

    def to_dictionary(self):
        """ Return the dictionary representation of the rectangle. """
        return {'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y, 'id': self.id}
