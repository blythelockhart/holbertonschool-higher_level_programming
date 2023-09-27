#!/usr/bin/python3
""" JSON repesentation of an object. """


import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file using JSON.
    Args:
        my_obj (str): The object to write.
        filename (str): The file to write in.
    """
    with open(filename, 'w', encoding='utf-8') as Phile:
        Phile.write(json.dump(my_obj))
