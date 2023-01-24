#!/usr/bin/python3
"""
This module defines a Square class and initialise its size
"""


class Square:
    """
    Square implementation
    """

    def __init__(self, size=0)
    if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
