# Grade Calculator
# WAP that calculates & display the letter grade as per the numerical score
#  A: 90 - 100
#  B: 80 - 89
#  C: 70 - 79
#  D: 60 - 69
#  F: 0 - 59

grade = float(input("Enter the grade\n"))

if grade>=90 and grade<=100:         # or 90 <= grade <= 100 -> known as simplified chaining format
    print(f"Grade: A, {grade}")
elif grade>=80 and grade<=89:
    print(f"Grade: B, {grade}")
elif grade>=70 and grade<=79:
    print(f"Grade: C, {grade}")
elif grade>=60 and grade<=69:
    print(f"Grade: D, {grade}")
elif grade>100:
    print("Impossible")
else:
    print(f"Grade: F, {grade}")
