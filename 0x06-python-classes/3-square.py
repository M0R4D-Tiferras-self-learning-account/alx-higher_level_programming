#!/bin/usr/python3

"""Defining a class called square"""


class Square:
    """
    A class that represent a square

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Creates new instances of the square

        Args:
            size (int): size of the square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A function that return the area of the square

        Returns:
            area (int): The area of the square.
        """
        area = self.__size ** 2
        return area
