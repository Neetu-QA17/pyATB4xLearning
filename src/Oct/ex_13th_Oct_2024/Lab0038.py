# WAP to find max between 3 numbers

# Logic building:
# user input - num1, num2, num3
# O/P: int or String with max num

# Logic? If else -1condition
# more tan 1 condition -> if elif else

# Syntax

#if condition_1:
#    print("do 1")
#elif condition_2:
#    print("do 2")
#else:
#    print("do 3")

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

if num1>num2 and num1>num2:
    print(f"Max num is: {num1}")
elif num2>num1 and num2>num3:
    print(f"Max num is: {num2}")
else:
    print(f"Max num is: {num3}")

# Can also be done as below:

result = max(num1, num2, num3)
print(result)