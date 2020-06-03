#!/usr/bin/python3
"""Function that allows convert from obj json to string"""
import json


def from_json_string(my_str):
    """Function: convert from obj json to string"""
    return(json.loads(my_str))
