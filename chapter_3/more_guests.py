guest_list = ['allen rickman', 'chris evans', 'martha stewart', 'snoop dog']
print(f"Hey {guest_list[0].title()}, I was able to find us a bigger table.")
print(f"Hey {guest_list[1].title()}, I was able to find us a bigger table.")
print(f"Hey {guest_list[2].title()}, I was able to find us a bigger table.")
print(f"Hey {guest_list[3].title()}, I was able to find us a bigger table.")

guest_list.insert(0, 'megan mullaly')
guest_list.insert(2, 'jennifer coolidge')
guest_list.append('dolley parton')
print(f"{guest_list[0]}, here's your new invitation.")
print(f"{guest_list[1]}, here's your new invitation.")
print(f"{guest_list[2]}, here's your new invitation.")
print(f"{guest_list[3]}, here's your new invitation.")
print(f"{guest_list[4]}, here's your new invitation.")
print(f"{guest_list[5]}, here's your new invitation.")
print(f"{guest_list[6]}, here's your new invitation.")
print(guest_list)