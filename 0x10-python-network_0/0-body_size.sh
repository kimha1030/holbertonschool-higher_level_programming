#!/bin/bash
# Task 0: Takes in a URL, sends a request to URL and displays the size of body
curl -sI "$1" | grep -i Content-length | awk '{print $2}'
