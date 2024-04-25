#!/bin/usr/python3

"""Divide a matrix"""

def check_size(matx):
    """A func that check if the 2D array elements are the same

    Args:
        matx (2D list): the matrix
    
    Returns:
        True, False (boolean): True if the lists inside the matrix are the same else retuen False
    """
    rows = len(matx)
    i = 0
    llog = len(matx[0])
    while (i < rows):
        if len(matx[i]) != llog:
            return False
        i += 1
    return True


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: The matrix whoses elements are to be divided by div.
        div: The dividing number.

    Raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix with elements rounded to 2 decimal places.
    """
    if not isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if check_size(matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda item: round(item / div, 2), row)) for row in matrix]
