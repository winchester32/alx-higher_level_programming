#!/usr/bin/python3
"""defines arectangle class"""
from models.base import Base


class Rectangle(Base):
    """rep a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height
