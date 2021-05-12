# Load digital dictionary file as a list of words

import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

while True:
    # Accept a word from user
    word = input('\n\nEnter a word or type "quit" to end the program.\n')
    if word == 'quit':
        break
    
    print("Input name = {}".format(word))
    word = word.lower()
    print("Using name = {}".format(word))

    # Create an empty list to hold anagrams
    anagrams = []

    # Sort the user-word
    word_sorted = sorted(word)

    # Loop through each word in the word list:
    for w in set(word_list):
        w = w.lower()
        if w != word:
            if sorted(w) == word_sorted:
                anagrams.append(w)

    print()
    if len(anagrams) == 0:
        print("You need a larger dictionary or a new word!")
    else:
        print("Anagrams =", *anagrams, sep='\n')