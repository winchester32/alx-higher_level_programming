#!/usr/bin/python3
"""function delared"""
import json


def load_from_json_file(filename):
    """function that creates obj from JSON"""
    with open(filename) as f:
        return json.load(f)
