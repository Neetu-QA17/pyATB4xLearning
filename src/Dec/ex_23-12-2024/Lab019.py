# find the max num out of 3 numbers - 3 numbers must be user input - with int datatype

num1 = int(input("Enter the 1st num: "))
num2 = int(input("Enter the 2nd num: "))
num3 = int(input("Enter the 3rd num: "))

if num1>num2 and num1>num3:
    print(f"Num1: {num1} is Greater")
elif num2>num1 and num2>num3:
    print(f"Num2: {num2} is Greater")
else:
    print(f"Num3: {num3} is Greater")

result = max(num1, num2, num3)
print(result)