#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list = []
    for x in my_list:
        if x % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
