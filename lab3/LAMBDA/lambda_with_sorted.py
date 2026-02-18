# Using lambda with sorted()

students = [("Ali", 85), ("Aruzhan", 92), ("Dias", 78)]

sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted by score:", sorted_students)
