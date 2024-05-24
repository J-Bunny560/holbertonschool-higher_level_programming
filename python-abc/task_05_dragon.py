#!/usr/bin/python3
# Creating Mixins

class SwimMixin:
    def swim(self):
        print("The creature swims!")



class FlyMixin:
    def fly(self):
        print("The creature flies!")



# Implementing Dragon

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
