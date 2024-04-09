#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Property setter for the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """Property setter for the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
            int: The area.
        """
        return self._height * self._width

    def perimeter(self):
        """Calculates the perimeter of a rectangle.

        Returns:
            int: The perimeter.
        """
        if self._height == 0 or self._width == 0:
            return 0
        else:
            return 2 * (self._height + self._width)

    def __str__(self):
        """Prints the rectangle with the character #.

        Returns:
            str: The rectangle.
        """
        rectangle = []

        if self._width == 0 or self._height == 0:
            return ""

        for i in range(self._height):
            for j in range(self._width):
                rectangle.append("#")
            rectangle.append("\n")

        # in order to remove blank line
        rectangle.pop()
        return "".join(rectangle)
