meat = {
    'kind': 'dog',
    'owner': 'megan',
}

jake = {
    'kind': 'dog',
    'owner': 'dustin',
}

kit = {
    'kind': 'fox',
    'owner': 'joe',
}

pets = [meat, jake, kit]

for pet in pets:
    print(pet)

# 6-9
favorite_places = {
    'dustin': ['spain', 'germany', 'turkey'],
    'megan': ['florida', 'home', 'bath'],
    'andrea': ['asleep', 'eating', 'france'],
}

for name, places in favorite_places.items():
    print(name.title())
    for place in places:
        print(f"\t{place.title()}")

