#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """base geometry"""
    def area(self):
        """ area define"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area define """
        return self.__width * self.__height

    def __str__(self):
        """ dunder __str__ define """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ square class that inherite fro rect class """
    def __init__(self, size):
        """ initial the methode size """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area square def """
        return self.__size ** 2

    def __str__(self):
        """ dunder __str__ define """
        return ("[Square] {}/{}".format(self.__size, self.__size))
