#!/usr/bin/python3
""" defines a base model class"""


class Base:
    """rep a class model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initiliazes a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
