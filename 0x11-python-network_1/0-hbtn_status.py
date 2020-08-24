#!/usr/bin/python3
"""Task 0: What's my status? #0"""
import urllib.request


def status():
    """Check the status of URL"""
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {:}".format(type(html)))
        print("\t- content: {:}".format(html))
        print("\t- utf8 content: {:}".format(html.decode("UTF-8")))


if __name__ == "__main__":
    status()
