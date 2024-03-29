#!/usr/bin/python3
"""
This module defines a Square class && initialise its size and check

for it's attribute
"""


class Square:
    """Square implementation
    """

    def __init__(self, size=0):
        """initialise"""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
