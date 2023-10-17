#!/usr/bin/python3
""" class list """


class MyList(list):
    """  class MyList that inherits fro list """
    def print_sorted(self):
        print(sorted(self))
