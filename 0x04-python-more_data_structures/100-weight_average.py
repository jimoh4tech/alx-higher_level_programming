#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    av = 0
    size = 0
    for t in my_list:
        av += (t[0] * t[1])
        size += t[1]
    return (av / size)
