#!/usr/bin/python3
"""Task 6: POST an email #1"""
import requests
from sys import argv


def post_request1():
    """Takes a url and email, sends POST request and display body"""
    post_url = argv[1]
    payload = {
        'email': argv[2]
    }
    req = requests.post(post_url, data=payload)
    print(req.text)


if __name__ == "__main__":
    post_request1()
