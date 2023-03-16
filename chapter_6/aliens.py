# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)

# make first 3 aliens green and worth 10 points
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yello'
        alien['points'] = 10
        alien['speed'] = 'medium'

# show first 5 aliens

for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# 

