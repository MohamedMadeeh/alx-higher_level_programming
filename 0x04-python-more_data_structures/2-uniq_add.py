#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    for element in set(my_list):
        n += element
    return n
