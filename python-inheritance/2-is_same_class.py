#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ Return whether obj is True or False.
    Args:
        obj (any): The object to evaluate.
        a_class (any): The class to evaluate against.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
