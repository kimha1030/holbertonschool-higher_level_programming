#!/usr/bin/python3

def lookup(obj):
    """Function that return the available attributes"""
    list_o = []
    list_o = dir(obj)
    return list_o
