# Exceptions
# try, except and finally
# file

import os
try:
    full_path = os.getcwd()  # cwd = current working directory
    print(full_path)
    full_path_file = full_path+"/example.txt"
    file = open(full_path_file, 'r')
    print(file.read())  # if file doesn't exist the error: n below"
# FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'" is displayed

except FileNotFoundError as fnfe:
    print("File Not Found Error exception, fix the path or create the file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)



