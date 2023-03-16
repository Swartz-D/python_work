# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']

# # for name, language in favorite_languages.items():
# #     print(f"Hi {name.title()}")

# #     if name in friends:
# #         language = favorite_languages[name].title()
# #         print(f"\t{name.title()} I see you love {language.title()}.")

# # Looping through dictionary in particular order

# for name in sorted(favorite_languages):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in sorted(set(favorite_languages.values())):
#     print(language.title())

# # 6-6

# take_poll = ['april', 'shelby', 'sarah', 'dustin', 'alex']

# for name in favorite_languages:
#     if name in take_poll:
#         print(f"Thank you {name.title()} for taking the poll.")
#     else:
#         print(f"{name.title()}, can you please take the poll?")

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")