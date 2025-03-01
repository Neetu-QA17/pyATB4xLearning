with open("Test_Data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="-")