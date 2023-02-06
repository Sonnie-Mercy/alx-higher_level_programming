#!/usr/bin/python3
"""A module that defines a class called MyList"""


class MyList(list):
    """
    A class that inherits from list
    """

    def print_sorted(self):
        """Public instance method that prints the list, but assorted"""
        print(sorted(self))
