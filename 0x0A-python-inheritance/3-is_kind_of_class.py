#!/usr/bin/python3
"""defines a class-checking function"""


def is_kind_of_class(obj, a_class):
    """check if an obj is an instance/ inheroited instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
