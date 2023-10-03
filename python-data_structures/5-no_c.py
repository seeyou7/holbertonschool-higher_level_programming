#!/usr/bin/python3
def no_c(my_string):
    rm_char = "cC"
    modify_str = ''.join([char for char in my_string if char not in rm_char])
    return modify_str
