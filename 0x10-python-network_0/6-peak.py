#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    n = len(list_of_integers)
    first = 0
    last = n - 1

    while first <= last:
        mid = (first + last) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1])
        and \ (mid == n - 1 or list_of_integers[mid] >=
                list_of_integers[mid + 1]):
            return list_of_integers[mid]

        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            last = mid - 1

        else:
            first = mid + 1

            return None
