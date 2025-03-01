# If File is present in different directory

import os

full_path_file = os.path.join("/Users/neetusingh/PycharmProjects/pyATB4xLearning/src/2025/January/ex_08-01-2025/neetu","neetu.txt")

file = open(full_path_file, 'r')
content = file.read()
print(content)
