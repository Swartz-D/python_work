guest_list = ['megan mullaly', 'allen rickman', 'jennifer coolidge', 'chris evans', 'martha stewart', 'snoop dog', 'dolley parton']
print(f"I apologize, but I will only be able to bring two people to dinner.")

print(f"Sorry {guest_list.pop()}, you are the weakest link. Goodbey.")
print(f"Sorry {guest_list.pop()}, you are the weakest link. Goodbey.")
print(f"Sorry {guest_list.pop()}, you are the weakest link. Goodbey.")
print(f"Sorry {guest_list.pop()}, you are the weakest link. Goodbey.")
print(f"Sorry {guest_list.pop()}, you are the weakest link. Goodbey.")

print(f"{guest_list[0].title()}, you are still invited.")
print(f"{guest_list[1].title()}, you are still invited.")

del guest_list[0]
del guest_list[0]

print("should be []", guest_list)