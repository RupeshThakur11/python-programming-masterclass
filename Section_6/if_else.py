#!/usr/bin/env python
name = input("Enter your name: ")
age = int(input("Enter your age {0}: ".format(name)))

if (age > 17) and (age < 31):
    print("Welcome to the holiday, {0}".format(name))
else:
    print("Sorry {0}, you need to be over 17 and under 31 to be able to go on this holiday".format(name))
