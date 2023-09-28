#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter (ASCII values between 97 and 122)
        if 97 <= ord(char) <= 122:
            # Convert the lowercase letter to uppercase using ASCII manipulation
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end="")
        else:
            # If the character is not a lowercase letter, print it as is
            print(char, end="")
    # Print a newline character after processing the entire string
    print()

