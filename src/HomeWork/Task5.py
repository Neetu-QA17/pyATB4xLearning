# Triangle Classifier


# equilateral triangle(all sides equal), isosceles triangle(2 sides are equal), scalene triangle(all sides are unequal)

a - float(input("Enter side a: "))
b - float(input("Enter side b: "))
c - float(input("Enter side c: "))

if a == b == c:
    print("Equilateral Triangle")
elif a==b or b==c or a==c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")