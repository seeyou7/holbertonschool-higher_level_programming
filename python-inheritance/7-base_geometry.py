#!/usr/bin/python3
""" creating a class """


class BaseGeometry:
    """ class base geometry """
    def area(self):
        """ pub instance methode that raise an error with msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ pub instance methode to raise err if.."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
