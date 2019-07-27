#!/usr/bin/python env

"""
# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we have done below.
---
menu = []
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage"])
menu.append(["egg", "sausage", "spam"])
menu.append(["bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage", "spam", "spam"])
menu.append(["egg", "spam", "spam"])
menu.append(["sausage", "spam", "spam"])
menu.append(["egg", "bacon"])
menu.append(["sausage", "bacon"])

for meal in menu:
    if "spam" not in meal:
        print("Meal: {}".format(meal))
---
"""

menu = []
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage"])
menu.append(["egg", "sausage", "spam"])
menu.append(["bacon", "sausage", "spam"])
menu.append(["egg", "bacon", "sausage", "spam", "spam"])
menu.append(["egg", "spam", "spam"])
menu.append(["sausage", "spam", "spam"])
menu.append(["egg", "bacon"])
menu.append(["sausage", "bacon"])

for meal in menu:
    if "spam" not in meal:
        print("Meal: {}".format(meal))
        print("Ingredients: ")
        for item in meal:
            print("{}".format(item))
        print("\n")
