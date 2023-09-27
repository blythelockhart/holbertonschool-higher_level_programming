#!/usr/bin/python3
""" Dictionary representation of an object. """


def class_to_json(obj):
    """ Return dictionary representation of an object.
    Args:
        obj (str):
    """
    return obj.__dict__
