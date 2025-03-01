def print_arguments(*args):
    print(args[0])
# *args = multiple argument with no limit - > list

print_arguments("neetu", "shubhra", "lucky")
print_arguments("shubhra", "lucky")
print_arguments("neetu", 10)
print_arguments("neetu", 10, True)
print_arguments("neetu", 10, True, False)
print_arguments("Neetu")
# print_arguments() - minimum 1 argument is required

