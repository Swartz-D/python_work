# requested_toppings = 'mushrooms'

# if requested_toppings != 'anchovies':
#     print("Hold the anchovies!")

# *************** part 2 ****************** #

# requested_toppings = []

# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# ************** part 3 ****************** #

available_toppings = [
    'mushrooms', 
    'olives', 
    'green peppers', 
    'pepperoni', 
    'pineapple', 
    'extra cheese'
]

requested_toppings = [
    'mushrooms', 
    'french fries', 
    'extra cheese'
]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza")

