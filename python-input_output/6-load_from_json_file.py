#!/usr/bin/python3
""" JSON repesentation of an object. """


import json


def load_from_json_file(filename):
    """ Write an object to a text file using JSON.
    Args:
        filename (str): The file to write in.
    """
    with open(filename) as Phile:
        return json.load(Phile)
