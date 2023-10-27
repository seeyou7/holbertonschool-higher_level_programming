#!/usr/bin/python3
""" first class base """


import json


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static methoode that return representation of list dict """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write list_ objs in filename using json """
        if list_objs is None:
            list_objs = []
        list_dict = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            """ create and convert list_dict to list of dictionaries """
            for i in list_objs:
                list_dict.append(i.to_dictionary())
            file.write(Base.to_json_string(list_dict))
