#!/usr/bin/env python3

"""
Modify the program below to use a while loop to
allow as many guesses as necessary.

The program should let the player know whether to
guess higher or lower, and should print a message
when the guess is correct. A correct guess will
terminate the program.

As an optional extra, allow the player to quit by entering
0 (zero) for their guess.
---
import random

highest = 10
answer = random.randint(1, highest)

print("Guess a number in 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Guess a higher number")
    else:
        print("Guess a lower number")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have not guessed correctly")
else:
    print("You got it the first time")
---
"""

import random

highest = 10
answer = random.randint(1, highest)

print("Guess a number in 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess < 1 or guess > 10:
        print("You quit!")
        break
    elif guess < answer:
        print("Guess a higher number")
    else:
        print("Guess a lower number")
    guess = int(input())
else:
    print("That's correct!!!")
