#!/bin/bash
# Task 2: Allowed Methods
curl -X OPTIONS -s "$1" -i | grep Allow | awk '{print $2, $3, $4}'
