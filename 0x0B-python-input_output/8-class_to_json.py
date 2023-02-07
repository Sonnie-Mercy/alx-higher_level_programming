#!/usr/bin/python3
"""
contains the function class_to_json
"""


import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
