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
            """ create and convert list_dict to list of dict """
            for i in list_objs:
                list_dict.append(i.to_dictionary())
            file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        else:
            obj = cls(3)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        instances = []

    try:
        with open(filename, "r") as file:
            json_str = file.read()
        data = cls.from_json_string(json_str)
        for item in data:
            instance = cls.create(**item)
            instances.append(instance)
    except FileNotFoundError:
        pass

        return instances
