def summary(data):
    for student in data:
        name = student['name']
        scores = student['scores']
        total = sum(scores)
        average = round(total / len(scores), 1)
        print(f"{name} 的總分是 {total}，平均是 {average}")

students = [
    {'name': 'Alice', 'scores': [90, 80, 70]},
    {'name': 'Bob', 'scores': [100, 85, 95]}
]

summary(students)
