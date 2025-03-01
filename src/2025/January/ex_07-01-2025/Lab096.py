import os
from os import listdir

# OS- files, path related to the OS

print(os.name)   # posix - unix based - system mac or linux

print(os.getcwd())  # /Users/neetusingh/PycharmProjects/pyATB4xLearning/src/2025/January/ex_07-01-2025 - gives the current working directory

print(os.listdir())
for file in listdir():
    print(file)   # will print all the files on the current directory

# to create a new directory
#os.makedirs('new_directory')

# to remove a directory
#os.rmdir('new_directory')

# the most important we are going to use is below
# to find the file in a folder
full_path = os.path.join('folder', 'file.txt')
print(full_path)

# to check whether file exist or not
print(os.path.exists('file.txt')) # this returns either true or false - False

# to check whether it is a file or not
print(os.path.isfile('file.txt'))     # False

# to check whether the  directory is available or not
print(os.path.isdir("directory_name"))