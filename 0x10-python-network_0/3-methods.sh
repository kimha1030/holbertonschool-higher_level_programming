#!/bin/bash
# Task 3: Allowed Methods
curl -X OPTIONS -s "$1" -i | grep Allow | cut -d: -f2-4
