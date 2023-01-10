#!/usr/bin/python3
"""class rectangle that inherits from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines a rectangle"""

    def __init__(self, width, height):
        """initializes a rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
