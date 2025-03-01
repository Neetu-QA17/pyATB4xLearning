# Lambda Expression

# A lambda is an anonymous function that returns some form of data

def add_10(n):
    return n + 10

o = add_10(100)
print(o)
# OR
o = lambda n: n + 10
print(o(100))

def mul(a,b):
    return a * b

oo = mul(3, 4)
print(oo)

# OR

oo = lambda a,b: a*b
print(oo(3,4))