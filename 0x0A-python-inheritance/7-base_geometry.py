#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is greater that 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if type(value) <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
