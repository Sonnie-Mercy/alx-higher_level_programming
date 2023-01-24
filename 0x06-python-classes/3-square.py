#!/usr/bin/python3
"""class Square that finds the area of a square"""


class Square():
    """square class with it's size and proper validation"""
    def __init__(self, size=0):
        """defines the size of the square"""
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

        def area(self):
            """finds the area"""
            return self.__size ** 2
