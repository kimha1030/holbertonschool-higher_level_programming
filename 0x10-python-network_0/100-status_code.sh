#!/bin/bash
# Task 7: Only status code
curl -o /dev/null -s -w "%{http_code}" "$1"
