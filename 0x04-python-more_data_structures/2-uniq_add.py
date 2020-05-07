#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        uniq = list(set(my_list))
        result = sum(uniq)
        return (result)
