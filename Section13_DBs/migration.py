#!/usr/bin/env python3

import ducks

flock = ducks.Flock()
duck1 = ducks.Ducks()
duck2 = ducks.Ducks()
duck3 = ducks.Ducks()
duck4 = ducks.Ducks()
duck5 = ducks.Ducks()
duck6 = ducks.Ducks()
duck7 = ducks.Ducks()
penguin = ducks.Penguin()

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(penguin)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
