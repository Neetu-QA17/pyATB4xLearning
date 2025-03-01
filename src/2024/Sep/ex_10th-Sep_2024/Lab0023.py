# if you want the value to the 2 or 3 or 4 decimal points - formatting is used
print(3/2)   # 1.5000

number = 3.14159265359
formatted_number = f"{number:.3f}"
print(formatted_number)

formatted_number2 = f"{number:.5f}"
print(formatted_number2)


# Format of string
num = 90
print(f"{num}")
print("This is the number you are working with "f"{num}") # its just the replacement of the value

# if you want to print the table of 9

number = 9
print(f"{number} * 1 = {number}")
print(f"{number} * 2 = {number*2}")
print(f"{number} * 3 = {number*3}")
print(f"{number} * 4 = {number*4}")
print(f"{number} * 5 = {number*5}")
print(f"{number} * 6 = {number*6}")


# we don't have increment/decrement operator in python
