person = {
    'name': 'John',
    'second_name': 'Doe',
    'height': [182, 123],
    'eyes': 'blue',
    'weight': [75, 12, 23]
}

for personal_property in person:
    print(personal_property)

print(person.keys())
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

print(person.items())
for key, value in person.items():
    if isinstance(value, list):
        for q in value:
            print(q)
        if len(value) == 2:
            x, y = value
            print(key, x, y)
        elif len(value) == 3:
            x, y, z = value
            print(key, x, y, z)
    else:
        print(key, value)
