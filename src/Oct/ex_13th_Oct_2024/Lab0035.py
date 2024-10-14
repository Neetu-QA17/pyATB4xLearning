# Conditions & Loops
# WAP to take user age & let him know that he can go to club

#Logic building
# user input - data type - int
# O/P - String - user can go to club

# Rough logic:
# if age> 21 -> print - can go
# if age< 21 -> print - can't go

# write logic

age = input("Enter your age\n")
age = int(age)

if age >= 21:
    print(f"Can go to club -> {age}")
else:
    print(f"Can't go to club -> {age}")