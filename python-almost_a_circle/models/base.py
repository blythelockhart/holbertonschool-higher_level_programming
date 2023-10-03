#!/usr/bin/python3
""" Base class. """


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize Base
        Args:
            id (int): The id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
