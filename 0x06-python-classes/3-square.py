#!/usr/bin/python3
"""define a class square"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """new square

        args:
        size (int):" size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current area"""
        return (self.__size * self.__size)
