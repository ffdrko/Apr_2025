school = {
    "student1": {
        "name": 'Fahim',
        'roll': 10,
        "class": "5th standard"
    },
    "student2": {
        "name": 'Rahim',
        'roll': 20,
        "class": "9th standard"
    },

}

print(school['student1']['name'])

for key, val in school.items():
    print("key: {}".format(key))
    for nested_key, nested_val in val.items():
        print("{} : {}".format(nested_key, nested_val))