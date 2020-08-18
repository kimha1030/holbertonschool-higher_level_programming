#!/bin/bash
# Task 7: Only status code
curl -s -o -i -w "{http_code}" "$1"
