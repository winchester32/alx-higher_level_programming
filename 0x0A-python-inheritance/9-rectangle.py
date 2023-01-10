#!/usr/bin/python3
"""defines a class rectangle that inherits from basefgeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines a rectangle"""

    def __init__(self, width, height):
        """initializes a rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return print() and str()"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
