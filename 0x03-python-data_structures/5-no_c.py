#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for c in my_string:
        if c != "c" and c != "C":
            s += c
    return s
