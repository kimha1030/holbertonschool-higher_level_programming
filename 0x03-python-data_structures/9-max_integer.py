#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return ('None')
    else:
        my_list_ord = sorted(my_list)
        last_position = length - 1
        return (my_list_ord[last_position])
