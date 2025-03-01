# Can also be done without using decorators and wrapper function

# defining of function
def start_ui():
        print("1. Before the running TC")
        print("2. Start the Browser")

def end_ui():
        print("3. Ending the running of TC")
        print("4. Closing the Browser")

def test_ui():
    print("I will be testing the UI")

# Calling of function
start_ui()
test_ui()
end_ui()

# if we don't want to create a new function we can use Wrapper and custom decorator