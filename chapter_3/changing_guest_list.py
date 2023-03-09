guest_list = ['allen rickman', 'chris evans', 'martha stewart', 'snoop dog']
print(f"Unfortunately, {guest_list[2].title()} will be unable to attend due to being in prison")

del guest_list[2]
guest_list.insert(2, 'David Beckhem')
print(f"Hey {guest_list[0]}! Come get some food.")
print(f"Hey {guest_list[1]}! Come get some food.")
print(f"Hey {guest_list[2]}! Come get some food.")
print(f"Hey {guest_list[3]}! Come get some food.")