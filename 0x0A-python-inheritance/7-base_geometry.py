#!/usr/bin/python3
""" module `7-base_geometry` the `BaseGeometry` class """


class BaseGeometry:
    """ `BaseGeometry` class """
    def area(self):
        """ raises `not implemented` exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ raise error if value is not a strictly positive integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
