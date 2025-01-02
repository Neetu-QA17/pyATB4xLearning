# FizzBuzz

# For numbers that are divisible by both 3 and 5 , print Fizz Buzz
# if divisible by 3 then print "Fizz"
# if divisible by 5 then print "Buzz"
# if other than 3 and 5 then print the number

for i in range(1, 101, 1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("FIZZ")
    elif i%5 == 0:
        print("BUZZ")
    else:
        print(i)