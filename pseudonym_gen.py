"""Program to select a random game of thrones name."""

import random

print("Welcome to the Game of Thrones name generator.'\n")

first = ('Addam', 'Aegon', 'Aemon', 'Alan', 'Allyria',
         'Arthur', 'Baelor', 'Bedwyck', 'Boremund', 'Bryan',
         'Clement', 'Daario', 'Edmund', 'Franklyn', 'Garth',
         'Gwayne', 'Harmon', 'Harry', 'Janos', 'Jeyne')

last = ('Stark','Greyjoy','Lannister','Mormont',
        'Karstark', 'Martell', 'Targaryan', 'Bolton',
        'Baratheon', 'Tully', 'Arryn', 'Blackfyre',
        'Tyrell')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName,lastName))
    print("\n\n")

    try_again = input("\n\nTry again? (Press enter, or press n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress enter to exit.\n")
