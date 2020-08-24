#!/usr/bin/python3
"""Task 1: Response header value #0"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    html = response.read()
    print(response.headers.get("x-request-id"))
