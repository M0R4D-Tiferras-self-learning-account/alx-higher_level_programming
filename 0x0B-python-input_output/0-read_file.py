#!/bin/usr/python3

""" A func that rad files"""

def  read_file(filename=""):
    """a function that reads a file:

    Args:
        filename (str, optional): the file name.
    """
    with open(filename, 'r', encoding="utf8") as file:
        content = file.read()
        print(content)
