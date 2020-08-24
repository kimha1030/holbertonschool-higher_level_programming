#!/usr/bin/python3
"""Task 9: My Github!"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def my_github():
    """Takes a url, sendsrequest and display body"""
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/users/' + username
    response = requests.get(
        url, ",", auth=HTTPBasicAuth(username, password))
    response_to_json = response.json()
    id_user = response_to_json.get('id')
    if id_user != "None":
        print(id_user)
    else:
        print("None")


if __name__ == "__main__":
    my_github()
