#!/usr/bin/python3
""" Check an object class. """


def is_same_class(obj, a_class):
    """ Return whether obj is True or False.
    Args:
        obj (any): The object to evaluate.
        a_class (any): The class to evaluate against.
    """
    if type(obj) == a_class:
        return True
    return False
