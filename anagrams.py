# Load digital dictionary file as a list of words
import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

while True:
    user_input = input('\n\nEnter a word or type "quit" to end the program.\n')
    if user_input == 'quit':
        break
    
    print("Input name = {}".format(user_input))
    user_input = user_input.lower()
    print("Using name = {}".format(user_input))

    anagrams = []

    word_sorted = sorted(user_input)

    for word in set(word_list):
        word = word.lower()
        if word != user_input:
            if sorted(word) == word_sorted:
                anagrams.append(word)

    print()
    if len(anagrams) == 0:
        print("You need a larger dictionary or a new word!")
    else:
        print("Anagrams =", *anagrams, sep='\n')