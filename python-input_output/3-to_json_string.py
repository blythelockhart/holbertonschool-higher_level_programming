#!/usr/bin/python3
""" JSON repesentation of an object. """


import json


def to_json_string(my_obj):
    """ Return a string representation of an object.
    Args:
        my_obj (str): The object to represent as a string.
    """
    return json.dumps(my_obj)
