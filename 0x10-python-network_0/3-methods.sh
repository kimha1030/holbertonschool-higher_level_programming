#!/bin/bash
# Task 3: Allowed Methods
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
