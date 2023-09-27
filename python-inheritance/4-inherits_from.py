#!/usr/bin/python3
""" Check an object class. """


def inherits_from(obj, a_class):
    """ Return whether an object is inherited from the specific class.
    Args:
        obj (any): The object to evaluate.
        a_class (any): The class to evaluate against.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
