# car = input()
# print(f"current car is {car}")

# if car.lower() == "toyota":
#     print("you gueseed corred")

# topping = input().lower()
# toppings = ['mushroom', 'sausage', 'bacon', 'olives']
# print(f"my toppings: {toppings}")

# if topping in toppings:
#     print(f"yes we have {topping}")
# else: 
#     print(f"we will have to add {topping} to our toppings")

age = int(input())

def canVote(age):
    if age >= 18:
        print("You are old enough to vote")
    else:
        print("You are too young to vote")

canVote(age)

