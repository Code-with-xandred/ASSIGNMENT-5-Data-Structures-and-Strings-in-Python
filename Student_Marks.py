# Task 1: Create a Dictionary of Student Marks

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")