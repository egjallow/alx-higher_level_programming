#!/usr/bin/python3
""" Prints square module
"""


def print_square(size):
    """ Prints a square

    Prints a square of '#' to stdout according to size argument

    Args:
        size (int)

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    """
    if type(size) in [int, float] and size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    for x in range(size):
        print("#" * size)
