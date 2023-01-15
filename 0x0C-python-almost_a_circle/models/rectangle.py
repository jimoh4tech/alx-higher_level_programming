#!/usr/bin/python3
""" Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiaize new Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle
            x (int): x-coordinates of the rectangle
            y (int): y-coordinate of the rectangle
        Raises:
            TypeError: If either width or height is not int
            ValueError: If either width or height <= 0
            TypeError: If either x or y is not int
            ValueError: If either x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter for the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter for the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter for the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter for the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """ Prints # characters representation of a rectangle """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Returns the print() and str() representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def to_dictionary(self):
        """ Returns dictionary representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Update rectangle

        Args:
           *args (int[]): attribute values.
                - 1st arg represents attribute id
                - 2nd arg represents attribute width
                - 3rd arg represents attribute height
                - 4th arg represents attribute x
                - 5th arg represents attribute y
            **kwargs (dic): key/value pair attributes
        """
        if args and len(args) > 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif c == 1:
                    self.width = arg
                elif c == 2:
                    self.height = arg
                elif c == 3:
                    self.x = arg
                elif c == 4:
                    self.y = arg
                c += 1

        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
