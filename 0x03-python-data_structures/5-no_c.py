#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string = list(my_string)
        new = list()
        for ch in my_string:
            if ch != 'c' and ch != 'C':
                new.append(ch)
        my_string = ''.join(new)
    return (my_string)
