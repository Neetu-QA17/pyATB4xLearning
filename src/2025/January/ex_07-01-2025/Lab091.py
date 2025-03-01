# EXCEPTIONS - Any event which disrupts the normal flow of a program when an error occurs.
# Exception can occur from various situations, suc as invalid operations or unexpected condition

# Error and exceptions in Python are both mechanism that indicate problems in a program

# Error generally occurs when there is a mistake in a code such as syntax error or logical error

#Exceptions are the issues that occur during the execution of a program
# - trying to divide by 0, or accessing an invalid index in a list
# - eg: TypeError occurs when an operation is performed on incompatible data types

# print(x)  # NameError: name 'x' is not defined

# print(10/0)  # ZeroDivisionError: division by zero

# print(1 + "1")      # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(int('a') )  # ValueError: invalid literal for int() with base 10: 'a'

# my_list = [1, 2, 3]
# print(my_list[5])     # IndexError: list index out of range

# while True print("Hello World")  # SyntaxError: invalid syntax

#        print("Hello World")   # IndentationError: unexpected indent