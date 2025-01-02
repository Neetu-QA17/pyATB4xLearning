# List
# Collection of items - saved in square brackets [], duplicate is allowed
# excepts only same type of data i.e int - index starts from '0'
# list can contain both heterogenous adn homogenous data
# List can contain dynamic data

my_list = [1,2,3]
print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[10])   # will throw error: "list index out of range"
print("**************************")
for element in my_list:
    print(element)

    # Append the same list
# append object at the end of the list
# using append we can add only single value to the list at the end
my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list)

# extend() is used to add multiple values to the list
# using extend we can add single value to the list also
my_list.extend([7, 8,9])
my_list.extend([10])
my_list.extend(["Singh"])
print(my_list)

# to add an item in the list in between we use insert()
# by providing the index number, value at the same index will be shifted to the right
my_list.insert(10, "Neetu")
print(my_list)

# there is no concept of replace in the list but re-assignment is done
my_list[0] = "Hello"
print(my_list)

# if we add negative index then reverse will be performed like below
my_list.insert(-1, "Lucknow")
print(my_list)

# REMOVE - to remove the element from the list
my_list.remove(5)
print(my_list)

# COPY - create a copy of the same list
my_copy_list = my_list.copy()
print(my_copy_list)
print("----------------------------")

print(my_list)
print(my_copy_list)
my_list.clear()    # will delete the elements from the list
print(my_list)
print(my_copy_list)
print("----------------------------")

# SORTING can also be performed on the list
# sorting is based on the datatype - also only integers and float values can be sorted
my_list2 = [3, 55, 1, 7, 22, 9, 0, 4]
print(my_list2)

my_list2.sort()
print(my_list2)

# REVERSE - we can also reverse the string
my_list2.reverse()
print(my_list2)

# CONCATENATION - can also be done as below
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)