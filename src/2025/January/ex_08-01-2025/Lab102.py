# Always try to open the file using try catch
try:
     with open("Test_Data.txt", "r") as file:
         content = file.readlines()
         print(content)

except FileNotFoundError as fnfe:
    print(fnfe)

finally:
    try:
        file.close()

    except NameError as ne:
        print("NE")