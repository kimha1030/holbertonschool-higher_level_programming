#!/usr/bin/python3
"""Task 0: What's my status? #0"""
import urllib.request


def status():
    """Check the status of URL"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body request:")
        print("\t- type: {:}".format(type(html)))
        print("\t- content: {:}".format(html))
        print("\t- utf-8: {:}".format(html.decode("UTF-8")))


if __name__ == "__main__":
    status()
