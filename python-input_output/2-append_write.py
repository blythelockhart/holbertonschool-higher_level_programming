#!/usr/bin/python3
""" Concatenates a string into a file. """


def append_write(filename="", text=""):
    """ Appends a string to a text file, and
        returns the number of characters written.
    Args:
        filename (str): The file to write in.
        test (str): The text to write.
    """
    with open(filename, "w", encoding="utf-8") as Phile:
        Phile.write(text)
        return len(text)
