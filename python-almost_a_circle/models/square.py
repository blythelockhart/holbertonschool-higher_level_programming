#!/usr/bin/python3
""" A Square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square. """
    def __init__(self, size, x=0, y=0, id=None):
        """ A new square.
        Args:
            size (int): Size of the square.
            x (int): The x variable.
            y (int): The y variable.
            id (int): The id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Override the '___str___' method. """
        strng = '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
                self.id, self.x, self.y, self.width)
        return strng

    @property
    def size(self):
        """ The size of the square. """
        return self.width

    @size.setter
    def size(self, i):
        """ Set the new size of the square.
        Args:
            size (int): The new size of the square.
        """
        self.width = i
        self.height = i

    def update(self, *args, **kwargs):
        """ Assign an argument to each attribute.
        Args:
            id (int): The id.
            size (int): Size of the square.
            x (int): The x variable.
            y (int): The y variable.
        Kwargs:
            Kwargs are arguments that match keywords.
        """
        arg = ['id', 'size', 'x', 'y']
        kwarg = kwargs.items()
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        else:
            for kw, val in kwarg:
                if hasattr(self, kw):
                    setattr(self, kw, val)
