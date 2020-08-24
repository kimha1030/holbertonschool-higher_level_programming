#!/usr/bin/python3
"""Task 1: Response header value #0"""
from urllib import request
from sys import argv


def response_header():
    """Takes a url, send request and display value"""
    url_request = argv[1]
    with request.urlopen(url_request) as response:
        html = response.read()
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    response_header()
