#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """ Defines a rectangle class."""

    def __init__(self, width=0, height=0):
        """ Initialize new Rectangle

        Args:
             width (int): with of new rectamgle.
             height (int): height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for variable width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for variable width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for variable height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
