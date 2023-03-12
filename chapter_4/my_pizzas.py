pizzas = ['supreme', 'meat lovers' ,'chicken-bacon-ranch']
friend_pizzas = pizzas[:]

pizzas.append('pepporoni')
friend_pizzas.append('sausage')

for pizza in pizzas:
    print(f"My favorite pizzas are {pizza}.")

for pizza in friend_pizzas:
    print(f"My friends favorite pizzas are {pizza}.")
