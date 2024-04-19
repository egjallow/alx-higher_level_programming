#!/usr/bin/python3
"""
class MyList that inherits from lis
"""


class MyList(list):
    """class that inherits a list"""

    def print_sorted(self):
        """
        prints list in ascending sort
        """
        sort_list = super().copy()
        sort_list = sorted(sort_list)
        print(sort_list)
        
