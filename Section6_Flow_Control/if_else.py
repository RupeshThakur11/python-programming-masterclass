#!/usr/bin/env python

"""
Write a small program to ask for a name and an age.
When both values have been entered, check if the person
is the right age to go on an 18-30 holiday (they must be
over 18 and under 31).
If they are, welcome them to the holiday, otherwise print
a (polite) message refusing them entry.
"""

name = input("Enter your name: ")
age = int(input("Enter your age {0}: ".format(name)))

if (age > 17) and (age < 31):
    print("Welcome to the holiday, {0}".format(name))
else:
    print("Sorry {0}, you need to be over 17 and under 31 to be able to go on this holiday".format(name))
