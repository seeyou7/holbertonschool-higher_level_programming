#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
        Returns the JSON representation of the provided object.

        Args:
        - my_obj: The object to be serialized to JSON.

        Returns:
        - A JSON-formatted string representing the object.
    """
    return json.dumps(my_obj)
