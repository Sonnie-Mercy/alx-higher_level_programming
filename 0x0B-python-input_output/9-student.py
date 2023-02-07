#!/usr/bin/python3
"""
module that contains a class called student
"""


class Student:
    """a class that defines student by first name, last name and age"""


def __init__(self, first_name, last_name, age):
    """initializes student"""
    self.first_name = first name
    self.last_name = last name
    self.age = age

    def to_json(self):
        """ Returns a dictionary representation of a Student instance."""
        return self.__dict__
