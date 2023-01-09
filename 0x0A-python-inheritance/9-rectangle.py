#!/bin/usr/python3
""" Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """ Initialize new Rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculate and return rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """ Return print() and str() rep of a rectangle"""
        string = "[{}] {}/{}".format(str(self.__class__.__name__),
                                     str(self.__width), str(self.__height))
        return string
