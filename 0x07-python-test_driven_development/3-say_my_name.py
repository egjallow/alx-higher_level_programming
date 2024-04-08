#!/usr/bin/python3
""" Say my name module
"""


def say_my_name(first_name, last_name=""):
    """ Prints a first and last name

    Args:
        first_name (str)
        last_name (str)

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if len(first_name) > 0:
        print("My name is {:s} {:s}".format(first_name, last_name))
