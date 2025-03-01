# Constructor - to set the values automatically - to initialize the values of attributes
# sole purpose of constructor is to assign the values to the variables defined in the class
# special function in a class, __init__()
# it is automatically created when we create an object
# 2 types - 1. default - with no arguments, 2. Parameterized - with arguments
# Constructor does not return anything


class Dog:
    name = None

    def __init__(self, name, age):
        print("Called, Object is created")
        self.name = name
        self.age = age

    def sleep(self):
        print("Who is Sleeping ->" + self.name, self.age)

dog1 = Dog("Chow", 12)
print(dog1.name)
dog1.sleep()

dog2 = Dog("Mow", 2)
print(dog2.name)
dog2.sleep()