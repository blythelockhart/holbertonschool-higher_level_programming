#!/usr/bin/python3
""" JSON repesentation of an object. """


import json


def from_json_string(my_str):
    """ Return an object representation of a JSON string.
    Args:
        my_str (str): The object to represent as a string.
    """
    return json.loads(my_str)
