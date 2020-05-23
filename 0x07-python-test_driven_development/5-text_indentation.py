#!/usr/bin/python3
"""Module to indent text
"""


def text_indentation(text):
    """ Function that allows indent text
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text
    for i in text:
        if i == "?":
            text = text.replace("? ", "?\n\n")
        if i == ":":
            text = text.replace(": ", ":\n\n")
        if i == ".":   
            text = text.replace(". ", ".\n\n")
    print(text, end="")