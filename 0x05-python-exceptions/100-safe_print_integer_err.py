#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except Exception as va:
        print("Exception: Unknown format code 'd' for object of type 'str'", va, file=sys.stderr)
        return False
