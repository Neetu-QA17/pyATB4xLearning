# Exceptions

print("--- Start of the program ---")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c = a / b  # if a=10, b=0 - zero division error and if a=neetu = then Value error exception is thrown
    print("Result Div is ", c)

except Exception as e:
    print(e)
    print("Please check your input, it should not be String or zero")

print("--- End of the program ---")
