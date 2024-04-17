#!/usr/bin/python3
""" module `4-inherits_from` provides the `inherits_from` function """


def inherits_from(obj, a_class):
    """ tests `obj` inheritance from `a_class` """
    return isinstance(obj, a_class) and type(obj) != a_class
