#!/usr/bin/python3
"""
This module defines Rectangle Object.
"""


class Rectangle:
    """
    Retangle object with getter and setters
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """privat method"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """private height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculate the area of a rec"""
        return self.height * self.width

    def perimeter(self):
        """calculate a perimeter of a rec"""
        if self.height <= 0 or self.width <= 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """ returns a string repentation of rec"""
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect
        for i in range(1, self.height):
            rect += '#' * self.width + "\n"
        rect += '#' * self.width
        return rect

    def __repr__(self):
        """return astring represendtation"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
