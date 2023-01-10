#!/usr/bin/python3
"""defines an object attribute lookup function"""


def lookup(obj):
    """funcction that returns list of attributes
    and methods of an object

    returns: list of attributes
    """

    return dir(obj)
