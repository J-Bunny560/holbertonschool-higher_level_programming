#!/usr/bin/env python3
""" Task 00 ABC """

from abc import ABC, abstractmethod

class Animal(ABC):
    """ ABC Animal """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """ ABC Dog """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """ ABC Cat """
    def sound(self):
        return "Meow"
