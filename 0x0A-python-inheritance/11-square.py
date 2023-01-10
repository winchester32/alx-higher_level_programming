#!/usr/bin/python3
"""defines a rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size):
        """initializes a new square"""
        self.integer_validator("size", size)
         self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area of a square"""
        return super().area()

    def __str__(self):
        """returns str"""
        return "[square] {}/{}".format(self.__size, self.__size)
