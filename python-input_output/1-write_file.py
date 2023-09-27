#!/usr/bin/python3
""" Concatenates a string into a file. """


def write_file(filename="", text=""):
    """ Writes a string to a text file, and
        returns the number of characters written.
    Args:
        filename (str): The file to write in.
        text (str): The text to write.
    """
    with open(filename, "w", encoding="utf-8") as Phile:
        Phile.write(text)
        return len(text)
