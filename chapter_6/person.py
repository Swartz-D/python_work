# 6-1

# person = {
#     'first_name': 'joe',
#     'last_name': 'manarino',
#     'age': 31,
#     'city': 'palm bay',
# }

# print(person.get('first_name'))
# print(person.get('last_name'))
# print(person.get('age'))
# print(person.get('city'))

# 6-2

# favorite_numbers = {
#     'dustin': 17,
#     'joe': 22,
#     'kylor': 13,
#     'david': 10,
#     'ian': 465,
#     'rachel': 12,
# }

# for key, value in favorite_numbers.items():
#     message = f"{key.title()}'s favorite number is {value}."
#     print(message)

# 6-3 / 6-4

glossary = {
    'dictionary': 'collection of key-value pairs',
    'tuple': 'an immutable list',
    'list': 'a collection of values',
    'print()': 'a method to display information to the console',
    '.get()': 'a method to access values in a dictionary',
}

for key, value in glossary.items():
    print(f"{key.title()}: {value}")

# 6-5

rivers = {
    'nile': 'egypt', 
    'mississippi': 'united states', 
    'delaware': 'united states'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers:
    print(river.title())

for country in set(rivers.values()):
    print(country.title())
