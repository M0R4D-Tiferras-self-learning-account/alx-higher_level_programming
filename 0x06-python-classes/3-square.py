#/bin/usr/python3

"""Defining a class called square"""


class Square:
    """
    A class that represent a square

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        try:
            if size >= 0 and type(size) == int:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
    
    def area(self):
        """A function that return the area of the square
        """
        area = self.__size * self.__size
        return area
