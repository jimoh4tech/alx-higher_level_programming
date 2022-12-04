#!/usr/bin/python3
def element_at(my_list, idx):
    """Return the element at a given index"""
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
