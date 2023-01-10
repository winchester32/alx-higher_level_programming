#!/usr/bin/python3
"""contains a function that returns an object"""
import json


def from_json_string(my_str):
    """function that returns a string from JSON"""
    return json.loads(my_str)
