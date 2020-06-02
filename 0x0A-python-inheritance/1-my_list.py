#!/usr/bin/python3
"""Class my_list"""


class MyList(list):
    """Class Mylist"""
    def print_sorted(self):
        """Method for ordered list"""
        print(sorted(self))
