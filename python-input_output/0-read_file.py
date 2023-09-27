#!/usr/bin/python3
""" Define a text file printer. """


def read_file(filename=""):
    """ Print a text file to stdout. """
    with open(filename, encoding="utf-8") as Phile:
        print(Phile.read(), end="")
