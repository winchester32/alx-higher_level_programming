#!/usr/bin/python3
""" defime a square """


class Square:
    """ a square"""
    def __init__(self, size=0):
        """ new square
        args:
        size(int): size of a mew square
        """
        if not isinstance(size, int):
            raise TypeError(
                    "size must be an integer")
        elif size < 0:
            raise ValueError(
                    "size must be >= 0")
            self.__size = size
