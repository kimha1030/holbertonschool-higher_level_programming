#!/usr/bin/python3
"""Task 7: Error code #0"""
import requests
from sys import argv


def error_code1():
    """Takes a url, sendsrequest and display body"""
    url_req = argv[1]
    req = requests.get(url_req)
    if req.status_code >= 400:
        print("Error code: {:}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    error_code1()
