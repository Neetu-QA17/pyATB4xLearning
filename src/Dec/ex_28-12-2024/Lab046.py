# Understanding decorators in python

def add_extra_security(func):
# two part
# wrapper and call
    def wrapper():
        print("1. Before the function is called")
        print("2. Add Helmet, Dashcash, Gloves, Knee Guards")
        # drive_bike()
        func()
        print("3. After the function is called")
        print("4. Secure Driving")

    return wrapper()

# definition
#@my_decorator
# def drive_bike()
# print("I am driving")

@add_extra_security
def drive_scooty():
    print("Normal Function")


# Benefits of usage of Decorators
# 1. Code Reusability
# 2. Separation of concerns
# 3. Enhanced Readability