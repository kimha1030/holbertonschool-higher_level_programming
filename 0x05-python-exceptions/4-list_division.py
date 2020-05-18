#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            n_list.append(res)
    return n_list
