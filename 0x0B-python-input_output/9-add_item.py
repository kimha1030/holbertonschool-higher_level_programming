#!/usr/bin/python3
"""Function that allows create a new json object"""
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
values = sys.argv[1:]

if os.path.isfile(filename):
    data_list = load_from_json_file(filename)
    data_list = data_list + values
    save_to_json_file(list(data_list), filename)
else:
    save_to_json_file(list(values), filename)
