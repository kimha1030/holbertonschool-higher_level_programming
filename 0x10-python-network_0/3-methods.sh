#!/bin/bash
# Task 2: Allowed Methods
curl -sI "$1" | grep Allow | awk '{print $2,$3,$4}'
