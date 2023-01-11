#!/usr/bin/python3
"""defines a class student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get a dictionary rep of student"""
        return self.__dict__
