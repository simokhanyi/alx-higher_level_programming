#!/usr/bin/python3
"""
Module mylist that inherits from list
"""


class MyList(list):
    """
    Class Mylist inherits list
    """

    def print_sorted(self):
        """
        prints the list, but sorted
        """
        print(sorted(self))
