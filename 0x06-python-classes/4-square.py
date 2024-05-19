#!/bin/usr/python3

"""Area of a square"""


class Square:
    """
    A class that represent a square

    Attributes:
        size (int): The size of the square.
        area (int): The area of the square.
    """
    def __init__(self, size=0):
        """Creates new instances of the square

        Args:
            size (int): size of the square
        """

        if type(size) != int:
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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer ")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
