# current_users = ['dj8080', 'larryb', 'admin', 'player5', 'guest']
# # current_users = []
# new_users = ['miles88', 'Player5', 'charles', 'larryb', 'guest2']

# if current_users:
#     for user in new_users:
#         if user.lower() in current_users:
#             print("Choose a new username")
#         else:
#             print(f"{user} is available")
# else:
#     print("We need to find some users!")

# *********** numbers ************* #

numbers = list(range(1, 10))

for number in numbers:
    number = str(number)
    if number == '1':
        print(number + 'st')
    elif number == '2':
        print(number + 'nd')
    elif number == '3':
        print(number + 'rd')
    else:
        print(number + 'th')