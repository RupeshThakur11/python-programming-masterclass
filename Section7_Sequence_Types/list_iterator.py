#!/usr/bin/env python3

"""
Create a list of items (you may use either strings or numbers in the list),
then create an iterator using the iter() function.

Use a for loop to loop "n" times, where n is the number of items in your list.
Each time round the loop, use next() on your list to print the next item.

hint: use the len() function rather than counting the number of items in the list.
"""

my_list = ['blah', 'hello', 1, 2, 3, 'cat', 123]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    item = next(my_iterator)
    print(item)
