#!/usr/bin/python3
"""function that returns JSOM of a string"""
import json


def to_json_string(my_obj):
    """return JSON"""
    return json.dumps(my_obj)
