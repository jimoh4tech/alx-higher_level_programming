#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list = my_list[:]
    for i in range(len(list)):
        if list[i] == search:
            list[i] = replace
    return list
