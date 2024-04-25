#!/bin/usr/python3

""" a func that add tow number """


def add_integer(a, b=98):
    """add_integer: a function that add tow num

    Args:
    a (integer, float): first num to add
    b (integer, float): second num to add

    Returns:
    a+b (int): as the sum of a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
