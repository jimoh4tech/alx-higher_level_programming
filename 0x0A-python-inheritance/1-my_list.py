#!/usr/bin/python3
""" Inherit from list class and defines another method. """


class MyList(list):
    """ subclass to list class """
    def __init__self(self):
        """ Initialize object"""
        super().__init__()

    def print_sorted(self):
        """ Prints list in sorted order"""
        print(sorted(self))
