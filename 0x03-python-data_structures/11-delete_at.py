#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if (idx < 0):
        return my_list
    elif (idx >= length):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                del my_list[idx]
        return my_list
