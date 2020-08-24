#!/usr/bin/python3
"""Task 3: Error code #0"""
from urllib import request
from urllib.error import HTTPError
from sys import argv


def error_code():
    """Takes a url, sendsrequest and display body"""
    url_request = argv[1]
    req = request.Request(url_request)
    try:
        with request.urlopen(req) as resp:
            html = resp.read()
            print(html.decode("UTF-8"))
    except HTTPError as e:
        print('Error code: ', e.code)


if __name__ == "__main__":
    error_code()
