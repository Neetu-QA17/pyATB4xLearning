# WAP to calc the area of a circle
# take the value of radius as a user input
import math

radius = float(input("Enter the value for radius\n"))

Area = math.pi * math.pow(radius, 2)
print(Area)
print(f"Area of a circle is -> {Area: .2f}")