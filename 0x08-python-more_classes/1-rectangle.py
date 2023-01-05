#!/usr/bin/python3
class Rectangle:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        
