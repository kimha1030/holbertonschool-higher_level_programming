#!/usr/bin/python3
"""Task 4: What's my status? #1"""
import requests


def my_status():
    """Takes a url, sends request and display body"""
    url_req = "https://intranet.hbtn.io/status"
    req = requests.get(url_req)
    print("Body response:")
    print("\t- type: {:}".format(type(req.text)))
    print("\t- content: {:}".format(req.text))


if __name__ == "__main__":
    my_status()
