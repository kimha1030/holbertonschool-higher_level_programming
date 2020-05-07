#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary.keys())
    for key, value in a_dictionary.items():
        if key:
            print("{:s}: {}".format(key, value))
