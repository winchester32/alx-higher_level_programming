#!/usr/bin/python3
"""function that reads a file"""


def read_file(filename=""):
    """function that reads from a file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
