# Class - blueprint
class Person:
    # Attributes
    id=None
    name=None
    age=None
    email=None
    height=None
    gender=None
    phn_no=None
    Address=None

    # Behaviour
    def talk(self):
        print("Ican talk")

    def sleep(self, name):  # argument with no return type
        print("I am a method!")
        print("Sleep", name)

    def sleep2(self, name):  # argument with return type
        print("I am a method!")
        return None

    def walk(self):
        print("I am walking")

    def walk2(self, ):   # argument with return type
         return "I am walking"

# Create Object of the Class
# ObjectRef=ClassName() - Object


shubhra = Person()
shubhra.name = "Shubhra"
print(shubhra.name)

nitya = Person()
nitya.name = "Neetu"
print(nitya.name)

