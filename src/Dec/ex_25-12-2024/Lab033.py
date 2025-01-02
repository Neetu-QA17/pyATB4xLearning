# Calling 1 function into another

def greet_to_all():
    print("Hi All")

def reply():
    print("Yes, Please")
    greet_to_all()    # calling

reply()   #calling