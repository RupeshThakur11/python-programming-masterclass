#!/usr/bin/env python3
""" list comprehension example """

numbers = [1, 2, 3, 4, 5, 6]

# squares = []
# for number in numbers:
#     squares.append(number ** 2)
# or
# squares = [number ** 2 for number in numbers]
squares = [number ** 2 for number in range(1, 7)]

print(squares)
