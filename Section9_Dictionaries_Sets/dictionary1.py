#!/usr/bin/env python3

"""
Modify the program so that the exits is a dictionary rather than a list,
with the keys being the numbers of the locations and the values being
dictionaries holding the exits (as they do at present). No change should
be needed to the actual code.

Once that is working, create another dictionary that contains words that
players may use. These words will be the keys, and their values will be
a single letter that the program can use to determine which way to go.

locations = {0: "At Home",
             1: "On the Road",
             2: "On the Hill",
             3: "In the Building",
             4: "In the Valley",
             5: "In the Forest"
             }

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}
         ]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go that way")
"""

locations = {0: "At Home",
             1: "On the Road",
             2: "On the Hill",
             3: "In the Building",
             4: "In the Valley",
             5: "In the Forest"
             }

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}
         }

vocab = {"QUIT": "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W"
         }

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    # Parse user input to use vocabulary dictionary if needed
    if len(direction) > 1:  # if more than one letter
        # for i in vocab:
        #     if i in direction:
        #         direction = vocab[i]
        words = direction.split()
        for i in words:
            if i in vocab:
                direction = vocab[i]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go that way")

