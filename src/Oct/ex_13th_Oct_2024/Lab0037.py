# WAP to find the Max number between 2 numbers

# Logic building:

#1. user input = 2 integers
#2. O/P: which ever is greater - it will return
#3. input method

num1 = int(input("Enter the num1\n"))

num2 = int(input("Enter the num2\n"))

if num1>num2:
    print("Max num is:", num1)
else:
    print(f"Max num is: {num2}")    # string formatting can also be used instead of commas
                                    # as shown in above print statement
