#!/bin/bash
# Task 3: Allowed Methods
curl -X OPTIONS -s "$1" -i | awk '$1=="Allow:" {print $2, $3, $4}'
