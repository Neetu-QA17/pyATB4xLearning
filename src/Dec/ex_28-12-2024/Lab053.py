# Convert below into Lambda expression

# def sum_three_numbers(a,b,c)
#     return a+b+c

res = lambda a,b,c: a+b+c
print(res(1,2,3))

def find_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# OR
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))