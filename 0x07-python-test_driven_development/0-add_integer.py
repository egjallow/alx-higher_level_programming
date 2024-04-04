#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) not in [int,float]:
        raise TypeError("a must be and integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float or type(b) == float:
        return float(a) + float(b)
    else:
        return a + b
