#!/usr/bin/python3
""" Matrix divided module
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix

    Inserts result of division on each element (rounded to two decimal places),
    into a new matrix

    Args:
        matrix []: matrix given
        div: number to divide by

    Returns:
        A new matrix with results of division

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        TypeError: Each row of the matrix must have the same size
        ZeroDivisionError: division by zero

    """
    TE = "matrix must be a matrix (list of lists) of integers/floats"
    SIZE = "Each row of the matrix must have the same size"

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(TE)

    for index, lyst in enumerate(matrix):
        if type(lyst) is not list or len(lyst) == 0:
            raise TypeError(TE)

        if len(lyst) != len(matrix[index - 1]):
            raise TypeError(SIZE)

        for item in lyst:
            if type(item) not in (int, float):
                raise TypeError(TE)

    if type(div) not in (float, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((y / div), 2) for y in x] for x in matrix]
