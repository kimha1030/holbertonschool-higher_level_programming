#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for e in new_list:
        if e == search:
            new_list[new_list.index(e)] = replace
    return (new_list)
