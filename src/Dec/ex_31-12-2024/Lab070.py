class Person:

    # Class Variable
    # Instance Variable
    #name = "Amit"  # if we define the value in the class then is common across all the variable - hard coded value
    # to avoid the hard coded value we need to use constructor

    def __init__(self, name):    # constructor are used to change the value for the instance variable
        self.name = name

    def walk(self, name):
        self.name = name
        print(self.name)

#amit = Person()
#pramod = Person()
#print(amit)
#print(pramod) # same value is printed as value defined in the class was hard coded so same output was printed

amit = Person("Amit")
pramod = Person("Pramod")
print(amit.name)
print(pramod.name)