# Strings
name="Neetu"

# also referred as str

print(type(name))
print(name.upper())
print(name.lower())
print(len(name)) # length always start from index: 1

a="90"
age=90
print(type(a))  # as 'a' is defined in double quotes
print(type(age))

name = "This is a big sentence"
print(type(name))
# name = name +1 # not possible  - string cannot be added to integer
# either add the number '1' in double quotes like: "1"
# or you can convert the number to string as: str(1)

name= name + str(1)
print(name)
print(type(name))


first_name = "Neetu"
last_name = "Singh"

full_name = first_name + last_name
print(full_name)


how_many_have_enrolled_in_JAVA_batch = None
print(type(how_many_have_enrolled_in_JAVA_batch))  # NoneType

# no concept of null in python

# id
age= 10
age2= 10
age3= 11
print(id(age)) # print the memory location where it is stored i.e. 4395918184
print(id(age2)) # allocation is same
print(id(age3)) # memory location is changed as new value is assigned i.e. 4332610440

