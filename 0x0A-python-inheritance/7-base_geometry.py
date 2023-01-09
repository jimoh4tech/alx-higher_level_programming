#!/usr/bin/python3
""" Empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """ Defines area for the base class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Valides the value
        Args:
            name (str): name of parameter
            value (int): parameter to validate
        Raises:
            TypeError: if value is not integer
            ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
