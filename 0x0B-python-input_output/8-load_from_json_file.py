#!/usr/bin/python3
"""Function that allow load from json to file"""
import json


def load_from_json_file(filename):
    """Function: load from json to file"""
    with open(filename, "r", encoding="UTF-8") as data_file:
        read_file = data_file.read()
        return json.loads(read_file)
