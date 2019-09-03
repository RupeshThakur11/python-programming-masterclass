#!/usr/bin/env python3

"""
Modify the program from the Second Dictionary challenge of lecture 56
to use shelves instead of dictionaries.

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

Do this by creating two programs. cave_initialise.py should create the two
shelves (locations and vocabulary) with the appropriate keys and values.

cave_game.py will then use the two shelves instead of dictionaries.
Apart from opening and closing the shelves, cave_game will need only
two changes to the actual code - remember that shelf keys MUST be strings!

Just to be clear, cave_game.py will contain the code from line 45, everything
before that (modified to use shelves) will be in cave_initialise.py.
"""

import shelve

locations = shelve.open('locations')

locations['0'] = {"desc": "At Home",
                  "exits": {},
                  "namedExits": {}
                  }
locations['1'] = {"desc": "On the Road",
                  "exits": {"W": '2', "E": '3', "N": '5', "S": '4', "Q": '0'},
                  "namedExits": {"2": '2', "3": '3', "5": '5', "4": '4'}
                  }
locations['2'] = {"desc": "On the Hill",
                  "exits": {"N": '5', "Q": '0'},
                  "namedExits": {"5": '5'}
                  }
locations['3'] = {"desc": "In the Building",
                  "exits": {"W": '1', "Q": '0'},
                  "namedExits": {"1": '1'}
                  }
locations['4'] = {"desc": "In the Valley",
                  "exits": {"N": '1', "W": '2', "Q": '0'},
                  "namedExits": {"1": '1', "2": '2'}
                  }
locations['5'] = {"desc": "In the Forest",
                  "exits": {"W": '2', "S": '1', "Q": '0'},
                  "namedExits": {"2": '2', "1": '1'}
                  }

vocab = shelve.open('vocab')

vocab['QUIT'] = "Q"
vocab['NORTH'] = "N"
vocab['SOUTH'] = "S"
vocab['EAST'] = "E"
vocab['WEST'] = "W"
vocab['ROAD'] = 1
vocab['HILL'] = 2
vocab['BUILDING'] = 3
vocab['VALLEY'] = 4
vocab['FOREST'] = 5

vocab.close()
locations.close()
