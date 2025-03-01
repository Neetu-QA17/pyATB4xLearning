# Formatting of numbers i.e. if you want 4 or 5 digits after decimal

number = 31.14159265359

formatted_num1 = f"{number:.4f}"
formatted_num2 = f"{number:.5f}"
formatted_num3 = f"{number:.6f}"

print(formatted_num1)
print(formatted_num2)
print(formatted_num3)

# formatting is used to view the final output user want to view as below

table = 2
print(f"{table}*1 = {table*1}")
print(f"{table}*2 = {table*2}")
print(f"{table}*3 = {table*3}")
print(f"{table}*4 = {table*4}")
print(f"{table}*5 = {table*5}")