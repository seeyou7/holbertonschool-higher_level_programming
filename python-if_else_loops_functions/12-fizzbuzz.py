#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz".format(i), end=" ")
        elif i % 3 == 0:
            print(f"Fizz".format(i), end=" ")
        elif i % 5 == 0:
            print(f"Buzz".format(i), end=" ")
        else:
            print("{:d}".format(i), end=" ")
