#!/usr/bin/python3
def weight_average(my_list=[]):
    elem_mul = []
    weight = []
    for elem in my_list:
        mult = elem[0] * elem[1]
        weight.append(elem[1])
        elem_mul.append(mult)
    sum_num = sum(elem_mul)
    sum_we = sum(weight)
    media = sum_num/sum_we
    return media
