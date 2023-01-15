#!/usr/bin/python3
""" Defines the base class """
import json
import csv
import turtle


class Base:
    """ Base class for all object.

    Attributes:
        __nb_objects (int): number of instatiated classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize  new base

        Args:
            id (int): Identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file

        Args:
           list_objs (list): list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None or list_objs == []:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

        Args:
            json_string (str): JSON str rep of list of dicts
        Return:
            empty list if json_string is None or empty
            else, JSON string rep
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set
        Args:
            **dictionary (dict): key/value pair attribute
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances

        Return:
             list of instances if file exist,
             else empty list
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes files in CSV
        Args:
            list_objs (list): list of objects from base instance
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes files in CSV
        Return:
            empty list of file does not exist,
            else list of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dic.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): list of rectangle objs to be drwan
            list_squares (list): list of sqaure objs to be drawn
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#AAAAAA")
        tur.pensize(3)
        tur.shape("turtle")
        tur.color("FFFFFFF")

        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()

            for i in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#BBBBBB")
        for sq in list_squares:
            tur.showturtle()
            tur.up()
            tur.up()
            tur.goto(sq.x, sq.y)
            tur.down()

            for i in range(2):
                tur.forward(sq.size)
                tur.left(90)
                tur.forward(sq.size)
                tur.left(90)
            tur.hideturtle()
        turtle.exitoncick()
