places_to_visit = ['istanbul', 'puerto rico', 'germany', 'italy', 'brazil']

print('original', places_to_visit)

print('sorted', sorted(places_to_visit))

print('should match original', places_to_visit)

print('sorted reverse', sorted(places_to_visit, reverse=True))

print('should match original', places_to_visit)

places_to_visit.reverse()
print('reversed', places_to_visit)

places_to_visit.sort()
print('alphabetical', places_to_visit)

places_to_visit.sort(reverse=True)
print('reversed alphabetical', places_to_visit)

