# Function Scope

global_b =12

def my_function():
     a = 10
     print(a)
     print(global_b)

my_function()
print(global_b)
