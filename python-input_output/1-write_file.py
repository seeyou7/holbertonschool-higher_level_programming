#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout:"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(text)
    num_char_writen = len(text)
    return num_char_writen
