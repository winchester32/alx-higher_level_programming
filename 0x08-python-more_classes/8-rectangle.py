#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ method that returns the value of the width
        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines the width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that returns the value of the height
        Returns:
            height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ method that defines the height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calculates perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0

        return self.width + self.height + self.width + self.height

    def __str__(self):
        """returns #"""
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """returns string"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints message when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
