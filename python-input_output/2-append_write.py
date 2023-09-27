#!/usr/bin/python3
""" Concatenates a string into a file. """


def append_write(filename="", text=""):
    """ Append a string to a text file, and
        return the number of characters written.
    Args:
        filename (str): The file to write in.
        text (str): The text to write.
    """
    with open(filename, "a", encoding="utf-8") as Phile:
        Phile.write(text)
        return len(text)
