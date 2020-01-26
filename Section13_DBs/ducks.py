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

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too!")

    def swim(self):
        print("Come on in, the water's a bit chilly")

    def quack(self):
        print("Are you 'avin a larf? I'm a penguin!!")

    def aviate(self):
        print("I won a lottery and bought a learjet!")


class Flock(object):

    def __init__(self):
        self.flock = []

    # params can be annotated, using a Type hint
    def add_duck(self, duck: Ducks) -> None:
        fly_method = getattr(duck, 'fly', None)
        # if isinstance(duck, Duck):
        if callable(fly_method):  # checking if method is callable, we are not interested in type
            self.flock.append(duck)
        else:
            raise TypeError("Can't add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down")
                problem = e

        if problem:
            raise problem


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
