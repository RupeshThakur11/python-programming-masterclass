#!/usr/bin/env python3

""" example to show nested comprehension """

burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print()

# outer comprehension is iterated over first
for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)
