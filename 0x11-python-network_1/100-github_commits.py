#!/usr/bin/python3
"""Task 9: My Github!"""
import requests
from sys import argv


def my_github1():
    """Takes a url, sendsrequest and display body"""
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
    response = requests.get(url)
    response_data = response.json()
    for i in range(10):
        print(response_data[i]['sha'], response_data[i]
              ['commit']['author']['name'])


if __name__ == "__main__":
    my_github1()
