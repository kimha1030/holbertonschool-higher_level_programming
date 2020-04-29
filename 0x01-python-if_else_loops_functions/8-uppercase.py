#!/usr/bin/python3
def uppercase(str):
    str = str + "\n"
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            letter = ord(str[i]) - 32
        else:
            letter = ord(str[i])
        print("{:c}".format(letter), end='')
