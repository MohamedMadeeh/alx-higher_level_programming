#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            k_del.append(key)
    for key in k_del:
        del a_dictionary[key]
    return a_dictionary
