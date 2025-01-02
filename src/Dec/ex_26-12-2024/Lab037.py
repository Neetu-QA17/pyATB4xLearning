# create a program to sum 3 numbers from user input


num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

def sum_of_3_numbers(n1, n2, n3):
    return n1+n2+n3

result = sum_of_3_numbers(num1,num2,num3)
print(result)
# or can also be written as
result = sum_of_3_numbers(n1=num1, n2=num2, n3=num3)
print(result)