# WAP to take 2 number as user input and print whether 1st is greater than or less than or equal to 2nd number

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if num1 > num2:
    print(f"Num1 {num1} is greater than Num2 {num2}")
elif num1< num2:
    print(f"Num1 {num1} is less than Num2 {num2}")
else:
    print(f"Num1 {num1} is equal to Num2 {num2}")

