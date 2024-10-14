# take the user input a, b and calculate sum, multiplication, div & sub
# Calculator program

# num1 = input("Enter 1st number: ")
# num2 = input("Enter 2nd number: ")


# concatenation is happening - bcoz num1 & num2 are treated as string
# to perform sum, mul, div & sub - we need to convert string to integer
# we can everything to int only by passing int as below:
# num1 = int(input("Enter 1st number: "))

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


print("Sum is: ", num1+num2)
print("Mul is: ", num1*num2)
print("Div is: ", num1/num2)
print("Sub is: ", num1-num2)


# div is always decimal - python is very smart - it knows there is very high chance value to be in decimal