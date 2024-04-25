#!/bin/usr/python3

""" A func that rad files"""


def read_file(filename=""):
    """a function that reads a file:

    Args:
        filename (str): the file name.
    """
    with open(filename, encoding="utf8") as file:
        content = file.read()
        print(content)
