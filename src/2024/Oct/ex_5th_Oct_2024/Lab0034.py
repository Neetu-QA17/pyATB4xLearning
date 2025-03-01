# WAP to calculate the  area of a circle
# given its radius using the formula
# area = 3.14 x r^2
import math

# Logic building formula
# Step1 Figure out the Input & Output
# input -> r -> data type -> float
# pi -> 3.14
# power  - > pow or ** -> any

# O/P: float - area , print area

# Step2
# rough logic = area = 3.14 * pow(r,2)


# Step3 Write the logic

radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = 3.14 * math.pow(radius,2)
print("Area of the circle is:", area)
print(f"Area of the circle is: , {area:.2f}")