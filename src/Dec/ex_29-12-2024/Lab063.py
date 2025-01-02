# Dictionary
# Key Value pair
# can contain  multiple key: value pair
# no effect on dictionary if it has the duplicate key value pair elements
# It is an unordered collection

student_information= {
    "First_Name": "Neetu",
    "Second_Name": "Singh",
    "Age": 30,
    "Age": 29,  # same key but different value in key value pair then latest key value pair is printed
    "Location": "Gurgaon",
    "Phn_Number": "97944"
}
print(student_information)
print(student_information["First_Name"])
print(student_information["Age"])
print(student_information["Location"])