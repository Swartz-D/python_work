motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'duke')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['yamaha', 'ducati', 'duke', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print('start', motorcycles)
