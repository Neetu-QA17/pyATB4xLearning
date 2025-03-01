# Escape Sequence

print("Hello World")
print("Hello\nWorld")   #\n -> new line
print("Hello\tWorld")   #\t -> tab line
print("Hello\bWorld")   #\b -> backspace

# r is used ot avoid the conversion to any escape character like below

dir = "C:\neetu\n.txt"
print(dir)

# O/P:
# C:
# eetu
# .txt

# to avoid this we have to use "r" which considered to be the raw string form

dir = r"C:\neetu\n.txt"
print(dir)

