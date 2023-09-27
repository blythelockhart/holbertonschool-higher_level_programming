#!/usr/bin/python3
""" Check an object class. """


def is_kind_of_class(obj, a_class):
    """ Return whether the object is an instance of,
        or inherited from, the specified class.
    Args:
        obj (any): The object to evaluate.
        a_class (any): The class to evaluate against.
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
