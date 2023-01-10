#!/usr/bin/python3
"""contains MyList class"""


class MyList(list):
    """inherited from lisy"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
