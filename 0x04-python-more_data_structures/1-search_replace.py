def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    else:
        new_list = my_list.copy()
        for n, e in new_list:
            if e == search:
                new_list[n] = replace
        return (new_list)
