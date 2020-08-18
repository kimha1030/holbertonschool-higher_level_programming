#!/bin/bash
# Task 7: Only status code
curl -sI "$1" | awk '$1=="HTTP/1.0" {print $2}'
