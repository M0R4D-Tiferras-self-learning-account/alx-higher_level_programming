#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file and return numb of
    written characters

    Args:
        filename (str): name of the file.
        text (str): text to write in the file.
    """
    with open(filename, encoding="utf8") as file:
        file.write(text)
    chars = 0
    for elem in text:
        chars += 1
    return chars
