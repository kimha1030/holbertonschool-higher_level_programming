#!/usr/bin/python3
"""Function that allows save a file in json"""
import json


def save_to_json_file(my_obj, filename):
    """Function: save a file in json"""
    with open(filename, "w", encoding="UTF-8") as data_file:
        return data_file.write(json.dumps(my_obj))
