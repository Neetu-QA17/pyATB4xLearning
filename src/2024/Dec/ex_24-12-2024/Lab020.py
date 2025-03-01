# For Loop

#SYNTAX:
# for i in range(1, 10, 1):
# print(i)

for i in range(1, 20, 2):
#    print(i) # will be printed in new line as by default end of line is new line
    print(i, end=' ') #ninstead of space we can use comma(,), slash(/), hyphen(-)

# Range(start, stop-1, step)

for i in range(1, 11):
    print("Hello -> ", i)