#!/usr/bin/python3
""" first class base """

from models.base import Base


class Rectangle(Base):
    """ child class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
        width: Width of the rectangle.
        height: Height of the rectangle.
        x: X-coordinate of the rectangle's position (default is 0).
        y: Y-coordinate of the rectangle's position (default is 0).
        id:optional identifier.If not provided,a unique id will be assigned.

        constructor of the parent cls(Base)called using super().__init__(id).
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Get the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heigt must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x-coordinate of the rectangle's position """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Set the x-coordinate of the rectangle's position """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y-coordinate of the rectangle's position """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set the y-coordinate of the rectangle's position """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ to define rectangle area """
        return (self.__height * self.__width)

    def display(self):
        """ diplay the rect using # char """
        chong = self.y * "\n"
        for siphan in range(self.height):
            chong += " " * self.x + "#" * self.width + "\n"
        print(chong, end="")

    def __str__(self):
        """ override using str """
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """" update the attribute of recta """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
