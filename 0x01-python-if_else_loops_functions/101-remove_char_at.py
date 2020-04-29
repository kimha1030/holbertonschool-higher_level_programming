#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if (n >= 0):
            str = str[:n] + str[n + 1:]
            return(str)
        else:
            return(str)
