#!/usr/bin/env python3

"""
Add 2 numbers and handle exceptions
"""
import sys


def getnum(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:  # if you enter anything other than a number
            print("Wrong input for division, please try again")
        except EOFError:  # if you hit ^D on input
            sys.exit(1)
        finally:
            print("Finally clause is executed")


def divide(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:  # dividing by zero
        print("You are dividing by 0. It is not allowed")
        sys.exit(2)


num1 = getnum("Enter 1st number: ")
num2 = getnum("Enter 2nd number: ")

divide(num1, num2)
