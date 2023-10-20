#!/usr/bin/python3
""" import module """


import json


def from_json_string(my_str):
    """
        Converts a JSON-formatted string into a Python object.

        Args:
        - my_str: The JSON-formatted string.

        Returns:
        - A Python object representing the JSON data.
    """
    return json.loads(my_str)
