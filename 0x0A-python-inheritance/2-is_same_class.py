#!/usr/bin/python3
"""defines a class-checking function"""


def is_same_class(obj, a_class):
    """check if object is an instance of a given class"""
    if type(obj) == a_class:
        return True
    else:
        return False
