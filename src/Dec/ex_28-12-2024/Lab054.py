import math


def give_me_pow(num):
    return math.pow(num, 2)
op = give_me_pow(10)
print(op)

# OR

op2 = lambda num: math.pow(num, 2)
print(op2(10))

# OR
op2 = lambda : math.pow(int(input("Enter the num:\n")), 2)
print(op2())