#!/usr/bin/python3
""" Lookup an object attribute. """


def lookup(obj):
    """ Return the list of available attributes and methods of an object. """
    return (dir(obj))
