#!/usr/bin/python3
""" import module """

import json


def load_from_json_file(filename):
    """
        func that create an obj from JSON file.

        Args:
        - filename: The name of the file to write to.

        Returns:
        - None
    """
    with open(filename, 'r') as file:
        to_load = json.load(file)
        return to_load

