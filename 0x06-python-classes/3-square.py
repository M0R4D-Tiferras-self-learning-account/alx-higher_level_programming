#!/bin/usr/python3
"""Area of a square"""


class Square:
    """
    A class that represent a square
    """

    def __init__(self, size=0):
        """Creates new instances of the square
        Args:
            size (int): size of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer ")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A function that return the area of the square

        Returns:
            area (int): The area of the square.
        """
        area = self.__size ** 2
        return area
