#!/usr/bin/python3
""" import module """


import json


def save_to_json_file(my_obj, filename):
    """
        Writes a Python object to a text file using its JSON representation.

        Args:
        - obj: The Python object to be serialized and written to the file.
        - filename: The name of the file to write to.

        Returns:
        - None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
