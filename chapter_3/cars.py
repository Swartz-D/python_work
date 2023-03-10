cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

print(sorted(cars))
print(cars)

newcars = sorted(cars)
print('newcars', newcars)
print('cars', cars)

cars.reverse()
print('reverse', cars)

print(len(cars))