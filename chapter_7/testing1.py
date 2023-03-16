# builds a pizza for user
crusts = ['thin', 'stuffed', 'classic']
sauces = ['classic marinara', 'white sauce']
meats = ['saussage', 'bacon', 'ham', 'chicken', 'beef', 'pepperoni']
veggies = ['banana peppers', 'green peppers', 'mushrooms', 'olives']

prompt1 = f"Hello, my name is chatBot. I am here to take your order.\nWhat type of crust would you like?\n{crusts}"
prompt2 = f"Which sauce would you like?\n{sauces}\n"
prompt3 = f"Which meats would you like?\n{meats}\n"
prompt4 = f"Which veggies would you like?\n{veggies}\n"
x = ['plates']
active = True
while active:
    print(x)
    print(prompt1)
    my_crust = input()
    print(my_crust, 'my crust')
    print(prompt2)
    my_sauce = input()
    print(prompt3)
    my_meats = input().split()
    print(prompt4)
    my_veggies = input().split()
    
    my_pizza = {
        'crust': my_crust,
        'sauce': my_sauce,
        'meats': my_meats,
        'veggies': my_veggies,
    }
    print(f"Here is your pizza\n{my_pizza}")
    active = False


