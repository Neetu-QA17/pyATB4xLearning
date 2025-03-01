# Exceptions

# try, except and Finally
# Exceptions

print("--- Start of the program ---")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    result = a / b  # if a=10, b=0 - zero division error and if a=neetu = then Value error exception is thrown

except ValueError as ve:
    print(ve)
    print("Value Error exception, You have entered the string and it should be integer")

except ZeroDivisionError as zde:
    print(zde)
    print("Zero Division Error, Dont use num2 as '0'")

else:
    print(f"Result is {result}")

finally:
    print("This code will be always executed")

print("--- End of the program ---")
