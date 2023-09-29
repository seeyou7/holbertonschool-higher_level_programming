#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argv_n = len(argv)
    if argv_n == 1:
        print("0 argements.")
    elif argv_n == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{argv_n -1} arguments:")
        for i in range(1, argv_n):
            print(f"{i}: {argv[i]}")
