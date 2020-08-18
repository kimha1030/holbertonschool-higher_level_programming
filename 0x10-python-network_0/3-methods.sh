#!/bin/bash
# Task 2: Allowed Methods
curl -sIX OPTIONS "$1" | grep Allow | awk '{print $2,$3,$4}'
