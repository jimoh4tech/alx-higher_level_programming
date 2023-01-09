#!/usr/bin/python3
""" Is Instance of a class"""


def is_same_class(obj, a_class):
    """ Checks of object is instance of a class

    Args:
         obj (any): The object to check.
         a_class (type): The class to match the type obj
    Return:
         True if obj is an instance else False
    """
    if type(obj) == a_class:
        return True
    return False
