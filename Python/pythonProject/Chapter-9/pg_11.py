studentList = ['student1', 'student2', 'student3']
student_Info = {
    'student1':
        {"name": "Ace", "roll": "10", "class": "10"},
    'student2':
        {"name": "Ace", "roll": "10", "class": "10"},
    'student3':
        {"name": "Ace", "roll": "10", "class": "10"}
}

school = dict(zip(studentList, student_Info))
print(school)
print(type(school))

emp = dict.fromkeys(['a', 'b', 'c'], 'employee')

print(emp)