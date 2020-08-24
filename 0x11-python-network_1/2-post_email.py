#!/usr/bin/python3
"""Task 2: POST an email #0"""
from urllib import request
from urllib import parse
from sys import argv


def post_request():
    """Takes a url and email, sends POST request and display body"""
    post_url = argv[1]
    params = {
        'email': argv[2]
    }
    query_string = parse.urlencode(params)
    post_data = query_string.encode("ascii")
    with request.urlopen(post_url, post_data) as post_response:
        response_text = post_response.read()
        print(response_text.decode("UTF-8"))


if __name__ == "__main__":
    post_request()
