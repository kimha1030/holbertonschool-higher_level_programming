#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    mod_tuple_a = tuple_a[0] + tuple_b[0]
    mod_tuple_b = tuple_a[1] + tuple_b[1]
    new_tuple = (mod_tuple_a, mod_tuple_b)
    return (new_tuple)
