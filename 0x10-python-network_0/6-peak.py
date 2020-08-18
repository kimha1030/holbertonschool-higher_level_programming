#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Function max integer"""
    if list_of_integers:
        return max(list_of_integers)
    else:
        return None
