#!/usr/bin/env python3

"""
We have mentioned that the data for the Adventure game could be organised in many
different ways.  We've created another way for you.
Your mission, if you choose to accept it, is to
change the code to make it work.
Below is the the complete program from the last video, but with the
locations dictionary modified so that everything is in a single dictionary.
Yes the code has some errors, that's what you need to fix!

locations = {0: {"desc": "At Home",
                 "exits": {},
                 "namedExits": {}
                 },
             1: {"desc": "On the Road",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}
                 },
             2: {"desc": "On the Hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}
                 },
             3: {"desc": "In the Building",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}
                 },
             4: {"desc": "In the Valley",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}
                 },
             5: {"desc": "In the Forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}
                 },
             }

voca = {"QUIT": "Q",
        "NORTH": "N",
        "SOUTH": "S",
        "EAST": "E",
        "WEST": "W",
        "ROAD": 1,
        "HILL": 2,
        "BUILDING": 3,
        "VALLEY": 4,
        "FOREST": 5
        }

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    # Parse user input to use vocabulary dictionary if needed
    if len(direction) > 1:
        words = direction.split()
        for i in words:
            if i in voca:
                direction = voca[i]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go that way")
"""

locations = {0: {"desc": "At Home",
                 "exits": {},
                 "namedExits": {}
                 },
             1: {"desc": "On the Road",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}
                 },
             2: {"desc": "On the Hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}
                 },
             3: {"desc": "In the Building",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}
                 },
             4: {"desc": "In the Valley",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}
                 },
             5: {"desc": "In the Forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}
                 },
             }

vocab = {"QUIT": "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W",
         "ROAD": 1,
         "HILL": 2,
         "BUILDING": 3,
         "VALLEY": 4,
         "FOREST": 5
         }

loc = 1
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])
        # print(allExits)

    direction = input("Available exits are " + availableExits + " ").upper()
    # print()

    # Parse user input to use vocabulary dictionary if needed
    if len(direction) > 1:
        words = direction.split()
        for i in words:
            if i in vocab:
                direction = vocab[i]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go that way")
