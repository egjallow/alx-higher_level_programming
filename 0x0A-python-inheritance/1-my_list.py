#!/usr/bin/python3
"""
class MyList that inherits from lis
"""


class MyList(list):
    """class that inherits a list"""

    def print_sorted(self):
        """Sorted list function"""
        sorted_list = sorted(self)
        print(sorted_list)
