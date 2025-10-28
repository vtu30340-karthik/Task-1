def bubble_sort_scores(students):
    n = len(students)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if students[j]['score'] > students[j + 1]['score']:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True
        if not swapped:
            break

# Example usage
students = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 95},
    {'name': 'Charlie', 'score': 75},
    {'name': 'Diana', 'score': 85}
]

print("Before sorting:")
for student in students:
    print(student)

bubble_sort_scores(students)

print("\nAfter sorting:")
for student in students:
    print(student)
