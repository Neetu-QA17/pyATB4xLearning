a, b, c = 10,11,12
print(a)
print(b)
print(c)

# Search in Tuple
cities = ("London", "France", "Paris", "Singapore", "Tokyo", "Los Angeles")
print("Paris" in cities)
print("New Delhi" in cities)

t = (12, 24, 36)
# t.append(12)     'tuple' object has no attribute 'append'
# to perform append - 1st convert to list - then append - then again convert to tuple
my_list = list(t)
my_list.append(4)
print(my_list)
my_list = tuple(my_list)
print(my_list)

# OR can also be done as below

t = (12, 24, 36)
my_tuple = t + (84,)
print(my_tuple)