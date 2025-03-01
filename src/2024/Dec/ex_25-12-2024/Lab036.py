# User Define function and Types
# 1. no return type
# 2. No return type functions with arguments
# 3. have parameter
# 4. have no parameters


# 1. no return type
# no return type - no parameter/argument

def greet():
    print("Hello World")

result = greet()
print(result)


# 2. No return type functions with arguments
def greet_by_name(name):
    print("Hello,", name)

res = greet_by_name("Neetu")
print(res)

# 3. No return type with default argument
def say_hello_to_default_argument(name="Neetu"):
    print("Hello,", name.upper())

say_hello_to_default_argument("Singh")
say_hello_to_default_argument()    # default value defined at line 29 is called
say_hello_to_default_argument(name = "Shubhra")    # also known as positional argument

def multiple_arguments(first_name="Shubhra", second_name="Asthana", location="Hardoi", phn_number=567):
    print("Multiple_arguments,", first_name, second_name, location, phn_number)

multiple_arguments(first_name="Neetu", second_name="Singh", location="Lucknow", phn_number=123)
multiple_arguments()

# 4. argument and return type
def sum_of_2_numbers(num1, num2):
    return num1+num2

result = sum_of_2_numbers(10, 34)
print(result)