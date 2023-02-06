#!/usr/bin/python3
"""
Module that containes the function is_same_class
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class,
    otherwise False
    obj: an object
    a_class: a class
    """
    return (type(obj) is a_class)
