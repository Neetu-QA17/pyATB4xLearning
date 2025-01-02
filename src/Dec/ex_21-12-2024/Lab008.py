# take a user input a, b and calculate add, sub, mul & div

"""
a= input("Enter the value1: ")
b= input("Enter the value2: ")

print(a+b)
print(a-b)
print(a*b)
print(a/b)

O/P:
Enter the value1: 10
Enter the value2: 5
105

"""
# as input function is considered to be the string data type
# and on addition - concatenation is considered when addition is performed
# instead of 10+5=15 it is giving 105
# to avoid this we need to convert it into the int as below

a= int(input("Enter the value1: "))
b= int(input("Enter the value2: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(type(a))
print(type(b))

"""
O/P1:
Enter the value1: 10
Enter the value2: 5
15
5
50
2.0
--------------------------

O/P2: 
Enter the value1: 20
Enter the value2: 5
25
15
100
4.0
<class 'int'>
<class 'int'>

Process finished with exit code 0
"""