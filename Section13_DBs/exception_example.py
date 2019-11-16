#!/usr/bin/env python3

"""
Exception handling example
"""


def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(9000))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")

print("Program terminating")
