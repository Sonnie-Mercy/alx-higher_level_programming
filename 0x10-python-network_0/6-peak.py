#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """peak finding function"""
    n = list_of_integers
    if n:
        n.sort()
        return n[-1]
    else:
        return None
