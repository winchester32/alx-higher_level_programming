#!/usr/bin/python3
"""defines a class student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dictionary rep of student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attributes of Student"""
        for i, v in json.items():
            setattr(self, i, v)
