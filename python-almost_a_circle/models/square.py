#!/usr/bin/python3
""" square class that inherite from rect class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ child class that inherit fro rect """

    def __init__(self, size, x=0, y=0, id=None):
        """ class square constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overloading  using str """
        return (
                f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}"
        )

