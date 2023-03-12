cities = ['dayton', 'columbus', 'toledo', 'cleveland', 'cincinatti']

cities.append('greenville')
print(cities)

cities.insert(1, 'gallopolis')
print(cities)

del cities[2]
print(cities)

cities.pop()
print(cities)

cities.remove('dayton')
print(cities)

cities.sort()
print(cities)

print(sorted(cities, key=len, reverse=True))

cities.reverse()
print(cities)

print(len(cities))
