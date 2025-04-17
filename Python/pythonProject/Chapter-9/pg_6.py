employee = {
    "id": 101,
    "name": "Fahim",
    "age": 25,
    "dept": "Senior dev",
    "salary": 10000
}

employee.update({"name": "Fahim Faisal Deepto"})

print(employee)

employee.pop('age')
print(employee)

employee.popitem()
print(employee)

employee.clear()

del employee