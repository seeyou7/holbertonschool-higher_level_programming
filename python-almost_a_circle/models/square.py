#!/usr/bin/python3
""" square class that inherite from rect class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ child class that inherit fro rect """

    def __init__(self, size, x=0, y=0, id=None):
        """ class square constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size of square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ overloading  using str """
        return (
                f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}"
        )

    def update(self, *args, **kwargs):
        """ update square by initiation arg to atribute """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dict for square """
        return {
                "id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
