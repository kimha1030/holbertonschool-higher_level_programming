#!/bin/bash
# Task 2: Allowed Methods
curl -sX OPTIONS "$1" -i | grep Allow | awk '{print $2,$3,$4}'
