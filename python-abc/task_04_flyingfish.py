#!/usr/bin/python3

class Fish:
    """
    A class representing a fish. Fish can swim and live in water.
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    A class representing a bird. Birds can fly and live in the sky.
    """
    def fly(self):
        print('The bird is flying')

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish. Flying fish can swim, fly, and live both in water and the sky.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
