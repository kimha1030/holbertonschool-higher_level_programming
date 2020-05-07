#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new_list = my_list.copy()
        for n, e in enumerate(my_list):
            if e == search:
                new_list[n] = replace
    return (new_list)
