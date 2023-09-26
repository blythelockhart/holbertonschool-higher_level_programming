#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """ Return whether the object is an instance of,
        or inherited from, the specifierd class.
    Args:
        obj (any): The object to evaluate.
        a_class (any): The class to evaluate against.
    """
    return isinstance(obj, a_class)
