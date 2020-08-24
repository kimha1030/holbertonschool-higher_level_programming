#!/usr/bin/python3
"""Task 5: Response header value #1"""
import requests
from sys import argv


def response_header1():
    """Takes a url, send request and display value"""
    url_req = argv[1]
    req = requests.get(url_req)
    req.text
    print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    response_header1()
