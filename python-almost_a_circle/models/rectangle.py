#!/usr/bin/python3
""" first class base """


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


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
        """ diplay the rect using # """
        chong = self.y * "\n"
        for siphan in range(self.height):
            chong += (" " * self.x)
            chong += ("#" * self.width) + "\n"
        print(chong, end="")

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -  {self.width}/{self.height}"
