# union is also performed
set1 = {1,2,3}
set2 = {4,5,6}
my_set = set1.union(set2)
print(my_set)

# intersection is also performed
set3 = {2, 3, 4,5}
set4 = {1, 2, 3, 4}
my_set2 = set3.intersection(set4)
print(my_set2)

# difference
my_set3 = set3.difference(set4)
print(my_set3)
my_set3 = set4.difference(set3)
print(my_set3)

# SUBSET
set1 = {1,2,3,4,5}
set2 = {2,3,8}
subset = set2.issubset(set1)
print(subset)