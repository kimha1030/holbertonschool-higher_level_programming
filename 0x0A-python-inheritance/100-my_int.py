#!/usr/bin/python3
"""Class My Integer"""


class MyInt(int):
    """Class My integer"""
    def __ne__(self, other):
        return True

    def __eq__(self, other):
        return False
