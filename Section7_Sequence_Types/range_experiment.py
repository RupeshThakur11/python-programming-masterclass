#!/usr/bin/python env

"""
Experiment with different ranges and slices to get a feel for how they work.
Remember that you can print the range as well as iterating through it to print
its values, to check that your ranges are what you expected.
You may also want to include things like.
---
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in o:
    print(i)
print('=' * 50)
for i in p:
    print(i)
---
and see if you can work out what will be printed before running the program. If you are unsure, use a
for loop to print out the values of o to see why p returns what it does.
"""

print('=' * 50)
string = 'egaugnal lufrewop yrev a si nohtyP'
print(string[::-1])

print('=' * 50)

r = range(0, 20)
for i in r[::-3]:
    print(i)

print('=' * 50)

for i in range(50, 0, -2):
    print(i)

print('=' * 50)

print(range(0, 100)[::-2] == range(99, 0, -2))
