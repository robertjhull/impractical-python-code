"""This is a program for translating words into pig latin."""

print("Welcome to the pig latin translator.\n")

def consonant(word):
    """Translates words that begin with consonants."""
    pig_latin = word[1:] + word[0] + "ay"
    return pig_latin

def vowel(word):
    """Translates words that begin with vowels."""
    pig_latin = word + "way"
    return pig_latin

vowels = ("a", "e", "i", "o", "u")

while True:
    new_word = input(
        "\n\nEnter a word to be translated, or type 'quit' to exit.\n"
        )

    if new_word == 'quit':
        break
    if new_word[0].lower() in vowels:
        translation = vowel(new_word)
    else:
        translation = consonant(new_word)

    print("\n\n")
    print(translation)
    print("\n\n")
