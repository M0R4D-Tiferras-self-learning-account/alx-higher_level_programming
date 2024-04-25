#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file
    and returns the number of characters added

    Args:
        filename (str):the file name.
        text (str):the text to append
    """
    with open(filename, 'a', encoding="utf8") as file:
        file.write(text)
    alpha = 0
    for elem in text:
        alpha += 1
    return alpha
