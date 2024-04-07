#!/usr/bin/python3

"""Defining a class called square"""


class Square:
    """
    A class that represent a square

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """A constractor function

        Args:
            size (int): The size of the square

        Raises:
            ValueError: The size must be a non-zero integer
            TypeError: The size must be a non-zero integer
        """
        if type(size) == int:
            if size > 0:
                self.size = size
                return
            elif size < 0:
                raise ValueError("size must be >= 0")
                return
        else:
            raise TypeError("size must be an integer")
