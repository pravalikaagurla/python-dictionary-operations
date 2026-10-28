# Task 4: Student Information Dictionary

# Creating a dictionary
student = {
    "Name": "Pravalika",
    "Age": 21,
    "course": "B.Tech CSE",
    "City": "Hyderabad"
}

# Displaying original dictionary
print("Student Information:", student)

# Accessing values
print("\nName:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["course"])
print("City:", student["City"])

# Adding a new key-value pair
student["College"] = "JBREC"
print("\nAfter Adding College:", student)

# Updating a value
student["City"] = "Jagtial"
print("\nAfter Updating City:", student)

# Removing data
student.pop("Age")
print("\nAfter Removing Age:", student)

# Displaying keys
print("\nDictionary Keys:")
for key in student.keys():
    print(key)

# Displaying values
print("\nDictionary Values:")
for value in student.values():
    print(value)

# Dictionary methods
print("\nNumber of Items:", len(student))
print("Course using get():", student.get("course"))
print("Is Name present?", "Name" in student)