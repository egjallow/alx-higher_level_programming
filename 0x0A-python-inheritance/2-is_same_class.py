#!/usr/bin/python3
""" module `2-is_same_class` provides `is_same_class` function """


def is_same_class(obj, a_class):
    """ tests if `obj` is exactly an instance of `a_class` """
    return type(obj) == a_class
