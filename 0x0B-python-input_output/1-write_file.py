#!/usr/bin/python3
""" contains a function that writes a string"""


def write_file(filename="", text=""):
    """function thats writes a string to a text file"""
    with open(filename, "w",  encoding="utf-8") as f:
        return f.write(text)
