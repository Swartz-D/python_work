people = {
    'dustin': {
        'age': 31,
        'sex': 'male',
        'city': 'palm bay',
    },
    'megan': {
        'age': 35,
        'sex': 'female',
        'city': 'springboro',
    },
    'sarah': {
        'age': 38,
        'sex': 'female',
        'city': 'centerville',
    },
    'andrea': {
        'age': 42,
        'sex': 'female',
        'city': 'tipp city',
    },
}

for person, person_info in people.items():
    print(f"\nName: {person.title()}")
    age = person_info['age']
    sex = person_info['sex']
    city = person_info['city']
    print(f"\t{age}\n\t{sex.title()}\n\t{city.title()}")
