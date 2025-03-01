# POLYMORPHISM
# Objects -> Many forms
# behaviour - based on who is calling
# Polymorphism allows object of different class to be treated as objects of a common superclass
# 2 types - Method Overloading - not supported in python and Method Overriding

# Method Overriding
class Shape:
    def area(self):
        return "Printing area of the shape"

class Rectangle(Shape):  # IS -A i.e. single inheritance is done

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    #def area(self):
        #return 3.14 * self.radius * self.radius

shape1 = Rectangle(3, 4)
print(shape1.area())   # local function is called

shape2 = Circle(10)  # if a class does not have a function and class inherits the parent class then
print(shape2.area()) # function defined in parent class is called

