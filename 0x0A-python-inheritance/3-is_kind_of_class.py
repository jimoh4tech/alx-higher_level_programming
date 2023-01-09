#!/usr/bin/python3
""" Checks if object isinstance """


def is_kind_of_class(obj, a_class):
    """ Checks wheather obj is instance or inheritance of a class

    Args:
        obj (any): object to check
        a_class (type): class to match type with.
    Returns:
        True if obj is an instance or inheritance, else False
    """
    if isinstance(obj, a_class):
        return True
    return False
