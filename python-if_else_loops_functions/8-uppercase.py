#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    print("{}".format(result))
