#!/usr/bin/python3
""" Define class: BaseGeometry. """


class BaseGeometry:
    """ Base geometry. """
    def area(self):
        """ Raise exception. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate a value as an integer.
        Args:
            name (str): The name of the value.
            value (int): The value of validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
