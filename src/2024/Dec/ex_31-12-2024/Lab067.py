# Take a user input and create a class in Python

class Person:

    def __init__(self):
        self.name = input("Enter the name:\n")
        self.age = int(input("Enter the age:\n"))
        self.phn_num = int(input("Enter the Phone number:\n"))
        self.address = input("Enter the address:\n")

    def name_of_function_to_display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone number is {self.phn_num}")
        print(f"Address is {self.address}")

# Create an object of the class
person1 = Person()

# Call the display function
person1.name_of_function_to_display()
