#!/usr/bin/python3
"""
  that returns True if the object is an instance of
  or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """ check the same class of an obj """
    if isinstance(obj, a_class):
        return True
