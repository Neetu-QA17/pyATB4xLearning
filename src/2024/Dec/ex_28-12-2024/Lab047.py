# Understanding decorators in python

def add_before_and_after_ui(custom_function_where_we_want_extra_functionality):
# two part
# wrapper and call
    def wrapper():
        print("1. Before the running TC")
        print("2. Start the Browser")
        custom_function_where_we_want_extra_functionality()
        print("3. Ending the running of TC")
        print("4. Closing the Browser")

    return wrapper()

# definition
#@my_decorator
# def drive_bike()
# print("I am driving")

@add_before_and_after_ui
def test_ui():
    print("I will be testing the UI")


# Benefits of usage of Decorators
# 1. Code Reusability
# 2. Separation of concerns
# 3. Enhanced Readability