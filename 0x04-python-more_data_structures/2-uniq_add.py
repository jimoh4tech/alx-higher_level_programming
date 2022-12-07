#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    for x in set(my_list):
        total += x
    return total
