#!/usr/bin/python3
""" creating a class """


class BaseGeometry:
    """ class base geometry """
    def area(self):
        """ pub instance methode that raise an error with msg"""
        raise Exception("area() is not implemented")
