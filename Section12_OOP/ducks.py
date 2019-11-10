#!/usr/bin/env python3

"""
Polymorphism example
Inheritance - "is a" relation
Composition - "has a" relation
"""


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("This is hard, but I am flying")
        else:
            print("Think I'll just walk")


class Ducks(object):

    def __init__(self):  # when a class contains another object like this, it's called composition
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's great")

    def quack(self):
        print("Quack quack!")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too!")

    def swim(self):
        print("Come on in, the water's a bit chilly")

    def quack(self):
        print("Are you 'avin a larf? I'm a penguin!!")


def test_duck(duck):  # polymorphic behavior
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    donald = Ducks()
    # test_duck(donald)
    donald.fly()

    percy = Penguin()
    # test_duck(percy)
