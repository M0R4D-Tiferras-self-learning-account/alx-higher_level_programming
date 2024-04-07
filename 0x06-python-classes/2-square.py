#!/usr/bin/python3

"""Initiallizing Square class"""


class Square:
    """
    A class that represent a square

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        if type(size) == int:
            if size > 0:
                self.size = size
                return
            elif size < 0:
                raise ValueError("size must be >= 0")
                return
        else:
            raise TypeError("size must be an integer")
