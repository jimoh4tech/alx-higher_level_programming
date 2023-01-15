#!/usr/bin/python3
""" Define square class that inherits from the rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represent a square class that inherits directly from the
        Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initiaize new squar
        Args:
            size (int): size of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns the string rep of square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.height)

    def to_dictionary(self):
        """ Returns dictionary representation of square"""
        return {
            "id": self.id,
            "size": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Update square attributes

        Args:
            *args (int[]): attribute values.
                - 1st rep attribute id
                - 2nd arg rep attribute size
                - 3rd arg rep attribute x
                - 4th arg rep attribute y
             **kwargs (dict): key/value pairs attributes
        """
        if args and len(args) > 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif c == 1:
                    self.size = arg
                elif c == 2:
                    self.x = arg
                elif c == 3:
                    self.y = arg
                c += 1
        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
