#!/bin/bash
# Task 8: POST request with json file
curl -sH "Content-Type: application/json" --data @"$2" "$1"
