# Tuples - Collection of items
# defined in normal braces ()
# no assignment or change of values is allowed in tuples
# no append is performed in tuples
my_tuple = (1,4,9,4,25,36)
print(my_tuple)
# my_tuple[3] = 64  # 'tuple' object does not support item assignment - immutable in nature

# conversion from tuple to list n vice-versa is possible
# less memory utilization
# it contains only fixed data

my_api_list = list(my_tuple)    # conversion
print(my_api_list)

my_api_list = tuple(my_api_list)
print(my_api_list)