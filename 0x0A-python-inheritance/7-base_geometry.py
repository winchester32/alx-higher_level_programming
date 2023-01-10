#!/usr/bin/python3
"""defines an empty class"""


class BaseGeometry:
    """contains public instance method"""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """receives value property"""
        if type(value) is not int:
            raise TypeError("{}  must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
