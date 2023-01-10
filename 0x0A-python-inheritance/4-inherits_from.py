#!/usr/bin/python3
"""an inherited class-checking function"""


def inherits_from(obj, a_class):
    """checks if an obj is an inherited inc=stance of a class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
