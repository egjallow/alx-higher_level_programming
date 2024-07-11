#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Find the peak number with the shortest algorithm."""
    if not list_of_integers:
        return None
    
    n = len(list_of_integers)
    mid = n // 2

    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
       (mid == n - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    
    return find_peak(list_of_integers[mid + 1:])

