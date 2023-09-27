#!/usr/bin/python3
""" JSON repesentation of an object. """


import json


def to_json_string(my_obj):
    """ Return an object represented by a JSON string.
    Args:
        my_obj (str): The object to represent as a string.
    """
    return json.loads(my_obj)
