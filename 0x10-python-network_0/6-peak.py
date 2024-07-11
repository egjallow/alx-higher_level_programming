#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find the peak number with the shortest algorithm"""

    l = list_of_integers
    return max(l) if l else None
