#!/usr/bin/python3
"""Module to indent text
"""


def text_indentation(text):
    """ Function that allows indent text
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text
    text = text.replace("? ", "?\n")
    text = text.replace("?", "?\n")
    text = text.replace(": ", ":\n")
    text = text.replace(":", ":\n")
    text = text.replace(". ", ".\n")
    text = text.replace(".", ".\n")
    print(text, end="")