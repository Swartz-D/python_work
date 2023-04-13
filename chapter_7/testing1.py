# builds a pizza for user
# crusts = ['thin', 'stuffed', 'classic']
# sauces = ['classic marinara', 'white sauce']
# meats = ['saussage', 'bacon', 'ham', 'chicken', 'beef', 'pepperoni']
# veggies = ['banana peppers', 'green peppers', 'mushrooms', 'olives']

# prompt1 = f"Hello, my name is chatBot. I am here to take your order.\nWhat type of crust would you like?\n{crusts}"
# prompt2 = f"Which sauce would you like?\n{sauces}\n"
# prompt3 = f"Which meats would you like?\n{meats}\n"
# prompt4 = f"Which veggies would you like?\n{veggies}\n"
# active = True
# while active:
#     print(prompt1)
#     my_crust = input()
#     print(my_crust, 'my crust')
#     print(prompt2)
#     my_sauce = input()
#     print(prompt3)
#     my_meats = input().split()
#     print(prompt4)
#     my_veggies = input().split()

#     my_pizza = {
#         'crust': my_crust,
#         'sauce': my_sauce,
#         'meats': my_meats,
#         'veggies': my_veggies,
#     }
#     print(f"Here is your pizza\n{my_pizza}")
#     active = False

# movie tickets
under3 = 0
between3and12 = 10
over12 = 15
ticket = 0
total = 0
active = True

while active:
    age = input("input age or 'quit' to get total\n")
    if age.lower() == 'quit':
        print(f"your total comes to ${total}")
        active = False
    else:
        try:
            age = int(age)
            ticket = (
                under3 if age < 3
                else over12 if age > 12
                else between3and12
            )
            total += ticket
        except ValueError:
            print("""
                Invalid input. 
                Please enter a valid age or 'quit' to continue.
                """
                  )
