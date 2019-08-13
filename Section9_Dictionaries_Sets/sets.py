#!/usr/bin/env python3

"""
Create a program that takes some text and returns a list of
all the characters in the text that are not vowels, sorted in
alphabetical order.

You can either enter the text from the keyboard or
initialise a string variable with the string.
"""

# input a string
stringSet = set(input("Enter a string"))

# set of vowels
# vowelSet = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
vowelSet = frozenset("aeiouAEIOU")

# difference
print(sorted(stringSet.difference(vowelSet)))
