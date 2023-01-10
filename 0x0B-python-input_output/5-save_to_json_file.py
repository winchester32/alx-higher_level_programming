#!/usr/bin/python3
"""contains function that writes an object to a text file"""
import json

def save_to_json_file(my_obj, filename):
    """function that writes obj to txt file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
