#!/usr/bin/python3
import abc

#  Setting up the Abstract class
class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def sound(self):
        pass

#  Implementing the subclasses
class Dog(Animal):

    def sound(self):
        return "Bark"

class Cat(Animal):

    def sound(self):
        return "Meow"
