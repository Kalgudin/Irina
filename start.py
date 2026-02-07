students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [70, 65, 80]},
    {"name": "Diana", "grades": [100, 95, 98]}
]

def find_top_student(students):
    best_average = 0
    top_student = None

    for student in students:
        grades = student['grades']
        average = sum(grades) / len(grades)
        if average > best_average:
            best_average = average
            top_student = student['name']
    return top_student

result = find_top_student(students)
print(result)

