# OOPs Concept

# Class - Blueprint
# Object - Instance of a class
# Encapsulation - public, private __ and protected _
# Inheritance - single, multiple, nulti-level, hierarchial, hybrid
# Poly - method overriding and method overloading
# Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name


    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")  # method must be completed only then the object is created


dog = Dog("PP")
dog.sound()