"""This program will produce a simple bar chart of the letters
used in any inputted sentence."""

import pprint

print("\n\nWelcome to the poor man's pie chart generator.\n")
pp = pprint.PrettyPrinter(indent=4,width=100)

alphabet = ["a","b","c","d","e","f","g",
            "h","i","j","k","l","m","n",
            "o","p","q","r","s","t","u",
            "v","w","x","y","z"]

while True:
    text = input('\nPlease enter the sentence you would like to analyze,\
or type "quit" to exit.')

    if text == 'quit':
        break

    print("\nText = " + '"' + text + '"\n')

    d = {}

    for key, letter in enumerate(alphabet):
        d[letter] = []
        if letter in text.lower():
            for y, value in enumerate(text):
                if value.lower() == letter:
                    d[letter].append(value)

    pp.pprint(d)

input('\nPress ENTER to quit.')
